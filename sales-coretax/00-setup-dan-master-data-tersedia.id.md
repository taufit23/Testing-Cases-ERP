---
title: (CORETAX) — Sales 00. Setup & Master Data
category: sales-coretax
description: Langkah WAJIB setup sales_configs (belum ter-seed sama sekali) sebelum test case integrasi Sales-Accounting bisa jalan, plus referensi customer/produk yang dipakai suite ini.
visibility: internal
---

# Sales CORETAX — 00. Setup & Master Data

> Master data lengkap (COA, produk, customer) ada di [`accounting-coretax/00-master-data-tersedia-dari-seeder.id.md`](../accounting-coretax/00-master-data-tersedia-dari-seeder.id.md) §12-14. File ini fokus ke yang SPESIFIK Sales — termasuk **langkah setup yang WAJIB dijalankan lebih dulu** karena, beda dari Purchasing, `sales_configs` untuk branch Pusat **KOSONG** (tidak ada seeder-nya sama sekali).

> ⚠️ **Dependensi antar-suite**: file `02-so-integrasi-accounting.id.md` di suite ini menjual SKU `SSD-512G` & `BUSI-NGK-STD` — SKU yang SAMA dengan yang dibeli di [`purchasing-coretax/02-po-integrasi-accounting.id.md`](../purchasing-coretax/02-po-integrasi-accounting.id.md) (GR masuk 10 & 20 pcs). **Jalankan suite `purchasing-coretax` lengkap dulu** supaya ada stock riil di Gudang Cikarang sebelum Sales Delivery dites — kalau tidak, Delivery akan gagal/nol karena semua SKU mulai dari stock 0 (lihat `accounting-coretax/00` §10).

## ⚠️ Langkah 1 — WAJIB: Buat Akun COA yang Belum Ada

`ar` (→ `1121`) dan `sales_revenue` (→ `4001`) sudah ada. Tapi `ppn_keluaran` dan `sales_return` belum punya akun:

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Buat akun PPN Keluaran | `POST chart-of-accounts/create {code:"2191", name:"PPN Keluaran", type_id:<DAGANG-LIABILITY>, parent_id:<GRP21>, level:3}` | 201 |
| Buat akun Retur Penjualan (kontra-pendapatan) | `POST chart-of-accounts/create {code:"4002", name:"Retur Penjualan", type_id:<DAGANG-REVENUE>, parent_id:<GRP40>, level:3}` | 201 — **kontra-Pendapatan**, JANGAN reuse `5002 Retur Pembelian` (itu kontra-Beban sisi Purchasing, normal balance beda) |

## ⚠️ Langkah 2 — WAJIB: `sales-configs/upsert`

Lihat [temuan lengkap](../../TemuanTestCase/Sales/CoretaxCompany/01-sales-config-belum-diseed.id.md) — tanpa langkah ini, SEMUA posting GL dari Sales Invoice/Payment/Return akan gagal `content.sales_config_is_not_set_up_for_this_branch`.

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Positif — setup awal** | `PUT sales/sales-configs/upsert {default_journal_mode:"auto", require_so_approval:true, require_delivery_approval:false, require_si_approval:false, allow_si_without_delivery:false, so_fulfillment_mode:"delivery_first", config_journals:[{functionality:"ar", coa_id:<1121>},{functionality:"sales_revenue", coa_id:<4001>},{functionality:"ppn_keluaran", coa_id:<2191>},{functionality:"cash_bank", coa_id:<1103>},{functionality:"sales_return", coa_id:<4002>}]}` | 200, `sales_configs` + 5 `sales_config_journals` terbentuk |
| Verifikasi | `POST sales/sales-configs/list` | 5 mapping aktif, sesuai payload di atas |

## Catatan Penting Lain

- **Tidak ada posting HPP/Inventory otomatis** di rantai Sales manapun (Delivery maupun Invoice) — lihat [temuan #2](../../TemuanTestCase/Sales/CoretaxCompany/02-tidak-ada-posting-hpp-otomatis.id.md). Jangan berharap `1410 Persediaan` berkurang otomatis dari SI.
- **Belum ada harga jual ter-set** di price list "Retail"/"Grosir" (`price_list_skus` kosong untuk kedua price list itu) — semua test case di suite ini kirim harga custom langsung di baris SO, tidak mengandalkan price list.

## Data yang Dipakai Suite Ini

- **Customer**: PT Cahaya Abadi Sejahtera (credit limit 25.000.000, termin 30 hari)
- **Produk & harga jual custom**: `SSD-512G` (jual 650.000/pcs, beli 480.000), `BUSI-NGK-STD` (jual 25.000/pcs, beli 18.000)
- **Discount**: `NEWCUST10` (10%, min order 500.000, maks potongan 200.000) — siap pakai untuk skenario diskon
- **Tax**: `PPN` (11%)
