---
title: (E-commerce) — 00. Profil Perusahaan & Master Data
category: accounting-ecommerce
description: Skenario PT Dagang Cepat (E-commerce) berbasis volume transaksi tinggi, multi-payment gateway, inventory, dan refund. Setup Chart of Account Type, Chart of Accounts, Business Unit (Channel), Fiscal Year, Accounting Period, Contact, dan Saldo Awal.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

## Profil Perusahaan (Skenario)

**PT Dagang Cepat** — perusahaan ritel e-commerce (fiktif) yang menjual produk elektronik konsumen secara online melalui website sendiri dan marketplace. Karakteristik bisnis: volume transaksi harian sangat tinggi, pembayaran menggunakan multi-payment gateway (Midtrans, Xendit) dan saldo marketplace (Shopee, Tokopedia), serta adanya retur/refund dari pelanggan.

Sudah menjadi **PKP** (PPN 11%). Memiliki 2 channel penjualan utama (Business Unit):

- **Channel Website** — penjualan langsung via web resmi.
- **Channel Marketplace** — penjualan via Shopee & Tokopedia.

Fiscal Year **FY2026**, periode akuntansi **BULANAN**.

> **Ruang lingkup**: Accounting berdiri sendiri — TIDAK menyentuh Purchase Order/Sales Order/POS maupun dokumen turunannya, sama seperti suite `accounting/` dan `accounting-manufaktur-2/`.

## 1. Chart of Account Type (`client-master/chart-of-account-types`)

| Nama                     | Kategori (`category`) | Saldo Normal (`normal_balance`) | Arus Kas (`cash_flow_section`) | Grup Laporan (`report_group`) |
| ------------------------ | --------------------- | ------------------------------- | ------------------------------ | ----------------------------- |
| Aset Lancar              | asset                 | debit                           | operating                      | Balance Sheet                 |
| Aset Tetap               | asset                 | debit                           | investing                      | Balance Sheet                 |
| Liabilitas Jangka Pendek | liability             | credit                          | operating                      | Balance Sheet                 |
| Ekuitas                  | equity                | credit                          | financing                      | Balance Sheet                 |
| Pendapatan               | revenue               | credit                          | operating                      | Income Statement              |
| Beban                    | expense               | debit                           | operating                      | Income Statement              |

## 2. Chart of Accounts (**Chart of Accounts**)

| Kode   | Nama Akun                                | Tipe                     | Flag khusus                                                                                       |
| ------ | ---------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------- |
| AST-01 | Bank BCA Operasional                     | Aset Lancar              | `is_cash_account: true`                                                                           |
| AST-02 | Saldo Payment Gateway (Midtrans/Xendit)  | Aset Lancar              | `is_cash_account: true`, `balance_required: true` — dana mengendap di PG sebelum ditarik ke bank  |
| AST-03 | Saldo Marketplace (Shopee/Tokopedia Pay) | Aset Lancar              | `is_cash_account: true`, `balance_required: true` — dana mengendap di marketplace sebelum ditarik |
| AST-04 | Piutang COD (Cash on Delivery)           | Aset Lancar              | `is_ar_control_account: true`, `balance_required: true` — dana di kurir ekspedisi                 |
| AST-05 | Persediaan Barang Dagang                 | Aset Lancar              | `balance_required: true`                                                                          |
| AST-06 | PPN Masukan                              | Aset Lancar              | `is_tax: true`, `tax_id: <PPN 11%>`                                                               |
| AST-07 | Peralatan Gudang                         | Aset Tetap               | —                                                                                                 |
| AST-08 | Akumulasi Penyusutan Peralatan Gudang    | Aset Tetap               | Kontra-aset (kredit) — dipakai sebagai `accum_dep_account_id` di modul Fixed Assets               |
| LIA-01 | Utang Dagang (Supplier)                  | Liabilitas Jangka Pendek | `is_ap_control_account: true`, `balance_required: true`                                           |
| LIA-02 | PPN Keluaran                             | Liabilitas Jangka Pendek | `is_tax: true`, `tax_id: <PPN 11%>`                                                               |
| EKT-01 | Modal Pemilik                            | Ekuitas                  | `is_opening_balance_equity_account: true`                                                         |
| EKT-02 | Laba Ditahan                             | Ekuitas                  | `is_retained_earnings_account: true`                                                              |
| PDT-01 | Pendapatan Penjualan E-commerce          | Pendapatan               | —                                                                                                 |
| PDT-02 | Retur & Potongan Penjualan               | Pendapatan               | Kontra-pendapatan (debit) — mencatat refund/retur barang                                          |
| BBN-01 | Harga Pokok Penjualan (HPP)              | Beban                    | —                                                                                                 |
| BBN-02 | Beban Biaya Admin Payment Gateway & MP   | Beban                    | Biaya potongan per transaksi dari PG/Marketplace                                                  |
| BBN-03 | Beban Ongkos Kirim Subsidi               | Beban                    | Subsidi ongkir gratis untuk pelanggan                                                             |
| BBN-04 | Beban Penyusutan Peralatan Gudang        | Beban                    | Dipakai sebagai `depreciation_account_id` di modul Fixed Assets                                   |
| BBN-05 | Beban Administrasi Bank                  | Beban                    | Dipakai di file `06` untuk jurnal penyesuaian rekonsiliasi bank                                   |

> **Catatan penting (bukan asumsi)**: field `chart_of_accounts` yang divalidasi di `App\Http\Controllers\ClientMaster\ChartOfAccounts::create()` termasuk `code`, `name`, `type_id`, dan flag boolean di atas. `balance_required: true` WAJIB di-set untuk AST-02/AST-03/AST-04/AST-05/LIA-01 karena keempatnya akan diposting saldo awal lewat **Chart of Accounts Balances** — endpoint itu menolak (`content.not_found_in_branch`-style validator error: "This COA does not require a balance record.") kalau `balance_required` masih `false`.

## 3. Business Unit / Dimensi Channel (**Business Units**)

- **Channel Website** (`code: CHN-WEB`)
- **Channel Marketplace** (`code: CHN-MP`)

## 4. Fiscal Year (**Fiscal Year**) & Accounting Period (**Accounting Period**)

| Field        | Nilai            |
| ------------ | ---------------- |
| `code`       | FY2026           |
| `name`       | Fiscal Year 2026 |
| `start_date` | 2026-01-01       |
| `end_date`   | 2026-12-31       |
| `is_active`  | true             |

Setelah Fiscal Year dibuat, generate periode lewat `client-master/fiscal-year/generate-accounting-period` (method `PUT`) dengan `duration_type: "monthly"` → menghasilkan 12 Accounting Period (2026-01 s.d. 2026-12). Posting saldo awal (§6) mensyaratkan ada Accounting Period yang **meng-cover tanggal hari ini** dan berstatus `is_closed: false, is_locked: false` (lihat `ChartOfAccountBalances::resolveCurrentPeriod()`) — kerjakan generate periode SEBELUM Saldo Awal.

## 5. Contact (**Contacts**)

| Nama                      | Tipe     | Catatan                                   |
| ------------------------- | -------- | ----------------------------------------- |
| Midtrans Indonesia        | supplier | Payment gateway partner (untuk referensi) |
| PT Sumber Elektronik Jaya | supplier | Supplier utama produk elektronik          |
| Umum (Pelanggan Retail)   | customer | Pelanggan individual, tidak per-nama      |

## 6. Saldo Awal Perusahaan (**Bank Accounts**, **Chart of Accounts Balances**)

| Akun                            |  Saldo Awal | Jalur                        | Wajib isi                                                                                            |
| ------------------------------- | ----------: | ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| AST-01 Bank BCA Operasional     | 200.000.000 | `finance/bank-accounts`      | `chart_of_account_id` = AST-01 (kalau kosong, opening_balance TIDAK diposting ke GL — lihat catatan) |
| AST-02 Saldo Payment Gateway    |  15.000.000 | `chart-of-accounts-balances` | `currency_id` (wajib, IDR)                                                                           |
| AST-03 Saldo Marketplace        |  35.000.000 | `chart-of-accounts-balances` | `currency_id`                                                                                        |
| AST-04 Piutang COD              |   8.000.000 | `chart-of-accounts-balances` | `currency_id`                                                                                        |
| AST-05 Persediaan Barang Dagang | 120.000.000 | `chart-of-accounts-balances` | `currency_id`                                                                                        |
| LIA-01 Utang Dagang             |  45.000.000 | `chart-of-accounts-balances` | `currency_id`                                                                                        |

Total Aset = 200.000.000 + 15.000.000 + 35.000.000 + 8.000.000 + 120.000.000 = **378.000.000**
Total Liabilitas = **45.000.000**
→ **Modal Pemilik (EKT-01) otomatis bersaldo kredit 333.000.000** (via `JournalPostingService::syncOpeningBalance()`, satu jurnal per akun: Dr {akun} / Cr Modal Pemilik).

## Skenario Pengujian

| Skenario | Detail                                                                                                                      | Hasil                                                                                                                                                                                    |
| -------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | Create Chart of Account Type "Aset Lancar" (`category: asset`, `normal_balance: debit`).                                    | 201, tipe akun terbuat.                                                                                                                                                                  |
| Positif  | Create Chart of Accounts AST-02 dengan `balance_required: true`, `is_cash_account: true`.                                   | 201, akun terbuat.                                                                                                                                                                       |
| Positif  | Create Business Unit CHN-WEB & CHN-MP.                                                                                      | 201 masing-masing.                                                                                                                                                                       |
| Positif  | Create Fiscal Year FY2026, lalu `PUT client-master/fiscal-year/generate-accounting-period` dengan `duration_type: monthly`. | 201 fiscal year, lalu 12 Accounting Period (2026-01 s.d. 2026-12) terbuat sekaligus (endpoint ini SELALU wipe periode lama fiscal year tsb dulu sebelum generate ulang).                 |
| Positif  | Create Bank Account "BCA Operasional" dengan `chart_of_account_id` = AST-01, `opening_balance: 200000000`.                  | 201, DAN otomatis posting jurnal Dr AST-01 / Cr EKT-01 200.000.000 ke GL (`opening_balance_journal_header_id` terisi).                                                                   |
| Positif  | Create Chart of Accounts Balance untuk AST-02 (`opening_balance: 15000000`, `currency_id` wajib diisi).                     | 201, jurnal Dr AST-02 / Cr EKT-01 15.000.000 terposting otomatis.                                                                                                                        |
| Negatif  | Create Chart of Accounts Balance untuk akun yang `balance_required: false` (mis. PDT-01).                                   | Ditolak — validator error "This COA does not require a balance record."                                                                                                                  |
| Negatif  | Create Chart of Accounts Balance TANPA `currency_id`.                                                                       | 422 — `currency_id` required.                                                                                                                                                            |
| Negatif  | Create Chart of Accounts Balance SEBELUM Accounting Period untuk hari ini dibuat (skip §4).                                 | Ditolak dengan error "No active accounting period found for today's date. Please generate accounting periods first."                                                                     |
| Negatif  | Create Bank Account TANPA `chart_of_account_id`.                                                                            | 201 tetap sukses (field nullable) TAPI `opening_balance` TIDAK terposting ke GL sama sekali (silent no-op) — jangan asumsikan saldo otomatis masuk Trial Balance kalau field ini kosong. |

## Netralisasi

- Hapus Chart of Accounts Balance yang dibuat via `chart-of-accounts-balances/delete` — otomatis mereverse jurnal opening balance terkait (amount di-set ulang ke 0 lewat `syncOpeningBalance`).
- Hapus Bank Account via `finance/bank-accounts/delete` — begitu juga otomatis mereverse jurnal opening balance-nya.
- Reopen/hapus Accounting Period & Fiscal Year jika perlu setup ulang (`client-master/accounting-period/reopen`, lalu `delete`).
