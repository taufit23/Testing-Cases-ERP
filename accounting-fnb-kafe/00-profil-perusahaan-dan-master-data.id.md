---
title: (F&B Kafe) — 00. Profil Perusahaan & Master Data
category: accounting-fnb-kafe
description: Skenario rantai kafe fiktif (PT Kopi Nusantara Berjaya, 3 outlet) berbasis volume transaksi harian sangat tinggi tapi nilai kecil — dasar seluruh test case modul Accounting, plus setup Chart of Accounts, Fiscal Year bulanan, Business Unit per outlet, Tax, Contact, dan Saldo Awal.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

> **Pola tiap skenario**: **Positif** (jalur normal, harus sukses) / **Negatif** (input/urutan salah, harus DITOLAK dengan pesan jelas — bukan crash/500, bukan silent-success) / **Netralisasi** (cara mengembalikan state ke semula setelah testing).
>
> File ini adalah **fondasi** — semua file test case lainnya (01-06) mengasumsikan master data & saldo awal di file ini sudah ada persis seperti yang tertulis, karena file 01 dst menelusuri angka secara presisi (debit=kredit dicek baris per baris). Kerjakan file ini PALING PERTAMA, dan JANGAN ubah nilai apapun di §9 (Saldo Awal) kalau mau angka-angka di file 01-06 tetap valid.
>
> **Ruang lingkup suite ini**: khusus modul Accounting berdiri sendiri (keputusan scope yang sama seperti 2 suite lain, `../accounting/` dan `../accounting-manufaktur/`) — TIDAK mencakup Purchase Order/Sales Order/POS maupun dokumen turunannya. Transaksi penjualan harian dicatat lewat **jurnal manual** (merepresentasikan rekap kasir/EOD report yang direkap akuntan ke jurnal), BUKAN lewat modul Sales/POS beneran.

## Profil Perusahaan (Skenario)

**PT Kopi Nusantara Berjaya** — rantai kafe/kedai kopi kekinian (fiktif, terinspirasi struktur bisnis nyata rantai kafe grab-and-go di Indonesia: banyak gerai kecil, transaksi ritel harian dalam jumlah SANGAT BANYAK tapi nilai per transaksi kecil — order tunggal biasanya Rp 15.000-60.000). Skala usaha jauh lebih kecil per-transaksi dibanding retail minimarket (`../accounting/`) atau manufaktur pangan (`../accounting-manufaktur/`), sehingga **akurasi akumulasi ribuan baris kecil ke laporan keuangan** jadi fokus utama suite ini — bukan kompleksitas satu transaksi besar.

Sudah menjadi **PKP** (wajib PPN 11%). Beroperasi dengan 3 outlet (Business Unit) yang aktif sekaligus, semua di Jakarta:

- **Outlet Kemang** — flagship, volume tersinggi, buka sejak lama.
- **Outlet Senayan** — outlet kedua, volume menengah (perkantoran, ramai jam makan siang).
- **Outlet BSD** — outlet terbaru (baru ekspansi), volume terkecil, sedang investasi peralatan & renovasi (dipakai skenario Aset Tetap di file `05`).

Setiap outlet punya kasir sendiri yang memegang kas fisik harian (uang tunai dari pelanggan) — kas ini baru disetor ke rekening bank pusat secara berkala (mingguan di suite ini), sehingga ada jeda waktu antara "kas tercatat di pembukuan" dan "kas benar-benar masuk rekening bank" — dipakai skenario Rekonsiliasi Bank di file `06`.

Tahun buku mengikuti kalender (Januari-Desember), **periode akuntansi BULANAN** (beda dari suite manufaktur yang kuartalan — kafe tutup buku tiap bulan karena volume transaksi tinggi butuh kontrol lebih sering). Mata uang operasional: **IDR (Rupiah)** — suite ini sengaja TIDAK menyentuh multi-currency (sudah dites lengkap di `../accounting-manufaktur/02-multi-currency-dan-selisih-kurs.id.md`), fokus penuh ke volume & akurasi.

## 1. Currency (**Currencies**)

| Skenario    | Detail                                                                | Hasil                                                              |
| ----------- | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Positif     | Pastikan `IDR` sudah ada (biasanya sudah ter-seed dari template Core) | 201 atau sudah ada, tersedia di `client-master/currencies/options` |
| Netralisasi | — (master global, jangan dihapus)                                     |

## 2. Chart of Account Type (**Chart of Account Type**)

| #   | Kode | Nama                     | `category` | `normal_balance` | `cash_flow_section` | Catatan                                          | Grup Laporan (`report_group`) |
| --- | ---- | ------------------------ | ---------- | ---------------- | ------------------- | ------------------------------------------------ | ----------------------------- |
| 1   | AL   | Aset Lancar              | asset      | debit            | operating           | Kas kasir, Bank, Piutang, Persediaan bahan baku  | Balance Sheet                 |
| 2   | AT   | Aset Tetap               | asset      | debit            | investing           | Peralatan dapur, renovasi interior               | Balance Sheet                 |
| 3   | LJP  | Liabilitas Jangka Pendek | liability  | credit           | operating           | Utang dagang, PPN Keluaran, voucher belum redeem | Balance Sheet                 |
| 4   | EK   | Ekuitas                  | equity     | credit           | financing           | Modal, laba ditahan                              | Balance Sheet                 |
| 5   | PD   | Pendapatan               | revenue    | credit           | operating           | Penjualan minuman & makanan                      | Income Statement              |
| 6   | BB   | Beban                    | expense    | debit            | operating           | HPP, gaji, listrik, penyusutan                   | Income Statement              |

| Skenario    | Detail                                                                                     | Hasil         |
| ----------- | ------------------------------------------------------------------------------------------ | ------------- |
| Positif     | Create ke-6 tipe di atas satu-satu                                                         | 201 tiap tipe |
| Negatif     | `normal_balance: "salah"`                                                                  | 422           |
| Negatif     | `category` kosong                                                                          | 422           |
| Netralisasi | `delete` tipe test — pastikan tidak ada `chart_of_accounts` yang masih pakai `type_id` ini |

## 3. Chart of Accounts (**Chart of Accounts**)

COA representatif untuk kafe multi-outlet — dipakai di SEMUA file berikutnya:

| Kode   | Nama Akun                                      | Tipe                     | Flag khusus                                                                                                                                                                                  |
| ------ | ---------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AST-01 | Kas Kasir Outlet Kemang                        | Aset Lancar              | `is_cash_account: true`, `balance_required: true`, `default_business_units_id: <Kemang>`                                                                                                     |
| AST-02 | Kas Kasir Outlet Senayan                       | Aset Lancar              | `is_cash_account: true`, `balance_required: true`, `default_business_units_id: <Senayan>`                                                                                                    |
| AST-03 | Kas Kasir Outlet BSD                           | Aset Lancar              | `is_cash_account: true`, `balance_required: true`, `default_business_units_id: <BSD>`                                                                                                        |
| AST-04 | Bank BCA Operasional (Pusat)                   | Aset Lancar              | `is_cash_account: true` (saldo awal via `finance/bank-accounts`, BUKAN `chart-of-accounts-balances`)                                                                                         |
| AST-05 | Piutang Dagang                                 | Aset Lancar              | `is_ar_control_account: true`, `balance_required: true`                                                                                                                                      |
| AST-06 | Persediaan Bahan Baku F&B                      | Aset Lancar              | `balance_required: true` (kopi, susu, sirup, kemasan)                                                                                                                                        |
| AST-07 | PPN Masukan                                    | Aset Lancar              | `is_tax: true`, `tax_id: <PPN 11%>`                                                                                                                                                          |
| AST-08 | Peralatan Dapur & Mesin Kopi                   | Aset Tetap               | — (dipakai file `05`)                                                                                                                                                                        |
| AST-09 | Akumulasi Penyusutan Peralatan Dapur           | Aset Tetap               | Kontra-aset — `normal_balance` tetap ikut induk (debit), bersaldo negatif karena selalu **dikredit**                                                                                         |
| AST-10 | Renovasi Interior Outlet BSD                   | Aset Tetap               | — (leasehold improvement, dipakai file `05`)                                                                                                                                                 |
| AST-11 | Akumulasi Penyusutan Renovasi Interior         | Aset Tetap               | Kontra-aset, sama seperti AST-09                                                                                                                                                             |
| LIA-01 | Utang Dagang                                   | Liabilitas Jangka Pendek | `is_ap_control_account: true`, `balance_required: true`                                                                                                                                      |
| LIA-02 | PPN Keluaran                                   | Liabilitas Jangka Pendek | `is_tax: true`, `tax_id: <PPN 11%>`                                                                                                                                                          |
| LIA-03 | Utang PPh 21 Karyawan                          | Liabilitas Jangka Pendek | `balance_required: true`                                                                                                                                                                     |
| LIA-04 | Pendapatan Diterima Dimuka (Voucher/Gift Card) | Liabilitas Jangka Pendek | `balance_required: true` — kewajiban voucher kopi prabayar yang belum diredeem pelanggan                                                                                                     |
| EKT-01 | Modal Pemilik                                  | Ekuitas                  | `is_opening_balance_equity_account: true` — **WAJIB tepat 1 akun** ber-flag ini                                                                                                              |
| EKT-02 | Laba Ditahan                                   | Ekuitas                  | `is_retained_earnings_account: true` — **WAJIB tepat 1 akun** ber-flag ini                                                                                                                   |
| PDT-01 | Pendapatan Penjualan Minuman                   | Pendapatan               | — (dimensi outlet lewat `business_unit_id` per baris jurnal, BUKAN akun terpisah per outlet)                                                                                                 |
| PDT-02 | Pendapatan Penjualan Makanan                   | Pendapatan               | —                                                                                                                                                                                            |
| BBN-01 | Harga Pokok Penjualan (HPP Bahan Baku F&B)     | Beban                    | —                                                                                                                                                                                            |
| BBN-02 | Beban Gaji Karyawan (Barista/Kasir)            | Beban                    | —                                                                                                                                                                                            |
| BBN-03 | Beban Listrik & Gas                            | Beban                    | —                                                                                                                                                                                            |
| BBN-04 | Beban Selisih Kas Kasir                        | Beban                    | Dipakai skenario opname kas kasir, file `01` §1.13                                                                                                                                           |
| BBN-05 | Beban Penyusutan Peralatan Dapur               | Beban                    | Dipakai file `05`                                                                                                                                                                            |
| BBN-06 | Beban Penyusutan Renovasi Interior             | Beban                    | Dipakai file `05`                                                                                                                                                                            |
| BBN-07 | Beban Sewa Outlet                              | Beban                    | Akun tersedia untuk eksperimen tambahan (akrual sewa) — TIDAK dipakai transaksi wajib di baseline suite ini, sama seperti pola akun cadangan di suite manufaktur (`PDT-02`/`BBN-03` di sana) |

| Skenario                                                     | Detail                                                                                                                                                    | Hasil                                                                                                                                                                                                                     |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                      | Create ke-26 akun di atas satu-satu, atau pakai `create-bulk`                                                                                             | 201, semua muncul di list dengan flag tersimpan benar (regression check field-drop)                                                                                                                                       |
| **Positif — verifikasi field control-account tersimpan**     | Setelah create akun AST-01/AST-05/AST-06/LIA-01/LIA-03/LIA-04/EKT-01/EKT-02, `GET .../show` ulang                                                         | Flag `is_ar_control_account`/`is_ap_control_account`/`is_retained_earnings_account`/`balance_required`/`is_opening_balance_equity_account` sesuai yang dikirim, BUKAN `false`/`null` diam-diam                            |
| **Positif — `default_business_units_id` per akun kas kasir** | `GET .../show` AST-01/AST-02/AST-03                                                                                                                       | Masing-masing menunjuk outlet-nya sendiri — dipakai sebagai default dimensi saat entry jurnal manual di FE (mempercepat input, mengurangi salah pilih outlet saat rekap harian volume tinggi)                             |
| Negatif                                                      | `type_id` tidak ada di branch aktif                                                                                                                       | 422 `not_found_in_branch`                                                                                                                                                                                                 |
| Negatif                                                      | Create akun ke-2 dengan `is_retained_earnings_account: true` (padahal EKT-02 sudah ada)                                                                   | Tidak ada validasi silang yang menolak ini saat ini (regresi temuan yang sama seperti 2 suite lain — `FiscalYear::closeYear()` nanti akan menolak dengan pesan `more_than_one_account_is_flagged...`, dites di file `03`) |
| Negatif                                                      | Create akun ke-2 dengan `is_opening_balance_equity_account: true` (padahal EKT-01 sudah ada)                                                              | Tidak ada validasi silang — kalau ada 2 akun ber-flag ini, `JournalPostingService::syncOpeningBalance()` pakai `first()`, HANYA akun pertama yang kepakai. Jangan sengaja buat 2 akun ber-flag ini                        |
| **Positif — kontra-aset (edge case penting)**                | Setelah file `05` men-kredit AST-09/AST-11, cek saldo di Trial Balance                                                                                    | Saldo harus **negatif** (mengurangi total Aset Tetap)                                                                                                                                                                     |
| Netralisasi                                                  | `delete` akun test — cek dulu tidak ada `journals`/`general_ledgers` yang mereferensikannya; kalau sudah dipakai, JANGAN dihapus, cukup `is_active=false` |

## 4. Fiscal Year (**Fiscal Year**)

| Skenario    | Payload                                                                                   | Hasil |
| ----------- | ----------------------------------------------------------------------------------------- | ----- |
| Positif     | `{code:"FY2026", name:"Tahun Buku 2026", start_date:"2026-01-01", end_date:"2026-12-31"}` | 201   |
| Negatif     | `end_date` sebelum `start_date`                                                           | 422   |
| Netralisasi | `delete` — pastikan tidak ada `accounting_periods` di bawahnya                            |

## 5. Accounting Period (**Accounting Period**)

| Skenario                   | Detail                                                                                               | Hasil                                                                            |
| -------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Positif — generate BULANAN | `PUT client-master/fiscal-year/generate-accounting-period {fiscal_year_id, duration_type:"monthly"}` | 12 periode (Jan-Des 2026) ter-generate, semua `is_closed:false, is_locked:false` |
| Negatif                    | Generate lagi untuk fiscal year yang sama                                                            | Ditolak/duplikat — cek behavior aktual, laporkan kalau malah generate duplikat   |
| Netralisasi                | `delete` periode test satu-satu, atau `delete` fiscal year                                           |

## 6. Business Unit / Dimensi Outlet (**Business Units**)

| Skenario                 | Payload                                                                                                             | Hasil                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Positif — Outlet Kemang  | `{code:"OTL-KMG", name:"Outlet Kemang", default_unit_type:"both"}`                                                  | 201                                                                                                        |
| Positif — Outlet Senayan | `{code:"OTL-SNY", name:"Outlet Senayan", default_unit_type:"both"}`                                                 | 201                                                                                                        |
| Positif — Outlet BSD     | `{code:"OTL-BSD", name:"Outlet BSD", default_unit_type:"both"}`                                                     | 201 — dipakai membandingkan pendapatan/biaya per outlet lewat filter dimensi di General Ledger (file `02`) |
| Negatif                  | `default_unit_type` di luar enum (`cost/profit/both`)                                                               | 422                                                                                                        |
| Netralisasi              | `delete` — pastikan tidak dipakai `journals.business_unit_id`/`chart_of_accounts.default_business_units_id` manapun |

## 7. Tax — PPN (**Taxes**)

| Skenario    | Payload                                                              | Hasil                                                                                                       |
| ----------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Positif     | `{name:"PPN 11%", code:"PPN11", rate:11, effect:"increase"}`         | 201 — dipakai di hampir SETIAP jurnal penjualan harian file `01` (ribuan baris kecil, akurasi rate krusial) |
| Negatif     | `rate` > 100                                                         | 422                                                                                                         |
| Negatif     | `effect` bukan `increase`/`decrease`                                 | 422                                                                                                         |
| Netralisasi | `delete` — pastikan tidak dipakai `chart_of_accounts.tax_id` manapun |

## 8. Contact — Customer & Supplier (**Contacts**)

Dipakai sebagai referensi di jurnal manual file `01` (paket voucher korporat via Piutang Dagang, dan pembelian bahan baku kredit via Utang Dagang) — BUKAN via dokumen Sales/Purchase Invoice, sesuai scope suite ini.

| Skenario           | Payload                                                                     | Hasil                                                                                 |
| ------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Positif — Customer | `{name:"PT Solusi Rapat Sejahtera", type:"customer", payment_term_days:30}` | 201 — klien korporat yang beli paket voucher kopi untuk meeting/event kantor (kredit) |
| Positif — Supplier | `{name:"CV Sumber Nikmat Boga", type:"supplier", payment_term_days:30}`     | 201 — supplier bahan baku F&B (kopi, susu, sirup) untuk restock mingguan              |
| Negatif            | `type` di luar enum (`supplier/customer/both`)                              | 422                                                                                   |
| Netralisasi        | `delete` — pastikan belum dipakai dokumen transaksi manapun                 |

## 9. Saldo Awal Perusahaan / Opening Balance (**Chart of Accounts Balances**, **Bank Accounts**)

**Prasyarat**: dikerjakan SETELAH §3 (COA) dan §5 (Accounting Period) — sebelum mulai transaksi harian di file `01-jurnal-harian-penjualan-dan-akumulasi.id.md`. Sama seperti 2 suite lain, jurnal saldo awal ini di-tanggal-i **hari ini (tanggal server saat tombol ditekan)** lewat `JournalPostingService::syncOpeningBalance()`, BUKAN tanggal yang kamu pilih — pastikan ada Accounting Period yang meng-cover tanggal hari ini dan masih terbuka.

**Skenario saldo awal** (angka kompak, per outlet, mudah ditelusuri manual):

| Akun                              | Saldo Awal | Jalur                                                                                              |
| --------------------------------- | ---------: | -------------------------------------------------------------------------------------------------- |
| AST-01 Kas Kasir Outlet Kemang    |  2.000.000 | `chart-of-accounts-balances`                                                                       |
| AST-02 Kas Kasir Outlet Senayan   |  1.500.000 | `chart-of-accounts-balances`                                                                       |
| AST-03 Kas Kasir Outlet BSD       |  1.000.000 | `chart-of-accounts-balances`                                                                       |
| AST-04 Bank BCA Operasional       | 50.000.000 | `finance/bank-accounts` (field `opening_balance`)                                                  |
| AST-05 Piutang Dagang             |  8.000.000 | `chart-of-accounts-balances`                                                                       |
| AST-06 Persediaan Bahan Baku F&B  | 15.000.000 | `chart-of-accounts-balances`                                                                       |
| LIA-01 Utang Dagang               |  6.000.000 | `chart-of-accounts-balances`                                                                       |
| LIA-03 Utang PPh 21 Karyawan      |    800.000 | `chart-of-accounts-balances`                                                                       |
| LIA-04 Pendapatan Diterima Dimuka |  3.000.000 | `chart-of-accounts-balances` — voucher kopi yang sudah terjual sebelum periode ini, belum diredeem |

Total Aset = 2.000.000+1.500.000+1.000.000+50.000.000+8.000.000+15.000.000 = **77.500.000**
Total Liabilitas = 6.000.000+800.000+3.000.000 = **9.800.000**
→ **Modal Pemilik (EKT-01) otomatis bersaldo kredit 67.700.000** (77,5jt − 9,8jt) setelah semua entri di atas diposting — ini poin verifikasi utama §9.4.

### 9.1 Guard — coba isi saldo awal SEBELUM ada akun equity ber-flag

| Skenario | Detail                                                                                                                                                                                                                       | Hasil                                                                  |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Negatif  | Pastikan dulu BELUM ada akun manapun ber-flag `is_opening_balance_equity_account`, lalu `POST client-master/chart-of-accounts-balances/create {chart_of_account_id: <AST-01>, currency_id: <IDR>, opening_balance: 2000000}` | Ditolak `no_opening_balance_equity_account_configured_for_this_branch` |
| Negatif  | `chart_of_account_id` menunjuk akun `balance_required: false` (mis. PDT-01)                                                                                                                                                  | Ditolak — "This COA does not require a balance record."                |

### 9.2 Flag Modal Pemilik jadi akun offset saldo awal

| Skenario | Payload                                                                                              | Hasil                                 |
| -------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------- |
| Positif  | `PUT client-master/chart-of-accounts/update {id: <EKT-01>, is_opening_balance_equity_account: true}` | 200, `GET .../show` konfirmasi `true` |

### 9.3 Saldo Awal Bank Account — Bank BCA Operasional (**Bank Accounts**)

| Skenario    | Payload                                                                                                                                                                                                           | Hasil                                                                                                                                                                      |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `POST finance/bank-accounts/create {account_name:"BCA Operasional Pusat", bank_name:"Bank Central Asia", account_number:"9871234560", currency_id:<IDR>, chart_of_account_id:<AST-04>, opening_balance:50000000}` | 201 — `opening_balance_journal_header_id` terisi, cek `accounting/journals/list` ada jurnal `JRN-OB-...`: Dr AST-04 50.000.000 / Cr EKT-01 50.000.000, status `JRN_POSTED` |
| Netralisasi | Simpan bank account ini untuk dipakai file `06` (Rekonsiliasi Bank) — JANGAN dihapus                                                                                                                              |

### 9.4 Saldo Awal via Chart of Account Balances — akun sisanya

Urutkan create satu-satu (tiap create memposting 1 jurnal `JRN-OB-...` sendiri, Dr akun / Cr EKT-01 — kecuali akun liability yang arahnya kebalikan):

| Skenario                                           | Payload                                                                       | Hasil                                                                                               |
| -------------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Positif — Kas Kasir Kemang                         | `{chart_of_account_id:<AST-01>, currency_id:<IDR>, opening_balance:2000000}`  | Dr AST-01 / Cr EKT-01, 2.000.000                                                                    |
| Positif — Kas Kasir Senayan                        | `{chart_of_account_id:<AST-02>, currency_id:<IDR>, opening_balance:1500000}`  | Dr AST-02 / Cr EKT-01, 1.500.000                                                                    |
| Positif — Kas Kasir BSD                            | `{chart_of_account_id:<AST-03>, currency_id:<IDR>, opening_balance:1000000}`  | Dr AST-03 / Cr EKT-01, 1.000.000                                                                    |
| Positif — Piutang Dagang                           | `{chart_of_account_id:<AST-05>, currency_id:<IDR>, opening_balance:8000000}`  | Dr AST-05 / Cr EKT-01, 8.000.000                                                                    |
| Positif — Persediaan Bahan Baku                    | `{chart_of_account_id:<AST-06>, currency_id:<IDR>, opening_balance:15000000}` | Dr AST-06 / Cr EKT-01, 15.000.000                                                                   |
| Positif — Utang Dagang (liability, arah kebalikan) | `{chart_of_account_id:<LIA-01>, currency_id:<IDR>, opening_balance:6000000}`  | **Cr LIA-01 / Dr EKT-01**, 6.000.000 — verifikasi arah ini benar (`normal_balance` LIA-01 = credit) |
| Positif — Utang PPh 21 Karyawan                    | `{chart_of_account_id:<LIA-03>, currency_id:<IDR>, opening_balance:800000}`   | Cr LIA-03 / Dr EKT-01, 800.000                                                                      |
| Positif — Pendapatan Diterima Dimuka               | `{chart_of_account_id:<LIA-04>, currency_id:<IDR>, opening_balance:3000000}`  | Cr LIA-04 / Dr EKT-01, 3.000.000                                                                    |
| Negatif                                            | `opening_balance` sebagai string, atau `currency_id` yang tidak ada           | 422                                                                                                 |
| Negatif                                            | `chart_of_account_id` dari branch lain                                        | 422 `not_found_in_branch`                                                                           |

### 9.5 Verifikasi ke General Ledger / Trial Balance

| Skenario | Detail                                                                  | Hasil                                                                                                                                                    |
| -------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/trial-balance` setelah §9.3+9.4 lengkap | `total_debit = total_credit`, saldo EKT-01 Modal Pemilik = **kredit 67.700.000 tepat** — kalau tidak sama persis, ada entri yang salah arah atau kelewat |
| Positif  | Cek `accounting/journals/list` filter kode `JRN-OB-*`                   | Total 9 jurnal (8 dari §9.4 + 1 dari §9.3), semua `status: JRN_POSTED`, semua `is_reversed: false`                                                       |

## Ringkasan Data Master yang Harus Sudah Ada Sebelum Lanjut

- [ ] Currency IDR
- [ ] 6 Chart of Account Type dengan `normal_balance`/`category`/`cash_flow_section` benar
- [ ] 26 Chart of Accounts (lihat §3), termasuk flag `is_cash_account`/`is_ar_control_account`/`is_ap_control_account`/`is_retained_earnings_account`/`balance_required`/`is_opening_balance_equity_account`/`default_business_units_id` tersimpan benar
- [ ] Fiscal Year FY2026 + 12 Accounting Period BULANAN
- [ ] 3 Business Unit (Outlet Kemang, Outlet Senayan, Outlet BSD)
- [ ] Tax PPN 11%
- [ ] 1 Contact customer (PT Solusi Rapat Sejahtera) + 1 Contact supplier (CV Sumber Nikmat Boga)
- [ ] Saldo awal terposting untuk 8 akun (§9): Kas Kemang 2jt, Kas Senayan 1,5jt, Kas BSD 1jt, Bank BCA 50jt, Piutang 8jt, Persediaan 15jt, Utang Dagang 6jt, Utang PPh21 800rb, Pendapatan Diterima Dimuka 3jt — Modal Pemilik otomatis 67,7jt, Trial Balance balanced

## Referensi Silang

- [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) — dasar pola §9 Saldo Awal (versi retail, bulanan, 2 toko)
- [`../accounting-manufaktur/00-profil-perusahaan-dan-master-data.id.md`](../accounting-manufaktur/00-profil-perusahaan-dan-master-data.id.md) — versi kuartalan dengan multi-currency, dasar pola dimensi Business Unit di jurnal
- §9: implementasi `App\Services\JournalPostingService::syncOpeningBalance()`, dipanggil dari `ClientMaster\ChartOfAccountBalances` dan `Finance\BankAccounts`
- Endpoint Fixed Assets terkonfirmasi via `routes/fixed_assets.php`: prefix `fixed-assets/assets/*` dan `fixed-assets/disposals/*` (BUKAN `finance/fixed-assets/*` — catatan koreksi dari pola penulisan di suite manufaktur, dipakai konsisten mulai file `01`/`05` di suite ini)
