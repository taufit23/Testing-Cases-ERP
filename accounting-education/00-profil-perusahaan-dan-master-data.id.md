---
title: (Yayasan Pendidikan) — 00. Profil Perusahaan & Master Data
category: accounting-education
description: Skenario yayasan pendidikan fiktif (Yayasan Cerdas Mandiri, 2 jenjang SD & SMP) — dasar seluruh test case modul Accounting, plus setup Chart of Accounts, Fiscal Year bulanan, Business Unit per jenjang, Contact, dan Saldo Awal.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

> **Pola tiap skenario**: **Positif** (jalur normal, harus sukses) / **Negatif** (input/urutan salah, harus DITOLAK dengan pesan jelas — bukan crash/500, bukan silent-success) / **Netralisasi** (cara mengembalikan state ke semula setelah testing).
>
> File ini adalah **fondasi** — semua file test case lainnya (01-06) mengasumsikan master data & saldo awal di file ini sudah ada persis seperti yang tertulis, karena file 01 dst menelusuri angka secara presisi (debit=kredit dicek baris per baris). Kerjakan file ini PALING PERTAMA, dan JANGAN ubah nilai apapun di §8 (Saldo Awal) kalau mau angka-angka di file 01-06 tetap valid.
>
> **Ruang lingkup suite ini**: khusus modul Accounting berdiri sendiri (keputusan scope yang sama seperti suite retail/manufaktur/F&B) — TIDAK mencakup Purchase Order/Sales Order/POS maupun dokumen turunannya. Semua transaksi (billing SPP, penerimaan, gaji guru, dsb) dicatat lewat **jurnal manual** (merepresentasikan rekap bendahara/tata usaha yang direkap akuntan yayasan ke jurnal), BUKAN lewat modul Sales/Purchasing beneran.

## Profil Perusahaan (Skenario)

**Yayasan Cerdas Mandiri** — yayasan pendidikan fiktif yang menaungi 2 jenjang sekolah dalam satu kompleks: **SD Cerdas Mandiri** dan **SMP Cerdas Mandiri**. Sumber pendapatan utama: SPP bulanan siswa dan uang pangkal (biaya masuk) siswa baru yang diakui **bertahap (amortisasi)** selama satu tahun ajaran, bukan diakui sekaligus saat diterima. Yayasan memberi keringanan/beasiswa parsial ke sejumlah siswa kurang mampu — dicatat sebagai **potongan kontra-pendapatan**, bukan sebagai beban.

**Jasa pendidikan formal TIDAK dikenakan PPN** (dikecualikan berdasarkan aturan perpajakan Indonesia) — suite ini SENGAJA tidak punya akun/skenario PPN Keluaran atas SPP maupun uang pangkal, berbeda dari suite retail/F&B/manufaktur. Pembelian ATK dari supplier dicatat sebesar nilai bruto (yayasan bukan PKP, tidak mengkreditkan PPN Masukan) — lihat catatan eksplisit di file `06` §3 untuk alasan keputusan scope ini.

Dua **Business Unit** dipakai sebagai dimensi jenjang (bukan cabang/lokasi seperti suite retail/F&B — di sini dipakai memisahkan pendapatan & beban SD vs SMP dalam satu entitas yayasan):

- **SD Cerdas Mandiri** — jenjang SD, 150 siswa aktif, SPP Rp 500.000/siswa/bulan.
- **SMP Cerdas Mandiri** — jenjang SMP, 100 siswa aktif, SPP Rp 650.000/siswa/bulan.

Tahun ajaran/buku mengikuti kalender (Januari-Desember), **periode akuntansi BULANAN**. Mata uang operasional: **IDR (Rupiah)** — suite ini TIDAK menyentuh multi-currency (sudah dites lengkap di `../accounting-manufaktur-2/02-multi-currency-dan-selisih-kurs.id.md`).

## 1. Currency (**Currencies**)

| Skenario    | Detail                                                                | Hasil                                                              |
| ----------- | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Positif     | Pastikan `IDR` sudah ada (biasanya sudah ter-seed dari template Core) | 201 atau sudah ada, tersedia di `client-master/currencies/options` |
| Netralisasi | — (master global, jangan dihapus)                                     |

## 2. Chart of Account Type (**Chart of Account Type**)

| #   | Kode | Nama                     | `category` | `normal_balance` | `cash_flow_section` | Catatan                                              | Grup Laporan (`report_group`) |
| --- | ---- | ------------------------ | ---------- | ---------------- | ------------------- | ---------------------------------------------------- | ----------------------------- |
| 1   | AL   | Aset Lancar              | asset      | debit            | operating           | Kas bendahara, Bank, Piutang SPP, Perlengkapan/ATK   | Balance Sheet                 |
| 2   | AT   | Aset Tetap               | asset      | debit            | investing           | Gedung sekolah, Peralatan laboratorium               | Balance Sheet                 |
| 3   | LJP  | Liabilitas Jangka Pendek | liability  | credit           | operating           | Utang usaha, Utang PPh 21, Uang pangkal belum diakui | Balance Sheet                 |
| 4   | EK   | Ekuitas                  | equity     | credit           | financing           | Modal/aset bersih yayasan, saldo dana                | Balance Sheet                 |
| 5   | PD   | Pendapatan               | revenue    | credit           | operating           | SPP, uang pangkal (diakui bertahap)                  | Income Statement              |
| 6   | BB   | Beban                    | expense    | debit            | operating           | Gaji guru, listrik, ATK, penyusutan                  | Income Statement              |

| Skenario    | Detail                                                                                     | Hasil         |
| ----------- | ------------------------------------------------------------------------------------------ | ------------- |
| Positif     | Create ke-6 tipe di atas satu-satu                                                         | 201 tiap tipe |
| Negatif     | `normal_balance: "salah"`                                                                  | 422           |
| Negatif     | `category` kosong                                                                          | 422           |
| Netralisasi | `delete` tipe test — pastikan tidak ada `chart_of_accounts` yang masih pakai `type_id` ini |

## 3. Chart of Accounts (**Chart of Accounts**)

| Kode   | Nama Akun                                          | Tipe                     | Flag khusus                                                                                              |
| ------ | -------------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------- |
| AST-01 | Kas Bendahara SD                                   | Aset Lancar              | `is_cash_account: true`, `balance_required: true`, `default_business_units_id: <SD>`                     |
| AST-02 | Kas Bendahara SMP                                  | Aset Lancar              | `is_cash_account: true`, `balance_required: true`, `default_business_units_id: <SMP>`                    |
| AST-03 | Bank BNI Operasional Yayasan                       | Aset Lancar              | `is_cash_account: true` (saldo awal via `finance/bank-accounts`, BUKAN `chart-of-accounts-balances`)     |
| AST-04 | Piutang SPP                                        | Aset Lancar              | `is_ar_control_account: true`, `balance_required: true`                                                  |
| AST-05 | Perlengkapan Belajar & ATK                         | Aset Lancar              | `balance_required: true`                                                                                 |
| AST-06 | Gedung Sekolah (Renovasi & Penambahan Ruang Kelas) | Aset Tetap               | — (dipakai file `05`, `category: building`)                                                              |
| AST-07 | Akumulasi Penyusutan Gedung Sekolah                | Aset Tetap               | Kontra-aset — `normal_balance` tetap ikut induk (debit), bersaldo negatif karena selalu **dikredit**     |
| AST-08 | Peralatan Laboratorium IPA                         | Aset Tetap               | — (dipakai file `05`, `category: equipment`)                                                             |
| AST-09 | Akumulasi Penyusutan Peralatan Laboratorium        | Aset Tetap               | Kontra-aset, sama seperti AST-07                                                                         |
| LIA-01 | Utang Usaha                                        | Liabilitas Jangka Pendek | `is_ap_control_account: true`, `balance_required: true`                                                  |
| LIA-02 | Utang PPh 21 Guru & Karyawan                       | Liabilitas Jangka Pendek | `balance_required: true`                                                                                 |
| LIA-03 | Pendapatan Diterima Dimuka — Uang Pangkal          | Liabilitas Jangka Pendek | `balance_required: true` — uang pangkal siswa baru yang belum diamortisasi jadi pendapatan               |
| EKT-01 | Modal/Aset Bersih Yayasan                          | Ekuitas                  | `is_opening_balance_equity_account: true` — **WAJIB tepat 1 akun** ber-flag ini                          |
| EKT-02 | Saldo Dana Tidak Terikat (Laba Ditahan)            | Ekuitas                  | `is_retained_earnings_account: true` — **WAJIB tepat 1 akun** ber-flag ini                               |
| PDT-01 | Pendapatan SPP                                     | Pendapatan               | — (dimensi jenjang lewat `business_unit_id` per baris jurnal, BUKAN akun terpisah per jenjang)           |
| PDT-02 | Pendapatan Uang Pangkal (Diamortisasi)             | Pendapatan               | Diakui bertahap dari LIA-03, lihat file `01` §1.4                                                        |
| PDT-03 | Potongan/Beasiswa SPP                              | Pendapatan               | Kontra-pendapatan — `normal_balance` tetap ikut induk (credit), bersaldo **debit** karena selalu didebit |
| BBN-01 | Beban Gaji Guru & Karyawan                         | Beban                    | —                                                                                                        |
| BBN-02 | Beban Listrik & Air                                | Beban                    | —                                                                                                        |
| BBN-03 | Beban Perlengkapan Belajar (ATK Terpakai)          | Beban                    | —                                                                                                        |
| BBN-04 | Beban Selisih Kas Bendahara                        | Beban                    | Dipakai skenario opname kas bendahara, file `01` §1.11                                                   |
| BBN-05 | Beban Penyusutan Gedung Sekolah                    | Beban                    | Dipakai file `05`                                                                                        |
| BBN-06 | Beban Penyusutan Peralatan Laboratorium            | Beban                    | Dipakai file `05`                                                                                        |
| BBN-07 | Beban Sewa/Perawatan Fasilitas                     | Beban                    | Akun cadangan untuk eksperimen tambahan — TIDAK dipakai transaksi wajib di baseline suite ini            |

| Skenario                                                         | Detail                                                                                                                                                    | Hasil                                                                                                                                                                                              |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                          | Create ke-23 akun di atas satu-satu, atau pakai `create-bulk`                                                                                             | 201, semua muncul di list dengan flag tersimpan benar (regression check field-drop)                                                                                                                |
| **Positif — verifikasi field control-account tersimpan**         | Setelah create akun AST-01/AST-04/AST-05/LIA-01/LIA-03/EKT-01/EKT-02, `GET .../show` ulang                                                                | Flag `is_ar_control_account`/`is_ap_control_account`/`is_retained_earnings_account`/`balance_required`/`is_opening_balance_equity_account` sesuai yang dikirim, BUKAN `false`/`null` diam-diam     |
| **Positif — `default_business_units_id` per akun kas bendahara** | `GET .../show` AST-01/AST-02                                                                                                                              | Masing-masing menunjuk jenjangnya sendiri — dipakai default dimensi saat entry jurnal manual di FE                                                                                                 |
| Negatif                                                          | `type_id` tidak ada di branch aktif                                                                                                                       | 422 `not_found_in_branch`                                                                                                                                                                          |
| Negatif                                                          | Create akun ke-2 dengan `is_retained_earnings_account: true` (padahal EKT-02 sudah ada)                                                                   | Tidak ada validasi silang yang menolak ini saat ini (regresi temuan yang sama seperti suite lain — `FiscalYear::closeYear()` nanti akan menolak, dites di file `03`)                               |
| Negatif                                                          | Create akun ke-2 dengan `is_opening_balance_equity_account: true` (padahal EKT-01 sudah ada)                                                              | Tidak ada validasi silang — kalau ada 2 akun ber-flag ini, `JournalPostingService::syncOpeningBalance()` pakai `first()`, HANYA akun pertama yang kepakai. Jangan sengaja buat 2 akun ber-flag ini |
| **Positif — kontra-aset & kontra-pendapatan (edge case)**        | Setelah AST-07/AST-09 dikredit (file `05`) dan PDT-03 didebit (file `01` §1.2), cek saldo di Trial Balance                                                | AST-07/AST-09 harus **negatif** (mengurangi Aset Tetap); PDT-03 harus **positif sebagai kontra** (mengurangi total Pendapatan SPP saat dijumlah dengan PDT-01)                                     |
| Netralisasi                                                      | `delete` akun test — cek dulu tidak ada `journals`/`general_ledgers` yang mereferensikannya; kalau sudah dipakai, JANGAN dihapus, cukup `is_active=false` |

## 4. Fiscal Year (**Fiscal Year**)

| Skenario    | Payload                                                                                     | Hasil |
| ----------- | ------------------------------------------------------------------------------------------- | ----- |
| Positif     | `{code:"FY2026", name:"Tahun Ajaran 2026", start_date:"2026-01-01", end_date:"2026-12-31"}` | 201   |
| Negatif     | `end_date` sebelum `start_date`                                                             | 422   |
| Netralisasi | `delete` — pastikan tidak ada `accounting_periods` di bawahnya                              |

## 5. Accounting Period (**Fiscal Year — `generate-accounting-period`**, **Accounting Period**)

| Skenario                   | Detail                                                                                               | Hasil                                                                            |
| -------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Positif — generate BULANAN | `PUT client-master/fiscal-year/generate-accounting-period {fiscal_year_id, duration_type:"monthly"}` | 12 periode (Jan-Des 2026) ter-generate, semua `is_closed:false, is_locked:false` |
| Negatif                    | Generate lagi untuk fiscal year yang sama                                                            | Ditolak/duplikat — cek behavior aktual, laporkan kalau malah generate duplikat   |
| Netralisasi                | `delete` periode test satu-satu, atau `delete` fiscal year                                           |

## 6. Business Unit / Dimensi Jenjang (**Business Units**)

| Skenario      | Payload                                                                                                             | Hasil                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Positif — SD  | `{code:"BU-SD", name:"SD Cerdas Mandiri", default_unit_type:"both"}`                                                | 201                                                                                                         |
| Positif — SMP | `{code:"BU-SMP", name:"SMP Cerdas Mandiri", default_unit_type:"both"}`                                              | 201 — dipakai membandingkan pendapatan/biaya per jenjang lewat filter dimensi di General Ledger (file `02`) |
| Negatif       | `default_unit_type` di luar enum (`cost/profit/both`)                                                               | 422                                                                                                         |
| Netralisasi   | `delete` — pastikan tidak dipakai `journals.business_unit_id`/`chart_of_accounts.default_business_units_id` manapun |

## 7. Contact — Supplier ATK (**Contacts**)

Dipakai sebagai referensi di jurnal manual file `01` (pembelian ATK kredit) — BUKAN via dokumen Purchase Invoice, sesuai scope suite ini. Karena SPP dicatat lewat rekap billing massal per jenjang (bukan per invoice per siswa), suite ini TIDAK membuat 1 Contact per siswa — cukup 1 Contact supplier ATK.

| Skenario           | Payload                                                             | Hasil                                     |
| ------------------ | ------------------------------------------------------------------- | ----------------------------------------- |
| Positif — Supplier | `{name:"CV Sumber Edukasi", type:"supplier", payment_term_days:30}` | 201 — supplier ATK & perlengkapan belajar |
| Negatif            | `type` di luar enum (`supplier/customer/both`)                      | 422                                       |
| Netralisasi        | `delete` — pastikan belum dipakai dokumen transaksi manapun         |

## 8. Saldo Awal Perusahaan / Opening Balance (**Chart of Accounts Balances**, **Bank Accounts**)

**Prasyarat**: dikerjakan SETELAH §3 (COA) dan §5 (Accounting Period) — sebelum mulai transaksi di file `01-jurnal-spp-dan-beasiswa.id.md`. Sama seperti suite lain, jurnal saldo awal ini di-tanggal-i **hari ini (tanggal server saat tombol ditekan)** lewat `JournalPostingService::syncOpeningBalance()`, BUKAN tanggal yang kamu pilih — pastikan ada Accounting Period yang meng-cover tanggal hari ini dan masih terbuka.

| Akun                                             | Saldo Awal | Jalur                                                                          |
| ------------------------------------------------ | ---------: | ------------------------------------------------------------------------------ |
| AST-01 Kas Bendahara SD                          |  3.000.000 | `chart-of-accounts-balances`                                                   |
| AST-02 Kas Bendahara SMP                         |  2.500.000 | `chart-of-accounts-balances`                                                   |
| AST-03 Bank BNI Operasional                      | 80.000.000 | `finance/bank-accounts` (field `opening_balance`)                              |
| AST-04 Piutang SPP                               | 12.000.000 | `chart-of-accounts-balances`                                                   |
| AST-05 Perlengkapan Belajar & ATK                |  6.000.000 | `chart-of-accounts-balances`                                                   |
| LIA-01 Utang Usaha                               |  4.000.000 | `chart-of-accounts-balances`                                                   |
| LIA-02 Utang PPh 21 Guru & Karyawan              |  1.200.000 | `chart-of-accounts-balances`                                                   |
| LIA-03 Pendapatan Diterima Dimuka — Uang Pangkal | 18.000.000 | `chart-of-accounts-balances` — uang pangkal siswa baru yang belum diamortisasi |

Total Aset = 3.000.000+2.500.000+80.000.000+12.000.000+6.000.000 = **103.500.000**
Total Liabilitas = 4.000.000+1.200.000+18.000.000 = **23.200.000**
→ **Modal/Aset Bersih Yayasan (EKT-01) otomatis bersaldo kredit 80.300.000** (103,5jt − 23,2jt) setelah semua entri di atas diposting — ini poin verifikasi utama §8.5.

### 8.1 Guard — coba isi saldo awal SEBELUM ada akun equity ber-flag

| Skenario | Detail                                                                                                                                                                                                                       | Hasil                                                                  |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Negatif  | Pastikan dulu BELUM ada akun manapun ber-flag `is_opening_balance_equity_account`, lalu `POST client-master/chart-of-accounts-balances/create {chart_of_account_id: <AST-01>, currency_id: <IDR>, opening_balance: 3000000}` | Ditolak `no_opening_balance_equity_account_configured_for_this_branch` |
| Negatif  | `chart_of_account_id` menunjuk akun `balance_required: false` (mis. PDT-01)                                                                                                                                                  | Ditolak — "This COA does not require a balance record."                |

### 8.2 Flag Modal/Aset Bersih Yayasan jadi akun offset saldo awal

| Skenario | Payload                                                                                              | Hasil                                 |
| -------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------- |
| Positif  | `PUT client-master/chart-of-accounts/update {id: <EKT-01>, is_opening_balance_equity_account: true}` | 200, `GET .../show` konfirmasi `true` |

### 8.3 Saldo Awal Bank Account — Bank BNI Operasional (**Bank Accounts**)

| Skenario    | Payload                                                                                                                                                                                                                 | Hasil                                                                                                                                                                      |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `POST finance/bank-accounts/create {account_name:"BNI Operasional Yayasan", bank_name:"Bank Negara Indonesia", account_number:"0123456789", currency_id:<IDR>, chart_of_account_id:<AST-03>, opening_balance:80000000}` | 201 — `opening_balance_journal_header_id` terisi, cek `accounting/journals/list` ada jurnal `JRN-OB-...`: Dr AST-03 80.000.000 / Cr EKT-01 80.000.000, status `JRN_POSTED` |
| Netralisasi | Simpan bank account ini untuk dipakai file `06` (Rekonsiliasi Bank) — JANGAN dihapus                                                                                                                                    |

### 8.4 Saldo Awal via Chart of Account Balances — akun sisanya

Urutkan create satu-satu (tiap create memposting 1 jurnal `JRN-OB-...` sendiri, Dr akun / Cr EKT-01 — kecuali akun liability yang arahnya kebalikan):

| Skenario                                          | Payload                                                                       | Hasil                                                                                               |
| ------------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Positif — Kas Bendahara SD                        | `{chart_of_account_id:<AST-01>, currency_id:<IDR>, opening_balance:3000000}`  | Dr AST-01 / Cr EKT-01, 3.000.000                                                                    |
| Positif — Kas Bendahara SMP                       | `{chart_of_account_id:<AST-02>, currency_id:<IDR>, opening_balance:2500000}`  | Dr AST-02 / Cr EKT-01, 2.500.000                                                                    |
| Positif — Piutang SPP                             | `{chart_of_account_id:<AST-04>, currency_id:<IDR>, opening_balance:12000000}` | Dr AST-04 / Cr EKT-01, 12.000.000                                                                   |
| Positif — Perlengkapan Belajar & ATK              | `{chart_of_account_id:<AST-05>, currency_id:<IDR>, opening_balance:6000000}`  | Dr AST-05 / Cr EKT-01, 6.000.000                                                                    |
| Positif — Utang Usaha (liability, arah kebalikan) | `{chart_of_account_id:<LIA-01>, currency_id:<IDR>, opening_balance:4000000}`  | **Cr LIA-01 / Dr EKT-01**, 4.000.000 — verifikasi arah ini benar (`normal_balance` LIA-01 = credit) |
| Positif — Utang PPh 21 Guru & Karyawan            | `{chart_of_account_id:<LIA-02>, currency_id:<IDR>, opening_balance:1200000}`  | Cr LIA-02 / Dr EKT-01, 1.200.000                                                                    |
| Positif — Pendapatan Diterima Dimuka Uang Pangkal | `{chart_of_account_id:<LIA-03>, currency_id:<IDR>, opening_balance:18000000}` | Cr LIA-03 / Dr EKT-01, 18.000.000                                                                   |
| Negatif                                           | `opening_balance` sebagai string, atau `currency_id` yang tidak ada           | 422                                                                                                 |
| Negatif                                           | `chart_of_account_id` dari branch lain                                        | 422 `not_found_in_branch`                                                                           |

### 8.5 Verifikasi ke General Ledger / Trial Balance

| Skenario | Detail                                                                  | Hasil                                                                                                                                                    |
| -------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/trial-balance` setelah §8.3+8.4 lengkap | `total_debit = total_credit`, saldo EKT-01 Modal Yayasan = **kredit 80.300.000 tepat** — kalau tidak sama persis, ada entri yang salah arah atau kelewat |
| Positif  | Cek `accounting/journals/list` filter kode `JRN-OB-*`                   | Total 8 jurnal (7 dari §8.4 + 1 dari §8.3), semua `status: JRN_POSTED`, semua `is_reversed: false`                                                       |

## Ringkasan Data Master yang Harus Sudah Ada Sebelum Lanjut

- [ ] Currency IDR
- [ ] 6 Chart of Account Type dengan `normal_balance`/`category`/`cash_flow_section` benar
- [ ] 23 Chart of Accounts (lihat §3), termasuk flag `is_cash_account`/`is_ar_control_account`/`is_ap_control_account`/`is_retained_earnings_account`/`balance_required`/`is_opening_balance_equity_account`/`default_business_units_id` tersimpan benar
- [ ] Fiscal Year FY2026 + 12 Accounting Period BULANAN
- [ ] 2 Business Unit (SD Cerdas Mandiri, SMP Cerdas Mandiri)
- [ ] 1 Contact supplier (CV Sumber Edukasi)
- [ ] Saldo awal terposting untuk 7 akun (§8): Kas SD 3jt, Kas SMP 2,5jt, Bank BNI 80jt, Piutang SPP 12jt, Perlengkapan/ATK 6jt, Utang Usaha 4jt, Utang PPh21 1,2jt, Pendapatan Diterima Dimuka Uang Pangkal 18jt — Modal Yayasan otomatis 80,3jt, Trial Balance balanced

## Referensi Silang

- [`../accounting-fnb-kafe/00-profil-perusahaan-dan-master-data.id.md`](../accounting-fnb-kafe/00-profil-perusahaan-dan-master-data.id.md) — dasar pola §8 Saldo Awal & dimensi Business Unit multi-lokasi
- [`../accounting-manufaktur-2/00-profil-perusahaan-dan-master-data.id.md`](../accounting-manufaktur-2/00-profil-perusahaan-dan-master-data.id.md) — dasar pola Fiscal Year/Accounting Period
- §8: implementasi `App\Services\JournalPostingService::syncOpeningBalance()`, dipanggil dari `ClientMaster\ChartOfAccountBalances` dan `Finance\BankAccounts`
- Endpoint Fixed Assets terkonfirmasi via `routes/fixed_assets.php`: prefix `fixed-assets/assets/*` dan `fixed-assets/disposals/*`; field akuisisi **`salvage_value`** (BUKAN `residual_value`) dan `category` WAJIB salah satu dari enum `land,building,vehicle,equipment,furniture,intangible` — dikonfirmasi dari `App\Http\Controllers\Finance\FixedAssets::create()` validator, dipakai konsisten mulai file `01`/`05` di suite ini
