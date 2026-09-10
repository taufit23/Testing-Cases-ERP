---
title: Test Case Purchasing (NUSATECH) — 01. Purchase Order Standalone (PR → PQ → PO)
category: PO Nusatech
description: Alur Purchase Requisition → Purchase Quotation → Purchase Order berdiri sendiri untuk PT NUSATECH — procurement software/hardware konsultan (BU-CONSULT) dan stok elektronik toko (BU-RETAIL), 1 branch.
visibility: internal
---

# 01. Purchase Order Standalone (PR → PQ → PO)

> Skenario perusahaan: **PT NUSATECH**, lihat [`../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md`](../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md).
>
> **Scope file ini**: PO berdiri sendiri sampai status `approved`/`sent`, **belum** menyentuh Goods Receipt/Purchase Invoice/GL. Integrasi ke Accounting ada di [`02-po-integrasi-accounting.id.md`](./02-po-integrasi-accounting.id.md).
>
> Dua alur berbeda diuji, KEDUANYA di branch **PT NUSATECH yang sama** (1 branch, tidak ada switch-context): **(A)** procurement hardware/software untuk kebutuhan internal konsultan (`BU-CONSULT`, tidak masuk stok dagang), **(B)** procurement stok dagang elektronik untuk dijual lagi di toko (`BU-RETAIL`, masuk `sku_stocks`).
>
> ⚠️ **`purchase_requests`/`purchase_quotations`/`purchase_orders` TIDAK punya kolom `business_unit_id`** (dicek di migration, tidak ada) — pemisahan alur A vs B di file ini murni dokumentasi/testing by convention (via supplier & item yang dipakai), bukan field yang benar-benar di-tag di payload PR/PQ/PO. Tag `business_unit_id` baru benar-benar tersimpan nanti di level **jurnal** hasil `export-to-journal` (lihat file 02) via mapping akun COA yang sudah ada `default_business_units_id`-nya.

## Master Data Tambahan

- Supplier hardware/software: **PT Distributor Teknologi Nusantara** (`payment_term_days:30`).
- Supplier elektronik dagang: **PT Grosir Elektronik Jaya** (`payment_term_days:30`).
- Barang alur A (non-inventory, dipakai internal): "Lisensi Microsoft 365 Business (5 seat)", "Laptop Dell Latitude untuk Tim Proyek (2 unit)" — kalau modul Inventory tidak di-scope untuk item internal ini, cukup baris manual (nama+qty+harga).
- Barang alur B (SKU dagang, sudah didaftarkan di `inventory-nusatech/`): `LPT-001 Laptop ASUS Vivobook 14`, `KOM-001 Keyboard Mechanical Logitech G213`, `KOM-002 SSD NVMe 512GB Samsung`.
- Pastikan status setup (`purchase-requests/status-setup`, `purchase-quotations/status-setup`, `purchase-orders/status-setup`) sudah ter-seed di branch PT NUSATECH sebelum create dokumen (status setup tetap branch-scoped, tapi karena cuma 1 branch, cukup 1 kali seed).

## A. Alur Procurement Internal Konsultan (BU-CONSULT)

### A.1 Purchase Request

| Skenario    | Detail                                                                                        | Hasil                                                                                                                                                            |
| ----------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `create` PR: 2 item (Lisensi M365 qty 5, Laptop Dell qty 2), status awal `draft`              | 201, `pr_number` ter-generate otomatis                                                                                                                           |
| Positif     | `submit` PR                                                                                   | Status pindah ke `submitted` (approval on) atau langsung `approved`/`sent` kalau `require_pr_approval` off — [[project_approval_engine_skip_submitted_when_off]] |
| Negatif     | `submit` PR tanpa item sama sekali                                                            | 422, ditolak                                                                                                                                                     |
| Negatif     | `create` PR dengan `branch_id` bukan branch aktif user                                        | 422/403 — isolasi branch (tetap berlaku walau cuma 1 branch valid — payload dengan `branch_id` lain harus tetap ditolak)                                         |
| Positif     | `approve` PR (kalau approval on)                                                              | Status `approved`, siap di-clone ke PQ                                                                                                                           |
| Netralisasi | `cancel`/`delete` PR test setelah selesai, pastikan tidak ada PQ yang sudah clone dari PR ini |

### A.2 Purchase Quotation

| Skenario    | Detail                                                                                                                             | Hasil                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Positif     | `clone-from-pr` dari PR di atas → PQ draft dengan item ter-copy                                                                    | 201, qty & nama item sama persis dengan PR |
| Positif     | `tiers/upsert` — isi harga penawaran PT Distributor Teknologi Nusantara (Lisensi M365 1.500.000/seat, Laptop Dell 12.000.000/unit) | Tersimpan per supplier tier                |
| Negatif     | `tiers/upsert` dengan `contact_id` bukan supplier (misal customer)                                                                 | 422 — validasi tipe kontak                 |
| Positif     | `submit` → `approve` PQ                                                                                                            | Status `approved`                          |
| Netralisasi | `delete` PQ test setelah tidak dipakai PO manapun                                                                                  |

### A.3 Purchase Order

| Skenario                 | Detail                                                                             | Hasil                                                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Positif                  | `create` PO dari PQ approved (PT Distributor Teknologi Nusantara, 2 item, PPN 11%) | 201, subtotal = 5×1.500.000 + 2×12.000.000 = 31.500.000, `tax_amount` PPN 11% = 3.465.000, `total_amount` = **34.965.000** |
| Positif                  | `submit` → `approve` PO                                                            | Status `approved` (approval on) atau langsung `approved` kalau off                                                         |
| Negatif                  | `create` PO dengan item qty 0 atau negatif                                         | 422                                                                                                                        |
| Negatif                  | `create` PO dengan `contact_id` yang `type` bukan supplier                         | 422                                                                                                                        |
| Positif — status history | `status-history-list` setelah beberapa transisi status                             | Urutan status lengkap & timestamp benar                                                                                    |
| Positif                  | `attachments/upload` PO (scan surat pesanan/kontrak lisensi)                       | Tersimpan, muncul di `attachments/list`                                                                                    |
| Netralisasi              | `cancel` PO test (jangan `delete` kalau sudah ada GR/PI turunan)                   |

## B. Alur Procurement Stok Dagang Elektronik (BU-RETAIL)

> **Branch dan user yang sama** dengan Alur A — tidak perlu switch context apapun, hanya beda supplier & item yang dipakai.

### B.1 Purchase Request

| Skenario    | Detail                                                               | Hasil                          |
| ----------- | -------------------------------------------------------------------- | ------------------------------ |
| Positif     | `create` PR: 3 item (LPT-001 qty 10, KOM-001 qty 20, KOM-002 qty 15) | 201, `pr_number` auto-generate |
| Positif     | `submit` → `approve` PR                                              | Status `approved`              |
| Netralisasi | `cancel`/`delete` PR test                                            |

### B.2 Purchase Quotation

| Skenario    | Detail                                                                                               | Hasil                 |
| ----------- | ---------------------------------------------------------------------------------------------------- | --------------------- |
| Positif     | `clone-from-pr` → PQ draft                                                                           | Item ter-copy dari PR |
| Positif     | `tiers/upsert` harga PT Grosir Elektronik Jaya (LPT-001 6.500.000, KOM-001 450.000, KOM-002 550.000) | Tersimpan             |
| Positif     | `submit` → `approve` PQ                                                                              | Status `approved`     |
| Netralisasi | `delete` PQ test                                                                                     |

### B.3 Purchase Order

| Skenario    | Detail                                                                                                                                             | Hasil                           |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| Positif     | `create` PO dari PQ approved: subtotal = 10×6.500.000 + 20×450.000 + 15×550.000 = 65.000.000+9.000.000+8.250.000 = 82.250.000, PPN 11% = 9.047.500 | `total_amount` = **91.297.500** |
| Positif     | `submit` → `approve` PO                                                                                                                            | Status `approved`               |
| Netralisasi | `cancel` PO test                                                                                                                                   |

## Ringkasan Sebelum Lanjut ke File 02

- [ ] Alur A: 1 PO approved (BU-CONSULT, secara dokumentasi), total 34.965.000, dari PT Distributor Teknologi Nusantara
- [ ] Alur B: 1 PO approved (BU-RETAIL, secara dokumentasi), total 91.297.500, dari PT Grosir Elektronik Jaya
- [ ] Status history lengkap di kedua PO

## Referensi Silang

- [`../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md`](../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md)
- [`02-po-integrasi-accounting.id.md`](./02-po-integrasi-accounting.id.md)
- [`../../../routes/purchasing.php`](../../../routes/purchasing.php)
- [[project_approval_engine_skip_submitted_when_off]]
