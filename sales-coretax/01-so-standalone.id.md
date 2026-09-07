---
title: (CORETAX) — Sales 01. SO Standalone
category: sales-coretax
description: Quotation → Sales Order sampai approved, belum ke Delivery/SI/GL, memakai customer & produk riil CORETAX.
visibility: internal
---

# Sales CORETAX — 01. SO Standalone

> Prasyarat: [`00`](./00-setup-dan-master-data-tersedia.id.md) — akun `2191`/`4002` dibuat, `sales_configs` sudah di-upsert. Customer **PT Cahaya Abadi Sejahtera**, produk `SSD-512G` (jual 650.000) & `BUSI-NGK-STD` (jual 25.000). `accounting_period_id` Agustus 2026 (sama seperti suite lain).

## 1. Quotation

Subtotal: (4×650.000) + (15×25.000) = 2.600.000 + 375.000 = **2.975.000**. PPN 11% = **327.250**. Total = **3.302.250**.

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Buat Quotation | `POST sales/quotations/create {date:"2026-08-18", contact_id:<PT Cahaya Abadi Sejahtera>, items:[{sku_id:<SSD-512G>, qty:4, price:650000},{sku_id:<BUSI-NGK-STD>, qty:15, price:25000}], tax_id:<PPN>}` | 201, status `draft`, `total:3302250` |
| Kirim ke customer | `POST sales/quotations/... sent` (cek nama action pasti) | Status `sent` |
| Customer terima | Update status `accepted` | Status `accepted` |

## 2. Sales Order (SO)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Positif — SO dari Quotation** | `POST sales/sales-orders/create {quotation_id:<Quotation di atas>, contact_id:<PT Cahaya Abadi Sejahtera>, accounting_period_id:<Agustus 2026>}` | 201, status langsung **`open`** (mirror pola PO, bukan draft — lihat `SalesStatusSeeder::DEFAULT_CODE_PER_MODULE`) |
| Submit approval (karena `require_so_approval:true` dari setup file 00) | `POST sales/sales-orders/submit {id}` | Cek status approval workflow |
| Approve | `POST sales/sales-orders/approve {id}` | Status `approved` |
| **Negatif — SO tanpa Quotation, `require_quotation_for_so` dicek dulu** | Cek nilai `require_quotation_for_so` di sales_configs (default belum di-set eksplisit di file 00 §Langkah 2 — kemungkinan `false`/null) — kalau `false`, SO standalone tanpa quotation harus BERHASIL | Dokumentasikan hasil aktual, jangan asumsikan |

## 3. Skenario Diskon (verifikasi terpisah, TIDAK dibawa ke file 02)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Quotation baru dengan diskon `NEWCUST10` | Sama items di atas + `discount_code:"NEWCUST10"` | Subtotal 2.975.000 × 10% = 297.500, TAPI `max_discount_amount:200.000` untuk kode ini → **diskon ter-cap di 200.000**, bukan 297.500. Verifikasi cap ini benar-benar diterapkan (jangan asumsikan, banyak sistem lupa apply cap) |
| **Negatif — diskon kadaluarsa** | Pakai kode `LEBARAN2026` (`is_active:false`) | Ditolak — kode tidak aktif |
| Netralisasi | Hapus quotation percobaan ini, tidak dilanjut ke SO | — |

## Ringkasan untuk File 02

SO dari Quotation utama (§2, tanpa diskon) — Total **3.302.250** (2.975.000 barang + 327.250 PPN Keluaran) — dipakai lanjut ke `02-so-integrasi-accounting.id.md`.

## Referensi Silang

- [`00-setup-dan-master-data-tersedia.id.md`](./00-setup-dan-master-data-tersedia.id.md)
- [`02-so-integrasi-accounting.id.md`](./02-so-integrasi-accounting.id.md)
