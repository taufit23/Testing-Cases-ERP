---
title: Test Case Purchasing — 01. Purchase Order Standalone (PR → PQ → PO)
category: Testing
description: Alur Purchase Requisition → Purchase Quotation → Purchase Order berdiri sendiri (belum sampai GR/PI/GL) untuk skenario PT Retail Nusantara Jaya.
visibility: internal
---

# 01. Purchase Order Standalone (PR → PQ → PO)

> Pakai skenario perusahaan yang sama seperti suite Accounting: **PT Retail Nusantara Jaya**, 2 toko (Toko Pusat Jakarta, Toko Cabang Bandung), sudah PKP. Lihat [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) untuk detail lengkap — jangan diulang di sini.
>
> **Scope file ini**: PO berdiri sendiri sampai status `approved`/`sent`, **belum** menyentuh Goods Receipt/Purchase Invoice/GL. Integrasi ke Accounting ada di file [`02-po-integrasi-accounting.id.md`](./02-po-integrasi-accounting.id.md).
>
> Pola: **Positif** / **Negatif** / **Netralisasi** seperti suite Accounting.

## Master Data Tambahan

- Supplier: pakai **CV Sumber Pangan Nusantara** (sudah dibuat di file `00` Accounting §8). Kalau belum ada, buat: `{name:"CV Sumber Pangan Nusantara", type:"supplier", payment_term_days:30}`.
- Barang: 2 SKU dagang minimarket — `BRG-001 Minyak Goreng 1L` (unit: pcs, harga beli ±Rp16.000), `BRG-002 Gula Pasir 1kg` (unit: pcs, harga beli ±Rp14.000). Kalau modul Inventory/Product belum di-scope test, cukup pakai baris manual (nama+qty+harga) sesuai field item yang tersedia di masing-masing dokumen.
- Pastikan status setup (`purchase-requests/status-setup`, `purchase-quotations/status-setup`, `purchase-orders/status-setup`) sudah ter-seed — cek dulu via `POST .../status-setup` sebelum create dokumen.

## 1. Purchase Request (**Purchase Requests**)

| Skenario     | Detail                                                                                         | Hasil                                                              |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Positif      | `create` PR Toko Pusat: 2 item (Minyak Goreng qty 50, Gula Pasir qty 30), status awal `draft`   | 201, `pr_number` ter-generate otomatis                             |
| Positif      | `submit` PR                                                                                       | Status pindah ke `submitted` (approval on) atau langsung `approved`/`sent` kalau `require_pr_approval` off — cek [[project_approval_engine_skip_submitted_when_off]] |
| Negatif      | `submit` PR tanpa item sama sekali                                                                | 422, ditolak (bukan submit dokumen kosong)                          |
| Negatif      | `create` PR dengan `branch_id` bukan branch aktif user                                            | 422/403 — isolasi branch                                            |
| Positif      | `approve` PR (kalau approval on)                                                                  | Status `approved`, siap di-clone ke PQ                              |
| Netralisasi  | `cancel` atau `delete` PR test setelah selesai, pastikan tidak ada PQ yang sudah clone dari PR ini |

## 2. Purchase Quotation (**Purchase Quotations**)

| Skenario    | Detail                                                                                                  | Hasil                                                                                       |
| ----------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Positif     | `clone-from-pr` dari PR di atas → PQ draft dengan item ter-copy                                        | 201, qty & nama item sama persis dengan PR                                                    |
| Positif     | `tiers/upsert` — isi harga penawaran dari CV Sumber Pangan Nusantara per item (Minyak 16.000, Gula 14.000) | Tersimpan per supplier tier                                                                    |
| Negatif     | `tiers/upsert` dengan `contact_id` bukan supplier (misal customer)                                     | 422 — validasi tipe kontak                                                                     |
| Positif     | `submit` → `approve` PQ                                                                                | Status `approved`, siap jadi dasar PO                                                          |
| Negatif     | `items/delete` item yang sudah dipakai di tier harga                                                   | Cek behavior — kalau tidak ada guard, catat sebagai gap (harga jadi tidak konsisten)           |
| Netralisasi | `delete` PQ test setelah tidak dipakai PO manapun                                                       |

## 3. Purchase Order (**Purchase Orders**)

| Skenario                        | Detail                                                                                                     | Hasil                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Positif                          | `create` PO dari PQ approved (Toko Pusat, supplier CV Sumber Pangan Nusantara, 2 item, PPN 11%)              | 201, `subtotal`/`tax_amount`/`total_amount` terhitung benar (Minyak 50×16.000 + Gula 30×14.000, +PPN 11%) |
| Positif                          | `submit` → `approve` PO                                                                                       | Status `approved` (approval on) atau langsung skip ke `approved` kalau off ([[project_approval_engine_skip_submitted_when_off]]) |
| Negatif                          | `create` PO dengan item qty 0 atau negatif                                                                    | 422                                                                                                 |
| Negatif                          | `create` PO dengan `contact_id` yang `type` bukan supplier                                                    | 422                                                                                                 |
| Negatif                          | `reject` PO lalu coba `submit` lagi tanpa `request-revision`                                                  | Cek flow status — harus lewat revision dulu atau ditolak                                            |
| **Positif — status history**     | `status-history-list` setelah beberapa transisi status                                                        | Urutan status lengkap & timestamp benar, dipakai audit trail                                        |
| Positif                          | `attachments/upload` PO (misal scan surat pesanan)                                                            | Tersimpan, muncul di `attachments/list`                                                             |
| Netralisasi                      | `cancel` PO test (jangan `delete` kalau sudah ada GR/PI turunan — lihat file 02) sebelum lanjut ke skenario berikutnya |

## Ringkasan Sebelum Lanjut ke File 02

- [ ] 1 PR approved (2 item, Toko Pusat)
- [ ] 1 PQ approved dengan tier harga CV Sumber Pangan Nusantara
- [ ] 1 PO approved dari PQ tsb, total sesuai perhitungan manual (subtotal + PPN 11%)
- [ ] Status history PO tercatat lengkap

## Referensi Silang

- [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) — profil perusahaan & COA dasar
- [`02-po-integrasi-accounting.id.md`](./02-po-integrasi-accounting.id.md) — lanjutan PO ini ke GR/PI/Payment/GL
- [`../../../routes/purchasing.php`](../../../routes/purchasing.php) — daftar endpoint lengkap
