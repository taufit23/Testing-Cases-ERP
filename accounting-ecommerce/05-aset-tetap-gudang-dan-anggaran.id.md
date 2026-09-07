---
title: (E-commerce) — 05. Aset Tetap Gudang & Anggaran
category: accounting-ecommerce
description: Fixed Assets (register, jadwal & jalankan penyusutan garis lurus) dan Budget vs Actual per channel — endpoint fixed-assets/assets/*, fixed-assets/disposals/*, accounting/budgets/*.
visibility: internal
---

# 05. Aset Tetap Gudang & Anggaran

> **Prasyarat**: File `00`-`01`. Endpoint Fixed Assets di suite ini memakai path yang benar: **Assets — `{action}`** dan **Disposals — `{action}`** — BUKAN `accounting/fixed-assets/*`.

## 1. Register Aset Tetap — Peralatan Gudang

`fixed-assets/assets/create`:

| Field                     | Nilai                                        |
| ------------------------- | -------------------------------------------- |
| `name`                    | Rak & Conveyor Gudang                        |
| `category`                | equipment                                    |
| `acquisition_date`        | 2026-01-01                                   |
| `acquisition_cost`        | 60.000.000                                   |
| `salvage_value`           | 6.000.000                                    |
| `useful_life_months`      | 60 (5 tahun)                                 |
| `depreciation_method`     | straight_line                                |
| `asset_account_id`        | AST-07 Peralatan Gudang                      |
| `depreciation_account_id` | BBN-04 Beban Penyusutan Peralatan Gudang     |
| `accum_dep_account_id`    | AST-08 Akumulasi Penyusutan Peralatan Gudang |

Penyusutan bulanan garis lurus = (60.000.000 − 6.000.000) / 60 = **900.000/bulan**.

> **Kontrak field asli Assets — `create`** (verifikasi baca kode langsung, `App\Http\Controllers\Finance\FixedAssets::create()`): `asset_code` TIDAK bisa diisi manual — server SELALU generate sendiri format `FA/{tahun}/{urutan}`, di-strip diam-diam kalau dikirim di payload. `category` HANYA menerima salah satu dari 6 nilai fix: `land|building|vehicle|equipment|furniture|intangible` — payload di atas sudah pakai `equipment` yang valid. Nama field nilai sisa yang benar adalah `salvage_value` (bukan `residual_value`). `current_book_value` saat registrasi = **full `acquisition_cost`** (BUKAN dikurangi `salvage_value` di muka) — book value baru turun setelah penyusutan beneran di-run.

## Skenario Pengujian

| Skenario | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif  | `fixed-assets/assets/create` dengan payload di atas.                                                                                                                                                                                                                                                                                                                                                                                                                  | 201, `asset_code` auto-generate format `FA/2026/0001`, `current_book_value` = **60.000.000** (= full `acquisition_cost`, `salvage_value` belum dipotong sama sekali saat create), `accumulated_depreciation: 0`.                                                                                                                                                                                      |
| Positif  | `fixed-assets/assets/calculate-depreciation` dengan `as_of_date=2026-03-01`.                                                                                                                                                                                                                                                                                                                                                                                          | 200, `schedule` read-only 2 baris (Feb, Mar — mulai bulan SETELAH `acquisition_date`), masing-masing `depreciation_amount: 900000`, `book_value_after` turun 900.000 tiap baris (59.100.000 lalu 58.200.000 dihitung dari book value awal 60.000.000, bukan dari `current_book_value` field). Endpoint ini TIDAK menulis apa pun ke DB (murni simulasi).                                                                       |
| Positif  | `fixed-assets/assets/run-depreciation` dengan `period_date=2026-02-01`.                                                                                                                                                                                                                                                                                                                                                                                               | 200, `created: 1`. Membuat 1 baris `AssetDepreciation` (`depreciation_amount: 900000`), asset `current_book_value` turun jadi 53.100.000 (54.000.000 − 900.000), `accumulated_depreciation: 900000`. KARENA `asset_account_id`/`depreciation_account_id`/`accum_dep_account_id` sudah diisi saat create, jurnal otomatis terbuat & terposting (Dr BBN-04 900.000 / Cr AST-08 900.000) — `is_posted: true` di baris depresiasi. |
| Positif  | `run-depreciation` lagi dengan `period_date=2026-02-01` (periode yang sama).                                                                                                                                                                                                                                                                                                                                                                                          | 200, `created: 0, skipped: 1` — idempotent, tidak dobel-posting untuk periode yang sama.                                                                                                                                                                                                                                                                                                                                       |
| Negatif  | `fixed-assets/assets/create` dengan `acquisition_cost` negatif.                                                                                                                                                                                                                                                                                                                                                                                                       | 422 — `acquisition_cost` min:0.                                                                                                                                                                                                                                                                                                                                                                                                |
| Negatif  | `fixed-assets/assets/create` dengan `depreciation_method` di luar `straight_line`/`declining_balance` (mis. `sum_of_years`).                                                                                                                                                                                                                                                                                                                                          | 422 — `in:straight_line,declining_balance`.                                                                                                                                                                                                                                                                                                                                                                                    |
| Positif  | `fixed-assets/disposals/create` untuk aset di atas setelah 2 bulan penyusutan (book value 53.100.000), `disposal_type: sold`, `disposal_proceeds: 50000000`.                                                                                                                                                                                                                                                                                                          | 201, `book_value_at_disposal: 53100000`, `gain_loss: 50000000 - 53100000 = -3100000` (rugi pelepasan). Asset `status` berubah jadi `sold`.                                                                                                                                                                                                                                                                                     |
| Negatif  | Disposal TIDAK menulis jurnal apa pun ke GL secara otomatis — ini gap yang harus didokumentasikan. `AssetDisposals::create()` hanya menyimpan `gain_loss` sebagai angka di tabel `asset_disposals`, TIDAK memanggil `JournalPostingService` sama sekali. Kalau tester berasumsi rugi/laba pelepasan otomatis masuk Laba Rugi (`reports/income-statement`), itu SALAH — harus dijurnal manual terpisah lewat `accounting/journals/create` kalau ingin tercermin di GL. | Bukan bug ditest sebagai "negatif ditolak", tapi sebagai gap fungsional yang wajib dicatat di laporan hasil test.                                                                                                                                                                                                                                                                                                              |
| Negatif  | `fixed-assets/disposals/create` untuk aset yang statusnya sudah bukan `active` (mis. sudah dilepas sebelumnya).                                                                                                                                                                                                                                                                                                                                                       | Ditolak — `content.asset_not_active`.                                                                                                                                                                                                                                                                                                                                                                                          |

## 2. Budget vs Actual per Channel

`accounting/budgets/create`:

| `account_id`                 | `business_unit_id` | `period_month` | `budgeted_amount` |
| ---------------------------- | ------------------ | -------------- | ----------------: |
| BBN-02 (Beban Admin PG & MP) | CHN-WEB            | 2026-01-01     |           500.000 |
| BBN-02 (Beban Admin PG & MP) | CHN-MP             | 2026-01-01     |           800.000 |

`accounting/budgets/vs-actual` (mengacu GL aktual T2 dari file `01`, satu-satunya aktivitas BBN-02 di Januari — tercatat dimensi CHN-WEB):

| Channel | Budgeted |  Actual |                                     Variance | Variance % |
| ------- | -------: | ------: | -------------------------------------------: | ---------: |
| CHN-WEB |  500.000 | 300.000 |                      −200.000 (under-budget) |       −40% |
| CHN-MP  |  800.000 |       0 | −800.000 (under-budget, belum ada transaksi) |      −100% |

`actual_amount` dihitung dari `normal_balance` tipe akun BBN-02 (Beban, debit-normal): `actual = debit − credit` dalam rentang `period_month` tsb, difilter juga `business_unit_id` line-nya.

## Skenario Pengujian (Budget)

| Skenario | Detail                                                                                    | Hasil                                                          |
| -------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Positif  | `accounting/budgets/create` dengan 2 baris di atas (`fiscal_year_id`, `name`, `lines[]`). | 201, `budget` + `lines` terbuat, `status: draft`.              |
| Positif  | `accounting/budgets/vs-actual` dengan `slug` budget di atas, SETELAH T2 sudah di-post.    | 200, hasil sesuai tabel di atas, `totals.variance = -1000000`. |
| Negatif  | `accounting/budgets/create` dengan `lines.*.budgeted_amount` negatif.                     | 422 — `budgeted_amount` min:0.                                 |
| Negatif  | `accounting/budgets/create` TANPA `fiscal_year_id`.                                       | 422 — `fiscal_year_id` required.                               |
| Negatif  | `accounting/budgets/create` dengan `lines` kosong (`[]`).                                 | 422 — `lines` minimal 1.                                       |
| Negatif  | `accounting/budgets/update` dengan `status` di luar `draft,active,closed`.                | 422 — `in:draft,active,closed`.                                |

## Netralisasi

- `fixed-assets/assets/delete` untuk aset yang belum punya baris `AssetDepreciation` (kalau sudah ada, endpoint menolak dengan `content.cannot_delete_has_depreciations` — reverse dulu jurnal penyusutannya via `accounting/journals/reverse` sebelum hapus record aset untuk keperluan reset test).
- `fixed-assets/disposals/delete` untuk baris disposal test.
- `accounting/budgets/delete` untuk budget test.
