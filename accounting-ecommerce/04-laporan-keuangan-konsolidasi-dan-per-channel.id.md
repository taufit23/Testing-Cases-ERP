---
title: (E-commerce) — 04. Laporan Keuangan Konsolidasi & per Channel
category: accounting-ecommerce
description: Laba Rugi, Neraca, dan Arus Kas konsolidasi — endpoint reports/income-statement, reports/balance-sheet, reports/cash-flow-statement — dan batasan filter dimensi channel yang sebenarnya.
visibility: internal
---

# 04. Laporan Keuangan Konsolidasi & per Channel

> **Prasyarat**: File `00`-`01` sudah dikerjakan (T1-T4 posted).
> **Koreksi penting**: `App\Http\Controllers\Reports\ReportController` (endpoint **Income Statement**, **Balance Sheet**, **Cash Flow Statement**) **TIDAK menerima parameter `business_unit_id` sama sekali** — ketiganya SELALU konsolidasi seluruh channel, tidak ada mode "per Channel" di level laporan keuangan. Breakdown per channel HANYA bisa didekati lewat **General Ledger — `summary-by-account`** + `business_unit_id` (lihat file `02`) untuk akun individual — bukan P&L/Neraca utuh per channel. Judul file ini sengaja menyebut "per Channel" untuk menegaskan batasan ini, bukan karena fitur itu ada.

## 1. Income Statement (**Income Statement**) — Januari 2026

`start_date=2026-01-01`, `end_date=2026-01-31`.

| Baris                                                                |         Jumlah |
| -------------------------------------------------------------------- | -------------: |
| PDT-01 Pendapatan Penjualan E-commerce                               |     50.000.000 |
| PDT-02 Retur & Potongan Penjualan (kontra, category tetap "revenue") |     −1.000.000 |
| **Total Revenue**                                                    | **49.000.000** |
| BBN-02 Beban Biaya Admin PG & MP                                     |        300.000 |
| **Total Expense**                                                    |    **300.000** |
| **Net Income**                                                       | **48.700.000** |

> Catatan: `incomeStatement()` menjumlahkan SEMUA akun berkategori `revenue` dengan net (`credit-debit`) tanpa membedakan flag kontra — PDT-02 otomatis masuk sebagai baris bernilai negatif dan mengurangi total revenue dengan benar. Ini BEDA dari logika `closeYear()` di file `03` yang skip akun kontra-pendapatan (`$balance <= 0` continue) — dua endpoint berbeda punya perilaku berbeda untuk akun yang sama, harus dites terpisah, jangan asumsikan konsisten.

## 2. Balance Sheet (**Balance Sheet**) — per 2026-01-31

| Aset                            |          Jumlah | Liabilitas & Ekuitas                   |          Jumlah |
| ------------------------------- | --------------: | -------------------------------------- | --------------: |
| AST-01 Bank BCA Operasional     |     200.000.000 | LIA-01 Utang Dagang                    |      45.000.000 |
| AST-02 Saldo Payment Gateway    |      35.790.000 | LIA-02 PPN Keluaran                    |       5.390.000 |
| AST-03 Saldo Marketplace        |      68.300.000 | EKT-01 Modal Pemilik                   |     333.000.000 |
| AST-04 Piutang COD              |       8.000.000 | Current Year Earnings (baris sintetis) |      48.700.000 |
| AST-05 Persediaan Barang Dagang |     120.000.000 |                                        |                 |
| **Total Aset**                  | **432.090.000** | **Total Liabilitas + Ekuitas**         | **432.090.000** |

`is_balanced: true` (selisih < 0.01). Baris "Current Year Earnings" adalah baris SINTETIS (bukan baris GL sungguhan) hasil `computeNetIncome()` dari awal fiscal year (2026-01-01) s.d. `as_of_date` — ini workaround karena belum ada closing-entry OTOMATIS per periode (closing hanya terjadi manual lewat `fiscal-year/close-year`, lihat file `03`). Sebelum `close-year` dijalankan, angka 48.700.000 ini akan MUNCUL LAGI dobel dengan saldo EKT-02 Laba Ditahan begitu `close-year` dijalankan (karena closing entry akan ikut menambah EKT-02 sebesar net income kategori revenue/expense yang benar-benar diproses) — pastikan test Neraca "sebelum closing" dan "sesudah closing" dijalankan sebagai skenario terpisah biar tidak salah baca dobel counting.

## Skenario Pengujian

| Skenario | Detail                                                                                                                  | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `reports/income-statement` `start_date=2026-01-01`, `end_date=2026-01-31`.                                              | 200, `revenue: 49000000`, `expense: 300000`, `net_income: 48700000`, `revenue_lines` berisi 2 entri (PDT-01 positif, PDT-02 negatif).                                                                                                                                                                                                                                                                                            |
| Positif  | `reports/balance-sheet` `as_of_date=2026-01-31`.                                                                        | 200, `total_assets: 432090000`, `total_liab_equity: 432090000`, `is_balanced: true`.                                                                                                                                                                                                                                                                                                                                             |
| Positif  | `reports/cash-flow-statement` `start_date=2026-01-01`, `end_date=2026-01-31`.                                           | 200, karena AST-01/AST-02/AST-03 sudah diflag `is_cash_account: true`, seluruh baris GL yang menyentuh akun-akun itu diklasifikasi via `cash_flow_section` dari akun lawan (kontra) — mis. T1 (kontra: PDT-01, Pendapatan, section `operating`) masuk Operating; opening balance AST-01 (kontra: EKT-01, Ekuitas, section `financing`) masuk Financing. `is_reconciled: true` kalau `beginning_cash + net_change = ending_cash`. |
| Negatif  | `reports/income-statement` dengan payload tambahan `business_unit_id: <CHN-WEB id>` mengira akan memfilter per channel. | Parameter diabaikan sepenuhnya (bukan 422) — hasil tetap konsolidasi semua channel. Ini KESALAHAN UMUM kalau tester menyalin pola `business_unit_id` dari `accounting/general-ledger/*` tanpa cek controller `ReportController` dulu.                                                                                                                                                                                            |
| Negatif  | `reports/balance-sheet` untuk branch yang belum punya `fiscal_years` row yang meng-cover `as_of_date`.                  | Tidak error — fallback ke awal tahun kalender (`Carbon::parse($asOfDate)->startOfYear()`) untuk hitung Current Year Earnings, BUKAN exception. Hasil hanya akurat kalau fiscal year branch tsb selaras kalender (kasus FY2026 di suite ini memang selaras).                                                                                                                                                                      |
| Positif  | `reports/cash-flow-statement` untuk branch yang belum flag `is_cash_account` sama sekali.                               | 200 dengan `has_cash_accounts_configured: false` dan semua total 0 — BUKAN error, state valid tapi belum terkonfigurasi.                                                                                                                                                                                                                                                                                                         |

## Netralisasi

- Tidak ada perubahan state (semua endpoint di file ini read-only). Reset lewat reverse jurnal di file `01` kalau perlu.
