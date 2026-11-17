---
title: (PT Medika Nusantara Sejahtera) — 00. Profil Perusahaan, Master Data Acuan dan Prasyarat
category: medika-nusantara-sejahtera
description: Skenario perusahaan kesehatan terpadu (apotek, klinik dan laboratorium, distribusi obat, pabrik herbal, kafe, sewa alat medis, tambang kapur) yang dipakai semua file di suite ini. Memuat cabang, peran, data acuan, urutan kerja dan aturan membaca hasil.
visibility: internal
---

# 00. Profil Perusahaan, Master Data Acuan dan Prasyarat

> **Kenapa bagian ini diuji (bahasa sederhana).** Menyiapkan "panggung" sebelum bermain: data perusahaan, cabang, pengguna, produk, mitra, dan akun yang akan dipakai semua file lain.
>
> **Kalau semuanya benar, artinya:** Semua file berikutnya punya bahan yang sama untuk dikerjakan. Kalau bagian ini berantakan, hasil uji di modul lain jadi membingungkan.


Suite ini menguji **seluruh modul dan seluruh bab manual book** lewat satu perusahaan kesehatan yang saling terhubung. Berbeda dari suite
`accounting-klinik-*` dan `accounting-rumah-sakit` yang berdiri di modul Akuntansi saja, di sini satu transaksi mengalir lintas modul:
barang dibeli, disimpan, dipindah, diolah, dijual, dibayar, digaji, dan akhirnya muncul di laporan.

> **Cara suite ini disusun.** File `01` adalah **alur terpadu** yang ditulis tangan dengan angka acuan yang bisa dihitung ulang.
> File `02` sampai `20` adalah **kasus per modul**: satu bagian per bab manual book, dengan baris Positif dan Negatif yang
> **dirancang oleh Ollama lokal (qwen2.5:7b-instruct) dari isi bab manual book** dan sudah disaring. Baris dari Ollama berstatus
> **draf**: harus dibaca penguji dan disesuaikan dengan layar sebenarnya sebelum dianggap final. File `99` memetakan setiap bab ke
> file ujinya, jadi tidak ada fitur yang terlewat.

> **Dua lapisan suite.** Lapisan pertama (`01`–`20`, `98`, `99`) mengikuti **modul yang sudah ada**. Lapisan kedua dibuat dari **kebutuhan bisnis grup usaha kesehatan**
> dan sengaja menguji hal yang mungkin belum didukung: riset di [`96`](./96-riset-kebutuhan-bisnis-grup-kesehatan.id.md), kasus uji dan status dukungan di
> [`21`](./21-kebutuhan-bisnis-kesehatan-dan-uji-celah.id.md), pembanding Odoo di [`97`](./97-referensi-odoo-amati-tiru-modifikasi.id.md), dan register celah beserta usulan
> perbaikan di [`95`](./95-daftar-celah-dan-usulan-perbaikan.id.md). Hasil pengujian lapisan kedua adalah **bahan memilih prioritas pengembangan**.

## 1. Profil

**PT Medika Nusantara Sejahtera** (merek "Medika Nusantara"), grup usaha kesehatan, berstatus PKP, mata uang Rupiah, tahun fiskal Januari sampai
Desember 2026. Periode uji utama: **Oktober 2026**.

### 1.1 Satu kalimat profil di atas diisi di tiga tingkat yang berbeda

Kalimat profil itu bukan satu formulir. Aplikasi memisahkan data menjadi **tiga tingkat**, dan tiap atribut hidup di tingkat yang berbeda:

| Tingkat | Artinya | Siapa yang mengisi | Contoh di profil ini |
| --- | --- | --- | --- |
| **Perusahaan (provider)** | Entitas klien yang berlangganan. **Tidak ada halaman "profil perusahaan" yang bisa diedit klien.** Terbentuk sekali lewat pengajuan `/subscribe` yang disetujui owner | Calon klien saat mendaftar; owner saat menyetujui | Nama "PT Medika Nusantara Sejahtera", paket langganan, batas cabang dan pengguna |
| **Cabang** | Satu lokasi atau unit usaha di bawah perusahaan. Hampir semua pengaturan operasional melekat di sini | Klien (Dr. Andika) | Alamat, cabang utama, mata uang bawaan, tahun fiskal, pajak, gudang |
| **Data master milik cabang** | Isi yang dipakai transaksi: akun, produk, mitra, gudang, pengguna | Klien | Seluruh data acuan §3 |

### 1.2 Atribut profil dan tempat memasukkannya

| Atribut di profil | Tingkat | Diisi di (menu dan URL) | Diisi dengan | Catatan |
| --- | --- | --- | --- | --- |
| Nama perusahaan "PT Medika Nusantara Sejahtera" | Perusahaan | Formulir `/subscribe` (kolom Nama Perusahaan); owner melihatnya di `Core → Penyuplai` (`/core/providers`) | `PT Medika Nusantara Sejahtera` | Sudah terisi lewat pengajuan. Klien tidak mengubahnya sendiri |
| Nama cabang pertama dan alamatnya | Cabang | Formulir `/subscribe` (cabang pertama); lanjutan di `Client Master → Branch Manage` (`/client-master/branch-manage`) | `Kantor Pusat & Distribusi Jakarta`, alamat, provinsi, kota, kecamatan, kelurahan, kode pos 5 digit | Koordinat bisa diisi lewat pencarian wilayah atau manual |
| Cabang lain (Bandung, Bekasi, Sukabumi, Kafe) | Cabang | `Client Master → Branch Manage` (`/client-master/branch-manage`) → **Add Branch** | Nama dan alamat tiap cabang (tabel di bawah) | Dibatasi **batas cabang paket**. Melebihi batas harus ditolak (`00a` S11) |
| Cabang utama (Pusat) | Cabang | `Branch Manage`, kolom **This branch is a main branch** | Aktif untuk Pusat | Cabang anak memakai **Reports to main branch**. Menentukan laporan gabungan |
| Pembukuan cabang digabung di pusat | Cabang | `Branch Manage`, kolom **Keep this branch's accounting in the main branch** | Biarkan mati untuk pengujian ini kecuali kasus khusus | Ini mode akuntansi terpusat; mengubah arah jurnal, jangan dinyalakan tanpa alasan |
| Mata uang Rupiah | Cabang | `Client Master → Mata Uang` (`/client-master/currencies`) | Pilih IDR, tandai sebagai mata uang yang dipakai cabang (badge **Used by branch**) | Dikerjakan **per cabang**. Kurs mata uang lain di `Client Master → Kurs Valuta Asing` |
| Tahun fiskal Januari sampai Desember 2026 | Cabang | `Client Master → Tahun Fiskal` (`/client-master/fiscal-year`) | Kode `FY2026`, nama, mulai `2026-01-01`, selesai `2026-12-31` | Wajib sebelum ada jurnal atau saldo awal |
| 12 periode akuntansi | Cabang | `Client Master → Periode Akuntansi` (`/client-master/accounting-period`) | Pilih tahun fiskal, durasi bulanan, mulai Januari 2026 | Periode berjalan bisa otomatis (mengikuti tanggal) atau dikunci manual |
| Berstatus PKP dan PPN 11% | Cabang | `Client Master → Pajak` (`/client-master/taxes`) | Kode `PPN`, nama `PPN 11%`, tarif `11`, jenis pajak keluaran dan masukan | **Tidak ada kolom "status PKP" di aplikasi** (tidak ditemukan di kode maupun skema). Cukup buat pajak PPN 11% dan pakai di dokumen. Kalau PKP formal ingin diuji, catat sebagai celah |
| Merek "Medika Nusantara" di dokumen cetak | Cabang | `Client Master → Pengaturan Penataan PDF` (`/client-master/pdf-layout-settings`), kolom **Company name override** | `Medika Nusantara` (opsional), logo, catatan header dan footer | **Tidak ada kolom merek di profil perusahaan.** Merek hanya muncul di tata letak PDF |
| Periode uji Oktober 2026 | Data uji | Tidak ada isian. Itu tanggal transaksi saat membuat dokumen | Tanggal dokumen di Oktober 2026 | Pastikan periode Oktober berstatus terbuka |

> **Kalau sebuah atribut tidak ketemu di layar:** kemungkinan besar memang tidak ada. Jangan dicari lama-lama; catat di tabel temuan README sebagai **Celah** dan lanjutkan.

### 1.3 Cabang yang dibuat

| Cabang | Fungsi | Modul yang dominan |
| --- | --- | --- |
| **Kantor Pusat & Distribusi Jakarta** (cabang utama) | gudang obat dan alat kesehatan, penjualan grosir ke klinik dan apotek mitra, pembukuan pusat | Pembelian, Persediaan, Penjualan, Kanvasing, Akuntansi, Keuangan, Aset Tetap |
| **Apotek Nusantara Bandung** | apotek retail, resep, QRIS | POS, Persediaan, Pembayaran online |
| **Klinik Pratama & Laboratorium Bekasi** | layanan medis, kasir, tenaga kesehatan | SDM, POS (kasir jasa), Proyek (akreditasi) |
| **Pabrik Herbal Sukabumi** | produksi jamu dan suplemen, bahan baku kalsium karbonat | Manufaktur, Pertambangan |
| **Kafe Sehat (lobi klinik)** | kafe pasien dan keluarga | Restoran |
| **Layanan Sewa Alat Medis** (dikelola Pusat) | kursi roda, tabung oksigen, tempat tidur pasien | Sewa |

Cabang Pusat adalah **cabang utama** (laporan bisa digabung dengan cabang anak). Provider ini **lahir dari alur berlangganan** ([`00a`](./00a-perjalanan-berlangganan-klien.id.md)): calon klien menemukan aplikasi di landing page, mengirim formulir minat, owner membuat Client Onboarding dan memprovisi, klien membayar tagihan dan login pertama. Data cabang, pengguna dan master di bawah ini dibuat **klien sendiri setelah itu**, bukan diisi lebih dulu oleh admin atau seeder.

## 2. Peran dan pengguna uji

| Peran | Contoh pengguna | Ruang lingkup |
| --- | --- | --- |
| Direktur (admin klien) | Dr. Andika Pratama Wijaya | semua modul, persetujuan tingkat akhir |
| Manajer Keuangan | Citra Maharani | Akuntansi, Keuangan, Aset Tetap, laporan, persetujuan biaya dan jurnal |
| Staf Pembelian | Fajar Nugroho | Pembelian |
| Kepala Gudang | Teguh Santosa | Persediaan, penerimaan barang, transfer, stok opname |
| Apoteker Penanggung Jawab | Apt. Ratna Kusumawati | POS apotek, obat resep, persetujuan retur |
| Kasir Apotek | Nadia Safitri | POS (hanya sesi kasirnya sendiri) |
| Sales Lapangan | Rizky Aulia | Kanvasing |
| Kepala Produksi | Slamet Riyadi | Manufaktur |
| Staf HR | Indah Permatasari | SDM, rekrutmen, payroll |
| Pemilik Platform | (akun owner) | Platform Owner: paket, klien, penangguhan |

### 2.1 Departemen dan jabatan (kerjakan SEBELUM membuat pengguna)

Tiap peran di tabel di atas punya **jabatan**, dan form Jabatan **mewajibkan Departemen**. Jadi departemen harus ada lebih dulu. Form Jabatan juga punya pilihan **Peran Akses**:
kamu bisa memilih peran yang sudah dibuat, atau mencentang "buat peran akses baru dengan nama jabatan ini" supaya peran terbentuk otomatis.

**Langkah 1: buat 8 departemen** di `HRM → Departemen` (`/hrm/departments`), tombol **Tambah Departemen**. Kode dan nama wajib; Departemen Induk dan deskripsi boleh kosong.

| Kode | Nama departemen | Departemen induk | Kenapa perlu |
| --- | --- | --- | --- |
| MNJ-001 | Manajemen | - | Menaungi Direktur |
| KEU-001 | Keuangan dan Akuntansi | - | Menaungi Manajer Keuangan |
| PBL-001 | Pembelian | - | Menaungi Staf Pembelian |
| GDG-001 | Gudang dan Logistik | - | Menaungi Kepala Gudang |
| FRM-001 | Farmasi | - | Menaungi Apoteker dan Kasir Apotek |
| PJL-001 | Penjualan Lapangan | - | Menaungi Sales Lapangan |
| PRD-001 | Produksi | - | Menaungi Kepala Produksi |
| SDM-001 | SDM dan Umum | - | Menaungi Staf HR |

**Langkah 2: buat peran** di `Client Master → Peran` dan atur izinnya (lihat "Cara membuatnya" di bawah). Kalau lebih suka cepat, lewati langkah ini dan biarkan form Jabatan membuat peran barunya (langkah 3), lalu atur izinnya belakangan.

**Langkah 3: buat 9 jabatan** di `HRM → Jabatan` (`/hrm/positions`), tombol **Tambah Posisi**. Nama dan Departemen wajib; gaji minimum dan maksimum, deskripsi, dan Peran Akses boleh kosong.

| Nama jabatan | Departemen | Peran Akses | Gaji minimum | Gaji maksimum |
| --- | --- | --- | ---: | ---: |
| Direktur | Manajemen | Direktur (admin klien) | 25.000.000 | 60.000.000 |
| Manajer Keuangan | Keuangan dan Akuntansi | Manajer Keuangan | 12.000.000 | 22.000.000 |
| Staf Pembelian | Pembelian | Staf Pembelian | 5.000.000 | 9.000.000 |
| Kepala Gudang | Gudang dan Logistik | Kepala Gudang | 7.000.000 | 13.000.000 |
| Apoteker Penanggung Jawab | Farmasi | Apoteker Penanggung Jawab | 9.000.000 | 16.000.000 |
| Kasir Apotek | Farmasi | Kasir Apotek | 4.500.000 | 7.000.000 |
| Sales Lapangan | Penjualan Lapangan | Sales Lapangan | 4.500.000 | 9.000.000 |
| Kepala Produksi | Produksi | Kepala Produksi | 8.000.000 | 15.000.000 |
| Staf HR | SDM dan Umum | Staf HR | 5.000.000 | 9.500.000 |

> **Kenapa urutannya begini.** Departemen adalah wadah, jabatan duduk di dalam departemen, dan pengguna serta karyawan menempati jabatan. Kalau dibalik, form Jabatan tidak punya pilihan
> Departemen dan tidak bisa disimpan. Angka gaji di atas hanya contoh untuk uji dan boleh disesuaikan; file `16` memakai jabatan ini saat mendaftarkan karyawan dan menghitung gaji.
> Kalau satu departemen sudah ada, jangan dibuat ganda: periksa daftar dulu.

### 2.2 Cara membuatnya (urutan lengkap)

| Langkah | Menu dan URL | Isi |
| --- | --- | --- |
| 1. Buat departemen | `HRM → Departemen` (`/hrm/departments`) | 8 departemen di tabel 2.1: kode, nama, departemen induk (kosong), deskripsi |
| 2. Buat peran | `Client Master → Peran` (`/client-master/roles`) | Nama peran (mis. `Kasir Apotek`), deskripsi, status aktif; lalu atur izinnya. Peran klien **hanya bisa memberi izin yang dimiliki pembuatnya**. Boleh dilewati bila peran dibuat lewat form Jabatan |
| 3. Buat jabatan | `HRM → Jabatan` (`/hrm/positions`) | Nama, **Departemen (wajib)**, gaji minimum dan maksimum, deskripsi, **Peran Akses** (pilih peran langkah 2, atau centang buat peran baru) |
| 4. Buat pengguna | `Client Master → Pengguna` (`/client-master/users`) | Nama, email, kata sandi dan konfirmasinya, status aktif, PIN override manajer (untuk kasir yang butuh persetujuan atasan) |
| 5. Hubungkan pengguna ke cabang | `Client Master → Branch Manage` (`/client-master/branch-manage`), pilih cabang → **Assign user** | Pilih pengguna, tandai aktif di cabang itu |
| 6. Data karyawan (untuk yang digaji) | `HRM → Karyawan` (`/hrm/employees`) | Dikerjakan di file `16`: karyawan memilih departemen dan jabatan dari langkah 1 dan 3 |

Pengguna dibatasi **batas pengguna paket**. Untuk uji izin, masuk bergantian sebagai tiap peran dan buka halaman yang bukan haknya.

Peran uji dipakai juga untuk kasus **izin**: setiap file modul punya baris "peran tanpa izin" yang harus berujung 403 dan tombol
berstatus nonaktif dengan penjelasan, bukan tombol hilang.

## 3. Data acuan

### 3.1 Mitra

| Kode | Nama | Jenis | Catatan |
| --- | --- | --- | --- |
| SUP-01 | PT Bintang Farmasi Utama | pemasok obat | termin 14 hari |
| SUP-02 | PT Alkes Prima Mandiri | pemasok alat kesehatan | termin 30 hari |
| SUP-03 | CV Kapur Medika | pemasok bahan baku (tambang kapur) | internal grup, dicatat sebagai pemasok |
| CUS-01 | Klinik Pratama Harapan Sehat | pelanggan grosir | batas kredit Rp 20.000.000, termin 14 hari |
| CUS-02 | Apotek Mitra Sehat | pelanggan grosir dan calon kanvasing | batas kredit Rp 10.000.000 |
| CUS-03 | Pasien Umum | pelanggan POS | tanpa kredit |

**Input di:** `Client Master → Kontak` (`/client-master/contacts`). Satu halaman untuk pemasok dan pelanggan; dibedakan lewat kolom **Type**.

| Yang diisi | Kolom di form | Contoh |
| --- | --- | --- |
| Nama | Name | `PT Bintang Farmasi Utama` |
| Jenis | Type | Pemasok untuk SUP-xx, pelanggan untuk CUS-xx |
| Telepon dan email | Phone, Email | bebas (telepon hanya angka) |
| Termin bayar | Payment term days | `14` untuk SUP-01 dan CUS-01, `30` untuk SUP-02 |
| Batas kredit | Credit limit | `20000000` untuk CUS-01, `10000000` untuk CUS-02 |
| Pelanggan POS bawaan | Walking customer (POS default) | aktif hanya untuk CUS-03 Pasien Umum |
| Mata uang | Currency | IDR |

Alamat dan rekening bank mitra diisi di halaman terpisah: `Client Master → Alamat Kontak` (`/client-master/contact-addresses`) dan `Rekening Bank Kontak` (`/client-master/contact-bank-accounts`).
Kode `SUP-01` dan seterusnya hanya **sebutan di dokumen uji**; aplikasi membuat kodenya sendiri, jadi catat nama pemasoknya.

### 3.2 Produk dan harga acuan

| SKU | Produk | Satuan | Harga beli | Harga jual grosir | Harga jual apotek | Catatan |
| --- | --- | --- | ---: | ---: | ---: | --- |
| OBT-001 | Paracetamol 500 mg | strip | 3.000 | 4.500 | 6.000 | obat bebas |
| OBT-002 | Amoxicillin 500 mg | strip | 9.000 | 12.000 | 15.000 | obat keras, wajib resep di apotek |
| SUP-001 | Vitamin C 1000 mg | botol | 25.000 | 32.000 | 40.000 | suplemen |
| ALK-001 | Masker Medis (box 50) | box | 25.000 | 35.000 | 45.000 | alat kesehatan |
| ALK-002 | Alkohol Swab (box 100) | box | 18.000 | 25.000 | 30.000 | alat kesehatan |
| HRB-001 | Jamu Kunyit Asam | sachet | 380 (biaya produksi) | 700 | 1.000 | hasil produksi pabrik |
| HRB-002 | Suplemen Kalsium | botol | dari BOM | 30.000 | 38.000 | hasil produksi, memakai kalsium karbonat |
| KAL-001 | Kalsium Karbonat (bahan baku) | kg | dari tambang | - | - | bahan baku, tidak dijual eceran |
| BHN-001 | Kunyit (bahan baku) | kg | 10.000 | - | - | bahan baku BOM HRB-001, kategori Bahan Baku, tidak dijual eceran |
| BHN-002 | Asam Jawa (bahan baku) | kg | 8.000 | - | - | bahan baku BOM HRB-001, kategori Bahan Baku, tidak dijual eceran |
| BHN-003 | Kemasan Sachet Jamu | sachet | 100 | - | - | bahan pengemas BOM HRB-001, 1 sachet kosong per sachet jamu, kategori Bahan Baku |
| RNT-001 | Sewa Kursi Roda | hari | - | 15.000 per hari | - | aset sewa, deposit Rp 100.000 per unit |
| MNU-001 | Teh Jahe Hangat | gelas | - | - | 12.000 | menu kafe |

**Input produk di:** `Client Master → Produk` (`/client-master/products`). Urutan yang benar:

1. Kategori di `Client Master → Kategori Produk` (`/client-master/product-categories`): Obat, Alat Kesehatan, Suplemen, Herbal, Bahan Baku, Jasa Sewa, Menu Kafe.
2. Satuan di `Client Master → Satuan Produk` (`/client-master/product-units`): strip, botol, box, sachet, kg, hari, gelas.
3. Produk di `Produk`: nama, kategori, merek, deskripsi, saluran penjualan, tanda **dapat dibeli**. Kode SKU, satuan, dan harga mengikuti isian SKU produk itu (cocokkan dengan layar; bisa juga lewat **Import Excel** di `/client-master/products/import`).
4. Harga jual berbeda per kanal (grosir 4.500, apotek 6.000) lewat `Client Master → Daftar Harga` (`/client-master/price-lists`): buat daftar harga `Grosir` dan `Apotek`, lalu isi harga per SKU.
5. Produk khusus: resep produksi di `Client Master → Resep Produk` (HRB-001, HRB-002), menu kafe di `Restoran → Menu`, aset sewa di `Sewa → Aset`.

**Persediaan awal tidak diinput.** Sengaja kosong; stok lahir dari Goods Receipt (`01` langkah 7).

### 3.3 Gudang

`WH-PST` (Pusat), `WH-BDG` (Apotek Bandung), `WH-SKB-RM` (bahan baku Sukabumi), `WH-SKB-FG` (barang jadi Sukabumi). Transfer antar
gudang wajib lewat **Transfer Stok**, bukan penyesuaian manual.

**Input gudang di:** `Client Master → Gudang` (`/client-master/warehouses`). Kolom: Name, Code (`WH-PST` dan seterusnya), Business unit, Type, alamat, telepon, koordinat, Status.
Gudang **butuh unit bisnis**, jadi buat dulu satu unit per cabang di `Client Master → Unit Bisnis` (`/client-master/business-units`). `WH-BDG` dibuat saat cabang aktif adalah Bandung.

### 3.4 Akun kunci

> **Daftar lengkap tipe akun dan akun (kode, tipe, saldo normal, dipakai modul mana) ada di [`00b`](./00b-tipe-akun-dan-akun-acuan.id.md).** Bagian ini hanya ringkasan nama. Kalau berbeda dengan `00b`, ikuti `00b`.

Kas Kecil, Bank Operasional, Piutang Usaha, Persediaan Barang Dagang, Persediaan Bahan Baku, Persediaan Barang Jadi, Aset Tetap, Akumulasi
Penyusutan, Utang Usaha, Utang PPN, PPN Masukan, Pendapatan Penjualan, Pendapatan Jasa, Harga Pokok Penjualan, Beban Gaji, Beban Listrik,
Beban Penyusutan, Modal Pemilik, Laba Ditahan, Laba/Rugi Pelepasan Aset, Laba/Rugi Selisih Kurs.

Saldo awal 1 Oktober 2026 (lewat fitur Saldo Awal): **Bank Operasional Rp 500.000.000** dan **Modal Pemilik Rp 500.000.000**. Tanpa
persediaan awal, supaya angka di file `01` bisa dihitung dari nol.

**Input akun di:** `Client Master → Chart of Account Type` (`/client-master/chart-of-account-type`) lalu `Client Master → Bagan Akun` (`/client-master/chart-of-accounts`).
Isi **sesuai [`00b`](./00b-tipe-akun-dan-akun-acuan.id.md)** (8 tipe, 40 akun), bukan template bawaan: template memakai kode yang bentrok dan template Kesehatan terlalu tipis. Klien baru memang mulai dengan COA kosong.
Kolom akun: Code, Name, Category, Effect, Normal balance, Report group.

**Input saldo awal (Bank Rp 500.000.000 dan Modal Rp 500.000.000):**

1. Tandai **satu akun ekuitas** (Modal Pemilik) sebagai **akun saldo awal** (opening balance equity) di `Bagan Akun`. **Tanpa ini saldo awal gagal dengan pesan kesalahan.**
2. Buat rekening bank di `Keuangan → Rekening Bank` (`/finance/bank-accounts`) untuk Bank Operasional.
3. Isi saldo awal lewat Chart of Accounts atau `Client Master → Chart of Accounts Balances` (`/client-master/chart-of-accounts-balances`), tanggal **1 Oktober 2026**.
4. Verifikasi di `Laporan → Neraca Saldo` (`/reports/trial-balance`): kedua sisi Rp 500.000.000.

## 4. Urutan kerja yang disarankan

0. File [`00a`](./00a-perjalanan-berlangganan-klien.id.md): **titik awal**, perjalanan berlangganan dari landing page sampai login pertama dan penagihan berkala.
1. File `02` (Platform Owner, Mulai Menggunakan, Pengaturan Akun): kedalaman per bab untuk provider, cabang, pengguna, peran.
2. File `03` (Konfigurasi Umum, Inti, Persetujuan): master data, template, alur persetujuan.
3. File `01` (alur terpadu) berjalan **mengikuti urutan langkahnya** dan memanggil file modul bila perlu rincian.
4. File modul `04` sampai `20` untuk kedalaman per bab, termasuk kasus Negatif dan izin.
5. File `98` (penutupan dan rekonsiliasi) terakhir, lalu `99` untuk memastikan tidak ada bab yang belum disentuh.

### 4.1 Urutan memasukkan data acuan (jangan dibalik, tiap langkah memakai langkah sebelumnya)

Dikerjakan oleh **Dr. Andika** (admin klien) setelah login. Untuk cabang selain Pusat, pindah cabang aktif dulu.

| # | Data | Menu dan URL | Bergantung pada |
| ---: | --- | --- | --- |
| 1 | Mata uang cabang | `Client Master → Mata Uang` (`/client-master/currencies`) | login |
| 2 | Pajak PPN 11% | `Client Master → Pajak` (`/client-master/taxes`) | - |
| 3 | Unit bisnis per cabang | `Client Master → Unit Bisnis` (`/client-master/business-units`) | - |
| 4 | Gudang (4 gudang) | `Client Master → Gudang` (`/client-master/warehouses`) | langkah 3 |
| 5 | Metode pembayaran (Tunai, Transfer, QRIS) dan tipe order | `Client Master → Metode Pembayaran` (`/client-master/payment-methods`), `Jenis Pesanan` (`/client-master/order-types`) | - |
| 6 | Jenis akun (8 tipe) dan Chart of Accounts (40 akun), **daftar di [`00b`](./00b-tipe-akun-dan-akun-acuan.id.md)** | `Client Master → Chart of Account Type`, `Bagan Akun` | langkah 3 |
| 7 | Tahun fiskal dan 12 periode | `Client Master → Tahun Fiskal`, `Periode Akuntansi` | - |
| 8 | Rekening bank, lalu saldo awal 1 Okt | `Keuangan → Rekening Bank`, `Chart of Accounts Balances` | langkah 6 dan 7 |
| 9 | Awalan nomor dokumen | `Client Master → Pengaturan Cabang` (`/client-master/branch-setup`) | - |
| 10 | Cabang lain, peran, pengguna | `Branch Manage`, `Peran`, `Pengguna` | langkah 1 sampai 8 untuk cabang baru |
| 10a | Departemen, lalu jabatan (jabatan mewajibkan departemen dan boleh memilih peran) | `HRM → Departemen` (`/hrm/departments`), `HRM → Jabatan` (`/hrm/positions`); tabel di bagian 2.1 | langkah 10 (peran dan cabang) |
| 11 | Kategori dan satuan produk | `Kategori Produk`, `Satuan Produk` | - |
| 12 | Produk, lalu daftar harga | `Produk`, `Daftar Harga` | langkah 11 |
| 13 | Pemasok dan pelanggan | `Client Master → Kontak` | langkah 1 |
| 14 | Alur persetujuan | `Client Master → Approval Workflow Configs` (`/client-master/approval-workflow-configs`) | langkah 10 (peran) |
| 15 | Pengaturan modul (Purchase Configs, Inventory Config, POS Configs, dst.) | menu `Konfigurasi` di tiap modul, dibahas di file `05` sampai `17` | langkah 1 sampai 13 |

## 5. Aturan membaca hasil

- **Positif**: jalur normal harus berhasil dan efek di modul lain harus terlihat. **Negatif**: harus ditolak dengan pesan jelas, bukan
  gagal diam-diam atau error server. **Netralisasi**: cara mengembalikan data ke keadaan semula bila diperlukan file berikutnya.
- Angka di file `01` adalah **acuan hitung**: bila hasil di layar berbeda, catat sebagai temuan dan jangan menyesuaikan angka acuannya.
  Angka yang bergantung pada konfigurasi cabang (pajak POS, mode jurnal, persetujuan) ditulis sebagai **hubungan** (mis. "Persediaan
  turun sebesar HPP"), bukan angka mutlak.
- Setiap kali sebuah baris menyebut "tombol nonaktif", yang diuji adalah **tombol terlihat tetapi nonaktif disertai alasan di tooltip**
  (aturan tampilan proyek), bukan tombol yang hilang.
- Pengujian dilakukan di **database uji**, bukan produksi. Untuk pembayaran online pakai kunci sandbox dan panduan
  `erpApiServices/docs/panduan-uji-kredensial-pembayaran.id.md`.

## 6. Batas cakupan

- Integrasi eksternal nyata (SMTP, WhatsApp, bank sungguhan) tidak diuji di sini; yang diuji adalah perilaku aplikasi saat integrasi
  belum diatur dan saat memakai mode sandbox.
- QRIS sandbox memakai kode tiruan; pembayaran disimulasikan dari dashboard penyedia, bukan dengan memindai.
- Fitur yang dikunci paket langganan diuji dua kali: dengan fitur aktif dan dengan fitur tidak termasuk paket (menu hilang dan 403).
