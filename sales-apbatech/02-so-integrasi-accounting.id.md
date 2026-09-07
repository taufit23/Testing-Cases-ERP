---
title: Test Case Sales (APBATECH) — 02. SO Terintegrasi Accounting (Invoice/Delivery → Payment → GL)
category: Sales Apbatech
description: Lanjutan SO approved file 01 ke Sales Invoice (langsung, jasa) dan Delivery→Invoice (barang, retail), Payment, dan GL untuk PT APBATECH (1 branch, dibedakan via business_unit_id).
visibility: internal
---

# 02. SO Terintegrasi Accounting (Invoice/Delivery → Payment → GL)

> Prasyarat: SO approved dari [`01-so-standalone.id.md`](./01-so-standalone.id.md). COA & saldo di [`../accounting-apbatech/00-profil-perusahaan-dan-master-data.id.md`](../accounting-apbatech/00-profil-perusahaan-dan-master-data.id.md).
>
> ✅ **Verifikasi kode**: `App\Http\Controllers\Sales\SalesInvoices` TIDAK mereferensikan `delivery_id`/`sales_delivery` sama sekali — Sales Invoice bisa dibuat **langsung dari SO** tanpa Delivery. Ini penting untuk Alur A (jasa, tidak ada barang fisik yang dikirim).

## A. Alur Jasa — Invoice Langsung dari SO, TANPA Delivery (BU-CONSULT / BU-MANAGED)

### A.1 Sales Invoice — Proyek Software Development (Milestone 2)

| Skenario              | Detail                                                                                              | Hasil                                                                                                                                                                                                                              |
| --------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif               | `create` SI langsung dari SO approved (proyek software, 45.000.000 + PPN), TANPA Delivery reference | 201, `total_amount` = 49.950.000                                                                                                                                                                                                   |
| Positif               | `submit` → `approve` SI → `export-to-journal`                                                       | Jurnal: **Debit** Piutang Usaha (AST-04), **Kredit** Pendapatan Jasa Konsultasi (PDT-01, `business_unit_id:<BU-CONSULT>`) + PPN Keluaran (LIA-02). **TIDAK ada jurnal HPP/Persediaan** — jasa tidak punya cost-of-goods di COA ini |
| Positif — GL tercatat | Cek `general-ledger/detail-ledger` AST-04/PDT-01/LIA-02 setelah export                              | Baris GL lengkap & seimbang — [[project_gl_auto_post_gap_fixed]]                                                                                                                                                                   |
| Negatif               | `export-to-journal` SI yang sudah export                                                            | Ditolak duplikat                                                                                                                                                                                                                   |
| Netralisasi           | Jangan `delete` SI yang sudah export — cek dulu belum ada Payment terkait                           |

### A.2 Sales Invoice — Managed Service Bulanan (PT Sinergi Pangan Nasional)

| Skenario    | Detail                                                                          | Hasil                                                                          |
| ----------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Positif     | `create` SI langsung dari SO managed-service (12.000.000 + PPN), TANPA Delivery | 201, `total_amount` = 13.320.000                                               |
| Positif     | `submit` → `approve` → `export-to-journal`                                      | Jurnal: Debit AST-04, Kredit PDT-02 (`business_unit_id:<BU-MANAGED>`) + LIA-02 |
| Netralisasi | Jangan `delete` setelah export                                                  |

### A.3 Sales Payment Bill — Termin 2 Tahap (Proyek Software Development)

> Nilai kontrak proyek dibayar 2 termin: 60% di muka (sudah lewat, di luar scope test ini) dan 40% pelunasan Milestone 2. Untuk simulasi termin di dalam scope file ini, split SI Milestone 2 (49.950.000) jadi 2 Payment Bill: 60% dan 40%.

| Skenario                 | Detail                                                                                               | Hasil                                                                                                                           |
| ------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Positif — termin 1 (60%) | `create` Sales Payment Bill 29.970.000 dari SI Milestone 2, terima via Bank BCA Operasional (AST-02) | 201                                                                                                                             |
| Positif                  | `mark-received` → `export-to-journal`                                                                | Jurnal: **Debit** Bank BCA (AST-02), **Kredit** Piutang Usaha (AST-04) sebesar 29.970.000                                       |
| Positif — termin 2 (40%) | Payment Bill kedua 19.980.000, sisa pelunasan                                                        | Setelah `mark-received`, SI Milestone 2 status `paid` penuh                                                                     |
| Positif — urutan termin  | `payment-schedule`/list Payment Bill SI ini                                                          | Urut berdasarkan `bill.date` terdekat duluan, bukan urutan input DB — pola [[project_payment_bill_termin_ordering]] versi Sales |
| Netralisasi              | `cancel` Payment test — jangan `delete` kalau sudah export-to-journal                                |

## B. Alur Retail — Delivery → Invoice (BU-RETAIL)

> **Branch dan user yang sama** dengan Alur A — tidak perlu switch context apapun.

### B.1 Sales Delivery

| Skenario    | Detail                                                                                                      | Hasil                                                                                                                                           |
| ----------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `create` Delivery dari SO reseller, kirim penuh (LPT-001 5, KOM-001 10, KOM-002 8) dari Gudang Utama Retail | 201, `sku_stocks` berkurang sesuai qty                                                                                                          |
| Negatif     | `create`/`update` Delivery qty melebihi sisa SO                                                             | 422 — cek guard over-delivery (gap serupa GR over-receipt, [[project_gr_over_receipt_validation]]); kalau belum ada guard, catat sebagai temuan |
| Positif     | `submit` → `approve` Delivery                                                                               | Status `approved`, siap jadi dasar Invoice                                                                                                      |
| Netralisasi | `delete` Delivery test — cek dulu belum ada SI referensi qty ini                                            |

### B.2 Sales Invoice

| Skenario              | Detail                                                                                     | Hasil                                                                                                                                                                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif               | `create` SI dari Delivery approved, termasuk PPN Keluaran 11%                              | 201, `total_amount` = 51.500.000 + 5.665.000 = 57.165.000                                                                                                                                                                                                                             |
| Positif               | `submit` → `approve` SI → `export-to-journal`                                              | Jurnal penjualan: **Debit** Piutang Usaha (AST-04), **Kredit** Pendapatan Penjualan Barang Elektronik (PDT-03, `business_unit_id:<BU-RETAIL>`) + PPN Keluaran (LIA-02); jurnal HPP: **Debit** HPP Barang Elektronik (HPP-01), **Kredit** Persediaan Barang Dagang Elektronik (AST-05) |
| Positif — GL tercatat | Cek `general-ledger/detail-ledger` untuk AST-04/PDT-03/LIA-02/HPP-01/AST-05 setelah export | Baris GL lengkap & seimbang                                                                                                                                                                                                                                                           |
| Netralisasi           | Jangan `delete` SI yang sudah export                                                       |

### B.3 Sales Payment Bill

| Skenario    | Detail                                                                                | Hasil                                                                                  |
| ----------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Positif     | `create` Payment dari SI approved, terima penuh via Bank Mandiri Operasional (AST-03) | 201                                                                                    |
| Positif     | `mark-received` → `export-to-journal`                                                 | Jurnal: **Debit** Bank Mandiri Operasional (AST-03), **Kredit** Piutang Usaha (AST-04) |
| Netralisasi | `cancel` Payment test — jangan `delete` kalau sudah export                            |

## C. Verifikasi Akhir — Trial Balance & Laba Rugi (1 branch)

| Skenario                   | Detail                                                                                                              | Hasil                                                                                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif                    | `general-ledger/trial-balance` setelah Alur A & B selesai (1 kali panggil)                                          | Debit=Kredit; Piutang Usaha 0 kalau semua SI lunas penuh (gabungan A+B)                                                                                |
| Positif — margin BU-RETAIL | `reports/income-statement`, breakdown manual `business_unit_id:<BU-RETAIL>` via `general-ledger/summary-by-account` | Margin kotor = Pendapatan Penjualan − HPP = 51.500.000 − (5×6.500.000+10×450.000+8×550.000=32.500.000+4.500.000+4.400.000=41.400.000) = **10.100.000** |
| Netralisasi keseluruhan    | Reverse/cancel seluruh dokumen (Payment → SI → Delivery(kalau ada) → SO → Quotation) urutan mundur per alur         |

## Referensi Silang

- [`01-so-standalone.id.md`](./01-so-standalone.id.md)
- [`../purchasing-apbatech/02-po-integrasi-accounting.id.md`](../purchasing-apbatech/02-po-integrasi-accounting.id.md) — pasangan sisi Purchasing
- [`../accounting-apbatech/02-general-ledger-trial-balance-per-branch.id.md`](../accounting-apbatech/02-general-ledger-trial-balance-per-branch.id.md), [`../accounting-apbatech/04-laporan-keuangan-konsolidasi-dan-per-branch.id.md`](../accounting-apbatech/04-laporan-keuangan-konsolidasi-dan-per-branch.id.md)
- [[project_gl_auto_post_gap_fixed]], [[project_gr_over_receipt_validation]], [[project_payment_bill_termin_ordering]]
