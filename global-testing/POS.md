# POS Business Case Testing Guide

## Panduan Pengujian Module POS Berdasarkan Skenario Bisnis

### Tujuan

Dokumen ini digunakan untuk menguji module POS dengan pendekatan bisnis murni.

Jangan mulai dengan pertanyaan:

> “Apakah kasir bisa membuat transaksi?”

Mulailah dengan:

> **“Apakah perusahaan dapat melayani customer, menerima pembayaran, mengelola transaksi, dan mempertanggungjawabkan seluruh uang serta barang yang bergerak melalui POS?”**

POS adalah titik pertemuan antara:

**Customer → Sales → Inventory → Payment → Cashier → Accounting**

Untuk restoran:

**Customer → Order → Kitchen → Inventory → Payment → Revenue**

Karena POS beroperasi secara langsung di hadapan customer, kesalahan kecil dapat langsung menjadi masalah operasional dan finansial.

---

# CARA MENGGUNAKAN PANDUAN INI

Gunakan beberapa jenis bisnis.

Minimal uji:

* Retail
* Restoran
* Cafe
* Minimarket
* Multi-outlet
* Bisnis dengan membership

Jangan menganggap semua POS memiliki pola yang sama.

---

# CASE 1 — PENJUALAN RETAIL SEDERHANA

## Profil

Nama: **Toko Maju**

Customer membeli:

* 2 × Produk A
* 1 × Produk B

Customer membayar tunai.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

* barang yang dibeli?
* jumlah?
* harga?
* discount?
* total?
* jumlah uang diterima?
* kembalian?
* kasir?
* waktu transaksi?

---

# CASE 2 — CUSTOMER TIDAK TERDAFTAR

Customer datang dan langsung membeli.

Customer tidak ingin memberikan identitas.

### Pertanyaan

Apakah transaksi tetap dapat dilakukan?

Tidak semua transaksi retail membutuhkan customer terdaftar.

Yang diuji:

> Apakah POS dapat membedakan transaksi dengan customer terdaftar dan transaksi umum?

---

# CASE 3 — CUSTOMER TERDAFTAR

Customer memiliki akun.

Customer membeli:

Rp1.500.000.

### Pertanyaan

Apakah transaksi dapat dikaitkan dengan customer?

Apakah histori pembelian customer dapat diketahui?

---

# CASE 4 — MULTIPLE PAYMENT

Total:

Rp500.000.

Customer membayar:

Rp200.000 cash

Rp300.000 transfer.

### Pertanyaan

Apakah satu transaksi dapat menggunakan lebih dari satu metode pembayaran?

Apakah total pembayaran tetap:

Rp500.000?

---

# CASE 5 — CUSTOMER MEMBAYAR LEBIH

Total:

Rp95.000.

Customer memberikan:

Rp100.000.

### Pertanyaan

Apakah POS menghitung:

> Kembalian Rp5.000

dengan benar?

---

# CASE 6 — CUSTOMER MEMBAYAR KURANG

Total:

Rp100.000.

Customer hanya memberikan:

Rp90.000.

### Pertanyaan

Apakah transaksi:

* ditolak?
* dianggap belum lunas?
* dapat dilanjutkan?
* menunggu pembayaran tambahan?

Yang diuji adalah bagaimana bisnis menangani pembayaran yang belum mencukupi.

---

# CASE 7 — DISCOUNT PER ITEM

Produk A:

Rp100.000.

Discount:

10%.

Customer membeli:

2 unit.

### Pertanyaan

Apakah kasir dapat mengetahui:

Harga awal

→ Discount

→ Harga setelah discount

→ Total

---

# CASE 8 — DISCOUNT SELURUH TRANSAKSI

Subtotal:

Rp1.000.000.

Discount:

10%.

### Pertanyaan

Apakah hasil transaksi tetap dapat dijelaskan dengan jelas?

---

# CASE 9 — PROMO

Promo:

> Beli 2 gratis 1.

Customer membeli:

6 unit.

### Pertanyaan

Berapa yang dibayar?

Berapa yang diberikan?

Bagaimana inventory terpengaruh?

Apakah customer memahami promo tersebut?

---

# CASE 10 — PROMO BERDASARKAN WAKTU

Promo:

> Discount 20% setiap hari Senin, pukul 14.00–17.00.

Customer datang:

Senin, 16.50.

Transaksi selesai:

17.05.

### Pertanyaan

Promo berlaku berdasarkan:

* waktu transaksi dibuat?
* waktu pembayaran?
* waktu order?

Business rule harus jelas.

---

# CASE 11 — MEMBER DISCOUNT

Customer memiliki membership:

**Gold**

Gold mendapatkan:

10% discount.

Customer membeli:

Rp2.000.000.

### Pertanyaan

Apakah discount otomatis diberikan?

Bagaimana jika membership sudah expired?

---

# CASE 12 — MEMBER TIER

Terdapat:

**Silver**

**Gold**

**Platinum**

Benefit masing-masing berbeda.

### Skenario

Customer sebelumnya Gold.

Kemudian memenuhi syarat Platinum.

### Pertanyaan

Kapan tier berubah?

Apakah transaksi saat ini menggunakan tier lama atau baru?

---

# CASE 13 — POINT / LOYALTY

Customer mendapatkan:

10 point setiap Rp100.000 pembelian.

Customer membeli:

Rp500.000.

### Pertanyaan

Apakah customer mendapatkan:

50 point?

Bagaimana jika transaksi kemudian direfund?

Apakah point dikembalikan?

---

# CASE 14 — PRODUCT RETURN

Customer membeli:

5 unit.

Kemudian mengembalikan:

2 unit.

### Pertanyaan

Apakah:

* transaksi awal tetap tercatat?
* retur tercatat?
* inventory bertambah kembali?
* uang customer dikembalikan?

---

# CASE 15 — REFUND SEBAGIAN

Total transaksi:

Rp500.000.

Customer meminta refund:

Rp100.000.

### Pertanyaan

Apakah transaksi dapat menunjukkan:

Original:

Rp500.000

Refund:

Rp100.000

Net:

Rp400.000

---

# CASE 16 — FULL REFUND

Customer membeli:

Rp1.000.000.

Seluruh barang dikembalikan.

### Pertanyaan

Apakah transaksi dapat dianggap:

> Fully refunded

tanpa menghapus histori transaksi awal?

Histori transaksi seharusnya tetap dapat ditelusuri.

---

# CASE 17 — SALAH HARGA

Kasir memasukkan harga:

Rp150.000.

Seharusnya:

Rp100.000.

### Pertanyaan

Apakah kasir boleh mengubah harga?

Jika boleh:

Apakah perlu alasan?

Apakah perlu persetujuan?

Apakah perubahan dapat dilacak?

---

# CASE 18 — SALAH PRODUK

Kasir memasukkan:

Produk A.

Customer sebenarnya membeli:

Produk B.

### Pertanyaan

Apakah item dapat dihapus sebelum pembayaran?

Bagaimana setelah pembayaran?

---

# CASE 19 — VOID TRANSACTION

Kasir membuat transaksi tetapi customer batal sebelum membayar.

### Pertanyaan

Apakah transaksi:

* dihapus?
* dibatalkan?
* tetap memiliki histori?

Apa alasan pembatalannya?

---

# CASE 20 — VOID SETELAH PEMBAYARAN

Customer sudah membayar.

Kasir kemudian menyadari ada kesalahan.

### Pertanyaan

Apakah transaksi dapat di-void?

Siapa yang berhak?

Apakah perlu approval?

Bagaimana uang customer diperlakukan?

---

# CASE 21 — CUSTOMER MENGUBAH PESANAN

Customer awalnya:

2 kopi.

Kemudian:

> “Tambah 1 kopi dan 2 cake.”

### Pertanyaan

Apakah order dapat berubah sebelum pembayaran?

Apakah total otomatis berubah?

---

# CASE 22 — RESTORAN: DINE-IN

Customer datang.

Memesan:

* 2 nasi goreng
* 3 minuman

Customer duduk di:

**Table 12**

### Pertanyaan

Apakah POS mengetahui:

* meja?
* order?
* item?
* jumlah?
* status pesanan?

---

# CASE 23 — RESTORAN: ORDER BELUM DIBAYAR

Customer sudah makan tetapi belum membayar.

### Pertanyaan

Apakah order:

> masih terbuka?

Dan bukan dianggap sebagai transaksi selesai?

---

# CASE 24 — RESTORAN: TAMBAH ORDER

Customer sudah memesan:

2 nasi goreng.

Kemudian menambahkan:

2 es teh.

Kemudian:

1 dessert.

### Pertanyaan

Apakah seluruh pesanan dapat tetap dikelola sebagai satu pengalaman customer?

---

# CASE 25 — RESTORAN: SPLIT BILL

Total meja:

Rp600.000.

Customer terdiri dari:

3 orang.

Mereka ingin membayar:

Customer A:

Rp200.000

Customer B:

Rp250.000

Customer C:

Rp150.000

### Pertanyaan

Apakah satu order dapat dibagi menjadi beberapa pembayaran?

---

# CASE 26 — RESTORAN: SPLIT ITEM

Total:

Rp600.000.

Customer A membayar:

2 nasi.

Customer B membayar:

3 minuman.

### Pertanyaan

Apakah pembayaran dapat berdasarkan item?

---

# CASE 27 — RESTORAN: MERGE TABLE

Meja 5:

4 customer.

Meja 6:

3 customer.

Mereka memutuskan bergabung.

### Pertanyaan

Apakah dua order dapat digabung?

---

# CASE 28 — RESTORAN: TRANSFER TABLE

Customer berpindah:

Table 5 → Table 8.

### Pertanyaan

Apakah order ikut berpindah?

Apakah histori tetap benar?

---

# CASE 29 — RESTORAN: CUSTOMER MENINGGALKAN MEJA

Customer pergi tanpa membayar.

### Pertanyaan

Bagaimana status order?

Apakah langsung dianggap sebagai revenue?

Apakah perlu ditandai sebagai:

> unpaid / loss / unresolved?

---

# CASE 30 — KITCHEN ORDER

Restoran memiliki dapur.

Customer memesan:

* nasi goreng
* steak
* jus

### Pertanyaan

Apakah dapur perlu mengetahui:

> Apa yang harus dibuat?

Apakah status pesanan dapat diketahui:

**Ordered**

→ **Preparing**

→ **Ready**

→ **Served**

---

# CASE 31 — ITEM DAPUR BERBEDA DENGAN ITEM POS

Customer membeli:

**Nasi Ayam**

Tetapi dapur membutuhkan:

* nasi
* ayam
* sambal

### Pertanyaan

Apakah POS dapat berhubungan dengan kebutuhan inventory tanpa membuat kasir harus memahami bahan baku?

---

# CASE 32 — MENU HABIS

Customer memesan:

> Steak.

Tetapi steak sudah habis.

### Pertanyaan

Apakah kasir dapat mengetahui bahwa item tidak tersedia?

Bagaimana jika customer sudah terlanjur memasukkannya ke order?

---

# CASE 33 — MODIFIER

Customer membeli:

> Kopi

Tetapi memilih:

* less sugar
* extra ice
* extra shot

### Pertanyaan

Apakah pilihan customer dapat dicatat?

Apakah tambahan tersebut dapat mempengaruhi harga?

---

# CASE 34 — TAKEAWAY

Customer memesan makanan untuk dibawa pulang.

### Pertanyaan

Apakah transaksi dapat dibedakan dari:

> Dine-in

dan:

> Delivery?

---

# CASE 35 — DELIVERY

Customer memesan melalui restoran untuk dikirim.

### Pertanyaan

Apakah POS dapat mengetahui:

* alamat?
* customer?
* order?
* biaya delivery?
* status pengiriman?

---

# CASE 36 — ORDER TYPE

Restoran memiliki:

* Dine-in
* Takeaway
* Delivery
* Pickup

### Pertanyaan

Apakah perusahaan dapat mengetahui penjualan berdasarkan jenis order?

---

# CASE 37 — SHIFT KASIR

Kasir A mulai bekerja.

Modal kas:

Rp500.000.

Selama shift:

Penjualan cash:

Rp3.000.000.

### Pertanyaan

Berapa uang yang seharusnya ada?

Rp3.500.000.

---

# CASE 38 — CASH OUT

Kasir mengeluarkan:

Rp200.000

untuk membeli kebutuhan operasional.

### Pertanyaan

Apakah uang cash di laci berubah?

Apakah alasan pengeluaran tercatat?

---

# CASE 39 — CASH IN

Kasir menerima:

Rp100.000

untuk kebutuhan tertentu.

### Pertanyaan

Apakah cash drawer berubah?

Apakah sumber uang tersebut dapat diketahui?

---

# CASE 40 — CLOSING SHIFT

Expected cash:

Rp3.400.000.

Actual cash:

Rp3.350.000.

Selisih:

Rp50.000.

### Pertanyaan

Apakah sistem dapat mengetahui selisih?

Apakah kasir harus memberikan alasan?

Apakah manager dapat melakukan pemeriksaan?

---

# CASE 41 — CASH SURPLUS

Expected:

Rp3.400.000.

Actual:

Rp3.450.000.

Selisih:

Rp50.000.

### Pertanyaan

Apakah kelebihan juga dicatat?

Jangan hanya menguji kekurangan kas.

---

# CASE 42 — PAYMENT FAILURE

Customer membayar menggunakan metode tertentu.

Pembayaran gagal.

### Pertanyaan

Apakah transaksi:

* dianggap belum dibayar?
* tetap terbuka?
* boleh menggunakan metode pembayaran lain?

Jangan sampai:

> uang belum diterima tetapi transaksi dianggap lunas.

---

# CASE 43 — DOUBLE PAYMENT

Customer membayar.

Kemudian terjadi masalah dan customer membayar lagi.

### Pertanyaan

Bagaimana perusahaan mengetahui adanya pembayaran berlebih?

---

# CASE 44 — REFUND MELALUI METODE BERBEDA

Customer awalnya membayar:

**Cash**

Kemudian meminta refund:

**Transfer**

### Pertanyaan

Apakah perusahaan mengizinkan?

Jika iya, bagaimana histori pembayaran tetap dapat dijelaskan?

---

# CASE 45 — PRICE CHANGE

Harga Produk A:

Rp100.000.

Management mengubah menjadi:

Rp110.000.

Customer sebelumnya sudah mendapatkan harga:

Rp100.000.

### Pertanyaan

Transaksi customer lama menggunakan harga mana?

Transaksi baru menggunakan harga mana?

---

# CASE 46 — PROMO BERTUMPUK

Customer memiliki:

* member discount 10%
* promo produk 20%

### Pertanyaan

Apakah keduanya boleh digunakan?

Jika tidak:

> Mana yang diprioritaskan?

---

# CASE 47 — MANUAL DISCOUNT

Kasir memberikan discount:

20%.

Padahal hak normalnya hanya:

10%.

### Pertanyaan

Apakah diperbolehkan?

Apakah membutuhkan approval?

Apakah alasan wajib?

---

# CASE 48 — CUSTOMER COMPLAINT

Customer mengatakan:

> “Harga di rak Rp90.000, tapi di kasir Rp100.000.”

### Pertanyaan

Harga mana yang digunakan?

Apakah kasir dapat melakukan koreksi?

Apakah management dapat melihat kejadian tersebut?

---

# CASE 49 — MULTI OUTLET

Perusahaan memiliki:

Outlet A

Outlet B

Outlet C

Customer berbelanja di Outlet A.

### Pertanyaan

Apakah transaksi dapat diketahui berasal dari outlet mana?

Apakah inventory outlet A yang berkurang?

Apakah revenue outlet A yang bertambah?

---

# CASE 50 — CUSTOMER MEMBELI DI OUTLET BERBEDA

Customer membeli di:

Outlet A.

Kemudian melakukan retur di:

Outlet B.

### Pertanyaan

Apakah perusahaan mengizinkan?

Jika iya, bagaimana outlet B mengetahui transaksi awal?

---

# CASE 51 — POS OFFLINE

Internet outlet terputus.

Customer tetap ingin membayar.

### Pertanyaan

Apakah operasional dapat tetap berjalan?

Jika iya:

> Bagaimana transaksi yang dibuat selama kondisi tersebut dipertanggungjawabkan?

Yang diuji bukan teknologinya.

Yang diuji:

> **Apakah bisnis memiliki cara untuk tetap beroperasi ketika sistem utama tidak dapat digunakan secara normal?**

---

# CASE 52 — POS TIDAK DAPAT DIGUNAKAN

POS mengalami gangguan.

Customer tetap antre.

### Pertanyaan

Apa prosedur bisnis perusahaan?

Apakah:

* transaksi ditunda?
* pencatatan manual?
* menggunakan POS lain?
* customer diminta menunggu?

Tidak ada jawaban universal.

Yang penting:

> **Prosedur bisnis harus dapat dipahami dan dipertanggungjawabkan.**

---

# CASE 53 — STOCK TIDAK CUKUP

Customer ingin membeli:

100 unit.

Stock tersedia:

80.

### Pertanyaan

Apakah POS:

* menolak?
* menjual 80?
* membuat backorder?
* memungkinkan stock negatif?

Kebijakan harus jelas.

---

# CASE 54 — PRODUCT RETURN TANPA RECEIPT

Customer membawa barang.

Mengatakan:

> “Saya beli di sini minggu lalu.”

Tetapi tidak memiliki bukti transaksi.

### Pertanyaan

Apakah retur diperbolehkan?

Jika iya:

> Bagaimana perusahaan memverifikasi pembelian?

---

# CASE 55 — CUSTOMER MEMINTA RECEIPT ULANG

Customer kehilangan bukti transaksi.

### Pertanyaan

Apakah transaksi lama dapat ditemukan?

Berdasarkan:

* tanggal
* customer
* nomor transaksi
* item
* metode pembayaran

---

# CASE 56 — TRANSACTION HISTORY

Management ingin melihat:

> Semua transaksi kasir hari ini.

### Pertanyaan

Apakah dapat diketahui:

* siapa kasir?
* kapan?
* outlet?
* total?
* metode pembayaran?
* discount?
* refund?
* void?

---

# CASE 57 — CASHIER PERFORMANCE

Management ingin mengetahui:

> “Kasir mana yang melakukan transaksi paling banyak?”

Kemudian:

> “Kasir mana yang paling banyak melakukan void?”

Kemudian:

> “Kasir mana yang paling banyak memberikan manual discount?”

### Pertanyaan

Apakah informasi tersebut tersedia?

---

# CASE 58 — SUSPICIOUS TRANSACTION

Kasir melakukan:

* banyak void
* banyak discount manual
* banyak refund

### Pertanyaan

Apakah management dapat melihat pola tersebut?

POS bukan hanya alat transaksi.

POS juga merupakan alat kontrol.

---

# CASE 59 — DAILY CLOSING

Outlet selesai beroperasi.

Management ingin mengetahui:

### Sales

Rp20.000.000

### Cash

Rp8.000.000

### Card

Rp7.000.000

### Transfer

Rp5.000.000

### Refund

Rp500.000

### Discount

Rp1.000.000

### Pertanyaan

Apakah laporan akhir hari dapat menjelaskan bagaimana angka tersebut terbentuk?

---

# CASE 60 — MANAGEMENT QUESTION

Owner bertanya:

> “Berapa penjualan hari ini?”

↓

Apakah dapat dijawab?

---

> “Berapa penjualan cash?”

↓

---

> “Berapa penjualan non-cash?”

↓

---

> “Berapa refund?”

↓

---

> “Berapa discount?”

↓

---

> “Berapa transaksi?”

↓

---

> “Produk apa yang paling laku?”

↓

---

> “Jam berapa outlet paling ramai?”

↓

---

> “Kasir mana yang paling banyak melakukan transaksi?”

↓

---

> “Outlet mana yang paling tinggi penjualannya?”

↓

---

> “Berapa uang yang seharusnya ada?”

↓

---

> “Berapa uang yang benar-benar ada?”

↓

---

> “Berapa selisihnya?”

↓

Jika semua dapat dijawab:

> POS mulai memberikan informasi bisnis, bukan sekadar menjadi mesin kasir.

---

# TESTING POS LIFECYCLE

Lakukan satu perjalanan lengkap:

**Customer datang**

↓

**Customer memilih barang/menu**

↓

**Order dibuat**

↓

**Harga dihitung**

↓

**Discount/promo diterapkan**

↓

**Customer mengonfirmasi**

↓

**Barang/menu disiapkan**

↓

**Customer menerima barang/menu**

↓

**Customer membayar**

↓

**Transaksi selesai**

↓

**Inventory berubah**

↓

**Revenue tercatat**

↓

**Cash/payment tercatat**

↓

**Shift ditutup**

↓

**Cash dihitung**

↓

**Management melihat hasil penjualan**

---

# TESTING RESTAURANT LIFECYCLE

Untuk POS + Resto:

**Customer datang**

↓

**Table dipilih**

↓

**Order dibuat**

↓

**Menu dipilih**

↓

**Modifier ditentukan**

↓

**Order dikirim ke dapur**

↓

**Kitchen menyiapkan**

↓

**Menu selesai**

↓

**Menu disajikan**

↓

**Customer menambah order**

↓

**Customer meminta bill**

↓

**Bill dihitung**

↓

**Split bill jika diperlukan**

↓

**Payment**

↓

**Table ditutup**

↓

**Inventory berkurang**

↓

**Sales tercatat**

↓

**Shift kasir diperbarui**

---

# TESTING PAYMENT

Jangan hanya menguji:

> “Payment berhasil.”

Uji:

### Cash

### Card

### Bank Transfer

### QR Payment

### E-wallet

### Multiple Payment

### Partial Payment

### Refund

### Failed Payment

### Overpayment

### Underpayment

### Payment Reversal

Pertanyaan utamanya:

> **Apakah status transaksi dan status uang selalu konsisten?**

---

# TESTING INVENTORY

Setiap transaksi POS yang menjual barang harus dapat menjawab:

> Apa yang keluar?

> Berapa jumlahnya?

> Dari lokasi mana?

> Kapan keluar?

> Kenapa keluar?

Untuk restoran, tambahkan:

> Bahan apa yang digunakan?

---

# TESTING CUSTOMER

Uji:

* Walk-in customer
* Registered customer
* Member
* Member expired
* Customer dengan harga khusus
* Customer dengan discount
* Customer dengan point
* Customer melakukan retur

---

# TESTING CONTROL

POS adalah area yang membutuhkan kontrol kuat.

Uji:

### Void

### Refund

### Manual Discount

### Price Override

### Cash In

### Cash Out

### Reprint Receipt

### Reopen Transaction

### Cancel Order

### Change Payment

Untuk masing-masing:

> Siapa yang boleh?

> Apakah perlu alasan?

> Apakah perlu approval?

> Apakah histori tetap ada?

---

# TESTING “TRANSACTION ≠ PAYMENT”

Ini wajib diuji.

Contoh:

Transaksi:

Rp1.000.000

Payment:

Rp500.000

Maka:

**Transaction Total = Rp1.000.000**

**Paid = Rp500.000**

**Outstanding = Rp500.000**

Jangan membuat:

> Transaction selesai hanya karena sebagian pembayaran masuk.

---

# TESTING “TRANSACTION ≠ CASH”

Transaksi:

Rp1.000.000.

Pembayaran:

* Cash Rp300.000
* Card Rp700.000

Cash drawer hanya bertambah:

Rp300.000.

Bukan:

Rp1.000.000.

---

# TESTING “SALES ≠ PROFIT”

POS menghasilkan penjualan.

Tetapi:

> Sales ≠ Profit.

Contoh:

Penjualan:

Rp1.000.000

Harga barang:

Rp700.000

Gross profit:

Rp300.000

Jangan menjadikan angka penjualan sebagai keuntungan perusahaan.

---

# TESTING EXCEPTION

Setelah seluruh happy path selesai, sengaja buat kondisi buruk:

### Customer membatalkan order.

### Customer mengubah order.

### Barang habis.

### Harga salah.

### Discount salah.

### Promo bertabrakan.

### Pembayaran gagal.

### Customer membayar kurang.

### Customer membayar lebih.

### Refund.

### Partial refund.

### Void.

### Salah item.

### Salah jumlah.

### Kasir salah memberikan kembalian.

### Cash drawer selisih.

### Customer tidak membayar.

### Transaksi dilakukan dua kali.

### Internet terputus.

### POS tidak dapat digunakan.

### Customer meminta retur tanpa receipt.

### Customer retur di outlet berbeda.

### Harga berubah ketika customer sedang bertransaksi.

### Member berubah tier.

### Point harus dibatalkan karena refund.

---

# TESTING CROSS-MODULE

Setelah POS selesai diuji sendiri, lakukan pengujian dengan module lain.

## POS → INVENTORY

Penjualan:

10 unit.

Inventory:

-10 unit.

---

## POS → RESTAURANT

Penjualan:

10 menu.

Inventory bahan:

berubah sesuai kebutuhan menu.

---

## POS → SALES

Jika bisnis menggunakan POS sebagai transaksi penjualan langsung:

POS harus dapat menjadi sumber informasi penjualan.

---

## POS → CUSTOMER

Transaksi customer harus dapat membentuk histori customer.

---

## POS → PAYMENT

Payment harus sesuai dengan nilai transaksi.

---

## POS → ACCOUNTING

Revenue, payment, refund, discount, dan kondisi finansial lainnya harus dapat diteruskan ke Accounting sesuai kebijakan perusahaan.

---

# TESTING MULTI-OUTLET

Uji:

**Outlet A**

↓

Transaksi

↓

Inventory A berubah

↓

Cash A berubah

↓

Revenue A bertambah

Kemudian:

**Outlet B**

↓

Transaksi

↓

Inventory B berubah

↓

Cash B berubah

↓

Revenue B bertambah

Management harus dapat melihat:

> masing-masing outlet

dan:

> total perusahaan.

---

# FORMAT CATATAN TESTING

Untuk setiap case gunakan:

**Business Case**

Apa yang terjadi?

**Expected Business Result**

Apa yang seharusnya terjadi?

**Actual Result**

Apa yang terjadi pada aplikasi?

**Gap**

Apa yang belum dapat direpresentasikan?

**Business Impact**

Apa dampaknya?

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

**1. Basic Sale**

↓

**2. Cash Payment**

↓

**3. Non-Cash Payment**

↓

**4. Multiple Payment**

↓

**5. Discount**

↓

**6. Promo**

↓

**7. Member**

↓

**8. Loyalty**

↓

**9. Refund**

↓

**10. Void**

↓

**11. Price Override**

↓

**12. Cash In / Cash Out**

↓

**13. Shift**

↓

**14. Closing**

↓

**15. Stock Integration**

↓

**16. Restaurant Order**

↓

**17. Kitchen**

↓

**18. Table Management**

↓

**19. Split Bill**

↓

**20. Merge / Transfer Table**

↓

**21. Takeaway**

↓

**22. Delivery**

↓

**23. Multi Outlet**

↓

**24. Offline / Failure Cases**

↓

**25. Exception Cases**

↓

**26. Management Questions**

↓

**27. Cross-module Testing**

↓

**28. Catat Gap**

↓

**29. Tentukan apakah Gap merupakan Bug, Konfigurasi, Keterbatasan, atau Kebutuhan Bisnis Baru**

---

# CHECKPOINT TERAKHIR

Bayangkan Anda adalah Owner restoran/retail.

Anda bertanya:

> **“Berapa penjualan hari ini?”**

> **“Uangnya masuk melalui apa?”**

> **“Berapa uang cash yang seharusnya ada?”**

> **“Kenapa cash aktual berbeda?”**

> **“Berapa transaksi yang dibatalkan?”**

> **“Berapa refund?”**

> **“Berapa discount?”**

> **“Kasir mana yang paling banyak melakukan void?”**

> **“Produk apa yang paling laku?”**

> **“Barang apa yang sudah terjual?”**

> **“Apakah stock sudah berkurang?”**

Untuk restoran:

> **“Meja mana yang masih open?”**

> **“Order mana yang belum dibayar?”**

> **“Order mana yang masih diproses dapur?”**

> **“Berapa penjualan dine-in?”**

> **“Berapa takeaway?”**

> **“Berapa delivery?”**

Jika pertanyaan tersebut dapat dijawab dengan jelas:

> **POS mulai menjadi pusat operasional penjualan.**

---

# PRINSIP UTAMA POS TESTING

Jangan mengejar:

> “Kasir bisa melakukan transaksi.”

Kejar:

> **“Setiap transaksi customer dapat dipertanggungjawabkan dari awal sampai akhir, termasuk barang yang dijual, harga yang diberikan, discount, pembayaran, uang yang diterima, perubahan transaksi, refund, dan dampaknya terhadap bisnis.”**

POS yang matang bukan sekadar:

> **Cash Register.**

POS adalah:

> **titik tempat aktivitas penjualan benar-benar terjadi.**

Dan karena itu POS harus mampu menjembatani:

**Customer**

↓

**Order**

↓

**Product / Menu**

↓

**Inventory**

↓

**Payment**

↓

**Revenue**

↓

**Accounting**

↓

**Management**

---

# PRINSIP PENUTUP

Ketika testing POS selesai, jangan langsung berkata:

> “POS sudah bagus karena transaksi berhasil.”

Tanyakan:

> **“Kalau saya menjadi kasir selama 10 jam dalam kondisi ramai, apakah saya dapat bekerja tanpa kebingungan?”**

Kemudian:

> **“Kalau saya menjadi supervisor, apakah saya dapat mengontrol aktivitas kasir?”**

Kemudian:

> **“Kalau saya menjadi owner, apakah saya percaya terhadap angka penjualan dan uang yang dilaporkan?”**

Kemudian:

> **“Kalau terjadi masalah, apakah saya dapat mengetahui apa yang sebenarnya terjadi?”**

Kalau keempat pertanyaan tersebut dapat dijawab **ya**, barulah POS mulai layak dianggap matang.

Karena pada akhirnya:

> **POS bukan tentang membuat transaksi.**

> **POS adalah tentang membuat transaksi yang terjadi di dunia nyata dapat dicatat, dikontrol, dipertanggungjawabkan, dan diterjemahkan menjadi informasi bisnis.**
