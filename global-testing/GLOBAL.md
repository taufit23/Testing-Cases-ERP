# ERP Business Integration Testing

## End-to-End Business Case Antar Module

### Tujuan

Panduan ini digunakan untuk menguji apakah seluruh module ERP dapat bekerja sebagai **satu sistem perusahaan**, bukan sebagai kumpulan aplikasi yang berdiri sendiri.

Fokus utama pengujian:

> **Apakah satu aktivitas bisnis dapat berjalan dari awal sampai akhir tanpa menghasilkan informasi yang saling bertentangan antar module?**

Accounting menjadi titik pemeriksaan finansial utama.

Namun tidak semua aktivitas harus langsung menghasilkan pencatatan akuntansi.

Hubungan sederhananya:

**Business Activity**

→ **Operational Event**

→ **Stock / Customer / Supplier / Employee / Payment**

→ **Financial Impact**

→ **Accounting**

---

# 1. CARA BERPIKIR TESTING

Jangan menguji:

> “Apakah PO bisa dibuat?”

Tetapi:

> “Apa yang terjadi kepada perusahaan setelah PO tersebut dibuat?”

Contoh:

Perusahaan membeli barang.

**Purchase Order**

↓

Barang datang

↓

**Inventory bertambah**

↓

Supplier menagih

↓

**Accounts Payable bertambah**

↓

Perusahaan membayar

↓

**Cash/Bank berkurang**

↓

Accounting mengetahui seluruh kejadian tersebut.

---

# 2. BUSINESS CYCLE UTAMA ERP

Secara umum ERP dapat diuji melalui beberapa siklus besar:

### Procure to Pay

Perusahaan membeli sesuatu.

**PO**

→ **Receipt**

→ **Supplier Invoice**

→ **Payment**

→ **Accounting**

---

### Order to Cash

Perusahaan menjual sesuatu.

**SO**

→ **Delivery**

→ **Customer Invoice**

→ **Payment**

→ **Accounting**

---

### Inventory Cycle

Barang bergerak.

**Purchase**

→ **Receive**

→ **Store**

→ **Transfer**

→ **Consume**

→ **Sell**

→ **Return**

→ **Adjustment**

---

### Employee to Payroll

Perusahaan membayar karyawan.

**Employee**

→ **Attendance**

→ **Salary**

→ **Payroll**

→ **Payment**

→ **Accounting**

---

### Restaurant Cycle

Customer membeli makanan.

**Order**

→ **Kitchen**

→ **Ingredient Consumption**

→ **Payment**

→ **Revenue**

→ **Accounting**

---

### Fixed Asset Cycle

Perusahaan membeli aset.

**Purchase**

→ **Asset**

→ **Depreciation**

→ **Maintenance**

→ **Disposal**

→ **Accounting**

---

# 3. CASE BESAR — PERUSAHAAN MEMBELI BARANG

## Profil

PT Maju Jaya membeli:

100 unit Produk A.

Harga:

Rp100.000/unit.

Total:

**Rp10.000.000**

Pembelian dilakukan secara kredit.

---

## Tahap 1 — Purchase Order

Perusahaan membuat PO:

100 unit.

### Pertanyaan

Apakah:

> PO = Rp10.000.000

?

Apakah PO tersebut belum dianggap sebagai hutang?

**PENTING**

PO bukan berarti perusahaan sudah berhutang.

---

## Tahap 2 — Barang Datang

Supplier hanya mengirim:

90 unit.

### Pertanyaan

Apakah inventory bertambah:

**90 unit**

bukan:

100 unit?

---

## Tahap 3 — Supplier Invoice

Supplier menagih:

90 unit.

Rp9.000.000.

### Pertanyaan

Apakah hutang perusahaan menjadi:

**Rp9.000.000**

?

---

## Tahap 4 — Payment

Perusahaan membayar:

Rp9.000.000.

### Pertanyaan

Apakah:

**Accounts Payable berkurang**

dan:

**Bank berkurang**

?

---

# 4. CASE PEMBELIAN DENGAN SELISIH

PO:

100 unit.

Receipt:

95 unit.

Invoice:

100 unit.

### Pertanyaan

Apa yang dilakukan?

Jangan langsung menganggap:

> Sistem error.

Bisa saja perusahaan memiliki kebijakan:

* menolak invoice
* menerima invoice
* menunggu kekurangan barang
* membayar sebagian

Yang diuji:

> **Apakah perbedaan tersebut dapat ditangani berdasarkan kebijakan perusahaan?**

---

# 5. CASE PEMBELIAN DENGAN DISCOUNT

Supplier memberikan:

10% discount.

Harga awal:

Rp10.000.000.

Harga setelah discount:

Rp9.000.000.

### Pertanyaan

Apakah:

* nilai pembelian
* hutang
* pembayaran
* accounting

menggunakan nilai yang konsisten?

---

# 6. CASE PURCHASE RETURN

Perusahaan menerima:

100 unit.

Kemudian menemukan:

10 unit rusak.

Barang dikembalikan.

### Pertanyaan

Apakah:

Inventory

↓

berkurang 10 unit?

Dan:

Hutang

↓

disesuaikan?

---

# 7. CASE SUPPLIER DEPOSIT

Perusahaan membayar supplier:

Rp5.000.000

sebelum barang datang.

### Pertanyaan

Apakah uang tersebut langsung dianggap sebagai expense?

Atau:

> Supplier Advance / Deposit

sesuai kebijakan perusahaan?

Kemudian barang datang.

### Pertanyaan

Apakah deposit dapat diperhitungkan terhadap tagihan?

---

# 8. CASE — PERUSAHAAN MENJUAL BARANG

PT Maju Jaya menjual:

100 unit.

Harga:

Rp150.000.

Total:

**Rp15.000.000**

Customer membeli secara kredit.

---

## Tahap 1 — Sales Order

SO:

Rp15.000.000.

### Pertanyaan

Apakah perusahaan sudah memiliki revenue?

Tidak selalu.

SO adalah komitmen/order.

---

## Tahap 2 — Delivery

Barang dikirim:

100 unit.

### Pertanyaan

Apakah inventory berkurang?

---

## Tahap 3 — Customer Invoice

Invoice:

Rp15.000.000.

### Pertanyaan

Apakah:

**Accounts Receivable**

bertambah?

---

## Tahap 4 — Customer Payment

Customer membayar:

Rp15.000.000.

### Pertanyaan

Apakah:

AR berkurang?

Bank/Cash bertambah?

---

# 9. SALES RETURN

Customer mengembalikan:

10 unit.

### Pertanyaan

Apakah:

Inventory bertambah kembali?

Piutang berkurang?

Revenue dikoreksi?

Cost terkait dikoreksi sesuai kebijakan?

---

# 10. SALES DISCOUNT

Customer mendapatkan:

10% discount.

Harga:

Rp15.000.000.

Discount:

Rp1.500.000.

Customer harus membayar:

**Rp13.500.000**

### Pertanyaan

Apakah seluruh module memahami nilai yang sama?

---

# 11. CASH SALE

Customer langsung membayar:

Rp15.000.000.

### Pertanyaan

Apakah:

Cash/Bank bertambah

dan

Revenue tercatat

sesuai kebijakan perusahaan?

---

# 12. POS SALE

Customer datang ke retail.

Membeli:

5 barang.

Bayar cash.

### Rantai

**POS**

→ Sales

→ Inventory

→ Payment

→ Accounting

### Pertanyaan

Apakah semua angka konsisten?

---

# 13. RESTAURANT SALE

Customer makan:

Rp500.000.

Restaurant menggunakan:

* bahan
* recipe
* kitchen
* table
* POS

Customer membayar cash.

### Rantai

**Restaurant**

→ **POS**

→ **Inventory Consumption**

→ **Payment**

→ **Revenue**

→ **Accounting**

### Pertanyaan

Apakah seluruh rantai konsisten?

---

# 14. RESTAURANT WASTE

Restaurant menjual:

100 porsi.

Tetapi bahan yang terpakai lebih tinggi dari standard.

### Pertanyaan

Apakah management dapat melihat:

> Standard Consumption

vs

> Actual Consumption

?

Dan apakah waste/variance dapat dipertanggungjawabkan?

---

# 15. INVENTORY TRANSFER

Warehouse A:

100 unit.

Transfer ke:

Warehouse B.

### Pertanyaan

Apakah total inventory perusahaan tetap:

100 unit?

Hanya lokasi yang berubah?

---

# 16. INVENTORY ADJUSTMENT

System menunjukkan:

100 unit.

Physical count:

95 unit.

Selisih:

5 unit.

### Pertanyaan

Apakah perusahaan dapat mencatat adjustment?

Apakah alasan dapat diketahui?

Apakah dampak finansialnya dapat dipertanggungjawabkan?

---

# 17. INVENTORY DAMAGE

10 unit rusak.

### Pertanyaan

Apakah:

Inventory berkurang?

Dan nilai kerusakan masuk ke perlakuan finansial yang sesuai?

---

# 18. STOCK OPNAME

Physical count dilakukan.

System:

1.000 unit.

Actual:

970 unit.

### Pertanyaan

Apakah:

Variance:

30 unit

dapat diketahui?

Kemudian:

> siapa yang melakukan?

> kapan?

> mengapa?

> apa keputusan perusahaan?

---

# 19. EMPLOYEE

Perusahaan memiliki:

10 karyawan.

Setiap bulan:

Salary dihitung.

### Pertanyaan

Apakah HR dapat memberikan informasi yang dibutuhkan payroll?

---

# 20. ATTENDANCE → PAYROLL

Employee memiliki:

* attendance
* overtime
* absence
* leave

### Pertanyaan

Apakah data tersebut mempengaruhi salary sesuai kebijakan perusahaan?

---

# 21. PAYROLL

Total salary:

Rp100.000.000.

Perusahaan melakukan pembayaran.

### Pertanyaan

Apakah:

Salary Expense

dan

Payroll Payable

serta

Cash/Bank

dapat dijelaskan?

---

# 22. EMPLOYEE LOAN

Karyawan menerima pinjaman:

Rp5.000.000.

Kemudian dipotong:

Rp500.000/bulan.

### Pertanyaan

Apakah:

Loan Balance

berkurang?

Payroll berubah?

Accounting mengetahui saldo pinjaman?

---

# 23. EMPLOYEE REIMBURSEMENT

Employee membeli kebutuhan perusahaan:

Rp2.000.000.

Perusahaan mengganti uang tersebut.

### Pertanyaan

Apakah:

Expense

dan

Payment

dapat ditelusuri?

---

# 24. FIXED ASSET

Perusahaan membeli laptop:

Rp20.000.000.

### Pertanyaan

Apakah laptop tersebut:

> langsung dianggap expense?

atau:

> Fixed Asset?

Tergantung kebijakan perusahaan.

---

# 25. ASSET DEPRECIATION

Asset:

Rp20.000.000.

Kemudian mengalami depreciation setiap periode.

### Pertanyaan

Apakah nilai buku asset berubah?

Apakah expense depreciation tercatat?

---

# 26. ASSET DISPOSAL

Asset dijual:

Rp8.000.000.

### Pertanyaan

Apakah:

* asset dikeluarkan?
* accumulated depreciation diperhitungkan?
* hasil penjualan dicatat?
* gain/loss diketahui?

---

# 27. COMPANY EXPENSE

Perusahaan membayar listrik:

Rp10.000.000.

### Pertanyaan

Apakah:

Expense

bertambah?

Cash/Bank

berkurang?

---

# 28. PREPAID EXPENSE

Perusahaan membayar:

Asuransi 12 bulan:

Rp12.000.000.

### Pertanyaan

Apakah seluruh Rp12.000.000 langsung dianggap expense?

Atau:

> Prepaid Expense

yang kemudian dialokasikan?

---

# 29. ACCRUAL

Listrik bulan ini:

Rp5.000.000.

Tetapi invoice belum diterima.

### Pertanyaan

Apakah perusahaan tetap dapat mengakui kewajiban/expense sesuai kebijakan akuntansi?

---

# 30. TAX

Perusahaan memiliki kewajiban pajak.

### Pertanyaan

Apakah transaksi yang relevan dapat menghasilkan informasi yang dibutuhkan untuk:

* tax calculation
* tax payable
* payment
* reporting

?

---

# 31. CUSTOMER CREDIT

Customer memiliki credit limit:

Rp100.000.000.

Customer sudah memiliki outstanding:

Rp90.000.000.

Customer membuat order:

Rp30.000.000.

### Pertanyaan

Apakah perusahaan dapat mengetahui:

> potensi exposure customer?

---

# 32. SUPPLIER CREDIT

Supplier memberikan credit limit.

Perusahaan sudah memiliki hutang:

Rp80.000.000.

Kemudian membuat pembelian:

Rp30.000.000.

### Pertanyaan

Apakah kondisi hutang dapat diketahui sebelum perusahaan menambah kewajiban?

---

# 33. PAYMENT PARTIAL

Invoice:

Rp10.000.000.

Dibayar:

Rp6.000.000.

### Pertanyaan

Apakah:

Paid:

Rp6.000.000

Outstanding:

Rp4.000.000

?

---

# 34. PAYMENT MULTIPLE INVOICE

Perusahaan memiliki:

Invoice A:

Rp5.000.000

Invoice B:

Rp3.000.000

Invoice C:

Rp2.000.000

Total:

Rp10.000.000.

Perusahaan membayar:

Rp10.000.000.

### Pertanyaan

Apakah payment dapat dialokasikan dengan benar?

---

# 35. PAYMENT OVERDUE

Invoice:

Rp20.000.000.

Jatuh tempo:

30 hari.

Hari ini:

45 hari.

### Pertanyaan

Apakah management dapat mengetahui:

> Invoice overdue?

---

# 36. CUSTOMER OVERDUE

Customer belum membayar.

### Pertanyaan

Apakah management dapat mengetahui:

* berapa outstanding?
* berapa lama?
* customer mana?
* invoice mana?

---

# 37. SUPPLIER OVERDUE

Perusahaan belum membayar supplier.

### Pertanyaan

Apakah Finance mengetahui:

> supplier mana yang harus dibayar?

---

# 38. CASH MANAGEMENT

Cashier memiliki:

Rp5.000.000.

Bank:

Rp100.000.000.

Petty cash:

Rp2.000.000.

### Pertanyaan

Apakah perusahaan mengetahui posisi cash secara keseluruhan?

---

# 39. CASH DIFFERENCE

Expected:

Rp10.000.000.

Actual:

Rp9.950.000.

### Pertanyaan

Apakah variance:

Rp50.000

dapat diketahui dan dijelaskan?

---

# 40. JOURNAL ADJUSTMENT

Terjadi kesalahan pencatatan.

### Pertanyaan

Apakah perusahaan memiliki mekanisme untuk melakukan koreksi tanpa menghancurkan histori transaksi?

---

# 41. PERIOD CLOSING

Bulan Januari selesai.

Management ingin menutup periode.

### Pertanyaan

Apakah transaksi Januari masih dapat diubah sembarangan?

---

# 42. BACKDATE

Pada Februari ditemukan invoice Januari yang belum tercatat.

### Pertanyaan

Apakah perusahaan boleh memasukkan transaksi ke Januari?

Jika boleh:

> siapa yang berhak?

> apakah ada kontrol?

---

# 43. MULTI OUTLET

Perusahaan:

Outlet A

Outlet B

Outlet C

### Pertanyaan

Apakah management dapat mengetahui:

Revenue A

Revenue B

Revenue C

Cost A

Cost B

Cost C

dan:

> Consolidated Company Result

?

---

# 44. DEPARTMENT / COST CENTER

Expense:

Rp10.000.000.

Dibebankan kepada:

**Marketing**

### Pertanyaan

Apakah management dapat mengetahui expense berdasarkan department?

---

# 45. PROJECT

Perusahaan memiliki:

Project A.

Project B.

Expense:

Rp20.000.000.

### Pertanyaan

Expense tersebut dialokasikan ke project mana?

---

# 46. PURCHASE → PROJECT

Project membutuhkan material:

Rp50.000.000.

Material dibeli.

### Pertanyaan

Apakah management dapat mengetahui:

> berapa biaya Project A?

---

# 47. SALES → PROJECT

Customer membayar:

Rp100.000.000.

untuk Project A.

### Pertanyaan

Apakah management dapat melihat:

Revenue Project A?

---

# 48. PROFITABILITY

Project A:

Revenue:

Rp100.000.000.

Cost:

Rp70.000.000.

### Pertanyaan

Apakah management dapat mengetahui:

> Gross/Project Margin

sesuai struktur bisnis perusahaan?

---

# 49. COMPANY DAY SIMULATION

Sekarang lakukan simulasi satu hari perusahaan.

---

## 08.00

Employee masuk.

↓

Attendance.

---

## 08.30

Warehouse menerima:

100 unit barang.

↓

Inventory bertambah.

---

## 09.00

Purchase invoice diterima.

↓

Payable bertambah.

---

## 09.30

Sales team membuat:

Sales Order.

---

## 10.00

Barang dikirim.

↓

Inventory berkurang.

---

## 10.30

Customer invoice dibuat.

↓

Receivable bertambah.

---

## 11.00

Customer membayar.

↓

Bank bertambah.

↓

Receivable berkurang.

---

## 12.00

Restaurant menerima customer.

↓

Order.

↓

Kitchen.

↓

Ingredient consumption.

↓

Payment.

↓

Revenue.

---

## 14.00

Employee melakukan reimbursement:

Rp500.000.

---

## 15.00

Warehouse menemukan:

5 barang rusak.

↓

Inventory adjustment.

---

## 16.00

Supplier dibayar:

Rp10.000.000.

↓

Payable berkurang.

↓

Bank berkurang.

---

## 17.00

POS melakukan sales:

Rp5.000.000.

---

## 18.00

Cashier closing.

---

## 19.00

Management melihat:

Sales

Inventory

Cash

Receivable

Payable

Expense

---

# 50. FULL BUSINESS CHAIN

Sekarang ambil **SATU barang**.

Misalnya:

> Kopi Arabica.

Telusuri dari awal sampai akhir.

---

Supplier menjual kopi.

↓

Purchase Order

↓

Goods Receipt

↓

Inventory

↓

Supplier Invoice

↓

Accounts Payable

↓

Payment

↓

Warehouse

↓

Restaurant

↓

Recipe

↓

Kitchen

↓

Customer Order

↓

POS

↓

Payment

↓

Revenue

↓

Inventory Consumption

↓

Cost

↓

Profitability

↓

Accounting

---

Kemudian tanyakan:

> **“Apakah saya dapat menelusuri perjalanan satu barang ini dari supplier sampai menjadi revenue?”**

Jika iya:

> ERP mulai memiliki integrasi nyata.

---

# 51. FULL CUSTOMER CHAIN

Ambil satu customer.

Customer membeli:

Rp10.000.000.

---

Customer

↓

Quotation

↓

Sales Order

↓

Delivery

↓

Invoice

↓

Accounts Receivable

↓

Payment

↓

Bank

↓

Revenue

↓

Cost

↓

Profit

---

Kemudian customer melakukan:

> Return Rp2.000.000.

Telusuri kembali:

Customer

↓

Return

↓

Inventory

↓

Invoice Adjustment

↓

Receivable

↓

Accounting

---

# 52. FULL SUPPLIER CHAIN

Ambil satu supplier.

Supplier menjual:

Rp50.000.000.

Telusuri:

Supplier

↓

PO

↓

Receipt

↓

Inventory

↓

Invoice

↓

Payable

↓

Payment

↓

Bank

---

Kemudian:

Supplier memberikan:

> Credit Note Rp5.000.000.

Telusuri kembali.

---

# 53. FULL EMPLOYEE CHAIN

Ambil satu employee.

Employee:

* bekerja
* overtime
* mengambil leave
* menerima salary
* menerima reimbursement
* memiliki loan

Telusuri:

Employee

↓

Attendance

↓

Payroll

↓

Loan

↓

Reimbursement

↓

Payment

↓

Accounting

---

# 54. FULL RESTAURANT CHAIN

Ambil satu order.

Customer:

4 orang.

Table:

12.

Order:

Rp750.000.

Telusuri:

Customer

↓

Table

↓

Order

↓

Kitchen

↓

Recipe

↓

Ingredient

↓

Inventory

↓

POS

↓

Payment

↓

Revenue

↓

Cost

↓

Profitability

↓

Accounting

---

# 55. FULL INVENTORY CHAIN

Ambil:

100 unit Produk A.

Telusuri:

Purchase:

+100

↓

Warehouse:

100

↓

Transfer:

Warehouse A → B

↓

Sales:

-20

↓

Return:

+5

↓

Damage:

-3

↓

Stock Adjustment:

-2

↓

Remaining:

80

---

Kemudian tanyakan:

> **“Apakah angka 80 dapat dijelaskan?”**

Kalau tidak:

> inventory belum dapat dipercaya.

---

# 56. ACCOUNTING RECONCILIATION TEST

Ini salah satu testing paling penting.

Ambil periode:

> 1 bulan.

Bandingkan:

### POS

Total Sales

↓

### Sales

Total Sales

↓

### Payment

Total Payment

↓

### Inventory

Total Consumption

↓

### Accounting

Revenue / Cost / Cash / Receivable

---

Pertanyaannya:

> **Apakah angka-angka tersebut dapat direkonsiliasi?**

Tidak harus selalu sama secara mentah.

Yang penting:

> **setiap perbedaan dapat dijelaskan.**

---

# 57. THE “WHY” TEST

Jangan hanya melihat:

> Revenue = Rp1.000.000.000.

Tanyakan:

> Kenapa?

Kemudian:

> Customer mana?

> Invoice mana?

> Sales mana?

> Produk apa?

> Outlet mana?

> Payment mana?

> Cost-nya berapa?

> Inventory yang keluar berapa?

> Profit-nya berapa?

ERP yang sehat harus memungkinkan angka besar dipecah menjadi sumbernya.

---

# 58. THE “REVERSE” TEST

Testing jangan hanya:

**Transaction → Accounting**

Lakukan sebaliknya.

Dari Accounting:

> “Kenapa Revenue bulan ini Rp1 M?”

↓

Cari transaksi.

↓

Cari customer.

↓

Cari invoice.

↓

Cari sales.

↓

Cari barang.

---

Begitu juga:

> “Kenapa Expense Rp100 juta?”

↓

Cari expense.

↓

Cari payment.

↓

Cari supplier.

↓

Cari invoice.

---

Ini disebut secara bisnis sebagai:

> **Traceability**

---

# 59. THE “ONE TRANSACTION” TEST

Pilih satu transaksi secara acak.

Misalnya:

> Sales Invoice #INV-00125

Kemudian telusuri:

**Customer**

→ **Sales Order**

→ **Delivery**

→ **Inventory**

→ **Invoice**

→ **Payment**

→ **Accounting**

Jika salah satu mata rantai tidak dapat dijelaskan:

> catat sebagai gap.

---

# 60. THE “ONE RUPIAH” TEST

Ambil:

Rp1.

Kemudian tanyakan:

> “Uang ini berasal dari mana?”

Misalnya:

Customer payment.

↓

Invoice.

↓

Sales.

↓

Product.

↓

Inventory.

↓

Purchase.

↓

Supplier.

↓

Cost.

Dengan cara ini, Anda memaksa ERP menjelaskan:

> **asal dan perjalanan nilai finansial.**

---

# 61. THE “ONE ITEM” TEST

Ambil satu item:

> Kopi Arabica.

Pertanyakan:

> Dibeli dari siapa?

> Berapa harganya?

> Berapa yang diterima?

> Berapa yang masuk inventory?

> Berapa yang dipindahkan?

> Berapa yang dikonsumsi?

> Berapa yang dijual?

> Berapa yang terbuang?

> Berapa yang tersisa?

> Berapa nilai inventory?

> Berapa cost yang muncul?

---

# 62. THE “ONE CUSTOMER” TEST

Ambil satu customer.

Tanyakan:

> Berapa total pembeliannya?

> Berapa outstanding?

> Invoice mana yang belum dibayar?

> Berapa retur?

> Berapa discount?

> Berapa payment?

> Berapa credit limit?

> Berapa profitability customer?

---

# 63. THE “ONE SUPPLIER” TEST

Ambil satu supplier.

Tanyakan:

> Berapa total pembelian?

> Berapa hutang?

> Invoice mana yang belum dibayar?

> Berapa payment?

> Berapa return?

> Berapa discount?

---

# 64. THE “ONE EMPLOYEE” TEST

Ambil satu employee.

Tanyakan:

> Berapa salary?

> Berapa overtime?

> Berapa reimbursement?

> Berapa loan?

> Berapa deduction?

> Berapa net payment?

---

# 65. THE “NO DATA DISAPPEARS” TEST

Ini penting.

Jika transaksi:

**Void**

jangan berarti:

> transaksi menghilang.

Jika:

**Refund**

jangan berarti:

> transaksi awal hilang.

Jika:

**Return**

jangan berarti:

> penjualan awal dihapus.

Jika:

**Adjustment**

jangan berarti:

> angka lama diganti tanpa histori.

Prinsip:

> **Kejadian bisnis harus tetap dapat ditelusuri.**

---

# 66. THE “NO MONEY APPEARS FROM NOWHERE” TEST

Setiap uang yang masuk harus memiliki alasan.

Contoh:

Bank bertambah:

Rp100.000.000.

Pertanyaan:

> Dari mana?

Harus dapat ditelusuri.

Customer payment?

Loan?

Capital injection?

Transfer antar rekening?

Refund reversal?

---

# 67. THE “NO MONEY DISAPPEARS” TEST

Bank berkurang:

Rp50.000.000.

Pertanyaan:

> Ke mana?

Harus dapat ditelusuri.

Supplier payment?

Payroll?

Expense?

Asset purchase?

Transfer?

---

# 68. THE “NO STOCK APPEARS” TEST

Inventory bertambah:

100 unit.

Pertanyaan:

> Dari mana?

Purchase?

Return?

Transfer?

Adjustment?

Production?

---

# 69. THE “NO STOCK DISAPPEARS” TEST

Inventory berkurang:

100 unit.

Pertanyaan:

> Ke mana?

Sales?

Consumption?

Waste?

Damage?

Transfer?

Adjustment?

---

# 70. THE “ACCOUNTING IS THE JUDGE” TEST

Setelah seluruh module diuji:

Jangan kembali ke:

> “Apakah masing-masing module bekerja?”

Tanyakan:

> **“Apakah Accounting dapat menjelaskan apa yang terjadi di perusahaan?”**

Accounting harus mampu menjawab:

### Apa yang kita miliki?

**Assets**

### Apa yang kita hutangi?

**Liabilities**

### Berapa modal kita?

**Equity**

### Berapa yang kita hasilkan?

**Revenue**

### Berapa biaya kita?

**Expense**

### Apakah kita untung?

**Profit**

---

# 71. FULL ERP BUSINESS SIMULATION

Terakhir, buat perusahaan fiktif.

Contoh:

## PT Maju Bersama

Memiliki:

### Purchasing

2 staff

### Warehouse

1 warehouse

### Sales

3 staff

### Restaurant

1 outlet

### POS

3 cashier

### HR

20 employee

### Finance

2 staff

---

## Simulasikan 1 bulan.

### Minggu 1

Purchase:

Rp100 juta.

Sales:

Rp150 juta.

Payroll:

Rp50 juta.

Restaurant:

Rp30 juta.

---

### Minggu 2

Purchase:

Rp80 juta.

Sales:

Rp200 juta.

Restaurant:

Rp45 juta.

Waste:

Rp5 juta.

---

### Minggu 3

Purchase:

Rp120 juta.

Sales:

Rp180 juta.

Return:

Rp20 juta.

---

### Minggu 4

Sales:

Rp250 juta.

Payroll:

Rp50 juta.

Supplier Payment:

Rp150 juta.

Tax:

Rp30 juta.

---

Kemudian tutup bulan.

---

# 72. OWNER TEST

Sekarang jangan buka module satu per satu.

Bertindak sebagai Owner.

Tanyakan:

> **Berapa revenue bulan ini?**

> **Berapa cost?**

> **Berapa profit?**

> **Berapa cash yang kita punya?**

> **Berapa uang di bank?**

> **Berapa customer yang belum membayar?**

> **Berapa hutang supplier?**

> **Berapa nilai inventory?**

> **Berapa inventory yang hilang/rusak?**

> **Berapa biaya payroll?**

> **Berapa biaya restaurant?**

> **Outlet mana yang paling profitable?**

> **Produk apa yang paling menguntungkan?**

> **Customer mana yang paling besar nilainya?**

> **Supplier mana yang paling banyak menyerap cash?**

> **Kenapa profit turun?**

Dan pertanyaan paling penting:

> **“Dari mana angka ini berasal?”**

---

# 73. FINANCE TEST

Sekarang menjadi Finance.

Tanyakan:

> Apakah semua revenue memiliki sumber?

> Apakah semua expense memiliki sumber?

> Apakah semua payment dapat ditelusuri?

> Apakah AR dapat direkonsiliasi?

> Apakah AP dapat direkonsiliasi?

> Apakah inventory dapat direkonsiliasi?

> Apakah cash dapat direkonsiliasi?

> Apakah bank dapat direkonsiliasi?

> Apakah payroll dapat direkonsiliasi?

> Apakah tax dapat direkonsiliasi?

---

# 74. AUDITOR TEST

Sekarang berpura-pura menjadi auditor.

Ambil angka:

> Revenue Rp1.000.000.000.

Kemudian pilih secara acak:

10 transaksi.

Telusuri sampai sumber.

Kemudian pilih:

10 expense.

Telusuri sampai sumber.

Kemudian:

10 inventory movement.

Telusuri sampai sumber.

Kemudian:

10 payment.

Telusuri sampai sumber.

Pertanyaannya:

> **Apakah seluruh angka dapat dipertanggungjawabkan?**

---

# 75. FINAL ERP CHECKPOINT

ERP dapat dianggap memiliki integrasi yang sehat apabila:

### Sales

dapat menjelaskan:

> apa yang dijual.

### Inventory

dapat menjelaskan:

> apa yang keluar/masuk.

### Purchasing

dapat menjelaskan:

> apa yang dibeli.

### HRM

dapat menjelaskan:

> siapa yang bekerja dan berapa kewajibannya.

### POS

dapat menjelaskan:

> transaksi customer.

### Restaurant

dapat menjelaskan:

> bagaimana operasional makanan berlangsung.

### Payment

dapat menjelaskan:

> bagaimana uang bergerak.

### Accounting

dapat menjelaskan:

> **apa dampak finansial dari semuanya.**

---

# 76. CORE PRINCIPLE

Jangan berpikir:

**HRM**

**PO**

**SO**

**Inventory**

**POS**

**Restaurant**

**Accounting**

sebagai module terpisah.

Bayangkan sebagai:

> **satu perusahaan yang kebetulan aktivitasnya dibagi menjadi beberapa module.**

Karena di dunia nyata:

**Perusahaan tidak memiliki “module”.**

Perusahaan memiliki:

> **aktivitas bisnis.**

ERP hanya membantu merepresentasikan aktivitas tersebut.

---

# 77. TESTING PRINCIPLE TERAKHIR

Untuk setiap aktivitas, selalu tanyakan 7 pertanyaan:

### 1. Apa yang terjadi?

### 2. Siapa yang terlibat?

### 3. Apa yang berubah?

### 4. Apa yang masuk?

### 5. Apa yang keluar?

### 6. Apa dampaknya terhadap perusahaan?

### 7. Apakah dampaknya dapat dipertanggungjawabkan melalui Accounting?

Jika ketujuh pertanyaan tersebut dapat dijawab:

> **ERP mulai benar-benar terintegrasi.**

---

# MASTER FLOW

Secara keseluruhan:

**EMPLOYEE**

→ HRM

↓

**PURCHASING**

→ PO

↓

**SUPPLIER**

→ Inventory

↓

**WAREHOUSE**

↓

**SALES**

→ SO

↓

**CUSTOMER**

↓

**RESTAURANT / POS**

↓

**PAYMENT**

↓

**CASH / BANK**

↓

**ACCOUNTING**

↓

**FINANCIAL REPORT**

---

Dan dari sisi barang:

**Supplier**

↓

**Purchase**

↓

**Inventory**

↓

**Restaurant / Sales**

↓

**Customer**

↓

**Revenue**

↓

**Cost**

↓

**Profit**

---

Dari sisi uang:

**Customer**

↓

**Payment**

↓

**Cash / Bank**

↓

**Revenue**

↓

**Profit**

↓

**Company**

---

Dari sisi kewajiban:

**Company**

↓

**Supplier / Employee / Government**

↓

**Payable**

↓

**Payment**

↓

**Cash / Bank**

---

# KESIMPULAN

Testing module secara individual menjawab:

> **“Apakah module ini bekerja?”**

Testing antar-module menjawab:

> **“Apakah module-module ini bekerja bersama?”**

Tetapi testing ERP secara keseluruhan harus menjawab:

> **“Apakah sistem mampu menggambarkan perusahaan secara utuh?”**

Dan Accounting menjadi salah satu **checkpoint terakhir** untuk memvalidasi konsekuensi finansial dari aktivitas tersebut.

Bukan berarti semua jalan harus berakhir di jurnal secara langsung.

Tetapi pada akhirnya, jika suatu aktivitas **memiliki dampak finansial**, ERP harus mampu menjelaskan:

> **apa yang terjadi → kenapa terjadi → berapa nilainya → dari mana asalnya → ke mana dampaknya → dan bagaimana perusahaan mempertanggungjawabkannya.**

Itulah titik di mana ERP framework mulai berubah dari sekadar **kumpulan module** menjadi **sistem perusahaan yang benar-benar terintegrasi.**
