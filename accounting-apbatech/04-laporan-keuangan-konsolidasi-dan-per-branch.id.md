---
title: (IT Consultant + Retail Elektronik) — 04. Laporan Keuangan & Breakdown per Business Unit
category: accounting-apbatech
description: Laba Rugi, Neraca, Arus Kas PT APBATECH (1 branch) — dan gap tidak-ada-breakdown-otomatis per Business Unit di endpoint laporan.
visibility: internal
---

# 04. Laporan Keuangan & Breakdown per Business Unit

> **Nama file dipertahankan** (`...-konsolidasi-dan-per-branch.id.md`) untuk menjaga referensi silang lintas suite tetap utuh — isi di bawah SUDAH direvisi total. Sebelumnya file ini menguji "konsolidasi 2 branch"; sekarang **tidak ada lagi konsolidasi lintas-branch sama sekali** (PT APBATECH cuma 1 branch, jadi 1 kali panggil laporan sudah otomatis mencakup semuanya). Yang tersisa relevan dari konsep lama adalah **breakdown per divisi (Business Unit)** — dan itu TETAP manual, bukan fitur laporan siap pakai.
>
> Format pengujian: **Positif** / **Negatif** / **Netralisasi**. Endpoint di `reports/*` (BUKAN `accounting/*`).
> Prasyarat: jurnal file 01 posted, opsional periode file 03 sudah/belum di-close (dua-duanya dites di bawah).

## 1. Laba Rugi PT APBATECH (`POST reports/income-statement`)

| Skenario                                                | Detail                                                                           | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                 | `POST reports/income-statement {start_date:"2026-08-01", end_date:"2026-08-31"}` | 200, satu laporan tunggal mencakup ketiga BU: Pendapatan Managed Services 17.000.000 + Pendapatan Jasa Konsultasi 45.000.000 + Pendapatan Penjualan Barang Elektronik 650.000 = 62.650.000; Beban Software License 3.500.000 + HPP Barang Elektronik 450.000 = 3.950.000; Net Income = **58.700.000**                                                                                                                                                                  |
| ❌ **Negatif — filter per Business Unit TIDAK didukung** | Kirim `business_unit_id:<BU-CONSULT>` berharap laporan hanya Divisi Konsultasi   | **Parameter ini diabaikan sepenuhnya oleh `ReportController::incomeStatement()`** — controller hanya membaca `start_date`/`end_date`+`branch_id` aktif, tidak ada filter/group by `business_unit_id`. Hasil tetap laporan gabungan ketiga divisi. Breakdown per divisi cuma bisa manual lewat `general-ledger/summary-by-account` (file 02 §2) — dokumentasikan ini sebagai gap fitur "P&L per Business Unit", relevan dengan BIG TODO [[project_scale_and_big_todos]] |

## 2. Neraca PT APBATECH (`POST reports/balance-sheet`)

| Skenario                                           | Detail                                                 | Hasil                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif                                            | `POST reports/balance-sheet {as_of_date:"2026-08-31"}` | 200, Total Aset = Total Liabilitas + Ekuitas (mencakup ketiga BU). Net income berjalan (58.700.000, kalau FY belum di-close) muncul sebagai baris sintetis "Current Year Earnings" di Ekuitas — hilang & pindah ke Laba Ditahan (EKT-02) kalau FY sudah di-close (file 03 §3)                                                                          |
| ❌ **Negatif — Neraca per Business Unit tidak ada** | Cari filter `business_unit_id` di endpoint ini         | Tidak relevan secara konsep juga — akun neraca (kas/bank/piutang/utang) umumnya milik perusahaan secara keseluruhan, bukan per divisi (kecuali akun yang memang di-tag `default_business_units_id` seperti AST-03/AST-05/AST-08/AST-09/LIA-04, lihat file 00 §4) — verifikasi manual per akun via `general-ledger/detail-ledger` kalau perlu breakdown |

## 3. Arus Kas PT APBATECH (`POST reports/cash-flow-statement`)

| Skenario | Detail                                                                              | Hasil                                                                                                                                                                                                                            |
| -------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST reports/cash-flow-statement {start_date:"2026-08-01", end_date:"2026-08-31"}` | 200 — verifikasi struktur Operating/Investing/Financing sesuai response aktual saat testing; cross-check klasifikasi akun yang di-override (mis. utang bank) sesuai [[project_balance_sheet_and_cash_flow_classification_fixes]] |

## 4. Rekap Manual Breakdown per Business Unit (dilakukan di luar sistem)

Karena tidak ada endpoint breakdown per-BU (§1), rekap manual di bawah WAJIB dijadikan bagian dari test case supaya angka "level divisi" tetap terverifikasi — datanya diambil dari `general-ledger/summary-by-account` (file 02 §2), bukan dari `reports/income-statement` langsung:

| Item                        | BU-CONSULT | BU-MANAGED | BU-RETAIL | Total Perusahaan |
| --------------------------- | ---------: | ---------: | --------: | ---------------: |
| Total Pendapatan            | 45.000.000 | 17.000.000 |   650.000 |       62.650.000 |
| Total Beban/HPP             |  3.500.000 |          0 |   450.000 |        3.950.000 |
| Net Income (per BU, manual) | 41.500.000 | 17.000.000 |   200.000 |       58.700.000 |

## Netralisasi

- Reverse jurnal sebelum periode closed, atau reopen periode dulu (file 03 §2) kalau harus koreksi setelah closed.

## Referensi Silang

- [`02-general-ledger-trial-balance-per-branch.id.md`](./02-general-ledger-trial-balance-per-branch.id.md)
- [`03-tutup-periode-dan-tahun-fiskal.id.md`](./03-tutup-periode-dan-tahun-fiskal.id.md)
- [[project_scale_and_big_todos]], [[project_balance_sheet_and_cash_flow_classification_fixes]]
