---
title: (Hospitality / Hotel) — 00. Profil Perusahaan & Master Data
category: accounting-hospitality
description: Skenario Hotel Bintang Indah (Hospitality) berbasis advance booking, deferred revenue, multi-currency (IDR/USD), dan integrasi pendapatan POS restoran/spa. Setup Currency, COA, Business Unit (Departemen), Fiscal Year, dan Saldo Awal.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

## Profil Perusahaan (Skenario)

**Hotel Bintang Indah** — hotel butik bintang 4 (fiktif) di Bali. Karakteristik bisnis: menerima pemesanan kamar di muka (advance booking) dengan pembayaran deposit (deferred revenue diakui saat check-out, bukan saat deposit diterima), transaksi multi-currency (IDR & USD) untuk tamu asing yang membayar deposit langsung ke rekening valas, serta pendapatan harian dari Point of Sales (POS) restoran dan spa yang direkap manual ke jurnal (modul POS itu sendiri TIDAK disentuh — hanya hasil rekapnya yang dijurnal, sama seperti pola "accounting berdiri sendiri" di suite lain).

Sudah menjadi **PKP** (PPN 11% untuk F&B/Spa). Untuk sewa kamar dikenakan **PB1 (Pajak Barang & Jasa Tertentu / Pajak Pembangunan 1) 10%** — **catatan penting**: PB1 adalah pajak daerah, bukan PPN, sehingga **tidak** dicatat lewat mekanisme `is_tax`/`tax_id` pada Chart of Accounts (yang di backend ini hanya mengenal satu tabel `taxes` dan dipakai `reports/tax-summary` sebatas PPN Masukan/Keluaran). PB1 diperlakukan sebagai **akun liabilitas manual biasa** (`LIA-03`), dihitung & dipisahkan manual di setiap baris jurnal pendapatan kamar — TIDAK akan pernah muncul di `reports/tax-summary` (itu murni laporan PPN). Ini dibuktikan di file `06`.

Fiscal Year: **FY2026** (2026-01-01 s/d 2026-12-31), periode **BULANAN** (`duration_type: "monthly"`). Mata uang operasional (base): **IDR**, mata uang transaksi asing: **USD**. Memiliki 3 departemen utama (Business Unit, dimensi profit center):

- **Departemen Kamar (Room)** — pendapatan sewa kamar.
- **Departemen F&B (Restoran)** — penjualan makanan & minuman.
- **Departemen Spa & Wellness** — jasa spa dan relaksasi.

## 1. Currency (**Currencies**)

Base currency branch defaultnya **IDR** (asumsi sudah ter-seed via `CurrencyTemplateService` saat branch dibuat — lihat catatan proyek). Perlu tambah **USD** untuk transaksi valas tamu asing.

| Skenario | Payload kunci                                                                                                                                                                      | Hasil                                                                                    |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Positif  | `POST client-master/currencies/create {country_name:"Amerika Serikat", name:"US Dollar", code:"USD", symbol:"$", thousand_separator:",", decimal_separator:".", decimal_places:2}` | 201 — dipakai transaksi valas §9 dan file `01`                                           |
| Negatif  | `code:"USD"` dikirim 2x (duplikat di branch yang sama)                                                                                                                             | 422 — validasi unique per branch (`currency_created_by_branch` pivot), lihat `content.*` |

## 2. Exchange Rates (**Exchange Rates**)

| Skenario                             | Payload kunci                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Hasil                                                                                                                                                     |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — rate awal                  | `POST client-master/exchange-rates/upsert {currency_id:<USD>, rate_date:"2026-01-01", rate_to_base:15500}`                                                                                                                                                                                                                                                                                                                                                                                                              | 201 — ini rate PERTAMA untuk USD di branch ini, otomatis `is_active:true`. `1 USD = Rp 15.500` berlaku untuk SEMUA transaksi valas berapapun tanggalnya, sampai ada rate lain yang di-`activate` eksplisit (`ExchangeRate::rateFor()` mengambil row `is_active=true`, `rate_date` cuma metadata, bukan penentu resolusi) |
| Positif — rate baru (rupiah melemah) | `POST .../upsert {currency_id:<USD>, rate_date:"2026-02-01", rate_to_base:15600}`                                                                                                                                                                                                                                                                                                                                                                                                                                       | 201 — TAPI ini rate KEDUA, TIDAK otomatis aktif. Harus `POST client-master/exchange-rates/activate {id:<rate 15.600>}` dulu sebelum dipakai — dites saat deposit USD tamu asing di file `01` §1.2                                                                                               |
| **Catatan kunci untuk §9 di bawah**  | `finance/bank-accounts::create` mengonversi `opening_balance` akun USD ke IDR pakai `CurrencyEngine::resolveRate()` — TIDAK ada parameter tanggal sama sekali, yang dipakai selalu rate USD yang SEDANG `is_active` di branch ini saat request dijalankan. Pastikan minimal 1 rate USD sudah pernah di-upsert (otomatis aktif kalau itu yang pertama) sebelum create bank account, kalau tidak resolve rate akan gagal | —                                                                                                                                                         |

## 3. Chart of Accounts (**Chart of Accounts**)

| Kode   | Nama Akun                                  | Tipe                     | Flag khusus                                                                                       |
| ------ | ------------------------------------------ | ------------------------ | ------------------------------------------------------------------------------------------------- |
| AST-01 | Kas Kasir Front Office                     | Aset Lancar              | `is_cash_account:true`, `balance_required:true`                                                   |
| AST-02 | Bank BCA Operasional (IDR)                 | Aset Lancar              | `is_cash_account:true`                                                                            |
| AST-03 | Bank Mandiri Valas (USD)                   | Aset Lancar              | `is_cash_account:true` — saldo awal via `finance/bank-accounts`, `currency_id:<USD>` (lihat §9)   |
| AST-04 | Piutang Agen Perjalanan (Travel Agent AR)  | Aset Lancar              | `is_ar_control_account:true`, `balance_required:true` — piutang ke Agoda/Booking.com              |
| AST-05 | PPN Masukan                                | Aset Lancar              | `is_tax:true`, `tax_id:<PPN 11%>`, `balance_required:true`                                        |
| AST-06 | Persediaan Bahan Baku F&B                  | Aset Lancar              | `balance_required:true`                                                                           |
| AST-07 | Peralatan & Perlengkapan Hotel             | Aset Tetap               | — (dipakai file `05`, diisi via jurnal manual, BUKAN opening balance)                             |
| AST-08 | Akumulasi Penyusutan Peralatan Hotel       | Aset Tetap               | Kontra-aset (saldo kredit) — dipakai file `05`                                                    |
| LIA-01 | Utang Dagang (Supplier F&B)                | Liabilitas Jangka Pendek | `is_ap_control_account:true`, `balance_required:true`                                             |
| LIA-02 | Uang Muka Pemesanan Kamar (Guest Deposit)  | Liabilitas Jangka Pendek | `balance_required:true` — pendapatan diterima dimuka sebelum tamu check-in                        |
| LIA-03 | Utang Pajak Pembangunan 1 (PB1 10%)        | Liabilitas Jangka Pendek | `balance_required:true` — pajak daerah manual, BUKAN akun `is_tax` (lihat catatan profil di atas) |
| LIA-04 | PPN Keluaran                               | Liabilitas Jangka Pendek | `is_tax:true`, `tax_id:<PPN 11%>`, `balance_required:true`                                        |
| LIA-05 | Utang PPh 21 Karyawan                      | Liabilitas Jangka Pendek | `balance_required:true`                                                                           |
| EKT-01 | Modal Pemilik                              | Ekuitas                  | `is_opening_balance_equity_account:true`                                                          |
| EKT-02 | Laba Ditahan                               | Ekuitas                  | `is_retained_earnings_account:true`                                                               |
| PDT-01 | Pendapatan Sewa Kamar                      | Pendapatan               | —                                                                                                 |
| PDT-02 | Pendapatan Restoran                        | Pendapatan               | —                                                                                                 |
| PDT-03 | Pendapatan Spa & Wellness                  | Pendapatan               | —                                                                                                 |
| BBN-01 | Beban Gaji & Upah Karyawan                 | Beban                    | —                                                                                                 |
| BBN-02 | Beban Perlengkapan Kamar (Guest Amenities) | Beban                    | —                                                                                                 |
| BBN-03 | Beban Penyusutan Peralatan Hotel           | Beban                    | Dipasang sebagai `depreciation_account_id` saat daftar aset di file `05`                          |
| BBN-04 | Beban Administrasi Bank                    | Beban                    | Dipakai file `06` (item penyesuai rekonsiliasi)                                                   |

Field validasi create COA sesuai `ChartOfAccounts::create()` aktual: `type_id` (required, harus milik branch aktif), `code`, `name`, `level` (required), `is_active`/`balance_required`/`is_tax`/`is_cash_account`/`is_ar_control_account`/`is_ap_control_account`/`is_retained_earnings_account`/`is_opening_balance_equity_account` (semua `nullable|boolean`), `tax_id` (nullable, exists `taxes`), `default_business_units_id` (nullable, exists `business_units`). Maksimal **1** akun boleh diflag `is_opening_balance_equity_account:true` dan **1** akun `is_retained_earnings_account:true` per branch (`assertAtMostOneFlaggedAccount`) — coba flag akun kedua dengan salah satu flag ini harus **422**.

## 4. Business Unit / Dimensi Departemen (**Business Units**)

Payload create hanya `code`, `name`, `parent_id` (nullable), `is_active`, `default_unit_type` (`in:cost,profit,both`, nullable) — TIDAK ada field lain.

| Skenario | Payload kunci                                                                     | Hasil                   |
| -------- | --------------------------------------------------------------------------------- | ----------------------- |
| Positif  | `{code:"DEPT-ROM", name:"Departemen Kamar", default_unit_type:"profit"}`          | 201                     |
| Positif  | `{code:"DEPT-FNB", name:"Departemen F&B", default_unit_type:"profit"}`            | 201                     |
| Positif  | `{code:"DEPT-SPA", name:"Departemen Spa & Wellness", default_unit_type:"profit"}` | 201                     |
| Negatif  | `code` duplikat di branch yang sama                                               | 422 (unique constraint) |

## 5. Fiscal Year & Accounting Period (**Fiscal Year**, **Accounting Period**)

| Skenario | Payload kunci                                                                                           | Hasil                                                         |
| -------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Positif  | `POST client-master/fiscal-year/create {name:"FY2026", start_date:"2026-01-01", end_date:"2026-12-31"}` | 201                                                           |
| Positif  | `PUT client-master/fiscal-year/generate-accounting-period {id:<FY2026>, duration_type:"monthly"}`       | 201 — 12 periode bulanan (Januari-Desember 2026) ter-generate |

## 6. Tax PPN (**Taxes**)

| Skenario | Payload kunci           | Hasil                                                 |
| -------- | ----------------------- | ----------------------------------------------------- |
| Positif  | `{name:"PPN", rate:11}` | 201 — `tax_id` ini dipasang di `AST-05`/`LIA-04` (§3) |

## 7. Contact (**Contacts**)

Payload create hanya: `name`, `type` (`in:supplier,customer,both`), `email`, `phone`, `npwp`, `currency_id`, `credit_limit`, `deposit_credit`/`deposit_debit`, `payment_term_days`, `is_active`, `is_consignment_supplier`/`is_consignment_customer`.

| Skenario | Payload kunci                                                              | Hasil                                                             |
| -------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Positif  | `{name:"Agoda Company Pte Ltd", type:"customer", payment_term_days:30}`    | 201 — dipakai sebagai OTA/agen perjalanan, piutangnya ke `AST-04` |
| Positif  | `{name:"Booking.com B.V.", type:"customer", payment_term_days:30}`         | 201                                                               |
| Positif  | `{name:"CV Sumber Boga Nusantara", type:"supplier", payment_term_days:30}` | 201 — supplier bahan baku F&B, piutangnya ke `LIA-01`             |

## 8. Saldo Awal Perusahaan (**Chart of Accounts Balances**, **Bank Accounts**)

Field create `chart-of-accounts-balances`: `chart_of_account_id` (required, harus `balance_required:true`), `currency_id` (required), `opening_balance`/`debit_total`/`credit_total` (nullable numeric), `is_locked` (nullable boolean). Field create `bank-accounts`: `account_name`, `bank_name`, `account_number`, `currency_id`, `opening_balance`, `chart_of_account_id`.

Saldo awal baru **masuk ke GL** setelah `JournalPostingService::syncOpeningBalance()` memposting jurnal ke akun yang diflag `is_opening_balance_equity_account` (EKT-01) — bukan cuma dekoratif di tabel balance. Untuk `AST-03` (akun USD), `opening_balance` diisi dalam **satuan USD** (bukan ekuivalen IDR manual) — sistem yang mengonversi otomatis ke IDR via `CurrencyEngine` (lihat catatan §2).

| Akun                              |   Saldo Awal | Jalur                                                                                                                   |
| --------------------------------- | -----------: | ----------------------------------------------------------------------------------------------------------------------- |
| AST-01 Kas Kasir Front Office     |   10.000.000 | `chart-of-accounts-balances`, `currency_id:<IDR>`                                                                       |
| AST-02 Bank BCA Operasional (IDR) |  350.000.000 | `finance/bank-accounts`, `currency_id:<IDR>`                                                                            |
| AST-03 Bank Mandiri Valas (USD)   | 10.000 (USD) | `finance/bank-accounts`, `currency_id:<USD>` → ekuivalen IDR **155.000.000** (10.000 × 15.500, rate 2026-01-01 dari §2) |
| AST-04 Piutang Agen Perjalanan    |   45.000.000 | `chart-of-accounts-balances`                                                                                            |
| AST-06 Persediaan Bahan Baku F&B  |   12.000.000 | `chart-of-accounts-balances`                                                                                            |
| LIA-01 Utang Dagang               |   30.000.000 | `chart-of-accounts-balances`                                                                                            |
| LIA-02 Uang Muka Pemesanan Kamar  |   75.000.000 | `chart-of-accounts-balances` — deposit booking tamu masa depan                                                          |
| LIA-03 Utang PB1                  |    8.000.000 | `chart-of-accounts-balances`                                                                                            |
| LIA-04 PPN Keluaran               |    5.000.000 | `chart-of-accounts-balances`                                                                                            |
| LIA-05 Utang PPh 21 Karyawan      |    2.000.000 | `chart-of-accounts-balances`                                                                                            |

Total Aset = 10.000.000 + 350.000.000 + 155.000.000 + 45.000.000 + 12.000.000 = **572.000.000**
Total Liabilitas = 30.000.000 + 75.000.000 + 8.000.000 + 5.000.000 + 2.000.000 = **120.000.000**
→ **Modal Pemilik (EKT-01) otomatis bersaldo kredit 452.000.000** (572.000.000 − 120.000.000)

| Skenario                | Detail                                                                                                                          | Hasil                                                                                                                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — verifikasi GL | `general-ledger/trial-balance` setelah semua saldo awal di atas dibuat                                                          | Trial Balance balanced, Total Debit = Total Kredit = **572.000.000**, `EKT-01` bersaldo kredit `452.000.000`                                                                                            |
| Negatif                 | `chart-of-accounts-balances/create` dengan `chart_of_account_id` mengarah ke akun yang `balance_required:false` (mis. `PDT-01`) | 422/error — `content.*` "This COA does not require a balance record"                                                                                                                                    |
| Negatif                 | `bank-accounts/create` dengan `currency_id:<USD>` TAPI belum ada `exchange-rates` ter-upsert untuk USD sama sekali              | Error saat `syncOpeningBalance` — `CurrencyEngine` gagal resolve rate (cek behavior aktual: exception vs fallback rate 0) — kalau fallback ke 0 tanpa warning eksplisit → 🔧 catat sebagai temuan kecil |

## Referensi Silang

- File `01` — semua transaksi jurnal booking/POS memakai kode akun & Business Unit di atas.
- File `05` — `AST-07`/`AST-08`/`BBN-03` dipakai saat registrasi & penyusutan aset tetap (BUKAN bagian saldo awal, sengaja mulai dari nol).
- File `06` — `BBN-04` dipakai item penyesuai rekonsiliasi bank; PB1 (`LIA-03`) dibuktikan TIDAK muncul di `reports/tax-summary`.
