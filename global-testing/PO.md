# Purchase Order Business Case Testing Guide

## Panduan Pengujian Module Purchase Order Berdasarkan Skenario Bisnis

### Tujuan

Dokumen ini digunakan untuk menguji module Purchase Order (PO) dengan pendekatan bisnis murni.

Jangan mulai dengan pertanyaan:

> “Apakah PO berhasil dibuat?”

Mulailah dengan:

> **“Jika saya adalah perusahaan ini, apakah seluruh proses pembelian saya dapat dijalankan dan dipertanggungjawabkan dengan benar?”**

Purchase Order bukan sekadar dokumen untuk membeli barang.

PO merupakan bagian dari proses:

**Kebutuhan → Permintaan → Persetujuan → Pemilihan Supplier → Kesepakatan → Pemesanan → Penerimaan → Tagihan → Pembayaran**

Testing harus memastikan seluruh perjalanan tersebut masuk akal dari sisi bisnis.

---

# CARA MENGGUNAKAN PANDUAN INI

Gunakan beberapa perusahaan dengan karakter berbeda.

Jangan menganggap semua perusahaan membeli dengan cara yang sama.

Untuk setiap case:

**Kenali kebutuhan → Tentukan barang/jasa → Pilih supplier → Dapatkan persetujuan → Buat pesanan → Terima → Periksa → Bayar**

Kemudian sengaja masukkan kondisi yang tidak ideal.

---

# CASE 1 — RESTORAN

## Profil Perusahaan

Nama: **Saji Rasa**

Jenis usaha: Restoran

Jumlah outlet: 1

Aktivitas pembelian:

* bahan makanan
* minuman
* kemasan
* alat dapur
* perlengkapan kebersihan
* peralatan restoran

---

# Skenario 1 — Pembelian Rutin

Kitchen membutuhkan:

* Beras 100 kg
* Minyak 50 liter
* Ayam 100 kg
* Telur 500 butir

Supplier yang biasa digunakan sudah diketahui.

### Pertanyaan

Bagaimana perusahaan mengetahui:

* apa yang dibutuhkan?
* berapa jumlahnya?
* dari supplier mana?
* berapa harga terakhir?
* kapan barang dibutuhkan?

Jangan hanya fokus pada pembuatan PO.

Tanyakan:

> “Apa yang menyebabkan perusahaan memutuskan untuk membeli?”

---

# Skenario 2 — Supplier Baru

Restoran menemukan supplier baru yang menawarkan harga lebih murah.

Namun supplier belum pernah digunakan sebelumnya.

### Pertanyaan

Apakah perusahaan dapat membedakan:

**supplier yang sudah dipercaya**

dengan

**supplier baru yang belum memiliki histori transaksi?**

Apa yang perlu dipertimbangkan sebelum perusahaan melakukan pembelian?

---

# Skenario 3 — Pembelian Darurat

Tiba-tiba stok ayam habis.

Restoran membutuhkan ayam hari itu juga.

Tidak memungkinkan menjalankan proses pembelian normal secara lengkap.

### Pertanyaan

Apakah perusahaan memiliki mekanisme untuk menangani pembelian darurat?

Dan setelah pembelian dilakukan:

> Apakah transaksi tersebut tetap dapat dipertanggungjawabkan?

---

# Skenario 4 — Harga Supplier Berubah

Harga ayam sebelumnya:

Rp35.000/kg

Supplier sekarang menawarkan:

Rp40.000/kg.

### Pertanyaan

Apakah perusahaan dapat mengetahui bahwa harga tersebut berubah?

Apakah orang yang melakukan pembelian boleh langsung menerima harga baru?

Atau diperlukan persetujuan?

---

# CASE 2 — PERUSAHAAN DISTRIBUSI

## Profil

Nama: **Maju Distribusi**

Jumlah karyawan: 75

Memiliki:

* Warehouse
* Purchasing
* Finance
* Sales

Pembelian dilakukan dalam jumlah besar.

---

# Skenario 1 — Permintaan Pembelian

Warehouse menyampaikan kebutuhan:

> “Stok produk A sudah mendekati batas minimum.”

Purchasing kemudian mencari supplier.

### Pertanyaan

Apakah pembelian dapat dimulai dari kebutuhan internal?

Apakah orang yang membutuhkan barang harus menjadi orang yang membuat PO?

---

# Skenario 2 — Perbandingan Supplier

Tiga supplier menawarkan harga:

Supplier A:
Rp95.000/unit

Supplier B:
Rp92.000/unit

Supplier C:
Rp98.000/unit

Namun:

* Supplier A memberikan tempo 30 hari.
* Supplier B harus dibayar langsung.
* Supplier C memiliki pengiriman paling cepat.

### Pertanyaan

Apakah supplier termurah otomatis menjadi pilihan terbaik?

Bagaimana perusahaan menentukan supplier?

---

# Skenario 3 — Approval

Purchasing membuat pembelian:

**Rp150.000.000**

Perusahaan memiliki aturan bahwa pembelian di atas jumlah tertentu harus disetujui management.

### Pertanyaan

Siapa yang boleh menyetujui?

Apakah orang yang membuat PO boleh menyetujui PO sendiri?

Apa yang terjadi jika approval ditolak?

---

# Skenario 4 — Perubahan Setelah Approval

PO sudah disetujui.

Kemudian supplier meminta perubahan harga.

Harga awal:

Rp100.000/unit

Harga baru:

Rp110.000/unit.

### Pertanyaan

Apakah perubahan tersebut boleh dilakukan langsung?

Atau perusahaan harus meminta persetujuan kembali?

---

# CASE 3 — PEMBELIAN BARANG DENGAN PENGIRIMAN BERTAHAP

## Skenario

Perusahaan memesan:

**1.000 unit barang**

Supplier hanya dapat mengirim:

* 400 unit minggu pertama
* 300 unit minggu kedua
* 300 unit minggu ketiga

### Pertanyaan

Apakah perusahaan menganggap PO selesai ketika 400 unit pertama datang?

Atau PO masih memiliki kewajiban yang belum terpenuhi?

---

# Skenario 2 — Barang Kurang

Supplier seharusnya mengirim:

100 unit

Tetapi hanya mengirim:

95 unit.

### Pertanyaan

Bagaimana perusahaan mengetahui ada kekurangan?

Apakah perusahaan:

* menerima 95?
* menolak seluruh pengiriman?
* menunggu 5 sisanya?

Tidak semua perusahaan memiliki kebijakan yang sama.

---

# Skenario 3 — Barang Rusak

Supplier mengirim:

100 unit.

Tetapi:

10 unit rusak.

### Pertanyaan

Apakah perusahaan menerima 90 unit saja?

Apakah 10 unit tersebut tetap dianggap terpenuhi?

Siapa yang bertanggung jawab?

---

# CASE 4 — PEMBELIAN JASA

Ini penting.

Tidak semua PO membeli barang.

## Profil

Nama: **Nusantara Digital**

Perusahaan membutuhkan:

* jasa konsultan
* jasa maintenance
* jasa cleaning
* jasa security
* jasa software subscription

---

# Skenario 1 — Jasa Konsultan

Perusahaan membuat pesanan:

**Jasa konsultasi 3 bulan**

Nilai:

Rp60.000.000.

Tidak ada barang yang dikirim.

### Pertanyaan

Bagaimana perusahaan mengetahui bahwa jasa tersebut sudah diterima?

Apakah cukup berdasarkan invoice?

Atau ada bukti bahwa pekerjaan memang telah dilakukan?

---

# Skenario 2 — Jasa Bulanan

Perusahaan menggunakan jasa cleaning:

Rp5.000.000/bulan.

Kontrak:

12 bulan.

### Pertanyaan

Apakah perusahaan membutuhkan satu PO untuk 12 bulan?

Atau PO per bulan?

Apakah keputusan tersebut harus selalu sama untuk semua perusahaan?

---

# CASE 5 — PURCHASE ORDER + KONTRAK

## Profil

Perusahaan memiliki kontrak dengan supplier selama satu tahun.

Supplier menyediakan bahan baku dengan harga yang sudah disepakati.

### Skenario

Kontrak:

12 bulan

Estimasi pembelian:

Rp500 juta.

Tetapi jumlah pembelian sebenarnya berubah setiap bulan.

### Pertanyaan

Apa perbedaan antara:

**kesepakatan jangka panjang**

dengan

**pesanan aktual?**

Jangan sampai perusahaan menganggap estimasi kebutuhan satu tahun sebagai kewajiban membeli seluruh Rp500 juta.

---

# CASE 6 — PARTIAL INVOICE

## Skenario

PO:

Rp100.000.000

Barang dikirim dalam tiga tahap.

Supplier mengirim invoice:

Tahap 1:
Rp40 juta

Tahap 2:
Rp30 juta

Tahap 3:
Rp30 juta

### Pertanyaan

Apakah perusahaan dapat mengetahui:

* nilai PO?
* nilai yang sudah diterima?
* nilai yang sudah ditagihkan?
* nilai yang belum ditagihkan?
* nilai yang belum diterima?

---

# CASE 7 — INVOICE LEBIH BESAR DARI PO

## Skenario

PO:

Rp50.000.000

Supplier mengirim invoice:

Rp55.000.000.

### Pertanyaan

Apakah perusahaan langsung membayar?

Atau perlu dilakukan pemeriksaan?

Apa penyebab perbedaannya?

Kemungkinan:

* harga berubah
* jumlah berubah
* biaya tambahan
* kesalahan supplier

---

# CASE 8 — BARANG DITERIMA TETAPI INVOICE BELUM DATANG

## Skenario

Barang senilai:

Rp20.000.000

sudah diterima.

Tetapi invoice belum dikirim supplier.

### Pertanyaan

Apakah perusahaan sudah memiliki kewajiban?

Bagaimana Finance mengetahui:

> “Barang sudah diterima, tetapi tagihan belum datang.”

Ini adalah case penting karena kehidupan bisnis tidak selalu berjalan:

> PO → Barang → Invoice → Bayar

secara langsung dan sempurna.

---

# CASE 9 — PO DIBATALKAN

## Skenario

PO:

Rp100.000.000

sudah disetujui.

Namun supplier mengalami masalah dan perusahaan membatalkan pesanan.

### Pertanyaan

Apakah PO masih dianggap aktif?

Apakah pembatalan harus diketahui pihak tertentu?

Apakah alasan pembatalan perlu diketahui?

Bagaimana perusahaan mengetahui bahwa PO tersebut pernah dibuat tetapi kemudian dibatalkan?

---

# CASE 10 — SUPPLIER TIDAK MEMENUHI PESANAN

## Skenario

Perusahaan memesan:

1.000 unit.

Supplier hanya mengirim:

600 unit.

Setelah itu supplier menyatakan tidak dapat memenuhi sisa 400 unit.

### Pertanyaan

Apa yang terjadi terhadap sisa pesanan?

Apakah perusahaan:

* menunggu?
* menutup sisa pesanan?
* mencari supplier lain?
* membuat pesanan baru?

Yang penting:

> Perusahaan harus mengetahui bahwa 400 unit tersebut tidak lagi akan datang.

---

# CASE 11 — PERUBAHAN JUMLAH PESANAN

## Skenario

PO awal:

1.000 unit.

Sebelum dikirim, perusahaan menyadari kebutuhannya hanya 700 unit.

### Pertanyaan

Apakah jumlah PO dapat berubah?

Siapa yang harus mengetahui?

Jika PO sudah disetujui, apakah perubahan tersebut membutuhkan persetujuan kembali?

---

# CASE 12 — PEMBELIAN BERDASARKAN BUDGET

## Skenario

Departemen Marketing memiliki budget:

**Rp100.000.000**

Marketing ingin melakukan pembelian:

**Rp80.000.000**

Kemudian ada pembelian tambahan:

**Rp40.000.000**

### Pertanyaan

Apakah perusahaan dapat mengetahui:

> Budget awal: Rp100 juta

> Pembelian: Rp120 juta

> Budget terlampaui: Rp20 juta

Apakah pembelian kedua seharusnya mendapatkan perhatian khusus?

---

# CASE 13 — PEMBELIAN MULTI DEPARTMENT

## Skenario

Perusahaan membeli laptop untuk:

* Finance
* HR
* Sales
* Management

Total:

Rp200.000.000.

### Pertanyaan

Apakah perusahaan mengetahui siapa yang membutuhkan barang?

Departemen mana yang menggunakan?

Untuk tujuan apa?

Siapa yang bertanggung jawab?

Jangan sampai setelah barang dibeli, perusahaan hanya mengetahui:

> “Kita beli laptop Rp200 juta.”

Tetapi tidak tahu:

> “Laptop tersebut sebenarnya untuk siapa?”

---

# CASE 14 — PEMBELIAN ASET

## Skenario

Perusahaan membeli mesin:

Rp300.000.000.

Pembelian dilakukan melalui supplier.

### Pertanyaan

Apakah pembelian tersebut hanya dianggap sebagai pembelian biasa?

Atau terdapat hubungan antara:

**Purchase → Asset → Accounting**

Pastikan PO dapat menjadi bagian dari perjalanan bisnis tersebut tanpa kehilangan konteks.

---

# CASE 15 — PEMBELIAN BERULANG

## Skenario

Perusahaan membeli:

* air mineral
* ATK
* bahan baku
* cleaning supplies

setiap bulan.

Supplier sama.

Harga relatif stabil.

### Pertanyaan

Apakah perusahaan harus selalu memulai semuanya dari nol?

Apakah histori pembelian dapat membantu keputusan pembelian berikutnya?

---

# CASE 16 — SUPPLIER MEMILIKI HARGA KHUSUS

## Skenario

Supplier A memberikan harga normal:

Rp100.000/unit.

Tetapi perusahaan memiliki kesepakatan:

> Jika membeli lebih dari 1.000 unit, harga menjadi Rp90.000.

Perusahaan membeli:

1.500 unit.

### Pertanyaan

Apakah perusahaan dapat mengetahui harga yang seharusnya berlaku?

Bagaimana jika jumlah pembelian hanya 500 unit?

---

# CASE 17 — PEMBELIAN DENGAN BIAYA TAMBAHAN

## Skenario

Harga barang:

Rp50.000.000.

Kemudian terdapat:

* ongkos kirim Rp2 juta
* asuransi Rp500 ribu
* biaya tambahan lainnya

### Pertanyaan

Apakah perusahaan dapat membedakan:

**harga barang**

dengan

**biaya tambahan pembelian?**

Apakah biaya tersebut harus selalu diperlakukan dengan cara yang sama?

---

# CASE 18 — MULTI OUTLET

## Profil

**Nusantara Hospitality Group**

Memiliki:

* Restaurant A
* Restaurant B
* Restaurant C

Purchasing dilakukan oleh Head Office.

---

# Skenario

Restaurant A membutuhkan:

Rp20 juta

Restaurant B:

Rp15 juta

Restaurant C:

Rp25 juta

Head Office membuat pembelian kepada satu supplier.

### Pertanyaan

Bagaimana perusahaan mengetahui barang tersebut sebenarnya untuk outlet mana?

Apakah pembelian harus dipisahkan?

Atau satu pesanan dapat melayani beberapa outlet?

---

# CASE 19 — SUPPLIER DENGAN KONDISI BERBEDA

Dua supplier menawarkan barang yang sama.

### Supplier A

Harga lebih murah.

Pembayaran harus dilakukan langsung.

### Supplier B

Harga lebih mahal.

Memberikan tempo 60 hari.

### Pertanyaan

Supplier mana yang lebih baik?

Tidak ada jawaban universal.

Yang diuji adalah:

> Apakah perusahaan memiliki informasi yang cukup untuk membuat keputusan?

---

# CASE 20 — MANAGEMENT MEMPERTANYAKAN PEMBELIAN

Management bertanya:

> “Kenapa bulan ini pembelian naik?”

↓

Apakah dapat diketahui?

---

> “Supplier mana yang paling banyak kita gunakan?”

↓

Apakah dapat diketahui?

---

> “Berapa nilai PO yang masih belum selesai?”

↓

Apakah dapat diketahui?

---

> “Berapa pembelian yang sudah disetujui tetapi belum diterima?”

↓

Apakah dapat diketahui?

---

> “Supplier mana yang paling sering terlambat?”

↓

Apakah histori cukup untuk menjawab?

---

> “Berapa banyak PO yang dibatalkan?”

↓

Apakah dapat diketahui?

---

> “Berapa nilai pembelian setiap departemen?”

↓

Apakah dapat diketahui?

---

# TESTING PURCHASE LIFECYCLE

Setelah seluruh case selesai, lakukan satu perjalanan lengkap.

Bayangkan:

**Departemen membutuhkan barang**

↓

**Kebutuhan diketahui**

↓

**Supplier dicari**

↓

**Penawaran dibandingkan**

↓

**Supplier dipilih**

↓

**Pembelian diminta**

↓

**Persetujuan dilakukan**

↓

**Purchase Order dibuat**

↓

**Supplier menerima pesanan**

↓

**Barang/Jasa diterima**

↓

**Barang diperiksa**

↓

**Invoice diterima**

↓

**Invoice diperiksa**

↓

**Kewajiban muncul**

↓

**Pembayaran dilakukan**

↓

**Pesanan selesai**

---

# TESTING DENGAN PERTANYAAN “WHAT IF?”

Setelah happy path selesai, sengaja ubah kondisi.

### Bagaimana jika...

Supplier menolak pesanan?

---

Harga berubah setelah approval?

---

Jumlah barang yang datang kurang?

---

Barang rusak?

---

Barang datang tanpa PO?

---

Invoice lebih besar daripada PO?

---

Invoice datang sebelum barang?

---

Barang datang tetapi invoice belum datang?

---

PO sudah disetujui tetapi dibatalkan?

---

Supplier tidak dapat memenuhi sisa pesanan?

---

Kebutuhan berubah setelah PO dibuat?

---

Supplier diganti di tengah proses?

---

Pembelian melebihi budget?

---

Barang ternyata untuk outlet lain?

---

Jasa tidak selesai sesuai kesepakatan?

---

Pembelian dilakukan dalam keadaan darurat?

---

# TESTING “WHO SHOULD KNOW?”

Untuk setiap kejadian, tanyakan:

> Siapa yang perlu mengetahui?

Contoh:

PO Rp200 juta dibuat.

Siapa yang perlu mengetahui?

* Requester
* Purchasing
* Manager
* Finance
* Management
* Supplier

Tidak semua informasi harus dilihat semua orang.

Tetapi perusahaan harus dapat menentukan:

> **Siapa yang membutuhkan informasi tersebut untuk menjalankan tanggung jawabnya?**

---

# TESTING “WHO IS RESPONSIBLE?”

Untuk setiap proses:

> Siapa yang bertanggung jawab?

Contoh:

Barang datang tetapi jumlahnya kurang.

Apakah:

* Purchasing?
* Warehouse?
* Supplier?
* Finance?

Tidak selalu orang yang sama.

Testing harus memastikan tanggung jawab bisnis tidak menjadi kabur.

---

# TESTING “COMMITMENT”

Ini konsep penting dalam Purchase Order.

Ketika PO sudah disetujui:

> Perusahaan telah membuat sebuah komitmen pembelian.

Tetapi belum tentu:

> barang sudah diterima.

Dan belum tentu:

> invoice sudah diterima.

Dan belum tentu:

> uang sudah dibayar.

Karena itu, testing harus mampu membedakan:

**Ordered**

→ sudah dipesan

**Received**

→ sudah diterima

**Invoiced**

→ sudah ditagihkan

**Paid**

→ sudah dibayar

Jangan menganggap keempat kondisi tersebut sebagai satu kejadian.

---

# TESTING REPORT

Management seharusnya dapat bertanya:

### Purchase Overview

> Berapa total pembelian bulan ini?

### Open Orders

> Berapa PO yang masih terbuka?

### Pending Receipt

> Apa yang belum diterima?

### Pending Invoice

> Apa yang sudah diterima tetapi belum ditagihkan?

### Pending Payment

> Apa yang sudah menjadi kewajiban tetapi belum dibayar?

### Supplier Performance

> Supplier mana yang sering terlambat?

### Purchase by Department

> Departemen mana yang paling banyak melakukan pembelian?

### Purchase by Supplier

> Supplier mana yang paling banyak digunakan?

### Purchase by Category

> Apa yang paling banyak dibeli?

### Purchase Trend

> Apakah pembelian meningkat atau menurun?

---

# TESTING MULTI-LEVEL APPROVAL

Buat beberapa kondisi.

### Rp1 juta

Tidak membutuhkan approval management.

### Rp20 juta

Membutuhkan Manager.

### Rp100 juta

Membutuhkan Director.

### Rp500 juta

Membutuhkan Management/Owner.

Kemudian ubah kondisi:

> Bagaimana jika pembelian Rp100 juta dibagi menjadi lima PO masing-masing Rp20 juta?

Pertanyaan bisnisnya:

> Apakah perusahaan menganggap ini lima pembelian kecil atau satu kebutuhan besar yang sengaja dipecah?

Ini adalah salah satu **pressure test** yang sangat bagus untuk sistem approval.

---

# TESTING PURCHASE vs EMERGENCY

Bandingkan dua kondisi.

### Normal

Kebutuhan direncanakan jauh sebelumnya.

### Emergency

Kebutuhan muncul tiba-tiba dan harus segera dipenuhi.

Pertanyaan:

> Apakah perusahaan memiliki cara berbeda untuk menangani keduanya tanpa kehilangan kontrol?

---

# TESTING PURCHASE vs BUSINESS REALITY

Ingat bahwa dunia nyata tidak selalu rapi.

Ideal:

**Request → Approval → PO → Receipt → Invoice → Payment**

Realita bisa menjadi:

**Request → Supplier dikontak → Barang datang → PO dibuat belakangan → Invoice datang → Barang ternyata kurang**

atau:

**PO → Supplier gagal → Supplier diganti**

atau:

**PO → Harga berubah → Approval ulang → Pengiriman tertunda**

Testing yang baik harus memasukkan kondisi seperti ini.

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

**1. Restaurant Basic Purchase**

↓

**2. Supplier Selection**

↓

**3. Approval**

↓

**4. Partial Delivery**

↓

**5. Partial Invoice**

↓

**6. Service Purchase**

↓

**7. Contract Purchase**

↓

**8. Budget**

↓

**9. Asset Purchase**

↓

**10. Multi Department**

↓

**11. Multi Outlet**

↓

**12. Emergency Purchase**

↓

**13. Cancellation**

↓

**14. Supplier Failure**

↓

**15. Exception Cases**

↓

**16. Management Questions**

↓

**17. Purchase Lifecycle**

↓

**18. Catat Gap**

↓

**19. Tentukan apakah Gap merupakan Bug, Konfigurasi, Keterbatasan, atau Kebutuhan Bisnis Baru**

---

# PRINSIP UTAMA PURCHASE ORDER TESTING

Jangan mengejar:

> “Semua PO berhasil dibuat.”

Kejar:

> **“Perusahaan selalu mengetahui apa yang mereka butuhkan, apa yang mereka pesan, kepada siapa mereka memesan, siapa yang menyetujui, apa yang sudah diterima, apa yang belum diterima, apa yang sudah ditagihkan, dan apa yang masih harus dibayar.”**

Purchase Order yang matang bukan hanya tempat membuat dokumen pembelian.

Ia menjadi **jejak komitmen perusahaan terhadap pembelian.**

---

# CHECKPOINT TERAKHIR

Bayangkan Anda adalah Owner.

Anda bertanya:

> **“Bulan ini kita beli apa saja?”**

> **“Kenapa kita membeli sebanyak itu?”**

> **“Siapa yang menyetujui?”**

> **“Barangnya sudah datang semua?”**

> **“Supplier sudah menagih?”**

> **“Sudah dibayar?”**

> **“Apa yang masih outstanding?”**

> **“Supplier mana yang bermasalah?”**

> **“Departemen mana yang paling banyak membeli?”**

> **“Apakah pembelian kita masih sesuai budget?”**

> **“Ada pembelian yang dilakukan tanpa kontrol?”**

Jika pertanyaan tersebut dapat dijawab dengan jelas, berarti Purchase Order mulai memiliki nilai bisnis yang nyata.

Jika tidak dapat dijawab:

> Jangan langsung memperbaiki.

Cari tahu terlebih dahulu **informasi apa yang sebenarnya hilang dari proses bisnis.**

---

# PRINSIP PENUTUP

**PO bukan akhir dari pembelian.**

PO adalah salah satu titik dalam perjalanan pembelian.

Yang harus diuji bukan:

> “Apakah PO dapat dibuat?”

Tetapi:

> **“Apakah perusahaan dapat mengendalikan seluruh komitmen pembeliannya dari kebutuhan sampai kewajiban tersebut selesai?”**

Dan jangan lupa:

**Satu perusahaan bukan representasi seluruh dunia bisnis.**

Restoran, distributor, perusahaan jasa, manufaktur, perusahaan multi-outlet, dan perusahaan besar dapat memiliki pola pembelian yang berbeda.

HRM, Accounting, dan Purchase Order harus diuji dengan pola yang berbeda-beda tersebut.

**Tujuan testing bukan membuat aplikasi mengikuti satu perusahaan.**

**Tujuannya menemukan pola bisnis yang cukup umum untuk dijadikan kemampuan sistem, dan pola yang berbeda untuk dijadikan konfigurasi.**
