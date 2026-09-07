---
title: (CORETAX) — 05. Anggaran & Aset Tetap
category: accounting-coretax
description: Budget vs Actual memakai transaksi file 01, dan registrasi + penyusutan aset tetap baru di atas akun 1600/1601 yang sudah ada.
visibility: internal
---

# 05. Anggaran & Aset Tetap

> Prasyarat: [`01`](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md) (T4 Beban Gaji 20.000.000 posted di Agustus 2026).
>
> **Sudah di-seed otomatis**: `database/seeders/CoretaxBudgetAndFixedAssetSeeder.php` sudah membuat akun `5503`, budget "Anggaran Beban Gaji Agustus 2026", aset "Toyota Avanza Operasional", DAN sudah menjalankan penyusutan Agustus-nya — semua angka di bawah SUDAH ADA di database, bukan langkah yang perlu dieksekusi ulang.

## 1. Anggaran (**Budgets**)

> Struktur payload: `create` terima header (`fiscal_year_id`, `name`) + `lines[]` (`account_id`, `accounting_period_id`, `budgeted_amount`) sekaligus — bukan endpoint terpisah per baris. Lihat koreksi struktur ini juga di suite `accounting-manufaktur-2/03-anggaran-kuartalan-dan-aset-tetap.id.md` §3.1 (temuan sama, bukan spesifik CORETAX).

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Buat anggaran Beban Gaji Agustus | `POST accounting/budgets/create {fiscal_year_id:<FY2026>, name:"Anggaran Beban Gaji Agustus 2026", lines:[{account_id:<5501>, accounting_period_id:<Agustus 2026>, budgeted_amount:18000000}]}` | 201 |
| **Budget vs Actual — over-budget** | `POST accounting/budgets/vs-actual {slug:<budget di atas>}` | Baris Agustus: `budgeted_amount:18.000.000`, `actual_amount:20.000.000` (dari T4 file 01) → **variance = +2.000.000 (over-budget, akun expense jadi variance positif = boros)** |
| Netralisasi | `DELETE accounting/budgets/delete {id}` setelah selesai | — |

## 2. Aset Tetap (**Assets**)

**Setup dulu**: akun `1600 Aset Tetap` & `1601 Akumulasi Penyusutan Aset Tetap` sudah ada (file 00 §2), tapi **belum ada akun Beban Penyusutan** — buat dulu:

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Buat akun beban penyusutan baru | `POST chart-of-accounts/create {code:"5503", name:"Beban Penyusutan Aset Tetap", type_id:<DAGANG-EXPENSE>, parent_id:<GRP55>, level:3}` | 201 |
| Registrasi aset — Kendaraan Operasional | `POST fixed-assets/assets/create {name:"Toyota Avanza Operasional", category:"vehicle", acquisition_date:"2026-08-01", acquisition_cost:250000000, salvage_value:25000000, useful_life_months:60, depreciation_method:"straight_line", asset_account_id:<1600>, depreciation_account_id:<5503>, accum_dep_account_id:<1601>}` | 201, `asset_code` auto-generate format `FA/2026/####` |
| Jalankan penyusutan Agustus | `POST fixed-assets/run-depreciation {period_date:"2026-08-01"}` | 1 baris `asset_depreciations`, nominal = (250.000.000−25.000.000)/60 = **Rp 3.750.000 tepat**, `current_book_value` = 250.000.000−3.750.000 = **246.250.000**, jurnal auto-post `Dr 5503 3.750.000 / Cr 1601 3.750.000` |
| **Negatif — double posting bulan sama** | Jalankan lagi `run-depreciation` period Agustus | Ditolak/di-skip, tidak ada baris kedua |
| Verifikasi saldo `1601` di Trial Balance | `general-ledger/trial-balance` per 2026-08-31 | `1601` sekarang punya delta tambahan −3.750.000 dari penyusutan aset baru ini, di atas baseline file 02 |

## Referensi Silang

- [`01-jurnal-manual-dan-verifikasi-saldo-awal.id.md`](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md) — actual Beban Gaji untuk Budget vs Actual
- [`accounting-manufaktur-2/03-anggaran-kuartalan-dan-aset-tetap.id.md`](../accounting-manufaktur-2/03-anggaran-kuartalan-dan-aset-tetap.id.md) — koreksi struktur payload budget yang sama berlaku di sini
