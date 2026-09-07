---
title: (Construction / Project Based) — 00. Profil Perusahaan & Master Data
category: accounting-construction
description: Skenario PT Bangun Persada (Konstruksi) berbasis pengakuan pendapatan progresif, uang muka, dan retensi. Setup COA proyek, Business Unit (Proyek), Fiscal Year/Periode, Tax, dan Saldo Awal.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

## Profil Perusahaan (Skenario)

**PT Bangun Persada** — kontraktor konstruksi gedung dan infrastruktur (fiktif). Fokus bisnis pada pengerjaan proyek fisik dengan sistem pembayaran termin berdasarkan progres fisik (milestone/opname lapangan). Memiliki mekanisme uang muka (advance payment) dan jaminan pemeliharaan (retention receivable/payable).

Sudah menjadi **PKP** (PPN 11%). Memiliki 2 proyek aktif (Business Unit):

- **Proyek Gedung Kantor A** — proyek swasta komersial.
- **Proyek Jembatan B** — proyek infrastruktur publik.

Periode akuntansi **BULANAN**, tahun buku FY2026.

## Istilah Khusus Proyek Konstruksi

Suite ini pakai istilah akuntansi umum yang sama dengan `../accounting/00-profil-perusahaan-dan-master-data.id.md` (debit/kredit, COA, GL, Trial Balance, dst — baca di sana dulu kalau belum familiar). Yang berbeda di sini murni istilah KHAS INDUSTRI KONSTRUKSI, karena cara proyek konstruksi ditagih beda dari retail biasa (bukan "jual putus", tapi bertahap sesuai progres fisik):

| Istilah                                          | Keterangan                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Uang Muka (Advance Payment)**                  | Pemilik proyek bayar sebagian dana DI DEPAN, sebelum pekerjaan fisik dimulai/selesai. Ini BUKAN pendapatan saat diterima — dicatat sebagai utang (LIA-02) dulu, karena kontraktor masih "berutang pekerjaan" senilai itu ke pemilik proyek.                                                                          |
| **Amortisasi Uang Muka**                         | Proses "mencairkan" uang muka sedikit-sedikit setiap kali ada tagihan progres baru — porsinya proporsional terhadap persentase uang muka dari total kontrak (lihat perhitungan di file 01 Jurnal T2). Uang muka baru benar-benar "lunas terpakai" setelah proyek selesai 100%.                                                                            |
| **Pengakuan Pendapatan Progresif / Percentage of Completion** | Beda dari retail (pendapatan diakui begitu barang terjual), proyek konstruksi mengakui pendapatan BERTAHAP sesuai persentase pekerjaan yang sudah selesai secara fisik (mis. "proyek sudah 30% jadi" → akui 30% dari nilai kontrak sebagai pendapatan), BUKAN menunggu proyek 100% selesai baru sekaligus diakui.                                          |
| **Opname Lapangan / Termin**                     | Verifikasi fisik di lokasi proyek untuk menentukan berapa persen pekerjaan yang benar-benar sudah selesai — angka inilah yang jadi dasar tagihan (termin) ke pemilik proyek. Sistem ini TIDAK punya fitur pencatatan opname lapangan otomatis, persentase progresnya dihitung manual lalu diinput sebagai jurnal.                                          |
| **Piutang Progres Proyek**                       | Sama seperti Piutang Dagang biasa (uang yang belum dibayar customer), tapi khusus untuk tagihan termin proyek — nilainya SUDAH dikurangi porsi retensi dan amortisasi uang muka (lihat contoh perhitungan di file 01).                                                                                                |
| **Retensi (Retention Receivable/Payable)**       | Persentase kecil (di sini 5%) dari tiap tagihan yang SENGAJA DITAHAN sebagai jaminan kualitas pekerjaan — baru dicairkan setelah masa pemeliharaan (jangka waktu setelah proyek selesai untuk membuktikan tidak ada cacat konstruksi) berakhir. Dari sisi kontraktor ke pemilik proyek, ini **Piutang Retensi** (uang kontraktor yang ditahan pemilik proyek). Dari sisi kontraktor ke subkontraktornya, ini **Utang Retensi** (uang subkontraktor yang DITAHAN kontraktor) — arahnya kebalikan tergantung posisi siapa yang menahan siapa.                        |
| **Beban Pokok Proyek**                           | Setara "Harga Pokok Penjualan" di retail (lihat gap COGS di `../accounting/04-laporan-keuangan.id.md`), tapi di sini justru SUDAH ada mekanismenya — bahan material yang dipakai untuk mengerjakan proyek dicatat sebagai beban saat dipakai (lihat file 01 Jurnal T7), bukan gap yang harus dijurnal manual seperti di suite retail.                        |
| **Gain/Loss Pelepasan Aset**                     | Selisih antara harga jual aset (`disposal_proceeds`) dengan nilai bukunya saat itu (`book_value_at_disposal`) — kalau harga jual LEBIH RENDAH dari nilai buku, itu **rugi pelepasan** (angkanya negatif), kalau lebih tinggi berarti **untung pelepasan**. Lihat contoh hitung di file 05 §3.                                                              |
| **Variance Favorable/Unfavorable**               | Istilah bahasa Inggris yang sering muncul apa adanya di response API — "favorable" = varians yang menguntungkan (beban lebih hemat dari anggaran, atau pendapatan melebihi target), "unfavorable" = kebalikannya (boros/di bawah target). Sama konsepnya dengan penjelasan "Variance" di `../accounting/05-anggaran-budget.id.md`.                          |

## 1. Chart of Accounts (**Chart of Accounts**)

| Kode   | Nama Akun                                   | Tipe                     | Flag khusus                                                                                        |
| ------ | ------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------- |
| AST-01 | Bank Mandiri Proyek                         | Aset Lancar              | `is_cash_account: true`                                                                            |
| AST-02 | Piutang Progres Proyek                      | Aset Lancar              | `is_ar_control_account: true`, `balance_required: true`                                            |
| AST-03 | Piutang Retensi (Retention Receivable)      | Aset Lancar              | `balance_required: true` — jaminan 5% yang ditahan pemilik proyek hingga masa pemeliharaan selesai |
| AST-04 | Persediaan Bahan Material Konstruksi        | Aset Lancar              | `balance_required: true`                                                                           |
| LIA-01 | Utang Subkontraktor                         | Liabilitas Jangka Pendek | `is_ap_control_account: true`, `balance_required: true`                                            |
| LIA-02 | Uang Muka Proyek Diterima (Advance Payment) | Liabilitas Jangka Pendek | `balance_required: true` — uang muka dari pemilik proyek yang diamortisasi per progres             |
| LIA-03 | Utang Retensi Subkontraktor                 | Liabilitas Jangka Pendek | `balance_required: true`                                                                           |
| LIA-04 | PPN Keluaran                                | Liabilitas Jangka Pendek | `is_tax: true`, `tax_id` → PPN 11% (§3)                                                            |
| AST-05 | Alat Berat (Excavator)                      | Aset Tetap               | dipakai sebagai `asset_account_id` di `fixed-assets/assets` (file 05)                              |
| AST-06 | Akumulasi Penyusutan Alat Berat             | Aset Tetap (kontra)      | dipakai sebagai `accum_dep_account_id` (file 05)                                                   |
| BBN-03 | Beban Penyusutan Alat Berat                 | Beban                    | dipakai sebagai `depreciation_account_id` (file 05)                                                |
| EKT-01 | Modal Pemilik                               | Ekuitas                  | `is_opening_balance_equity_account: true`                                                          |
| EKT-02 | Laba Ditahan                                | Ekuitas                  | `is_retained_earnings_account: true`                                                               |
| PDT-01 | Pendapatan Progres Proyek                   | Pendapatan               | —                                                                                                  |
| BBN-01 | Beban Pokok Proyek (Bahan & Upah)           | Beban                    | —                                                                                                  |
| BBN-02 | Beban Subkontraktor                         | Beban                    | —                                                                                                  |

> Catatan penting: sistem ini **tidak** punya field pajak khusus di baris jurnal manual — PPN diposting dengan cara flag akun COA `is_tax: true` + `tax_id` menunjuk record **Taxes** (lihat `Journal::createLines()` di `app/Http/Controllers/Accounting/Journal.php`, yang otomatis membuat baris `journal_taxes` untuk akun ber-flag `is_tax`). Karena subkontraktor konstruksi umumnya non-PKP/final, skenario ini hanya butuh **PPN Keluaran** (LIA-04) — tidak ada akun PPN Masukan.

## 2. Business Unit / Dimensi Proyek (**Business Units**)

- **Proyek Gedung Kantor A** (`code: PRJ-GDA`)
- **Proyek Jembatan B** (`code: PRJ-JMB`)

## 3. Tax PPN (**Taxes**)

| Nama    | Rate | Dipakai oleh                         |
| ------- | ---: | ------------------------------------ |
| PPN 11% |  11% | LIA-04 PPN Keluaran (field `tax_id`) |

## 4. Fiscal Year & Accounting Period (**Fiscal Year**, **Accounting Period**)

**WAJIB dibuat sebelum Saldo Awal (§6)** — `ChartOfAccountBalances::create()` menolak posting saldo awal kalau tidak ada Accounting Period yang meng-cover tanggal hari ini (`is_closed: false`, `is_locked: false`); errornya _"No active accounting period found for today's date. Please generate accounting periods first."_.

- **Fiscal Year FY2026** (`client-master/fiscal-year/create`): `code: FY2026`, `start_date: 2026-01-01`, `end_date: 2026-12-31`, `is_active: true`.
- Generate periode via `client-master/fiscal-year/generate-accounting-period` (`PUT`), `duration_type: monthly` → 12 Accounting Period (`FY2026-01` s.d. `FY2026-12`), semua `is_closed: false`, `is_locked: false`.

## 5. Contact (referensi bebas teks, bukan field relasional)

Meski suite ini "Accounting berdiri sendiri" (tanpa PO/SO), baris jurnal manual (`Journal::createLines()`) **tidak punya field `contact_id`** — dimensi proyek murni lewat `business_unit_id`, dan nama pemilik proyek/subkontraktor hanya dicatat bebas teks di kolom `descriptions` tiap jurnal (§01). Contact di `client-master/contacts` dibuat sekadar sebagai referensi cerita skenario, bukan sesuatu yang divalidasi backend:

- **PT Graha Sentosa Realty** (customer) — pemilik Proyek Gedung Kantor A.
- **Dinas PUPR Kota** (customer) — pemilik Proyek Jembatan B.
- **CV Baja Perkasa** (supplier) — subkontraktor struktur baja.

## 6. Saldo Awal Perusahaan (**Chart of Accounts Balances**, **Bank Accounts**)

Setiap baris `chart-of-accounts-balances/create` WAJIB `currency_id` (required) — pakai currency dasar branch (IDR). `opening_balance` hanya efektif pada akun dengan `balance_required: true` (§1); akun tanpa flag ini ditolak validator dengan pesan _"This COA does not require a balance record."_.

| Akun                               |  Saldo Awal | Jalur                                                                                              |
| ---------------------------------- | ----------: | -------------------------------------------------------------------------------------------------- |
| AST-01 Bank Mandiri Proyek         | 500.000.000 | `finance/bank-accounts/create`, field `opening_balance` (BUKAN lewat `chart-of-accounts-balances`) |
| AST-02 Piutang Progres Proyek      | 120.000.000 | `chart-of-accounts-balances/create`                                                                |
| AST-03 Piutang Retensi             |  30.000.000 | `chart-of-accounts-balances/create`                                                                |
| AST-04 Persediaan Bahan Material   |  80.000.000 | `chart-of-accounts-balances/create`                                                                |
| LIA-01 Utang Subkontraktor         |  50.000.000 | `chart-of-accounts-balances/create`                                                                |
| LIA-02 Uang Muka Proyek Diterima   | 100.000.000 | `chart-of-accounts-balances/create`                                                                |
| LIA-03 Utang Retensi Subkontraktor |  15.000.000 | `chart-of-accounts-balances/create`                                                                |

Total Aset = 500.000.000 + 120.000.000 + 30.000.000 + 80.000.000 = **730.000.000**
Total Liabilitas = 50.000.000 + 100.000.000 + 15.000.000 = **165.000.000**
→ **Modal Pemilik (EKT-01) otomatis bersaldo kredit 565.000.000** (diposting otomatis via `JournalPostingService::syncOpeningBalance()`, lawan akun `is_opening_balance_equity_account: true` — bukan input manual).

## 7. Skenario Pengujian Master Data

| Skenario | Detail                                                                                                         | Hasil                                                                                                                       |
| -------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Positif  | Buat 16 akun COA §1 dengan flag masing-masing (`client-master/chart-of-accounts/create-bulk`).                 | 201, semua akun tersimpan dengan flag benar.                                                                                |
| Positif  | Buat 2 Business Unit (PRJ-GDA, PRJ-JMB).                                                                       | 201, dipakai sebagai `business_unit_id` di setiap baris jurnal (file 01-06).                                                |
| Positif  | Buat Tax PPN 11%, lalu flag LIA-04 dengan `is_tax: true` + `tax_id` PPN 11%.                                   | 201, akun siap dipakai sebagai baris PPN Keluaran otomatis di jurnal manual.                                                |
| Positif  | Buat Fiscal Year FY2026, lalu `PUT generate-accounting-period` dengan `duration_type: monthly`.                | 200, 12 Accounting Period bulanan terbuat, semua `is_closed: false`.                                                        |
| Positif  | Posting saldo awal 6 akun non-kas via `chart-of-accounts-balances/create`.                                     | 201 tiap baris; masing-masing memicu jurnal saldo awal otomatis (`opening_balance_journal_header_id` terisi, lawan EKT-01). |
| Positif  | Posting saldo awal Bank Mandiri Proyek via `finance/bank-accounts/create` dengan `opening_balance: 500000000`. | 201, jurnal saldo awal Bank ikut terbentuk otomatis (lawan EKT-01).                                                         |
| Negatif  | Posting `chart-of-accounts-balances/create` ke akun `balance_required: false` (mis. PDT-01).                   | Error "This COA does not require a balance record."                                                                         |
| Negatif  | Posting saldo awal SEBELUM Accounting Period digenerate.                                                       | Error "No active accounting period found for today's date. Please generate accounting periods first."                       |
| Negatif  | Flag 2 akun sekaligus sebagai `is_opening_balance_equity_account: true` dalam 1 branch.                        | Ditolak — `ChartOfAccounts::assertAtMostOneFlaggedAccount()` membatasi maksimal 1 akun per branch per flag.                 |
| Negatif  | `chart-of-accounts-balances/create` tanpa `currency_id`.                                                       | 422, `currency_id` wajib diisi.                                                                                             |

## Netralisasi

- Hapus baris `chart-of-accounts-balances` test — otomatis mereverse jurnal saldo awal via `syncOpeningBalance(amount: 0, ...)` (lihat `ChartOfAccountBalances::delete()`).
- Hapus Bank Account test — **catatan penting**: `finance/bank-accounts/delete` TIDAK mereverse jurnal saldo awal secara otomatis (beda perilaku dari `chart-of-accounts-balances`); kalau perlu bersih total, reverse manual jurnal saldo awal Bank lewat `accounting/journals/reverse` sebelum/sesudah hapus akun bank.
- Hapus Business Unit & Fiscal Year/Accounting Period test hanya jika tidak ada jurnal yang mereferensikannya (Accounting Period tidak bisa di-close kalau masih ada jurnal unposted di rentang tanggalnya).
