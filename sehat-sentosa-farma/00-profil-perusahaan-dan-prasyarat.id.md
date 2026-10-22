---
title: (PT Sehat Sentosa Farma) — 00. Profil Perusahaan, Master Data Acuan dan Prasyarat
category: sehat-sentosa-farma
description: Skenario perusahaan kesehatan terpadu (apotek, klinik dan laboratorium, distribusi obat, pabrik herbal, kafe, sewa alat medis, tambang kapur) yang dipakai semua file di suite ini. Memuat cabang, peran, data acuan, urutan kerja dan aturan membaca hasil.
visibility: internal
---

# 00. Profil Perusahaan, Master Data Acuan dan Prasyarat

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

**PT Sehat Sentosa Farma** (merek "Sentosa Farma"), grup usaha kesehatan, berstatus PKP, mata uang Rupiah, tahun fiskal Januari sampai
Desember 2026. Periode uji utama: **Oktober 2026**.

### 1.1 Satu kalimat profil di atas diisi di tiga tingkat yang berbeda

Kalimat profil itu bukan satu formulir. Aplikasi memisahkan data menjadi **tiga tingkat**, dan tiap atribut hidup di tingkat yang berbeda:

| Tingkat | Artinya | Siapa yang mengisi | Contoh di profil ini |
| --- | --- | --- | --- |
| **Perusahaan (provider)** | Entitas klien yang berlangganan. **Tidak ada halaman "profil perusahaan" yang bisa diedit klien.** Terbentuk sekali lewat pengajuan `/subscribe` yang disetujui owner | Calon klien saat mendaftar; owner saat menyetujui | Nama "PT Sehat Sentosa Farma", paket langganan, batas cabang dan pengguna |
| **Cabang** | Satu lokasi atau unit usaha di bawah perusahaan. Hampir semua pengaturan operasional melekat di sini | Klien (Dr. Rahmat) | Alamat, cabang utama, mata uang bawaan, tahun fiskal, pajak, gudang |
| **Data master milik cabang** | Isi yang dipakai transaksi: akun, produk, mitra, gudang, pengguna | Klien | Seluruh data acuan §3 |

### 1.2 Atribut profil dan tempat memasukkannya

| Atribut di profil | Tingkat | Diisi di (menu dan URL) | Diisi dengan | Catatan |
| --- | --- | --- | --- | --- |
| Nama perusahaan "PT Sehat Sentosa Farma" | Perusahaan | Formulir `/subscribe` (kolom Nama Perusahaan); owner melihatnya di `Core → Providers` (`/core/providers`) | `PT Sehat Sentosa Farma` | Sudah terisi lewat pengajuan. Klien tidak mengubahnya sendiri |
| Nama cabang pertama dan alamatnya | Cabang | Formulir `/subscribe` (cabang pertama); lanjutan di `Client Master → Branch Manage` (`/client-master/branch-manage`) | `Kantor Pusat & Distribusi Jakarta`, alamat, provinsi, kota, kecamatan, kelurahan, kode pos 5 digit | Koordinat bisa diisi lewat pencarian wilayah atau manual |
| Cabang lain (Bandung, Bekasi, Sukabumi, Kafe) | Cabang | `Client Master → Branch Manage` (`/client-master/branch-manage`) → **Add Branch** | Nama dan alamat tiap cabang (tabel di bawah) | Dibatasi **batas cabang paket**. Melebihi batas harus ditolak (`00a` S11) |
| Cabang utama (Pusat) | Cabang | `Branch Manage`, kolom **This branch is a main branch** | Aktif untuk Pusat | Cabang anak memakai **Reports to main branch**. Menentukan laporan gabungan |
| Pembukuan cabang digabung di pusat | Cabang | `Branch Manage`, kolom **Keep this branch's accounting in the main branch** | Biarkan mati untuk pengujian ini kecuali kasus khusus | Ini mode akuntansi terpusat; mengubah arah jurnal, jangan dinyalakan tanpa alasan |
| Mata uang Rupiah | Cabang | `Client Master → Currencies` (`/client-master/currencies`) | Pilih IDR, tandai sebagai mata uang yang dipakai cabang (badge **Used by branch**) | Dikerjakan **per cabang**. Kurs mata uang lain di `Client Master → Exchange Rates` |
| Tahun fiskal Januari sampai Desember 2026 | Cabang | `Client Master → Fiscal Year` (`/client-master/fiscal-year`) | Kode `FY2026`, nama, mulai `2026-01-01`, selesai `2026-12-31` | Wajib sebelum ada jurnal atau saldo awal |
| 12 periode akuntansi | Cabang | `Client Master → Accounting Period` (`/client-master/accounting-period`) | Pilih tahun fiskal, durasi bulanan, mulai Januari 2026 | Periode berjalan bisa otomatis (mengikuti tanggal) atau dikunci manual |
| Berstatus PKP dan PPN 11% | Cabang | `Client Master → Taxes` (`/client-master/taxes`) | Kode `PPN`, nama `PPN 11%`, tarif `11`, jenis pajak keluaran dan masukan | **Tidak ada kolom "status PKP" di aplikasi** (tidak ditemukan di kode maupun skema). Cukup buat pajak PPN 11% dan pakai di dokumen. Kalau PKP formal ingin diuji, catat sebagai celah |
| Merek "Sentosa Farma" di dokumen cetak | Cabang | `Client Master → PDF Layout Settings` (`/client-master/pdf-layout-settings`), kolom **Company name override** | `Sentosa Farma` (opsional), logo, catatan header dan footer | **Tidak ada kolom merek di profil perusahaan.** Merek hanya muncul di tata letak PDF |
| Periode uji Oktober 2026 | Data uji | Tidak ada isian. Itu tanggal transaksi saat membuat dokumen | Tanggal dokumen di Oktober 2026 | Pastikan periode Oktober berstatus terbuka |

> **Kalau sebuah atribut tidak ketemu di layar:** kemungkinan besar memang tidak ada. Jangan dicari lama-lama; catat di tabel temuan README sebagai **Celah** dan lanjutkan.

### 1.3 Cabang yang dibuat

| Cabang | Fungsi | Modul yang dominan |
| --- | --- | --- |
| **Kantor Pusat & Distribusi Jakarta** (cabang utama) | gudang obat dan alat kesehatan, penjualan grosir ke klinik dan apotek mitra, pembukuan pusat | Pembelian, Persediaan, Penjualan, Kanvasing, Akuntansi, Keuangan, Aset Tetap |
| **Apotek Sentosa Bandung** | apotek retail, resep, QRIS | POS, Persediaan, Pembayaran online |
| **Klinik Pratama & Laboratorium Bekasi** | layanan medis, kasir, tenaga kesehatan | SDM, POS (kasir jasa), Proyek (akreditasi) |
| **Pabrik Herbal Sukabumi** | produksi jamu dan suplemen, bahan baku kalsium karbonat | Manufaktur, Pertambangan |
| **Kafe Sehat (lobi klinik)** | kafe pasien dan keluarga | Restoran |
| **Layanan Sewa Alat Medis** (dikelola Pusat) | kursi roda, tabung oksigen, tempat tidur pasien | Sewa |

Cabang Pusat adalah **cabang utama** (laporan bisa digabung dengan cabang anak). Provider ini **lahir dari alur berlangganan** ([`00a`](./00a-perjalanan-berlangganan-klien.id.md)): calon klien menemukan aplikasi di landing page, mengirim formulir minat, owner membuat Client Onboarding dan memprovisi, klien membayar tagihan dan login pertama. Data cabang, pengguna dan master di bawah ini dibuat **klien sendiri setelah itu**, bukan diisi lebih dulu oleh admin atau seeder.

## 2. Peran dan pengguna uji

| Peran | Contoh pengguna | Ruang lingkup |
| --- | --- | --- |
| Direktur (admin klien) | Dr. Rahmat Hidayat | semua modul, persetujuan tingkat akhir |
| Manajer Keuangan | Sari Wulandari | Akuntansi, Keuangan, Aset Tetap, laporan, persetujuan biaya dan jurnal |
| Staf Pembelian | Bima Prakoso | Pembelian |
| Kepala Gudang | Hendra Saputra | Persediaan, penerimaan barang, transfer, stok opname |
| Apoteker Penanggung Jawab | Apt. Lestari Dewi | POS apotek, obat resep, persetujuan retur |
| Kasir Apotek | Rina Marlina | POS (hanya sesi kasirnya sendiri) |
| Sales Lapangan | Dewi Anggraini | Kanvasing |
| Kepala Produksi | Joko Santoso | Manufaktur |
| Staf HR | Maya Puspita | SDM, rekrutmen, payroll |
| Pemilik Platform | (akun owner) | Platform Owner: paket, klien, penangguhan |

**Cara membuatnya:**

| Langkah | Menu dan URL | Isi |
| --- | --- | --- |
| 1. Buat peran | `Client Master → Roles` (`/client-master/roles`) | Nama peran (mis. `Kasir Apotek`), deskripsi, status aktif; lalu atur izinnya. Peran klien **hanya bisa memberi izin yang dimiliki pembuatnya** |
| 2. Buat pengguna | `Client Master → Users` (`/client-master/users`) | Nama, email, kata sandi dan konfirmasinya, status aktif, PIN override manajer (untuk kasir yang butuh persetujuan atasan) |
| 3. Hubungkan pengguna ke cabang | `Client Master → Branch Manage` (`/client-master/branch-manage`), pilih cabang → **Assign user** | Pilih pengguna, tandai aktif di cabang itu |
| 4. Data karyawan (untuk yang digaji) | `HRM → Employees` (`/hrm/employees`) | Dikerjakan di file `16`, bukan di sini |

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

**Input di:** `Client Master → Contacts` (`/client-master/contacts`). Satu halaman untuk pemasok dan pelanggan; dibedakan lewat kolom **Type**.

| Yang diisi | Kolom di form | Contoh |
| --- | --- | --- |
| Nama | Name | `PT Bintang Farmasi Utama` |
| Jenis | Type | Pemasok untuk SUP-xx, pelanggan untuk CUS-xx |
| Telepon dan email | Phone, Email | bebas (telepon hanya angka) |
| Termin bayar | Payment term days | `14` untuk SUP-01 dan CUS-01, `30` untuk SUP-02 |
| Batas kredit | Credit limit | `20000000` untuk CUS-01, `10000000` untuk CUS-02 |
| Pelanggan POS bawaan | Walking customer (POS default) | aktif hanya untuk CUS-03 Pasien Umum |
| Mata uang | Currency | IDR |

Alamat dan rekening bank mitra diisi di halaman terpisah: `Client Master → Contact Addresses` (`/client-master/contact-addresses`) dan `Contact Bank Accounts` (`/client-master/contact-bank-accounts`).
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
| RNT-001 | Sewa Kursi Roda | hari | - | 15.000 per hari | - | aset sewa, deposit Rp 100.000 per unit |
| MNU-001 | Teh Jahe Hangat | gelas | - | - | 12.000 | menu kafe |

**Input produk di:** `Client Master → Products` (`/client-master/products`). Urutan yang benar:

1. Kategori di `Client Master → Product Categories` (`/client-master/product-categories`): Obat, Alat Kesehatan, Suplemen, Herbal, Bahan Baku, Jasa Sewa, Menu Kafe.
2. Satuan di `Client Master → Product Units` (`/client-master/product-units`): strip, botol, box, sachet, kg, hari, gelas.
3. Produk di `Products`: nama, kategori, merek, deskripsi, saluran penjualan, tanda **dapat dibeli**. Kode SKU, satuan, dan harga mengikuti isian SKU produk itu (cocokkan dengan layar; bisa juga lewat **Import Excel** di `/client-master/products/import`).
4. Harga jual berbeda per kanal (grosir 4.500, apotek 6.000) lewat `Client Master → Price Lists` (`/client-master/price-lists`): buat daftar harga `Grosir` dan `Apotek`, lalu isi harga per SKU.
5. Produk khusus: resep produksi di `Client Master → Product Recipes` (HRB-001, HRB-002), menu kafe di `Restaurant → Menu`, aset sewa di `Rental → Assets`.

**Persediaan awal tidak diinput.** Sengaja kosong; stok lahir dari Goods Receipt (`01` langkah 7).

### 3.3 Gudang

`WH-PST` (Pusat), `WH-BDG` (Apotek Bandung), `WH-SKB-RM` (bahan baku Sukabumi), `WH-SKB-FG` (barang jadi Sukabumi). Transfer antar
gudang wajib lewat **Transfer Stok**, bukan penyesuaian manual.

**Input gudang di:** `Client Master → Warehouses` (`/client-master/warehouses`). Kolom: Name, Code (`WH-PST` dan seterusnya), Business unit, Type, alamat, telepon, koordinat, Status.
Gudang **butuh unit bisnis**, jadi buat dulu satu unit per cabang di `Client Master → Business Units` (`/client-master/business-units`). `WH-BDG` dibuat saat cabang aktif adalah Bandung.

### 3.4 Akun kunci

> **Daftar lengkap tipe akun dan akun (kode, tipe, saldo normal, dipakai modul mana) ada di [`00b`](./00b-tipe-akun-dan-akun-acuan.id.md).** Bagian ini hanya ringkasan nama. Kalau berbeda dengan `00b`, ikuti `00b`.

Kas Kecil, Bank Operasional, Piutang Usaha, Persediaan Barang Dagang, Persediaan Bahan Baku, Persediaan Barang Jadi, Aset Tetap, Akumulasi
Penyusutan, Utang Usaha, Utang PPN, PPN Masukan, Pendapatan Penjualan, Pendapatan Jasa, Harga Pokok Penjualan, Beban Gaji, Beban Listrik,
Beban Penyusutan, Modal Pemilik, Laba Ditahan, Laba/Rugi Pelepasan Aset, Laba/Rugi Selisih Kurs.

Saldo awal 1 Oktober 2026 (lewat fitur Saldo Awal): **Bank Operasional Rp 500.000.000** dan **Modal Pemilik Rp 500.000.000**. Tanpa
persediaan awal, supaya angka di file `01` bisa dihitung dari nol.

**Input akun di:** `Client Master → Chart of Account Type` (`/client-master/chart-of-account-type`) lalu `Client Master → Chart of Accounts` (`/client-master/chart-of-accounts`).
Isi **sesuai [`00b`](./00b-tipe-akun-dan-akun-acuan.id.md)** (8 tipe, 40 akun), bukan template bawaan: template memakai kode yang bentrok dan template Kesehatan terlalu tipis. Klien baru memang mulai dengan COA kosong.
Kolom akun: Code, Name, Category, Effect, Normal balance, Report group.

**Input saldo awal (Bank Rp 500.000.000 dan Modal Rp 500.000.000):**

1. Tandai **satu akun ekuitas** (Modal Pemilik) sebagai **akun saldo awal** (opening balance equity) di `Chart of Accounts`. **Tanpa ini saldo awal gagal dengan pesan kesalahan.**
2. Buat rekening bank di `Finance → Bank Accounts` (`/finance/bank-accounts`) untuk Bank Operasional.
3. Isi saldo awal lewat Chart of Accounts atau `Client Master → Chart of Accounts Balances` (`/client-master/chart-of-accounts-balances`), tanggal **1 Oktober 2026**.
4. Verifikasi di `Reports → Trial Balance` (`/reports/trial-balance`): kedua sisi Rp 500.000.000.

## 4. Urutan kerja yang disarankan

0. File [`00a`](./00a-perjalanan-berlangganan-klien.id.md): **titik awal**, perjalanan berlangganan dari landing page sampai login pertama dan penagihan berkala.
1. File `02` (Platform Owner, Mulai Menggunakan, Pengaturan Akun): kedalaman per bab untuk provider, cabang, pengguna, peran.
2. File `03` (Konfigurasi Umum, Inti, Persetujuan): master data, template, alur persetujuan.
3. File `01` (alur terpadu) berjalan **mengikuti urutan langkahnya** dan memanggil file modul bila perlu rincian.
4. File modul `04` sampai `20` untuk kedalaman per bab, termasuk kasus Negatif dan izin.
5. File `98` (penutupan dan rekonsiliasi) terakhir, lalu `99` untuk memastikan tidak ada bab yang belum disentuh.

### 4.1 Urutan memasukkan data acuan (jangan dibalik, tiap langkah memakai langkah sebelumnya)

Dikerjakan oleh **Dr. Rahmat** (admin klien) setelah login. Untuk cabang selain Pusat, pindah cabang aktif dulu.

| # | Data | Menu dan URL | Bergantung pada |
| ---: | --- | --- | --- |
| 1 | Mata uang cabang | `Client Master → Currencies` (`/client-master/currencies`) | login |
| 2 | Pajak PPN 11% | `Client Master → Taxes` (`/client-master/taxes`) | - |
| 3 | Unit bisnis per cabang | `Client Master → Business Units` (`/client-master/business-units`) | - |
| 4 | Gudang (4 gudang) | `Client Master → Warehouses` (`/client-master/warehouses`) | langkah 3 |
| 5 | Metode pembayaran (Tunai, Transfer, QRIS) dan tipe order | `Client Master → Payment Methods` (`/client-master/payment-methods`), `Order Types` (`/client-master/order-types`) | - |
| 6 | Jenis akun (8 tipe) dan Chart of Accounts (40 akun), **daftar di [`00b`](./00b-tipe-akun-dan-akun-acuan.id.md)** | `Client Master → Chart of Account Type`, `Chart of Accounts` | langkah 3 |
| 7 | Tahun fiskal dan 12 periode | `Client Master → Fiscal Year`, `Accounting Period` | - |
| 8 | Rekening bank, lalu saldo awal 1 Okt | `Finance → Bank Accounts`, `Chart of Accounts Balances` | langkah 6 dan 7 |
| 9 | Awalan nomor dokumen | `Client Master → Branch Setup` (`/client-master/branch-setup`) | - |
| 10 | Cabang lain, peran, pengguna | `Branch Manage`, `Roles`, `Users` | langkah 1 sampai 8 untuk cabang baru |
| 11 | Kategori dan satuan produk | `Product Categories`, `Product Units` | - |
| 12 | Produk, lalu daftar harga | `Products`, `Price Lists` | langkah 11 |
| 13 | Pemasok dan pelanggan | `Client Master → Contacts` | langkah 1 |
| 14 | Alur persetujuan | `Client Master → Approval Workflow Configs` (`/client-master/approval-workflow-configs`) | langkah 10 (peran) |
| 15 | Pengaturan modul (Purchase Configs, Inventory Config, POS Configs, dst.) | menu `Config` di tiap modul, dibahas di file `05` sampai `17` | langkah 1 sampai 13 |

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
