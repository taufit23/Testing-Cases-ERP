# Restaurant Business Case Testing Guide

## Panduan Pengujian Module Restaurant Berdasarkan Skenario Bisnis

### Tujuan

Dokumen ini digunakan untuk menguji Restaurant Module dengan pendekatan bisnis murni.

Jangan mulai dengan:

> “Apakah waiter bisa membuat order?”

Mulailah dengan:

> **“Apakah sebuah restoran dapat menjalankan seluruh kegiatan operasionalnya melalui sistem, dari customer datang sampai restoran melakukan closing?”**

Restaurant Module harus mampu menggambarkan kondisi nyata restoran:

**Customer**

→ **Table**

→ **Reservation / Walk-in**

→ **Order**

→ **Kitchen**

→ **Food Preparation**

→ **Serving**

→ **Payment**

→ **Inventory**

→ **Closing**

Untuk restoran yang lebih kompleks, tambahkan:

**Recipe**

**Modifier**

**Ingredient**

**Waste**

**Shift**

**Outlet**

**Delivery**

**Takeaway**

**Membership**

---

# CARA MENGGUNAKAN PANDUAN

Jangan hanya menggunakan satu tipe restoran.

Bandingkan beberapa pola:

* Warung sederhana
* Cafe
* Casual dining
* Fine dining
* Food court
* Restaurant keluarga
* Restaurant multi-outlet
* Restaurant dengan delivery
* Restaurant dengan reservasi

Tujuannya bukan membuat semua restoran mengikuti pola yang sama.

Tujuannya adalah mencari:

**Pola umum → sistem harus mendukung**

**Pola berbeda → konfigurasi**

**Pola khusus → kebutuhan tambahan**

---

# CASE 1 — RESTORAN BARU BUKA

## Profil

Restaurant:

**Saji Rasa**

Memiliki:

* 20 meja
* 3 waiter
* 4 kitchen staff
* 2 cashier
* 1 supervisor

Restoran buka:

**10.00**

### Pertanyaan

Sebelum customer datang:

* Apakah meja memiliki status?
* Apakah kitchen siap menerima order?
* Apakah menu tersedia?
* Apakah item yang habis diketahui?
* Siapa yang bertugas?
* Shift apa yang sedang berjalan?

---

# CASE 2 — WALK-IN CUSTOMER

Customer datang tanpa reservasi.

Jumlah:

4 orang.

Waiter mencari meja kosong.

### Pertanyaan

Apakah waiter dapat mengetahui:

> Meja mana yang tersedia?

Kemudian customer ditempatkan di:

**Table 8**

### Pertanyaan

Apakah status meja berubah menjadi:

> Occupied

?

---

# CASE 3 — RESERVATION

Customer melakukan reservasi:

**Table 10**

Pukul:

19.00

Jumlah:

6 orang.

### Pertanyaan

Apakah restoran dapat mengetahui:

* nama customer?
* jumlah orang?
* waktu?
* meja?
* status reservasi?

---

# CASE 4 — CUSTOMER DATANG TERLAMBAT

Reservasi:

19.00

Customer baru datang:

19.40.

### Pertanyaan

Apa yang dilakukan restoran?

Kemungkinan:

* tetap mempertahankan meja
* memberikan grace period
* membatalkan reservasi
* memberikan meja lain

Tidak ada satu jawaban universal.

Yang diuji:

> **Apakah kebijakan reservasi restoran dapat dijalankan?**

---

# CASE 5 — CUSTOMER TIDAK DATANG

Customer reservasi:

Table 10.

Tetapi tidak datang.

### Pertanyaan

Apakah reservation dapat ditandai:

> No-show

?

Apakah meja kembali tersedia?

---

# CASE 6 — TABLE STATUS

Gunakan beberapa meja:

Table 1:

Available

Table 2:

Occupied

Table 3:

Reserved

Table 4:

Cleaning

Table 5:

Out of Service

### Pertanyaan

Apakah restaurant dapat membedakan seluruh kondisi tersebut?

Jangan hanya:

> Available / Occupied.

---

# CASE 7 — CUSTOMER PINDAH MEJA

Customer berada di:

Table 5.

Kemudian meminta:

> “Boleh pindah ke Table 8?”

### Pertanyaan

Apakah order ikut berpindah?

Apakah Table 5 kembali tersedia?

Apakah histori tetap benar?

---

# CASE 8 — MERGE TABLE

Customer datang:

7 orang.

Table 5:

4 kursi.

Table 6:

4 kursi.

Kedua meja digabung.

### Pertanyaan

Apakah restaurant dapat menganggap:

Table 5 + Table 6

sebagai satu area customer?

---

# CASE 9 — SPLIT TABLE

Customer awalnya duduk bersama.

Kemudian:

3 orang ingin pindah.

### Pertanyaan

Apakah order dapat dipisahkan?

---

# CASE 10 — CUSTOMER DATANG DENGAN JUMLAH BERUBAH

Reservasi:

4 orang.

Customer datang:

7 orang.

### Pertanyaan

Apakah restoran dapat menyesuaikan meja?

Apakah reservasi tetap valid?

---

# CASE 11 — ORDER PERTAMA

Customer di Table 8 memesan:

* 2 Nasi Goreng
* 1 Mie Goreng
* 3 Es Teh

### Pertanyaan

Apakah order dapat dicatat?

Apakah waiter dapat mengetahui order tersebut milik Table 8?

---

# CASE 12 — CUSTOMER MENAMBAH ORDER

Setelah 20 menit:

> “Tambah 2 kopi.”

Kemudian:

> “Tambah 1 dessert.”

### Pertanyaan

Apakah order lama dan tambahan order dapat dikelola dengan baik?

---

# CASE 13 — CUSTOMER MEMBATALKAN ITEM

Customer awalnya:

2 Nasi Goreng.

Kemudian membatalkan:

1.

### Pertanyaan

Jika makanan belum dibuat:

> Apakah item dapat dibatalkan?

Jika sudah dibuat:

> Apakah prosesnya berbeda?

---

# CASE 14 — ITEM SUDAH DIPROSES KITCHEN

Customer memesan:

Steak.

Kitchen sudah mulai memasak.

Customer kemudian membatalkan.

### Pertanyaan

Apakah restoran mencatat:

> Customer cancel

?

Apakah makanan menjadi:

> Waste?

Atau:

> Dapat diberikan kepada customer lain?

Business policy harus jelas.

---

# CASE 15 — MODIFIER

Customer memesan:

**Nasi Goreng**

dengan:

* tidak pedas
* telur mata sapi
* extra ayam

### Pertanyaan

Apakah waiter dapat mencatat permintaan tersebut?

Apakah kitchen dapat melihatnya?

Apakah extra item mempengaruhi harga?

---

# CASE 16 — MODIFIER TANPA TAMBAHAN HARGA

Customer:

> “Tidak pakai bawang.”

### Pertanyaan

Apakah restoran dapat mencatat permintaan khusus tanpa mengubah harga?

---

# CASE 17 — MENU HABIS

Customer memesan:

**Sup Iga**

Tetapi kitchen kehabisan bahan.

### Pertanyaan

Bagaimana restaurant menangani?

Apakah menu dapat ditandai:

> Unavailable

?

Apakah waiter mengetahui kondisi tersebut?

---

# CASE 18 — INGREDIENT HABIS

Menu:

**Ayam Bakar**

Stock ayam:

0.

### Pertanyaan

Apakah restaurant dapat mengetahui bahwa menu tertentu terdampak?

---

# CASE 19 — KITCHEN ORDER

Order:

* 2 nasi goreng
* 1 steak
* 3 es teh

Kitchen menerima order.

### Pertanyaan

Apakah kitchen mengetahui:

* order number?
* table?
* item?
* quantity?
* modifier?
* catatan?

---

# CASE 20 — KITCHEN STATUS

Setelah order diterima:

**New**

→ **Preparing**

→ **Ready**

→ **Served**

### Pertanyaan

Apakah waiter dapat mengetahui kapan makanan siap?

---

# CASE 21 — PARTIAL READY

Order:

* nasi goreng → Ready
* steak → Preparing
* es teh → Ready

### Pertanyaan

Apakah waiter dapat melihat bahwa order belum sepenuhnya selesai?

---

# CASE 22 — KITCHEN DELAY

Customer sudah menunggu:

30 menit.

Steak belum selesai.

### Pertanyaan

Apakah restaurant dapat mengetahui order yang terlambat?

---

# CASE 23 — ORDER PRIORITY

VIP customer datang.

Customer biasa juga sedang menunggu.

### Pertanyaan

Apakah kitchen memiliki kebijakan mengenai prioritas order?

Jika iya:

> Apakah sistem dapat merepresentasikannya?

---

# CASE 24 — WRONG ORDER

Kitchen membuat:

Nasi Goreng 2.

Seharusnya:

Nasi Goreng 1.

### Pertanyaan

Apa yang terjadi?

Apakah harus:

* dibuat ulang?
* dibatalkan?
* menjadi waste?
* tetap diberikan?

---

# CASE 25 — FOOD WASTE

Kitchen salah memasak:

3 porsi.

Tidak dapat digunakan lagi.

### Pertanyaan

Apakah restaurant mencatat:

> 3 porsi waste?

Apakah inventory bahan ikut diperhitungkan?

---

# CASE 26 — SPOILED INGREDIENT

Kitchen menemukan:

10 kg ayam rusak.

### Pertanyaan

Apakah restaurant dapat mencatat:

* quantity?
* alasan?
* tanggal?
* lokasi?
* siapa yang menemukan?

---

# CASE 27 — RECIPE

Menu:

**Nasi Goreng Ayam**

Membutuhkan:

* 150g beras
* 100g ayam
* 20g minyak
* 10g bumbu

Customer membeli:

10 porsi.

### Pertanyaan

Apa yang seharusnya terjadi terhadap inventory bahan?

---

# CASE 28 — RECIPE CHANGE

Recipe sebelumnya:

100g ayam.

Management mengubah menjadi:

120g ayam.

### Pertanyaan

Mulai kapan recipe baru berlaku?

Apakah order lama menggunakan recipe lama?

---

# CASE 29 — PORTION SIZE

Restaurant menjual:

Small

Medium

Large

### Pertanyaan

Apakah masing-masing memiliki:

* harga berbeda?
* kebutuhan bahan berbeda?
* ukuran berbeda?

---

# CASE 30 — MENU COMBO

Restaurant menjual:

**Family Package**

Isi:

* 4 nasi
* 4 ayam
* 4 minuman

Customer membeli:

2 package.

### Pertanyaan

Apakah inventory mengetahui kebutuhan bahan/menu di dalam package?

---

# CASE 31 — TAKEAWAY

Customer memesan:

3 makanan.

Tetapi tidak makan di restaurant.

### Pertanyaan

Apakah order type menjadi:

> Takeaway

?

Apakah biaya atau packaging berbeda?

---

# CASE 32 — DELIVERY

Customer memesan untuk dikirim.

### Pertanyaan

Apakah restaurant mengetahui:

* customer?
* alamat?
* nomor kontak?
* order?
* biaya delivery?
* status order?

---

# CASE 33 — DELIVERY STATUS

Order:

**Confirmed**

→ **Preparing**

→ **Ready**

→ **Picked Up**

→ **Delivered**

### Pertanyaan

Apakah restaurant dapat mengetahui status order?

---

# CASE 34 — DELIVERY PARTNER

Restaurant menerima order dari pihak delivery.

### Pertanyaan

Bagaimana restaurant mengetahui:

> Order berasal dari channel mana?

Misalnya:

* Direct
* Delivery Partner A
* Delivery Partner B
* Marketplace

---

# CASE 35 — CUSTOMER REQUEST

Customer mengatakan:

> “Saya alergi kacang.”

### Pertanyaan

Apakah waiter dapat memberikan catatan khusus?

Apakah informasi tersebut sampai ke kitchen?

---

# CASE 36 — CUSTOMER COMPLAINT

Customer menerima makanan yang salah.

### Pertanyaan

Apakah restaurant dapat mengetahui:

* order asli?
* item yang salah?
* siapa waiter?
* waktu order?
* kitchen yang mengerjakan?

---

# CASE 37 — FREE ITEM / COMPLIMENTARY

Manager memberikan:

> 1 dessert gratis.

### Pertanyaan

Apakah item tersebut:

* tetap tercatat?
* dianggap discount?
* complimentary?
* mempengaruhi inventory?

---

# CASE 38 — MANAGER DISCOUNT

Total:

Rp1.000.000.

Manager memberikan discount:

Rp100.000.

### Pertanyaan

Apakah pemberian discount dapat dilacak?

---

# CASE 39 — SERVICE CHARGE

Restaurant menerapkan:

**Service Charge 5%**

### Pertanyaan

Apakah service charge:

* dihitung otomatis?
* dapat berbeda berdasarkan order type?
* dapat dikecualikan?

---

# CASE 40 — TAX

Restaurant menerapkan pajak sesuai kebijakan bisnis.

### Pertanyaan

Apakah perhitungan:

Subtotal

→ Discount

→ Service Charge

→ Tax

→ Grand Total

dapat dijelaskan?

Urutan perhitungan harus konsisten dengan kebijakan restaurant.

---

# CASE 41 — SPLIT BILL

Table 10:

Rp900.000.

Customer:

3 orang.

Pembayaran:

Customer A:

Rp300.000

Customer B:

Rp350.000

Customer C:

Rp250.000

### Pertanyaan

Apakah bill dapat dibagi?

---

# CASE 42 — SPLIT ITEM

Customer A:

2 makanan.

Customer B:

3 minuman.

### Pertanyaan

Apakah bill dapat dibagi berdasarkan item?

---

# CASE 43 — COMBINE BILL

Dua table ingin membayar bersama.

### Pertanyaan

Apakah bill dapat digabung?

---

# CASE 44 — CUSTOMER LEAVES

Customer pergi sebelum membayar.

### Pertanyaan

Bagaimana order ditangani?

Apakah menjadi:

* unpaid?
* loss?
* outstanding?
* incident?

Jangan langsung dianggap sebagai revenue.

---

# CASE 45 — PAYMENT

Customer membayar:

Cash.

### Pertanyaan

Apakah restaurant dapat mengetahui:

* amount?
* cashier?
* time?
* transaction?
* table?
* order?

---

# CASE 46 — MULTIPLE PAYMENT

Total:

Rp1.000.000.

Customer membayar:

Rp400.000 cash

Rp600.000 QR.

### Pertanyaan

Apakah pembayaran dapat dibagi?

---

# CASE 47 — REFUND

Customer sudah membayar.

Kemudian restaurant menyetujui refund.

### Pertanyaan

Apakah refund dapat dikaitkan dengan transaksi awal?

---

# CASE 48 — VOID

Waiter salah memasukkan item.

Order belum dibayar.

### Pertanyaan

Apakah item dapat di-void?

Siapa yang memiliki hak?

---

# CASE 49 — VOID SETELAH KITCHEN MEMPROSES

Item sudah dibuat kitchen.

Waiter meminta void.

### Pertanyaan

Apakah prosesnya berbeda?

Apakah kitchen harus diberitahu?

Apakah inventory/waste terdampak?

---

# CASE 50 — TABLE CLOSED

Customer sudah membayar.

### Pertanyaan

Apakah Table otomatis kembali:

> Available

?

Atau harus:

> Cleaning

terlebih dahulu?

Ini tergantung bisnis.

---

# CASE 51 — CLEANING TABLE

Table baru saja ditinggalkan customer.

Belum dibersihkan.

### Pertanyaan

Apakah waiter dapat mengetahui bahwa meja belum siap digunakan?

---

# CASE 52 — TABLE OUT OF SERVICE

Table rusak.

### Pertanyaan

Apakah table dapat dinonaktifkan sementara?

Customer tidak boleh ditempatkan di sana.

---

# CASE 53 — SHIFT WAITER

Waiter A bekerja:

10.00–18.00.

Waiter B:

18.00–02.00.

### Pertanyaan

Apakah order dapat diketahui siapa yang menangani?

---

# CASE 54 — SHIFT KITCHEN

Kitchen memiliki shift berbeda.

### Pertanyaan

Apakah order dapat dilacak berdasarkan shift?

---

# CASE 55 — SHIFT CASHIER

Cashier A membuka shift.

Modal:

Rp500.000.

Closing:

Expected:

Rp5.000.000.

Actual:

Rp4.950.000.

### Pertanyaan

Apakah selisih:

Rp50.000

dapat diketahui?

---

# CASE 56 — DAILY CLOSING

Restaurant selesai beroperasi.

Management ingin mengetahui:

* total sales
* cash
* non-cash
* discount
* refund
* void
* waste
* jumlah customer
* jumlah order
* table utilization

### Pertanyaan

Apakah kondisi operasional hari tersebut dapat dijelaskan?

---

# CASE 57 — RESTAURANT BUSY HOURS

Management ingin mengetahui:

> “Jam berapa restaurant paling ramai?”

Contoh:

12.00–13.00

200 customer.

19.00–20.00

300 customer.

### Pertanyaan

Apakah data operasional dapat memberikan informasi tersebut?

---

# CASE 58 — MENU PERFORMANCE

Management ingin mengetahui:

> “Menu apa yang paling laku?”

Contoh:

Nasi Goreng:

500 porsi.

Steak:

200 porsi.

Es Teh:

800 gelas.

### Pertanyaan

Apakah restaurant dapat mengetahui performa menu?

---

# CASE 59 — MENU PROFITABILITY

Menu A:

Sales:

Rp10.000.000.

Menu B:

Sales:

Rp8.000.000.

Tetapi Menu B memiliki margin lebih tinggi.

### Pertanyaan

Apakah management dapat membedakan:

> Popularity

dengan:

> Profitability

?

---

# CASE 60 — TABLE PERFORMANCE

Management ingin mengetahui:

> “Meja mana yang paling sering digunakan?”

> “Berapa lama rata-rata customer berada di meja?”

> “Berapa revenue per table?”

### Pertanyaan

Apakah restaurant dapat mendapatkan informasi tersebut?

---

# CASE 61 — CUSTOMER RETURNING

Customer datang kembali.

### Pertanyaan

Apakah restaurant dapat mengetahui histori:

* kunjungan?
* order?
* spending?
* membership?
* preference?

Jika fitur customer/loyalty tersedia.

---

# CASE 62 — MEMBER CUSTOMER

Customer:

**Gold Member**

Benefit:

10% discount.

### Pertanyaan

Apakah benefit member otomatis diterapkan?

Bagaimana jika membership expired?

---

# CASE 63 — RESERVATION DEPOSIT

Customer melakukan reservasi.

Restaurant meminta:

Rp500.000 deposit.

### Pertanyaan

Apakah deposit dapat dicatat?

Ketika customer datang:

> Apakah deposit diperhitungkan terhadap bill?

---

# CASE 64 — NO-SHOW DEPOSIT

Customer tidak datang.

Restaurant memiliki kebijakan:

> Deposit tidak dikembalikan.

### Pertanyaan

Bagaimana kondisi tersebut dicatat?

---

# CASE 65 — RESTAURANT MULTI OUTLET

Restaurant memiliki:

Outlet Jakarta

Outlet Bandung

Outlet Surabaya

### Pertanyaan

Apakah masing-masing outlet dapat memiliki:

* meja?
* menu?
* harga?
* stock?
* staff?
* shift?
* sales?

Management tetap harus dapat melihat:

> Total perusahaan.

---

# CASE 66 — MENU BERBEDA PER OUTLET

Outlet Jakarta menjual:

Menu A.

Outlet Bandung tidak menjual:

Menu A.

### Pertanyaan

Apakah menu dapat dikonfigurasi berdasarkan outlet?

---

# CASE 67 — HARGA BERBEDA PER OUTLET

Menu:

Rp50.000 di Jakarta.

Rp55.000 di Bandung.

### Pertanyaan

Apakah harga dapat berbeda berdasarkan outlet?

---

# CASE 68 — INGREDIENT SHARED

Outlet A dan B menggunakan bahan dari lokasi penyimpanan yang sama.

### Pertanyaan

Bagaimana restaurant mengetahui konsumsi masing-masing outlet?

---

# CASE 69 — KITCHEN STOCK

Kitchen memiliki bahan:

* ayam
* beras
* minyak
* bumbu

### Pertanyaan

Apakah bahan yang digunakan kitchen dapat ditelusuri?

---

# CASE 70 — STOCK WASTE

Hari ini:

Ayam terbuang:

5 kg.

Beras:

2 kg.

Minyak:

1 liter.

### Pertanyaan

Apakah management dapat mengetahui:

> Berapa waste?

Dan:

> Apa penyebabnya?

---

# CASE 71 — STOCK THEORETICAL VS ACTUAL

Menurut recipe:

Ayam seharusnya digunakan:

50 kg.

Actual usage:

60 kg.

### Pertanyaan

Ada selisih:

10 kg.

Apakah management dapat mengetahui adanya variance?

---

# CASE 72 — MENU RECIPE VARIANCE

Restaurant menjual:

1.000 porsi.

Recipe membutuhkan:

100g ayam/porsi.

Theoretical:

100 kg.

Actual:

110 kg.

### Pertanyaan

Apakah management dapat mengetahui:

> Ada penggunaan 10 kg lebih tinggi dari standard?

Ini dapat menjadi indikasi:

* portion tidak konsisten
* waste
* pencurian
* kesalahan pencatatan
* recipe tidak sesuai kondisi nyata

---

# CASE 73 — KITCHEN INVENTORY

Kitchen membutuhkan:

20 kg ayam.

Storage memiliki:

10 kg.

### Pertanyaan

Bagaimana kitchen mendapatkan kekurangan?

Apakah ada proses:

> Requisition / transfer

dari inventory?

---

# CASE 74 — KITCHEN REQUEST

Kitchen meminta:

30 kg ayam.

Warehouse hanya memiliki:

20 kg.

### Pertanyaan

Apakah kondisi shortage dapat diketahui?

---

# CASE 75 — SUPPLIER DELIVERY

Supplier mengirim bahan:

100 kg ayam.

Restaurant menerima:

95 kg.

### Pertanyaan

Apa yang terjadi terhadap:

5 kg selisih?

---

# CASE 76 — FOOD SAFETY

Bahan memiliki:

Expiration Date.

### Pertanyaan

Apakah kitchen mengetahui bahan yang:

> paling dekat expired?

---

# CASE 77 — CUSTOMER PEAK

Restaurant tiba-tiba ramai.

Dalam 30 menit:

100 order masuk.

### Pertanyaan

Apakah restaurant dapat mengetahui:

* jumlah order?
* kitchen workload?
* table availability?
* menu availability?
* payment queue?

---

# CASE 78 — KITCHEN OVERLOAD

Order terlalu banyak.

Kitchen tidak mampu memenuhi semua order tepat waktu.

### Pertanyaan

Apakah management dapat melihat backlog?

---

# CASE 79 — MENU TEMPORARILY DISABLED

Kitchen sedang overload.

Management menonaktifkan sementara:

> Steak.

### Pertanyaan

Apakah waiter langsung mengetahui bahwa menu tersebut tidak tersedia?

---

# CASE 80 — END OF DAY

Restaurant tutup.

Pastikan seluruh kondisi dapat diketahui:

### Tables

* Available
* Occupied
* Reserved
* Cleaning
* Out of Service

### Orders

* Completed
* Open
* Cancelled
* Unpaid

### Kitchen

* Completed
* Pending
* Cancelled
* Waste

### Payment

* Paid
* Partial
* Failed
* Refunded

### Inventory

* Used
* Wasted
* Remaining

### Cashier

* Expected Cash
* Actual Cash
* Variance

---

# RESTAURANT FULL-DAY TEST

Ini adalah salah satu testing terpenting.

Jangan melakukan 1 transaksi lalu menyatakan:

> “Restaurant Module berhasil.”

Simulasikan satu hari.

---

## 09.30 — Opening

Staff masuk.

↓

Restaurant dibuka.

↓

Kitchen diperiksa.

↓

Stock diperiksa.

↓

Table diperiksa.

---

## 10.15 — Customer Pertama

2 customer.

↓

Dine-in.

↓

Order.

↓

Kitchen.

↓

Serve.

↓

Payment.

↓

Table cleaning.

↓

Table available.

---

## 12.00 — Lunch Rush

20 customer datang.

↓

Beberapa table occupied.

↓

Multiple order.

↓

Additional order.

↓

Kitchen mulai overload.

↓

Beberapa menu habis.

↓

Beberapa customer menunggu.

---

## 13.30 — Customer Complaint

Customer menerima menu salah.

↓

Correction.

↓

Replacement.

---

## 15.00 — Takeaway

Customer melakukan takeaway.

---

## 16.00 — Delivery

Order delivery masuk.

↓

Kitchen.

↓

Packing.

↓

Pickup.

---

## 18.00 — Shift Change

Waiter A selesai.

Waiter B mulai.

Cashier A → Cashier B.

---

## 19.00 — Dinner Rush

Restaurant kembali ramai.

↓

Reservation.

↓

Walk-in.

↓

Table merge.

↓

Additional order.

↓

Split bill.

---

## 22.00 — Closing

Restaurant mulai kosong.

↓

Table cleaning.

↓

Kitchen closing.

↓

Waste recording.

↓

Cashier closing.

↓

Stock review.

↓

Management melihat laporan.

---

# MANAGEMENT QUESTIONS

Setelah simulasi satu hari selesai, bertindak sebagai Owner.

Tanyakan:

> **“Berapa total penjualan hari ini?”**

> **“Berapa jumlah customer?”**

> **“Berapa jumlah order?”**

> **“Menu apa yang paling laku?”**

> **“Menu apa yang paling banyak dibatalkan?”**

> **“Berapa makanan yang terbuang?”**

> **“Kenapa banyak makanan terbuang?”**

> **“Berapa table yang digunakan?”**

> **“Berapa lama customer rata-rata berada di table?”**

> **“Jam berapa restaurant paling ramai?”**

> **“Berapa penjualan dine-in?”**

> **“Berapa takeaway?”**

> **“Berapa delivery?”**

> **“Berapa discount?”**

> **“Berapa refund?”**

> **“Berapa void?”**

> **“Berapa cash yang seharusnya ada?”**

> **“Berapa cash aktual?”**

> **“Ada selisih?”**

> **“Berapa bahan yang digunakan?”**

> **“Berapa waste?”**

> **“Apakah penggunaan bahan sesuai recipe?”**

> **“Menu apa yang paling menguntungkan?”**

Jika pertanyaan tersebut dapat dijawab:

> **Restaurant Module mulai memberikan informasi operasional yang nyata.**

---

# RESTAURANT LIFECYCLE

Gunakan lifecycle ini sebagai pengujian utama:

**Reservation / Walk-in**

↓

**Table Assignment**

↓

**Order**

↓

**Modifier / Special Request**

↓

**Kitchen**

↓

**Preparation**

↓

**Ready**

↓

**Serving**

↓

**Additional Order**

↓

**Bill**

↓

**Payment**

↓

**Table Cleaning**

↓

**Table Available**

↓

**Inventory Consumption**

↓

**Revenue**

↓

**Closing**

---

# TESTING EXCEPTION

Setelah happy path selesai, sengaja buat kondisi buruk:

### Customer tidak datang.

### Customer terlambat.

### Jumlah customer berubah.

### Customer pindah meja.

### Table penuh.

### Table rusak.

### Order salah.

### Order dibatalkan.

### Menu habis.

### Ingredient habis.

### Kitchen overload.

### Kitchen salah membuat makanan.

### Customer complaint.

### Food waste.

### Ingredient waste.

### Customer tidak membayar.

### Partial payment.

### Refund.

### Void.

### Discount berlebihan.

### Reservation bentrok.

### Delivery terlambat.

### Kitchen kehilangan order.

### Stock bahan tidak sesuai.

### Recipe tidak sesuai pemakaian aktual.

### Cashier mengalami selisih.

---

# CROSS-MODULE TESTING

Setelah Restaurant Module selesai diuji sendiri:

## RESTAURANT → POS

Order restaurant:

→ POS

Payment:

→ POS

---

## RESTAURANT → INVENTORY

Menu terjual:

→ bahan berkurang

Waste:

→ inventory adjustment

Recipe:

→ consumption

---

## RESTAURANT → CUSTOMER

Customer:

→ order history

→ loyalty

→ membership

---

## RESTAURANT → SALES

Jika restaurant menggunakan Sales sebagai bagian dari proses:

→ order / sales information harus konsisten.

---

## RESTAURANT → ACCOUNTING

Sales:

→ Revenue

Payment:

→ Cash / Bank

Discount:

→ Discount

Refund:

→ Refund

Consumption:

→ Cost

Waste:

→ Loss / Cost sesuai kebijakan.

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

Apa dampaknya bagi restaurant?

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

**1. Restaurant Opening**

↓

**2. Table Management**

↓

**3. Walk-in**

↓

**4. Reservation**

↓

**5. Customer Seating**

↓

**6. Basic Order**

↓

**7. Additional Order**

↓

**8. Modifier**

↓

**9. Kitchen**

↓

**10. Kitchen Status**

↓

**11. Serving**

↓

**12. Menu Availability**

↓

**13. Recipe**

↓

**14. Inventory Consumption**

↓

**15. Waste**

↓

**16. Takeaway**

↓

**17. Delivery**

↓

**18. Bill**

↓

**19. Split Bill**

↓

**20. Payment**

↓

**21. Refund**

↓

**22. Void**

↓

**23. Table Closing**

↓

**24. Shift**

↓

**25. Daily Closing**

↓

**26. Multi Outlet**

↓

**27. Management Report**

↓

**28. Exception Cases**

↓

**29. Cross-module Testing**

↓

**30. Full-day Simulation**

↓

**31. Catat Gap**

↓

**32. Tentukan apakah Gap merupakan Bug, Konfigurasi, Keterbatasan, atau Kebutuhan Bisnis Baru**

---

# CHECKPOINT TERAKHIR

Bayangkan Anda adalah:

### Waiter

> “Apakah saya bisa melayani customer tanpa kebingungan?”

### Kitchen

> “Apakah saya tahu makanan apa yang harus dibuat dan kapan harus selesai?”

### Cashier

> “Apakah saya tahu berapa yang harus dibayar customer dan berapa uang yang saya terima?”

### Supervisor

> “Apakah saya bisa mengetahui apa yang sedang terjadi di restaurant?”

### Owner

> “Apakah saya percaya angka penjualan, penggunaan bahan, waste, dan uang yang dihasilkan restaurant?”

Jika semuanya:

**Ya**

maka Restaurant Module mulai matang.

---

# PRINSIP UTAMA RESTAURANT TESTING

Jangan mengejar:

> **“Order makanan berhasil dibuat.”**

Kejar:

> **“Seluruh aktivitas operasional restaurant dari customer datang sampai restaurant tutup dapat direpresentasikan, dikontrol, dan dipertanggungjawabkan.”**

Karena Restaurant Module bukan sekadar:

> **Table + Menu + Order.**

Restaurant Module sebenarnya menggambarkan:

> **Customer + Table + Order + Kitchen + Recipe + Inventory + Payment + Staff + Operational Control**

Dan ketika digabung dengan POS:

**Restaurant**

↓

**POS**

↓

**Inventory**

↓

**Accounting**

maka satu transaksi customer dapat memiliki perjalanan:

> Customer memesan makanan
> → kitchen membuat makanan
> → bahan inventory digunakan
> → customer membayar
> → revenue tercatat
> → cash/bank bertambah
> → table kembali tersedia.

---

# PRINSIP PENUTUP

Setelah semua testing selesai, jangan hanya bertanya:

> **“Apakah restaurant bisa menerima order?”**

Tanyakan:

> **“Kalau restaurant ini benar-benar ramai malam ini, apakah seluruh staff bisa menjalankan pekerjaannya?”**

Kemudian:

> **“Kalau terjadi kesalahan, apakah saya tahu apa yang terjadi?”**

Kemudian:

> **“Kalau ada makanan terbuang, apakah saya tahu berapa dan kenapa?”**

Kemudian:

> **“Kalau stock bahan habis, apakah operasional mengetahuinya sebelum customer kecewa?”**

Dan terakhir:

> **“Kalau saya sebagai owner melihat laporan malam ini, apakah saya percaya angka tersebut?”**

Jika jawabannya **ya**, maka Restaurant Module bukan lagi sekadar fitur tambahan POS.

Ia sudah menjadi:

> **sistem operasional restoran.**
