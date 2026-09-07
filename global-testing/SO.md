# Sales Order Business Case Testing Guide

## Panduan Pengujian Module Sales Order Berdasarkan Skenario Bisnis

### Tujuan

Dokumen ini digunakan untuk menguji module Sales Order (SO) dengan pendekatan bisnis murni.

Jangan mulai dengan pertanyaan:

> “Apakah Sales Order berhasil dibuat?”

Mulailah dengan:

> **“Jika saya adalah perusahaan ini, apakah seluruh komitmen penjualan kepada customer dapat dikelola dengan benar sampai kewajibannya selesai?”**

Sales Order bukan sekadar dokumen pesanan.

SO merupakan bagian dari perjalanan:

**Kebutuhan Customer → Penawaran → Persetujuan → Pesanan → Pemenuhan → Pengiriman → Tagihan → Pembayaran**

Namun dunia nyata tidak selalu berjalan lurus.

Karena itu, testing harus mencakup:

* perubahan pesanan
* pembatalan
* partial fulfillment
* perubahan harga
* retur
* pembayaran sebagian
* keterlambatan
* produk tidak tersedia
* customer baru
* customer lama
* multi outlet
* jasa
* kontrak
* penjualan berulang

---

# CARA MENGGUNAKAN PANDUAN INI

Gunakan beberapa jenis perusahaan.

Jangan menganggap semua bisnis menjual dengan cara yang sama.

Untuk setiap case:

**Kenali kebutuhan customer → Buat kesepakatan → Terima pesanan → Penuhi pesanan → Kirim/selesaikan → Tagih → Terima pembayaran → Selesaikan pesanan**

Kemudian sengaja ubah kondisi untuk melihat apakah proses bisnis masih dapat dikendalikan.

---

# CASE 1 — RESTORAN

## Profil Perusahaan

Nama: **Saji Rasa**

Jenis usaha: Restoran

Jumlah outlet: 1

Produk:

* makanan
* minuman
* paket makanan
* catering

---

# Skenario 1 — Pesanan Langsung

Customer memesan:

* 10 nasi ayam
* 5 es teh
* 5 jus

Total:

Rp500.000.

Customer membayar langsung.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

* apa yang dipesan?
* jumlahnya?
* harga?
* siapa customer?
* metode pembayaran?
* apakah pesanan sudah selesai?

---

# Skenario 2 — Pesanan Catering

Customer memesan catering:

**100 porsi**

untuk tanggal:

**15 September**

Nilai pesanan:

**Rp8.000.000**

Customer membayar uang muka:

**Rp3.000.000**

### Pertanyaan

Apakah perusahaan mengetahui:

* total nilai pesanan?
* uang muka?
* sisa pembayaran?
* tanggal pemenuhan?
* jumlah yang harus disiapkan?

---

# Skenario 3 — Perubahan Pesanan

Customer awalnya memesan:

100 porsi.

Kemudian mengubah menjadi:

120 porsi.

Perubahan dilakukan seminggu sebelum acara.

### Pertanyaan

Apakah perubahan tersebut dapat diketahui?

Apakah harga berubah?

Apakah customer harus menyetujui perubahan?

Apakah tim operasional mengetahui jumlah terbaru?

---

# Skenario 4 — Pembatalan

Customer membatalkan catering.

Pembatalan dilakukan:

3 hari sebelum tanggal acara.

Customer sudah membayar uang muka.

### Pertanyaan

Apa yang terjadi terhadap:

* pesanan?
* uang muka?
* kewajiban perusahaan?
* persiapan operasional?

Apakah kebijakan pembatalan dapat berbeda untuk jenis pesanan tertentu?

---

# CASE 2 — DISTRIBUTOR

## Profil

Nama: **Maju Distribusi**

Jumlah karyawan: 75

Customer:

* toko retail
* supermarket
* reseller
* perusahaan

Penjualan dilakukan dalam jumlah besar.

---

# Skenario 1 — Customer Memesan Barang

Customer memesan:

1.000 unit Produk A

Harga:

Rp100.000/unit.

Total:

Rp100.000.000.

Barang tidak langsung dikirim.

### Pertanyaan

Apakah perusahaan dapat mengetahui bahwa:

> Customer sudah memiliki pesanan senilai Rp100 juta

meskipun barang belum dikirim dan belum dibayar?

---

# Skenario 2 — Customer Meminta Tempo

Customer tidak membayar langsung.

Kesepakatan:

**30 hari setelah tagihan.**

### Pertanyaan

Apakah perusahaan dapat mengetahui:

* nilai pesanan?
* kapan tagihan akan muncul?
* kapan pembayaran diharapkan?
* customer mana yang memiliki kewajiban?

---

# Skenario 3 — Barang Tidak Cukup

Customer memesan:

1.000 unit.

Stock perusahaan hanya:

700 unit.

### Pertanyaan

Apa yang dilakukan?

Kemungkinan:

* kirim 700 dahulu
* menunggu 300
* mencari stock dari lokasi lain
* menawarkan pengganti
* meminta customer mengurangi pesanan

Tidak semua perusahaan memiliki kebijakan yang sama.

Yang diuji:

> **Apakah perusahaan dapat mengelola kondisi tersebut tanpa kehilangan konteks pesanan customer?**

---

# Skenario 4 — Partial Delivery

Pesanan:

1.000 unit.

Pengiriman:

Hari 1 → 400 unit

Hari 2 → 300 unit

Hari 3 → 300 unit

### Pertanyaan

Apakah perusahaan dapat mengetahui:

* total pesanan?
* total yang sudah dikirim?
* total yang belum dikirim?
* pengiriman mana yang sudah selesai?

---

# CASE 3 — JASA KONSULTASI

## Profil

Nama: **Nusantara Consulting**

Menjual:

* konsultasi
* training
* implementation
* maintenance

Tidak menjual barang fisik.

---

# Skenario 1 — Kontrak Jasa

Customer menyetujui jasa:

**Rp120.000.000**

untuk periode 12 bulan.

### Pertanyaan

Apakah perusahaan memahami bahwa:

> Customer membeli sebuah layanan,

bukan barang yang dikirim?

Bagaimana perusahaan mengetahui bahwa layanan sudah diberikan?

---

# Skenario 2 — Pembayaran Bertahap

Kontrak:

Rp120 juta.

Pembayaran:

* 30% saat kontrak
* 40% setelah tahap kedua
* 30% setelah selesai

### Pertanyaan

Apakah perusahaan mengetahui:

* total kontrak?
* jumlah yang sudah dibayar?
* jumlah yang dapat ditagihkan?
* milestone yang sudah selesai?
* sisa nilai kontrak?

---

# Skenario 3 — Customer Meminta Perubahan Scope

Awalnya:

> 3 bulan konsultasi.

Kemudian customer meminta tambahan:

> 1 bulan.

Nilai kontrak berubah.

### Pertanyaan

Apakah perubahan tersebut dapat dibedakan dari kesepakatan awal?

Apakah perubahan membutuhkan persetujuan customer?

Apakah nilai pesanan lama tetap dapat diketahui?

---

# CASE 4 — MANUFACTURING

## Profil

Nama: **Manufacture Jaya**

Perusahaan membuat produk berdasarkan pesanan customer.

---

# Skenario 1 — Make to Order

Customer memesan:

**500 unit produk khusus**

Produk belum tersedia.

Perusahaan harus memproduksinya terlebih dahulu.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

> “Ada 500 unit yang harus diproduksi karena customer sudah memesan.”

SO tidak selalu berarti:

> Barang sudah tersedia.

---

# Skenario 2 — Customer Mengubah Spesifikasi

Customer mengubah spesifikasi produk setelah pesanan diterima.

### Pertanyaan

Apakah perubahan tersebut:

* diperbolehkan?
* memerlukan persetujuan?
* mengubah harga?
* mengubah waktu pengiriman?

Dan yang paling penting:

> Apakah tim produksi mengetahui versi pesanan yang benar?

---

# Skenario 3 — Produksi Terlambat

Customer meminta barang:

15 September.

Produksi baru dapat selesai:

25 September.

### Pertanyaan

Apa yang harus diketahui perusahaan?

Siapa yang perlu diberitahu?

Apakah tanggal yang dijanjikan customer masih dianggap berlaku?

---

# CASE 5 — CUSTOMER BARU

## Skenario

Customer baru ingin melakukan pembelian:

Rp200.000.000.

Perusahaan belum pernah bertransaksi dengan customer tersebut.

### Pertanyaan

Apakah perusahaan memiliki proses berbeda untuk customer baru?

Apakah transaksi besar langsung diperbolehkan?

Apakah diperlukan pemeriksaan atau persetujuan tertentu?

---

# CASE 6 — CUSTOMER MEMILIKI HARGA KHUSUS

## Skenario

Harga normal Produk A:

Rp100.000.

Customer tertentu memiliki kesepakatan:

Rp90.000.

Customer membeli:

1.000 unit.

### Pertanyaan

Apakah harga khusus dapat dikenali?

Bagaimana jika customer membeli hanya 100 unit?

Bagaimana jika masa berlaku harga khusus sudah berakhir?

---

# CASE 7 — DISCOUNT

## Skenario

Customer mendapatkan:

Diskon 10%.

Pesanan:

Rp50.000.000.

### Pertanyaan

Apakah perusahaan dapat membedakan:

* harga awal
* diskon
* nilai setelah diskon
* pajak
* total yang harus dibayar?

---

# CASE 8 — HARGA BERUBAH SETELAH PESANAN

## Skenario

Customer memesan:

100 unit × Rp100.000.

Setelah pesanan diterima, perusahaan menaikkan harga menjadi:

Rp110.000.

### Pertanyaan

Apakah harga pesanan customer berubah otomatis?

Atau harga yang sudah disepakati tetap berlaku?

Jika ingin mengubah harga:

> Siapa yang harus menyetujui?

---

# CASE 9 — CUSTOMER MEMINTA PEMBATALAN SEBAGIAN

## Skenario

Customer memesan:

1.000 unit.

Kemudian membatalkan:

300 unit.

### Pertanyaan

Apa yang terjadi terhadap:

* 700 unit?
* 300 unit?
* nilai pesanan?
* persiapan pengiriman?

Apakah pembatalan sebagian dapat dibedakan dari pembatalan seluruh pesanan?

---

# CASE 10 — CUSTOMER MENGEMBALIKAN BARANG

## Skenario

Customer menerima:

100 unit.

Kemudian mengembalikan:

10 unit karena rusak.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

* jumlah awal?
* jumlah yang dikirim?
* jumlah yang diterima customer?
* jumlah yang dikembalikan?
* alasan retur?
* kondisi akhir pesanan?

---

# CASE 11 — BARANG DITOLAK CUSTOMER

## Skenario

Perusahaan mengirim:

500 unit.

Customer hanya menerima:

480 unit.

20 unit ditolak karena rusak.

### Pertanyaan

Apa yang terjadi terhadap 20 unit?

Apakah pesanan dianggap selesai?

Siapa yang bertanggung jawab?

Apakah perusahaan harus mengirim ulang?

---

# CASE 12 — DELIVERY TERLAMBAT

## Skenario

Customer meminta:

> Barang tiba tanggal 10.

Perusahaan baru dapat mengirim tanggal 15.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

* tanggal yang dijanjikan?
* tanggal pengiriman?
* keterlambatan?
* alasan keterlambatan?

Apakah customer harus diberitahu?

---

# CASE 13 — MULTI OUTLET / MULTI LOCATION

## Profil

**Nusantara Hospitality Group**

Memiliki:

* Restaurant A
* Restaurant B
* Restaurant C

Customer melakukan pesanan:

* 100 unit untuk Restaurant A
* 50 unit untuk Restaurant B
* 150 unit untuk Restaurant C

Total:

300 unit.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

> Total pesanan: 300

dan sekaligus:

> A: 100

> B: 50

> C: 150

---

# CASE 14 — SALES ORDER DARI QUOTATION

## Skenario

Sales membuat quotation:

Rp100.000.000.

Customer menyetujui quotation tersebut.

Kemudian perusahaan membuat Sales Order.

### Pertanyaan

Apakah perusahaan dapat mengetahui hubungan:

**Quotation**

↓

**Customer Acceptance**

↓

**Sales Order**

↓

**Fulfillment**

↓

**Invoice**

↓

**Payment**

Jangan sampai setelah menjadi SO, hubungan dengan kesepakatan awal hilang.

---

# CASE 15 — CUSTOMER MEMINTA KONTRAK

Customer menyetujui quotation tetapi mengatakan:

> “Kami harus menggunakan kontrak resmi sebelum pesanan dapat dijalankan.”

### Pertanyaan

Apakah perusahaan dapat membedakan:

* quotation diterima
* kontrak belum selesai
* kontrak sudah selesai
* SO sudah boleh dijalankan

Tidak semua customer memiliki persyaratan legal yang sama.

---

# CASE 16 — DOWN PAYMENT

## Skenario

SO:

Rp100.000.000.

Customer membayar:

**Rp30.000.000**

sebagai uang muka.

Barang belum dikirim.

### Pertanyaan

Apakah perusahaan mengetahui:

* total pesanan?
* uang muka?
* sisa?
* status pemenuhan?
* status pembayaran?

---

# CASE 17 — PARTIAL PAYMENT

## Skenario

Tagihan:

Rp100.000.000.

Customer membayar:

* Rp40 juta
* Rp30 juta
* Rp30 juta

### Pertanyaan

Apakah perusahaan mengetahui bahwa:

> Tagihan sudah lunas

meskipun pembayaran terjadi tiga kali?

---

# CASE 18 — CUSTOMER TIDAK MEMBAYAR

Customer memiliki tagihan:

Rp50.000.000.

Jatuh tempo:

30 hari.

Sudah lewat:

90 hari.

### Pertanyaan

Apakah perusahaan dapat mengetahui bahwa customer memiliki masalah pembayaran?

Apakah informasi tersebut dapat digunakan untuk keputusan penjualan berikutnya?

---

# CASE 19 — CUSTOMER MEMESAN ULANG

Customer yang sama membeli produk yang sama setiap bulan.

### Pertanyaan

Apakah histori dapat membantu sales mengetahui:

* apa yang biasa dibeli?
* berapa jumlah biasanya?
* harga sebelumnya?
* frekuensi pembelian?
* perubahan pola pembelian?

Tujuannya bukan sekadar menyimpan histori.

Tujuannya:

> **Membantu perusahaan mengambil keputusan penjualan.**

---

# CASE 20 — MANAGEMENT MEMPERTANYAKAN PENJUALAN

Management bertanya:

> “Berapa total pesanan bulan ini?”

↓

Apakah dapat dijawab?

---

> “Berapa pesanan yang belum dipenuhi?”

↓

Apakah dapat dijawab?

---

> “Customer mana yang paling banyak membeli?”

↓

Apakah dapat dijawab?

---

> “Berapa nilai pesanan yang masih belum ditagihkan?”

↓

Apakah dapat dijawab?

---

> “Berapa pesanan yang terlambat?”

↓

Apakah dapat dijawab?

---

> “Berapa pesanan yang dibatalkan?”

↓

Apakah dapat dijawab?

---

> “Berapa pesanan yang sudah dikirim tetapi belum dibayar?”

↓

Apakah dapat dijawab?

---

> “Customer mana yang paling sering melakukan retur?”

↓

Apakah dapat dijawab?

---

> “Berapa nilai penjualan yang berasal dari setiap outlet?”

↓

Apakah dapat dijawab?

---

# TESTING SALES LIFECYCLE

Setelah seluruh case selesai, lakukan satu perjalanan lengkap.

Bayangkan:

**Customer membutuhkan sesuatu**

↓

**Sales membuat penawaran**

↓

**Customer menerima penawaran**

↓

**Kesepakatan dibuat**

↓

**Sales Order dibuat**

↓

**Customer melakukan pembayaran awal jika diperlukan**

↓

**Perusahaan menyiapkan barang/jasa**

↓

**Barang/jasa dipenuhi**

↓

**Pengiriman dilakukan**

↓

**Customer menerima**

↓

**Invoice dibuat**

↓

**Customer membayar**

↓

**Pesanan selesai**

---

# TESTING STATUS BISNIS

Jangan hanya melihat:

> “SO ada.”

Pertanyakan kondisi sebenarnya.

Contoh:

### Ordered

Customer sudah memesan.

### Approved

Pesanan sudah mendapatkan persetujuan.

### Confirmed

Kesepakatan sudah dikonfirmasi.

### Fulfillment

Perusahaan sedang memenuhi pesanan.

### Partially Fulfilled

Sebagian sudah dipenuhi.

### Fulfilled

Seluruh pesanan sudah dipenuhi.

### Invoiced

Sudah ditagihkan.

### Partially Paid

Sebagian sudah dibayar.

### Paid

Sudah lunas.

### Cancelled

Pesanan dibatalkan.

### Returned

Sebagian atau seluruh barang dikembalikan.

---

# PENTING: STATUS TIDAK SELALU LINEAR

Jangan menganggap:

**Draft → Approved → Delivered → Invoiced → Paid**

selalu menjadi satu-satunya jalan.

Dunia nyata bisa seperti:

**SO → Partial Delivery → Partial Invoice → Partial Payment → Return → Replacement → Final Payment**

atau:

**SO → Approved → Cancelled**

atau:

**SO → Partial Fulfillment → Customer Cancel Remaining Quantity**

atau:

**SO → Fulfilled → Invoice → Overdue**

Testing harus memeriksa apakah bisnis tetap dapat memahami kondisi tersebut.

---

# TESTING “COMMITMENT”

Ketika customer menyetujui sebuah Sales Order:

> Perusahaan memiliki komitmen untuk memenuhi pesanan.

Tetapi:

**Ordered ≠ Delivered**

**Delivered ≠ Invoiced**

**Invoiced ≠ Paid**

Ini harus selalu dibedakan.

Contoh:

SO:

Rp100 juta

Barang sudah dikirim:

Rp70 juta

Invoice:

Rp50 juta

Payment:

Rp30 juta

Management harus tetap dapat memahami masing-masing kondisi tersebut.

---

# TESTING “WHO SHOULD KNOW?”

Misalnya terdapat SO:

Rp500.000.000.

Siapa yang perlu mengetahui?

* Sales
* Sales Manager
* Warehouse
* Finance
* Management
* Customer

Tetapi tidak semuanya membutuhkan informasi yang sama.

Sales perlu mengetahui:

> status pesanan.

Warehouse perlu mengetahui:

> apa yang harus dipenuhi.

Finance perlu mengetahui:

> apa yang harus ditagihkan dan diterima.

Management perlu mengetahui:

> nilai dan risiko bisnis.

Testing harus memastikan informasi yang dibutuhkan masing-masing pihak tersedia.

---

# TESTING “WHO IS RESPONSIBLE?”

Customer belum menerima barang.

Siapa yang bertanggung jawab?

Kemungkinan:

* Sales
* Warehouse
* Logistics
* Supplier
* Customer

Jangan menganggap semua masalah fulfillment adalah tanggung jawab Sales.

Business case harus memperjelas siapa yang memiliki tanggung jawab pada setiap tahap.

---

# TESTING EXCEPTION

Setelah happy path selesai, sengaja buat masalah.

### Customer membatalkan seluruh pesanan.

### Customer membatalkan sebagian.

### Barang tidak tersedia.

### Barang rusak.

### Barang kurang.

### Barang dikirim ke lokasi yang salah.

### Customer meminta perubahan alamat.

### Harga berubah.

### Discount berubah.

### Customer meminta tambahan quantity.

### Customer meminta pengurangan quantity.

### Customer tidak membayar.

### Customer membayar sebagian.

### Customer membayar lebih.

### Customer melakukan retur.

### Supplier terlambat sehingga fulfillment terlambat.

### Customer meminta pesanan dipercepat.

### Pesanan melewati tanggal yang dijanjikan.

### Kontrak belum selesai.

### Legal document belum lengkap.

### Pesanan membutuhkan approval tambahan.

### Customer meminta perubahan setelah approval.

---

# TESTING SALES VS INVENTORY

Jika sebuah produk terjual:

**100 unit**

tetapi stock hanya:

**70 unit**

### Pertanyaan

Apa yang harus diketahui?

Apakah perusahaan:

* mengirim 70?
* menunggu 30?
* mencari stock lain?
* melakukan backorder?

Jangan memaksa satu jawaban.

Yang diuji:

> **Apakah SO mampu merepresentasikan keputusan bisnis yang dipilih perusahaan?**

---

# TESTING SALES VS ACCOUNTING

Ketika SO menjadi penjualan:

Jangan langsung menganggap:

> “SO = uang masuk.”

Karena bisa terjadi:

**SO dibuat**

↓

**Barang belum dikirim**

↓

**Invoice belum dibuat**

↓

**Customer belum membayar**

atau:

**SO dibuat**

↓

**Customer membayar uang muka**

↓

**Barang belum dikirim**

atau:

**SO dibuat**

↓

**Barang dikirim**

↓

**Invoice dibuat**

↓

**Customer belum membayar**

Accounting harus dapat menerima konsekuensi finansial dari proses tersebut pada titik yang tepat.

---

# TESTING MULTI-CHANNEL SALES

Perusahaan dapat menerima pesanan dari:

* Sales
* POS
* Website
* Marketplace
* Customer Service
* WhatsApp
* Distributor

### Pertanyaan

Apakah semuanya harus menjadi proses yang sama?

Tidak selalu.

Yang diuji:

> Apakah berbagai sumber pesanan dapat tetap menghasilkan informasi penjualan yang konsisten?

---

# TESTING MANAGEMENT VIEW

Owner bertanya:

> “Berapa total order kita?”

> “Berapa yang sudah selesai?”

> “Berapa yang masih outstanding?”

> “Berapa yang sudah dikirim tetapi belum dibayar?”

> “Customer mana yang paling besar?”

> “Produk apa yang paling banyak dipesan?”

> “Berapa nilai order yang dibatalkan?”

> “Berapa nilai order yang terlambat?”

> “Berapa customer yang memiliki tagihan jatuh tempo?”

> “Outlet mana yang menghasilkan order terbesar?”

> “Berapa potensi penjualan yang masih belum selesai?”

Jika pertanyaan tersebut tidak dapat dijawab, cari tahu:

> Informasi apa yang hilang?

---

# FORMAT CATATAN TESTING

Untuk setiap case gunakan:

**Business Case**

Apa yang terjadi?

**Expected Business Result**

Apa yang seharusnya dapat diketahui atau dilakukan perusahaan?

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

**1. Simple Sales**

↓

**2. Quotation → Sales Order**

↓

**3. Customer Approval**

↓

**4. Down Payment**

↓

**5. Fulfillment**

↓

**6. Partial Fulfillment**

↓

**7. Delivery**

↓

**8. Invoice**

↓

**9. Partial Payment**

↓

**10. Return**

↓

**11. Cancellation**

↓

**12. Discount & Special Pricing**

↓

**13. Contract / Legal Requirement**

↓

**14. Service Sales**

↓

**15. Manufacturing / Make to Order**

↓

**16. Multi Outlet**

↓

**17. Multi Channel**

↓

**18. Exception Cases**

↓

**19. Management Questions**

↓

**20. Catat Gap**

↓

**21. Tentukan apakah Gap merupakan Bug, Konfigurasi, Keterbatasan, atau Kebutuhan Bisnis Baru**

---

# CHECKPOINT TERAKHIR

Bayangkan Anda adalah Owner.

Anda bertanya:

> **“Apa saja yang sudah dipesan customer?”**

> **“Mana yang belum kita penuhi?”**

> **“Mana yang sudah dikirim?”**

> **“Mana yang sudah ditagihkan?”**

> **“Mana yang sudah dibayar?”**

> **“Siapa yang belum membayar?”**

> **“Pesanan mana yang terlambat?”**

> **“Kenapa terlambat?”**

> **“Berapa nilai pesanan yang dibatalkan?”**

> **“Berapa potensi penjualan yang masih outstanding?”**

> **“Customer mana yang paling bernilai?”**

Jika pertanyaan tersebut dapat dijawab dengan jelas, maka SO mulai memberikan nilai bisnis yang nyata.

---

# PRINSIP UTAMA SALES ORDER TESTING

Jangan mengejar:

> “Semua Sales Order berhasil dibuat.”

Kejar:

> **“Perusahaan selalu mengetahui apa yang telah dijanjikan kepada customer, apa yang harus dipenuhi, apa yang sudah dipenuhi, apa yang harus ditagihkan, apa yang sudah dibayar, dan apa yang masih menjadi tanggung jawab perusahaan.”**

Sales Order yang matang bukan hanya dokumen pesanan.

Ia merupakan:

> **catatan komitmen perusahaan kepada customer.**

Dan sama seperti Purchase Order:

**Satu perusahaan bukan representasi seluruh dunia bisnis.**

Restaurant, distributor, jasa, manufacturing, retail, multi-outlet, dan perusahaan enterprise dapat memiliki pola penjualan yang berbeda.

Tujuan testing adalah menemukan:

**Pola bisnis umum → kemampuan sistem**

**Pola bisnis berbeda → konfigurasi**

**Pola bisnis khusus → kebutuhan khusus**

Bukan memaksa semua perusahaan mengikuti satu alur.
