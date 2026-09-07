---
title: Test Case Sales — 01. Sales Order Standalone (Quotation → SO)
category: Testing
description: Alur Quotation → Sales Order berdiri sendiri (belum sampai Delivery/Invoice/GL) untuk skenario PT Retail Nusantara Jaya.
visibility: internal
---

# 01. Sales Order Standalone (Quotation → SO)

> Skenario perusahaan sama: **PT Retail Nusantara Jaya**, lihat [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md).
>
> **Scope file ini**: Quotation → Sales Order sampai `approved`, **belum** menyentuh Delivery/Invoice/GL. Integrasi ke Accounting ada di [`02-so-integrasi-accounting.id.md`](./02-so-integrasi-accounting.id.md).

## Master Data Tambahan

- Customer: pakai **PT Mitra Grosir Indonesia** (sudah dibuat di file `00` Accounting §8, `payment_term_days:30`).
- Barang jual: SKU sama seperti Purchasing (Minyak Goreng 1L, Gula Pasir 1kg) tapi harga jual retail markup — Minyak Rp19.000, Gula Rp16.500.
- Pastikan `sales-orders/status-setup` dan `quotations/status-setup` sudah ter-seed.

## 1. Quotation (**Quotations**)

| Skenario                    | Detail                                                                                       | Hasil                                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| Positif                      | `create` Quotation untuk PT Mitra Grosir Indonesia, 2 item (Minyak qty 100, Gula qty 60)          | 201, subtotal + PPN 11% terhitung benar                                                          |
| Negatif                      | `create` dengan SKU duplikat di 2 baris item berbeda                                              | Ditolak/di-merge — regression check [[project_quotation_so_flow_fixes_20260720]] (dulu ada bug duplicate SKU) |
| Positif                      | `submit` → `resend-to-customer` → `customer-accept`                                               | Status akhir `accepted`, siap convert ke SO                                                       |
| Negatif                      | `customer-accept` pada Quotation yang belum `sent`                                                | 422/403 — urutan status                                                                           |
| Positif                      | `download-pdf`                                                                                     | Gated — hanya bisa setelah status tertentu (bukan draft) — [[project_quotation_so_flow_fixes_20260720]] |
| Positif                      | `convert-to-so`                                                                                    | Harus lewat approval gate (bukan langsung create SO tanpa cek) — [[project_quotation_so_flow_fixes_20260720]] |
| Netralisasi                  | `delete` Quotation test kalau belum di-convert ke SO                                              |

## 2. Sales Order (**Sales Orders**)

| Skenario                              | Detail                                                                                        | Hasil                                                                                             |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Positif                                | SO ter-create otomatis dari `convert-to-so` Quotation di atas                                        | Item & harga sama persis dengan Quotation accepted                                                     |
| **Positif — cek credit limit**         | `customer-credit-status` untuk PT Mitra Grosir Indonesia sebelum `approve` SO                        | Preview status kredit (dalam limit / melebihi) — Sales Phase 4 gate                                    |
| Negatif                                | `approve` SO yang total-nya melebihi credit limit customer (kalau credit limit di-set kecil utk test) | Ditolak, pesan jelas soal credit limit                                                                 |
| Positif                                | `submit` → `approve` SO                                                                              | Status `approved` (approval on) atau skip ke approved kalau off — [[project_approval_engine_skip_submitted_when_off]] |
| Negatif                                | `create` SO manual dengan qty 0                                                                       | 422                                                                                                     |
| Positif                                | `status_history` (lihat via `show` + relasi `status_histories` — ingat [[feedback_relation_json_snake_case]]) | Urutan status lengkap                                                                                   |
| Netralisasi                            | `cancel` SO test (jangan `delete` kalau sudah ada Delivery/Invoice turunan — lihat file 02)            |

## Ringkasan Sebelum Lanjut ke File 02

- [ ] 1 Quotation accepted (2 item, PT Mitra Grosir Indonesia)
- [ ] 1 SO approved hasil convert dari Quotation tsb, lolos credit-limit check
- [ ] Total SO sesuai perhitungan manual (subtotal + PPN 11%)

## Referensi Silang

- [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md)
- [`02-so-integrasi-accounting.id.md`](./02-so-integrasi-accounting.id.md) — lanjutan SO ini ke Delivery/Invoice/Payment/GL
- [[project_quotation_so_flow_fixes_20260720]], [[project_approval_engine_skip_submitted_when_off]]
- [`../../../routes/sales.php`](../../../routes/sales.php) — daftar endpoint lengkap
