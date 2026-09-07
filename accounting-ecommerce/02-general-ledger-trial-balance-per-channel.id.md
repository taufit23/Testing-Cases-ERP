---
title: (E-commerce) — 02. General Ledger & Trial Balance per Channel
category: accounting-ecommerce
description: Detail Ledger, Summary by Account (dengan filter dimensi Business Unit/channel), dan Trial Balance konsolidasi — endpoint accounting/general-ledger/*.
visibility: internal
---

# 02. General Ledger & Trial Balance per Channel

> **Prasyarat**: File `00` (master data) dan `01` (T1-T4 sudah di-create DAN di-post, sehingga GL terisi) sudah dikerjakan.
> **Penting soal dimensi channel**: filter `business_unit_id` HANYA tersedia di **General Ledger — `detail-ledger`** dan **General Ledger — `summary-by-account`** (lihat `App\Http\Controllers\Accounting\GeneralLedger`). Endpoint **General Ledger — `trial-balance`** **TIDAK menerima parameter `business_unit_id` sama sekali** — Trial Balance di sistem ini selalu konsolidasi seluruh channel, bukan per-channel. Kalau butuh breakdown per channel, pakai `summary-by-account` dengan `business_unit_id` per akun, bukan `trial-balance`.

## Trial Balance Konsolidasi per akhir Januari 2026 (hasil posting T1-T4 + saldo awal file 00)

| Akun                            |           Debit |          Kredit |
| ------------------------------- | --------------: | --------------: |
| AST-01 Bank BCA Operasional     |     200.000.000 |                 |
| AST-02 Saldo Payment Gateway    |      35.790.000 |                 |
| AST-03 Saldo Marketplace        |      68.300.000 |                 |
| AST-04 Piutang COD              |       8.000.000 |                 |
| AST-05 Persediaan Barang Dagang |     120.000.000 |                 |
| LIA-01 Utang Dagang             |                 |      45.000.000 |
| LIA-02 PPN Keluaran             |                 |       5.390.000 |
| EKT-01 Modal Pemilik            |                 |     333.000.000 |
| PDT-01 Pendapatan Penjualan     |                 |      50.000.000 |
| PDT-02 Retur & Potongan         |       1.000.000 |                 |
| BBN-02 Beban Admin PG & MP      |         300.000 |                 |
| **Total**                       | **433.390.000** | **433.390.000** |

Perhitungan AST-02 (Saldo Payment Gateway): opening 15.000.000 + T1 Dr 22.200.000 − T2 Cr 300.000 − T3 Cr 1.110.000 = **35.790.000**.
Perhitungan AST-03: opening 35.000.000 + T4 Dr 33.300.000 = **68.300.000**.
Perhitungan LIA-02 (PPN Keluaran): T1 Cr 2.200.000 + T4 Cr 3.300.000 − T3 Dr 110.000 = **5.390.000** (kredit/liability bertambah).
Perhitungan PDT-01: T1 Cr 20.000.000 + T4 Cr 30.000.000 = **50.000.000**.

## Breakdown per Channel (via `summary-by-account` + `business_unit_id`)

| Channel              |                                                 AST-02/AST-03 (kas channel) | PDT-01 Pendapatan |                           LIA-02 PPN Keluaran |  PDT-02 Retur |      BBN-02 |
| -------------------- | --------------------------------------------------------------------------: | ----------------: | --------------------------------------------: | ------------: | ----------: |
| CHN-WEB (Website)    | AST-02: Dr 22.200.000, Cr 1.410.000 (netto Dr 20.790.000 aktivitas periode) |     Cr 20.000.000 | Cr 2.200.000, Dr 110.000 (netto Cr 2.090.000) |  Dr 1.000.000 |  Dr 300.000 |
| CHN-MP (Marketplace) |                                                       AST-03: Dr 33.300.000 |     Cr 30.000.000 |                                  Cr 3.300.000 |             — |           — |
| **Total**            |                                                54.090.000 aktivitas periode |    **50.000.000** |                                 **5.390.000** | **1.000.000** | **300.000** |

Total kedua channel untuk PDT-01 = 20.000.000 + 30.000.000 = 50.000.000, cocok dengan Trial Balance konsolidasi — verifikasi silang wajib dilakukan tiap kali sebelum mendokumentasikan angka breakdown per channel.

## Skenario Pengujian

| Skenario | Detail                                                                                                                        | Hasil                                                                                                                                                                                                                       |
| -------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `accounting/general-ledger/trial-balance` dengan `accounting_period_id` = Januari 2026.                                       | 200, daftar semua akun dengan `opening_debit/credit`, `period_debit/credit`, `closing_debit/credit` — total closing_debit = total closing_credit = 433.390.000, TIDAK ada filter channel di response ini.                   |
| Positif  | `accounting/general-ledger/summary-by-account` dengan `business_unit_id` = CHN-WEB.                                           | 200, hanya menjumlahkan baris GL yang `business_units_id` = CHN-WEB (AST-02 sebagian, PDT-01 20.000.000, LIA-02 sebagian, PDT-02, BBN-02).                                                                                  |
| Positif  | `accounting/general-ledger/summary-by-account` dengan `business_unit_id` = CHN-MP.                                            | 200, hanya AST-03 & baris T4 (PDT-01 30.000.000, LIA-02 3.300.000).                                                                                                                                                         |
| Positif  | `accounting/general-ledger/detail-ledger` dengan `chart_of_account_id` = AST-02, tanpa `business_unit_id`.                    | 200, `opening_debit` 15.000.000, lalu 3 baris (T1, T2, T3) dengan `running_debit`/`running_credit` berjalan, `closing_debit` net 35.790.000 (setelah dikurangi credit).                                                     |
| Positif  | `accounting/general-ledger/list` dengan `date_from`/`date_to` Januari 2026.                                                   | 200, menampilkan seluruh baris GL bulan tsb (opening balance + T1-T4), terurut `trans_date` DESC.                                                                                                                           |
| Negatif  | `trial-balance` dikirim dengan payload `business_unit_id` (mengira endpoint ini mendukung filter channel seperti suite lain). | Parameter diabaikan (bukan error 422) — endpoint ini memang tidak mem-validasi/membaca `business_unit_id` sama sekali, hasilnya tetap konsolidasi semua channel. Jangan salah baca "tidak error" sebagai "filter berhasil". |
| Negatif  | `detail-ledger`/`summary-by-account` dengan `date_to` sebelum `date_from`.                                                    | 422 — `date_to` harus `after_or_equal:date_from`.                                                                                                                                                                           |
| Negatif  | `summary-by-account` dengan `chart_of_account_id` yang tidak ada di branch aktif.                                             | 422 — `chart_of_account_id` tidak ditemukan (`exists:chart_of_accounts,id` gagal).                                                                                                                                          |

## Netralisasi

- Tidak ada perubahan state di file ini (semua endpoint read-only). Kalau perlu reset, reverse jurnal T1-T4 seperti di file `01`.
