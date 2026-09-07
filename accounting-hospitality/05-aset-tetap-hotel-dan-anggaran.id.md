---
title: (Hospitality / Hotel) — 05. Aset Tetap Hotel & Anggaran
category: accounting-hospitality
description: Registrasi & penyusutan aset tetap hotel (auto-post GL saat COA depresiasi dipasang di awal), akuisisi via jurnal manual, dan Budget vs Actual per departemen.
visibility: internal
---

# 05. Aset Tetap Hotel & Anggaran

> Prasyarat: [`01-jurnal-booking-dan-revenue-recognition.id.md`](./01-jurnal-booking-dan-revenue-recognition.id.md) sudah posted (Bank BCA = 331.250.000). Endpoint: **Assets — `{create|calculate-depreciation|run-depreciation}`**, **Budgets — `{create|vs-actual}`**.

## 1. Registrasi Aset Tetap — AC & Peralatan Kamar

**Field validasi aktual `fixed-assets/assets/create`**: `name` (required), `category` (nullable, **enum ketat** `in:land,building,vehicle,equipment,furniture,intangible` — BUKAN teks bebas), `acquisition_date` (required, `Y-m-d`), `acquisition_cost` (required, numeric), `salvage_value` (nullable — **BUKAN** `residual_value`), `useful_life_months`, `depreciation_method` (`in:straight_line,declining_balance`), `asset_account_id`/`depreciation_account_id`/`accum_dep_account_id` (nullable, exists `chart_of_accounts`), `status` (`in:active,disposed,sold,idle`). `asset_code` **di-generate otomatis server-side** (`nextAssetCode()`) — TIDAK dikirim di payload dan TIDAK bisa diisi manual. `current_book_value` saat registrasi = **full `acquisition_cost`** (bug lama yang net-in `salvage_value` sejak hari pertama sudah difix).

| Skenario | Payload kunci                                                                                                                                                                                                                                                                                                                                                 | Hasil                                                                                                                                                                                                                                                                                                     |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST fixed-assets/assets/create {name:"AC Split & Peralatan Laundry Kamar", category:"equipment", acquisition_date:"2026-02-10", acquisition_cost:60000000, salvage_value:6000000, useful_life_months:60, depreciation_method:"straight_line", asset_account_id:<AST-07>, depreciation_account_id:<BBN-03>, accum_dep_account_id:<AST-08>, status:"active"}` | 201 — `asset_code` auto (mis. `FA/2026/0001`), `current_book_value:60000000` (= full `acquisition_cost`, `salvage_value` belum dipotong sama sekali saat registrasi — baru turun setelah penyusutan beneran di-run) |
| Negatif  | `category:"Peralatan Kamar"` (teks bebas, tidak ada di enum)                                                                                                                                                                                                                                                                                                  | 422 — invalid enum value                                                                                                                                                                                                                                                                                  |

## 2. Jurnal Akuisisi (Manual, Terpisah dari Registrasi Aset)

**Catatan proses 2-langkah (bukan bug)**: `fixed-assets/assets/create` HANYA mendaftarkan aset — TIDAK otomatis membuat jurnal akuisisi (Dr Aset / Cr Kas-Bank). Harus dibuat manual.

| Skenario       | Payload kunci                                                                                     | Hasil                                                                                                               |
| -------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Positif        | `code:"JRN-008"`, `date:"2026-02-10"`, `lines:[{AST-07,debit:60000000},{AST-02,credit:60000000}]` | 200, balanced → post                                                                                                |
| Positif — post | `PUT accounting/journals/post`                                                                    | 200 — Peralatan & Perlengkapan Hotel (`AST-07`) = **60.000.000**; Bank BCA = 331.250.000−60.000.000=**271.250.000** |

## 3. Kalkulasi & Jalankan Penyusutan Bulanan

`run-depreciation` **branch-wide** (memproses SEMUA aset `status:active` sekaligus, tidak ada filter per-aset/slug) dan **auto-post GL** HANYA jika `depreciation_account_id` DAN `accum_dep_account_id` sudah dipasang saat registrasi (§1 — sudah dipasang di sini, jadi auto-post). Tidak ada proration hari-dalam-bulan — penyusutan dihitung 1 bulan penuh terlepas dari tanggal akuisisi di tengah bulan.

Penyusutan bulanan (garis lurus) = (60.000.000−6.000.000)/60 = **Rp 900.000/bulan**.

| Skenario                            | Payload kunci                                                                               | Hasil                                                                                                                                                                                                                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — preview                   | `POST fixed-assets/assets/calculate-depreciation {slug:<FA-0001>, as_of_date:"2026-02-28"}` | 200 — `schedule` menampilkan proyeksi penyusutan bulanan Rp 900.000, tidak mengubah data (read-only preview)                                                                                                                                                                      |
| Positif — jalankan                  | `POST fixed-assets/assets/run-depreciation {period_date:"2026-02-10"}`                      | 200 — dinormalisasi ke awal bulan (`2026-02-01`), `created:1` (aset ini), auto-post jurnal Dr `BBN-03` 900.000 / Cr `AST-08` 900.000 KARENA kedua COA sudah terpasang §1; `current_book_value` aset = 54.000.000−900.000=**53.100.000**; `accumulated_depreciation` = **900.000** |
| Negatif — run 2x untuk periode sama | `POST .../run-depreciation {period_date:"2026-02-10"}` (lagi)                               | 200 tapi `created:0, skipped:1` — idempotent, tidak dobel-posting untuk `period_date` yang sama                                                                                                                                                                                   |
| Positif — verifikasi GL             | `general-ledger/trial-balance`                                                              | Beban Penyusutan (`BBN-03`) = **900.000**; Akumulasi Penyusutan (`AST-08`) saldo kredit **900.000**                                                                                                                                                                               |

## 4. Budget per Departemen vs Actual

**Field validasi aktual `accounting/budgets/create`**: `fiscal_year_id` (required), `name` (required), `lines` (required, array min:1), tiap baris `account_id` (required), `business_unit_id` (nullable), `period_month` (required, `Y-m-d`), `budgeted_amount` (required, numeric **min:0** — TIDAK menerima negatif).

| Skenario            | Payload kunci                                                                                                                                                                                                       | Hasil                                                                                                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif             | `POST accounting/budgets/create {fiscal_year_id:<FY2026>, name:"Budget Departemen Kamar Feb 2026", lines:[{account_id:<PDT-01>, business_unit_id:<DEPT-ROM>, period_month:"2026-02-01", budgeted_amount:6000000}]}` | 200                                                                                                                                                                                                    |
| Negatif             | `budgeted_amount: -1000000`                                                                                                                                                                                         | 422 — gagal `min:0`                                                                                                                                                                                    |
| Positif — vs Actual | `POST accounting/budgets/vs-actual {slug:<budget di atas>}`                                                                                                                                                         | 200 — Actual Pendapatan Kamar Februari = **4.545.455** (dari GL `PDT-01` + `business_unit_id:<DEPT-ROM>` di rentang `period_month`) vs Budget 6.000.000 → **under-budget** 1.454.545 (75,76% tercapai) |

## Referensi Silang

- [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) — `AST-07`/`AST-08`/`BBN-03` sengaja mulai dari 0 (bukan bagian saldo awal)
- [`01-jurnal-booking-dan-revenue-recognition.id.md`](./01-jurnal-booking-dan-revenue-recognition.id.md) — Bank BCA sebelum akuisisi (331.250.000)
- [`06-rekonsiliasi-bank-dan-pajak-daerah.id.md`](./06-rekonsiliasi-bank-dan-pajak-daerah.id.md) — Bank BCA setelah akuisisi (271.250.000) jadi baseline rekonsiliasi
