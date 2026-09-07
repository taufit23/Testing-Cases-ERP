---
title: (Manufaktur) — 01. Jurnal Manual, Arus Biaya Produksi & Pinjaman Bank
category: accounting-manufaktur
description: Arus biaya produksi lengkap (bahan baku → WIP → barang jadi → HPP) via jurnal manual, akuisisi aset dari pinjaman bank, cicilan pokok+bunga — skenario yang belum pernah dites di suite retail lama.
visibility: internal
---

# 01. Jurnal Manual, Arus Biaya Produksi & Pinjaman Bank

> Prasyarat: [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) sudah lengkap (Modal Pemilik = 369.100.000, Trial Balance balanced). Semua transaksi di file ini bertanggal **Januari 2026** (dalam Q1-2026), `PurchaseConfig.requires_journal_approval = false` (auto-approve jalur pendek, sama seperti Skenario A suite lama).

## 1.1 Pembelian Bahan Baku Lokal (Tunai)

Transaksi: beli bahan baku dari CV Kemasan Jaya Sentosa senilai Rp 40.000.000 + PPN 11% (Rp 4.400.000), tunai dari Bank Mandiri Operasional.

| Skenario    | Payload kunci                                                                                                          | Hasil                                    |
| ----------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| Positif     | `date:"2026-01-08"`, `lines:[{AST-05, debit:40000000},{AST-08, debit:4400000, tax_rate:11},{AST-02, credit:44400000}]` | 201, PENDING_REVIEW → post manual (§1.7) |
| Netralisasi | Reverse setelah posted                                                                                                 |

## 1.2 Pemakaian Bahan Baku ke Produksi (Issue to WIP)

Bahan baku dipakai produksi: Lini A Rp 25.000.000, Lini B Rp 15.000.000 (total Rp 40.000.000) — dimensi Business Unit WAJIB terisi per baris supaya file 04 bisa membedah biaya per lini.

| Skenario                                             | Payload kunci                                                                                                                                                    | Hasil                                                                                                                                                                                                                   |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Positif                                              | `date:"2026-01-10"`, `lines:[{AST-06, debit:25000000, business_unit_id:<Lini A>},{AST-06, debit:15000000, business_unit_id:<Lini B>},{AST-05, credit:40000000}]` | 201 — **jurnal 3-baris, 2 debit ke akun yang SAMA (AST-06) dengan dimensi berbeda** — verifikasi validasi balance tetap benar untuk 2 baris akun identik tapi BU beda (kombinasi yang belum pernah dites di suite lama) |
| **Positif — verifikasi split BU tersimpan terpisah** | `GET .../show`                                                                                                                                                   | 2 baris AST-06 muncul terpisah (bukan digabung jadi 1 baris 40.000.000 tanpa BU) — kalau backend/FE menggabungkan baris dengan akun sama, dimensi Lini A vs B akan hilang                                               | Kalau tergabung → 🆕 gap (harus dites, laporkan kalau ternyata terjadi) |
| Netralisasi                                          | Reverse setelah posted                                                                                                                                           |

## 1.3 Tenaga Kerja Langsung Pabrik → WIP (dengan Potongan PPh 21)

Gaji tenaga kerja pabrik Rp 30.000.000 dikapitalisasi ke WIP (bukan expense langsung, sesuai costing manufaktur) — dibayar bersih, potongan PPh 21 ditahan sebagai utang.

| Skenario    | Payload kunci                                                                                              | Hasil                                                                              |
| ----------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Positif     | `date:"2026-01-15"`, `lines:[{AST-06, debit:30000000},{AST-02, credit:28500000},{LIA-04, credit:1500000}]` | 201 — saldo LIA-04 setelah posted: 3.000.000 (opening) + 1.500.000 = **4.500.000** |
| Netralisasi | Reverse setelah posted (saldo LIA-04 balik ke 3.000.000)                                                   |

## 1.4 Overhead Pabrik → WIP (Produk) vs Overhead Non-Produksi Langsung (Periode)

Dua jenis overhead pabrik dengan perlakuan BEDA — satu masuk product cost (WIP), satu lagi period cost (expense langsung). Kasus nyata: listrik mesin produksi masuk WIP, tapi gaji satpam/admin pabrik adalah period cost.

| Skenario                                                        | Payload kunci                                                                     | Hasil                                                                                                                                                              |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif — overhead produksi (ke WIP)                            | `date:"2026-01-16"`, `lines:[{AST-06, debit:12000000},{AST-02, credit:12000000}]` | 201 — WIP bertambah 12.000.000                                                                                                                                     |
| Positif — overhead non-produksi (period cost, expense langsung) | `date:"2026-01-16"`, `lines:[{BBN-02, debit:5000000},{AST-02, credit:5000000}]`   | 201 — **langsung ke Beban, TIDAK lewat WIP** — beda pola dari baris di atas, verifikasi user/FE tidak keliru menganggap semua "overhead pabrik" otomatis masuk WIP |
| Netralisasi                                                     | Reverse keduanya setelah posted                                                   |

## 1.5 Penyelesaian Produksi (WIP → Barang Jadi)

Setelah §1.2-1.4, total WIP bertambah = 40.000.000 (§1.2) + 30.000.000 (§1.3) + 12.000.000 (§1.4) = 82.000.000. WIP awal 15.000.000, jadi WIP sebelum completion = **97.000.000**. Produksi selesai senilai Rp 90.000.000 (sisa 7.000.000 tetap WIP, belum selesai).

| Skenario    | Payload kunci                                                                                                                       | Hasil                                                                                                                                                                               |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `date:"2026-01-20"`, `lines:[{AST-07, debit:90000000},{AST-06, credit:90000000}]`                                                   | 201 — **verifikasi setelah posted**: saldo AST-06 (WIP) = 97.000.000 − 90.000.000 = **7.000.000**, saldo AST-07 (Barang Jadi) = 25.000.000 (opening) + 90.000.000 = **115.000.000** |
| Netralisasi | Reverse setelah posted (urutan mundur — reverse ini SEBELUM reverse §1.2-1.4 kalau mau bongkar total, karena WIP saling bergantung) |

## 1.6 Penjualan Barang Jadi ke Distributor (Kredit) + Pengakuan HPP

Penjualan kredit ke PT Nusantara Snack Distribusindo — Lini A senilai Rp 70.000.000 + PPN 11% (Rp 7.700.000). HPP yang diakui bersamaan: Rp 55.000.000 (dari Barang Jadi).

| Skenario                                                                     | Payload kunci                                                                                                                                                                                                                                                                                                                                                                                                                             | Hasil                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| Positif — pengakuan pendapatan                                               | `date:"2026-01-25"`, `lines:[{AST-04, debit:77700000},{PDT-01, credit:70000000, business_unit_id:<Lini A>},{LIA-03, credit:7700000, tax_rate:11}]`                                                                                                                                                                                                                                                                                        | 201                                                                                                                                                                                                    |
| Positif — pengakuan HPP (jurnal terpisah, tanggal sama)                      | `lines:[{BBN-01, debit:55000000},{AST-07, credit:55000000}]`                                                                                                                                                                                                                                                                                                                                                                              | 201 — **verifikasi setelah kedua jurnal posted**: saldo AST-07 (Barang Jadi) = 115.000.000 − 55.000.000 = **60.000.000**, saldo AST-04 (Piutang) = 45.000.000 (opening) + 77.700.000 = **122.700.000** |
| **Negatif — 2 jurnal terpisah untuk 1 transaksi bisnis (desain, bukan bug)** | Sengaja dipisah 2 jurnal (bukan 1 jurnal 5-baris) supaya lebih mudah ditelusuri di audit trail — kalau mau digabung jadi 1 jurnal 5-baris balanced, boleh juga (`Dr Piutang 77.700.000 / Cr Penjualan 70.000.000 / Cr PPN Keluaran 7.700.000 / Dr HPP 55.000.000 / Cr Barang Jadi 55.000.000`) — dites SATU pola saja cukup, catat kalau ada perbedaan hasil antara digabung vs dipisah (seharusnya TIDAK ada beda, cuma gaya pencatatan) | —                                                                                                                                                                                                      | ✅  |
| Netralisasi                                                                  | Reverse kedua jurnal setelah posted                                                                                                                                                                                                                                                                                                                                                                                                       |

## 1.7 Susut Bahan Baku (Opname Gudang)

Selisih fisik bahan baku saat opname: kurang Rp 800.000 dari catatan (spoilage/kerusakan, umum di manufaktur pangan).

| Skenario    | Payload kunci                                                                 | Hasil                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `date:"2026-01-27"`, `lines:[{BBN-08, debit:800000},{AST-05, credit:800000}]` | 201 — **verifikasi**: saldo AST-05 (Bahan Baku) = 60.000.000 (opening) + 40.000.000 (§1.1) − 40.000.000 (§1.2) − 800.000 = **59.200.000** |
| Netralisasi | Reverse setelah posted                                                        |

## 1.8 Pinjaman Bank + Akuisisi Mesin & Kendaraan

Pencairan pinjaman investasi mesin Rp 150.000.000, dipakai LANGSUNG beli Mesin Produksi (total Rp 180.000.000, sisa Rp 30.000.000 dari kas sendiri). Kendaraan Operasional (truck box) Rp 250.000.000 dibayar tunai penuh, TIDAK lewat pinjaman.

> **Catatan proses 2-langkah (bukan bug)**: **Assets — `create`** HANYA mendaftarkan aset (nilai buku awal) — TIDAK otomatis posting jurnal akuisisi (beda dengan depresiasi bulanan yang auto-post, lihat file 05 §5.2). Jurnal akuisisi harus dibuat manual terpisah, seperti di bawah ini. Kalau salah satu langkah lupa dikerjakan, nilai buku di modul Fixed Assets akan "mengambang" tanpa jejak GL — bukan error yang kelihatan, jadi WAJIB selalu dites keduanya.
>
> **Kontrak field asli Assets — `create`** (verifikasi baca kode langsung, `App\Http\Controllers\Finance\FixedAssets::create()`) — payload di bawah SUDAH disesuaikan ke kontrak asli, catatan penting:
> - `asset_code` TIDAK bisa diisi manual — server SELALU generate sendiri format `FA/{tahun}/{urutan}` (mis. `FA/2026/0001`), field ini di-strip diam-diam kalau dikirim di payload.
> - `category` cuma menerima salah satu dari 6 nilai fix: `land|building|vehicle|equipment|furniture|intangible` — BUKAN teks bebas. "Mesin Produksi" dipetakan ke `equipment`, "Kendaraan" ke `vehicle`.
> - Nama field yang benar adalah `salvage_value`, BUKAN `residual_value` — field asing di-strip diam-diam tanpa error, `salvage_value` kesimpan 0 tanpa peringatan apapun kalau salah nama field.
> - `current_book_value` saat registrasi = **full `acquisition_cost`** (BUKAN dikurangi `salvage_value` di muka) — `salvage_value` cuma dipakai buat hitung rate penyusutan nanti (file 05), book value baru turun setelah depresiasi beneran di-run. 🔧 Ini sempat jadi bug BE (`current_book_value` dihitung `acquisition_cost - salvage_value` sejak hari pertama, padahal belum ada penyusutan) — sudah difix.
> - **BARU**: `currency_id` (opsional) sekarang didukung — `acquisition_cost`/`salvage_value` dianggap dalam unit `currency_id` tsb, dikonversi ke base currency via `ExchangeRate::rateFor()` SEBELUM disimpan (kolom `acquisition_cost`/`salvage_value` di DB tetap base-currency truth). `rateFor()` mengambil rate yang SEDANG AKTIF (`is_active=true`) untuk currency itu SAAT create dipanggil — BUKAN rate pada `acquisition_date` (sistem tidak punya konsep rate historis per tanggal). Nilai asli + rate yang dipakai disimpan di `foreign_acquisition_cost`/`foreign_salvage_value`/`exchange_rate` untuk audit trail. Sebelumnya modul ini TIDAK BISA input aset dibeli pakai mata uang asing sama sekali (gap, sudah ditutup).

| Skenario                                                    | Payload kunci                                                                                                                                                                                                                                                                                       | Hasil                                                            |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Positif — daftar Mesin Produksi                             | `POST fixed-assets/assets/create {name:"Mesin Pengiris & Penggorengan Otomatis", category:"equipment", acquisition_date:"2026-01-05", acquisition_cost:180000000, salvage_value:18000000, useful_life_months:60, depreciation_method:"straight_line", status:"active"}` | 201, `current_book_value:180000000` (= full acquisition cost; `asset_code` auto-generate `FA/2026/xxxx`) |
| Positif — daftar Kendaraan                                  | `POST fixed-assets/assets/create {name:"Truck Box Pengiriman", category:"vehicle", acquisition_date:"2026-01-05", acquisition_cost:250000000, salvage_value:40000000, useful_life_months:96, depreciation_method:"declining_balance", status:"active"}`                    | 201, `current_book_value:250000000` (= full acquisition cost; `asset_code` auto-generate `FA/2026/xxxx`) |
| Positif — jurnal akuisisi (pencairan pinjaman + beli mesin) | `date:"2026-01-05"`, `lines:[{AST-09, debit:180000000},{AST-02, credit:30000000},{LIA-05, credit:150000000}]`                                                                                                                                                                                       | 201 — saldo LIA-05 = 0 (opening) + 150.000.000 = **150.000.000** |
| Positif — jurnal akuisisi kendaraan (tunai)                 | `date:"2026-01-05"`, `lines:[{AST-11, debit:250000000},{AST-02, credit:250000000}]`                                                                                                                                                                                                                 | 201                                                              |
| Netralisasi                                                 | Reverse jurnal akuisisi setelah posted — TAPI kalau sudah kepakai file 05 (penyusutan), jangan reverse, buat aset test baru terpisah untuk eksperimen lain                                                                                                                                          |

## 1.9 Cicilan Pinjaman Bulan Pertama (Pokok + Bunga)

Bunga dihitung 1%/bulan dari saldo pinjaman (simplifikasi flat, bukan anuitas) — cicilan pertama: pokok Rp 5.000.000 + bunga Rp 1.500.000, total dibayar Rp 6.500.000.

| Skenario                                      | Payload kunci                                                                                           | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif                                       | `date:"2026-01-31"`, `lines:[{LIA-05, debit:5000000},{BBN-06, debit:1500000},{AST-02, credit:6500000}]` | 201 — saldo LIA-05 setelah posted = 150.000.000 − 5.000.000 = **145.000.000**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Negatif — bayar lebih dari saldo pinjaman** | Coba cicilan dengan pokok `debit: 200000000` (lebih besar dari saldo LIA-05 yang cuma 150.000.000)      | Cek behavior aktual: apakah ada validasi yang menolak (saldo akun tidak boleh "negatif" untuk akun kontrol tertentu), atau lolos begitu saja membuat LIA-05 bersaldo debit (piutang ke bank, tidak masuk akal). Kalau lolos tanpa peringatan → 🔧 **improvement kecil**: akun ber-flag tertentu (liability control account) idealnya dapat soft-warning kalau transaksi membuat saldonya berbalik arah dari `normal_balance`-nya — TAPI ini juga bisa false-positive legit (liability kadang memang boleh overpaid sementara), jadi warning bukan hard-block |
| Netralisasi                                   | Reverse setelah posted                                                                                  |

## 1.10 Post & Reverse (Regression Check dari Suite Lama)

| Skenario            | Detail                                                                                                                                    | Hasil                                            |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Positif — post-bulk | Semua jurnal draft/pending §1.1-1.9 sekaligus → `PUT accounting/journals/post-bulk`                                                       | Semua ter-post, GL entries kebuat untuk semuanya |
| Positif             | Verifikasi total GL cocok dengan semua angka "Hasil" di atas — kumpulkan di 1 query `general-ledger/trial-balance` sebelum lanjut file 02 | Balanced, tidak ada selisih                      |
| Netralisasi         | — (biarkan semua tetap posted, jadi baseline file 02-06)                                                                                  |

## Ringkasan Saldo Akun Kunci Setelah File 01 (Baseline untuk File 02-06)

| Akun                            |                                                                                                                              Saldo Setelah File 01 |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------: |
| AST-02 Bank Mandiri Operasional | 200.000.000 − 44.400.000 − 28.500.000 − 12.000.000 − 5.000.000 − 30.000.000 − 250.000.000 − 6.500.000 = **-176.400.000** ⚠️ lihat catatan di bawah |
| AST-05 Persediaan Bahan Baku    |                                                                                                                                         59.200.000 |
| AST-06 Persediaan WIP           |                                                                                                                                          7.000.000 |
| AST-07 Persediaan Barang Jadi   |                                                                                                                                         60.000.000 |
| AST-04 Piutang Dagang           |                                                                                                                                        122.700.000 |
| AST-09 Mesin Produksi           |                                                                                                                                        180.000.000 |
| AST-11 Kendaraan Operasional    |                                                                                                                                        250.000.000 |
| LIA-04 Utang PPh 21 Karyawan    |                                                                                                                                          4.500.000 |
| LIA-05 Utang Bank               |                                                                                                                                        145.000.000 |

> **⚠️ Catatan penting — Bank Mandiri Operasional NEGATIF setelah semua transaksi**: dengan saldo awal 200.000.000, total pengeluaran di file ini (44.400.000+28.500.000+12.000.000+5.000.000+30.000.000+250.000.000+6.500.000 = 376.400.000) MELEBIHI saldo awal — hasil akhir **minus Rp 176.400.000**. Ini SENGAJA dibiarkan sebagai skenario "kas menipis, butuh suntikan modal tambahan" yang realistis di lapangan (perusahaan manufaktur baru investasi besar-besaran) — bukan kesalahan hitung.

| Skenario                                   | Detail                                                                                                                    | Hasil                                                                                                                                      | Label temuan                                                                                                                                                                                                                                             |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Negatif — cek apakah overdraft ditolak** | Sebelum menambah jurnal suntikan modal di bawah, post urutan jurnal §1.1-1.9 sampai salah satu membuat saldo AST-02 minus | Cek behavior aktual: apakah ada validasi yang menolak transaksi kas/bank sampai saldo minus (overdraft check), atau lolos tanpa peringatan | Kalau lolos tanpa peringatan sama sekali → 🔧 **improvement kecil**: akun ber-flag `is_cash_account:true` idealnya bisa dapat opsional warning "saldo kas/bank akan menjadi negatif" (bukan hard block, overdraft/cerukan bank itu valid di dunia nyata) |
| Positif — suntikan modal tambahan          | **WAJIB sebelum lanjut file 02/06**: `lines:[{AST-02, debit:200000000},{EKT-01, credit:200000000}]`, `date:"2026-01-31"`  | Saldo AST-02 akhir jadi **23.600.000** — kalau langkah ini terlewat, seluruh angka Bank Mandiri Operasional di file 02/06 akan meleset     |

## Referensi Silang

- [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) — saldo awal & master data
- [`02-multi-currency-dan-selisih-kurs.id.md`](./02-multi-currency-dan-selisih-kurs.id.md) — lanjutan transaksi valas, butuh saldo AST-02/AST-03 dari file ini
- [`03-anggaran-kuartalan-dan-aset-tetap.id.md`](./03-anggaran-kuartalan-dan-aset-tetap.id.md) — penyusutan bulanan Mesin Produksi & Kendaraan yang didaftarkan di §1.8 (WAJIB dikerjakan SEBELUM file 04 Tutup Periode — lihat catatan urutan di file itu)
