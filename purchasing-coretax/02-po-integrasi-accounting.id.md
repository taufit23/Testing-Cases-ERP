---
title: (CORETAX) — Purchasing 02. PO Integrasi Accounting
category: purchasing-coretax
description: Goods Receipt → Purchase Invoice → Payment Bill dari PO file 01, verifikasi posting GL memakai COA mapping CORETAX (1410/2105/1424/2102/1103).
visibility: internal
---

# Purchasing CORETAX — 02. PO Integrasi Accounting

> Prasyarat: [`01`](./01-po-standalone.id.md) — PO `open`, total 5.394.600 (4.860.000 barang + 534.600 PPN Masukan), 10× `SSD-512G` + 20× `BUSI-NGK-STD`.

## 0. Verifikasi Journal Mode Sebelum Mulai

`purchase_configs.default_journal_mode = 'manual'` (lihat [file 00](./00-setup-dan-master-data-tersedia.id.md)) — kalau nilainya benar-benar `manual`, GR/PI TIDAK auto-post ke GL, harus di-export manual (`export-to-journal` atau endpoint setara). Verifikasi dulu:

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Cek mode aktif | `GET`/`POST purchasing/purchase-configs/list` | Kalau `default_journal_mode:"manual"`, set dulu ke `auto` (`PUT purchasing/purchase-configs/upsert {default_journal_mode:"auto"}`) supaya test case posting GL di bawah bisa jalan otomatis — atau kalau mau tetap `manual`, catat langkah export manual di tiap skenario |

## 1. Goods Receipt (GR)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Positif — terima penuh** | `POST purchasing/purchase-receipts/create {purchase_order_id:<PO file 01>, warehouse_id:<Gudang Cikarang>, items:[{sku_id:<SSD-512G>, qty:10},{sku_id:<BUSI-NGK-STD>, qty:20}]}` | 201, status `completed` — stock `SSD-512G` & `BUSI-NGK-STD` di Gudang Cikarang naik dari 0 → 10 & 0 → 20 |
| **Negatif — over-receipt** | GR kedua untuk PO yang sama, `qty:1` tambahan (melebihi sisa PO item, karena sudah diterima penuh) | Ditolak — validasi qty vs sisa PO item (lihat pola `project_gr_over_receipt_validation`, sudah ada di modul ini) |
| Verifikasi GL (kalau `auto` mode) | `general-ledger/detail-ledger` akun `1410` & `2105` | `Dr 1410 Persediaan Barang Dagang 4.860.000` / `Cr 2105 GR/IR Clearing 4.860.000` (barang saja, TANPA PPN — PPN baru masuk di PI) |

## 2. Purchase Invoice (PI)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Positif — PI dari GR** | `POST purchasing/purchase-invoices/create {purchase_order_id:<PO>, purchase_receipt_id:<GR>, tax_id:<PPN>}` | 201, `total:5394600`, status `unpaid` |
| Post ke GL | `PUT purchasing/purchase-invoices/post {id}` (atau via export-to-journal tergantung mode) | `Dr 2105 GR/IR Clearing 4.860.000` (menutup clearing dari GR) + `Dr 1424 PPN Masukan 534.600` = `Cr 2102 Utang Usaha 5.394.600` |
| Verifikasi saldo `2105` setelah PI | `general-ledger/summary-by-account {chart_of_account_id:<2105>}` | Net 0 — kredit dari GR (4.860.000) ditutup penuh debit dari PI (4.860.000) |
| **Negatif — PI tanpa GR saat `require_gr_for_po_close` aktif** | (opsional, karena `allow_pi_without_gr:true` sebenarnya MENGIZINKAN ini) — buat PI standalone dari PO lain tanpa GR | 201 (diizinkan) — verifikasi baris jurnal PAKAI `purchase_expense→5001` (BUKAN `gr_ir→2105`, karena tidak ada clearing untuk ditutup) sesuai `expenseFunctionality` di `JournalPostingService::buildPurchaseInvoiceFunctionalityLines()` |

## 3. Payment Bill

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Bayar PI penuh via Bank | `POST purchasing/purchase-payment-bills/create {purchase_invoice_id:<PI>, amount:5394600, payment_method:<TRF-BCA>, bank_account_id:<BCA Operasional>}` | 201, status `pending` → verifikasi apakah butuh approve terpisah sebelum posting |
| Post payment ke GL | Endpoint post/approve payment | `Dr 2102 Utang Usaha 5.394.600` / `Cr 1103 Bank 5.394.600` |
| Verifikasi PO status | `purchasing/purchase-orders/show {id}` | Status PO berubah — cek apakah otomatis `closed`/`invoiced`/`paid` setelah GR+PI+Payment lengkap (lihat pola status tambahan `partially_paid` yang pernah ditambahkan — [`project_po_partially_paid_status_added`]) |
| Verifikasi Trial Balance akhir | `accounting/general-ledger/trial-balance` per 2026-08-31 | `1410:+4.860.000`, `2105: 0 (net)`, `1424:+534.600`, `2102: 0 (net, lunas)`, `1103:−5.394.600` |

## Referensi Silang

- [`01-po-standalone.id.md`](./01-po-standalone.id.md) — sumber PO
- [`accounting-coretax/02-general-ledger-dan-trial-balance.id.md`](../accounting-coretax/02-general-ledger-dan-trial-balance.id.md) — gabungkan delta modul ini dengan delta jurnal manual kalau mau Trial Balance total gabungan
