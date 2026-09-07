# HRM Business Case Testing Guide

## Panduan Pengujian HRM Berdasarkan Skenario Bisnis

### Tujuan

Dokumen ini digunakan untuk menguji module HRM dengan pendekatan bisnis murni.

Testing tidak dimulai dari pertanyaan:

> “Apakah tombol ini bekerja?”

Tetapi dari:

> “Jika saya menjadi perusahaan ini, apakah seluruh proses pengelolaan karyawan saya dapat dijalankan dengan benar?”

Tujuan akhirnya adalah menemukan apakah HRM mampu menangani **perbedaan pola bisnis**, bukan hanya menjalankan satu pola perusahaan.

---

# CARA MENGGUNAKAN PANDUAN INI

Untuk setiap perusahaan, bayangkan bahwa Anda baru ditunjuk untuk mengelola HR perusahaan tersebut.

Jangan langsung memikirkan bagaimana aplikasi harus bekerja.

Ikuti alurnya:

**Kenali perusahaan → Kenali karyawan → Buat aturan → Jalankan aktivitas → Hadapi kejadian → Evaluasi hasil**

Setiap case memiliki aturan yang berbeda.

Jika sebuah proses dapat berjalan pada Case A tetapi gagal pada Case B, jangan langsung menganggap Case B salah.

Justru itulah tujuan testing.

---

# CASE 1 — RESTORAN SINGLE OUTLET

## Profil Perusahaan

Nama: **Saji Rasa**

Jenis usaha: Restoran

Jumlah outlet: 1

Jumlah karyawan: 22 orang

Jam operasional: 10.00–22.00

Pembagian karyawan:

* 1 Restaurant Manager
* 2 Supervisor
* 6 Cashier
* 8 Kitchen Staff
* 5 Service Staff

Perusahaan masih dikelola langsung oleh pemilik.

---

## Pola Kerja

Restoran memiliki dua kelompok jam kerja:

**Shift Pagi**

* 09.00–17.00

**Shift Sore**

* 14.00–22.00

Karyawan mendapatkan satu hari libur dalam satu minggu.

Hari libur tidak selalu sama untuk semua karyawan.

---

## Skenario 1 — Karyawan Baru

Perusahaan menerima seorang Kitchen Staff baru.

Informasi:

Nama: Andi

Posisi: Kitchen Staff

Departemen: Kitchen

Atasan: Kitchen Supervisor

Tanggal mulai bekerja: 1 September

Gaji bulanan: Rp4.000.000

### Pertanyaan Testing

Apakah perusahaan dapat:

* mencatat Andi sebagai karyawan?
* menentukan posisi Andi?
* menentukan departemen?
* menentukan atasannya?
* menentukan tanggal mulai bekerja?
* menentukan jadwal kerjanya?
* memasukkan Andi ke dalam struktur perusahaan?

---

# Skenario 2 — Perpindahan Posisi

Setelah bekerja selama 8 bulan, Andi dipromosikan menjadi Kitchen Supervisor.

Perubahan tersebut berlaku mulai 1 Mei.

Gaji juga berubah.

### Pertanyaan Testing

Apakah riwayat Andi tetap menunjukkan bahwa sebelumnya ia adalah Kitchen Staff?

Apakah posisi barunya mulai berlaku pada tanggal yang benar?

Apakah informasi sebelumnya tetap dapat diketahui?

---

# Skenario 3 — Karyawan Tidak Masuk

Seorang Cashier tidak masuk karena sakit.

Supervisor mengetahui bahwa karyawan tersebut sakit pada pagi hari.

### Pertanyaan

Bagaimana perusahaan mencatat kejadian tersebut?

Apakah ketidakhadiran tersebut berbeda dengan:

* cuti?
* izin?
* tanpa keterangan?

---

# Skenario 4 — Lembur

Pada hari Sabtu restoran sangat ramai.

Seorang Kitchen Staff bekerja 3 jam lebih lama dari jadwal normal.

### Pertanyaan

Bagaimana perusahaan mengetahui bahwa karyawan tersebut lembur?

Siapa yang seharusnya mengetahui atau menyetujui lembur?

Bagaimana lembur tersebut mempengaruhi hak karyawan?

---

# CASE 2 — PERUSAHAAN DISTRIBUSI

## Profil Perusahaan

Nama: **Maju Distribusi**

Jenis usaha: Distributor FMCG

Jumlah karyawan: 75 orang

Lokasi: 1 kantor pusat + 1 gudang

Departemen:

* Management
* Finance
* HR
* Sales
* Warehouse
* Delivery

---

## Pola Kerja

Tidak semua karyawan memiliki jadwal yang sama.

### Office Staff

Senin–Jumat:

08.00–17.00

### Warehouse

Senin–Sabtu:

07.00–15.00

### Sales

Tidak selalu berada di kantor.

### Driver

Memiliki jadwal berdasarkan kebutuhan pengiriman.

---

# Skenario 1 — Satu Perusahaan, Banyak Pola Kerja

HR harus mengelola tiga kelompok karyawan dengan pola kerja berbeda.

### Testing

Pastikan perusahaan dapat memiliki:

* jam kerja berbeda
* hari kerja berbeda
* aturan kehadiran berbeda
* pola kerja berbeda

tanpa harus membuat perusahaan baru.

---

# Skenario 2 — Transfer Departemen

Seorang Sales dipindahkan menjadi bagian dari Warehouse.

Perpindahan berlaku mulai tanggal 1 Juli.

Atasan berubah.

Jadwal kerja juga berubah.

### Testing

Periksa apakah seluruh perubahan dapat dicatat tanpa menghilangkan riwayat sebelumnya.

---

# Skenario 3 — Karyawan Dipindahkan Sementara

Seorang Warehouse Staff diminta membantu Sales selama dua minggu untuk kegiatan promosi.

Status kepegawaiannya tidak berubah.

### Pertanyaan

Apakah perusahaan dapat membedakan:

**perubahan permanen**

dengan

**penugasan sementara?**

Ini penting karena perusahaan nyata sering memiliki kondisi seperti ini.

---

# Skenario 4 — Keterlambatan

Seorang karyawan datang terlambat selama 45 menit.

Perusahaan memiliki aturan:

* keterlambatan dicatat
* supervisor dapat memberikan toleransi
* keterlambatan berulang dapat mempengaruhi evaluasi karyawan

### Testing

Jangan hanya menguji apakah “terlambat” dapat dicatat.

Pikirkan juga:

> Apa konsekuensi bisnis dari keterlambatan tersebut?

---

# CASE 3 — PERUSAHAAN TEKNOLOGI

## Profil Perusahaan

Nama: **Nusantara Digital**

Jenis usaha: Software Development

Jumlah karyawan: 120 orang

Departemen:

* Engineering
* Product
* Design
* Sales
* Marketing
* Finance
* HR
* Management

---

## Pola Kerja

Perusahaan menerapkan flexible working.

Sebagian karyawan bekerja dari kantor.

Sebagian bekerja remote.

Sebagian menggunakan pola hybrid.

---

# Skenario 1 — Karyawan Remote

Seorang programmer bekerja dari luar kota.

Ia tetap merupakan karyawan perusahaan.

Tidak memiliki meja atau lokasi kerja tetap.

### Testing

Apakah konsep “tempat kerja” harus selalu berupa kantor fisik?

Apakah perusahaan dapat mengelola karyawan dengan pola kerja berbeda?

---

# Skenario 2 — Cuti

Seorang karyawan mengajukan cuti selama 5 hari.

HR harus mengetahui:

* berapa hak cutinya?
* berapa yang telah digunakan?
* berapa yang tersisa?
* apakah cuti tersebut disetujui?
* siapa yang menyetujui?

---

# Skenario 3 — Atasan Mengajukan Cuti

Seorang Engineering Manager juga mengajukan cuti.

Tetapi bawahannya tetap harus bekerja.

### Pertanyaan

Siapa yang menangani pekerjaan selama Manager tidak berada di tempat?

Apakah perusahaan membutuhkan pengganti sementara?

Case ini menguji apakah HRM hanya memahami “orang”, atau juga memahami **struktur tanggung jawab**.

---

# Skenario 4 — Karyawan Resign

Seorang programmer mengundurkan diri.

Tanggal terakhir bekerja: 30 November.

Perusahaan tetap membutuhkan riwayat karyawan tersebut.

### Testing

Setelah karyawan tidak lagi aktif:

Apakah riwayatnya tetap ada?

Apakah perusahaan masih dapat melihat:

* posisi terakhir?
* departemen?
* riwayat perpindahan?
* riwayat cuti?
* riwayat kehadiran?
* masa kerja?

Karyawan tidak boleh seolah-olah “hilang” hanya karena sudah tidak aktif.

---

# CASE 4 — GRUP PERUSAHAAN / MULTI OUTLET

## Profil Perusahaan

Nama: **Nusantara Hospitality Group**

Memiliki:

* 3 restoran
* 1 hotel kecil
* 1 kantor pusat

Total karyawan: 250 orang.

---

## Struktur

### Head Office

Mengelola:

* HR
* Finance
* Management

### Restaurant A

60 karyawan.

### Restaurant B

45 karyawan.

### Restaurant C

55 karyawan.

### Hotel

90 karyawan.

---

# Skenario 1 — Karyawan Pindah Outlet

Seorang Supervisor Restaurant A dipindahkan ke Restaurant B.

Orang yang sama.

Perusahaan yang sama.

Tetapi lokasi kerjanya berubah.

### Testing

Pastikan perpindahan tersebut tidak dianggap sebagai:

> karyawan baru.

Riwayat karyawan harus tetap utuh.

---

# Skenario 2 — Karyawan Membantu Outlet Lain

Restaurant C kekurangan karyawan.

Seorang Service Staff dari Restaurant B diminta membantu selama 10 hari.

Setelah itu kembali ke Restaurant B.

### Pertanyaan

Apakah perusahaan dapat memahami perbedaan:

* tempat kerja utama
* penugasan sementara
* perpindahan permanen

---

# Skenario 3 — Struktur Atasan Berbeda

Di Restaurant A:

Service Staff → Supervisor → Restaurant Manager

Di Head Office:

HR Staff → HR Manager → Director

Di Hotel:

Staff → Supervisor → Department Manager → General Manager

### Testing

Jangan berasumsi semua departemen memiliki struktur yang sama.

---

# CASE PEMBANDING — PERBEDAAN POLA PERUSAHAAN

Gunakan tabel ini sebagai pengingat bahwa HRM tidak boleh dibangun hanya berdasarkan satu perusahaan.

| Aspek               | Restoran       | Distributor | Tech Company | Group Company     |
| ------------------- | -------------- | ----------- | ------------ | ----------------- |
| Jumlah karyawan     | Kecil          | Sedang      | Besar        | Besar             |
| Shift               | Sangat penting | Penting     | Tidak selalu | Sangat penting    |
| Remote              | Tidak umum     | Jarang      | Umum         | Bisa berbeda      |
| Multi lokasi        | Rendah         | Sedang      | Bisa tinggi  | Sangat tinggi     |
| Transfer            | Ada            | Sering      | Ada          | Sangat sering     |
| Penugasan sementara | Ada            | Ada         | Ada          | Sangat sering     |
| Struktur atasan     | Sederhana      | Sedang      | Kompleks     | Kompleks          |
| Cuti                | Ada            | Ada         | Ada          | Ada               |
| Lembur              | Sering         | Bisa sering | Tergantung   | Berbeda tiap unit |

---

# TESTING LEVEL 1 — EMPLOYEE LIFECYCLE

Setelah seluruh case di atas selesai, lakukan satu perjalanan lengkap seorang karyawan.

Bayangkan:

> “Saya adalah seorang karyawan yang masuk perusahaan hari ini.”

Ikuti perjalanan:

**Recruitment → Join → Penempatan → Bekerja → Cuti → Sakit → Terlambat → Lembur → Promosi → Transfer → Penugasan → Evaluasi → Resign**

Untuk setiap tahap, tanyakan:

> “Apakah perusahaan memiliki informasi yang cukup untuk mengambil keputusan?”

Jika jawabannya tidak, cari tahu informasi apa yang hilang.

---

# TESTING LEVEL 2 — PERUBAHAN

HRM yang bagus bukan hanya mampu mencatat kondisi saat ini.

Ia juga harus mampu memahami perubahan.

Uji:

### Karyawan

Tetap orang yang sama.

Tetapi:

* posisi berubah
* departemen berubah
* atasan berubah
* lokasi berubah
* jadwal berubah
* gaji berubah

### Pertanyaan utama

> Apakah kondisi lama masih dapat diketahui?

Kalau tidak, HRM berpotensi kehilangan sejarah bisnis.

---

# TESTING LEVEL 3 — EXCEPTION CASE

Setelah happy path selesai, sengaja buat masalah.

Contoh:

### Karyawan masuk di tengah bulan

Bagaimana perlakuannya?

### Karyawan keluar sebelum akhir bulan

Bagaimana statusnya?

### Karyawan dipindahkan di tengah periode

Mana aturan lama dan mana aturan baru?

### Karyawan memiliki dua jenis jadwal

Bagaimana perusahaan menentukan jadwal yang berlaku?

### Karyawan cuti ketika atasannya juga sedang cuti

Siapa yang menangani?

### Karyawan salah mencatat kehadiran

Bagaimana koreksinya?

### Karyawan bekerja pada hari libur

Bagaimana perusahaan memperlakukannya?

### Karyawan bekerja lembur tetapi tidak disetujui

Apa yang terjadi?

---

# TESTING LEVEL 4 — “APAKAH SAYA SEBAGAI HR BISA MENJAWAB?”

Ini adalah pengujian yang sangat penting.

Jangan melihat menu aplikasi.

Ambil sebuah pertanyaan dari Management:

> “Berapa jumlah karyawan kita saat ini?”

Lalu:

> “Berapa orang yang sedang cuti?”

> “Siapa saja yang baru masuk bulan ini?”

> “Siapa yang sudah bekerja lebih dari 5 tahun?”

> “Siapa yang pindah departemen bulan ini?”

> “Berapa orang yang resign bulan ini?”

> “Departemen mana yang paling banyak kehilangan karyawan?”

> “Siapa yang sedang tidak aktif?”

> “Siapa yang bekerja di outlet tertentu?”

> “Siapa atasan dari karyawan X?”

> “Sejak kapan dia menjadi Supervisor?”

Jika HRM dapat membantu menjawab pertanyaan bisnis tersebut, berarti data yang dikumpulkan mulai memiliki nilai.

---

# ATURAN TESTING

Selama melakukan testing, gunakan tiga jenis pertanyaan.

## 1. WHAT?

Apa yang terjadi?

Contoh:

> Andi dipromosikan.

## 2. WHEN?

Kapan kejadian tersebut berlaku?

Contoh:

> Promosi berlaku mulai 1 Mei.

## 3. WHY / CONSEQUENCE?

Apa akibatnya bagi perusahaan?

Contoh:

> Setelah promosi, posisi, atasan, tanggung jawab, dan kemungkinan kompensasi Andi berubah.

Jangan berhenti pada:

> “Data promosi berhasil disimpan.”

Itu bukan business testing.

Pertanyaan sebenarnya:

> “Apakah perusahaan sekarang memiliki gambaran yang benar tentang kondisi Andi setelah promosi?”

---

# FORMAT CATATAN TESTING

Untuk setiap kasus, gunakan format sederhana:

**Business Case**

Apa yang terjadi?

**Expected Business Result**

Apa yang seharusnya diketahui atau dapat dilakukan perusahaan?

**Actual Result**

Apa yang terjadi ketika kasus dijalankan?

**Gap**

Apa yang belum dapat direpresentasikan?

**Impact**

Seberapa besar masalah tersebut bagi perusahaan?

**Decision**

Apakah:

* perlu diperbaiki?
* dapat dikonfigurasi?
* merupakan batasan yang dapat diterima?
* perlu dipikirkan ulang?

---

# PRIORITAS MENEMUKAN GAP

Tidak semua gap harus langsung diperbaiki.

Gunakan empat kategori:

### Critical

Bisnis tidak dapat menjalankan proses penting.

### High

Proses masih dapat berjalan tetapi berpotensi menyebabkan masalah serius.

### Medium

Mengganggu kenyamanan atau efisiensi.

### Low

Masalah kecil atau kebutuhan tambahan.

---

# TUJUAN AKHIR TESTING

Jangan mengejar:

> “HRM saya harus memiliki semua fitur HR.”

Kejar:

> “HRM saya mampu merepresentasikan berbagai cara perusahaan menjalankan bisnis.”

Karena perusahaan A mungkin menggunakan shift.

Perusahaan B menggunakan office hour.

Perusahaan C menggunakan remote.

Perusahaan D memiliki multi-outlet.

Perusahaan E memiliki struktur organisasi yang sangat kompleks.

Sistem yang baik bukan sistem yang memaksa semuanya menggunakan satu pola.

Sistem yang baik mampu **mengakomodasi pola yang berbeda tanpa kehilangan kontrol terhadap bisnis.**

---

# URUTAN TESTING YANG DISARANKAN

Mulai dari:

**1. Single Outlet Restaurant**

↓

**2. Distributor**

↓

**3. Technology Company**

↓

**4. Multi-Outlet / Group Company**

↓

**5. Employee Lifecycle**

↓

**6. Change & Transfer**

↓

**7. Exception Cases**

↓

**8. Management Questions**

↓

**9. Catat Gap**

↓

**10. Tentukan apakah Gap merupakan Bug, Keterbatasan, atau Kebutuhan Bisnis Baru**

---

# CATATAN UNTUK PENGEMBANG

Jangan buru-buru mengubah aplikasi ketika menemukan sebuah gap.

Tanyakan terlebih dahulu:

> “Apakah ini benar-benar kebutuhan umum perusahaan, atau hanya kebiasaan perusahaan yang sedang saya jadikan referensi?”

Kemudian tanyakan:

> “Apakah pola ini dapat terjadi pada perusahaan lain?”

Jika jawabannya iya, pertimbangkan sebagai kebutuhan sistem.

Jika hanya terjadi karena kebijakan satu perusahaan, pertimbangkan apakah seharusnya menjadi konfigurasi.

Jika hanya kasus ekstrem, jangan langsung membuat arsitektur menjadi rumit.

---

## Prinsip Utama

**Jangan mengembangkan HRM berdasarkan cara satu perusahaan bekerja.**

**Kembangkan HRM berdasarkan pola yang dapat terjadi pada banyak jenis perusahaan.**

Testing adalah proses untuk menemukan pola tersebut.
