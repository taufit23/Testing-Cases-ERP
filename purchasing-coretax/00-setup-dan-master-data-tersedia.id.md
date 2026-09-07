---
title: (CORETAX) — Purchasing 00. Setup & Master Data Tersedia
category: purchasing-coretax
description: Konfigurasi purchase_configs yang sudah ter-seed untuk CORETAX + referensi supplier/produk yang dipakai suite ini.
visibility: internal
---

# Purchasing CORETAX — 00. Setup & Master Data

> Master data lengkap (COA, produk, supplier, warehouse) sudah didokumentasikan di [`accounting-coretax/00-master-data-tersedia-dari-seeder.id.md`](../accounting-coretax/00-master-data-tersedia-dari-seeder.id.md) §11-13. File ini cuma highlight bagian yang SPESIFIK ke Purchasing.

## Purchase Config (sudah ter-seed lengkap, `PurchaseConfigSeeder` + `PurchaseModuleCoaMappingSeeder`)

| Flag | Nilai | Dampak ke test case |
| --- | --- | --- |
| `po_flow_mode` | `flexible` | PO bisa dibuat langsung tanpa PQ |
| `require_pr_approval` | `true` | PR WAJIB approve dulu sebelum lanjut ke PQ/PO |
| `allow_pq_without_pr` | `true` | PQ boleh dibuat tanpa PR sebelumnya |
| `require_pq_before_po` | `false` | PO **boleh** dibuat langsung tanpa PQ — jalur pendek valid |
| `require_pq_approval` | `true` | PQ WAJIB approve dulu (kalau dipakai) |
| `min_quotation_suppliers` | `1` | PQ cukup ke 1 supplier (biasanya untuk perbandingan harga, di sini minimal 1 tidak wajib banding) |
| `require_gr_for_po_close` | `true` | PO tidak bisa `closed` sebelum ada Goods Receipt |
| `allow_pi_without_gr` | `true` | PI **boleh** dibuat tanpa GR dulu — tapi suite ini pakai jalur WITH-GR sebagai jalur utama (lebih realistis) |
| `require_payment_proof` | `false` | Payment Bill tidak wajib upload bukti transfer |
| `default_journal_mode` | `manual` | **PENTING**: auto-posting jurnal ke GL TIDAK aktif default untuk config header — verifikasi di §1 file `02-po-integrasi-accounting.id.md` apakah perlu di-set `auto`/`hybrid` dulu sebelum GL benar-benar terbentuk otomatis |

**COA Mapping functionality** (sudah lengkap, lihat [`accounting-coretax/00`](../accounting-coretax/00-master-data-tersedia-dari-seeder.id.md#2-chart-of-accounts-35-baris--13-groupsubgroup--22-akun-leaf)): `inventory→1410`, `gr_ir→2105`, `ppn_masukan→1424`, `cash_bank→1103`, `return→5002`, `ap→2102`, `dp→1422`, `purchase_expense→5001`.

## Status Awal Dokumen (dari `PurchaseStatusSeeder`)

| Modul | Status saat create |
| --- | --- |
| Purchase Request | `draft` |
| Purchase Quotation | `draft` |
| Purchase Order | **`open`** (bukan draft — langsung aktif) |
| Purchase Receipt | `completed` |
| Purchase Invoice | `unpaid` |
| Purchase Payment Bill | `pending` |
| Purchase Return | `pending` |

## Data yang Dipakai Suite Ini

- **Supplier**: PT Sumber Makmur (credit limit 50.000.000, termin 30 hari)
- **Produk**: `SSD-512G` (SSD NVMe 512GB M.2, harga beli 480.000/pcs), `BUSI-NGK-STD` (Busi NGK CR6HSA Standard, harga beli 18.000/pcs)
- **Warehouse**: Gudang Cikarang (stock awal 0 untuk kedua SKU)
- **Tax**: `PPN` (code, 11%, increase)
