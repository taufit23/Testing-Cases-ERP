---
title: (Construction / Project Based) — 04. Laporan Keuangan Konsolidasi & per Proyek
category: accounting-construction
description: Neraca, Laba Rugi, dan Arus Kas PT Bangun Persada dari reports/balance-sheet, reports/income-statement, reports/cash-flow-statement — sebelum dan sesudah Close Fiscal Year.
visibility: internal
---

# 04. Laporan Keuangan Konsolidasi & per Proyek

> Endpoint: **Balance Sheet**, **Income Statement**, **Cash Flow Statement** (semua `POST`, param `as_of_date`/`start_date`+`end_date`). Angka acuan dari file 02 §1 (state SEBELUM Close Fiscal Year, file 03).
>
> Arti masing-masing laporan (Neraca = snapshot per tanggal, Laba Rugi = rentang waktu, Arus Kas = pergerakan kas) sudah dijelaskan di `../accounting/04-laporan-keuangan.id.md` (Konsep Dasar Tambahan) — file ini fokus ke bagaimana angka proyek konstruksi (uang muka, retensi, pendapatan progres) muncul di 3 laporan itu.

## 1. Neraca (Balance Sheet) — `as_of_date` sebelum Close Fiscal Year

| Bagian                         | Akun                                                      |             Saldo |
| ------------------------------ | --------------------------------------------------------- | ----------------: |
| Aset                           | AST-01 Bank Mandiri Proyek                                |       850.200.000 |
| Aset                           | AST-02 Piutang Progres Proyek                             |       345.000.000 |
| Aset                           | AST-03 Piutang Retensi                                    |        45.000.000 |
| Aset                           | AST-04 Persediaan Bahan Material                          |        40.000.000 |
| **Total Aset**                 |                                                           | **1.280.200.000** |
| Liabilitas                     | LIA-01 Utang Subkontraktor                                |       145.000.000 |
| Liabilitas                     | LIA-02 Uang Muka Proyek Diterima                          |       360.000.000 |
| Liabilitas                     | LIA-03 Utang Retensi Subkontraktor                        |        15.000.000 |
| Liabilitas                     | LIA-04 PPN Keluaran                                       |        35.200.000 |
| **Total Liabilitas**           |                                                           |   **555.200.000** |
| Ekuitas                        | EKT-01 Modal Pemilik                                      |       565.000.000 |
| Ekuitas                        | Current Year Earnings (sintetis, belum ada closing entry) |       160.000.000 |
| **Total Ekuitas**              |                                                           |   **725.200.000** |
| **Total Liabilitas + Ekuitas** |                                                           | **1.280.200.000** |

Total Aset (1.280.200.000) = Total Liabilitas + Ekuitas (1.280.200.000) ✓. "Current Year Earnings" adalah baris sintetis yang dihitung `balanceSheet()` dari net income tahun berjalan (lihat `ReportController::balanceSheet()` docblock) — SELAMA belum `close-year`, ini bukan baris GL sungguhan di EKT-02.

## 2. Neraca SETELAH Close Fiscal Year (file 03 §2)

Setelah `close-year`, baris "Current Year Earnings" sintetis hilang dan digantikan saldo GL nyata di EKT-02 Laba Ditahan = 160.000.000 — Total Ekuitas tetap 725.200.000, Total Aset/Liabilitas tidak berubah karena closing entry hanya menutup akun Pendapatan/Beban ke Ekuitas (tidak menyentuh Aset/Liabilitas).

## 3. Laba Rugi (Income Statement) — `start_date: 2026-01-01`, `end_date: 2026-01-31`

| Baris                              |          Jumlah |
| ---------------------------------- | --------------: |
| Pendapatan Progres Proyek (PDT-01) |     300.000.000 |
| **Total Pendapatan**               | **300.000.000** |
| Beban Pokok Proyek (BBN-01)        |      40.000.000 |
| Beban Subkontraktor (BBN-02)       |     100.000.000 |
| **Total Beban**                    | **140.000.000** |
| **Net Income**                     | **160.000.000** |

## 4. Arus Kas (Cash Flow Statement, metode langsung) — `start_date: 2026-01-01`, `end_date: 2026-01-31`

Prasyarat: AST-01 Bank Mandiri Proyek WAJIB `is_cash_account: true` (file 00 §1) — kalau belum di-flag, `cashFlowStatement()` mengembalikan semua section 0 dengan `has_cash_accounts_configured: false` (bukan error).

| Aktivitas              | Baris                                                                      |           Jumlah |
| ---------------------- | -------------------------------------------------------------------------- | ---------------: |
| Operating              | T1 Uang Muka Proyek A (kontra LIA-02, tipe Liabilitas → default operating) |     +222.000.000 |
| Operating              | T5 Pencairan retensi subkontraktor (kontra LIA-03)                         |       −5.000.000 |
| Operating              | T6 Uang Muka Proyek B (kontra LIA-02)                                      |     +133.200.000 |
| Operating              | T4 + reversal (kontra LIA-01, saling meniadakan)                           |                0 |
| **Total Operating**    |                                                                            | **+350.200.000** |
| Investing              | (tidak ada transaksi aset tetap di suite ini — lihat file 05)              |                0 |
| Financing              | (tidak ada pinjaman bank di suite ini)                                     |                0 |
| **Net Change in Cash** |                                                                            | **+350.200.000** |

Beginning cash (sebelum Januari 2026) = 500.000.000 (saldo awal Bank, file 00 §6). Ending cash = 500.000.000 + 350.200.000 = **850.200.000** — cocok dengan saldo AST-01 di Neraca §1 (`is_reconciled: true`).

**Sebab-akibat:** uang muka proyek (T1, T6) masuk **Operating**, BUKAN Financing — ini gampang disalahsangka karena "uang muka" terdengar seperti pinjaman/pendanaan. Tapi klasifikasi arus kas murni ikut `cash_flow_section` akun LAWANNYA (LIA-02 Uang Muka Proyek Diterima, tipe Liabilitas Jangka Pendek dengan `cash_flow_section: operating` — lihat §00 §2 di suite `accounting/`), bukan ikut "kesan" nama transaksinya. Financing itu khusus modal pemilik/pinjaman bank jangka panjang, yang di suite ini memang tidak ada transaksinya (makanya section Financing di tabel atas selalu 0).

## 5. Skenario Pengujian

| Skenario | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Hasil                                                                                                                                       |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `reports/balance-sheet` `as_of_date: 2026-01-31` (sebelum close year).                                                                                                                                                                                                                                                                                                                                                                                                                                                | `is_balanced: true`, `total_assets` = `total_liab_equity` = 1.280.200.000 sesuai §1.                                                        |
| Positif  | `reports/income-statement` `start_date/end_date` Januari 2026.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `net_income` = 160.000.000 sesuai §3.                                                                                                       |
| Positif  | `reports/cash-flow-statement` `start_date/end_date` Januari 2026.                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `is_reconciled: true`, `ending_cash` = 850.200.000 sesuai §4.                                                                               |
| Positif  | Filter Laba Rugi per dimensi proyek — **CATATAN GAP**: `reports/income-statement` (`ReportController::incomeStatement()`) TIDAK menerima parameter `business_unit_id` sama sekali — laporan ini SELALU konsolidasi semua proyek dalam 1 branch, tidak ada breakdown per proyek bawaan sistem. Kalau butuh Laba Rugi per proyek, pakai `accounting/general-ledger/summary-by-account` dengan filter `business_unit_id` manual per akun Pendapatan/Beban (lihat file 02 §2), BUKAN endpoint `reports/income-statement`. | Dokumentasikan sebagai keterbatasan fitur, bukan bug — jangan buat test case yang mengharap `reports/income-statement` punya filter proyek. |
| Positif  | `reports/balance-sheet` `as_of_date` SETELAH `close-year` (file 03).                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `is_balanced: true` tetap, tapi baris Ekuitas sekarang murni dari GL (EKT-01 + EKT-02), tanpa baris sintetis "Current Year Earnings".       |
| Negatif  | `reports/cash-flow-statement` sebelum AST-01 di-flag `is_cash_account`.                                                                                                                                                                                                                                                                                                                                                                                                                                               | `has_cash_accounts_configured: false`, semua section 0 — bukan error, tapi harus dibedakan dari "memang tidak ada mutasi kas".              |

## Netralisasi

- Tidak ada perubahan state di file ini (semua endpoint `reports/*` read-only) — netralisasi cukup mengikuti file 01/03.
