---
title: — 00. Profil Perusahaan & Master Data
category: Accounting + POS
description: Skenario perusahaan baru (PT Mitra Sembako Jaya, jaringan minimarket "SembakoMart", 2 toko) yang berlangganan modul Accounting DAN POS bersamaan — TIDAK berlangganan Purchasing/Sales. Menguji integrasi Cash Session → POS Transaction → General Ledger, bukan Accounting berdiri sendiri seperti suite `accounting*/` lain.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

> **Beda dari semua suite `accounting-*/` lain**: suite-suite itu sengaja **Accounting berdiri sendiri** (TIDAK menyentuh Purchase Order/Sales Order/POS). Suite ini kebalikannya — perusahaan fiktif ini berlangganan **Accounting + POS**, TIDAK berlangganan Purchasing maupun Sales. Konsekuensinya: **tidak ada jalur pembelian resmi di sistem** untuk mengisi stok awal — stok awal & pengadaan barang dicatat manual (jurnal + stock adjustment), bukan lewat Purchase Order/Goods Receipt. Ini realistis: banyak minimarket kecil beli stok dari distributor secara tunai/COD di luar sistem ERP, lalu cuma mencatat hasilnya.
>
> **Kerjakan file ini PALING PERTAMA** — file [`01-setup-toko-warehouse-dan-cash-session.id.md`](./01-setup-toko-warehouse-dan-cash-session.id.md), [`02-transaksi-pos-harian.id.md`](./02-transaksi-pos-harian.id.md), dan [`03-integrasi-akuntansi-dan-laporan-keuangan.id.md`](./03-integrasi-akuntansi-dan-laporan-keuangan.id.md) mengasumsikan master data di sini sudah ada.

## Konsep Dasar (ditulis ulang di sini biar file ini berdiri sendiri, TIDAK perlu buka suite lain)

| Istilah                              | Penjelasan                                                                                                                                                                                                                               |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Debit / Kredit**                   | Dua sisi tiap baris jurnal. Aset & Beban naik lewat Debit, turun lewat Kredit. Liabilitas, Ekuitas, & Pendapatan naik lewat Kredit, turun lewat Debit.                                                                                   |
| **`normal_balance`**                 | Flag di Chart of Account Type yang nentuin sisi "normal"/naik akun tipe itu — `debit` untuk Aset Lancar/Aset Tetap/Beban, `credit` untuk Liabilitas/Ekuitas/Pendapatan.                                                                  |
| **Balanced**                         | Syarat wajib tiap jurnal: total Debit HARUS sama persis dengan total Kredit sebelum bisa di-Post.                                                                                                                                        |
| **Chart of Accounts (COA)**          | Daftar akun (kode + nama + tipe) yang jadi tujuan posting tiap transaksi — lihat §2 di bawah.                                                                                                                                            |
| **Fiscal Year vs Accounting Period** | Fiscal Year = 1 tahun buku (mis. FY2026, Jan-Des). Accounting Period = pecahan bulanan/mingguan/kuartalan di dalam 1 Fiscal Year — transaksi hanya bisa diposting ke Accounting Period yang statusnya masih terbuka (`is_closed:false`). |
| **General Ledger (GL)**              | Kumpulan seluruh baris jurnal yang sudah di-Post, per akun, urut tanggal — dasar dari Trial Balance & Laporan Keuangan.                                                                                                                  |
| **Trial Balance**                    | Rekap saldo akhir tiap akun di 1 periode; total kolom Debit HARUS sama dengan total kolom Kredit (`is_balanced:true`) kalau semua jurnal balanced.                                                                                       |

## Profil Perusahaan (Skenario)

**PT Mitra Sembako Jaya** — jaringan minimarket **"SembakoMart"**, PKP, 2 toko fisik yang sekaligus jadi 2 titik kasir POS:

- **SembakoMart Cempaka Putih** — Jakarta Pusat
- **SembakoMart Kelapa Dua** — Depok

Mata uang IDR. Tahun buku kalender (Jan-Des), mulai beroperasi **1 Agustus 2026**. Periode akuntansi **BULANAN**.

## 1. Chart of Account Type (6 tipe)

**Halaman:** `client-master/chart-of-account-type`. Field di form: Code, Name, Report Group, Normal Balance (dropdown), Category (dropdown), Cash Flow Section (dropdown), Description, Default Unit Type, Status — sama persis dengan suite `accounting/` (lihat [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) §2), 3 field (`Category`/`Normal Balance`/`Cash Flow Section`) wajib diisi benar karena salah isi tidak memicu error saat create — efeknya baru kelihatan di laporan keuangan yang salah kelompok/salah arah.

| Kode | Nama Tipe                | Category | Normal Balance | Cash Flow Section | Dipakai untuk                                                           | Grup Laporan (`report_group`) |
| ---- | ------------------------- | -------- | --------------- | ------------------- | ------------------------------------------------------------------------ | ------------------------------ |
| AL   | Aset Lancar               | asset    | debit            | operating            | Kas Kecil, Bank BCA, Kas Hasil Penjualan POS, Persediaan (akun 11xx)    | Balance Sheet                  |
| AT   | Aset Tetap                | asset    | debit            | investing            | Peralatan Toko & Kasir, Akumulasi Penyusutan Peralatan Toko (akun 12xx) | Balance Sheet                  |
| LJP  | Liabilitas Jangka Pendek  | liability| credit           | operating            | PPN Keluaran, Utang PPh 21 Karyawan (akun 21xx)                         | Balance Sheet                  |
| EK   | Ekuitas                   | equity   | credit           | financing            | Modal Pemilik, Laba Ditahan (akun 31xx)                                 | Balance Sheet                  |
| PD   | Pendapatan                | revenue  | credit           | operating            | Penjualan Barang Dagang (akun 41xx)                                     | Income Statement               |
| BB   | Beban                     | expense  | debit            | operating            | HPP, Beban Sewa/Gaji/Listrik/Penyusutan/Selisih Kas (akun 5xxx)         | Income Statement               |

| Skenario    | Langkah di UI                                                                                                                                                                                             | Hasil                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Positif     | **Chart of Account Type** → **+ Create** → isi Code, Name, Category, Normal Balance, Cash Flow Section, Report Group PERSIS sesuai tabel di atas (AL/AT/BB = Debit, LJP/EK/PD = Kredit) → ulangi untuk ke-6 baris | 6 tipe muncul di list dengan badge kategori benar |
| Negatif     | Create tipe dengan Code duplikat (mis. "AL" dua kali)                                                                                                                                                     | Ditolak validasi unique |
| Netralisasi | Hapus tipe test SETELAH semua akun & jurnal turunannya dihapus (FK constraint)                                                                                                                            |                         |

## 2. Chart of Accounts (16 akun)

**Sengaja lebih ramping dari suite `accounting*/`** — tidak ada akun Piutang Dagang/Utang Dagang/PPN Masukan karena tidak ada modul Purchasing/Sales (semua transaksi POS lunas tunai/kartu/QRIS saat itu juga, tidak ada termin).

**Kode akun sengaja TIDAK disamakan 1:1 dengan suite `accounting/`** (mis. di sana `1103` = Piutang Dagang, di sini `1103` = Kas Hasil Penjualan POS) — branch suite ini sudah lebih dulu punya akun kas/bank spesifik POS di kode-kode 11xx tersebut, jadi menyamakan kode persis dengan suite lain akan bentrok/menimpa akun yang sudah dipakai (Bank BCA, Kas Hasil Penjualan POS). Yang disamakan dari suite `accounting/` adalah **level detail & format tabel** (lihat §1 di atas), bukan kode akunnya.

| Kode | Nama Akun                           | Tipe                     | Flag                                | Catatan                                                                                |
| ---- | ----------------------------------- | ------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------- |
| 1101 | Kas Kecil                           | Aset Lancar              | `is_cash_account`                   | Operasional kantor pusat                                                               |
| 1102 | Bank BCA                            | Aset Lancar              | `is_cash_account`                   | Rekening utama perusahaan                                                              |
| 1103 | Kas Hasil Penjualan POS             | Aset Lancar              | `is_cash_account`                   | **Fungsi GL `pos_cash`** — semua transaksi POS (tunai/kartu/QRIS) masuk sini, lihat §5 |
| 1104 | Persediaan Barang Dagang            | Aset Lancar              | —                                   | Diisi manual via jurnal + Stock Adjustment (§1 file 01), BUKAN dari Goods Receipt      |
| 1201 | Peralatan Toko & Kasir              | Aset Tetap               | —                                   | Mesin kasir, printer struk, rak                                                        |
| 1202 | Akumulasi Penyusutan Peralatan Toko | Aset Tetap               | Kontra-aset                         |                                                                                        |
| 2102 | PPN Keluaran                        | Liabilitas Jangka Pendek | `is_tax`, Tax: PPN 11%              | **Fungsi GL `ppn_keluaran`**                                                           |
| 2103 | Utang PPh 21 Karyawan               | Liabilitas Jangka Pendek | —                                   |                                                                                        |
| 3101 | Modal Pemilik                       | Ekuitas                  | `is_opening_balance_equity_account` |                                                                                        |
| 3102 | Laba Ditahan                        | Ekuitas                  | `is_retained_earnings_account`      |                                                                                        |
| 4101 | Penjualan Barang Dagang             | Pendapatan               | —                                   | **Fungsi GL `sales_revenue`**                                                          |
| 5101 | Harga Pokok Penjualan               | Beban                    | —                                   | **TIDAK pernah diposting otomatis oleh POS** — lihat catatan wajib di §5 dan file 03   |
| 5201 | Beban Sewa Toko                     | Beban                    | —                                   |                                                                                        |
| 5202 | Beban Gaji Karyawan & Kasir         | Beban                    | —                                   |                                                                                        |
| 5203 | Beban Listrik & Air                 | Beban                    | —                                   |                                                                                        |
| 5204 | Beban Penyusutan Peralatan Toko     | Beban                    | —                                   |                                                                                        |
| 5205 | Beban Selisih Kas                   | Beban                    | —                                   | Dipakai saat tutup Cash Session ada selisih kas fisik vs sistem — lihat file 01 §3     |

| Skenario    | Langkah di UI                                                          | Hasil                        |
| ----------- | ---------------------------------------------------------------------- | ---------------------------- |
| Positif     | **Chart of Accounts** → create 16 akun di atas satu-satu               | Muncul di list, siap dipakai |
| Negatif     | Create akun dengan kode duplikat (mis. `1103` dua kali)                | Ditolak validasi unique      |
| Netralisasi | Hapus akun test — cek dulu tidak ada Journal/GL yang mereferensikannya |                              |

## 3. Fiscal Year & Accounting Period — FY2026

**Halaman:** `client-master/fiscal-year` + `client-master/accounting-period`.

| Skenario    | Langkah di UI                                                                                                                                                  | Hasil                                                         |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Positif     | **Fiscal Year** → **+ Add** → Code "FY2026", Name "Tahun Buku 2026", Start `2026-01-01`, End `2026-12-31` → **Create** → **Generate**, Duration Type "Monthly" | 12 periode Jan-Des 2026 ter-generate, semua `is_closed:false` |
| Netralisasi | Hapus periode/fiscal year test mundur dari periode terakhir                                                                                                    |                                                               |

## 4. Business Unit (dimensi per toko)

Dipakai sebagai dimensi `business_unit_id` di baris jurnal penjualan POS supaya laporan bisa dipecah per toko.

| Kode  | Nama               | Tipe               |
| ----- | ------------------ | ------------------ |
| BU-CP | Toko Cempaka Putih | Cost/Profit Center |
| BU-KD | Toko Kelapa Dua    | Cost/Profit Center |

| Skenario    | Langkah di UI                                                        | Hasil          |
| ----------- | -------------------------------------------------------------------- | -------------- |
| Positif     | **Business Unit** → create BU-CP dan BU-KD                           | Muncul di list |
| Netralisasi | Hapus BU test setelah tidak direferensikan Warehouse/Journal manapun |                |

## 5. Setup Fungsi GL POS — `pos/pos-configs`

**POS punya tabel config sendiri, independen dari Sales** (`pos_configs`/`pos_config_journals`, terpisah dari `sales_configs`/`sales_config_journals` milik modul Sales) — POS tidak lagi "menumpang" config Sales, dan tetap bisa posting jurnal walau modul Sales/SO sama sekali tidak berlangganan (relevan untuk suite ini, karena perusahaan skenario TIDAK berlangganan Sales). Kalau langkah di bawah dilewati, `pos-transactions/create` akan gagal posting jurnal (`pos_config_is_not_set_up_for_this_branch` atau functionality account belum di-map) meskipun transaksi POS-nya sendiri tetap tercatat sebagai `completed`.

| Functionality Key | Akun Tujuan                    | Dipakai Untuk                                                                                                 |
| ----------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `pos_cash`        | 1103 — Kas Hasil Penjualan POS | Debit sisi kas tiap transaksi POS (total, TERLEPAS dari `payment_method` — lihat catatan verifikasi di bawah) |
| `sales_revenue`   | 4101 — Penjualan Barang Dagang | Credit (subtotal − discount_amount)                                                                           |
| `ppn_keluaran`    | 2102 — PPN Keluaran            | Credit tax_amount                                                                                             |

| Skenario                                   | Langkah di UI/Postman                                                                                                     | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                    | Buka **POS Configs** (`pos/pos-configs`) → map ketiga functionality di atas ke akun masing-masing → **Save**             | Config tersimpan, siap dipakai POS — cek juga branch ini otomatis sudah punya row `pos_configs` kosong (auto-provisioned saat branch dibuat), jadi langkah ini murni isi COA-nya, bukan bikin config dari nol                                                                                                                                                                                                                                                                                        |
| Negatif                                    | Buat transaksi POS SEBELUM functionality `pos_cash`/`sales_revenue`/`ppn_keluaran` di-map                                 | Verifikasi behavior aktual: transaksi tetap `completed` tapi TIDAK ada Journal/GL yang terbentuk (silent gap, `gl_posting_error` di response berisi pesan `no_active_chart_of_account_mapping_found_for_functionality_x`) — dokumentasikan mana yang benar, karena ini menentukan apakah admin WAJIB setup config dulu sebelum toko buka                                                                                                                                                              |
| **Perlu diverifikasi manual saat testing** | Buat 1 transaksi POS bayar kartu debit dan 1 lagi bayar QRIS (bukan tunai) → cek Journal yang terbentuk                   | Pastikan APAKAH keduanya tetap posting ke akun `pos_cash` (1103) yang sama seperti transaksi tunai, atau ada pemisahan akun per metode pembayaran (mis. akun kliring EDC/Midtrans terpisah). Kalau ternyata SEMUA metode pembayaran (tunai, kartu, QRIS) diperlakukan sama dan masuk ke satu akun `pos_cash`, catat ini sebagai **temuan** — di dunia nyata dana kartu/QRIS TIDAK langsung jadi kas fisik, seharusnya masuk akun "Piutang EDC"/"Deposit Payment Gateway" dulu sebelum dicairkan ke bank |

**Catatan teknis** (buat yang perlu trace kode): jurnal POS di-posting lewat `JournalPostingService::postForPosDocument()`, tipe jurnal tersendiri `"{branch}-pos-journal"` dengan kode prefix dinamis (setup key `pos_journal_prefix`, default `POS`) — terpisah total dari `postForSalesDocument()`/tipe "Sales Journal" yang dipakai modul Sales. Kalau branch ini sebelumnya sempat pakai versi lama (POS reuse `sales_configs`), histori jurnal lama tetap tercatat di bawah tipe "Sales Journal"/prefix `SJ-` — cuma transaksi POS baru setelah migrasi ini yang pakai jalur `pos_configs`/tipe "POS Journal".

## 6. Payment Methods

| Skenario    | Langkah di UI                                                         | Hasil                                                             |
| ----------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Positif     | **Payment Methods** → create 3: "Tunai", "Kartu Debit/Kredit", "QRIS" | Muncul di list, siap dipilih di `payment_method_id` transaksi POS |
| Netralisasi | Hapus payment method test setelah tidak dipakai transaksi manapun     |                                                                   |

## 7. Modal Awal, Peralatan Toko & Stok Awal — Jurnal Manual

**Sebab-akibat:** karena tidak berlangganan Purchasing, tidak ada Purchase Order/Goods Receipt untuk mencatat pengadaan barang dagang & peralatan. Semua dicatat manual via **Journals** biasa (`accounting/journals`), tanggal `2026-08-01` (hari pertama beroperasi), Accounting Period Agustus 2026 harus dalam keadaan terbuka.

| Skenario                          | Langkah di UI                                                                                                                                                                                                     | Hasil                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Positif — setoran modal           | Create Journal, Date `2026-08-01`, Description "Setoran modal awal pemilik" → baris 1: `<Bank BCA>` Debit `150.000.000`; baris 2: `<Modal Pemilik>` Credit `150.000.000` → Save → Post                            | Saldo Bank BCA 150.000.000                      |
| Positif — isi kas kecil           | Create Journal, Date `2026-08-01` → `<Kas Kecil>` Debit `5.000.000` / `<Bank BCA>` Credit `5.000.000` → Post                                                                                                      | Kas Kecil 5.000.000, Bank BCA 145.000.000       |
| Positif — beli peralatan kasir    | Create Journal, Date `2026-08-01` → `<Peralatan Toko & Kasir>` Debit `20.000.000` / `<Bank BCA>` Credit `20.000.000` → Post                                                                                       | Bank BCA 125.000.000, Peralatan Toko 20.000.000 |
| Positif — stok awal barang dagang | Create Journal, Date `2026-08-01`, Description "Pengadaan stok awal sembako dari distributor (tunai, di luar sistem)" → `<Persediaan Barang Dagang>` Debit `40.000.000` / `<Bank BCA>` Credit `40.000.000` → Post | Bank BCA 85.000.000, Persediaan 40.000.000      |
| Netralisasi                       | JANGAN reverse — jurnal ini fondasi seluruh suite (dipakai file 01-03)                                                                                                                                            |                                                 |

**Total setelah §7**: Bank BCA 85.000.000, Kas Kecil 5.000.000, Peralatan Toko 20.000.000, Persediaan 40.000.000 — total Debit = Kredit = 150.000.000, Modal Pemilik 150.000.000.

## Ringkasan Data Master Sebelum Lanjut ke File 01

- [ ] 6 Chart of Account Type (§1)
- [ ] 16 Chart of Accounts (§2)
- [ ] Fiscal Year FY2026, 12 periode bulanan (§3)
- [ ] Business Unit BU-CP & BU-KD (§4)
- [ ] POS Config functionality `pos_cash`/`sales_revenue`/`ppn_keluaran` ter-map (§5)
- [ ] 3 Payment Methods: Tunai, Kartu Debit/Kredit, QRIS (§6)
- [ ] 4 jurnal manual modal awal/peralatan/stok posted (§7) — saldo akhir Bank BCA 85.000.000, Kas Kecil 5.000.000, Peralatan Toko 20.000.000, Persediaan 40.000.000
