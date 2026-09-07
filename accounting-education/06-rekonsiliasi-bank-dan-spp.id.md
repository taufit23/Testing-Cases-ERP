---
title: (Yayasan Pendidikan) — 06. Rekonsiliasi Bank & Catatan PPN
category: accounting-education
description: Rekonsiliasi Bank BNI Operasional Maret 2026 terhadap mutasi jurnal file 01 (biaya admin bank belum tercatat), guard selisih tidak nol pada complete(), dan catatan eksplisit kenapa suite ini tidak punya skenario PPN/tax-summary.
visibility: internal
---

# 06. Rekonsiliasi Bank & Catatan PPN

> Prasyarat: [`01-jurnal-spp-dan-beasiswa.id.md`](./01-jurnal-spp-dan-beasiswa.id.md) selesai — saldo Bank BNI Operasional (AST-03) per buku = **60.125.000** (lihat Ringkasan Saldo Akun Kunci file `01`). Endpoint dikonfirmasi dari `routes/finance.php`, controller `App\Http\Controllers\Finance\BankReconciliations`: `list`, `show`, `create`, `update`, `complete` (POST), `delete`.
>
> **Temuan penting dari kode**: `BankReconciliations` TIDAK punya endpoint/mekanisme "tambah item penyesuaian per baris" (tidak ada `lines`/`items` di payload `create`/`update`) dan `complete()` **TIDAK otomatis membuat jurnal penyesuaian** — hanya membandingkan `statement_balance` vs `closing_balance` (field manual yang diisi user) dan menolak `complete()` kalau `difference != 0` lewat `response()->json()->warn()`. Jurnal penyesuaian (biaya admin bank, dsb) HARUS dibuat manual via **Journals — `create`** terpisah, baru field `closing_balance` di-update ulang lewat `update` sampai `difference = 0`. Ini beda dari asumsi awal skenario (task brief menyebut "adjustment journal auto-creation") — dikoreksi di sini berdasarkan kode aktual, BUKAN diasumsikan dari nama endpoint.

## 6.1 Buat Reconciliation Draft — Periode Maret 2026

Mutasi Bank BNI per pembukuan (jurnal §1.3, §1.5, §1.6, §1.9, §1.10, §1.12, §1.13, §1.14 di file `01`) menghasilkan saldo akhir buku 60.125.000. Mutasi rekening koran (statement) BELUM mencatat biaya admin bank bulanan Rp 25.000 yang baru terpotong otomatis oleh bank — situasi umum di rekening operasional yayasan dengan volume transaksi rendah-menengah.

| Skenario | Payload                                                                                                                                                                                                                                                                                    | Hasil                                                                                                                                                                  |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST finance/bank-reconciliations/create {bank_account_id:<Bank BNI Operasional>, period_start:"2026-03-01", period_end:"2026-03-31", opening_balance:80000000, closing_balance:60125000, statement_balance:60100000, notes:"Rekonsiliasi Maret 2026 — biaya admin bank belum tercatat"}` | 201, `reconciliation_number:"RCN/2026/03/0001"`, `status:"draft"`, `difference: 60100000 - 60125000 = -25000` (dihitung server-side saat create, BUKAN dikirim client) |
| Negatif  | `bank_account_id` tidak ada di branch aktif                                                                                                                                                                                                                                                | 422                                                                                                                                                                    |
| Negatif  | `period_end` sebelum `period_start`                                                                                                                                                                                                                                                        | 422 — validasi `after_or_equal:period_start`                                                                                                                           |

## 6.2 Coba Complete Selagi Masih Ada Selisih

| Skenario | Payload                                                                                                                      | Hasil                                                                                                                                                                                                                                                                   |
| -------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif  | `POST finance/bank-reconciliations/complete {slug:<slug RCN/2026/03/0001>}` (selagi `difference: -25000`, BELUM disesuaikan) | BUKAN 422 — respons `warn()`: `{"message":"Reconciliation has unresolved difference of -25000","difference":-25000}`, `status` TETAP `"draft"` (tidak berubah jadi `"completed"`) — catat perbedaan status HTTP ini kalau tim FE mengharapkan 422 untuk semua penolakan |

## 6.3 Buat Jurnal Penyesuaian Biaya Admin Bank (Manual)

Karena `complete()` tidak membuat jurnal otomatis (lihat catatan pembuka), biaya admin bank harus dibukukan manual dulu sebelum reconciliation bisa di-`update` dan di-`complete`.

| Skenario    | Payload kunci                                                                                                                                                                                                                                                                                                                                                                                                   | Hasil                                                                                                                              |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `POST accounting/journals/create {code:"JRN-EDU-016", date:"2026-03-31", lines:[{BBN-07,debit:25000},{AST-03,credit:25000}]}` lalu `PUT accounting/journals/post`                                                                                                                                                                                                                                               | 201 lalu 200 — Bank BNI Operasional (AST-03) buku sekarang = 60.125.000 − 25.000 = **60.100.000**, sama dengan `statement_balance` |
| Netralisasi | Kalau reconciliation ini murni untuk latihan (bukan baseline permanen), reverse jurnal ini SETELAH §6.4 selesai diverifikasi — TAPI perhatikan: setelah reconciliation di-`complete` (draft-only update/delete guard di §6.5), reverse jurnal historis TIDAK akan mengubah field `closing_balance` yang sudah tersimpan di reconciliation (data reconciliation independen dari GL, tidak re-kalkulasi otomatis) |

## 6.4 Update Reconciliation dengan Closing Balance Baru, lalu Complete

| Skenario                                      | Payload                                                                                            | Hasil                                                                                                                                                                                                                                                                               |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                       | `PUT finance/bank-reconciliations/update {slug:<slug RCN/2026/03/0001>, closing_balance:60100000}` | 200, `difference` di-recalculate = `statement_balance(60100000) - closing_balance(60100000)` = **0**                                                                                                                                                                                |
| Positif                                       | `POST finance/bank-reconciliations/complete {slug:<slug RCN/2026/03/0001>}`                        | 200, `status:"completed"` (karena `difference == 0` sekarang)                                                                                                                                                                                                                       |
| **Negatif — complete lagi setelah completed** | `complete` untuk slug yang sama                                                                    | Query `update()`/`complete()` di controller memfilter `where("status","draft")` — kalau sudah `completed`, `firstOrFail()` akan gagal → error (bukan 422 terstruktur, laporkan behavior aktual: exception 500 atau pesan generik `$th->getMessage()` dari `ModelNotFoundException`) |

## 6.5 Guard — Update/Delete Reconciliation yang Sudah Completed

| Skenario | Detail                                                                                    | Hasil                                                                                                                                                                                                                    |
| -------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Negatif  | `PUT finance/bank-reconciliations/update {slug:<RCN yang sudah completed>, notes:"edit"}` | Sama seperti §6.4 — query `where("status","draft")` gagal `firstOrFail()`, update ditolak (reconciliation completed bersifat immutable)                                                                                  |
| Negatif  | `DELETE finance/bank-reconciliations/delete {id:<id RCN yang sudah completed>}`           | Query delete juga memfilter `where("status","draft")` — baris `completed` TIDAK ikut terhapus meski request "sukses" (`{"deleted":0}` bukan error, hati-hati kalau FE menganggap response sukses = benar-benar terhapus) |

## 6.6 Setoran Kas Bendahara Belum Sepenuhnya Mengendap di Bank (Uncleared)

Setoran kas Bendahara SD ke bank (§1.10 file `01`, Rp 50.000.000, tanggal 2026-03-29) DICATAT di buku tanggal 29 Maret, tapi secara nyata butuh 1-2 hari kerja bank untuk benar-benar mengendap di rekening koran (uncleared deposit in transit) — kasus umum kalau bank reconciliation dilakukan SEBELUM tanggal efektif kliring.

| Skenario                                             | Detail                                                                                                                                                                                                                          | Hasil                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — dokumentasi kasus, bukan endpoint tambahan | Kalau reconciliation dibuat tanggal 30-31 Maret dan setoran §1.10 BELUM kliring di rekening koran per tanggal itu, `statement_balance` yang dimasukkan user harus MENGURANGI 50.000.000 dari saldo real rekening koran saat itu | Sistem TIDAK punya field/mekanisme "uncleared items" terpisah (tidak seperti field `opening_balance`/`closing_balance`/`statement_balance` yang eksplisit) — seluruh look-ahead uncleared-deposit harus dihitung manual oleh user sebelum mengisi `statement_balance`, sama seperti keterbatasan §6.1's catatan pembuka |

## 6.7 Kenapa Suite Ini TIDAK Punya Skenario PPN/Tax Summary

Berbeda dari suite retail/F&B/manufaktur yang punya skenario PPN Keluaran/Masukan dan `reports/tax-summary`, suite pendidikan ini SENGAJA tidak menyentuh keduanya:

- Jasa pendidikan formal (SPP, uang pangkal) **dikecualikan dari PPN** menurut aturan perpajakan Indonesia — tidak ada PPN Keluaran yang perlu dipungut atas pendapatan utama yayasan (lihat file `00`, Profil Perusahaan).
- Pembelian ATK dari supplier (file `01` §1.7) dicatat sebesar nilai bruto tanpa memisahkan PPN Masukan — yayasan pendidikan formal umumnya tidak terdaftar sebagai PKP untuk kegiatan utamanya, sehingga tidak berhak mengkreditkan PPN Masukan.
- `reports/tax-summary` (dikonfirmasi ada di `routes/reports.php`) TETAP bisa dipanggil secara teknis, tapi akan mengembalikan hasil kosong/nol untuk branch ini karena tidak ada `chart_of_accounts.is_tax:true`/`tax_id` yang dikonfigurasi — kalau tim ingin memverifikasi endpoint ini tetap tidak error pada branch tanpa akun pajak, jalankan `POST reports/tax-summary {start_date:"2026-03-01", end_date:"2026-03-31"}` dan pastikan hasilnya kosong/nol, BUKAN exception.

## Netralisasi

- Reconciliation `RCN/2026/03/0001` yang sudah `completed` di §6.4 sengaja dibiarkan sebagai baseline permanen (immutable per §6.5) — TIDAK perlu dan TIDAK BISA dihapus lewat jalur normal.
- Jurnal `JRN-EDU-016` (biaya admin bank) dibiarkan posted sebagai bagian dari saldo akhir Bank BNI Operasional yang sudah dipakai file `04`/`05` — JANGAN reverse kecuali sudah tidak ada laporan lain yang bergantung padanya.

## Referensi Silang

- [`01-jurnal-spp-dan-beasiswa.id.md`](./01-jurnal-spp-dan-beasiswa.id.md) §1.10/§1.12/§1.13/§1.14 — mutasi Bank BNI yang direkonsiliasi di file ini
- [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) §8.3 — pendaftaran awal Bank BNI Operasional lewat `finance/bank-accounts`
- [`../accounting-fnb-kafe/06-rekonsiliasi-bank-setoran-kasir.id.md`](../accounting-fnb-kafe/06-rekonsiliasi-bank-setoran-kasir.id.md) — kasus setoran kasir belum kliring yang serupa dengan §6.6
