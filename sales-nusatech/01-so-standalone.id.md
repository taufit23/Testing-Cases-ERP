---
title: Test Case Sales (NUSATECH) — 01. Sales Order Standalone (Quotation → SO)
category: Sales Nusatech
description: Alur Quotation → Sales Order berdiri sendiri untuk PT NUSATECH — kontrak jasa konsultasi/managed-service (BU-CONSULT/BU-MANAGED, termin/milestone) dan penjualan retail unit ke reseller (BU-RETAIL), 1 branch.
visibility: internal
---

# 01. Sales Order Standalone (Quotation → SO)

> Skenario: **PT NUSATECH**, lihat [`../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md`](../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md).
>
> **Scope file ini**: Quotation → SO sampai `approved`, **belum** Delivery/Invoice/GL. Integrasi ke Accounting di [`02-so-integrasi-accounting.id.md`](./02-so-integrasi-accounting.id.md).
>
> Dua alur, KEDUANYA di branch **PT NUSATECH yang sama** (1 branch, tidak ada switch-context): **(A)** kontrak jasa (`BU-CONSULT`/`BU-MANAGED`) — SO berbasis termin/milestone, TANPA barang fisik jadi TANPA Delivery. **(B)** penjualan retail unit ke reseller (`BU-RETAIL`) — SO dengan barang fisik, pakai Delivery seperti alur dagang biasa.
>
> ⚠️ **`quotations`/`sales_orders` TIDAK punya kolom `business_unit_id`** — sama seperti sisi Purchasing, tagging BU baru benar-benar tersimpan di level jurnal (Sales Invoice `export-to-journal`, lihat file 02) lewat akun COA pendapatan yang sudah punya `default_business_units_id` (PDT-01/PDT-02/PDT-03).

## Master Data Tambahan

- Customer jasa: **PT Solusi Niaga Digital** (proyek software, `payment_term_days:30`), **PT Sinergi Pangan Nasional** (managed service, `payment_term_days:14`) — sudah dibuat di file `00` Accounting.
- Customer retail: **CV Reseller Gadget Bandung** (`payment_term_days:14`).
- SKU jual Alur B: `LPT-001 Laptop ASUS Vivobook 14` (Rp 7.800.000), `KOM-001 Keyboard Mechanical Logitech G213` (Rp 650.000), `KOM-002 SSD NVMe 512GB Samsung` (Rp 750.000).
- Pastikan `sales-orders/status-setup` dan `quotations/status-setup` sudah ter-seed di branch PT NUSATECH (branch-scoped, tapi karena cuma 1 branch, cukup 1 kali seed).

## A. Alur Kontrak Jasa Konsultasi & Managed Service (BU-CONSULT / BU-MANAGED)

> **Catatan struktural**: modul Sales di backend didesain generik untuk barang+jasa. Untuk jasa berbasis proyek/milestone, "item" di Quotation/SO diisi baris jasa (bukan SKU fisik) — pakai deskripsi bebas per baris (mis. "Milestone 2 — Modul Payroll") dengan `qty:1`, harga sesuai nilai kontrak. **Tidak ada field milestone/termin khusus di Sales Order** — modul ini tidak punya konsep "payment schedule" bertahap bawaan; termin dilakukan lewat beberapa **Sales Payment Bill parsial** terhadap 1 Sales Invoice (lihat file 02 §3, pola sama seperti [[project_payment_bill_termin_ordering]] versi Sales).

### A.1 Quotation — Proyek Software Development (PT Solusi Niaga Digital)

| Skenario    | Detail                                                                                                                | Hasil                                                                    |
| ----------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Positif     | `create` Quotation, 1 baris jasa "Pengembangan Custom Software — Milestone 2 (Modul Payroll)" qty 1, harga 45.000.000 | 201, subtotal 45.000.000 + PPN 11% = 49.950.000                          |
| Positif     | `submit` → `resend-to-customer` → `customer-accept`                                                                   | Status `accepted`, siap convert ke SO                                    |
| Negatif     | `customer-accept` pada Quotation yang belum `sent`                                                                    | 422/403 — urutan status                                                  |
| Positif     | `convert-to-so`                                                                                                       | Harus lewat approval gate — [[project_quotation_so_flow_fixes_20260720]] |
| Netralisasi | `delete` Quotation test kalau belum di-convert                                                                        |

### A.2 Sales Order — Proyek Software Development

| Skenario                   | Detail                                                                | Hasil                                                    |
| -------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------- |
| Positif                    | SO ter-create otomatis dari `convert-to-so`                           | Baris jasa & harga sama persis dengan Quotation accepted |
| Positif — cek credit limit | `customer-credit-status` PT Solusi Niaga Digital sebelum `approve` SO | Preview status kredit                                    |
| Positif                    | `submit` → `approve` SO                                               | Status `approved`                                        |
| Netralisasi                | `cancel` SO test (jangan `delete` kalau sudah ada Invoice turunan)    |

### A.3 Quotation & SO — Kontrak Managed Service Bulanan (PT Sinergi Pangan Nasional)

| Skenario            | Detail                                                                                                                                                                                 | Hasil                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Positif             | `create` Quotation, 1 baris jasa "Managed IT Support — Kontrak Bulanan Agustus 2026" qty 1, harga 12.000.000                                                                           | 201, subtotal 12.000.000 + PPN 11% = 13.320.000                |
| Positif             | `submit` → `resend-to-customer` → `customer-accept` → `convert-to-so`                                                                                                                  | SO ter-create, `approved` setelah credit-limit check + approve |
| ⚠️ Catatan recurring | Sama seperti jurnal manual Accounting file 01, **tidak ada fitur auto-generate SO/Invoice bulanan** — kontrak bulan berikutnya harus dibuat Quotation→SO baru secara manual tiap bulan | Jangan uji "auto-renewal" yang tidak ada                       |
| Netralisasi         | `cancel` SO test                                                                                                                                                                       |

## B. Alur Penjualan Retail ke Reseller (BU-RETAIL)

> **Branch dan user yang sama** dengan Alur A — tidak perlu switch context apapun.

### B.1 Quotation

| Skenario    | Detail                                                                                                     | Hasil                                                                                                               |
| ----------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Positif     | `create` Quotation untuk CV Reseller Gadget Bandung, 3 item (LPT-001 qty 5, KOM-001 qty 10, KOM-002 qty 8) | 201, subtotal = 5×7.800.000+10×650.000+8×750.000 = 39.000.000+6.500.000+6.000.000 = 51.500.000, PPN 11% = 5.665.000 |
| Negatif     | `create` dengan SKU duplikat di 2 baris berbeda                                                            | Ditolak/di-merge — [[project_quotation_so_flow_fixes_20260720]]                                                     |
| Positif     | `submit` → `resend-to-customer` → `customer-accept`                                                        | Status `accepted`                                                                                                   |
| Positif     | `download-pdf`                                                                                             | Gated — hanya bisa setelah status tertentu                                                                          |
| Positif     | `convert-to-so`                                                                                            | Lewat approval gate                                                                                                 |
| Netralisasi | `delete` Quotation kalau belum di-convert                                                                  |

### B.2 Sales Order

| Skenario                   | Detail                                                                                    | Hasil                                  |
| -------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------- |
| Positif                    | SO ter-create dari `convert-to-so`                                                        | Item & harga sama persis               |
| Positif — cek credit limit | `customer-credit-status` CV Reseller Gadget Bandung                                       | Preview status kredit                  |
| Negatif                    | `approve` SO yang total-nya melebihi credit limit reseller (set kecil utk test)           | Ditolak, pesan jelas soal credit limit |
| Positif                    | `submit` → `approve` SO                                                                   | Status `approved`                      |
| Negatif                    | `create` SO manual dengan qty 0                                                           | 422                                    |
| Positif                    | `status_history` (relasi `status_histories`, ingat [[feedback_relation_json_snake_case]]) | Urutan status lengkap                  |
| Netralisasi                | `cancel` SO test (jangan `delete` kalau sudah ada Delivery/Invoice turunan)               |

## Ringkasan Sebelum Lanjut ke File 02

- [ ] Alur A: 2 SO approved (BU-CONSULT/BU-MANAGED, secara dokumentasi) — proyek software (49.950.000) & managed service bulanan (13.320.000)
- [ ] Alur B: 1 SO approved (BU-RETAIL, secara dokumentasi) — reseller, total 57.165.000, lolos credit-limit check

## Referensi Silang

- [`../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md`](../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md)
- [`02-so-integrasi-accounting.id.md`](./02-so-integrasi-accounting.id.md)
- [[project_quotation_so_flow_fixes_20260720]], [[project_approval_engine_skip_submitted_when_off]], [[feedback_relation_json_snake_case]]
- [`../../../routes/sales.php`](../../../routes/sales.php)
