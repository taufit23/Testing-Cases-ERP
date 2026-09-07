---
title: (Nonprofit / NGO) — 02. General Ledger & Trial Balance per Program
category: accounting-ngo
description: Detail Ledger, Summary by Account, dan Trial Balance dengan filter dimensi Business Unit (Program) — endpoint nyata di modul accounting/general-ledger.
visibility: internal
---

# 02. General Ledger & Trial Balance per Program

> Prasyarat: [`01-jurnal-hibah-dan-fund-accounting.id.md`](./01-jurnal-hibah-dan-fund-accounting.id.md) sudah posted (§1.1-1.6), jurnal §1.7 sudah direverse. Endpoint: **General Ledger — `{action}`** — `detail-ledger`, `summary-by-account`, `by-account`, `trial-balance`. Hanya endpoint di modul **General Ledger** yang mendukung filter `business_unit_id`; endpoint `reports/*` (balance-sheet, income-statement, cash-flow-statement) **TIDAK** mendukung filter ini (lihat catatan penting di file [`04`](./04-laporan-keuangan-aktivitas-per-program.id.md)).

## 1. Trial Balance Konsolidasi (Tanpa Filter)

| Skenario | Payload kunci                                                            | Hasil                                                                                                                                                                                                  |
| -------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif  | `POST accounting/general-ledger/trial-balance {as_of_date:"2026-01-31"}` | Total Debit = Total Kredit = **280.000.000** (lihat rincian di [file 01, Ringkasan](./01-jurnal-hibah-dan-fund-accounting.id.md#ringkasan-saldo-akun-kunci-setelah-file-01-baseline-untuk-file-02-06)) |

## 2. Trial Balance / Summary per Program (Filter `business_unit_id`)

| Skenario                                          | Payload kunci                                                                    | Hasil                                                                                                                                                                  |
| ------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — Program Pendidikan Anak                 | `POST accounting/general-ledger/summary-by-account {business_unit_id:<PRG-EDU>}` | Hanya baris dengan dimensi PRG-EDU: AST-02 (debit 50jt, kredit 15jt), PDT-01 (kredit 50jt), BBN-01 (debit 15jt) — net PDT-01 − BBN-01 = **35.000.000** surplus program |
| Positif — Program Bantuan Bencana                 | `POST accounting/general-ledger/summary-by-account {business_unit_id:<PRG-DIS>}` | AST-01 (debit 40jt, kredit 12jt), PDT-02 (kredit 40jt), BBN-02 (debit 12jt) — net **28.000.000** surplus program                                                       |
| Positif — Operasional Umum                        | `POST accounting/general-ledger/summary-by-account {business_unit_id:<PRG-GEN>}` | AST-01 (debit 10jt, kredit 5jt), PDT-03 (kredit 10jt), BBN-03 (debit 5jt) — net **5.000.000** surplus                                                                  |
| Positif — cek total 3 program = total konsolidasi | Jumlahkan net 3 program: 35.000.000 + 28.000.000 + 5.000.000 = **68.000.000**    | Harus sama dengan (Total Pendapatan 100.000.000 − Total Beban 32.000.000) = **68.000.000** dari trial balance konsolidasi §1 ✅                                        |

## 3. Detail Ledger per Akun Bank

| Skenario | Payload kunci                                                                                                      | Hasil                                                                                                                                                                                                                                                                                        |
| -------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/detail-ledger {account_id:<AST-02>, date_from:"2026-01-01", date_to:"2026-01-31"}` | 3 baris: saldo awal 100.000.000 → +50.000.000 (§1.1) → −15.000.000 (§1.4) → running balance akhir **135.000.000**. Kalau jurnal §1.7 belum direverse tuntas saat query ini dijalankan, akan muncul baris ke-4 (−3.000.000) yang TIDAK sesuai baseline — konfirmasi dulu file 01 sudah bersih |

## 4. Filter Dimensi pada Akun yang Tidak Punya Transaksi per Program (Negatif/Edge)

| Skenario     | Payload kunci                                                                                                                                                                                   | Hasil                                                                                                                        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Negatif/edge | `POST accounting/general-ledger/summary-by-account {business_unit_id:<PRG-DIS>, account_id:<AST-02>}` (Bank Donor Pendidikan tidak pernah dipakai untuk dimensi PRG-DIS setelah §1.7 direverse) | Hasil kosong (array 0 baris), bukan error — pastikan endpoint tidak crash pada kombinasi filter yang tidak menghasilkan data |

## Netralisasi

- Endpoint ini read-only (query GL), tidak ada state untuk dinetralisasi.
- Kalau ada devisiasi angka dari yang diharapkan, cek dulu apakah jurnal §1.7 (file 01) benar-benar sudah direverse sebelum melapor sebagai bug.
