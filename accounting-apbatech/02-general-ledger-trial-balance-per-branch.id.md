---
title: (IT Consultant + Retail Elektronik) — 02. General Ledger & Trial Balance
category: accounting-apbatech
description: Verifikasi Detail Ledger, Summary by Account (dimensi Business Unit), dan Trial Balance PT APBATECH (1 branch, 1 set GL) atas transaksi file 01.
visibility: internal
---

# 02. General Ledger & Trial Balance

> **Nama file dipertahankan** (`...-per-branch.id.md`) untuk menjaga referensi silang lintas suite tetap utuh — isi di bawah SUDAH direvisi ke model 1 branch. Judul konten sekarang "General Ledger & Trial Balance" biasa (bukan lagi "per branch"), karena PT APBATECH cuma 1 branch — breakdown per divisi memakai dimensi Business Unit (§2), bukan isolasi branch.
>
> Prasyarat: [`01`](./01-jurnal-invoice-jasa-konsultasi-dan-milestone.id.md) — jurnal §1.1–1.5 posted (semua di branch PT APBATECH yang sama, hanya beda `business_unit_id`).
>
> Semua endpoint `general-ledger/*` dan `reports/*` di-scope `BranchHelper::activeBranchId($request)` — karena cuma ada 1 branch, tidak ada lagi switch-context untuk melihat "sisi lain" data. Satu kali panggil endpoint sudah mencakup seluruh transaksi (ketiga BU tercampur), kecuali difilter manual pakai `business_unit_id` (§2).

## 1. Detail Ledger — PT APBATECH

| Skenario                                      | Payload kunci                                                                                               | Hasil                                                                                                                                                  |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Detail Ledger akun Piutang Usaha              | `general-ledger/detail-ledger {chart_of_account_id:<AST-04>, date_from:"2026-08-01", date_to:"2026-08-31"}` | 2 baris (1.1 debit 13.320.000, 1.2 debit 49.050.000) — saldo akhir naik dari saldo awal 45.000.000 jadi **107.370.000**                                |
| Detail Ledger akun PPN Keluaran               | Filter `LIA-02`                                                                                             | 3 baris (1.1 credit 1.320.000, 1.2 credit 4.950.000, 1.5 credit 71.500) — saldo akhir **+6.341.500**                                                   |
| Detail Ledger akun Bank BCA                   | Filter `AST-02`                                                                                             | 1 baris (1.4 credit 3.500.000) — saldo akhir turun dari 300.000.000 jadi **296.500.000**                                                               |
| Detail Ledger akun Bank Mandiri (Toko Retail) | Filter `AST-03`                                                                                             | 1 baris (1.5 debit 721.500) — saldo akhir naik dari 60.000.000 jadi **60.721.500**                                                                     |
| Detail Ledger akun Pendapatan Diterima Dimuka | Filter `LIA-04`                                                                                             | 1 baris (1.3 debit 5.000.000) — saldo akhir turun dari 30.000.000 jadi **25.000.000**                                                                  |
| Detail Ledger akun Persediaan                 | Filter `AST-05`                                                                                             | 1 baris (1.5 credit 450.000) — saldo akhir turun dari 32.500.000 jadi **32.050.000** (jurnal manual, BUKAN dari `sku_stocks` — lihat gap file 01 §1.5) |

## 2. Summary by Account — Filter Dimensi Business Unit

> Ini adalah pengganti konsep "per branch" yang lama. Karena 1 branch, drill-down per divisi dilakukan lewat filter `business_unit_id` di `general-ledger/summary-by-account` — BUKAN switch-branch.

| Skenario                                                                | Payload kunci                                                                                                           | Hasil                                                                                                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Summary akun Pendapatan Managed Services, filter `BU-MANAGED`           | `general-ledger/summary-by-account {chart_of_account_id:<PDT-02>, business_unit_id:<BU-MANAGED>}`                       | Total movement = 12.000.000 (1.1) + 5.000.000 (1.3) = **17.000.000**                                                                                  |
| Summary akun Pendapatan Jasa Konsultasi, filter `BU-CONSULT`            | `chart_of_account_id:<PDT-01>, business_unit_id:<BU-CONSULT>`                                                           | Total = **45.000.000** (1.2)                                                                                                                          |
| Summary akun Pendapatan Penjualan Barang Elektronik, filter `BU-RETAIL` | `chart_of_account_id:<PDT-03>, business_unit_id:<BU-RETAIL>`                                                            | Total = **650.000** (1.5)                                                                                                                             |
| Summary akun Beban Software License, tanpa filter BU                    | `chart_of_account_id:<BBN-04>`                                                                                          | Total = 3.500.000 — cocok karena hanya 1 baris & sudah ada `business_unit_id:<BU-CONSULT>`                                                            |
| Negatif — baris tanpa `business_unit_id`                                | Filter BU pada akun yang punya baris campuran (ber-BU dan tidak, mis. AST-04 Piutang Usaha yang tidak di-tag BU apapun) | Baris tanpa BU harus ke-exclude dari hasil filter — verifikasi behavior aktual (pola sama seperti temuan `docs/testing/accounting-coretax/02-...` §2) |

## 3. Trial Balance PT APBATECH

| Skenario                                        | Payload kunci                                                       | Hasil                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Trial Balance per 2026-08-31                    | `general-ledger/trial-balance {as_of:"2026-08-31"}`                 | Debit = Kredit; total mengikuti saldo awal file 00 §10 + jurnal §1.1–1.5 file 01 — SATU set trial balance saja, mencakup ketiga BU tercampur                                                                                                                                                                                                                            |
| ❌ **Tidak ada Trial Balance per Business Unit** | Cari parameter `business_unit_id` di `general-ledger/trial-balance` | Tidak ada — trial balance selalu di level branch penuh. Breakdown P&L per divisi (BU-CONSULT/BU-MANAGED/BU-RETAIL) hanya bisa lewat `summary-by-account` per akun (§2), bukan 1 laporan trial-balance per-BU siap pakai — lihat detail keterbatasan di [`04-laporan-keuangan-konsolidasi-dan-per-branch.id.md`](./04-laporan-keuangan-konsolidasi-dan-per-branch.id.md) |

## Referensi Silang

- [`01-jurnal-invoice-jasa-konsultasi-dan-milestone.id.md`](./01-jurnal-invoice-jasa-konsultasi-dan-milestone.id.md)
- [`04-laporan-keuangan-konsolidasi-dan-per-branch.id.md`](./04-laporan-keuangan-konsolidasi-dan-per-branch.id.md)
