---
title: Ranahku — Urutan Input Data Master (Langkah demi Langkah)
description: Daftar semua data master Ranahku disusun sesuai urutan penginputan saat testing — dari struktur dasar, bagan akun, pajak, gudang, mitra, produk, SDM, saldo awal, sampai konfigurasi jurnal per modul. Tiap tahap punya tabel siap-ketik. Turunan dari berkas 00 (profil).
---

# Ranahku — Urutan Input Data Master

> Ikuti tahap 1 → 12 berurutan. Tahap berikutnya butuh data dari tahap sebelumnya
> (mis. Jabatan butuh Departemen, Karyawan butuh Jabatan). Angka & nama diambil
> dari [`00-profil-perusahaan-dan-master-data.id.md`](00-profil-perusahaan-dan-master-data.id.md).
>
> Tanggal mulai operasi: **1 September 2026**. Periode uji: **September 2026**.

---

## Ringkasan Tahap

| #   | Tahap                 | Isi                                                | Prasyarat            |
| --- | --------------------- | -------------------------------------------------- | -------------------- |
| 1   | Struktur dasar        | Cabang, Mata Uang, Tahun Buku, Unit/Kegiatan Usaha | —                    |
| 2   | Bagan akun            | Tipe Akun, Daftar Akun                             | Tahap 1              |
| 3   | Pajak                 | Daftar Pajak                                       | Tahap 2 (akun PPN)   |
| 4   | Gudang                | Gudang toko & dapur                                | Tahap 1              |
| 5   | Mitra                 | Pemasok, Pelanggan                                 | Tahap 1              |
| 6   | Produk toko           | Kategori, Satuan, Barang, Harga Jual, Harga Beli   | Tahap 4, 5           |
| 7   | Menu rumah makan      | Kategori menu, Menu, Bahan baku                    | Tahap 4              |
| 8   | Layanan sewa aplikasi | Paket sewa + tarif                                 | Tahap 1              |
| 9   | SDM                   | Departemen, Jabatan (+ Role Akses), Karyawan       | Tahap 1              |
| 10  | Saldo awal            | Rekening Bank, Saldo Awal Akun                     | Tahap 2, 3           |
| 11  | Konfigurasi jurnal    | Pemetaan akun per modul (Auto-map lalu sesuaikan)  | Tahap 2, semua modul |
| 12  | Pelengkap             | Metode pembayaran, syarat pembayaran               | Tahap 1              |

---

## TAHAP 1 — Struktur Dasar

### 1.1 Cabang (**Branches**)

| Nama    | Keterangan                                                                         |
| ------- | ---------------------------------------------------------------------------------- |
| Ranahku | Cabang tunggal — menaungi seluruh operasional (sewa aplikasi + toko + rumah makan) |

> Biasanya sudah terbentuk saat pendaftaran tenant. Pastikan user tester
> `active_branch`-nya = Ranahku.

### 1.2 Mata Uang (**Currencies**)

| Kode | Nama   | Utama? |
| ---- | ------ | ------ |
| IDR  | Rupiah | Ya     |

> Umumnya ter-generate otomatis per cabang baru. Tidak ada transaksi multi-mata-uang.

### 1.3 Tahun Buku & Periode (**Fiscal Years**, **Accounting Periods**)

| Item                        | Nilai                              |
| --------------------------- | ---------------------------------- |
| Tahun Buku 2026             | 1 Januari 2026 – 31 Desember 2026  |
| Periode                     | 12 periode bulanan (auto-generate) |
| Periode aktif untuk testing | September 2026 (1–30 Sep 2026)     |

### 1.4 Unit / Kegiatan Usaha (**Business Units**)

Dipakai untuk memisahkan laba-rugi 3 kegiatan di dalam satu cabang. Semua `default_unit_type` = `profit`, tanpa induk (flat).

| Kode     | Nama                  | Catatan                                             |
| -------- | --------------------- | --------------------------------------------------- |
| `SEWA`   | Layanan Sewa Aplikasi | Pendapatan sewa bulanan/tahunan + pendampingan awal |
| `RETAIL` | Toko Retail Ranahku   | Penjualan barang kebutuhan sehari-hari & alat tulis |
| `RESTO`  | Rumah Makan Ranahku   | Penjualan makanan & minuman                         |

---

## TAHAP 2 — Bagan Akun

### 2.1 Tipe Akun (**Chart of Accounts Types**) — buat SEBELUM akun

| #   | Kode         | Nama                  | Kategori    | Saldo Normal | Bagian Arus Kas | Kelompok Laporan |
| --- | ------------ | --------------------- | ----------- | ------------ | --------------- | ---------------- |
| 1   | `AST_LANCAR` | Harta Lancar          | `asset`     | `debit`      | `operating`     | Balance Sheet    |
| 2   | `AST_TETAP`  | Harta Tetap           | `asset`     | `debit`      | `investing`     | Balance Sheet    |
| 3   | `KEWAJIBAN`  | Kewajiban             | `liability` | `credit`     | `operating`     | Balance Sheet    |
| 4   | `MODAL`      | Modal                 | `equity`    | `credit`     | `financing`     | Balance Sheet    |
| 5   | `PENDAPATAN` | Pendapatan            | `revenue`   | `credit`     | `operating`     | Income Statement |
| 6   | `HPP`        | Harga Pokok Penjualan | `expense`   | `debit`      | `operating`     | Income Statement |
| 7   | `BEBAN`      | Beban Usaha           | `expense`   | `debit`      | `operating`     | Income Statement |

### 2.2 Daftar Akun (**Chart of Accounts**)

Kolom **Kegiatan** mengisi *default tag business unit* akun (opsional, bisa di-override per baris jurnal). Kolom **Flag** = penanda khusus yang harus dicentang.

| Kode  | Nama Akun                           | Tipe (2.1)   | Kegiatan | Flag                                                       |
| ----- | ----------------------------------- | ------------ | -------- | ---------------------------------------------------------- |
| 1-101 | Kas Kecil Kantor                    | `AST_LANCAR` | —        | akun kas, wajib saldo                                      |
| 1-102 | Kas Toko Retail                     | `AST_LANCAR` | `RETAIL` | akun kas                                                   |
| 1-103 | Kas Rumah Makan                     | `AST_LANCAR` | `RESTO`  | akun kas                                                   |
| 1-110 | Bank Operasional                    | `AST_LANCAR` | —        | akun kas/bank                                              |
| 1-120 | Piutang Sewa Aplikasi               | `AST_LANCAR` | `SEWA`   | **akun kontrol piutang**, wajib saldo                      |
| 1-130 | Persediaan Barang Toko              | `AST_LANCAR` | `RETAIL` | wajib saldo (dikendalikan stok)                            |
| 1-131 | Persediaan Bahan Rumah Makan        | `AST_LANCAR` | `RESTO`  | wajib saldo                                                |
| 1-140 | Sewa Ruko Dibayar Dimuka            | `AST_LANCAR` | —        | —                                                          |
| 1-150 | Jaminan Sewa Ruko                   | `AST_LANCAR` | —        | —                                                          |
| 1-160 | PPN Masukan                         | `AST_LANCAR` | —        | **akun pajak** → tautkan ke pajak `PPN-IN`                 |
| 1-170 | Uang Muka PPh 23                    | `AST_LANCAR` | `SEWA`   | **akun pajak** → tautkan ke pajak `PPH23`                  |
| 1-201 | Peralatan Kantor & Komputer         | `AST_TETAP`  | —        | —                                                          |
| 1-202 | Kendaraan Operasional               | `AST_TETAP`  | —        | —                                                          |
| 1-203 | Peralatan & Perlengkapan Toko       | `AST_TETAP`  | `RETAIL` | —                                                          |
| 1-204 | Peralatan Dapur & Rumah Makan       | `AST_TETAP`  | `RESTO`  | —                                                          |
| 1-209 | Akumulasi Penyusutan                | `AST_TETAP`  | —        | kontra-aset                                                |
| 2-101 | Utang Usaha                         | `KEWAJIBAN`  | —        | **akun kontrol utang**, wajib saldo                        |
| 2-110 | Utang Bank                          | `KEWAJIBAN`  | —        | wajib saldo                                                |
| 2-120 | PPN Keluaran                        | `KEWAJIBAN`  | —        | **akun pajak** → tautkan ke pajak `PPN-OUT`                |
| 2-121 | Utang Pajak Restoran (PB1)          | `KEWAJIBAN`  | `RESTO`  | **akun pajak** → tautkan ke pajak `PB1`                    |
| 2-122 | Utang PPh 21 Karyawan               | `KEWAJIBAN`  | —        | **akun pajak** → tautkan ke pajak `PPH21`                  |
| 2-130 | Utang Gaji                          | `KEWAJIBAN`  | —        | —                                                          |
| 2-131 | Utang BPJS                          | `KEWAJIBAN`  | —        | —                                                          |
| 2-140 | Pendapatan Sewa Diterima Dimuka     | `KEWAJIBAN`  | `SEWA`   | wajib saldo                                                |
| 3-101 | Modal Pemilik                       | `MODAL`      | —        | —                                                          |
| 3-102 | Laba Ditahan                        | `MODAL`      | —        | **flag Laba Ditahan**                                      |
| 3-103 | Ekuitas Saldo Awal                  | `MODAL`      | —        | **flag Ekuitas Saldo Awal** (wajib ada tepat 1 per cabang) |
| 4-101 | Pendapatan Sewa Aplikasi            | `PENDAPATAN` | `SEWA`   | —                                                          |
| 4-102 | Pendapatan Pendampingan Awal        | `PENDAPATAN` | `SEWA`   | —                                                          |
| 4-201 | Pendapatan Penjualan Toko           | `PENDAPATAN` | `RETAIL` | —                                                          |
| 4-301 | Pendapatan Rumah Makan              | `PENDAPATAN` | `RESTO`  | —                                                          |
| 4-901 | Pendapatan Lain-lain (Selisih Stok) | `PENDAPATAN` | —        | menampung selisih lebih opname                             |
| 5-201 | Harga Pokok Penjualan Toko          | `HPP`        | `RETAIL` | —                                                          |
| 5-301 | Harga Pokok Bahan Rumah Makan       | `HPP`        | `RESTO`  | —                                                          |
| 6-101 | Beban Gaji & Upah                   | `BEBAN`      | —        | —                                                          |
| 6-102 | Beban Komisi Penjualan              | `BEBAN`      | `SEWA`   | —                                                          |
| 6-103 | Beban Sewa Ruko                     | `BEBAN`      | —        | —                                                          |
| 6-104 | Beban Listrik, Air & Internet       | `BEBAN`      | —        | —                                                          |
| 6-105 | Beban Transportasi & Bahan Bakar    | `BEBAN`      | `SEWA`   | —                                                          |
| 6-106 | Beban Penyusutan                    | `BEBAN`      | —        | —                                                          |
| 6-107 | Beban Perlengkapan & Alat Tulis     | `BEBAN`      | —        | —                                                          |
| 6-108 | Beban Pemasaran & Promosi           | `BEBAN`      | —        | —                                                          |
| 6-109 | Beban Administrasi Bank             | `BEBAN`      | —        | —                                                          |
| 6-110 | Beban Bunga Pinjaman                | `BEBAN`      | —        | —                                                          |
| 6-190 | Beban Kerugian Persediaan           | `BEBAN`      | —        | menampung susut/rusak stok                                 |

**45 akun.** (Tambahan dari berkas 00: `2-121`, `2-122`, `2-131`, `3-103` — dibutuhkan untuk pajak restoran, PPh 21, BPJS, dan offset saldo awal.)

---

## TAHAP 3 — Pajak (**Taxes**)

| Kode      | Nama                     | Tarif | Efek       | Dipakai untuk                                              |
| --------- | ------------------------ | ----- | ---------- | ---------------------------------------------------------- |
| `PPN-OUT` | PPN Keluaran 11%         | 11%   | menambah   | Penjualan toko retail & tagihan sewa aplikasi              |
| `PPN-IN`  | PPN Masukan 11%          | 11%   | mengurangi | Pembelian barang/jasa dari pemasok PKP (kredit pajak)      |
| `PPH23`   | PPh 23 Dipotong 2%       | 2%    | mengurangi | Tagihan sewa ke pelanggan badan usaha (dipotong pelanggan) |
| `PPH21`   | PPh 21 Karyawan          | 5%    | mengurangi | Potongan pajak penghasilan pada slip gaji                  |
| `PB1`     | Pajak Restoran (PB1) 10% | 10%   | menambah   | Penjualan rumah makan (pajak daerah, bukan PPN)            |

> Rumah makan kena **PB1**, bukan PPN. Toko retail & sewa aplikasi kena **PPN**.

---

## TAHAP 4 — Gudang (**Warehouses**)

| Nama               | Tipe    | Kegiatan | Catatan                                                 |
| ------------------ | ------- | -------- | ------------------------------------------------------- |
| Gudang Toko Retail | `store` | `RETAIL` | Stok sembako, minuman, ATK — juga titik jual kasir toko |
| Dapur Rumah Makan  | `store` | `RESTO`  | Stok bahan baku dapur — titik jual kasir rumah makan    |

---

## TAHAP 5 — Mitra

### 5.1 Pemasok (**Contacts** — tipe *supplier*)

| Nama                          | Termin  | Memasok                             | Kegiatan       |
| ----------------------------- | ------- | ----------------------------------- | -------------- |
| PT Sumber Elektronik Andalan  | 30 hari | Komputer, printer, perangkat kantor | Kantor         |
| CV Grosir Sembako Makmur      | 21 hari | Sembako & minuman untuk toko        | RETAIL         |
| Koperasi Percetakan Kreatif   | Tunai   | Alat tulis & buku untuk toko        | RETAIL         |
| UD Pasar Segar                | Tunai   | Sayur, daging, ayam, telur          | RESTO          |
| PT Distribusi Minuman Kemasan | 14 hari | Teh, sirup, air mineral, gas        | RESTO & RETAIL |

### 5.2 Pelanggan (**Contacts** — tipe *customer*)

| Nama                                | Termin             | Catatan                                                             |
| ----------------------------------- | ------------------ | ------------------------------------------------------------------- |
| Toko Bangunan Sumber Rejeki         | Tunai lalu bulanan | Sewa aplikasi via kanvasing — Paket Usaha                           |
| Bengkel Motor Laju Jaya             | Bulanan            | Sewa aplikasi via kanvasing — Paket Dasar                           |
| Apotek Sehat Bersama                | 14 hari            | Sewa aplikasi via penjualan — Paket Pro tahunan                     |
| Distributor Minuman Segar Nusantara | 30 hari            | Sewa via penjualan — Paket Pro tahunan, badan usaha (potong PPh 23) |
| CV Katering Nikmat Rasa             | Bayar di muka      | Sewa jangka pendek (mingguan, musim hajatan)                        |
| Pembeli Umum                        | Tunai              | Penampung semua transaksi tunai toko & rumah makan                  |

---

## TAHAP 6 — Produk Toko Retail

### 6.1 Kategori Produk (**Product Categories**) — buat SEBELUM produk

| Slug         | Nama                      |
| ------------ | ------------------------- |
| `sembako`    | Sembako                   |
| `minuman`    | Minuman                   |
| `gas-lpg`    | Gas & LPG                 |
| `alat-tulis` | Alat Tulis & Perlengkapan |
| `kebersihan` | Kebutuhan Kebersihan      |

### 6.2 Satuan Produk (**Product Units**) — buat SEBELUM produk

| Nama    | Singkatan |
| ------- | --------- |
| Karung  | `karung`  |
| Pouch   | `pouch`   |
| Pcs     | `pcs`     |
| Galon   | `galon`   |
| Renceng | `renceng` |
| Dus     | `dus`     |
| Pak     | `pak`     |
| Lusin   | `lusin`   |
| Tabung  | `tabung`  |

### 6.3 Produk + Kode Barang (**Products** → **Product SKUs**)

| Kode    | Nama Barang                       | Kategori     | Satuan  | Harga Beli | Harga Jual | Stok Awal | Nilai Stok Awal |
| ------- | --------------------------------- | ------------ | ------- | ---------: | ---------: | --------: | --------------: |
| BRG-001 | Beras Premium 5 kg                | `sembako`    | Karung  |     62.000 |     72.000 |       300 |      18.600.000 |
| BRG-002 | Minyak Goreng 2 L                 | `sembako`    | Pouch   |     32.000 |     38.000 |       400 |      12.800.000 |
| BRG-003 | Gula Pasir 1 kg                   | `sembako`    | Pcs     |     14.000 |     16.500 |       500 |       7.000.000 |
| BRG-004 | Air Mineral Galon 19 L            | `minuman`    | Galon   |     18.000 |     22.000 |       250 |       4.500.000 |
| BRG-005 | Kopi Sachet (renceng isi 10)      | `minuman`    | Renceng |     11.000 |     14.000 |       600 |       6.600.000 |
| BRG-006 | Teh Kotak 250 ml (dus isi 24)     | `minuman`    | Dus     |     62.000 |     78.000 |       150 |       9.300.000 |
| BRG-007 | Buku Tulis 58 lembar (pak isi 10) | `alat-tulis` | Pak     |     38.000 |     48.000 |       200 |       7.600.000 |
| BRG-008 | Pulpen (lusin)                    | `alat-tulis` | Lusin   |     22.000 |     30.000 |       300 |       6.600.000 |
| BRG-009 | Gas Elpiji 3 kg (isi ulang)       | `gas-lpg`    | Tabung  |     18.000 |     22.000 |       400 |       7.200.000 |
| BRG-010 | Sabun Mandi Batang (pak isi 4)    | `kebersihan` | Pak     |     16.000 |     21.000 |       150 |       2.400.000 |
|         |                                   |              |         |            |            | **Total** |  **90.000.000** |

### 6.4 Daftar Harga Jual (**Price Lists** → **Price List SKUs**)

| Daftar Harga    | Isi                                                                       |
| --------------- | ------------------------------------------------------------------------- |
| Harga Toko 2026 | Semua 10 barang di atas, `min_qty: 1`, aktif — harga = kolom "Harga Jual" |

### 6.5 Harga Beli per Pemasok (**Contact Product SKU Prices**)

Semua barang toko dari **CV Grosir Sembako Makmur** & **PT Distribusi Minuman Kemasan** (BRG-004, 005, 006) — `vendor_price` = kolom "Harga Beli". Angka ini jadi acuan nilai persediaan awal (Tahap 10).

---

## TAHAP 7 — Menu Rumah Makan

### 7.1 Kategori Menu (**Product Categories**)

| Slug            | Nama          |
| --------------- | ------------- |
| `makanan-utama` | Makanan Utama |
| `minuman-resto` | Minuman       |

### 7.2 Satuan

| Nama  | Singkatan |
| ----- | --------- |
| Porsi | `porsi`   |
| Gelas | `gelas`   |
| Botol | `botol`   |

### 7.3 Menu (**Products** → **Product SKUs**)

Bahan baku dikelola sebagai satu kelompok persediaan (akun `1-131`), pemakaian dicatat sebagai harga pokok `5-301` saat menu terjual. Kolom "Biaya Bahan" hanya acuan.

| Kode    | Menu                        | Kategori        | Satuan | Harga Jual | Biaya Bahan (acuan) |
| ------- | --------------------------- | --------------- | ------ | ---------: | ------------------: |
| MNU-001 | Nasi Goreng Spesial         | `makanan-utama` | Porsi  |     25.000 |               9.000 |
| MNU-002 | Ayam Bakar + Nasi + Lalapan | `makanan-utama` | Porsi  |     32.000 |              13.000 |
| MNU-003 | Mie Goreng Spesial          | `makanan-utama` | Porsi  |     23.000 |               8.000 |
| MNU-004 | Soto Ayam + Nasi            | `makanan-utama` | Porsi  |     24.000 |               9.500 |
| MNU-005 | Paket Nasi Ayam Komplit     | `makanan-utama` | Porsi  |     38.000 |              15.000 |
| MNU-006 | Es Teh Manis                | `minuman-resto` | Gelas  |      6.000 |               1.500 |
| MNU-007 | Es Jeruk                    | `minuman-resto` | Gelas  |      8.000 |               2.500 |
| MNU-008 | Air Mineral Botol           | `minuman-resto` | Botol  |      5.000 |               2.000 |

### 7.4 Stok bahan dapur awal

Rp **20.000.000** (sayur, beras, ayam, daging, bumbu, minyak, minuman) — masuk sebagai nilai persediaan awal akun `1-131` di Tahap 10.

---

## TAHAP 8 — Layanan Sewa Aplikasi (**Products** / layanan, non-stok)

| Kode            | Paket                 |     Tarif | Satuan tagih           |
| --------------- | --------------------- | --------: | ---------------------- |
| PKT-DASAR       | Paket Dasar           |   150.000 | per bulan              |
| PKT-USAHA       | Paket Usaha           |   350.000 | per bulan              |
| PKT-PRO         | Paket Pro             |   750.000 | per bulan              |
| PKT-TAHUN-USAHA | Paket Usaha (tahunan) | 3.500.000 | per tahun              |
| PKT-TAHUN-PRO   | Paket Pro (tahunan)   | 7.500.000 | per tahun              |
| PKT-SEWA-HARI   | Sewa Jangka Pendek    |   100.000 | per hari (min. 3 hari) |
| PKT-DAMPING     | Pendampingan Awal     |   500.000 | sekali                 |

Semua bertipe layanan/jasa (tidak dikelola stok). Pendapatan → `4-101` (sewa) / `4-102` (pendampingan).

---

## TAHAP 9 — SDM

### 9.1 Departemen (**Departments**) — buat SEBELUM jabatan

| Kode    | Nama                  |
| ------- | --------------------- |
| `MGT`   | Manajemen & Umum      |
| `KEU`   | Keuangan & Akuntansi  |
| `SEWA`  | Layanan Sewa Aplikasi |
| `TOKO`  | Toko Retail           |
| `RESTO` | Rumah Makan           |

### 9.2 Jabatan / Posisi (**Positions**) — buat SEBELUM karyawan

Untuk **setiap** jabatan: centang **"Buat role baru untuk posisi ini"** supaya role akses otomatis terbentuk (nama role = nama jabatan). Hak akses tiap role diatur belakangan dari halaman **Roles** (jabatan hanya membuat role kosong + menautkan).

| #   | Jabatan                       | Departemen | Gaji Min.  | Gaji Maks. | Buat Role? |
| --- | ----------------------------- | ---------- | ---------: | ---------: | ---------- |
| 1   | Direktur Utama                | `MGT`      | 25.000.000 | 30.000.000 | Ya         |
| 2   | Manajer Operasional           | `MGT`      | 15.000.000 | 20.000.000 | Ya         |
| 3   | Manajer Keuangan              | `KEU`      | 15.000.000 | 20.000.000 | Ya         |
| 4   | Staf Akunting                 | `KEU`      |  6.500.000 |  9.000.000 | Ya         |
| 5   | Staf Penagihan & Kasir Kantor | `KEU`      |  5.000.000 |  7.000.000 | Ya         |
| 6   | Staf Administrasi & SDM       | `MGT`      |  5.500.000 |  7.500.000 | Ya         |
| 7   | Koordinator Layanan Aplikasi  | `SEWA`     |  9.000.000 | 12.000.000 | Ya         |
| 8   | Petugas Kanvasing             | `SEWA`     |  4.000.000 |  6.000.000 | Ya         |
| 9   | Eksekutif Penjualan           | `SEWA`     |  6.000.000 |  9.000.000 | Ya         |
| 10  | Admin Kontrak & Sewa          | `SEWA`     |  4.500.000 |  6.000.000 | Ya         |
| 11  | Staf Pendampingan Pelanggan   | `SEWA`     |  4.500.000 |  6.000.000 | Ya         |
| 12  | Supervisor Toko               | `TOKO`     |  6.000.000 |  8.000.000 | Ya         |
| 13  | Pramuniaga                    | `TOKO`     |  3.500.000 |  4.500.000 | Ya         |
| 14  | Kasir Toko                    | `TOKO`     |  3.500.000 |  4.500.000 | Ya         |
| 15  | Staf Gudang                   | `TOKO`     |  3.800.000 |  5.000.000 | Ya         |
| 16  | Supervisor Rumah Makan        | `RESTO`    |  6.000.000 |  8.000.000 | Ya         |
| 17  | Juru Masak                    | `RESTO`    |  4.500.000 |  6.000.000 | Ya         |
| 18  | Pelayan                       | `RESTO`    |  3.500.000 |  4.500.000 | Ya         |
| 19  | Kasir Rumah Makan             | `RESTO`    |  3.500.000 |  4.500.000 | Ya         |

> **Cepat:** pakai **Import from Excel** (Download Template → isi 19 baris → upload → review → Import). Kolom **Buat Role Baru = Ya** di template = role akses auto-terbentuk per jabatan.

> Setelah semua jabatan dibuat: buka halaman **Roles**, isi hak akses tiap role
> (19 role baru). Contoh: role "Kasir Toko" cukup akses kasir + lihat produk;
> role "Manajer Keuangan" akses penuh keuangan & laporan.

### 9.3 Karyawan (**Employees**) — 25 orang

Saat membuat karyawan: pilih Jabatan → sistem otomatis menautkan role dari jabatan
itu ke akun login-nya (jika "Buat akun login" dicentang & ada email). Gaji pokok
mengikuti jabatan.

| #   | Nama            | Jabatan (9.2)                 | Email (untuk akun login) |
| --- | --------------- | ----------------------------- | ------------------------ |
| 1   | Arman Halim     | Direktur Utama                | arman.halim@ranahku.test |
| 2   | Retno Wulandari | Manajer Operasional           | retno.w@ranahku.test     |
| 3   | Sofyan Nugroho  | Manajer Keuangan              | sofyan.n@ranahku.test    |
| 4   | Dewi Anjani     | Staf Akunting                 | dewi.a@ranahku.test      |
| 5   | Lestari Ningsih | Staf Penagihan & Kasir Kantor | lestari.n@ranahku.test   |
| 6   | Yoga Pratama    | Staf Administrasi & SDM       | yoga.p@ranahku.test      |
| 7   | Fajar Ramadhan  | Koordinator Layanan Aplikasi  | fajar.r@ranahku.test     |
| 8   | Andi Saputra    | Petugas Kanvasing             | andi.s@ranahku.test      |
| 9   | Rizal Kurnia    | Petugas Kanvasing             | rizal.k@ranahku.test     |
| 10  | Sari Melati     | Petugas Kanvasing             | sari.m@ranahku.test      |
| 11  | Nadia Puspita   | Eksekutif Penjualan           | nadia.p@ranahku.test     |
| 12  | Bagas Wicaksono | Eksekutif Penjualan           | bagas.w@ranahku.test     |
| 13  | Intan Permata   | Admin Kontrak & Sewa          | intan.p@ranahku.test     |
| 14  | Hendra Gunawan  | Staf Pendampingan Pelanggan   | hendra.g@ranahku.test    |
| 15  | Maya Oktaviani  | Staf Pendampingan Pelanggan   | maya.o@ranahku.test      |
| 16  | Dodi Herlambang | Supervisor Toko               | dodi.h@ranahku.test      |
| 17  | Wati Suryani    | Pramuniaga                    | wati.s@ranahku.test      |
| 18  | Eko Prasetyo    | Pramuniaga                    | eko.p@ranahku.test       |
| 19  | Fitri Handayani | Kasir Toko                    | fitri.h@ranahku.test     |
| 20  | Slamet Riyadi   | Staf Gudang                   | slamet.r@ranahku.test    |
| 21  | Ratna Kusuma    | Supervisor Rumah Makan        | ratna.k@ranahku.test     |
| 22  | Trisno Aji      | Juru Masak                    | trisno.a@ranahku.test    |
| 23  | Sumarni         | Juru Masak                    | sumarni@ranahku.test     |
| 24  | Agus Setiawan   | Pelayan                       | agus.s@ranahku.test      |
| 25  | Novi Ramadhani  | Kasir Rumah Makan             | novi.r@ranahku.test      |

---

## TAHAP 10 — Saldo Awal per 1 September 2026

### 10.1 Rekening Bank (**Bank Accounts**)

| Akun                   | Nama Rekening            |  Saldo Awal |
| ---------------------- | ------------------------ | ----------: |
| 1-110 Bank Operasional | Bank Operasional Ranahku | 815.000.000 |

### 10.2 Saldo Awal Akun (**Chart of Accounts Balances**)

| Akun                                | Posisi |                                       Nilai (Rp) |
| ----------------------------------- | ------ | -----------------------------------------------: |
| 1-101 Kas Kecil Kantor              | Debit  |                                       15.000.000 |
| 1-102 Kas Toko Retail               | Debit  |                                        5.000.000 |
| 1-103 Kas Rumah Makan               | Debit  |                                        5.000.000 |
| 1-110 Bank Operasional              | Debit  |        815.000.000 *(via Rekening Bank di 10.1)* |
| 1-130 Persediaan Barang Toko        | Debit  | 90.000.000 *(harus = total stok awal Tahap 6.3)* |
| 1-131 Persediaan Bahan Rumah Makan  | Debit  |                       20.000.000 *(= Tahap 7.4)* |
| 1-140 Sewa Ruko Dibayar Dimuka      | Debit  |                                      120.000.000 |
| 1-150 Jaminan Sewa Ruko             | Debit  |                                       15.000.000 |
| 1-201 Peralatan Kantor & Komputer   | Debit  |                                      250.000.000 |
| 1-202 Kendaraan Operasional         | Debit  |                                      180.000.000 |
| 1-203 Peralatan & Perlengkapan Toko | Debit  |                                       60.000.000 |
| 1-204 Peralatan Dapur & Rumah Makan | Debit  |                                      120.000.000 |
| 2-110 Utang Bank                    | Kredit |                                      200.000.000 |
| 3-101 Modal Pemilik                 | Kredit |                                    1.500.000.000 |

Jumlah Harta = **1.700.000.000** · Jumlah Kewajiban + Modal = **1.700.000.000** → seimbang.
Offset selisih otomatis lewat akun `3-103 Ekuitas Saldo Awal`.

---

## TAHAP 11 — Konfigurasi Jurnal per Modul

Untuk tiap halaman konfigurasi: klik **"Auto-map from Chart of Accounts"** dulu, lalu
sesuaikan baris yang perlu mengikut tabel di bawah, lalu Simpan.

### 11.1 Persediaan (**inventory/config**)

| Fungsi                    | Akun                                            |
| ------------------------- | ----------------------------------------------- |
| `inventory`               | 1-130 Persediaan Barang Toko                    |
| `inventory_loss`          | 6-190 Beban Kerugian Persediaan                 |
| `other_income_adjustment` | 4-901 Pendapatan Lain-lain (Selisih Stok)       |
| `transit_clearing`        | *(kosongkan — tidak ada transfer antar-gudang)* |

### 11.2 Penjualan (**sales/sales-journal-configuration**) — retail via alur Sales

| Fungsi          | Akun                                                                                  |
| --------------- | ------------------------------------------------------------------------------------- |
| `ar`            | 1-120 Piutang Sewa Aplikasi *(atau buat 1-121 Piutang Usaha Toko jika retail kredit)* |
| `sales_revenue` | 4-201 Pendapatan Penjualan Toko                                                       |
| `ppn_keluaran`  | 2-120 PPN Keluaran                                                                    |
| `cash_bank`     | 1-102 Kas Toko Retail                                                                 |
| `cogs`          | 5-201 Harga Pokok Penjualan Toko                                                      |
| `inventory`     | 1-130 Persediaan Barang Toko                                                          |
| `sales_return`  | 4-201 Pendapatan Penjualan Toko *(kontra)*                                            |

### 11.3 Kasir Toko (**pos/pos-configs**)

| Fungsi                                    | Akun                                                             |
| ----------------------------------------- | ---------------------------------------------------------------- |
| `pos_cash`                                | 1-102 Kas Toko Retail                                            |
| `sales_revenue`                           | 4-201 Pendapatan Penjualan Toko                                  |
| `ppn_keluaran`                            | 2-120 PPN Keluaran                                               |
| `cogs`                                    | 5-201 Harga Pokok Penjualan Toko                                 |
| `inventory`                               | 1-130 Persediaan Barang Toko                                     |
| `cash_over_short`                         | 6-190 *(atau buat 6-111 Selisih Kas)*                            |
| `cashback_liability` / `cashback_expense` | *(hasil auto-map — biarkan jika program cashback tidak dipakai)* |

### 11.4 Rumah Makan (**restaurant/config**)

| Fungsi                             | Akun                                                              |
| ---------------------------------- | ----------------------------------------------------------------- |
| `restaurant_sales_revenue`         | 4-301 Pendapatan Rumah Makan                                      |
| `restaurant_tax_output`            | 2-121 Utang Pajak Restoran (PB1)                                  |
| `restaurant_cash_clearing`         | 1-103 Kas Rumah Makan                                             |
| `restaurant_cogs`                  | 5-301 Harga Pokok Bahan Rumah Makan                               |
| `restaurant_inventory`             | 1-131 Persediaan Bahan Rumah Makan                                |
| `restaurant_sales_discount`        | 4-301 *(kontra)*                                                  |
| `restaurant_service_charge_income` | 4-901 *(jika tidak pakai service charge, biarkan hasil auto-map)* |

### 11.5 Sewa Aplikasi (**rental/rental-configs**)

| Fungsi                     | Akun                                                                           |
| -------------------------- | ------------------------------------------------------------------------------ |
| `rental_ar`                | 1-120 Piutang Sewa Aplikasi                                                    |
| `rental_revenue`           | 4-101 Pendapatan Sewa Aplikasi                                                 |
| `cash_bank`                | 1-110 Bank Operasional                                                         |
| `rental_deposit_liability` | 2-140 Pendapatan Sewa Diterima Dimuka *(atau buat 2-141 Titipan Deposit Sewa)* |

### 11.6 Pembelian (**purchasing/purchase-journal-configuration**)

| Fungsi             | Akun                                                     |
| ------------------ | -------------------------------------------------------- |
| `inventory`        | 1-130 Persediaan Barang Toko                             |
| `ap`               | 2-101 Utang Usaha                                        |
| `gr_ir`            | *(hasil auto-map — akun clearing)*                       |
| `ppn_masukan`      | 1-160 PPN Masukan                                        |
| `cash_bank`        | 1-110 Bank Operasional                                   |
| `dp`               | *(hasil auto-map — Uang Muka Pembelian)*                 |
| `return`           | *(hasil auto-map — Retur Pembelian)*                     |
| `purchase_expense` | 6-107 Beban Perlengkapan & Alat Tulis *(atau sesuaikan)* |

### 11.7 Penggajian (**hrm/payroll-journal-configuration**)

| Fungsi                     | Akun                                              |
| -------------------------- | ------------------------------------------------- |
| `salary_expense`           | 6-101 Beban Gaji & Upah                           |
| `salary_payable`           | 2-130 Utang Gaji                                  |
| `pph21_payable`            | 2-122 Utang PPh 21 Karyawan                       |
| `bpjs_payable`             | 2-131 Utang BPJS                                  |
| `other_deductions_payable` | 2-130 Utang Gaji *(atau buat akun potongan lain)* |
| `cash_bank`                | 1-110 Bank Operasional                            |

---

## TAHAP 12 — Pelengkap

### 12.1 Metode Pembayaran (**Payment Methods**)

| Nama                      | Akun kas/bank          |
| ------------------------- | ---------------------- |
| Tunai — Kantor            | 1-101 Kas Kecil Kantor |
| Tunai — Toko              | 1-102 Kas Toko Retail  |
| Tunai — Rumah Makan       | 1-103 Kas Rumah Makan  |
| Transfer Bank Operasional | 1-110 Bank Operasional |
| QRIS                      | 1-110 Bank Operasional |

### 12.2 Syarat Pembayaran (**Payment Terms**) — jika belum ada bawaan

| Nama    | Hari |
| ------- | ---- |
| Tunai   | 0    |
| 14 Hari | 14   |
| 21 Hari | 21   |
| 30 Hari | 30   |

---

## Daftar Periksa Cepat

- [ ] Tahap 1: cabang, IDR, tahun buku 2026, 3 unit usaha (SEWA/RETAIL/RESTO)
- [ ] Tahap 2: 7 tipe akun → 45 akun (cek flag pajak/kontrol/laba-ditahan/ekuitas-saldo-awal)
- [ ] Tahap 3: 5 pajak, tautkan ke akun pajak masing-masing
- [ ] Tahap 4: 2 gudang (Toko, Dapur)
- [ ] Tahap 5: 5 pemasok, 5 pelanggan + Pembeli Umum
- [ ] Tahap 6: 5 kategori, 9 satuan, 10 barang, 1 daftar harga, harga beli per pemasok
- [ ] Tahap 7: 2 kategori menu, 8 menu, stok bahan dapur 20 jt
- [ ] Tahap 8: 7 paket sewa (layanan non-stok)
- [ ] Tahap 9: 5 departemen → 19 jabatan (semua "buat role") → atur hak akses 19 role → 25 karyawan
- [ ] Tahap 10: 1 rekening bank + saldo awal (harta = 1,7 M, seimbang)
- [ ] Tahap 11: 7 halaman konfigurasi jurnal — Auto-map lalu sesuaikan
- [ ] Tahap 12: metode pembayaran, syarat pembayaran
