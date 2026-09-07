---
title: (Service Business / Agency) — 04. Laporan Keuangan per Divisi
category: accounting-service-agency
description: Skenario pengujian 04. laporan keuangan per divisi dengan ciri khas Service Business / Agency.
visibility: internal
---

# 04. Laporan Keuangan per Divisi

> **Ciri Khas Skenario**: Fokus pada pengakuan pendapatan bertahap (amortisasi retainer), tagihan recurring, dan pelacakan profitabilitas per divisi (Marketing vs Dev).
> Format pengujian mengikuti standar: **Positif** (jalur normal harus sukses) / **Negatif** (input salah harus ditolak) / **Netralisasi** (rollback).
> Endpoint di `reports/*` (BUKAN `accounting/*`).

## 1. Laba Rugi (`POST reports/income-statement`)

| Skenario                                          | Detail                                                                           | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                           | `POST reports/income-statement {start_date:"2026-08-01", end_date:"2026-08-31"}` | 200, `revenue_lines[]`, `expense_lines[]`, `net_income = revenue - expense` sesuai perhitungan manual dari jurnal yang sudah di-post di file 01                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ❌ **Negatif — filter per divisi TIDAK didukung** | Kirim `business_unit_id:<DIV-MKT>` berharap laporan hanya Divisi Marketing       | **Parameter ini diabaikan sepenuhnya oleh `ReportController::incomeStatement()`** — controller hanya membaca `start_date`/`end_date`, tidak ada logic filter/group by `business_unit_id` sama sekali. Hasil yang keluar TETAP laporan konsolidasi semua divisi. Ini gap fitur, bukan bug validasi — jangan tulis test case "Filter Laba Rugi per dimensi" sebagai kalau itu didukung. Kalau breakdown per divisi dibutuhkan, satu-satunya jalan saat ini adalah `accounting/general-ledger/summary-by-account` dengan `business_unit_id` per akun pendapatan/beban (lihat file 02 §3), dihitung manual per divisi |

## 2. Neraca (`POST reports/balance-sheet`)

| Skenario | Detail                                                 | Hasil                                                                                                                                                                                                                                                                                                                       |
| -------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST reports/balance-sheet {as_of_date:"2026-08-31"}` | 200, Total Aset = Total Liabilitas + Ekuitas. Net income tahun berjalan (kalau fiscal year belum di-close) dilipat masuk ke Ekuitas sebagai baris sintetis "Current Year Earnings" — kalau fiscal year SUDAH di-close (file 03 §4), net income tersebut sudah pindah ke Laba Ditahan (EKT-02) dan baris sintetis ini hilang |

## 3. Arus Kas (`POST reports/cash-flow-statement`)

| Skenario | Detail                                                                              | Hasil                                                                                                                         |
| -------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST reports/cash-flow-statement {start_date:"2026-08-01", end_date:"2026-08-31"}` | 200 — verifikasi struktur Operating/Investing/Financing sesuai response aktual saat testing (belum dicek detail di suite ini) |

## Netralisasi

- Reverse jurnal sebelum periode closed, atau reopen periode dulu (file 03 §3) kalau harus koreksi setelah closed.
