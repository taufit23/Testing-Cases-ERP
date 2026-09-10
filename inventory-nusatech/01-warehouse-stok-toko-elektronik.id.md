---
title: Test Case Inventory (NUSATECH) — 01. Warehouse & Stok Toko Elektronik
category: Inventory Nusatech
description: Warehouse Gudang Utama Retail (tag business_unit_id = BU-RETAIL), stok awal via Stock Adjustment, Stock Take, dan Stock Lots/Serials untuk sisi retail PT NUSATECH (1 branch).
visibility: internal
---

# 01. Warehouse & Stok Toko Elektronik (BU-RETAIL)

> Skenario: **PT NUSATECH**, branch **PT NUSATECH** (1 branch tunggal), divisi **BU-RETAIL**. Lihat [`../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md`](../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md) untuk profil & saldo awal.
>
> Berbeda dari suite `accounting-pos-retail` (minimarket, warehouse `type:store` + Cash Session POS): PT NUSATECH menjual lewat alur Sales biasa (Quotation→SO→Delivery→Invoice, lihat [`../sales-nusatech/`](../sales-nusatech/)), **BUKAN** POS kasir walk-in. Warehouse di sini cukup `type:central`, di-tag `business_unit_id = BU-RETAIL` — TIDAK perlu Cash Session sama sekali.

## 1. Warehouse (**Warehouses**)

| Skenario    | Detail                                                                                   | Hasil                                                           |
| ----------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Positif     | `create` "Gudang Utama Retail", `type:central` (default), `business_unit_id:<BU-RETAIL>` | Warehouse terdaftar, `branch_id` = PT NUSATECH (branch tunggal) |
| Negatif     | `create` warehouse dengan `branch_id` bukan branch aktif                                 | 422/403 — isolasi branch                                        |
| Netralisasi | Jangan hapus warehouse ini selama masih ada `sku_stocks`/dokumen referensi               |

## 2. Stok Awal via Stock Adjustment (bukan Goods Receipt — untuk stok pembuka SEBELUM PO pertama)

> **Sebab-akibat**: stok awal (opening) sebelum ada transaksi Purchasing dicatat via **Stock Adjustment** (bukan Goods Receipt, karena tidak ada PO/supplier untuk stok pembuka bisnis). Mengikuti pola [`accounting-pos-retail/01-...`](../accounting-pos-retail/01-setup-toko-warehouse-dan-cash-session.id.md) §2 — reasoning sama, konteks beda (bukan minimarket, tapi elektronik/komputer).

| SKU     | Nama Produk                       | Qty Awal | Sesuai Saldo Awal COA (file 00 §10)                    |
| ------- | --------------------------------- | -------- | ------------------------------------------------------ |
| LPT-001 | Laptop ASUS Vivobook 14           | 5        | 5 × 6.500.000 = 32.500.000 (AST-05)                    |
| KOM-001 | Keyboard Mechanical Logitech G213 | 0        | belum ada stok awal, diisi lewat PO Purchasing pertama |
| KOM-002 | SSD NVMe 512GB Samsung            | 0        | idem                                                   |

| Skenario    | Detail                                                                                                                                                            | Hasil                                                                                                              |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Positif     | **Product Catalog** → create 3 SKU di atas dengan harga jual sesuai file 00 §9                                                                                    | 3 produk muncul di list                                                                                            |
| Positif     | `stock-adjustments/create` → Gudang Utama Retail, tambah qty 5 Laptop ASUS Vivobook (alasan "Stok awal pengadaan mandiri sebelum PO pertama") → `submit` → `post` | `sku_stocks` LPT-001 bertambah 5 — nilai HARUS konsisten dengan saldo awal AST-05 32.500.000 di Accounting file 00 |
| Negatif     | `post` Stock Adjustment tanpa `submit` dulu (kalau status setup mensyaratkan urutan submit→post)                                                                  | Cek behavior aktual — 422 kalau memang ada guard urutan status                                                     |
| Netralisasi | Reverse stock adjustment test HANYA sebelum ada transaksi penjualan yang memakai stok itu                                                                         |

## 3. Stock Adjustment Reasons (master data pendukung)

| Skenario | Detail                                                                                                                   | Hasil                                             |
| -------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| Positif  | `stock-adjustment-reasons/options` — pastikan alasan "Stok awal pengadaan mandiri" tersedia sebelum create adjustment §2 | Muncul di dropdown, kalau belum ada `create` dulu |
| Positif  | `stock-adjustment-reasons/create` — tambah alasan "Kerusakan unit display toko" untuk skenario §5 di bawah               | Tersimpan                                         |

## 4. Stock Lots & Serials (opsional — kalau tracking per-unit dibutuhkan untuk laptop bergaransi)

> Laptop biasanya dijual dengan nomor serial per unit untuk klaim garansi — cocok pakai **Stock Serials**, bukan Stock Lots (lot lebih cocok untuk barang batch seperti aksesoris non-serial).

| Skenario    | Detail                                                                                                             | Hasil                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| Positif     | `stock-serials/create` untuk masing-masing 5 unit Laptop ASUS Vivobook (SN unik per unit)                          | 5 record serial terdaftar, terhubung ke `sku_id` LPT-001                             |
| Negatif     | `create` Serial dengan nomor SN duplikat                                                                           | 422 — cek constraint unique SN kalau ada, catat sebagai temuan kalau tidak ada guard |
| Positif     | `stock-lots/effective-cost` untuk KOM-001/KOM-002 (costing_method-aware, fifo/average) setelah GR Purchasing masuk | 200, unit cost sesuai `costing_method` yang di-set di `inventory-configs`            |
| Netralisasi | Hapus serial/lot test kalau belum terpakai di Delivery/penjualan                                                   |

## 5. Stock Take (Opname Berkala)

> Fitur scan-to-count — lihat [[project_stock_opname_scan_and_bugfixes]] untuk histori bug yang sudah difix (create() crash, field-name mismatch, update-item endpoint hilang — semua sudah beres, aman dipakai).

| Skenario    | Detail                                                                                                                                      | Hasil                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Positif     | `stock-takes/create` untuk Gudang Utama Retail, snapshot semua SKU                                                                          | 201, `counted_qty` awal = 0 semua baris                                            |
| Positif     | `stock-takes/scan {barcode:<barcode LPT-001>}` berkali-kali sampai `counted_qty` = qty fisik aktual                                         | Increment otomatis per scan                                                        |
| Positif     | `stock-takes/update-item` — manual override 1 item kalau scan gagal (barcode rusak)                                                         | `counted_qty` ter-update manual                                                    |
| Negatif     | Temukan selisih: fisik 4 unit Laptop padahal sistem 5 (1 unit rusak, dicatat via Stock Adjustment Reasons "Kerusakan unit display toko" §3) | `complete` Stock Take → `sku_stocks` disesuaikan ke qty fisik, selisih -1 tercatat |
| Positif     | `complete`                                                                                                                                  | Status `completed`, `sku_stocks` final = hasil hitung fisik                        |
| Netralisasi | Stock Take yang sudah `completed` adalah state akhir wajar — tidak perlu di-reverse                                                         |

## 6. Stock Adjustment — Selisih & Inventory Journal Otomatis

> Beda jalur dari §5 (Stock Take) — Stock Take `complete()` saat ini menulis `sku_stocks` langsung lewat `StockMovements::recordMovement()`, **BELUM** lewat `StockAdjustmentFinalizer`, jadi selisih dari Stock Take **TIDAK** memicu Inventory Journal (lihat `docs/inventory-auto-replenishment-plan.id.md` bagian 2 — batasan yang belum dibereskan). Skenario di bawah pakai jalur **Stock Adjustment langsung** (`stock-adjustments/create`), satu-satunya jalur yang saat ini benar-benar posting jurnal. Prasyarat: mapping COA §11 di [`accounting-nusatech/00-...`](../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md#11-inventory-journal--chart-of-accounts-mapping-inventoryconfig) harus sudah diisi.

| Skenario    | Detail                                                                                                                                                                                                  | Hasil                                                                                                                                                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `stock-adjustments/create` → Gudang Utama Retail, item LPT-001: `qty_system:5`, `qty_actual:4`, `unit_cost:6500000` (1 unit rusak, alasan "Kerusakan unit display toko" §3) → `submit` → `post`         | `qty_difference = -1`. Setelah finalize: `sku_stocks` LPT-001 turun jadi 4, DAN 1 jurnal Inventory Journal (`IJ-...`) auto-posted: **Dr BBN-06 Beban Kerugian Persediaan 6.500.000 / Cr AST-05 Persediaan 6.500.000**                    |
| Positif     | Cek `general-ledger/detail-ledger` filter AST-05 & BBN-06 setelah adjustment di atas                                                                                                                    | AST-05 turun 6.500.000 dari saldo sebelumnya, BBN-06 bertambah 6.500.000 — total debit=kredit balance                                                                                                                                    |
| Positif     | Adjustment lain: item KOM-001 (sudah ada stok dari GR Purchasing, lihat `purchasing-nusatech/`) dengan `qty_actual` LEBIH BESAR dari `qty_system` (ketemu unit ekstra saat opname) + `unit_cost` terisi | `qty_difference` positif. Jurnal: **Dr AST-05 Persediaan / Cr PDT-04 Pendapatan Lain-lain (Selisih Opname)** senilai selisih × unit_cost                                                                                                 |
| Negatif     | Buat adjustment dengan `unit_cost:0` (atau kosong) pada item yang selisih                                                                                                                               | `sku_stocks` tetap ter-update (stok fisik tidak boleh terhambat akuntansi), TAPI item itu di-exclude dari perhitungan jurnal — kalau semua item di adjustment itu `unit_cost:0`, TIDAK ADA jurnal yang terbuat sama sekali (bukan error) |
| Negatif     | Hapus/kosongkan salah satu mapping COA §11 (mis. `inventory_loss`), lalu ulangi skenario shrinkage di atas                                                                                              | Stock movement & status `posted` tetap sukses seperti biasa (fail-soft) — cek log aplikasi (`storage/logs/laravel.log`) ada warning `StockAdjustmentFinalizer: gagal posting jurnal variance`, TIDAK ADA jurnal terbuat                  |
| Netralisasi | Reverse/koreksi adjustment test HANYA sebelum ada transaksi penjualan yang memakai stok LPT-001 pasca-adjustment                                                                                        |

## Ringkasan

- [ ] Gudang Utama Retail terdaftar, tag `business_unit_id = BU-RETAIL`
- [ ] 3 SKU produk terdaftar, stok awal LPT-001 = 5 unit (konsisten dengan AST-05 file 00)
- [ ] Serial number per unit Laptop terdaftar (opsional)
- [ ] Stock Take selesai dengan 1 selisih kerusakan terdokumentasi
- [ ] Stock Adjustment shrinkage (§6) posting jurnal Dr BBN-06/Cr AST-05 dengan benar, balance di GL

## Referensi Silang

- [`../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md`](../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md) — §11 mapping COA Inventory Journal
- `docs/inventory-auto-replenishment-plan.id.md` — desain lengkap Inventory Journal & auto-replenishment
- [`../purchasing-nusatech/02-po-integrasi-accounting.id.md`](../purchasing-nusatech/02-po-integrasi-accounting.id.md) — GR menambah stok KOM-001/KOM-002
- [`../sales-nusatech/02-so-integrasi-accounting.id.md`](../sales-nusatech/02-so-integrasi-accounting.id.md) — Delivery mengurangi stok
- [[project_stock_opname_scan_and_bugfixes]]
