# Accounting Business Case Testing Guide

## Panduan Pengujian Module Accounting Berdasarkan Skenario Bisnis

### Tujuan

Dokumen ini digunakan untuk menguji module Accounting dengan pendekatan bisnis murni.

Jangan mulai dengan pertanyaan:

> “Apakah jurnal ini berhasil dibuat?”

Mulailah dengan:

> “Jika saya adalah perusahaan ini, apakah seluruh kejadian keuangan saya dapat dicatat, dikendalikan, dan dijelaskan dengan benar?”

Accounting bukan hanya tempat mencatat uang masuk dan keluar.

Accounting harus mampu menjelaskan:

* Dari mana uang berasal?
* Untuk apa uang digunakan?
* Apa yang menjadi hak perusahaan?
* Apa yang menjadi kewajiban perusahaan?
* Berapa keuntungan perusahaan?
* Apa yang dimiliki perusahaan?
* Apa yang masih harus dibayar?
* Apa yang masih harus diterima?
* Bagaimana kondisi keuangan perusahaan?
* Bagaimana perubahan tersebut terjadi?

---

# CARA MENGGUNAKAN PANDUAN INI

Gunakan beberapa perusahaan dengan karakter berbeda.

Jangan menggunakan satu pola perusahaan saja.

Untuk setiap case:

**Kenali bisnis → Identifikasi transaksi → Catat kejadian → Tentukan kewajiban/hak → Tutup periode → Evaluasi laporan**

Jangan memikirkan database, API, jurnal otomatis, atau istilah teknis aplikasi selama tahap pertama.

Berpikir sebagai:

> Owner → Finance → Accounting → Management

---

# CASE 1 — RESTORAN

## Profil Perusahaan

Nama: **Saji Rasa**

Jenis usaha: Restoran

Jumlah outlet: 1

Pemilik: 1 orang

Karyawan: 22 orang

Aktivitas utama:

* Menjual makanan
* Membeli bahan baku
* Membayar karyawan
* Membayar listrik dan air
* Membayar sewa
* Membeli peralatan restoran

---

# Skenario 1 — Modal Awal

Pemilik memasukkan uang sebesar:

**Rp200.000.000**

ke dalam bisnis untuk memulai usaha.

### Pertanyaan

Apakah perusahaan mengetahui:

* berapa modal yang diberikan pemilik?
* berapa uang yang masuk?
* berapa nilai modal perusahaan?

Setelah transaksi ini, kondisi keuangan perusahaan harus dapat dijelaskan.

---

# Skenario 2 — Membeli Peralatan

Restoran membeli:

* Kompor: Rp8.000.000
* Freezer: Rp12.000.000
* Meja dan kursi: Rp15.000.000

Pembayaran dilakukan langsung.

### Pertanyaan

Apakah semua pembelian tersebut dianggap sebagai pengeluaran biasa?

Atau ada sebagian yang memiliki manfaat untuk jangka panjang?

---

# Skenario 3 — Pembelian Bahan Baku

Restoran membeli bahan makanan senilai:

**Rp5.000.000**

Pembayaran langsung dilakukan.

### Pertanyaan

Apa yang sebenarnya terjadi?

Perusahaan mendapatkan sesuatu yang akan digunakan untuk menghasilkan penjualan.

Jangan hanya berpikir:

> “Uang keluar Rp5 juta.”

Tanyakan:

> “Apa yang sekarang dimiliki perusahaan?”

---

# Skenario 4 — Penjualan Harian

Dalam satu hari:

Penjualan makanan:

**Rp7.500.000**

Pembayaran:

* Cash: Rp2.000.000
* Bank: Rp3.500.000
* QR/payment: Rp2.000.000

### Pertanyaan

Apakah perusahaan dapat mengetahui:

* total penjualan?
* sumber pembayaran?
* uang yang benar-benar diterima?
* transaksi yang belum masuk ke rekening?
* biaya yang dikenakan payment provider?

---

# Skenario 5 — Biaya Payment Provider

Dari transaksi payment provider sebesar Rp2.000.000, perusahaan menerima:

**Rp1.960.000**

Terdapat biaya:

**Rp40.000**

### Pertanyaan

Apakah perusahaan dapat menjelaskan perbedaan Rp40.000 tersebut?

Jangan sampai laporan hanya menunjukkan:

> Penjualan Rp1.960.000

Padahal pelanggan sebenarnya membayar:

> Rp2.000.000

---

# Skenario 6 — Pembelian Secara Kredit

Supplier mengirim bahan baku:

**Rp10.000.000**

Tetapi pembayaran dilakukan 30 hari kemudian.

### Pertanyaan

Apakah perusahaan sudah memiliki kewajiban kepada supplier?

Bagaimana perusahaan mengetahui:

> “Bulan depan kita harus membayar supplier Rp10 juta?”

---

# Skenario 7 — Membayar Supplier

30 hari kemudian perusahaan membayar Rp10.000.000.

### Pertanyaan

Setelah pembayaran:

* apakah kewajiban hilang?
* apakah pengeluaran uang tercatat?
* apakah perusahaan masih menganggap hutang tersebut belum dibayar?

---

# CASE 2 — PERUSAHAAN DISTRIBUSI

## Profil

Nama: **Maju Distribusi**

Jumlah karyawan: 75

Aktivitas:

* Membeli barang
* Menyimpan inventory
* Menjual barang
* Memberikan kredit kepada customer
* Membayar supplier
* Menerima pembayaran customer

---

# Skenario 1 — Membeli Inventory Kredit

Perusahaan membeli barang:

**Rp100.000.000**

Supplier memberikan tempo 30 hari.

### Pertanyaan

Apa yang berubah?

Perusahaan:

* memiliki barang
* memiliki kewajiban

Tetapi:

* belum mengeluarkan uang

Pastikan laporan mampu menjelaskan kondisi tersebut.

---

# Skenario 2 — Menjual Barang Secara Kredit

Perusahaan menjual barang senilai:

**Rp30.000.000**

Customer membayar bulan depan.

### Pertanyaan

Apakah perusahaan sudah menghasilkan penjualan?

Apakah perusahaan sudah menerima uang?

Apakah kedua hal tersebut harus dianggap sama?

---

# Skenario 3 — Customer Membayar

Customer kemudian membayar Rp30 juta.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

> “Customer mana yang masih memiliki kewajiban?”

dan:

> “Customer mana yang sudah melunasi?”

---

# Skenario 4 — Customer Tidak Membayar

Salah satu customer memiliki tagihan:

**Rp20.000.000**

Sudah jatuh tempo selama 90 hari.

### Pertanyaan

Bagaimana management mengetahui bahwa uang tersebut belum diterima?

Apakah perusahaan dapat melihat umur tagihan?

---

# CASE 3 — PERUSAHAAN JASA

## Profil

Nama: **Nusantara Consulting**

Bisnis:

Memberikan jasa konsultasi kepada perusahaan lain.

Tidak memiliki inventory barang.

Jumlah karyawan: 30.

---

# Skenario 1 — Kontrak Jasa

Customer menyetujui kontrak:

**Rp120.000.000**

untuk jasa selama 12 bulan.

Customer membayar seluruhnya di awal.

### Pertanyaan

Apakah perusahaan langsung menganggap seluruh Rp120 juta sebagai pendapatan?

Atau ada bagian yang berkaitan dengan periode mendatang?

---

# Skenario 2 — Pembayaran Gaji

Perusahaan membayar gaji:

**Rp80.000.000**

setiap bulan.

Tetapi ada beberapa komponen:

* gaji pokok
* tunjangan
* potongan
* kewajiban perusahaan

### Pertanyaan

Apakah Accounting dapat menjelaskan total biaya tenaga kerja?

Apakah uang yang keluar selalu sama dengan biaya yang menjadi beban perusahaan?

---

# Skenario 3 — Biaya Dibayar di Muka

Perusahaan membayar:

**Rp12.000.000**

untuk software subscription selama 12 bulan.

Pembayaran dilakukan sekaligus.

### Pertanyaan

Apakah seluruh Rp12 juta merupakan biaya bulan pertama?

Atau manfaatnya digunakan selama 12 bulan?

---

# CASE 4 — PERUSAHAAN DENGAN FIXED ASSET

## Profil

Nama: **Manufacture Jaya**

Perusahaan memiliki:

* Mesin produksi
* Kendaraan
* Gedung
* Komputer
* Peralatan kantor

---

# Skenario 1 — Membeli Mesin

Perusahaan membeli mesin:

**Rp240.000.000**

Mesin diperkirakan digunakan selama beberapa tahun.

### Pertanyaan

Apakah seluruh Rp240 juta langsung menjadi biaya?

Atau perusahaan memiliki aset yang digunakan untuk menghasilkan manfaat selama beberapa tahun?

---

# Skenario 2 — Penyusutan

Mesin digunakan selama bertahun-tahun.

Nilainya secara akuntansi tidak tetap sama selama masa penggunaannya.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

* nilai awal aset?
* berapa nilai yang telah dialokasikan?
* nilai aset saat ini?
* kapan aset mulai digunakan?
* kapan masa penggunaannya berakhir?

---

# Skenario 3 — Aset Rusak

Mesin mengalami kerusakan berat dan tidak dapat digunakan lagi.

### Pertanyaan

Bagaimana perusahaan memperlakukan aset tersebut?

Apakah aset masih dianggap aktif?

Apakah perusahaan masih harus melihat nilainya sebagai bagian dari aset?

---

# Skenario 4 — Menjual Aset

Perusahaan menjual kendaraan yang sebelumnya dimiliki.

Harga jual:

**Rp80.000.000**

### Pertanyaan

Apakah perusahaan hanya mencatat:

> “Uang masuk Rp80 juta.”

Atau perusahaan juga perlu membandingkan harga jual dengan nilai aset tersebut?

---

# CASE 5 — PERUSAHAAN MULTI OUTLET

## Profil

Nama: **Nusantara Hospitality Group**

Memiliki:

* Restaurant A
* Restaurant B
* Restaurant C
* Hotel
* Head Office

Management ingin mengetahui performa masing-masing unit.

---

# Skenario 1 — Pendapatan Berbeda

Restaurant A menghasilkan:

Rp500 juta/bulan

Restaurant B:

Rp300 juta/bulan

Restaurant C:

Rp700 juta/bulan

### Pertanyaan

Management ingin mengetahui:

> “Outlet mana yang paling menguntungkan?”

Apakah sistem mampu memberikan informasi yang cukup untuk menjawabnya?

---

# Skenario 2 — Biaya Bersama

Head Office membayar:

**Rp30.000.000**

untuk software yang digunakan semua outlet.

### Pertanyaan

Bagaimana management mengetahui biaya tersebut berkaitan dengan siapa?

Apakah biaya tersebut hanya milik Head Office?

Atau perlu dialokasikan?

---

# Skenario 3 — Transfer Antar Unit

Restaurant A membeli bahan dari Restaurant B.

Nilai:

**Rp5.000.000**

### Pertanyaan

Bagaimana transaksi antar unit tersebut dipahami?

Apakah perusahaan melihatnya sebagai transaksi eksternal?

Atau sebagai perpindahan antar bagian dari satu kelompok bisnis?

---

# CASE 6 — PAJAK

## Profil

Perusahaan sudah memiliki kewajiban perpajakan.

Selama operasional:

* melakukan penjualan
* membeli barang/jasa
* membayar karyawan
* membayar supplier

---

# Skenario 1 — Pajak Penjualan

Perusahaan melakukan transaksi yang memiliki komponen pajak.

### Pertanyaan

Apakah perusahaan dapat membedakan:

* nilai transaksi
* pajak
* total pembayaran?

---

# Skenario 2 — Pajak Belum Dibayar

Pajak sudah menjadi kewajiban perusahaan tetapi belum dibayarkan.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

> “Berapa kewajiban pajak yang masih harus dibayar?”

---

# Skenario 3 — Pembayaran Pajak

Perusahaan kemudian membayar kewajiban pajak tersebut.

### Pertanyaan

Setelah pembayaran:

* apakah kewajiban berkurang?
* apakah saldo kas berkurang?
* apakah histori pembayaran tetap dapat dilacak?

---

# CASE 7 — BANK & CASH

## Skenario 1 — Banyak Rekening

Perusahaan memiliki:

* Cash
* Bank BCA
* Bank Mandiri
* E-wallet
* Payment Provider

### Pertanyaan

Management ingin mengetahui:

> “Berapa uang perusahaan yang tersedia sekarang?”

Tetapi uang tersebar di berbagai tempat.

Apakah informasi tersebut dapat dilihat dengan jelas?

---

# Skenario 2 — Selisih Rekening

Menurut catatan perusahaan:

Saldo Bank BCA:

**Rp100.000.000**

Menurut rekening bank:

**Rp98.500.000**

### Pertanyaan

Apa yang harus dilakukan?

Apakah Accounting dapat menemukan penyebab perbedaan?

---

# Skenario 3 — Pengeluaran Kecil

Selama satu minggu terdapat banyak pengeluaran:

* Parkir
* ATK
* Transportasi
* Konsumsi
* Biaya kecil lainnya

### Pertanyaan

Bagaimana perusahaan memastikan semua pengeluaran tersebut tetap dapat dipertanggungjawabkan?

---

# CASE 8 — PERIOD END / TUTUP BULAN

Ini salah satu testing paling penting.

## Kondisi

Tanggal 31 Januari.

Perusahaan ingin menutup bulan Januari.

Tetapi masih terdapat:

* tagihan supplier yang belum dibayar
* customer belum membayar
* gaji belum dibayar
* biaya listrik belum diterima tagihannya
* aset masih digunakan
* pembayaran di muka
* pajak belum dibayar

### Pertanyaan

Apakah perusahaan dapat menghasilkan gambaran keuangan Januari yang masuk akal?

Jangan hanya bertanya:

> “Apakah semua transaksi sudah masuk?”

Tanyakan:

> “Apakah Januari benar-benar menggambarkan kondisi ekonomi perusahaan pada bulan tersebut?”

---

# CASE 9 — KOREKSI KESALAHAN

## Skenario

Accounting salah mencatat biaya:

Rp10.000.000

seharusnya:

Rp1.000.000.

Kesalahan ditemukan setelah beberapa hari.

### Pertanyaan

Bagaimana perusahaan memperbaiki kesalahan?

Apakah:

* catatan lama hilang?
* histori perubahan tetap diketahui?
* nilai akhir menjadi benar?
* laporan sebelumnya dapat dipahami?

---

# CASE 10 — PEMILIK MENGAMBIL UANG

Pemilik mengambil:

**Rp20.000.000**

dari rekening perusahaan untuk keperluan pribadi.

### Pertanyaan

Apakah ini merupakan biaya operasional perusahaan?

Atau merupakan transaksi antara perusahaan dengan pemilik?

Bagaimana management dapat membedakannya?

---

# TESTING UTAMA — ACCOUNTING LIFECYCLE

Setelah seluruh case selesai, lakukan satu perjalanan lengkap.

Bayangkan sebuah perusahaan baru berdiri.

Ikuti:

**Pemilik memberikan modal**

↓

**Perusahaan membeli aset**

↓

**Perusahaan membeli barang**

↓

**Perusahaan memiliki hutang**

↓

**Perusahaan menjual**

↓

**Customer memiliki piutang**

↓

**Customer membayar**

↓

**Perusahaan membayar supplier**

↓

**Perusahaan membayar karyawan**

↓

**Perusahaan membayar biaya operasional**

↓

**Perusahaan memiliki pajak**

↓

**Perusahaan menggunakan aset**

↓

**Perusahaan melakukan penyusutan**

↓

**Akhir bulan**

↓

**Koreksi jika ada kesalahan**

↓

**Tutup periode**

↓

**Management membaca laporan**

---

# TESTING UTAMA — DARI TRANSAKSI MENJADI CERITA

Untuk setiap transaksi, tanyakan tiga hal.

## 1. WHAT?

Apa yang sebenarnya terjadi?

Contoh:

> Perusahaan membeli mesin Rp240 juta.

## 2. WHAT CHANGED?

Apa yang berubah dalam kondisi perusahaan?

Contoh:

> Uang berkurang, aset bertambah.

## 3. WHAT DOES MANAGEMENT NEED TO KNOW?

Apa informasi yang nantinya dibutuhkan management?

Contoh:

> Berapa nilai aset perusahaan saat ini?

Jangan berhenti pada:

> “Jurnalnya benar.”

Pastikan:

> “Cerita keuangan perusahaan tetap benar.”

---

# TESTING LAPORAN

Jangan hanya menguji apakah laporan muncul.

Gunakan pertanyaan bisnis.

## Management bertanya:

> “Berapa uang perusahaan sekarang?”

↓

Apakah dapat dijawab?

---

> “Berapa customer yang masih berhutang kepada kita?”

↓

Apakah dapat dijawab?

---

> “Berapa yang harus kita bayar kepada supplier?”

↓

Apakah dapat dijawab?

---

> “Berapa keuntungan bulan ini?”

↓

Apakah dapat dijawab?

---

> “Apa saja yang kita miliki?”

↓

Apakah dapat dijawab?

---

> “Berapa kewajiban perusahaan?”

↓

Apakah dapat dijawab?

---

> “Outlet mana yang paling menguntungkan?”

↓

Apakah dapat dijawab?

---

> “Kenapa keuntungan bulan ini turun?”

↓

Apakah data cukup untuk menjelaskan?

---

# TESTING EXCEPTION

Setelah happy path selesai, sengaja buat masalah.

### Customer membayar sebagian

Tagihan Rp10 juta.

Customer hanya membayar Rp6 juta.

Apa yang tersisa?

---

### Supplier dibayar sebagian

Hutang Rp20 juta.

Dibayar Rp12 juta.

Apa yang tersisa?

---

### Transaksi dibatalkan

Penjualan sudah terjadi tetapi kemudian dibatalkan.

Bagaimana kondisi keuangannya?

---

### Refund

Customer menerima pengembalian uang.

Bagaimana perusahaan memahami transaksi tersebut?

---

### Salah bayar

Perusahaan membayar supplier dua kali.

Apa yang terjadi?

---

### Pembayaran terlambat

Customer terlambat membayar 90 hari.

Apa yang harus diketahui management?

---

### Biaya terlambat diketahui

Tagihan listrik Januari baru diterima Februari.

Periode mana yang seharusnya mencerminkan biaya tersebut?

---

### Aset dijual

Aset yang masih memiliki nilai kemudian dijual.

Apa yang terjadi pada catatan perusahaan?

---

### Aset rusak

Aset tidak lagi memberikan manfaat.

Bagaimana perusahaan memperlakukannya?

---

# TESTING MULTI-CURRENCY

Jika suatu hari perusahaan melakukan transaksi dalam mata uang berbeda:

Perusahaan membeli jasa:

**USD 1.000**

### Pertanyaan

Bagaimana perusahaan memahami nilai transaksi tersebut dalam mata uang perusahaan?

Bagaimana jika nilai tukar berubah?

Tidak perlu langsung membangun fitur ini.

Yang diuji terlebih dahulu adalah:

> “Apakah pola bisnis ini mungkin terjadi dan apakah konsep accounting kita mampu menampungnya?”

---

# TESTING MANAGEMENT VIEW

Sekarang berhenti menjadi Accounting.

Anggap Anda adalah Owner.

Anda membuka laporan dan bertanya:

### Profit

> “Kita untung atau rugi?”

### Cash

> “Uang kita sebenarnya ada berapa?”

### Receivable

> “Siapa yang belum bayar?”

### Payable

> “Kita harus bayar siapa?”

### Asset

> “Apa saja yang perusahaan miliki?”

### Liability

> “Apa kewajiban perusahaan?”

### Expense

> “Biaya terbesar kita apa?”

### Business Unit

> “Outlet mana yang bagus?”

### Trend

> “Kenapa bulan ini lebih buruk daripada bulan lalu?”

Jika pertanyaan-pertanyaan tersebut sulit dijawab, cari tahu apakah masalahnya:

* data tidak tersedia
* pencatatan tidak lengkap
* struktur bisnis belum cukup fleksibel
* proses bisnis belum didukung
* atau memang laporan belum tersedia

---

# TESTING PERIOD COMPARISON

Jangan hanya melihat satu bulan.

Bandingkan:

**Januari**

vs

**Februari**

vs

**Maret**

Kemudian tanyakan:

> Apa yang berubah?

> Kenapa berubah?

> Apakah perubahan tersebut berasal dari penjualan?

> Biaya?

> Piutang?

> Hutang?

> Aset?

> Faktor lain?

Accounting yang baik bukan hanya memberi angka.

Ia membantu perusahaan **memahami perubahan angka tersebut.**

---

# FORMAT CATATAN TESTING

Gunakan format berikut untuk setiap case:

**Business Case**

Apa yang terjadi?

**Expected Business Result**

Apa yang seharusnya diketahui atau terjadi dalam bisnis?

**Actual Result**

Apa yang terjadi ketika case dijalankan?

**Gap**

Apa yang belum dapat direpresentasikan?

**Business Impact**

Apa dampaknya bagi perusahaan?

**Priority**

* Critical
* High
* Medium
* Low

**Decision**

* Perlu diperbaiki
* Perlu konfigurasi
* Dapat diterima
* Membutuhkan konsep baru

---

# HAL YANG PALING PERLU DIWASPADAI

Jangan membangun Accounting hanya berdasarkan:

> “Begini cara perusahaan saya bekerja.”

Accounting memiliki banyak pola bisnis yang berbeda.

Perusahaan dagang berbeda dengan perusahaan jasa.

Restoran berbeda dengan manufaktur.

Single outlet berbeda dengan multi outlet.

Perusahaan kecil berbeda dengan perusahaan dengan banyak unit bisnis.

---

# URUTAN TESTING YANG DISARANKAN

Mulai dari:

**1. Restaurant**

↓

**2. Distributor**

↓

**3. Service Company**

↓

**4. Fixed Asset Company**

↓

**5. Multi Outlet / Multi Business Unit**

↓

**6. Tax**

↓

**7. Bank & Cash**

↓

**8. Period End**

↓

**9. Correction**

↓

**10. Exception Cases**

↓

**11. Management Questions**

↓

**12. Period Comparison**

↓

**13. Catat Gap**

↓

**14. Tentukan apakah Gap merupakan Bug, Keterbatasan, Konfigurasi, atau Kebutuhan Bisnis Baru**

---

# PRINSIP UTAMA ACCOUNTING TESTING

Jangan mengejar:

> “Semua transaksi bisa dibuat.”

Kejar:

> **“Kondisi keuangan perusahaan selalu dapat dijelaskan dengan benar.”**

Setiap angka harus memiliki cerita.

Jika kas berubah, harus jelas kenapa.

Jika hutang muncul, harus jelas dari mana.

Jika piutang bertambah, harus jelas berasal dari transaksi apa.

Jika aset bertambah, harus jelas apa yang dimiliki perusahaan.

Jika laba berubah, harus dapat dijelaskan penyebabnya.

Jika periode ditutup, kondisi periode tersebut harus tetap dapat dipertanggungjawabkan.

---

# CHECKPOINT TERAKHIR

Setelah selesai melakukan seluruh testing, tanyakan kepada diri sendiri:

> **“Kalau saya adalah owner perusahaan dan saya menyerahkan seluruh pencatatan keuangan kepada sistem ini, apakah saya percaya laporan yang diberikan?”**

Jika jawabannya:

**Ya**

→ Accounting mulai matang.

Jika:

**Belum**

→ cari tahu kenapa.

Jangan langsung memperbaiki.

Temukan dulu akar masalahnya.

Karena tujuan testing bukan membuat aplikasi terlihat sempurna.

Tujuan testing adalah menemukan **seberapa jauh aplikasi mampu merepresentasikan dunia bisnis yang sebenarnya.**
