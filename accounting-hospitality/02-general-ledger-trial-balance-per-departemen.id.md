---
title: (Hospitality / Hotel) — 02. GL & Trial Balance per Departemen
category: accounting-hospitality
description: Detail Ledger, Summary by Account dengan filter dimensi Business Unit (Kamar/F&B/Spa), dan Trial Balance — verifikasi silang seluruh angka file 01.
visibility: internal
---

# 02. GL & Trial Balance per Departemen

> Prasyarat: [`01-jurnal-booking-dan-revenue-recognition.id.md`](./01-jurnal-booking-dan-revenue-recognition.id.md) — semua jurnal §1.1-1.7 sudah `posted`. Endpoint: **General Ledger — `{detail-ledger|summary-by-account|trial-balance}`** (semua `POST`).

## 1. Trial Balance (**General Ledger — `trial-balance`**)

| Skenario               | Payload kunci                                                            | Hasil                                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                | `POST accounting/general-ledger/trial-balance {as_of_date:"2026-02-06"}` | 200 — Total Debit = Total Kredit = **573.815.000** (identik dengan Total Aset file `01`), tiap akun cocok persis dengan tabel "Ringkasan Saldo Akun Kunci" file `01` |
| Positif — cek `AST-03` | Baris `AST-03 Bank Mandiri Valas` di Trial Balance                       | Saldo **162.800.000** (IDR, sudah hasil konversi `CurrencyEngine` — Trial Balance TIDAK menampilkan nilai USD mentah, hanya base currency)                           |

## 2. Detail Ledger per Akun (**General Ledger — `detail-ledger`**)

| Skenario                               | Payload kunci                                                           | Hasil                                                                                                                                                                                                      |
| -------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                | `{account_id:<LIA-02>, start_date:"2026-02-01", end_date:"2026-02-06"}` | 200 — running balance: 75.000.000 (opening) → +5.000.000 (§1.1) → +7.800.000 (§1.2) → −5.000.000 (§1.3) → saldo akhir **82.800.000**, 3 baris mutasi tampil berurutan sesuai tanggal                       |
| Positif — jejak reverse tetap terlihat | `{account_id:<AST-01>, start_date:"2026-02-01", end_date:"2026-02-06"}` | 200 — 5 baris: opening 10.000.000, +2.220.000 (§1.4), +1.665.000 (§1.5), −50.000 (§1.8 test), +50.000 (§1.8 reversal) — baris reversal TETAP muncul (bukan dihapus), saldo akhir kembali ke **13.885.000** |

## 3. Summary by Account dengan Filter Dimensi Departemen (**General Ledger — `summary-by-account`**)

Verifikasi breakdown per Business Unit cocok dengan total konsolidasi — pola sama seperti suite F&B kafe (per outlet) dan manufaktur (per lini produksi), di sini per departemen hotel.

| Skenario                                                  | Payload kunci                                                                   | Hasil                                                                                                                                                                                                                            |
| --------------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — filter DEPT-ROM                                 | `{business_unit_id:<DEPT-ROM>, start_date:"2026-02-01", end_date:"2026-02-06"}` | 200 — hanya menampilkan mutasi §1.1, §1.2, §1.3 (semua bertag `DEPT-ROM`): `AST-02` +5.000.000, `AST-03` +7.800.000, `LIA-02` net +7.800.000 (5.000.000+7.800.000−5.000.000), `PDT-01` +4.545.455, `LIA-03` +454.545             |
| Positif — filter DEPT-FNB                                 | `{business_unit_id:<DEPT-FNB>, ...}`                                            | 200 — hanya §1.4: `AST-01` +2.220.000, `PDT-02` +2.000.000, `LIA-04` +220.000                                                                                                                                                    |
| Positif — filter DEPT-SPA                                 | `{business_unit_id:<DEPT-SPA>, ...}`                                            | 200 — hanya §1.5: `AST-01` +1.665.000, `PDT-03` +1.500.000, `LIA-04` +165.000                                                                                                                                                    |
| **Positif — verifikasi total 3 departemen = konsolidasi** | Jumlahkan `PDT-01`+`PDT-02`+`PDT-03` dari 3 filter di atas                      | 4.545.455+2.000.000+1.500.000 = **8.045.455** — HARUS sama persis dengan total pendapatan tanpa filter dimensi (Trial Balance)                                                                                                   |
| Positif — mutasi tanpa dimensi (perusahaan-wide)          | `{account_id:<LIA-01>, business_unit_id:null, ...}`                             | 200 — §1.6 (restock F&B) TIDAK bertag Business Unit — muncul di summary konsolidasi tapi TIDAK muncul di filter per departemen manapun (perilaku benar: transaksi non-operasional departemen, e.g. pembelian & payroll gabungan) |
| Negatif                                                   | `business_unit_id` milik branch lain (cross-tenant)                             | Hasil kosong / tidak ada mutasi — bukan error, sesuai isolasi branch                                                                                                                                                             |

## Referensi Silang

- [`01-jurnal-booking-dan-revenue-recognition.id.md`](./01-jurnal-booking-dan-revenue-recognition.id.md) — sumber seluruh angka di atas
- [`04-laporan-keuangan-konsolidasi-dan-per-departemen.id.md`](./04-laporan-keuangan-konsolidasi-dan-per-departemen.id.md) — Trial Balance ini jadi acuan mutlak Neraca & Laba Rugi
