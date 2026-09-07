---
title: (CORETAX) — Purchasing 01. PO Standalone
category: purchasing-coretax
description: Purchase Request → Purchase Quotation → Purchase Order sampai open, belum ke GR/PI/GL, memakai supplier & produk riil CORETAX.
visibility: internal
---

# Purchasing CORETAX — 01. PO Standalone

> Prasyarat: [`00`](./00-setup-dan-master-data-tersedia.id.md). Supplier **PT Sumber Makmur**, produk `SSD-512G` (480.000/pcs) & `BUSI-NGK-STD` (18.000/pcs), warehouse **Gudang Cikarang**. Pakai `accounting_period_id` Agustus 2026 (sama seperti suite `accounting-coretax`, catat `id`-nya dari `accounting-periods/list`).

## 1. Purchase Request (PR) — Restock Sparepart

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Buat PR | `POST purchasing/purchase-requests/create {date:"2026-08-15", warehouse_id:<Gudang Cikarang>, items:[{sku_id:<SSD-512G>, qty:10},{sku_id:<BUSI-NGK-STD>, qty:20}]}` | 201, status `draft` |
| **Negatif — submit tanpa approval dulu langsung ke PO** | Coba lompat ke PO tanpa approve PR | Cek behavior: karena `require_pr_approval:true`, apakah PO create nolak referensi PR yang belum approved, atau PR cuma rekomendasi (tidak benar-benar gating PO create) — dokumentasikan mana yang benar |
| Submit PR | `POST purchasing/purchase-requests/submit {id}` | Status → `JRN_PENDING_REVIEW`-setara (cek nama status approval PR yang sebenarnya) |
| Approve PR | `POST purchasing/purchase-requests/approve {id}` | Status → `approved` (atau setara) |

## 2. Purchase Quotation (PQ) — Opsional (karena `require_pq_before_po:false`)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Buat PQ dari PR, ke 1 supplier | `POST purchasing/purchase-quotations/create {purchase_request_id:<PR di atas>, contact_id:<PT Sumber Makmur>, items:[...]}` | 201 — cukup 1 supplier karena `min_quotation_suppliers:1` |
| Supplier respon harga | Update PQ dengan harga quoted: `SSD-512G` 480.000/pcs, `BUSI-NGK-STD` 18.000/pcs (samakan dengan price list default supaya perhitungan konsisten) | — |
| Approve PQ | `POST purchasing/purchase-quotations/approve {id}` | Status `approved` (wajib, `require_pq_approval:true`) |
| Pilih PQ ini untuk jadi PO | Tandai `selected` | — |

## 3. Purchase Order (PO)

Total barang: (10×480.000) + (20×18.000) = 4.800.000 + 360.000 = **4.860.000**. PPN 11% = **534.600**. Total PO = **5.394.600**.

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Positif — PO dari PQ terpilih** | `POST purchasing/purchase-orders/create {purchase_quotation_id:<PQ>, contact_id:<PT Sumber Makmur>, date:"2026-08-16", accounting_period_id:<Agustus 2026>, items:[{sku_id:<SSD-512G>, qty:10, price:480000},{sku_id:<BUSI-NGK-STD>, qty:20, price:18000}], tax_id:<PPN>}` | 201, status langsung **`open`** (bukan draft, lihat file 00), `total_amount:5394600` |
| **Positif — PO standalone TANPA PQ** (verifikasi `require_pq_before_po:false`) | PO baru, langsung `contact_id` + `items` tanpa `purchase_quotation_id` | 201 juga berhasil — kalau ternyata ditolak, itu berarti flag `require_pq_before_po` tidak benar-benar dihormati (temuan) |
| **Negatif — qty 0** | Salah satu item `qty:0` | Ditolak validasi |
| **Negatif — supplier tidak match currency** | (skip kalau semua currency IDR — tidak relevan untuk CORETAX karena tidak ada exchange rate aktif, lihat gap di `accounting-coretax/00` §18) | — |
| Netralisasi | Reverse/cancel PO test kedua (standalone) kalau tidak dipakai lanjut ke file `02` | — |

## Ringkasan untuk File 02

PO dari PQ (skenario Positif pertama) dipakai lanjut ke `02-po-integrasi-accounting.id.md` — Total **5.394.600** (4.860.000 barang + 534.600 PPN Masukan).

## Referensi Silang

- [`00-setup-dan-master-data-tersedia.id.md`](./00-setup-dan-master-data-tersedia.id.md)
- [`02-po-integrasi-accounting.id.md`](./02-po-integrasi-accounting.id.md) — GR → PI → Payment dari PO ini
