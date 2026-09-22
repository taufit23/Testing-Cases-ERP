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
| 7   | Menu rumah makan      | Kategori menu, Menu, Bahan baku, Area/Meja/Stasiun Dapur | Tahap 4        |
| 8   | Layanan sewa aplikasi | Paket sewa + tarif                                 | Tahap 1              |
| 9   | SDM                   | Departemen, Jabatan (+ Role Akses), Karyawan, Jenis Cuti, Acuan BPJS/Pajak | Tahap 1 |
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

> **⚠️ Temuan struktural (2026-09-14, ditemukan lewat testing UI langsung):** UI "Add Price" di
> halaman detail Product → SKU (`Manage Prices`) **tidak punya field untuk memilih Price List** —
> hanya `Currency`, `Unit`, `Price`, `Min Qty`, `Status`. Artinya harga jual SKU tidak bisa
> ditautkan ke Price List custom bernama bebas seperti "Harga Toko 2026" lewat UI ini; harga
> otomatis masuk ke Price List default per branch (di provider ini bernama **"Daftar Harga Jual
> Retail"**, hasil dari `Use Template` di halaman Price Lists — 8 price list default lain juga
> ikut ter-provision: Harga Modal, Promo, Member/Reseller, Online, Cabang, Grosir, Beli Default).
> Dicek langsung: seluruh 10 SKU BRG-001..010 **sudah** punya harga jual `Active` yang cocok
> persis dengan kolom "Harga Jual" di 6.3, dengan `min_qty: 1` — jadi **intent Tahap 6.4 sudah
> terpenuhi secara fungsional** lewat price list default tersebut, walau bukan lewat list bernama
> literal "Harga Toko 2026". Percobaan membuat price list terpisah bernama "Harga Toko 2026"
> berakhir jadi list kosong tak terpakai (sudah dihapus lagi) karena tidak ada jalur UI untuk
> mengisi itemnya. **Rekomendasi ke tim dev**: baik (a) tambahkan Price List selector di modal
> "Add Price"/"Manage Prices", atau (b) update dokumentasi test-case supaya Tahap 6.4 eksplisit
> menyebut "pakai price list default hasil Use Template" alih-alih menyuruh bikin list baru.

### 6.5 Harga Beli per Pemasok (**Contact Product SKU Prices**)

Semua barang toko dari **CV Grosir Sembako Makmur** & **PT Distribusi Minuman Kemasan** (BRG-004, 005, 006) — `vendor_price` = kolom "Harga Beli". Angka ini jadi acuan nilai persediaan awal (Tahap 10).

> **⚠️ Temuan struktural (2026-09-14, ditemukan lewat testing UI langsung):** Tidak ada field
> harga di modal "Manage Suppliers" (Product → Manage Suppliers) maupun "Manage Products"
> (Contact → kebab menu → Manage Products) — keduanya cuma checklist asosiasi supplier↔produk,
> **tanpa field `vendor_price` sama sekali**. Yang bisa dieksekusi: (1) asosiasi dibuat —
> BRG-005 (Kopi Sachet) → **CV Grosir Sembako Makmur**; BRG-004 (Air Mineral Galon) & BRG-006
> (Teh Kotak) → **PT Distribusi Minuman Kemasan** (sesuai daftar pasokan di dokumen profil
> bagian 7). (2) Dicek expand row SKU → panel PRICES: ketiganya **sudah** punya harga beli
> default (Price List "Daftar Harga Beli Default", Inactive) yang cocok persis kolom "Harga
> Beli": BRG-004 = 18.000, BRG-005 = 11.000, BRG-006 = 62.000 — jadi intent Tahap 6.5 (nilai
> acuan persediaan awal Tahap 10 sudah benar) **terpenuhi secara fungsional**, hanya saja harga
> ini generik per-SKU, bukan spesifik per-vendor. Detail & rekomendasi ke tim dev: lihat
> [`TemuanTestCase/ClientMaster/Ranahku/02-manage-suppliers-tidak-punya-field-harga-per-vendor.id.md`](../../erpApiServices/docs/TemuanTestCase/ClientMaster/Ranahku/02-manage-suppliers-tidak-punya-field-harga-per-vendor.id.md).

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

> **Catatan gap (ditemukan 2026-09-15 saat menjalankan `02-alur-transaksi.id.md` Tahap D.2):**
> saat membuat menu di atas, pastikan setiap SKU juga diberi **Sales Channel** (minimal
> **Sales**), bukan cuma disiapkan untuk dijual lewat kasir meja Restaurant. Ditemukan bahwa
> MNU-005 (Paket Nasi Ayam Komplit) belum diberi kanal penjualan sama sekali, sehingga transaksi
> lewat modul Sales (mis. pesanan katering partai besar di Tahap D.2) gagal disimpan sampai Sales
> Channel-nya ditambahkan manual. Produk Layanan Sewa Aplikasi di Tahap 8 sendiri sudah benar
> diberi Sales Channel sejak awal (Sales, Rental, Canvassing) — jadi gap ini spesifik untuk menu
> Rumah Makan yang tadinya cuma disiapkan untuk kasir meja, bukan pola yang berulang di semua
> modul produk.

### 7.4 Stok bahan dapur awal

Rp **20.000.000** (sayur, beras, ayam, daging, bumbu, minyak, minuman) — masuk sebagai nilai persediaan awal akun `1-131` di Tahap 10.

> **Catatan gap (ditemukan 2026-09-15 saat menjalankan `02-alur-transaksi.id.md` Tahap E.2):**
> daftar produk bahan baku yang benar-benar dibuat di **Products** ternyata hanya barang kering/
> kemasan (beras, minyak, bumbu kemasan, dsb) — belum ada produk khusus untuk bahan segar seperti
> **sayur, ayam potong, dan telur**. Saat pengujian pembelian restock ke pemasok bahan segar
> (UD Pasar Segar) mencoba mencari produk "Sayur" di form Purchase Order, hasilnya nihil sama
> sekali. Lihat rincian di
> [`erpApiServices/docs/TemuanTestCase/Inventory/Ranahku/02-produk-bahan-baku-dapur-sayur-ayam-telur-belum-ada-di-master-data.id.md`](../../erpApiServices/docs/TemuanTestCase/Inventory/Ranahku/02-produk-bahan-baku-dapur-sayur-ayam-telur-belum-ada-di-master-data.id.md).
> **Untuk pengujian berikutnya**: tambahkan produk bahan segar (mis. Sayur Campur, Ayam Potong,
> Telur Ayam) di **Products**, kategori bahan baku, satuan Kg/Butir, warehouse default "Dapur
> Rumah Makan", SEBELUM menjalankan skenario pembelian bahan segar di Tahap E.2.

### 7.5 Master Data Operasional Rumah Makan (**Areas**, **Tables**, **Kitchen Stations**)

> **Catatan gap (ditemukan 2026-09-15 saat menjalankan `02-alur-transaksi.id.md` Tahap D):** modul
> **Restaurant** butuh master data Areas (area/zona meja), Tables (nomor meja per area), dan
> Kitchen Stations (stasiun dapur tujuan pesanan, mis. Dapur Panas/Dingin/Minuman) sebagai
> prasyarat tersembunyi sebelum sesi kasir meja (`restaurant/orders`) bisa dibuka — tidak
> disebutkan secara eksplisit di tahap mana pun pada dokumen ini sebelumnya. Tanpa data ini,
> halaman pembukaan sesi meja tidak punya area/meja untuk dipilih.
>
> **Untuk pengujian berikutnya**, tambahkan sebelum Tahap D dijalankan:
>
> | Sub-langkah      | Contoh data minimal                                                      |
> | ----------------- | ------------------------------------------------------------------------ |
> | Areas             | "Area Dalam", "Area Luar" (2 area cukup untuk uji Transfer Table)         |
> | Tables             | Meja 1–6 di "Area Dalam", Meja 7–10 di "Area Luar" (kapasitas bebas)      |
> | Kitchen Stations   | "Dapur Panas", "Dapur Dingin/Minuman" (dipetakan ke kategori menu 7.1)    |

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

> **Status: Selesai (2026-09-14).** Ketujuh produk jasa dibuat di `client-master/products`,
> Category **Layanan Sewa Aplikasi**, Sales Channels **Sales, Rental, Canvassing** (bukan Point
> of Sale — jasa langganan/sewa dijual lewat sales/kanvasing, bukan transaksi kasir langsung).
> Harga di-set via SKU → **Manage Prices** → **Add Price** (Currency **wajib** diganti manual ke
> IDR — dropdown selalu default ke currency lain, lihat temuan
> [`01-add-price-tidak-punya-price-list-selector.id.md`](../../erpApiServices/docs/TemuanTestCase/ClientMaster/Ranahku/01-add-price-tidak-punya-price-list-selector.id.md)).
> Terverifikasi tiap SKU: PKT-DASAR 150.000/bulan, PKT-USAHA 350.000/bulan, PKT-PRO 750.000/bulan,
> PKT-TAHUN-USAHA 3.500.000/tahun, PKT-TAHUN-PRO 7.500.000/tahun, PKT-SEWA-HARI 100.000/hari
> (Min Qty diset **3**), PKT-DAMPING 500.000/sekali — semua status Active.
>
> **Catatan gap untuk PKT-SEWA-HARI:** field **Min Qty** di modal Add Price generik untuk semua
> tipe harga (artinya "kuantitas minimum pembelian pada tier harga ini"), bukan business rule
> "durasi sewa minimum" yang tervalidasi otomatis saat transaksi (mis. sistem tidak otomatis
> menolak input sewa 1 atau 2 hari saat transaksi Rental/Canvassing dibuat). Min Qty = 3 di sini
> hanya representasi data master, belum tentu benar-benar men-*enforce* aturan "sewa minimal 3
> hari" di alur transaksional — perlu diverifikasi ulang saat menjalankan
> `02-alur-transaksi.id.md` Tahap C (atau tahap transaksi Rental terkait) apakah validasi minimum
> qty ini benar-benar dicek backend saat create order.

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

> **Status: Selesai (2026-09-14).** Ke-5 departemen dan ke-19 jabatan sudah
> dibuat sesuai tabel di atas, masing-masing dengan role akses otomatis
> (nama role sama dengan nama jabatan) dan gaji minimum/maksimum yang cocok.
>
> Hak akses tiap role sudah diisi dengan cara memilih modul yang relevan
> dengan pekerjaan jabatan tersebut, lalu menyalakan semua izin di modul itu
> sekaligus (bukan satu per satu). Beberapa jabatan mendapat tambahan izin
> dari modul lain yang memang dibutuhkan, misalnya kasir toko juga diberi
> izin melihat data produk. Untuk dua jabatan pucuk pimpinan (Direktur Utama
> dan Manajer Operasional), semua izin di seluruh sistem dinyalakan karena
> keduanya memang perlu bisa mengawasi semua bagian.
>
> Jumlah izin akhir tiap role: Direktur Utama 1118, Manajer Operasional 1118,
> Manajer Keuangan 56, Admin Kontrak & Sewa 68, Kasir Toko 27, Eksekutif
> Penjualan 120, Juru Masak 3, Kasir Rumah Makan 83, Koordinator Layanan
> Aplikasi 82, Pelayan 58, Petugas Kanvasing 48, Pramuniaga 27, Staf
> Administrasi & SDM 148, Staf Akunting 45, Staf Gudang 80, Staf Penagihan &
> Kasir Kantor 23, Staf Pendampingan Pelanggan 68, Supervisor Rumah Makan 83,
> Supervisor Toko 89. Pemilihan modul untuk tiap jabatan adalah keputusan
> praktis berdasarkan nama dan tanggung jawab jabatan, bukan daftar resmi
> dari perusahaan — jika ada kebutuhan akses yang lebih spesifik, sebaiknya
> disesuaikan lagi belakangan oleh yang paham alur kerja tiap bagian.

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

> **Status: Selesai (2026-09-14).** Ke-25 karyawan sudah dibuat sesuai tabel di
> atas, masing-masing dengan Jabatan yang benar (Departemen tidak diisi
> per-baris karena asosiasi departemen sudah cukup diwakili lewat Jabatan di
> Tahap 9.2, dan sistem tidak mewajibkannya). Semua akun login dicentang
> "Buat akun login" sehingga role dari Jabatan otomatis ikut menempel ke
> akun masing-masing. Nomor karyawan otomatis berurutan EMP/2026/0001 sampai
> EMP/2026/0025 sesuai urutan pembuatan (bukan urutan nomor di tabel).
>
> Satu catatan penting: saat mencentang "Buat akun login" di form tambah
> banyak karyawan, sistem membuatkan password sementara acak untuk tiap akun
> (ditampilkan sekali di layar, tidak bisa diatur manual ke angka tertentu).
> Ini tidak sesuai dengan instruksi awal supaya semua akun baru memakai
> password yang sama (12345678). Sebagai perbaikan, semua 25 password akun
> ini sudah disamakan manual ke 12345678 lewat halaman Users Manage
> (menu kebab tiap akun → Edit → isi "New Password" & "Password
> Confirmation" → Update) — jadi hasil akhirnya tetap sesuai kebutuhan,
> hanya prosesnya perlu satu langkah tambahan di luar form tambah banyak
> karyawan.

### 9.4 Jenis Cuti (**Leave Types**)

> **Catatan gap (ditemukan 2026-09-14 saat menjalankan `02-alur-transaksi.id.md` Tahap F.1):**
> menu **Human Resource Management > Leave Types** ternyata kosong sama sekali — tidak
> disebutkan sebagai langkah setup di dokumen ini sebelumnya, padahal jadi prasyarat wajib
> sebelum satu pun Leave Request bisa dibuat.
>
> **Untuk pengujian berikutnya**, tambahkan minimal 1 jenis cuti sebelum Tahap F.1, misalnya:
>
> | Kode           | Nama         | Kuota (hari) | Is Paid | Requires Approval | Active |
> | -------------- | ------------ | -----------: | ------- | ------------------ | ------ |
> | `CUTI-TAHUNAN` | Cuti Tahunan |           12 | Ya      | Ya                  | Ya     |
>
> **Perhatian saat mengisi**: toggle Is Paid/Requires Approval/Active yang diaktifkan saat
> **Create** tidak tersimpan (selalu jatuh ke Unpaid/No/Inactive) — bug yang sudah tercatat di
> [`erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/03-toggle-saat-buat-jenis-cuti-baru-tidak-tersimpan.id.md`](../../erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/03-toggle-saat-buat-jenis-cuti-baru-tidak-tersimpan.id.md).
> Setelah Create, buka **Edit** pada record yang sama dan aktifkan ulang ketiga toggle di sana
> supaya benar-benar tersimpan sebelum dipakai untuk pengajuan cuti.

### 9.5 Acuan BPJS & Pajak Penggajian (**Bpjs Settings**, **Payroll Tax Reference**)

> **Catatan gap (ditemukan 2026-09-14 saat menjalankan `02-alur-transaksi.id.md` Tahap F.2):**
> data acuan **Bpjs Settings** (rate iuran per program BPJS) dan **Payroll Tax Reference**
> (PTKP, tabel TER, tabel pajak progresif Pasal 17) untuk tahun 2026 ternyata **kosong sama
> sekali** — tidak disebutkan sebagai langkah setup di dokumen ini sebelumnya, padahal jadi
> prasyarat wajib supaya `payroll-periods/process` menghitung potongan BPJS/PPh21 yang benar
> (bukan Rp 0 untuk semua karyawan). Rincian lengkap ada di
> [`erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/06-potongan-bpjs-dan-pph21-payroll-selalu-nol-data-master-belum-diisi.id.md`](../../erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/06-potongan-bpjs-dan-pph21-payroll-selalu-nol-data-master-belum-diisi.id.md).
>
> **Untuk pengujian berikutnya**: sebelum mempercayai hasil Tahap F.2, pastikan lebih dulu ke tim
> dev bahwa seeder acuan BPJS/pajak tahun berjalan (2026 atau tahun saat pengujian dilakukan)
> sudah dijalankan di lingkungan yang diuji — halaman **Bpjs Settings** saat ini tidak
> menyediakan cara mengisi data ini secara manual lewat tampilan, jadi tidak bisa diakali dari
> sisi tester saja.

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

> **Status: Selesai (2026-09-14).** Rekening Bank "Bank Operasional Ranahku" berhasil
> dibuat dengan saldo awal 815.000.000, dan ke-14 baris saldo awal akun di atas (termasuk
> baris 1-110 yang otomatis tercatat lewat pembuatan rekening bank) sudah diisi lewat
> menu "Chart Of Accounts Balances", semua bertanggal 1 September 2026.
>
> Dua catatan penting selama proses ini:
>
> 1. **Rekening bank tidak bisa dibuat dengan saldo awal sebelum satu akun ditandai
>    sebagai "Is Opening Balance Equity Account".** Percobaan pertama membuat rekening
>    bank gagal dengan pesan "No Opening Balance Equity Account Configured For This
>    Branch". Setelah ditelusuri, ternyata akun `3-103 Ekuitas Saldo Awal` — walau
>    namanya dan kodenya sudah persis sesuai kebutuhan sejak Tahap 2 — belum otomatis
>    memiliki tanda ini. Perbaikannya: buka Chart of Accounts → Edit akun 3-103 →
>    aktifkan saklar "Is Opening Balance Equity Account" → Simpan. Setelah itu,
>    rekening bank berhasil dibuat.
> 2. **Sebagian besar akun tidak bisa langsung diisi saldo awalnya** lewat menu "Chart
>    Of Accounts Balances" sebelum kolom "Balance Is Required" pada akun tersebut
>    diaktifkan — sistem menolak dengan pesan "This COA does not require a balance
>    record." Dari 14 akun di tabel atas, hanya 1-101, 1-120 (tidak dipakai di tabel
>    ini), 1-130, 1-131, 2-110, dan 3-103 yang sudah otomatis punya tanda ini sejak
>    awal. Sisanya (1-102, 1-103, 1-140, 1-150, 1-201, 1-202, 1-203, 1-204, 3-101)
>    diaktifkan dulu tanda "Balance Is Required"-nya (lewat menu Bulk Edit Chart Of
>    Accounts atau satu-satu lewat "Edit With Balance"), baru saldo awalnya bisa
>    diisi. Kedua langkah ini kemungkinan besar memang bagian normal dari alur
>    konfigurasi (bukan bug), tapi tidak disebutkan di dokumentasi awal — dicatat di
>    sini supaya pengujian berikutnya tidak bingung kalau menemukan pesan error yang
>    sama.
>
> Total saldo Harta yang berhasil diinput dari 12 akun bertipe Debit murni (di luar
> 3-103) berjumlah 1.695.000.000, sedikit di bawah 1.700.000.000 yang disebut di
> ringkasan spesifikasi. Selisih 5.000.000 ini persis sesuai dengan yang sudah
> diantisipasi lewat catatan "offset otomatis lewat akun 3-103" di atas, sehingga
> akun `3-103 Ekuitas Saldo Awal` diisi saldo awal sebesar 5.000.000 supaya total
> Harta genap 1.700.000.000, seimbang dengan total Kewajiban + Modal.

> **Catatan gap (ditemukan 2026-09-14 saat menjalankan `02-alur-transaksi.id.md` Tahap C):**
> saldo awal stok barang toko (baris 1-130 di atas, senilai 90.000.000) ternyata hanya masuk ke
> **Gudang Utama** — **Gudang Toko Retail** (dari Tahap 4) tetap kosong sama sekali. Akibatnya,
> tombol "Open Session" kasir toko otomatis nonaktif karena warehouse tujuan tidak punya stok.
> Sistem sendiri sudah benar mencegah pembukaan sesi kasir dari gudang kosong, tapi langkah
> "pindahkan sebagian stok dari Gudang Utama ke Gudang Toko Retail" ini belum pernah disebutkan
> di dokumen ini sebagai bagian dari alur setup resmi. Detail di
> [`erpApiServices/docs/TemuanTestCase/Inventory/Ranahku/01-warehouse-baru-perlu-transfer-stok-manual-dari-gudang-utama.id.md`](../../erpApiServices/docs/TemuanTestCase/Inventory/Ranahku/01-warehouse-baru-perlu-transfer-stok-manual-dari-gudang-utama.id.md).
>
> **Untuk pengujian berikutnya**: sebelum membuka sesi kasir toko (Tahap C), buat dulu 1 dokumen
> **Stock Transfer** (Gudang Utama → Gudang Toko Retail) berisi SKU yang akan dipakai untuk
> transaksi kasir, dengan kuantitas secukupnya.

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

> **Status: Selesai (2026-09-14).** Ketujuh halaman konfigurasi jurnal (11.1 sampai 11.7)
> sudah diisi dan berhasil disimpan, semua sudah dicek ulang dengan cara membuka ulang
> halamannya supaya yakin datanya benar-benar tersimpan, bukan cuma kelihatan tersimpan
> sesaat.
>
> Beberapa catatan penting selama mengerjakan tahap ini:
> - Tombol "Auto Map From Chart Of Accounts" selalu menghasilkan pesan "tidak ada yang
>   bisa dipetakan otomatis" di ketujuh halaman. Ini wajar dan sudah diduga sebelumnya,
>   karena daftar akun (Chart of Accounts) Ranahku memakai nama-nama berbahasa Indonesia
>   yang dibuat khusus, sedangkan fitur auto-map mencocokkan berdasarkan nama akun
>   berbahasa Inggris bawaan sistem. Jadi semua pemetaan di atas dikerjakan manual satu
>   per satu sesuai tabel, dan ini bukan tanda ada yang salah/rusak.
> - Untuk fungsi yang di tabel tertulis "hasil auto-map" atau "kosongkan" (misalnya
>   `transit_clearing`, `cashback_liability`, `gr_ir`, `dp`, `return`,
>   `restaurant_service_charge_income`), kolom akunnya sengaja dibiarkan "Not Set" karena
>   fitur terkait (transfer antar gudang, program cashback, uang muka pembelian, dll)
>   memang belum dipakai di skenario pengujian Ranahku ini.
> - Fungsi `other_deductions_payable` di halaman Penggajian tidak punya akun khusus
>   "potongan lain-lain" di daftar akun Ranahku, jadi dipetakan sementara ke akun yang
>   sama dengan `salary_payable` (2-130 Utang Gaji) mengikuti catatan alternatif di
>   tabel spesifikasi.
> - Ditemukan satu catatan tampilan (bukan masalah fungsi) khusus di halaman Penggajian
>   (**hrm/payroll-journal-configuration**): nama-nama fungsi di kolom kiri tabel
>   (misalnya untuk `salary_expense`, `salary_payable`, dst) tampil sebagai kode program
>   mentah, bukan kalimat biasa seperti di enam halaman konfigurasi lainnya. Tidak
>   mengganggu proses simpan data (semua tetap tersimpan dengan benar), tapi sudah
>   dicatat detailnya di
>   `erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/01-payroll-journal-configuration-key-terjemahan-belum-ada.id.md`
>   supaya bisa diperbaiki tampilannya oleh tim developer.

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

> **Status: Selesai (2026-09-14), dengan penyesuaian.** Setelah dicek, kedua sub-tahap ini
> tidak bisa dijalankan persis seperti tertulis karena keterbatasan aplikasi, jadi dikerjakan
> versi yang paling mendekati sesuai kemampuan sistem saat ini. Detail lengkapnya sudah dicatat
> di
> `erpApiServices/docs/TemuanTestCase/ClientMaster/Ranahku/03-payment-methods-dan-payment-terms-tidak-sesuai-spec.id.md`.
> Ringkasnya:
> - **12.1 Metode Pembayaran**: halaman Payment Methods tidak punya cara memilih akun kas/bank
>   untuk tiap metode. Branch Ranahku ternyata sudah punya 10 metode pembayaran bawaan yang
>   aktif (Cash, Bank Transfer, Debit Card, Credit Card, QRIS, E-Wallet, Virtual Account,
>   Cheque, Cash on Delivery, Store Credit), jadi tidak perlu membuat metode baru. Penautan ke
>   akun kas/bank yang benar sudah tercakup lewat hasil kerja Tahap 11 (misalnya `pos_cash` di
>   Kasir Toko, `cash_bank` di Sewa Aplikasi dan Pembelian).
> - **12.2 Syarat Pembayaran**: tidak ada halaman master data "Payment Terms" di sistem ini
>   (dicoba dibuka, hasilnya halaman tidak ditemukan). Yang ada cuma kotak isian angka
>   "Payment Term Days" langsung di form tiap Contact, dan sudah dicek nilainya di data
>   kontak yang ada sekarang sudah sesuai kebutuhan (0, 14, 21, dan 30 hari).

---

## Daftar Periksa Cepat

- [ ] Tahap 1: cabang, IDR, tahun buku 2026, 3 unit usaha (SEWA/RETAIL/RESTO)
- [ ] Tahap 2: 7 tipe akun → 45 akun (cek flag pajak/kontrol/laba-ditahan/ekuitas-saldo-awal)
- [ ] Tahap 3: 5 pajak, tautkan ke akun pajak masing-masing
- [ ] Tahap 4: 2 gudang (Toko, Dapur)
- [ ] Tahap 5: 5 pemasok, 5 pelanggan + Pembeli Umum
- [ ] Tahap 6: 5 kategori, 9 satuan, 10 barang, 1 daftar harga, harga beli per pemasok
- [ ] Tahap 7: 2 kategori menu, 8 menu, stok bahan dapur 20 jt
- [x] Tahap 8: 7 paket sewa (layanan non-stok) — selesai 2026-09-14, lihat catatan gap Min Qty di atas
- [x] Tahap 9: 5 departemen → 19 jabatan (semua "buat role") → atur hak akses 19 role → 25 karyawan — selesai semua (2026-09-14), termasuk penyamaan password 25 akun login ke 12345678
- [x] Tahap 10: 1 rekening bank + saldo awal (harta = 1,7 M, seimbang) — selesai (2026-09-14), lihat catatan syarat "Balance Is Required" & "Is Opening Balance Equity Account" di atas
- [x] Tahap 11: 7 halaman konfigurasi jurnal — selesai (2026-09-14), lihat catatan "auto-map tidak menemukan apa pun" & temuan tampilan halaman Penggajian di atas
- [x] Tahap 12: metode pembayaran, syarat pembayaran — selesai (2026-09-14) dengan penyesuaian, lihat catatan gap fitur di atas
