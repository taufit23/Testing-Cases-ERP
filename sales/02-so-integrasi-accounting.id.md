---
title: Test Case Sales — 02. SO Terintegrasi Accounting (Delivery → SI → Payment → GL)
category: Testing
description: Lanjutan SO approved dari file 01 ke Sales Delivery, Sales Invoice, Sales Payment Bill, dan verifikasi posting ke General Ledger (AR control account, PPN Keluaran, HPP).
visibility: internal
---

# 02. SO Terintegrasi Accounting (Delivery → SI → Payment → GL)

> Prasyarat: SO approved dari [`01-so-standalone.id.md`](./01-so-standalone.id.md). Skenario & COA sama seperti [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md).
>
> Fokus: setiap dokumen turunan SO memposting jurnal benar — Piutang Dagang (1103), PPN Keluaran (2102), Penjualan (4101), dan HPP (5101) vs Persediaan (1104) saat barang keluar.

## 1. Sales Delivery (**Sales Deliveries**)

| Skenario                     | Detail                                                                          | Hasil                                                                                          |
| -------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Positif                        | `create` Delivery dari SO, kirim penuh (Minyak 100, Gula 60)                        | 201                                                                                                |
| Negatif                        | `create`/`update` Delivery qty melebihi sisa SO                                     | 422 — cek apakah guard over-delivery sudah ada (gap serupa GR over-receipt, [[project_gr_over_receipt_validation]]); kalau belum ada, catat sebagai temuan |
| Positif                        | `submit` → `approve` Delivery                                                       | Status `approved`, siap jadi dasar Invoice                                                        |
| Netralisasi                    | `delete` Delivery test — cek dulu belum ada SI yang reference qty ini               |

## 2. Sales Invoice (**Sales Invoices**)

| Skenario                              | Detail                                                                                       | Hasil                                                                                                             |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Positif                                | `create` SI dari Delivery approved, termasuk PPN Keluaran 11%                                       | 201, `total_amount` = subtotal jual + PPN Keluaran (akun 2102)                                                          |
| Positif                                | `submit` → `approve` SI → `export-to-journal`                                                       | Jurnal penjualan: **Debit** Piutang Dagang (1103), **Kredit** Penjualan (4101) + PPN Keluaran (2102); jurnal HPP: **Debit** HPP (5101), **Kredit** Persediaan (1104) |
| **Positif — GL benar-benar tercatat**  | Cek `accounting/general-ledger` untuk 1103/4101/2102/5101/1104 setelah export                       | Baris GL lengkap & seimbang — regression check [[project_gl_auto_post_gap_fixed]]                                       |
| Negatif                                | `export-to-journal` SI yang sudah pernah export                                                     | Ditolak duplikat                                                                                                          |
| Netralisasi                            | Jangan `delete` SI yang sudah export — cek dulu belum ada Payment terkait                            |

## 3. Sales Payment Bill (**Sales Payment Bills**)

| Skenario                        | Detail                                                                                | Hasil                                                                                       |
| ----------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Positif                           | `create` Payment dari SI approved, terima penuh via Bank BCA                                | 201                                                                                                 |
| Positif                           | `mark-received` → `export-to-journal`                                                        | Jurnal: **Debit** Bank BCA (1102), **Kredit** Piutang Dagang (1103)                                 |
| Positif — termin (opsional)       | 2 Payment parsial (60%+40%) untuk 1 SI                                                       | Urutan termin sesuai tanggal terdekat duluan, konsisten dengan pola [[project_payment_bill_termin_ordering]] (versi Sales) |
| Netralisasi                       | `cancel` Payment test — jangan `delete` kalau sudah export-to-journal                        |

## 4. Verifikasi Akhir

| Skenario                | Detail                                                                                     | Hasil                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Positif                   | `accounting/reports/trial-balance` setelah alur Delivery→SI→Payment selesai                  | Debit=Kredit; Piutang Dagang balik ke 0 kalau lunas; Persediaan turun sesuai qty terjual                    |
| Positif                   | `accounting/reports/income-statement` (Laba Rugi)                                            | Penjualan (4101) dan HPP (5101) periode ini muncul benar, margin kotor = Penjualan − HPP sesuai perhitungan manual |
| Positif                   | `accounting/reports/ar-aging` (kalau sudah digarap — lihat [`../_deferred-integrated/06-piutang-dan-utang-aging.id.md`](../_deferred-integrated/06-piutang-dan-utang-aging.id.md)) | SI belum lunas muncul dengan umur piutang benar                                                             |
| Netralisasi keseluruhan  | Reverse/cancel seluruh dokumen (Payment → SI → Delivery → SO → Quotation) urutan mundur, cek GL balik bersih |

## Referensi Silang

- [`01-so-standalone.id.md`](./01-so-standalone.id.md) — tahap sebelum Delivery
- [`../purchasing/02-po-integrasi-accounting.id.md`](../purchasing/02-po-integrasi-accounting.id.md) — pasangan sisi Purchasing (pola sama, akun berlawanan)
- [`../accounting/02-general-ledger-neraca-saldo.id.md`](../accounting/02-general-ledger-neraca-saldo.id.md), [`../accounting/04-laporan-keuangan.id.md`](../accounting/04-laporan-keuangan.id.md)
- [[project_gl_auto_post_gap_fixed]], [[project_gr_over_receipt_validation]]
