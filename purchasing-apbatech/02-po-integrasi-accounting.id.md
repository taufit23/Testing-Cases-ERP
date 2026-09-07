---
title: Test Case Purchasing (APBATECH) — 02. PO Terintegrasi Accounting (GR → PI → Payment → GL)
category: PO Apbatech
description: Lanjutan PO approved dari file 01 ke Goods Receipt, Purchase Invoice, Payment Bill, dan verifikasi posting GL untuk PT APBATECH (1 branch, 2 profil procurement dibedakan via business_unit_id di jurnal).
visibility: internal
---

# 02. PO Terintegrasi Accounting (GR → PI → Payment → GL)

> Prasyarat: PO approved dari [`01-po-standalone.id.md`](./01-po-standalone.id.md) — Alur A (BU-CONSULT) dan Alur B (BU-RETAIL), keduanya di branch PT APBATECH yang sama. COA & saldo di [`../accounting-apbatech/00-profil-perusahaan-dan-master-data.id.md`](../accounting-apbatech/00-profil-perusahaan-dan-master-data.id.md).
>
> Fokus: verifikasi jurnal turunan PO benar per Business Unit — regression check [[project_gl_auto_post_gap_fixed]], [[project_gr_over_receipt_validation]], [[project_pi_payment_requires_approval_gate]].
>
> ⚠️ **`purchase_config_journals` (mapping akun default untuk export-to-journal GR/PI) TIDAK punya kolom `business_unit_id`** (dicek di migration `2026_06_18_000024_create_purchase_config_journals_table.php` dan turunannya — tidak ada). Artinya sistem TIDAK bisa otomatis menurunkan tag `business_unit_id` ke baris jurnal hasil `export-to-journal` berdasarkan config mapping ini. Tag BU pada baris jurnal (mis. Beban/Aset BU-CONSULT, Persediaan/HPP BU-RETAIL) — kalau memang perlu presisi per BU — HARUS di-tag manual/di-edit di jurnal hasil export sebelum `post`, ATAU cukup diandalkan dari `default_business_units_id` di level akun COA-nya sendiri (AST-05/AST-08/AST-09/HPP-01/BBN-04 sudah punya BU default masing-masing di file 00 §4) untuk keperluan `summary-by-account` filter nanti. Dokumentasikan ini sebagai keterbatasan, jangan asumsikan mapping otomatis menurunkan `business_unit_id`.

## A. Alur Internal Konsultan (BU-CONSULT) — Non-Inventory

> Item Lisensi M365/Laptop Dell adalah pengadaan internal, BUKAN barang dagang — GR tetap dipakai sebagai bukti terima barang/jasa sebelum invoice, tapi TIDAK menaikkan akun Persediaan Barang Dagang (AST-05, itu khusus BU-RETAIL). Mapping GR-clearing untuk pembelian non-inventory harus diarahkan ke akun beban/aset tetap yang sesuai (mis. Beban Software License BBN-04 untuk lisensi, Peralatan IT Konsultan AST-08 untuk laptop) via `purchase-configs` mapping — verifikasi mapping ini benar sebelum export-to-journal, karena default mapping banyak sistem mengarah ke akun Persediaan yang di skenario ini tidak relevan.

| Skenario                          | Detail                                                                            | Hasil                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                           | `create` GR dari PO Alur A, terima **penuh** (5 seat Lisensi, 2 unit Laptop Dell) | 201, `status` draft → submit → approve                                                                                                                                                                                                                                                                                                            |
| Negatif — over-receipt            | `create`/`update` GR qty melebihi sisa PO (Laptop qty 3 padahal PO cuma 2)        | 422 ditolak — [[project_gr_over_receipt_validation]]                                                                                                                                                                                                                                                                                              |
| Positif                           | `approve` GR → `export-to-journal`                                                | Jurnal: **Debit** BBN-04/AST-08 (sesuai mapping item) — **Kredit** Utang Usaha (LIA-01) atau akun GR-clearing. Baris Debit otomatis "ber-BU" secara implisit lewat `default_business_units_id` akun BBN-04/AST-08 (`BU-CONSULT`) — TAPI itu properti akun, bukan properti baris jurnal (`business_unit_id` baris tetap NULL kecuali diisi manual) |
| Positif — GL benar-benar tercatat | Cek `general-ledger/detail-ledger` untuk BBN-04/AST-08/LIA-01 setelah export      | Baris GL ada dan seimbang — [[project_gl_auto_post_gap_fixed]]                                                                                                                                                                                                                                                                                    |
| Netralisasi                       | `delete`/`cancel` GR test — cek dulu belum ada PI turunan                         |

### A.2 Purchase Invoice & Payment

| Skenario                 | Detail                                                               | Hasil                                                                                                            |
| ------------------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Positif                  | `create` PI dari GR, termasuk PPN Masukan 11%                        | 201, `total_amount` = 31.500.000 + PPN Masukan 3.465.000                                                         |
| Positif                  | `submit` → `approve` PI → `export-to-journal`                        | Jurnal: **Debit** PPN Masukan (AST-06) + clear GR-clearing, **Kredit** Utang Usaha (LIA-01)                      |
| Positif — status PO sync | Setelah PI approved & fully invoiced, cek status PO                  | PO pindah ke `invoiced` (atau `partially_paid` setelah ada payment — [[project_po_partially_paid_status_added]]) |
| Positif                  | `create` Payment Bill, bayar penuh via Bank BCA Operasional (AST-02) | 201                                                                                                              |
| Negatif — approval gate  | `create`/`mark-paid` Payment sebelum PI `approved`                   | Ditolak — [[project_pi_payment_requires_approval_gate]]                                                          |
| Positif                  | `mark-paid` → `export-to-journal`                                    | Jurnal: **Debit** Utang Usaha (LIA-01), **Kredit** Bank BCA (AST-02)                                             |
| Netralisasi              | Jangan `delete` PI/Payment yang sudah export-to-journal              |

## B. Alur Stok Dagang Elektronik (BU-RETAIL) — Inventory

> **Branch dan user yang sama** dengan Alur A, tidak perlu switch apapun. Berbeda dari Alur A: GR di sini WAJIB menaikkan `sku_stocks` gudang (Gudang Utama Retail) DAN akun Persediaan Barang Dagang Elektronik (AST-05).

| Skenario               | Detail                                                                                               | Hasil                                                                                           |
| ---------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Positif                | `create` GR dari PO Alur B, terima penuh (LPT-001 10, KOM-001 20, KOM-002 15) ke Gudang Utama Retail | 201, `sku_stocks` bertambah sesuai qty                                                          |
| Negatif — over-receipt | GR qty melebihi sisa PO                                                                              | 422 ditolak — [[project_gr_over_receipt_validation]]                                            |
| Positif — landed cost  | `additional-costs/create` — biaya kirim antar-kota Rp 500.000 dialokasikan ke 3 item                 | Harga pokok per unit (untuk HPP nanti) naik proporsional                                        |
| Positif                | `approve` GR → `export-to-journal`                                                                   | Jurnal: **Debit** Persediaan Barang Dagang Elektronik (AST-05), **Kredit** Utang Usaha (LIA-01) |
| Positif — GL tercatat  | Cek `general-ledger/detail-ledger` AST-05 & LIA-01 setelah export                                    | Baris GL ada dan seimbang (naik 82.250.000 + alokasi landed cost)                               |
| Netralisasi            | `delete`/`cancel` GR test — cek dulu belum ada PI/penjualan referensi stok ini                       |

### B.2 Purchase Invoice & Payment

| Skenario    | Detail                                                             | Hasil                                                                                       |
| ----------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Positif     | `create` PI dari GR, termasuk PPN Masukan 11%                      | 201, `total_amount` = 82.250.000 + 9.047.500 = 91.297.500                                   |
| Positif     | `submit` → `approve` PI → `export-to-journal`                      | Jurnal: **Debit** PPN Masukan (AST-06) + clear GR-clearing, **Kredit** Utang Usaha (LIA-01) |
| Positif     | `create` Payment Bill, bayar via Bank Mandiri Operasional (AST-03) | 201                                                                                         |
| Positif     | `mark-paid` → `export-to-journal`                                  | Jurnal: **Debit** Utang Usaha (LIA-01), **Kredit** Bank Mandiri Operasional (AST-03)        |
| Netralisasi | Jangan `delete` PI/Payment yang sudah export-to-journal            |

## C. Verifikasi Akhir — Trial Balance & Breakdown per Business Unit

| Skenario                | Detail                                                                                                        | Hasil                                                                                                                                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                 | `general-ledger/trial-balance` setelah Alur A & B selesai (1 kali panggil, tidak ada lagi "per branch")       | Debit=Kredit; Utang Usaha kembali 0 kalau sudah lunas penuh (gabungan A+B)                                                                                                                                                                                            |
| Positif — breakdown BU  | `general-ledger/summary-by-account {chart_of_account_id:<AST-05>, business_unit_id:<BU-RETAIL>}`              | Total movement AST-05 = kenaikan GR B (82.250.000 + landed cost) — akun ini murni milik BU-RETAIL lewat `default_business_units_id`, walau baris jurnal individual mungkin tidak eksplisit `business_unit_id` (lihat catatan di atas soal `purchase_config_journals`) |
| Netralisasi keseluruhan | Reverse/cancel seluruh dokumen (Payment → PI → GR → PO → PQ → PR) urutan mundur per alur, cek GL balik bersih |

## Referensi Silang

- [`01-po-standalone.id.md`](./01-po-standalone.id.md)
- [`../accounting-apbatech/02-general-ledger-trial-balance-per-branch.id.md`](../accounting-apbatech/02-general-ledger-trial-balance-per-branch.id.md)
- [`../inventory-apbatech/`](../inventory-apbatech/) — verifikasi `sku_stocks` naik konsisten dengan GR B
- [[project_gr_over_receipt_validation]], [[project_gl_auto_post_gap_fixed]], [[project_pi_payment_requires_approval_gate]], [[project_po_partially_paid_status_added]]
