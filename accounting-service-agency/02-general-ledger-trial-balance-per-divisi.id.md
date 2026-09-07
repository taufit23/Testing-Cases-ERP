---
title: (Service Business / Agency) — 02. GL & Trial Balance per Divisi
category: accounting-service-agency
description: Skenario pengujian 02. gl & trial balance per divisi dengan ciri khas Service Business / Agency.
visibility: internal
---

# 02. GL & Trial Balance per Divisi

> **Ciri Khas Skenario**: Fokus pada pengakuan pendapatan bertahap (amortisasi retainer), tagihan recurring, dan pelacakan profitabilitas per divisi (Marketing vs Dev).
> Format pengujian mengikuti standar: **Positif** (jalur normal harus sukses) / **Negatif** (input salah harus ditolak) / **Netralisasi** (rollback).
> Prasyarat: jurnal-jurnal di file 01 sudah di-`post` (bukan cuma create) supaya masuk `general_ledgers`.

## 1. Trial Balance (**General Ledger — `trial-balance`**)

| Skenario                       | Detail                                                                                                                                             | Hasil                                                                                                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                        | `POST accounting/general-ledger/trial-balance {date_from:"2026-08-01", date_to:"2026-08-31"}` — atau kirim `accounting_period_id` sebagai gantinya | 200, tiap akun tampil `opening balance + period movement = ending balance`; Total Debit = Total Kredit persis                                            |
| Negatif — tanpa anchor tanggal | Kirim body kosong (tanpa `date_from` maupun `accounting_period_id`)                                                                                | Endpoint tetap 200 (semua field `nullable`) tapi opening balance jadi sejak awal data — bukan error 422, verifikasi behavior aktual bukan asumsi ditolak |

## 2. Detail Ledger per Akun (**General Ledger — `detail-ledger`**)

| Skenario                 | Detail                                                                                                                                    | Hasil                                                                                                                                    |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                  | `POST accounting/general-ledger/detail-ledger {chart_of_account_id:<Piutang Usaha AST-03>, date_from:"2026-08-01", date_to:"2026-08-31"}` | 200, `lines[]` berisi tiap baris GL urut tanggal dengan `running_debit`/`running_credit` kumulatif dari `opening_debit`/`opening_credit` |
| Positif — filter dimensi | Tambahkan `business_unit_id:<DIV-MKT>`                                                                                                    | Hanya baris GL dengan `business_units_id` = DIV-MKT yang tampil                                                                          |
| Negatif — akun fiktif    | `chart_of_account_id` tidak ada                                                                                                           | 422                                                                                                                                      |

## 3. Summary by Account per Divisi (**General Ledger — `summary-by-account`**)

| Skenario                      | Detail                                                                                                                         | Hasil                                                                                                                                                                                 |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                       | `POST accounting/general-ledger/summary-by-account {business_unit_id:<DIV-MKT>, date_from:"2026-08-01", date_to:"2026-08-31"}` | Hanya menampilkan total mutasi akun (pendapatan & beban) milik Divisi Marketing — akun yang barisnya tidak pernah dikirim `business_unit_id:DIV-MKT` tidak akan muncul di summary ini |
| Positif — bandingkan 2 divisi | Ulangi dengan `business_unit_id:<DIV-DEV>`, lalu jumlahkan pendapatan kedua hasil                                              | Total harus sama dengan `summary-by-account` TANPA filter `business_unit_id` (konsolidasi) — kalau tidak sama berarti ada baris jurnal yang lupa diisi `business_unit_id`             |

## Netralisasi

- Reverse jurnal (bukan hapus) untuk jurnal yang sudah posted, supaya GL & Trial Balance tetap konsisten.
