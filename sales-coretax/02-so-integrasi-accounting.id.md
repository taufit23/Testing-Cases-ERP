---
title: (CORETAX) — Sales 02. SO Integrasi Accounting
category: sales-coretax
description: Sales Delivery → Sales Invoice → Payment Bill dari SO file 01, verifikasi posting GL (AR, Penjualan, PPN Keluaran) dan verifikasi eksplisit TIDAK ada posting HPP otomatis.
visibility: internal
---

# Sales CORETAX — 02. SO Integrasi Accounting

> Prasyarat: [`01`](./01-so-standalone.id.md) — SO `approved`, total 3.302.250 (2.975.000 barang + 327.250 PPN Keluaran), 4× `SSD-512G` + 15× `BUSI-NGK-STD`. **Stock kedua SKU ini harus sudah ada dari [`purchasing-coretax/02`](../purchasing-coretax/02-po-integrasi-accounting.id.md)** (10 & 20 pcs masuk via GR).

## 1. Sales Delivery — TIDAK Menyentuh GL

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Positif — kirim penuh** | `POST sales/sales-deliveries/create {sales_order_id:<SO file 01>, warehouse_id:<Gudang Cikarang>, items:[{sku_id:<SSD-512G>, qty:4},{sku_id:<BUSI-NGK-STD>, qty:15}]}` | 201, status `completed`. Stock `SSD-512G` 10→6, `BUSI-NGK-STD` 20→5 |
| **Verifikasi — TIDAK ada entri GL dari Delivery** | `general-ledger/detail-ledger` akun `1410` (Persediaan) tepat setelah Delivery ini, SEBELUM Invoice dibuat | Ekspektasi: **TIDAK ADA baris baru** di `1410` dari Delivery ini — kontras dengan Purchasing GR yang justru posting `1410` (lihat [temuan](../../TemuanTestCase/Sales/CoretaxCompany/02-tidak-ada-posting-hpp-otomatis.id.md)). Kalau ternyata ADA baris, berarti temuan ini salah — koreksi |
| **Negatif — over-delivery** | Delivery kedua untuk SO yang sama, qty melebihi sisa SO item | Ditolak — validasi qty vs sisa SO item |

## 2. Sales Invoice (SI)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Positif — SI dari Delivery** | `POST sales/sales-invoices/create {sales_order_id:<SO>, sales_delivery_id:<Delivery>, tax_id:<PPN>}` | 201, `total:3302250`, status `unpaid` |
| Post ke GL | `PUT sales/sales-invoices/post {id}` (mode `auto` dari setup file 00 §Langkah 2) | `Dr 1121 Piutang Usaha 3.302.250` = `Cr 4001 Penjualan 2.975.000` + `Cr 2191 PPN Keluaran 327.250` — **HANYA 3 baris ini, TIDAK ADA baris `1410`/HPP** |
| **Verifikasi HPP tetap tidak muncul** | Cek ulang `1410` setelah SI posted | Masih tidak berubah — kalau test case butuh HPP tercermin di Laba Rugi, WAJIB jurnal manual terpisah: `Dr 5008/5009 xxx / Cr 1410 xxx` sebesar harga pokok (4×480.000 + 15×18.000 = 1.920.000+270.000=2.190.000) — opsional, dokumentasikan sebagai langkah tambahan bukan default |

## 3. Payment Bill

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Terima pembayaran penuh via Bank | `POST sales/sales-payment-bills/create {sales_invoice_id:<SI>, amount:3302250, payment_method:<TRF-BCA>, bank_account_id:<BCA Operasional>}` | 201 |
| Post ke GL | Endpoint post/approve payment | `Dr 1103 Bank 3.302.250` / `Cr 1121 Piutang Usaha 3.302.250` — saldo `1121` dari SO ini net kembali 0 |

## 4. Sales Return (opsional, verifikasi akun `4002`)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Retur 2 pcs `BUSI-NGK-STD` (customer komplain) | `POST sales/sales-returns/create {sales_invoice_id:<SI>, items:[{sku_id:<BUSI-NGK-STD>, qty:2}]}` | Nilai retur = 2×25.000 = 50.000 (tanpa PPN di baris ini — cek apakah PPN ikut di-retur proporsional atau tidak, dokumentasikan) |
| Post ke GL | — | `Dr 4002 Retur Penjualan 50.000` / `Cr 1121 Piutang Usaha 50.000` (lihat `buildSalesReturnFunctionalityLines()` — cuma 2 baris, TANPA reversal HPP karena memang tidak pernah ada HPP yang diakui di awal) |

## Ringkasan Akhir Suite `sales-coretax`

| Akun | Delta |
| --- | ---: |
| `1121` Piutang Usaha | +3.302.250 (SI) − 3.302.250 (Payment) − 50.000 (Return) = **−50.000** |
| `4001` Penjualan | +2.975.000 |
| `2191` PPN Keluaran | +327.250 |
| `1103` Bank | +3.302.250 |
| `4002` Retur Penjualan | +50.000 |
| `1410` Persediaan | **0 (tidak tersentuh sama sekali, lihat temuan HPP)** |

## Referensi Silang

- [`01-so-standalone.id.md`](./01-so-standalone.id.md)
- [`purchasing-coretax/02-po-integrasi-accounting.id.md`](../purchasing-coretax/02-po-integrasi-accounting.id.md) — sumber stock yang dijual di sini
- [`TemuanTestCase/Sales/CoretaxCompany/`](../../TemuanTestCase/Sales/CoretaxCompany/) — detail gap `sales_configs` & HPP
