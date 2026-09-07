---
title: (Nonprofit / NGO) — 04. Laporan Keuangan & Aktivitas per Program
category: accounting-ngo
description: Neraca, Laba Rugi, Arus Kas (reports/*) — DAN batasan penting soal filter per-program (business_unit_id) yang TIDAK didukung endpoint ini.
visibility: internal
---

# 04. Laporan Keuangan & Aktivitas per Program

> Prasyarat: [`03`](./03-tutup-periode-bulanan-dan-tahun-fiskal.id.md) — FY2026 sudah closed, closing entry sudah posted (Pendapatan/Beban ter-nol-kan, EKT-03 = 68.000.000). Endpoint: `reports/{balance-sheet,income-statement,cash-flow-statement}` (controller `Reports\ReportController`).

## 1. Batasan Penting — Tidak Ada "Laporan Aktivitas per Program" Native

Nama file draf lama ("Laporan Aktivitas per Program") mengasumsikan ada 1 endpoint laporan laba-rugi yang bisa difilter per Business Unit. **Ini TIDAK benar** — sudah dicek `Reports\ReportController`: `balance-sheet`, `income-statement`, dan `cash-flow-statement` tidak menerima parameter `business_unit_id` sama sekali. Filter dimensi HANYA ada di modul `accounting/general-ledger` (lihat file [`02`](./02-general-ledger-trial-balance-per-program.id.md)).

Konsekuensi: "Laporan Aktivitas per Program" versi NGO harus disusun **manual** dari `accounting/general-ledger/summary-by-account` per `business_unit_id` (sudah dikerjakan di file 02 §2), BUKAN dari 1 panggilan endpoint laporan resmi. Ini bukan bug — ini gap fitur yang harus dicatat, bukan diasumsikan "sudah ada".

| Skenario                                 | Payload kunci                                                | Hasil                                                                                                                                                                                                                                                                                        |
| ---------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif/edge — buktikan tidak ada filter | `POST reports/income-statement {business_unit_id:<PRG-EDU>}` | Parameter `business_unit_id` diabaikan (bukan error) — response tetap laporan konsolidasi seluruh yayasan, BUKAN laporan khusus Program Pendidikan. Kalau ternyata backend melempar error validasi "unknown field", itu perilaku lebih baik (fail loud) — catat perilaku aktual yang terjadi |

## 2. Neraca (Balance Sheet) Per 31 Desember 2026

| Skenario | Payload kunci                                          | Hasil                                                                                                                                                                                                                                                                                                                           |
| -------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST reports/balance-sheet {as_of_date:"2026-12-31"}` | Aset = AST-01 (83.000.000) + AST-02 (135.000.000) + AST-03 (30.000.000) = **248.000.000**; Liabilitas = LIA-01 = **10.000.000**; Ekuitas = EKT-01 (70.000.000) + EKT-02 (100.000.000) + EKT-03 (68.000.000, hasil closing) = **238.000.000**; Liabilitas + Ekuitas = 10.000.000 + 238.000.000 = **248.000.000** = Total Aset ✅ |

## 3. Laba Rugi (Income Statement) Konsolidasi Tahun Berjalan

Setelah closing FY2026 di file 03, saldo Pendapatan/Beban sudah di-nol-kan — laporan Laba Rugi "per tanggal setelah closing" akan menampilkan nol untuk seluruh tahun yang sudah ditutup. Untuk melihat aktivitas Januari 2026 SEBELUM closing, jalankan laporan ini di file 03 sebelum §5 (Close Fiscal Year) dijalankan, atau gunakan rentang tanggal yang jatuh di periode yang belum closed.

| Skenario                                                                               | Payload kunci                                                                  | Hasil                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — sebelum FY ditutup (urutan disarankan: jalankan test ini SEBELUM file 03 §5) | `POST reports/income-statement {date_from:"2026-01-01", date_to:"2026-01-31"}` | Pendapatan 100.000.000 (50jt+40jt+10jt) − Beban 32.000.000 (15jt+12jt+5jt) = Net Income **68.000.000** — cocok dengan perhitungan manual di file [`01` Ringkasan](./01-jurnal-hibah-dan-fund-accounting.id.md#ringkasan-saldo-akun-kunci-setelah-file-01-baseline-untuk-file-02-06) |
| Positif — sesudah FY ditutup                                                           | `POST reports/income-statement {date_from:"2026-01-01", date_to:"2026-12-31"}` | Net Income **0** (Pendapatan & Beban sudah dipindahkan ke EKT-03 lewat closing entry) — INI PERILAKU BENAR, bukan bug, tapi mudah membingungkan kalau tidak tahu closing sudah jalan                                                                                                |

## 4. Arus Kas (Cash Flow Statement)

| Skenario | Payload kunci                                                                     | Hasil                                                                                                                                                                                                                                                                                                                                                                                      |
| -------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif  | `POST reports/cash-flow-statement {date_from:"2026-01-01", date_to:"2026-01-31"}` | Seluruh transaksi file 01 adalah kas langsung (tidak ada piutang/utang bergerak di periode ini) — Kas Masuk Operasional 100.000.000 (hibah+donasi), Kas Keluar Operasional 32.000.000 (beban program), Net Cash Flow **68.000.000**, cocok dengan kenaikan saldo AST-01+AST-02 gabungan: (83.000.000−50.000.000) + (135.000.000−100.000.000) = 33.000.000 + 35.000.000 = **68.000.000** ✅ |

## Netralisasi

- Endpoint laporan bersifat read-only, tidak ada state untuk dinetralisasi.
- Kalau file 03 §5 (Close Fiscal Year) sudah dijalankan sebelum §3 di file ini dites, jalankan ulang §3 dengan rentang tanggal yang masih open, atau `reopen` periode terkait dulu.
