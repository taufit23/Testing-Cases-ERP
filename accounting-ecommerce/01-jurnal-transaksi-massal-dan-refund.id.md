---
title: (E-commerce) — 01. Jurnal Transaksi Massal & Refund
category: accounting-ecommerce
description: Create/post jurnal manual satuan dan massal (create-bulk), potongan payment gateway, refund/retur, dimensi Business Unit per channel — endpoint accounting/journals/*.
visibility: internal
---

# 01. Jurnal Transaksi Massal & Refund

> **Ciri Khas Skenario**: Volume transaksi tinggi (pakai **Journals — `create-bulk`**), potongan payment gateway, retur/refund pelanggan, dimensi Business Unit per channel.
> **Prasyarat**: Master data file `00` (COA, Business Unit CHN-WEB/CHN-MP, Fiscal Year FY2026 + periode Januari 2026 sudah di-generate).
> **Penting**: **Journals — `create`** HANYA membuat jurnal berstatus draft/balanced-awaiting-post (atau `JRN_PENDING_REVIEW` kalau approval flag branch ini ON — default OFF). Jurnal baru benar-benar **terposting ke GL** setelah dipanggil eksplisit `PUT accounting/journals/post` (atau `post-bulk`). "Jurnal terposting" bukan hasil otomatis dari `create`.

## 1. Rekap Penjualan Web (T1)

Dr Saldo Payment Gateway (AST-02) 22.200.000
Cr Pendapatan Penjualan E-commerce (PDT-01) 20.000.000
Cr PPN Keluaran (LIA-02) 2.200.000 (11% × 20.000.000)
Total Debit = Total Kredit = **22.200.000** ✓. Dimensi (`business_unit_id`) = CHN-WEB pada baris AST-02 dan PDT-01.

## 2. Potongan Admin Payment Gateway (T2)

Dr Beban Biaya Admin PG & MP (BBN-02) 300.000
Cr Saldo Payment Gateway (AST-02) 300.000
Total = **300.000** ✓. Dimensi CHN-WEB.

## 3. Refund Pelanggan (T3)

Dr Retur & Potongan Penjualan (PDT-02) 1.000.000
Dr PPN Keluaran (LIA-02) 110.000 (mengoreksi output tax yang sudah terlanjur diakui di T1)
Cr Saldo Payment Gateway (AST-02) 1.110.000
Total Debit = 1.000.000 + 110.000 = **1.110.000** = Total Kredit ✓. Dimensi CHN-WEB.

## 4. Rekap Penjualan Marketplace, batch harian (T4 — `create-bulk`)

Jurnal terpisah untuk channel Marketplace, dikirim dalam SATU call `accounting/journals/create-bulk` bersama T1 (2 jurnal sekaligus, mensimulasikan rekap harian multi-channel):

Dr Saldo Marketplace (AST-03) 33.300.000
Cr Pendapatan Penjualan E-commerce (PDT-01) 30.000.000
Cr PPN Keluaran (LIA-02) 3.300.000
Total = **33.300.000** ✓. Dimensi CHN-MP.

## Skenario Pengujian

| Skenario | Detail                                                                                         | Hasil                                                                                                                                                                                                                                                                                                                                  |
| -------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `accounting/journals/create` — T1 (2 baris kredit, dimensi CHN-WEB di baris pendapatan & PG).  | 201, jurnal terbuat, status draft/balanced-awaiting-post (BUKAN posted — `posted_at` masih null).                                                                                                                                                                                                                                      |
| Positif  | `PUT accounting/journals/post` untuk T1.                                                       | 200, `posted_at` terisi, GL entries tertulis (3 baris: 1 debit AST-02, 2 kredit PDT-01 & LIA-02).                                                                                                                                                                                                                                      |
| Positif  | `accounting/journals/create-bulk` mengirim T1 + T4 (Website & Marketplace) sekaligus.          | 201, 2 jurnal terbuat sekaligus dengan `code` masing-masing unik & tidak boleh sama (`journals.*.code` wajib `distinct` dalam 1 batch).                                                                                                                                                                                                |
| Positif  | `PUT accounting/journals/post-bulk` dengan `ids` dari 2 jurnal T1+T4.                          | 200, kedua jurnal terposting sekaligus, GL bertambah 6 baris total.                                                                                                                                                                                                                                                                    |
| Positif  | T2 (potongan admin PG) create lalu post.                                                       | 201 → 200, GL: Dr BBN-02 300.000 / Cr AST-02 300.000.                                                                                                                                                                                                                                                                                  |
| Positif  | T3 (refund, 2 baris debit) create lalu post.                                                   | 201 → 200, GL 3 baris: Dr PDT-02 1.000.000, Dr LIA-02 110.000, Cr AST-02 1.110.000.                                                                                                                                                                                                                                                    |
| Negatif  | Create jurnal dengan `lines` total Dr ≠ total Cr (mis. Dr 22.200.000 tapi Cr cuma 20.000.000). | 201 tetap dibuat (bukan ditolak!) TAPI otomatis mengendap di status draft ("belum balance") — TIDAK pernah diajukan ke approval/GL. `post` terhadap jurnal ini akan tetap sukses menulis GL yang TIDAK balance kalau dipaksa, karena `post()` tidak mem-validasi ulang balance — jangan panggil `post` pada jurnal yang belum balance. |
| Negatif  | `create` dengan `lines` kurang dari 2 baris.                                                   | 422 — `lines` minimal 2.                                                                                                                                                                                                                                                                                                               |
| Negatif  | `create` dengan `code` yang sudah dipakai jurnal lain di branch yang sama.                     | 422 — pesan `content.journal_code_already_used`.                                                                                                                                                                                                                                                                                       |
| Negatif  | Refund (T3) melebihi saldo Payment Gateway yang tersisa.                                       | **Bukan ditolak** — sistem TIDAK memvalidasi saldo akun (`chart_of_accounts_balances`/running GL balance) sebelum posting jurnal manual. Selama Dr=Cr, jurnal manual apa pun akan sukses diposting walau membuat AST-02 bersaldo negatif secara akuntansi. Ini gap yang harus didokumentasikan, BUKAN diasumsikan tervalidasi.         |
| Negatif  | `post` jurnal yang sama dua kali.                                                              | 422 — `content.journal_already_posted`.                                                                                                                                                                                                                                                                                                |
| Negatif  | `reverse` jurnal yang belum pernah di-post.                                                    | 422 — `content.journal_not_posted`.                                                                                                                                                                                                                                                                                                    |

## Netralisasi

- `POST accounting/journals/reverse` untuk setiap jurnal yang sudah di-post (T1, T2, T3, T4) — membuat jurnal kontra baru (additive, TIDAK menghapus baris GL asli) sehingga net per akun kembali ke 0.
- Jurnal yang masih draft (belum posted) boleh langsung `DELETE accounting/journals/delete`.
