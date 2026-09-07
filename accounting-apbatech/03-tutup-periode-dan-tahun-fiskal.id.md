---
title: (IT Consultant + Retail Elektronik) — 03. Tutup Periode Bulanan & Tahun Fiskal
category: accounting-apbatech
description: Close/lock/reopen Accounting Period dan Close Fiscal Year — 1 kali saja untuk PT APBATECH (1 branch), mencakup ketiga Business Unit sekaligus.
visibility: internal
---

# 03. Tutup Periode Bulanan & Tahun Fiskal

> Format pengujian: **Positif** / **Negatif** / **Netralisasi**. Endpoint periode: **Accounting Period** (`client-master/accounting-period/*`). Endpoint tahun fiskal: **Fiscal Year** (`client-master/fiscal-year/*`).
>
> Accounting Period & Fiscal Year adalah master data **branch-scoped**, TAPI karena PT APBATECH cuma 1 branch, cukup **1 set periode/fiscal year** yang menaungi ketiga Business Unit sekaligus (dibuat di file 00 §5). Close periode Agustus otomatis menutup SEMUA transaksi bulan itu, apapun `business_unit_id`-nya — tidak ada lagi close terpisah per divisi/toko.

## 1. Close Accounting Period Agustus 2026

| Skenario                               | Detail                                                                                                                                                                  | Hasil                                                                                                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                | `PUT client-master/accounting-period/close {id:<periode Agustus 2026>}` — pastikan semua jurnal §1.1–1.5 file 01 sudah `post` (ketiga BU), periode September masih open | 200, `is_closed:true`                                                                                                                   |
| Negatif — ada jurnal unposted          | Sisakan 1 jurnal draft bertanggal Agustus (belum di-post), apapun `business_unit_id`-nya                                                                                | 422, `content.accounting_period_has_unposted_journals_post_or_void_them_first`                                                          |
| Negatif — periode sudah closed         | Close periode yang sama 2x                                                                                                                                              | 422, `content.accounting_period_already_closed`                                                                                         |
| Negatif — periode berikutnya belum ada | Close periode terakhir yang dibuat padahal bukan periode terakhir FY                                                                                                    | 422, `content.cannot_close_period_the_next_period_has_not_been_created_yet` — skip guard ini kalau memang periode terakhir tahun fiskal |

## 2. Lock & Reopen Period

| Skenario               | Detail                                                                                                           | Hasil                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Positif — Lock         | `PUT client-master/accounting-period/lock` pada periode yang sudah closed                                        | 200, `is_locked:true`                                                                |
| Negatif — belum closed | Lock periode yang masih open                                                                                     | 422, `content.accounting_period_must_be_closed_before_it_can_be_locked`              |
| Positif — Reopen       | `PUT client-master/accounting-period/reopen {id, reason:"koreksi jurnal milestone proyek Solusi Niaga Digital"}` | 200, `is_closed:false` DAN `is_locked:false` sekaligus (reopen selalu buka keduanya) |
| Negatif — masih open   | Reopen periode yang belum pernah di-close                                                                        | 422, `content.accounting_period_is_not_closed_or_locked`                             |

## 3. Close Fiscal Year

> Endpoint di controller **Fiscal Year**, BUKAN `accounting-period`.

| Skenario                            | Detail                                                                                     | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                             | Semua 12 periode FY2026 closed → `POST client-master/fiscal-year/close-year {id:<FY2026>}` | Net Income tahun berjalan (gabungan ketiga BU, karena hanya 1 COA/GL) di-posting ke Laba Ditahan (EKT-02). **Tidak ada lagi "jurnal penutup per branch"** — 1 kali close-year sudah final untuk seluruh perusahaan; breakdown net income per BU untuk keperluan analisis tetap harus dihitung manual dari `general-ledger/summary-by-account` (file 02 §2) SEBELUM close-year, karena setelah closed saldo P&L per akun sudah di-zero-kan ke Laba Ditahan |
| Negatif — masih ada periode terbuka | Close fiscal year padahal ada periode bulanan yang belum closed                            | Ditolak — verifikasi pesan aktual saat testing riil                                                                                                                                                                                                                                                                                                                                                                                                       |

## Netralisasi

- Reopen periode kalau perlu koreksi (§2), atau reverse jurnal SEBELUM periode di-close (reverse setelah closed akan diblok guard posting periode closed/locked).

## Referensi Silang

- [`02-general-ledger-trial-balance-per-branch.id.md`](./02-general-ledger-trial-balance-per-branch.id.md)
- [`04-laporan-keuangan-konsolidasi-dan-per-branch.id.md`](./04-laporan-keuangan-konsolidasi-dan-per-branch.id.md)
