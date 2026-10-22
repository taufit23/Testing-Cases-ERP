---
title: (PT Sehat Sentosa Farma) — 00b. Tipe Akun dan Chart of Accounts Acuan
category: sehat-sentosa-farma
description: Daftar tipe akun dan akun yang harus ada di Chart of Accounts sebelum transaksi diuji, lengkap dengan kode, tipe, saldo normal, dipakai oleh modul mana, dan saldo awal. Menjadi acuan untuk alur terpadu file 01 dan semua pemeriksaan jurnal.
visibility: internal
---

# 00b. Tipe Akun dan Chart of Accounts Acuan

> **Kenapa file ini ada.** Klien baru dari `/subscribe` **tidak** mendapat tipe akun maupun akun otomatis. Tanpa daftar acuan, tiap penguji membuat akun
> seenaknya, sehingga angka jurnal di file `01` ("Dr Persediaan / Cr barang diterima belum ditagih" dan seterusnya) tidak bisa dibandingkan.
> Daftar di bawah dihitung dari **akun yang benar-benar disentuh alur `01`**, bukan dari template umum.

## 1. Cara memasukkannya

**Dikerjakan oleh:** Dr. Rahmat. **Cabang aktif:** Kantor Pusat & Distribusi Jakarta (ulangi untuk cabang lain yang punya pembukuan sendiri).

| Langkah | Menu dan URL | Yang dikerjakan |
| --- | --- | --- |
| 1 | `Client Master → Chart of Account Type` (`/client-master/chart-of-account-type`) | Buat **8 tipe akun** di bagian 2 |
| 2 | `Client Master → Chart of Accounts` (`/client-master/chart-of-accounts`) | Buat **akun** di bagian 3, satu per satu atau massal (**Bulk Add**) atau impor Excel |
| 3 | Chart of Accounts, kolom akun saldo awal | Tandai **Modal Pemilik** (`3101`) sebagai **akun saldo awal** |
| 4 | `Finance → Bank Accounts` (`/finance/bank-accounts`) | Hubungkan **Bank Operasional** (`1102`) ke rekening bank |
| 5 | `Client Master → Chart of Accounts Balances` (`/client-master/chart-of-accounts-balances`) atau lewat COA | Isi saldo awal bagian 5, tanggal 1 Oktober 2026 |
| 6 | Halaman konfigurasi tiap modul (bagian 4) | Hubungkan akun ke fungsi jurnal modul |

> **Jangan mencampur dengan template.** Tombol **Use Template** menyalin pohon akun siap pakai (kode seperti `1101 Kas dan Setara Kas`, `1401 Persediaan`) yang **kodenya bentrok** dengan daftar ini.
> Pilih satu jalur untuk suite ini:
> - **Jalur A (disarankan):** COA masih kosong, buat sendiri dari bagian 2 dan 3. Hasilnya persis sama dengan angka acuan `01`.
> - **Jalur B (uji tombol template):** pakai template **Dagang** atau **Umum**, lalu tambahkan akun yang kurang di bagian 3 (tandai di kolom "Ada di template?"). Catat selisih nama dan kode sebagai temuan, jangan mengubah acuan.
>
> Template **Kesehatan** hanya berisi 13 akun (Kas, Piutang BPJS, Stok Obat dan Alkes, Peralatan Medis, Gaji Tenaga Medis, Biaya Obat dan BHP, dan induknya). **Tidak cukup** untuk alur ini dan tidak punya akun pajak, utang, atau ekuitas lengkap.

## 2. Tipe akun (8 tipe)

Kolom di form tipe akun: **Code**, **Name**, **Report group**. Gunakan kode di bawah.

| Code | Name | Report group | Dipakai untuk |
| --- | --- | --- | --- |
| `SSF-AST-LANCAR` | Aset Lancar | Balance Sheet | Kas, bank, piutang, persediaan, pajak dibayar di muka |
| `SSF-AST-TETAP` | Aset Tetap | Balance Sheet | Peralatan medis, aset sewa, akumulasi penyusutan |
| `SSF-LIABILITAS` | Liabilitas | Balance Sheet | Utang usaha, utang pajak, utang gaji, deposit |
| `SSF-EKUITAS` | Ekuitas | Balance Sheet | Modal pemilik, laba ditahan |
| `SSF-PENDAPATAN` | Pendapatan | Income Statement | Penjualan, jasa, sewa, kafe, pendapatan lain |
| `SSF-HPP` | Harga Pokok | Income Statement | HPP, retur pembelian, selisih persediaan |
| `SSF-BEBAN` | Beban Usaha | Income Statement | Gaji, listrik, penyusutan, royalti, administrasi |
| `SSF-LAIN` | Pendapatan dan Beban Lain | Income Statement | Selisih kurs, laba atau rugi pelepasan aset |

## 3. Akun (kode, nama, tipe, saldo normal)

Nama di kolom **Nama akun** adalah acuan yang dipakai di file `01` dan di pemeriksaan jurnal. Kode boleh kamu sesuaikan, **nama jangan**.
Kolom **Saldo normal**: D = debit, K = kredit.

### 3.1 Aset lancar (`SSF-AST-LANCAR`)

| Kode | Nama akun | Saldo normal | Dipakai oleh |
| --- | --- | --- | --- |
| `1101` | Kas Kecil | D | Pembayaran tunai: Sales Payment Bill, kas POS, penagihan lapangan, kafe |
| `1102` | Bank Operasional | D | Transfer pembayaran pembelian dan penjualan, **saldo awal**, payout biaya, rekonsiliasi bank |
| `1103` | Dana Gateway dan QRIS (Penyelesaian) | D | Pembayaran QRIS sebelum dana masuk bank (`/finance/payment-settlements`) |
| `1201` | Piutang Usaha | D | Sales Invoice, Rental Invoice, umur piutang |
| `1301` | Persediaan Barang Dagang | D | Goods Receipt, transfer stok, penjualan, opname (obat, alkes) |
| `1302` | Persediaan Bahan Baku | D | Bahan baku produksi (kunyit, asam, kalsium karbonat) |
| `1303` | Persediaan Barang Dalam Proses | D | Production Order saat berjalan |
| `1304` | Persediaan Barang Jadi | D | Hasil produksi (jamu, suplemen) di gudang barang jadi |
| `1401` | PPN Masukan | D | Pajak pada Purchase Invoice |
| `1402` | Uang Muka Pembelian | D | Down payment ke pemasok (fungsi `dp` di Purchase Configs) |

### 3.2 Aset tetap (`SSF-AST-TETAP`)

| Kode | Nama akun | Saldo normal | Dipakai oleh |
| --- | --- | --- | --- |
| `1501` | Aset Tetap | D | Autoclave Rp 60.000.000 dan peralatan lain (`/fixed-assets/assets`) |
| `1502` | Akumulasi Penyusutan | K | Penyusutan bulanan (kontra aset) |
| `1503` | Aset Sewa Alat Medis | D | Kursi roda, tabung oksigen, tempat tidur (modul Sewa) |

### 3.3 Liabilitas (`SSF-LIABILITAS`)

| Kode | Nama akun | Saldo normal | Dipakai oleh |
| --- | --- | --- | --- |
| `2101` | Utang Usaha | K | Purchase Invoice, umur utang |
| `2102` | Barang Diterima Belum Ditagih | K | Penghubung Goods Receipt dan Purchase Invoice (fungsi `gr_ir`) |
| `2201` | Utang PPN (PPN Keluaran) | K | Pajak pada Sales Invoice |
| `2301` | Utang Gaji | K | Payroll sebelum dibayar |
| `2302` | Utang Biaya | K | Biaya (listrik 2.500.000) sebelum dibayar |
| `2303` | Utang Deposit Sewa | K | Deposit pelanggan sewa (300.000 pada `01` langkah 23) |
| `2304` | Utang Royalti Tambang | K | Royalti modul Pertambangan |

### 3.4 Ekuitas (`SSF-EKUITAS`)

| Kode | Nama akun | Saldo normal | Dipakai oleh |
| --- | --- | --- | --- |
| `3101` | Modal Pemilik | K | **Akun saldo awal** (wajib ditandai). Lawan saldo awal bank |
| `3102` | Laba Ditahan | K | Tutup tahun fiskal |

### 3.5 Pendapatan (`SSF-PENDAPATAN`)

| Kode | Nama akun | Saldo normal | Dipakai oleh |
| --- | --- | --- | --- |
| `4101` | Pendapatan Penjualan | K | Sales Invoice grosir, POS apotek, kanvasing |
| `4102` | Pendapatan Jasa | K | POS kasir jasa (klinik, lab) |
| `4103` | Pendapatan Sewa | K | Rental Invoice |
| `4104` | Pendapatan Kafe | K | Restoran |
| `4201` | Retur dan Potongan Penjualan | D | Sales Return, retur POS, diskon |
| `4901` | Pendapatan Lain-lain | K | Denda sewa (50.000), selisih kas lebih |

### 3.6 Harga pokok (`SSF-HPP`)

| Kode | Nama akun | Saldo normal | Dipakai oleh |
| --- | --- | --- | --- |
| `5101` | Harga Pokok Penjualan | D | Delivery, POS (acuan `01` langkah 13: 4.300.000) |
| `5102` | Retur Pembelian | K | Purchase Return (kontra pembelian) |
| `5103` | Selisih Persediaan | D | Stock adjustment dan opname (kurang 2 strip = 6.000) |
| `5104` | Biaya Pengiriman dan Landed Cost | D | Purchase Charge Invoice (ongkir, asuransi, bea masuk) |

### 3.7 Beban usaha (`SSF-BEBAN`)

| Kode | Nama akun | Saldo normal | Dipakai oleh |
| --- | --- | --- | --- |
| `6101` | Beban Gaji | D | Payroll Oktober |
| `6201` | Beban Listrik | D | Kategori biaya Listrik (`01` langkah 28) |
| `6301` | Beban Penyusutan | D | Penyusutan autoclave 1.000.000 per bulan |
| `6401` | Beban Royalti Tambang | D | Modul Pertambangan |
| `6501` | Selisih Kas Kasir | D | Tutup sesi POS bila selisih dicatat |
| `6601` | Beban Umum dan Administrasi | D | Biaya lain-lain, biaya proyek bila saklarnya menyala |

### 3.8 Pendapatan dan beban lain (`SSF-LAIN`)

| Kode | Nama akun | Saldo normal | Dipakai oleh |
| --- | --- | --- | --- |
| `7101` | Laba atau Rugi Selisih Kurs | K | Transaksi mata uang asing (bila diuji) |
| `7102` | Laba atau Rugi Pelepasan Aset | K | Penjualan atau penghapusan aset tetap |

**Jumlah: 8 tipe dan 40 akun.** Akun `1304`, `1303`, `2304`, `6401`, `1503`, `2303` hanya perlu bila modul terkait (Manufaktur, Pertambangan, Sewa) ikut diuji.
Kalau modul itu belum kamu sentuh, akunnya boleh menyusul, tetapi **buat sebelum langkahnya**, bukan sesudah.

## 4. Hubungkan akun ke modul (langkah yang sering terlupa)

Membuat akun saja tidak cukup. Tiap modul perlu tahu **akun mana untuk fungsi jurnal mana**. Kalau belum diisi, dokumen tetap bisa dibuat tetapi **jurnalnya kosong atau gagal**.
Kerjakan sebelum transaksi modul itu:

| Modul | Halaman | Hubungkan |
| --- | --- | --- |
| Pembelian | `/purchasing/purchase-configs` | `inventory` → 1301, `ap` → 2101, `gr_ir` → 2102, `ppn_masukan` → 1401, `cash_bank` → 1102, `dp` → 1402, `return` → 5102, `purchase_expense` → 5104 |
| Penjualan | `/sales/sales-journal-configuration` | Piutang → 1201, Pendapatan → 4101, Utang PPN → 2201, HPP → 5101, Persediaan → 1301, Retur → 4201, Kas dan bank → 1101 dan 1102 |
| Persediaan | `/inventory/config` | Akun selisih persediaan → 5103 |
| POS | `/pos/pos-configs` | Kas → 1101, QRIS → 1103, Pendapatan → 4101 dan 4102, selisih kas → 6501 |
| Restoran | `/restaurant/config` | Pendapatan → 4104, kas dan QRIS |
| Manufaktur | `/manufacturing/config` | Bahan baku → 1302, WIP → 1303, barang jadi → 1304 |
| Pertambangan | `/mining/config` | Royalti → 2304 dan 6401 |
| Sewa | `/rental/rental-configs` | Piutang → 1201, Pendapatan → 4103, Deposit → 2303, Denda → 4901 |
| SDM | `/hrm/payroll-journal-configuration` | Beban gaji → 6101, Utang gaji → 2301, Bank → 1102 |
| Biaya | `/expense/expense-categories` | Kategori **Listrik** → 6201, lawan utang biaya → 2302 |
| Aset tetap | `/fixed-assets/assets` | Aset → 1501, akumulasi → 1502, beban penyusutan → 6301, pelepasan → 7102 |

> Label fungsi di tiap halaman bisa sedikit berbeda dari tabel ini. Pasangkan berdasarkan **arti** akunnya. Kalau satu fungsi tidak punya akun yang cocok di daftar, catat sebagai temuan.

## 5. Saldo awal (1 Oktober 2026)

| Akun | Debit | Kredit |
| --- | ---: | ---: |
| `1102` Bank Operasional | 500.000.000 | |
| `3101` Modal Pemilik | | 500.000.000 |
| **Total** | **500.000.000** | **500.000.000** |

Tanpa persediaan awal, supaya semua angka di file `01` bisa dihitung dari nol. Setelah diisi, `Reports → Trial Balance` (`/reports/trial-balance`) harus menunjukkan kedua sisi **Rp 500.000.000**.

## 6. Kasus uji khusus data akun

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — tipe akun | Buat 8 tipe bagian 2 satu per satu, dua di antaranya lewat **Bulk Add** | Semua tipe tersimpan dengan kode unik |
| Negatif — kode tipe ganda | Buat tipe dengan kode `SSF-HPP` yang sudah ada | Ditolak dengan pesan jelas |
| Positif — akun | Buat akun bagian 3 dengan tipe sesuai | Muncul di pohon akun dengan saldo normal benar |
| Negatif — akun tanpa tipe | Kosongkan tipe lalu simpan | Ditolak per kolom |
| Negatif — kode akun ganda | Buat akun dengan kode `1101` yang sudah ada | Ditolak |
| Aturan manual — akun saldo awal | Isi saldo awal **sebelum** menandai `3101` sebagai akun saldo awal | Gagal dengan pesan jelas (bukan error server) |
| Positif — saldo awal | Tandai `3101`, isi saldo bagian 5 | Trial Balance seimbang Rp 500.000.000 per sisi |
| Negatif — saldo awal tidak seimbang | Isi Bank 500.000.000 tanpa modal | Ditolak atau ditandai tidak seimbang, tidak diam-diam tersimpan |
| Positif — hubungkan modul | Isi tabel bagian 4 untuk Pembelian, lalu buat satu Goods Receipt | Jurnal GR menyebut `1301` dan `2102` dengan angka sesuai |
| Negatif — modul belum dihubungkan | Buat Goods Receipt sebelum fungsi `inventory` diisi | Pesan jelas bahwa akun belum diatur, bukan jurnal kosong diam-diam |
| Negatif — peran tanpa izin | Masuk sebagai Kasir lalu buka `/client-master/chart-of-accounts` | Tombol nonaktif dengan tooltip, endpoint 403 |
| Netralisasi | Akun yang sudah dipakai jurnal tidak dihapus; nonaktifkan atau balik jurnalnya | Data uji berikutnya tetap utuh |
