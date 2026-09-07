---
title: (Service Business / Agency) — 03. Tutup Periode Bulanan
category: accounting-service-agency
description: Skenario pengujian 03. tutup periode bulanan dengan ciri khas Service Business / Agency.
visibility: internal
---

# 03. Tutup Periode Bulanan

> **Ciri Khas Skenario**: Fokus pada pengakuan pendapatan bertahap (amortisasi retainer), tagihan recurring, dan pelacakan profitabilitas per divisi (Marketing vs Dev).
> Format pengujian mengikuti standar: **Positif** (jalur normal harus sukses) / **Negatif** (input salah harus ditolak) / **Netralisasi** (rollback).
> Endpoint periode: **Accounting Period**. Endpoint tahun fiskal: **Fiscal Year**.

## 1. Close Accounting Period (`PUT client-master/accounting-period/close`)

| Skenario                               | Detail                                                                                                                                                                        | Hasil                                                                                                                                                                                                                                     |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                | `PUT client-master/accounting-period/close {id:<periode Agustus 2026>}` — pastikan semua jurnal bertanggal Agustus sudah `post`, dan periode September sudah ada & masih open | 200, `is_closed:true`                                                                                                                                                                                                                     |
| Negatif — ada jurnal unposted          | Sisakan 1 jurnal draft/belum-post bertanggal di dalam periode ini                                                                                                             | 422, pesan `content.accounting_period_has_unposted_journals_post_or_void_them_first` (BUKAN teks generik "Unposted journals exist")                                                                                                       |
| Negatif — periode sudah closed         | Close periode yang sama 2x                                                                                                                                                    | 422, `content.accounting_period_already_closed`                                                                                                                                                                                           |
| Negatif — periode berikutnya belum ada | Close periode terakhir yang sudah dibuat padahal masih di tengah tahun fiskal (bukan periode terakhir FY)                                                                     | 422, `content.cannot_close_period_the_next_period_has_not_been_created_yet` — guard ini SKIP kalau periode yang di-close memang periode terakhir tahun fiskal (biar year-end close tidak terhalang periode tahun depan yang belum dibuat) |

## 2. Lock Period (`PUT client-master/accounting-period/lock`)

| Skenario               | Detail                                   | Hasil                                                                   |
| ---------------------- | ---------------------------------------- | ----------------------------------------------------------------------- |
| Positif                | Lock periode yang sudah `is_closed:true` | 200, `is_locked:true`                                                   |
| Negatif — belum closed | Lock periode yang masih open             | 422, `content.accounting_period_must_be_closed_before_it_can_be_locked` |

## 3. Reopen Period (`PUT client-master/accounting-period/reopen`)

| Skenario                     | Detail                                                                                                                 | Hasil                                                                                                                               |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Positif                      | `PUT client-master/accounting-period/reopen {id, reason:"koreksi jurnal Agustus"}` pada periode closed dan/atau locked | 200, `is_closed:false` DAN `is_locked:false` sekaligus (reopen selalu membuka keduanya bersamaan, walau cuma salah satu yang aktif) |
| Negatif — periode masih open | Reopen periode yang belum pernah di-close                                                                              | 422, `content.accounting_period_is_not_closed_or_locked`                                                                            |

## 4. Close Fiscal Year (`POST client-master/fiscal-year/close-year`)

> Endpoint ini ada di controller **Fiscal Year**, BUKAN di `accounting-period` — beda modul dari close/lock/reopen periode bulanan di atas.

| Skenario                            | Detail                                                                                                       | Hasil                                                                                                                                      |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif                             | Semua 12 periode bulanan FY2026 sudah closed, lalu `POST client-master/fiscal-year/close-year {id:<FY2026>}` | Net Income tahun berjalan (Pendapatan − Beban dari Trial Balance) di-posting ke Laba Ditahan (EKT-02, `is_retained_earnings_account:true`) |
| Negatif — masih ada periode terbuka | Close fiscal year padahal ada periode bulanan yang belum closed                                              | Ditolak — verifikasi pesan aktual di response (belum diverifikasi di suite ini, cek behavior riil saat testing)                            |

## Netralisasi

- Reopen periode kalau perlu koreksi (§3), atau reverse jurnal yang salah SEBELUM periode di-close (reverse setelah closed akan diblok oleh guard posting periode closed/locked).
