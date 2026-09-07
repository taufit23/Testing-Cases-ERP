---
title: (F&B Kafe) — 01. Jurnal Harian Penjualan & Akumulasi
category: accounting-fnb-kafe
description: Inti suite ini — 5 hari rekap penjualan kas harian (10 baris/jurnal, 3 outlet x 2 kategori menu + PPN) diakumulasi jadi total presisi, plus restock bahan baku kredit, gaji, listrik, setoran kasir ke bank, voucher prabayar, selisih kas, dan akuisisi 2 aset tetap. Semua angka diverifikasi manual baris-per-baris.
visibility: internal
---

# 01. Jurnal Harian Penjualan & Akumulasi

> Prasyarat: [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) sudah lengkap (Modal Pemilik = 67.700.000, Trial Balance balanced). Semua transaksi di file ini bertanggal **Februari 2026** (dalam periode Accounting Period Februari yang harus sudah `is_closed:false`), `PurchaseConfig.requires_journal_approval = false` (auto-approve jalur pendek, sama seperti Skenario A di suite retail).
>
> **Kenapa file ini penting**: ini adalah inti tema suite — bukan 1-2 transaksi besar seperti suite retail/manufaktur, tapi PULUHAN baris jurnal bernilai kecil (Rp 230.000 - Rp 3,6jt per baris) yang harus terakumulasi PERSIS ke total akhir. Kalau ada satu baris saja salah tanggal/salah akun/salah `business_unit_id`, akumulasi akan meleset dan langsung ketahuan di file `02` (Trial Balance) karena semua angka Hasil di bawah sudah diverifikasi manual dobel (identitas debit=kredit dicek tiap baris, lalu ditotal ulang dari nol via T-account).

## 1.1 - 1.5 Rekap Penjualan Kas Harian (5 Hari Kerja, 3 Outlet x 2 Kategori Menu)

Tiap hari kasir 3 outlet setor rekap penjualan (dari EOD report kasir/POS internal, di luar sistem ERP) ke akuntan, yang merekapnya jadi **1 jurnal manual 10-baris**: 3 baris debit (kas kasir tiap outlet, terima tunai), 6 baris kredit pendapatan (2 kategori menu x 3 outlet, akun SAMA `PDT-01`/`PDT-02` tapi `business_unit_id` beda — pola split-baris-akun-sama yang juga dites di suite manufaktur), 1 baris kredit PPN Keluaran (agregat, tanpa dimensi outlet).

**Cara baca tabel per hari**: kolom Minuman/Makanan = harga jual belum PPN (base), Subtotal = Minuman+Makanan, PPN = 11% dari Subtotal (selalu bilangan bulat karena Subtotal selalu kelipatan 100), Total Kas = Subtotal+PPN (yang diterima kasir tunai).

### 1.1 Hari 1 — Senin, 2026-02-02

| Outlet           |       Minuman |       Makanan |      Subtotal |     PPN 11% |     Total Kas |
| ---------------- | ------------: | ------------: | ------------: | ----------: | ------------: |
| Kemang           |     1.850.000 |       620.000 |     2.470.000 |     271.700 |     2.741.700 |
| Senayan          |     1.240.000 |       410.000 |     1.650.000 |     181.500 |     1.831.500 |
| BSD              |       780.000 |       260.000 |     1.040.000 |     114.400 |     1.154.400 |
| **Total Hari 1** | **3.870.000** | **1.290.000** | **5.160.000** | **567.600** | **5.727.600** |

| Skenario                                                          | Payload kunci                                                                                                                                                                                                                                                                                                                                              | Hasil                                                                                                                                                                         |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                           | `date:"2026-02-02"`, `lines:[{AST-01,debit:2741700,bu:Kemang},{AST-02,debit:1831500,bu:Senayan},{AST-03,debit:1154400,bu:BSD},{PDT-01,credit:1850000,bu:Kemang},{PDT-01,credit:1240000,bu:Senayan},{PDT-01,credit:780000,bu:BSD},{PDT-02,credit:620000,bu:Kemang},{PDT-02,credit:410000,bu:Senayan},{PDT-02,credit:260000,bu:BSD},{LIA-02,credit:567600}]` | 201 — jurnal 10 baris balanced (Dr 5.727.600 = Cr 5.727.600), PENDING_REVIEW → post manual di §1.10                                                                           |
| **Positif — verifikasi split baris akun sama tersimpan terpisah** | `GET .../show`                                                                                                                                                                                                                                                                                                                                             | 3 baris `PDT-01` dan 3 baris `PDT-02` muncul TERPISAH per outlet (bukan digabung 1 baris tanpa dimensi) — kalau tergabung → 🆕 gap, dimensi outlet hilang dari laporan per-BU |

### 1.2 Hari 2 — Selasa, 2026-02-03

| Outlet           |       Minuman |       Makanan |      Subtotal |     PPN 11% |     Total Kas |
| ---------------- | ------------: | ------------: | ------------: | ----------: | ------------: |
| Kemang           |     2.100.000 |       705.000 |     2.805.000 |     308.550 |     3.113.550 |
| Senayan          |     1.320.000 |       455.000 |     1.775.000 |     195.250 |     1.970.250 |
| BSD              |       690.000 |       230.000 |       920.000 |     101.200 |     1.021.200 |
| **Total Hari 2** | **4.110.000** | **1.390.000** | **5.500.000** | **605.000** | **6.105.000** |

| Skenario | Detail                                                            | Hasil                   |
| -------- | ----------------------------------------------------------------- | ----------------------- |
| Positif  | Sama pola §1.1, `date:"2026-02-03"`, nominal sesuai tabel di atas | 201, balanced 6.105.000 |

### 1.3 Hari 3 — Rabu, 2026-02-04

| Outlet           |       Minuman |       Makanan |      Subtotal |     PPN 11% |     Total Kas |
| ---------------- | ------------: | ------------: | ------------: | ----------: | ------------: |
| Kemang           |     1.960.000 |       640.000 |     2.600.000 |     286.000 |     2.886.000 |
| Senayan          |     1.180.000 |       390.000 |     1.570.000 |     172.700 |     1.742.700 |
| BSD              |       810.000 |       275.000 |     1.085.000 |     119.350 |     1.204.350 |
| **Total Hari 3** | **3.950.000** | **1.305.000** | **5.255.000** | **578.050** | **5.833.050** |

| Skenario                             | Detail                                                                                                                      | Hasil                                                                                                                                                                                  |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                              | `date:"2026-02-04"`, nominal sesuai tabel                                                                                   | 201, balanced 5.833.050                                                                                                                                                                |
| **Negatif — jurnal sengaja timpang** | Buat jurnal test terpisah dengan salah satu baris kredit dikurangi 1 rupiah (mis. `PDT-01 Kemang: 1959999` bukan `1960000`) | Ditolak — total debit ≠ total kredit, sistem HARUS menolak walau selisihnya cuma Rp 1 (uji sensitivitas validasi balance di angka kecil, relevan karena suite ini penuh nominal kecil) |
| Netralisasi                          | Hapus jurnal test timpang di atas sebelum lanjut                                                                            |

### 1.4 Hari 4 — Kamis, 2026-02-05

| Outlet           |       Minuman |       Makanan |      Subtotal |     PPN 11% |     Total Kas |
| ---------------- | ------------: | ------------: | ------------: | ----------: | ------------: |
| Kemang           |     2.250.000 |       700.000 |     2.950.000 |     324.500 |     3.274.500 |
| Senayan          |     1.410.000 |       480.000 |     1.890.000 |     207.900 |     2.097.900 |
| BSD              |       760.000 |       240.000 |     1.000.000 |     110.000 |     1.110.000 |
| **Total Hari 4** | **4.420.000** | **1.420.000** | **5.840.000** | **642.400** | **6.482.400** |

| Skenario | Detail                                    | Hasil                   |
| -------- | ----------------------------------------- | ----------------------- |
| Positif  | `date:"2026-02-05"`, nominal sesuai tabel | 201, balanced 6.482.400 |

### 1.5 Hari 5 — Jumat, 2026-02-06 (hari tersibuk, persiapan weekend)

| Outlet           |       Minuman |       Makanan |      Subtotal |     PPN 11% |     Total Kas |
| ---------------- | ------------: | ------------: | ------------: | ----------: | ------------: |
| Kemang           |     2.480.000 |       810.000 |     3.290.000 |     361.900 |     3.651.900 |
| Senayan          |     1.550.000 |       520.000 |     2.070.000 |     227.700 |     2.297.700 |
| BSD              |       890.000 |       300.000 |     1.190.000 |     130.900 |     1.320.900 |
| **Total Hari 5** | **4.920.000** | **1.630.000** | **6.550.000** | **720.500** | **7.270.500** |

| Skenario               | Detail                                                                                                                                        | Hasil                   |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Positif                | `date:"2026-02-06"`, nominal sesuai tabel                                                                                                     | 201, balanced 7.270.500 |
| Netralisasi (§1.1-1.5) | Reverse ke-5 jurnal setelah posted (§1.10) kalau mau bongkar total — urutan bebas, tidak saling bergantung seperti kasus WIP suite manufaktur |

### Rekap Akumulasi 5 Hari (Verifikasi Silang — WAJIB cocok sebelum lanjut)

| Item                        |    Hari 1 |    Hari 2 |    Hari 3 |    Hari 4 |    Hari 5 | **Total 5 Hari** |
| --------------------------- | --------: | --------: | --------: | --------: | --------: | ---------------: |
| Pendapatan Minuman (PDT-01) | 3.870.000 | 4.110.000 | 3.950.000 | 4.420.000 | 4.920.000 |   **21.270.000** |
| Pendapatan Makanan (PDT-02) | 1.290.000 | 1.390.000 | 1.305.000 | 1.420.000 | 1.630.000 |    **7.035.000** |
| PPN Keluaran (LIA-02)       |   567.600 |   605.000 |   578.050 |   642.400 |   720.500 |    **3.113.550** |
| Total Kas Masuk             | 5.727.600 | 6.105.000 | 5.833.050 | 6.482.400 | 7.270.500 |   **31.418.550** |

Verifikasi silang: (21.270.000 + 7.035.000) × 11% = 28.305.000 × 11% = **3.113.550** — HARUS persis sama dengan total PPN Keluaran di atas. Kalau beda walau Rp 1, ada salah hitung di salah satu baris harian sebelum lanjut.

**Breakdown per outlet (dipakai verifikasi dimensi Business Unit di file `02`)**:

| Outlet    |                                             Total Kas Masuk 5 Hari |
| --------- | -----------------------------------------------------------------: |
| Kemang    | 2.741.700+3.113.550+2.886.000+3.274.500+3.651.900 = **15.667.650** |
| Senayan   |  1.831.500+1.970.250+1.742.700+2.097.900+2.297.700 = **9.940.050** |
| BSD       |  1.154.400+1.021.200+1.204.350+1.110.000+1.320.900 = **5.810.850** |
| **Total** |              **31.418.550** (cocok dengan Total Kas Masuk di atas) |

## 1.6 Pemakaian Bahan Baku Mingguan (Estimasi HPP ~35% dari Pendapatan)

Estimasi COGS F&B kafe (rasio umum industri ~33-38%) dari total Subtotal 5 hari 28.305.000 × 35% = **9.906.750**.

| Skenario    | Payload kunci                                                                 | Hasil                                                                                                  |
| ----------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Positif     | `date:"2026-02-06"`, `lines:[{BBN-01,debit:9906750},{AST-06,credit:9906750}]` | 201 — Persediaan Bahan Baku (AST-06) setelah posted = 15.000.000 (opening) − 9.906.750 = **5.093.250** |
| Netralisasi | Reverse setelah posted                                                        |

## 1.7 Restock Bahan Baku (Kredit dari Supplier)

Persediaan menipis (§1.6), restock dari CV Sumber Nikmat Boga senilai Rp 20.000.000 + PPN 11% (Rp 2.200.000), **kredit** (utang dagang, bukan tunai — termin 30 hari sesuai Contact di file `00` §8).

| Skenario    | Payload kunci                                                                                                      | Hasil                                                                                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `date:"2026-02-06"`, `lines:[{AST-06,debit:20000000},{AST-07,debit:2200000,tax_rate:11},{LIA-01,credit:22200000}]` | 201 — Persediaan setelah posted = 5.093.250 + 20.000.000 = **25.093.250**, Utang Dagang (LIA-01) = 6.000.000 (opening) + 22.200.000 = **28.200.000** |
| Netralisasi | Reverse setelah posted                                                                                             |

## 1.8 Setoran Kasir ke Bank Pusat (Akhir Minggu)

Tiap outlet menyetor sebagian besar kas kasirnya ke Bank BCA Operasional, menyisakan sedikit sebagai kas kecil/modal kembalian minggu depan. **Catatan penting untuk file `06`**: nominal di jurnal ini adalah nominal yang DICATAT akuntan berdasarkan slip setoran kasir — BELUM tentu sama dengan yang benar-benar masuk ke mutasi rekening bank (dites di file `06` §6.2).

| Skenario                  | Payload kunci                                                                             | Hasil                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Positif — setoran Kemang  | `date:"2026-02-06"`, `lines:[{AST-04,debit:17000000},{AST-01,credit:17000000,bu:Kemang}]` | 201 — Kas Kasir Kemang tersisa = 2.000.000 (opening) + 15.667.650 (§1.1-1.5) − 17.000.000 = **667.650**   |
| Positif — setoran Senayan | `lines:[{AST-04,debit:11000000},{AST-02,credit:11000000,bu:Senayan}]`                     | 201 — Kas Kasir Senayan tersisa = 1.500.000 + 9.940.050 − 11.000.000 = **440.050**                        |
| Positif — setoran BSD     | `lines:[{AST-04,debit:6500000},{AST-03,credit:6500000,bu:BSD}]`                           | 201 — Kas Kasir BSD tersisa = 1.000.000 + 5.810.850 − 6.500.000 = **310.850** (sebelum §1.13 selisih kas) |
| Netralisasi               | Reverse ketiganya setelah posted                                                          |

## 1.9 Gaji Karyawan (Barista/Kasir) dengan Potongan PPh 21

Gaji kotor mingguan tim gabungan 3 outlet Rp 12.000.000, potongan PPh 21 Rp 600.000, dibayar bersih dari Bank BCA.

| Skenario    | Payload kunci                                                                                          | Hasil                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Positif     | `date:"2026-02-06"`, `lines:[{BBN-02,debit:12000000},{LIA-03,credit:600000},{AST-04,credit:11400000}]` | 201 — Utang PPh 21 (LIA-03) setelah posted = 800.000 (opening) + 600.000 = **1.400.000** |
| Netralisasi | Reverse setelah posted                                                                                 |

## 1.10 Beban Listrik & Gas (Split per Outlet)

Tagihan listrik & gas mingguan gabungan Rp 1.500.000, dibayar dari Bank BCA, dialokasikan per outlet (dimensi Business Unit pada akun BEBAN, bukan cuma akun kas).

| Skenario    | Payload kunci                                                                                                                                        | Hasil                                         |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Positif     | `date:"2026-02-06"`, `lines:[{BBN-03,debit:700000,bu:Kemang},{BBN-03,debit:500000,bu:Senayan},{BBN-03,debit:300000,bu:BSD},{AST-04,credit:1500000}]` | 201, total debit 1.500.000 = kredit 1.500.000 |
| Netralisasi | Reverse setelah posted                                                                                                                               |

## 1.11 Penjualan Paket Voucher Korporat (Kredit + Pendapatan Diterima Dimuka)

PT Solusi Rapat Sejahtera (Contact file `00` §8) memesan 50 voucher kopi @Rp 100.000 untuk keperluan meeting kantor, dibayar TERMIN 30 hari (Piutang Dagang). Karena voucher BELUM diredeem, tidak diakui sebagai pendapatan langsung — masuk **Pendapatan Diterima Dimuka** dulu.

| Skenario                                                                | Payload kunci                                                                                                                     | Hasil                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — penjualan voucher                                             | `date:"2026-02-06"`, `lines:[{AST-05,debit:5550000},{LIA-04,credit:5000000},{LIA-02,credit:550000,tax_rate:11}]`                  | 201 — Piutang Dagang (AST-05) = 8.000.000 (opening) + 5.550.000 = **13.550.000**; Pendapatan Diterima Dimuka (LIA-04) = 3.000.000 (opening) + 5.000.000 = **8.000.000**                                                                                                                                                                     |
| **Positif — redemption sebagian (20 voucher dipakai di Outlet Kemang)** | `date:"2026-02-06"`, `lines:[{LIA-04,debit:2000000},{PDT-01,credit:2000000,bu:Kemang}]`                                           | 201 — **baru sekarang** diakui sebagai pendapatan (bukan saat voucher terjual) — Pendapatan Diterima Dimuka tersisa = 8.000.000 − 2.000.000 = **6.000.000**, Pendapatan Minuman Kemang bertambah 2.000.000 (TIDAK ada PPN tambahan di baris ini, karena PPN sudah dipungut penuh saat penjualan voucher)                                    |
| **Negatif — redemption melebihi saldo voucher tersisa**                 | Coba redemption `debit: 10000000` (lebih besar dari saldo LIA-04 tersisa)                                                         | Cek behavior aktual: apakah ada validasi yang menolak (saldo liability tidak boleh berbalik arah), atau lolos begitu saja membuat LIA-04 bersaldo debit (voucher "minus", tidak masuk akal secara bisnis) — kalau lolos tanpa peringatan → 🔧 **improvement kecil**, sama kategori dengan temuan overpay liability di suite manufaktur §1.9 |
| Netralisasi                                                             | Reverse redemption dulu, baru reverse penjualan voucher (urutan mundur, karena redemption bergantung saldo LIA-04 dari penjualan) |

## 1.12 Selisih Kas Kasir Outlet BSD (Opname Fisik)

Spot-check kas fisik Outlet BSD akhir minggu: tercatat 310.850 (§1.8), tapi hasil hitung fisik cuma 305.850 — kurang Rp 5.000 (uang receh hilang/kembalian salah, kasus umum di kafe volume tinggi dengan banyak uang receh).

| Skenario    | Payload kunci                                                                         | Hasil                                                                                                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `date:"2026-02-06"`, `lines:[{BBN-04,debit:5000,bu:BSD},{AST-03,credit:5000,bu:BSD}]` | 201 — **nominal terkecil di seluruh suite ini (Rp 5.000)**, sengaja dipakai menguji sistem tidak membulatkan/menolak nominal sangat kecil — Kas Kasir BSD final = 310.850 − 5.000 = **305.850**                                                         |
| **Negatif** | Coba kirim nominal `debit: 0` (selisih nol, seharusnya tidak perlu jurnal)            | Cek behavior aktual — idealnya FE mencegah submit jurnal 2-baris dengan nominal 0 (bukan error backend, tapi guard UX); kalau backend justru menerima `0` sebagai baris valid dan membuat jurnal "kosong" → catat sebagai temuan kecil, bukan prioritas |
| Netralisasi | Reverse setelah posted                                                                |

## 1.13 Suntikan Modal Tambahan (Persiapan Ekspansi Outlet BSD)

Pemilik menyuntik modal tambahan untuk mendanai investasi peralatan & renovasi Outlet BSD (§1.14-1.15) — realistis di lapangan, ekspansi kafe baru sering butuh modal segar di luar kas operasional harian.

| Skenario    | Payload kunci                                                                                                                                                      | Hasil                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Positif     | `date:"2026-02-06"`, `lines:[{AST-04,debit:40000000},{EKT-01,credit:40000000}]`                                                                                    | 201 — Modal Pemilik (EKT-01) = 67.700.000 (opening) + 40.000.000 = **107.700.000** |
| Netralisasi | Reverse setelah posted (TAPI kalau sudah dipakai §1.14-1.15 mendanai akuisisi aset, jangan reverse — buat modal tambahan di jurnal terpisah untuk eksperimen lain) |

## 1.14-1.15 Akuisisi 2 Aset Tetap untuk Ekspansi Outlet BSD

**Catatan proses 2-langkah (bukan bug, sama seperti suite manufaktur)**: `fixed-assets/assets/create` HANYA mendaftarkan aset (nilai buku awal) — TIDAK otomatis posting jurnal akuisisi. Jurnal akuisisi dibuat manual terpisah di bawah ini.

> **Kontrak field asli Assets — `create`** (verifikasi baca kode langsung, `App\Http\Controllers\Finance\FixedAssets::create()`): `asset_code` TIDAK bisa diisi manual — server SELALU generate sendiri format `FA/{tahun}/{urutan}`, di-strip diam-diam kalau dikirim di payload (jadi kode `KDP-001`/`REN-001` di bawah TIDAK akan tersimpan). `category` HANYA menerima salah satu dari 6 nilai fix: `land|building|vehicle|equipment|furniture|intangible` — "Peralatan Dapur" dipetakan ke `equipment`, "Renovasi/Leasehold Improvement" dipetakan ke `building`. Nama field nilai sisa yang benar adalah `salvage_value` (bukan `residual_value`). `current_book_value` saat registrasi = full `acquisition_cost` (belum dikurangi `salvage_value`).

| Skenario                                                          | Payload kunci                                                                                                                                                                                                                                                                                                     | Hasil                                                                                                                     |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Positif — daftar Peralatan Dapur                                  | `POST fixed-assets/assets/create {name:"Mesin Espresso 2 Grup + Grinder Set", category:"equipment", acquisition_date:"2026-02-06", acquisition_cost:48000000, salvage_value:3000000, useful_life_months:60, depreciation_method:"straight_line", status:"active"}`                   | 201, `asset_code` auto-generate `FA/2026/xxxx`, `current_book_value:48000000` — penyusutan bulanan = (48.000.000−3.000.000)/60 = **750.000/bulan** (dites file `05`) |
| Positif — daftar Renovasi Interior                                | `POST fixed-assets/assets/create {name:"Renovasi Interior & Furniture Outlet BSD", category:"building", acquisition_date:"2026-02-06", acquisition_cost:36000000, salvage_value:0, useful_life_months:36, depreciation_method:"declining_balance", status:"active"}` | 201, `asset_code` auto-generate `FA/2026/xxxx`, `current_book_value:36000000`                                                                                        |
| Positif — jurnal akuisisi Peralatan Dapur (tunai dari Bank BCA)   | `date:"2026-02-06"`, `lines:[{AST-08,debit:48000000},{AST-04,credit:48000000}]`                                                                                                                                                                                                                                   | 201                                                                                                                       |
| Positif — jurnal akuisisi Renovasi Interior (tunai dari Bank BCA) | `date:"2026-02-06"`, `lines:[{AST-10,debit:36000000},{AST-04,credit:36000000}]`                                                                                                                                                                                                                                   | 201                                                                                                                       |
| Netralisasi                                                       | Reverse jurnal akuisisi setelah posted — TAPI kalau sudah kepakai file `05` (penyusutan), jangan reverse, buat aset test baru terpisah                                                                                                                                                                            |

## 1.16 Post-Bulk & Verifikasi Akhir (Regression Check)

| Skenario            | Detail                                                                                                                   | Hasil                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| Positif — post-bulk | Semua jurnal draft/pending §1.1-1.15 sekaligus → `PUT accounting/journals/post-bulk`                                     | Semua ter-post, GL entries kebuat untuk semuanya |
| Positif             | Verifikasi total GL cocok dengan semua angka "Hasil" di atas via `general-ledger/trial-balance` sebelum lanjut file `02` | Balanced, tidak ada selisih                      |
| Netralisasi         | — (biarkan semua tetap posted, jadi baseline file `02`-`06`)                                                             |

## Ringkasan Saldo Akun Kunci Setelah File 01 (Baseline untuk File 02-06)

Ditelusuri via T-account dari opening balance (file `00` §9) + tiap jurnal §1.1-1.15, diverifikasi ulang dari nol (bukan cuma dijumlah berurutan) — identitas Debit=Kredit dicek per jurnal SEKALIGUS per total keseluruhan.

| Akun                              |                                                                                                                                          Saldo Akhir | Perhitungan                                                                                                                           |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------- |
| AST-01 Kas Kasir Kemang           |                                                                                                                                              667.650 | 2.000.000 + 15.667.650 (§1.1-1.5) − 17.000.000 (§1.8)                                                                                 |
| AST-02 Kas Kasir Senayan          |                                                                                                                                              440.050 | 1.500.000 + 9.940.050 − 11.000.000                                                                                                    |
| AST-03 Kas Kasir BSD              |                                                                                                                                              305.850 | 1.000.000 + 5.810.850 − 6.500.000 − 5.000 (§1.12)                                                                                     |
| AST-04 Bank BCA Operasional       |                                                                                                                                           27.600.000 | 50.000.000 + 34.500.000 (§1.8) − 11.400.000 (§1.9) − 1.500.000 (§1.10) + 40.000.000 (§1.13) − 48.000.000 (§1.14) − 36.000.000 (§1.15) |
| AST-05 Piutang Dagang             |                                                                                                                                           13.550.000 | 8.000.000 + 5.550.000 (§1.11)                                                                                                         |
| AST-06 Persediaan Bahan Baku      |                                                                                                                                           25.093.250 | 15.000.000 − 9.906.750 (§1.6) + 20.000.000 (§1.7)                                                                                     |
| AST-07 PPN Masukan                |                                                                                                                                            2.200.000 | 0 + 2.200.000 (§1.7)                                                                                                                  |
| AST-08 Peralatan Dapur            |                                                                                                                                           48.000.000 | §1.14                                                                                                                                 |
| AST-10 Renovasi Interior          |                                                                                                                                           36.000.000 | §1.15                                                                                                                                 |
| **Total Aset**                    |                                                                                                                                      **153.856.800** |                                                                                                                                       |
| LIA-01 Utang Dagang               |                                                                                                                                           28.200.000 | 6.000.000 + 22.200.000 (§1.7)                                                                                                         |
| LIA-02 PPN Keluaran               |                                                                                                                                            3.663.550 | 3.113.550 (§1.1-1.5) + 550.000 (§1.11)                                                                                                |
| LIA-03 Utang PPh 21 Karyawan      |                                                                                                                                            1.400.000 | 800.000 + 600.000 (§1.9)                                                                                                              |
| LIA-04 Pendapatan Diterima Dimuka |                                                                                                                                            6.000.000 | 3.000.000 + 5.000.000 − 2.000.000 (§1.11)                                                                                             |
| **Total Liabilitas**              |                                                                                                                                       **39.263.550** |                                                                                                                                       |
| EKT-01 Modal Pemilik              |                                                                                                                                          107.700.000 | 67.700.000 + 40.000.000 (§1.13)                                                                                                       |
| EKT-02 Laba Ditahan               |                                                                                                                                                    0 | Belum ada closing entry                                                                                                               |
| PDT-01 Pendapatan Minuman         |                                                                                                                                           23.270.000 | 21.270.000 (§1.1-1.5) + 2.000.000 (§1.11 redemption)                                                                                  |
| PDT-02 Pendapatan Makanan         |                                                                                                                                            7.035.000 | §1.1-1.5                                                                                                                              |
| BBN-01 HPP                        |                                                                                                                                            9.906.750 | §1.6                                                                                                                                  |
| BBN-02 Beban Gaji Karyawan        |                                                                                                                                           12.000.000 | §1.9                                                                                                                                  |
| BBN-03 Beban Listrik & Gas        |                                                                                                                                            1.500.000 | §1.10                                                                                                                                 |
| BBN-04 Beban Selisih Kas Kasir    |                                                                                                                                                5.000 | §1.12                                                                                                                                 |
| **Identitas Neraca**              | Aset(153.856.800) = Liabilitas(39.263.550) + Ekuitas(107.700.000) + Laba Berjalan(30.305.000−23.411.750=6.893.250) → **153.856.800 = 153.856.800** ✓ |                                                                                                                                       |

## Referensi Silang

- [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) — saldo awal & master data
- [`02-general-ledger-trial-balance-per-outlet.id.md`](./02-general-ledger-trial-balance-per-outlet.id.md) — verifikasi akhir seluruh angka file ini per akun & per dimensi outlet
- [`05-aset-tetap-peralatan-dapur-dan-renovasi.id.md`](./05-aset-tetap-peralatan-dapur-dan-renovasi.id.md) — penyusutan bulanan KDP-001/REN-001 yang didaftarkan di §1.14-1.15
- [`06-rekonsiliasi-bank-setoran-kasir.id.md`](./06-rekonsiliasi-bank-setoran-kasir.id.md) — verifikasi setoran §1.8 vs mutasi bank aktual
