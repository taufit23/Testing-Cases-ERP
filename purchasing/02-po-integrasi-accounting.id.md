---
title: Test Case Purchasing — 02. PO Terintegrasi Accounting (GR → PI → Payment → GL)
category: Testing
description: Lanjutan PO approved dari file 01 ke Goods Receipt, Purchase Invoice, Payment Bill, dan verifikasi posting ke General Ledger (AP control account, PPN Masukan, Persediaan).
visibility: internal
---

# 02. PO Terintegrasi Accounting (GR → PI → Payment → GL)

> Prasyarat: PO approved dari [`01-po-standalone.id.md`](./01-po-standalone.id.md) sudah ada. Skenario perusahaan & COA sama seperti [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md).
>
> Fokus file ini: **setiap dokumen turunan PO memposting jurnal yang benar ke akun yang benar** — ini titik gap paling sering ditemukan (lihat [[project_gl_auto_post_gap_fixed]], [[project_gr_over_receipt_validation]], [[project_pi_payment_requires_approval_gate]]).

## 1. Goods Receipt / Purchase Receipt (**Purchase Receipts**)

| Skenario                          | Detail                                                                                     | Hasil                                                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Positif                            | `create` GR dari PO, terima **penuh** (Minyak 50, Gula 30)                                    | 201, `status` draft → submit → approve                                                                       |
| **Negatif — over-receipt**         | `create`/`update` GR qty melebihi sisa PO (misal Minyak qty 60 padahal PO cuma 50)            | 422 ditolak — regression check [[project_gr_over_receipt_validation]]                                        |
| Positif — landed cost              | `additional-costs/create` — tambah biaya angkut Rp100.000 dialokasikan ke 2 item              | Harga pokok per item (untuk HPP nanti) naik proporsional                                                     |
| Positif                            | `approve` GR → `export-to-journal`                                                             | Jurnal otomatis: **Debit** Persediaan Barang Dagang (1104), **Kredit** Utang Dagang (2101) atau akun GR-clearing sesuai `purchase-configs` mapping |
| **Positif — GL benar-benar tercatat** | Setelah `export-to-journal`, cek `accounting/general-ledger` untuk akun 1104 & 2101            | Baris GL ada dan seimbang — regression check [[project_gl_auto_post_gap_fixed]] (dulu auto-post gak nulis GL) |
| Negatif                            | `export-to-journal` GR yang sudah pernah di-export                                             | Ditolak duplikat, bukan dobel posting                                                                         |
| Netralisasi                        | `delete`/`cancel` GR test — cek dulu belum ada PI yang reference qty diterima ini              |

## 2. Purchase Invoice (**Purchase Invoices**)

| Skenario                          | Detail                                                                                    | Hasil                                                                                                          |
| ------------------------------------ | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Positif                            | `create` PI dari GR (referensi qty diterima), termasuk PPN Masukan 11%                         | 201, `total_amount` = subtotal barang + PPN Masukan (akun 1105)                                                 |
| Negatif                            | `create` PI dengan qty invoice > qty GR yang diterima                                          | 422 (gap serupa GR — kalau tidak ada guard, catat sebagai temuan)                                               |
| Positif                            | `submit` → `approve` PI → `export-to-journal`                                                  | Jurnal: **Debit** PPN Masukan (1105) + clear akun GR-clearing, **Kredit** Utang Dagang (2101)                    |
| **Positif — cek PO status sync**   | Setelah PI approved & fully invoiced, cek status PO                                            | PO pindah ke status `invoiced` (atau `partially_paid` kalau sudah ada payment — lihat [[project_po_partially_paid_status_added]]) |
| Netralisasi                        | Jangan `delete` PI yang sudah export-to-journal — cek dulu belum ada Payment Bill terkait       |

## 3. Purchase Payment Bill (**Purchase Payment Bills**)

| Skenario                                | Detail                                                                                       | Hasil                                                                                                        |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Positif                                  | `create` Payment Bill dari PI approved, bayar penuh via Bank BCA (1102)                            | 201                                                                                                                |
| **Negatif — approval gate**              | `create`/`mark-paid` Payment sebelum PI berstatus `approved`                                        | Ditolak — regression check [[project_pi_payment_requires_approval_gate]] (guard harus di backend, bukan cuma FE) |
| Positif                                  | `mark-paid` → `export-to-journal`                                                                   | Jurnal: **Debit** Utang Dagang (2101), **Kredit** Bank BCA (1102)                                                 |
| **Positif — status PO final**            | Cek status PO setelah payment lunas                                                                 | PO `paid` (fully paid) — kalau bayar termin sebagian, cek `partially_paid` dan urutan termin (lihat [[project_payment_bill_termin_ordering]]) |
| Positif — termin/cicilan (opsional)      | Buat 2 Payment Bill parsial (60% lalu 40%) untuk 1 PI yang sama                                     | Urutan termin sesuai `bill.date` terdekat duluan (bukan urutan input DB) — [[project_payment_bill_termin_ordering]] |
| Netralisasi                              | `cancel` Payment test — cek efek balik ke status PO/PI, jangan `delete` kalau sudah export-to-journal |

## 4. Verifikasi Akhir — Trial Balance & AP Aging

| Skenario                     | Detail                                                                                    | Hasil                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Positif                       | `accounting/reports/trial-balance` setelah seluruh alur GR→PI→Payment selesai                | Total Debit = Total Kredit; Persediaan naik sesuai GR, Utang Dagang balik ke 0 kalau sudah lunas penuh    |
| Positif                       | `accounting/reports/ap-aging` (kalau sudah digarap — lihat [`../_deferred-integrated/06-piutang-dan-utang-aging.id.md`](../_deferred-integrated/06-piutang-dan-utang-aging.id.md)) | PI yang belum lunas muncul dengan umur hutang benar; PI lunas tidak muncul lagi |
| Netralisasi keseluruhan       | Reverse/cancel seluruh dokumen (Payment → PI → GR → PO → PQ → PR) urutan mundur, cek GL balik bersih |

## Referensi Silang

- [`01-po-standalone.id.md`](./01-po-standalone.id.md) — tahap sebelum GR
- [`../accounting/02-general-ledger-neraca-saldo.id.md`](../accounting/02-general-ledger-neraca-saldo.id.md) — cara baca Trial Balance/GL detail
- [[project_gr_over_receipt_validation]], [[project_gl_auto_post_gap_fixed]], [[project_pi_payment_requires_approval_gate]], [[project_po_partially_paid_status_added]], [[project_payment_bill_termin_ordering]]
