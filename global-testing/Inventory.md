# Inventory Business Case Testing Guide

## Panduan Pengujian Module Inventory Berdasarkan Skenario Bisnis

### Tujuan

Dokumen ini digunakan untuk menguji module Inventory dengan pendekatan bisnis murni.

Jangan mulai dengan pertanyaan:

> “Apakah jumlah stok berubah?”

Mulailah dengan:

> **“Apakah perusahaan selalu mengetahui barang apa yang dimiliki, berada di mana, berapa jumlahnya, dari mana datangnya, ke mana bergerak, dan kenapa jumlahnya berubah?”**

Inventory adalah penghubung berbagai aktivitas perusahaan.

Inventory dapat menerima pengaruh dari:

**Purchase → Inventory**

**Inventory → Sales**

**Inventory → Transfer**

**Inventory → Production**

**Inventory → Return**

**Inventory → Adjustment**

**Inventory → Accounting**

Karena itu, Inventory harus diuji sebagai **pusat perjalanan barang**, bukan hanya sebagai daftar jumlah stock.

---

# CARA MENGGUNAKAN PANDUAN INI

Gunakan beberapa jenis perusahaan.

Jangan menganggap semua barang diperlakukan sama.

Bandingkan:

* Restoran
* Distributor
* Retail
* Manufacturing
* Multi Outlet
* Perusahaan Jasa

Perhatikan bahwa setiap bisnis memiliki pola inventory yang berbeda.

---

# KONSEP DASAR YANG HARUS SELALU DIPERIKSA

Untuk setiap barang, tanyakan:

### WHAT?

Barang apa?

### HOW MANY?

Berapa jumlahnya?

### WHERE?

Di mana barang tersebut berada?

### WHO?

Siapa yang bertanggung jawab?

### WHEN?

Kapan barang tersebut masuk atau keluar?

### WHY?

Kenapa jumlahnya berubah?

### STATUS?

Apakah barang:

* tersedia?
* dipesan?
* sedang dikirim?
* diterima?
* rusak?
* dikarantina?
* dikembalikan?
* sudah digunakan?

Jika salah satu pertanyaan tersebut tidak dapat dijawab, catat sebagai potential gap.

---

# CASE 1 — RESTORAN

## Profil

Nama: **Saji Rasa**

Memiliki:

* bahan makanan
* minuman
* kemasan
* perlengkapan dapur
* peralatan

---

# Skenario 1 — Barang Masuk

Restoran menerima:

**100 kg beras**

dari supplier.

### Pertanyaan

Apakah perusahaan mengetahui:

* barang apa?
* jumlah?
* tanggal diterima?
* dari supplier siapa?
* masuk ke lokasi mana?

---

# Skenario 2 — Barang Digunakan

Restoran menggunakan:

**20 kg beras**

untuk kegiatan operasional.

### Pertanyaan

Bagaimana perusahaan mengetahui bahwa stock berkurang?

Yang penting:

> Apakah pengurangan stock memiliki alasan yang jelas?

---

# Skenario 3 — Stock Rusak

Ditemukan:

**5 kg beras rusak.**

### Pertanyaan

Apakah perusahaan hanya mengurangi stock?

Atau harus diketahui:

> 5 kg hilang karena kerusakan.

Informasi penyebab sangat penting.

---

# Skenario 4 — Stock Fisik Berbeda

Catatan menunjukkan:

**75 kg**

Tetapi saat dihitung secara fisik:

**70 kg**

### Pertanyaan

Apa yang terjadi?

Apakah perusahaan dapat melakukan pemeriksaan?

Apakah selisih dapat dicatat?

Apakah alasan selisih dapat diketahui?

---

# Skenario 5 — Stock Minimum

Restoran menetapkan:

> Beras minimum 30 kg.

Stock sekarang:

25 kg.

### Pertanyaan

Apakah perusahaan mengetahui bahwa stock sudah berada di bawah batas yang ditentukan?

Apakah kondisi tersebut dapat memicu kebutuhan pembelian?

---

# CASE 2 — DISTRIBUTOR

## Profil

Nama: **Maju Distribusi**

Memiliki:

* 1 gudang utama
* 5.000 SKU
* barang masuk dari supplier
* barang keluar untuk customer

---

# Skenario 1 — Purchase Masuk

PO:

1.000 unit.

Supplier mengirim:

700 unit.

### Pertanyaan

Inventory harus mengetahui:

> 700 sudah diterima.

Dan:

> 300 masih belum diterima.

Jangan menganggap seluruh 1.000 unit sudah menjadi stock.

---

# Skenario 2 — Barang Masuk Bertahap

Hari pertama:

400 unit.

Hari kedua:

300 unit.

### Pertanyaan

Apakah histori penerimaan tetap dapat diketahui?

---

# Skenario 3 — Sales Mengirim Barang

Customer memesan:

500 unit.

Gudang mengirim:

300 unit.

### Pertanyaan

Apakah inventory mengetahui:

* 300 sudah keluar?
* 200 masih menjadi kewajiban?
* stock berkurang 300?

---

# Skenario 4 — Backorder

Customer membutuhkan:

500 unit.

Perusahaan hanya memiliki:

300 unit.

### Pertanyaan

Apa yang dilakukan terhadap 200 unit?

Kemungkinan:

* menunggu stock
* pembelian baru
* transfer dari gudang lain
* customer setuju menunggu
* customer membatalkan sisa

Yang diuji:

> Apakah inventory dapat merepresentasikan kondisi tersebut?

---

# CASE 3 — MULTI WAREHOUSE

## Profil

Perusahaan memiliki:

**Warehouse Jakarta**

**Warehouse Bandung**

**Warehouse Surabaya**

---

# Skenario

Jakarta memiliki:

1.000 unit.

Bandung:

100 unit.

Surabaya:

50 unit.

Customer Jakarta membutuhkan:

300 unit.

### Pertanyaan

Apakah perusahaan dapat mengetahui stock berdasarkan lokasi?

Total perusahaan:

1.150 unit.

Tetapi:

> Stock Jakarta hanya 1.000.

Ini adalah perbedaan penting.

---

# Skenario 2 — Transfer Warehouse

100 unit dipindahkan:

Jakarta → Bandung.

### Pertanyaan

Setelah transfer:

Jakarta berkurang 100.

Bandung bertambah 100.

Tetapi total perusahaan tetap sama.

Apakah sistem memahami perbedaan:

**perubahan lokasi**

dengan

**penambahan stock?**

---

# CASE 4 — RESTAURANT MULTI OUTLET

## Profil

**Nusantara Food Group**

Memiliki:

* Restaurant A
* Restaurant B
* Restaurant C

Setiap outlet memiliki stock sendiri.

---

# Skenario

Restaurant A:

100 kg ayam

Restaurant B:

20 kg ayam

Restaurant C:

5 kg ayam

Restaurant C membutuhkan:

30 kg.

### Pertanyaan

Apakah perusahaan dapat memindahkan:

25 kg

dari outlet lain?

Dan apakah:

> stock perusahaan tetap sama?

---

# Skenario 2 — Outlet Menggunakan Stock

Restaurant A menggunakan:

20 kg bahan.

### Pertanyaan

Apakah hanya stock Restaurant A yang berubah?

Apakah management tetap dapat melihat total stock seluruh perusahaan?

---

# CASE 5 — BARANG DENGAN UNIT BERBEDA

## Skenario

Supplier menjual:

**1 karton**

yang berisi:

**24 botol**

Restaurant menggunakan:

**botol**.

### Pertanyaan

Apakah perusahaan memahami hubungan:

1 karton = 24 botol?

Bagaimana jika membeli:

10 karton?

Berapa botol?

---

# CASE 6 — BARANG DENGAN SATUAN BERAT

Supplier menjual:

**1 karung**

tetapi berat setiap karung tidak selalu sama.

Karung A:

48 kg

Karung B:

52 kg

### Pertanyaan

Apakah perusahaan dapat menangani kondisi bahwa satu unit fisik tidak selalu memiliki berat yang sama?

---

# CASE 7 — BARANG DENGAN BATCH

## Profil

Perusahaan menjual produk makanan.

Setiap produk memiliki batch produksi.

Batch:

**A001**

Jumlah:

500 unit.

Batch:

**A002**

Jumlah:

500 unit.

### Skenario

Customer membeli:

100 unit.

### Pertanyaan

Apakah perusahaan mengetahui barang berasal dari batch mana?

Ini menjadi penting jika suatu hari:

> Batch A001 bermasalah dan harus ditarik.

---

# CASE 8 — EXPIRATION DATE

## Skenario

Restaurant memiliki:

Produk A:

Expired 10 September

Produk A:

Expired 30 September

Produk A:

Expired 15 Oktober

### Pertanyaan

Ketika menggunakan barang, mana yang seharusnya digunakan terlebih dahulu?

Apakah perusahaan dapat mengetahui barang yang mendekati expired?

---

# CASE 9 — SERIAL NUMBER

## Skenario

Perusahaan menjual:

50 laptop.

Setiap laptop memiliki serial number unik.

### Pertanyaan

Apakah perusahaan mengetahui:

* laptop mana yang masuk?
* laptop mana yang dijual?
* customer mana yang menerima?
* laptop mana yang dikembalikan?
* laptop mana yang masih dimiliki perusahaan?

Tidak semua inventory membutuhkan serial number.

Tetapi bisnis tertentu sangat bergantung padanya.

---

# CASE 10 — BARANG RUSAK

## Skenario

Gudang menemukan:

20 unit barang rusak.

### Pertanyaan

Apakah barang tersebut:

* masih tersedia untuk dijual?
* harus dipisahkan?
* menunggu pemeriksaan?
* harus dikembalikan ke supplier?
* harus dimusnahkan?

Jangan hanya berpikir:

> “Kurangi stock 20.”

Pertanyaan bisnisnya:

> **“Apa status sebenarnya dari 20 barang tersebut?”**

---

# CASE 11 — CUSTOMER RETURN

## Skenario

Customer membeli:

100 unit.

Kemudian mengembalikan:

10 unit.

Tetapi:

* 7 unit masih bagus
* 3 unit rusak

### Pertanyaan

Apakah ketiga kondisi tersebut dapat dibedakan?

7 unit mungkin kembali tersedia.

3 unit mungkin tidak dapat dijual kembali.

---

# CASE 12 — SUPPLIER RETURN

## Skenario

Supplier mengirim:

100 unit.

5 unit rusak.

Perusahaan mengembalikan 5 unit kepada supplier.

### Pertanyaan

Apakah inventory mengetahui:

* 100 diterima?
* 5 dikembalikan?
* 95 tetap dimiliki?

---

# CASE 13 — STOCK ADJUSTMENT

## Skenario

Stock sistem:

1.000 unit.

Stock fisik:

980 unit.

Setelah pemeriksaan, ditemukan:

20 unit hilang.

### Pertanyaan

Apakah perusahaan dapat melakukan koreksi?

Dan yang lebih penting:

> Apakah perusahaan tetap mengetahui kenapa stock berubah?

---

# CASE 14 — STOCK COUNT

## Skenario

Perusahaan melakukan stock opname setiap akhir bulan.

Selama stock opname:

Warehouse tetap menerima barang.

Warehouse tetap mengeluarkan barang.

### Pertanyaan

Bagaimana perusahaan mencegah hasil penghitungan menjadi kacau?

Tidak perlu menentukan solusi teknis.

Yang diuji:

> **Apa proses bisnis yang dibutuhkan agar hasil stock opname dapat dipercaya?**

---

# CASE 15 — RESERVED STOCK

## Skenario

Warehouse memiliki:

1.000 unit.

Customer A sudah memesan:

600 unit.

Customer B ingin membeli:

500 unit.

### Pertanyaan

Secara fisik:

1.000 unit memang ada.

Tetapi apakah seluruhnya masih bebas dijual?

Customer A sudah memiliki pesanan.

Maka perusahaan perlu membedakan:

**Physical Stock**

dengan

**Available Stock**

---

# CASE 16 — PURCHASE + SALES BERSAMAAN

## Skenario

Stock:

100 unit.

Customer A memesan:

80 unit.

Pada hari yang sama:

Supplier mengirim:

100 unit.

### Pertanyaan

Bagaimana perusahaan memahami kondisi stock?

Apakah stock supplier yang baru datang otomatis dapat memenuhi pesanan?

Yang diuji adalah hubungan:

**Incoming**

**Available**

**Reserved**

**Outgoing**

---

# CASE 17 — INVENTORY UNTUK PRODUKSI

## Profil

Manufacture Jaya membuat:

**Meja**

Untuk membuat satu meja membutuhkan:

* 1 papan
* 4 kaki
* 8 baut

---

# Skenario

Perusahaan ingin membuat:

100 meja.

### Pertanyaan

Berapa kebutuhan:

* papan?
* kaki?
* baut?

Jika stock tidak cukup:

> Apa yang harus diketahui perusahaan?

---

# Skenario 2 — Produksi Selesai

Produksi menghasilkan:

100 meja.

### Pertanyaan

Apa yang terjadi terhadap:

* bahan baku?
* barang jadi?

Inventory tidak hanya mengalami:

> stock keluar.

Tetapi juga:

> bahan berubah menjadi produk lain.

---

# CASE 18 — INVENTORY UNTUK PACKAGING / BUNDLE

## Skenario

Perusahaan menjual:

**Paket A**

Isi:

* 1 produk utama
* 2 minuman
* 1 snack

Customer membeli:

10 Paket A.

### Pertanyaan

Apakah perusahaan perlu mengetahui dampaknya terhadap masing-masing barang?

---

# CASE 19 — CONSIGNMENT

## Skenario

Supplier menitipkan:

500 unit barang

di gudang perusahaan.

Barang belum menjadi milik perusahaan.

Perusahaan hanya menyimpan dan menjualnya.

### Pertanyaan

Apakah 500 unit tersebut boleh dianggap sebagai stock milik perusahaan?

Ini menguji perbedaan:

**barang berada di lokasi perusahaan**

dengan:

**barang dimiliki perusahaan.**

---

# CASE 20 — BARANG MILIK CUSTOMER

## Skenario

Customer menitipkan bahan:

100 unit

kepada perusahaan untuk diproses.

Barang berada di gudang perusahaan.

### Pertanyaan

Apakah perusahaan boleh menganggap barang tersebut sebagai miliknya?

Sekali lagi:

> **Location ≠ Ownership**

---

# CASE 21 — INVENTORY IN TRANSIT

## Skenario

100 unit dikirim:

Jakarta → Surabaya.

Barang sudah keluar dari Jakarta.

Tetapi belum diterima Surabaya.

### Pertanyaan

Apakah barang:

* sudah tidak ada di Jakarta?
* sudah ada di Surabaya?
* atau sedang dalam perjalanan?

Perusahaan harus dapat memahami:

> **Inventory in transit**

---

# CASE 22 — INVENTORY LOSS

## Skenario

Barang hilang selama perjalanan.

100 unit dikirim.

90 unit diterima.

10 unit hilang.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

* 100 dikirim?
* 90 diterima?
* 10 hilang?
* siapa yang bertanggung jawab?
* apa penyebabnya?

---

# CASE 23 — BARANG GRATIS

## Skenario

Supplier memberikan:

100 unit barang gratis sebagai bonus pembelian.

### Pertanyaan

Apakah barang tersebut masuk ke perusahaan?

Apakah jumlah stock bertambah?

Bagaimana perusahaan memahami bahwa barang tersebut tidak berasal dari pembelian biasa?

---

# CASE 24 — STOCK NEGATIF

## Skenario

Customer membeli:

100 unit.

Stock tercatat:

80 unit.

### Pertanyaan

Apakah perusahaan:

* boleh menjual 100?
* harus menolak?
* memperbolehkan stock negatif?
* melakukan backorder?

Tidak ada jawaban universal.

Yang diuji:

> **Apakah kebijakan inventory perusahaan dapat ditentukan dan dikontrol?**

---

# CASE 25 — STOCK MINIMUM DAN REORDER

## Skenario

Produk A:

Stock minimum: 100

Stock saat ini: 90

Lead time supplier:

7 hari

Rata-rata penggunaan:

20 unit/hari.

### Pertanyaan

Apakah perusahaan hanya melihat:

> “Stock di bawah 100.”

Atau juga mempertimbangkan:

> “Dalam 7 hari, kita mungkin membutuhkan 140 unit.”

Ini menguji apakah keputusan pembelian dapat mempertimbangkan kebutuhan bisnis, bukan hanya angka stock saat ini.

---

# CASE 26 — MANAGEMENT MEMPERTANYAKAN INVENTORY

Management bertanya:

> “Berapa total stock kita?”

↓

Apakah dapat dijawab?

---

> “Stock kita berada di mana?”

↓

Apakah dapat dijawab?

---

> “Barang apa yang paling banyak?”

↓

Apakah dapat dijawab?

---

> “Barang apa yang hampir habis?”

↓

Apakah dapat dijawab?

---

> “Barang apa yang sudah lama tidak bergerak?”

↓

Apakah dapat dijawab?

---

> “Barang apa yang mendekati expired?”

↓

Apakah dapat dijawab?

---

> “Barang apa yang sedang dalam perjalanan?”

↓

Apakah dapat dijawab?

---

> “Barang mana yang sudah dipesan customer tetapi belum dikirim?”

↓

Apakah dapat dijawab?

---

> “Berapa stock yang rusak?”

↓

Apakah dapat dijawab?

---

> “Berapa stock yang hilang?”

↓

Apakah dapat dijawab?

---

> “Berapa nilai inventory kita?”

↓

Apakah dapat dijawab?

---

# TESTING INVENTORY LIFECYCLE

Lakukan satu perjalanan lengkap.

Bayangkan:

**Perusahaan membutuhkan barang**

↓

**Barang dipesan**

↓

**Supplier mengirim**

↓

**Barang diterima**

↓

**Barang diperiksa**

↓

**Barang disimpan**

↓

**Barang dialokasikan / reserved**

↓

**Customer memesan**

↓

**Barang dikeluarkan**

↓

**Barang dikirim**

↓

**Customer menerima**

↓

**Customer melakukan retur**

↓

**Barang diperiksa kembali**

↓

**Barang dijual kembali / rusak / dikarantina**

↓

**Stock opname**

↓

**Ditemukan selisih**

↓

**Dilakukan koreksi**

↓

**Management mengevaluasi inventory**

---

# TESTING INVENTORY STATE

Jangan hanya melihat angka.

Gunakan konsep:

### On Hand

Barang secara fisik berada di bawah penguasaan perusahaan.

### Available

Barang yang masih dapat digunakan/dijual.

### Reserved

Barang sudah dialokasikan untuk kebutuhan tertentu.

### Incoming

Barang sedang menuju perusahaan.

### Outgoing

Barang sedang meninggalkan perusahaan.

### In Transit

Barang sedang berpindah lokasi.

### Damaged

Barang rusak.

### Quarantine

Barang belum boleh digunakan atau dijual karena masih diperiksa.

### Returned

Barang kembali dari customer atau supplier.

### Consignment

Barang berada di perusahaan tetapi bukan milik perusahaan.

Tidak semua bisnis membutuhkan semua kondisi tersebut.

Namun testing harus memastikan konsep-konsep yang relevan dapat direpresentasikan.

---

# TESTING “QUANTITY”

Jangan hanya menguji:

> “Stock = 100.”

Uji:

> **100 itu apa?**

Contoh:

Stock fisik:

100

Reserved:

60

Available:

40

Incoming:

100

Outgoing:

20

Management harus dapat memahami perbedaan masing-masing angka.

---

# TESTING “LOCATION”

Jangan hanya menguji:

> “Stock = 1.000.”

Uji:

Jakarta:

600

Bandung:

300

Surabaya:

100

Total:

1.000

Kemudian:

100 sedang dipindahkan Jakarta → Surabaya.

Maka kondisi perusahaan harus dapat dipahami tanpa menghitung barang tersebut dua kali.

---

# TESTING “OWNERSHIP”

Ini sangat penting.

Barang dapat berada di gudang perusahaan tetapi bukan milik perusahaan.

Contoh:

* Consignment
* Barang customer
* Barang supplier
* Barang titipan

Karena itu:

> **Stock Location ≠ Stock Ownership**

---

# TESTING “VALUE”

Inventory bukan hanya quantity.

Contoh:

Perusahaan memiliki:

100 unit Produk A.

Harga perolehan:

Rp50.000.

Nilai:

Rp5.000.000.

Kemudian terdapat:

* barang rusak
* barang hilang
* barang dikembalikan
* harga perolehan berbeda

### Pertanyaan

Apakah perusahaan dapat memahami bukan hanya:

> “Berapa jumlahnya?”

tetapi juga:

> **“Berapa nilai ekonominya?”**

---

# TESTING INVENTORY VS PURCHASE

Pastikan hubungan:

**Purchase Order**

↓

**Barang Diterima**

↓

**Inventory Bertambah**

Tetapi:

PO:

1.000

Received:

700

Inventory:

+700

Outstanding:

300

Jangan sampai:

> PO 1.000

langsung menyebabkan stock:

> +1.000

---

# TESTING INVENTORY VS SALES

Pastikan hubungan:

**Sales Order**

↓

**Fulfillment**

↓

**Barang Keluar**

Jika SO:

1.000

Barang dikirim:

600

Maka:

Delivered:

600

Outstanding:

400

Jangan sampai seluruh 1.000 dianggap keluar.

---

# TESTING INVENTORY VS ACCOUNTING

Inventory memiliki hubungan dengan nilai perusahaan.

Ketika barang dibeli:

> Perusahaan memperoleh inventory.

Ketika barang dijual:

> Inventory berkurang.

Ketika barang rusak:

> Nilai inventory dapat berubah.

Ketika stock hilang:

> Perusahaan mengalami kehilangan.

Karena itu Inventory nantinya harus dapat memberikan informasi yang cukup kepada Accounting.

Jangan menguji Accounting secara terpisah dari Inventory jika tujuan akhirnya adalah memastikan nilai inventory perusahaan benar.

---

# TESTING INVENTORY VS POS

Untuk restoran:

Customer membeli:

2 nasi ayam.

POS mencatat transaksi.

Inventory harus dapat memahami bahwa bahan yang digunakan untuk menjual menu tersebut mungkin berbeda dengan barang yang terlihat oleh customer.

Contoh:

**1 Nasi Ayam**

menggunakan:

* beras
* ayam
* minyak
* bumbu
* packaging

Maka:

> Penjualan menu dapat menyebabkan perubahan beberapa bahan inventory.

Ini adalah salah satu pengujian penting untuk bisnis restoran.

---

# TESTING EXCEPTION

Setelah happy path selesai, sengaja buat masalah.

### Barang kurang saat diterima.

### Barang rusak saat diterima.

### Barang hilang saat pengiriman.

### Barang expired.

### Stock fisik berbeda dengan catatan.

### Barang salah lokasi.

### Barang salah jumlah.

### Barang customer tercampur dengan stock perusahaan.

### Barang supplier tercampur dengan stock perusahaan.

### Transfer antar warehouse gagal.

### Customer mengembalikan barang.

### Supplier menerima retur.

### Stock berada di bawah minimum.

### Stock negatif.

### Barang dipesan tetapi belum datang.

### Barang sudah datang tetapi belum diperiksa.

### Barang sudah reserved tetapi customer membatalkan.

### Barang sudah dikirim tetapi customer menolak.

### Barang sudah dikirim tetapi hilang.

### Barang ditemukan kembali setelah sebelumnya dianggap hilang.

---

# TESTING MANAGEMENT VIEW

Bayangkan Anda adalah Owner.

Tanyakan:

> **“Berapa stock kita sekarang?”**

> **“Stock tersebut berada di mana?”**

> **“Berapa yang masih bisa dijual?”**

> **“Berapa yang sudah dipesan customer?”**

> **“Berapa yang sedang datang?”**

> **“Apa yang hampir habis?”**

> **“Apa yang sudah lama tidak bergerak?”**

> **“Apa yang rusak?”**

> **“Apa yang expired?”**

> **“Apa yang hilang?”**

> **“Apa yang sedang ditransfer?”**

> **“Barang apa yang bukan milik kita?”**

> **“Berapa nilai inventory kita?”**

Jika pertanyaan tersebut dapat dijawab dengan jelas, Inventory mulai memberikan nilai bisnis yang nyata.

---

# TESTING INVENTORY DENGAN SATU BARANG

Pilih satu produk.

Contoh:

**Produk A**

Kemudian ikuti perjalanan:

**100 unit dibeli**

↓

**80 unit diterima**

↓

**10 unit rusak**

↓

**70 unit tersedia**

↓

**30 unit reserved**

↓

**20 unit dijual**

↓

**10 unit dikirim**

↓

**5 unit dikembalikan**

↓

**2 unit rusak**

↓

**Stock opname**

↓

**Ditemukan selisih**

↓

**Management melihat laporan**

Kemudian tanyakan:

> **“Bisakah saya menjelaskan perjalanan setiap perubahan stock tersebut?”**

Jika bisa, berarti konsep inventory mulai kuat.

---

# FORMAT CATATAN TESTING

Untuk setiap case gunakan:

**Business Case**

Apa yang terjadi?

**Expected Business Result**

Apa yang seharusnya diketahui atau dilakukan perusahaan?

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

# URUTAN TESTING YANG DISARANKAN

Mulai dari:

**1. Basic Stock In**

↓

**2. Basic Stock Out**

↓

**3. Purchase → Inventory**

↓

**4. Sales → Inventory**

↓

**5. Partial Receipt**

↓

**6. Partial Delivery**

↓

**7. Warehouse Transfer**

↓

**8. Multi Outlet**

↓

**9. Reservation**

↓

**10. Return**

↓

**11. Damaged Stock**

↓

**12. Stock Adjustment**

↓

**13. Stock Opname**

↓

**14. Batch**

↓

**15. Expiration**

↓

**16. Serial Number**

↓

**17. Consignment**

↓

**18. Inventory in Transit**

↓

**19. Manufacturing**

↓

**20. POS / Restaurant Consumption**

↓

**21. Reorder**

↓

**22. Inventory Value**

↓

**23. Exception Cases**

↓

**24. Management Questions**

↓

**25. Cross-module Testing**

↓

**26. Catat Gap**

↓

**27. Tentukan apakah Gap merupakan Bug, Konfigurasi, Keterbatasan, atau Kebutuhan Bisnis Baru**

---

# CROSS-MODULE TESTING

Setelah Inventory diuji sendiri, jangan berhenti.

Uji hubungan dengan module lain.

### PURCHASE

Purchase Order
→ Barang diterima
→ Inventory bertambah

---

### SALES

Sales Order
→ Fulfillment
→ Inventory berkurang

---

### POS

Transaksi
→ Barang/menu digunakan
→ Inventory berubah

---

### ACCOUNTING

Inventory berubah
→ Nilai finansial perusahaan ikut berubah

---

### ASSET

Barang dibeli untuk menjadi aset
→ Jangan otomatis dianggap sebagai inventory yang tersedia untuk dijual.

---

### MANUFACTURING

Bahan baku keluar
→ Barang jadi masuk

---

# CHECKPOINT TERAKHIR

Bayangkan Anda adalah Owner.

Anda bertanya:

> **“Apakah angka stock yang saya lihat benar-benar dapat dipercaya?”**

Kemudian:

> **“Kalau berubah, kenapa berubah?”**

> **“Kalau berkurang, siapa yang mengambil atau menggunakan?”**

> **“Kalau bertambah, dari mana datangnya?”**

> **“Kalau barang ada di gudang, apakah benar milik kita?”**

> **“Kalau stock kurang, apa penyebabnya?”**

> **“Kalau barang sudah dipesan customer, apakah masih bisa dijual ke customer lain?”**

> **“Kalau barang sedang dikirim antar lokasi, sebenarnya stock itu berada di mana?”**

> **“Kalau barang rusak, apakah masih dianggap tersedia?”**

> **“Berapa nilai inventory kita sebenarnya?”**

Jika semua pertanyaan tersebut dapat dijawab dengan jelas:

> **Inventory mulai dapat dipercaya sebagai sumber informasi bisnis.**

---

# PRINSIP UTAMA INVENTORY TESTING

Jangan mengejar:

> “Jumlah stock selalu benar.”

Kejar:

> **“Setiap perubahan stock memiliki alasan, lokasi, status, waktu, dan konteks bisnis yang dapat dijelaskan.”**

Karena:

**Stock bukan sekadar angka.**

Stock adalah:

> **barang + jumlah + lokasi + status + kepemilikan + nilai + histori**

Dan ketika Inventory menjadi penghubung:

**Purchase → Inventory → Sales**

**Purchase → Inventory → Accounting**

**Sales → Inventory → Accounting**

**POS → Inventory**

**Manufacturing → Inventory**

maka kualitas Inventory akan sangat menentukan kualitas keseluruhan ERP.

---

# PRINSIP PENUTUP

**Inventory bukan gudang angka.**

Inventory adalah gambaran mengenai:

> **Apa yang perusahaan miliki, di mana barang tersebut berada, apa yang dapat digunakan atau dijual, apa yang sedang bergerak, dan bagaimana barang tersebut berubah sepanjang aktivitas bisnis.**

Satu perusahaan bukan representasi seluruh dunia bisnis.

Restoran, distributor, retail, manufacturing, perusahaan jasa, multi-outlet, dan perusahaan dengan consignment dapat memiliki kebutuhan inventory yang berbeda.

Tujuan testing adalah menemukan:

**Pola umum → kemampuan sistem**

**Pola berbeda → konfigurasi**

**Pola khusus → kebutuhan khusus**

Bukan memaksa semua perusahaan mengikuti satu pola inventory.
