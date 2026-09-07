---
title: — 00. Profil Perusahaan & Master Data (Multi-Tahun)
category: Accounting 2
description: Skenario perusahaan berjalan penuh (PT Retail Nusantara Jaya, sama seperti suite `accounting/`) dari awal berdiri Januari 2025 sampai bulan berjalan Agustus 2026 — 20 bulan berturut-turut dengan transaksi nyata tiap bulan, dipakai untuk menguji sistem dalam kondisi "perusahaan sungguhan sudah lama jalan", bukan cuma snapshot 1 tahun.
visibility: internal
---

# 00. Profil Perusahaan & Master Data (Multi-Tahun)

> **Suite ini adalah PERUSAHAAN YANG SAMA dengan [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md)** (PT Retail Nusantara Jaya, 2 toko, PKP) — sengaja DIDUPLIKASI ke folder terpisah (`accounting-retail-tahun-berjalan/`), BUKAN menimpa suite asli, supaya kamu bisa jalankan dua-duanya independen di branch/env yang beda tanpa bentrok data. Istilah dasar (Debit/Kredit, `normal_balance`, Balanced, COA, Fiscal Year vs Accounting Period, GL, Trial Balance, Opening Balance, PPN) SUDAH dijelaskan lengkap di bagian "Konsep Dasar" file itu — baca dulu di sana kalau belum familiar, tidak diulang di sini.
>
> **Bedanya dengan suite `accounting/` yang cuma 1 tahun buku (FY2026 saja):** suite ini membentang **20 bulan berturut-turut, Januari 2025 sampai Agustus 2026 (bulan berjalan/current)** — 2 tahun fiskal (FY2025 penuh + FY2026 berjalan sampai bulan ke-8). Tujuannya menguji sistem sebagai **perusahaan yang SUDAH LAMA beroperasi**, bukan cuma perusahaan baru mulai tahun ini: banyak Accounting Period yang sudah lewat & bisa di-close, siklus utang-piutang yang berulang lintas bulan, penyusutan aset yang berjalan belasan periode, cicilan pinjaman bank yang terus berkurang, dan laporan keuangan yang harus tetap benar walau dibandingkan lintas 2 tahun fiskal berbeda.
>
> **Tiap bulan (Feb 2025 - Ags 2026) MINIMAL punya 2 transaksi fundamental (pendapatan bulanan + beban operasional bulanan) DITAMBAH minimal 3 transaksi lain** (siklus pembelian-pembayaran utang, penyusutan, cicilan pinjaman, dan sesekali transaksi khusus seperti piutang, retur, prive, setor PPh 21, dst) — detail lengkap & angka per bulan ada di file [`01-jurnal-transaksi-2025.id.md`](./01-jurnal-transaksi-2025.id.md) dan [`02-jurnal-transaksi-2026.id.md`](./02-jurnal-transaksi-2026.id.md). Seluruh 176 jurnal di 20 bulan itu **sudah disimulasikan dulu di luar sistem (Python) sebelum ditulis di sini** supaya totalnya pasti Debit = Kredit di setiap titik waktu — angka-angka acuan itu yang dipakai sebagai "jawaban benar" untuk membandingkan hasil testing kamu di file 03 (Trial Balance) dan 05 (Laporan Keuangan).
>
> **Kerjakan file ini PALING PERTAMA** — semua file lain (01-05) mengasumsikan master data di sini sudah ada.

## Profil Perusahaan (Skenario)

**PT Retail Nusantara Jaya** — retail consumer goods (minimarket modern), PKP, 2 toko (**Toko Pusat** Jakarta, **Toko Cabang** Bandung). Mata uang IDR. Tahun buku kalender (Jan-Des).

**Narasi baru untuk suite ini**: perusahaan ini **baru mulai beroperasi 2 Januari 2025** (bukan sudah berjalan sebelum sistem dipakai) — jadi suite ini **TIDAK memakai fitur Saldo Awal / Opening Balance** (`chart-of-accounts-balances`/`bank-accounts`) sama sekali. Alasannya murni teknis: fitur itu **selalu mem-posting jurnal bertanggal hari ini** (tanggal server saat tombol ditekan), bukan tanggal yang dipilih user (lihat catatan di `../accounting/00-...md` §9) — kalau dipakai di sini, "saldo awal 2025" itu akan nyasar ke Accounting Period bulan kamu benar-benar menekan tombolnya (misal Agustus 2026), merusak seluruh narasi kronologis 20 bulan. Solusinya: modal awal dicatat **manual lewat Journal biasa bertanggal 2025-01-02** (persis pola `../accounting/01-jurnal-manual.id.md` §1.1, cuma sekarang jadi TITIK AWAL cerita, bukan contoh isolasi) — jurnal manual BISA bertanggal bebas asal Accounting Period tanggal itu masih terbuka, beda dari fitur Opening Balance yang dipaksa "hari ini".

## 1-8. Master Data yang Direuse 100% dari Suite `accounting/`

Buat/pastikan sudah ada persis seperti didokumentasikan di `../accounting/00-profil-perusahaan-dan-master-data.id.md`, section yang sama:

| #   | Master Data                                        | Rujukan | Catatan untuk suite ini                                                        |
| --- | -------------------------------------------------- | ------- | ------------------------------------------------------------------------------ |
| 1   | Currency IDR                                       | §1      | Sama persis                                                                    |
| 2   | Chart of Account Type (6 tipe: AL/AT/LJP/EK/PD/BB) | §2      | Sama persis                                                                    |
| 4   | Business Unit (Toko Pusat, Toko Cabang)            | §6      | Sama persis — dipakai dimensi `business_unit_id` di baris Penjualan tiap bulan |
| 5   | Tax PPN 11%                                        | §7      | Sama persis                                                                    |
| 6   | Contact (1 Customer, 1 Supplier)                   | §8      | Sama persis — dipakai transaksi kredit di §1.11 file transaksi (Jan/Feb 2026)  |

**Chart of Accounts** juga direuse **24 akun** dari `../accounting/00-...md` §3 dan §10 (18 akun dasar + 6 akun tambahan retail) — **kode dan flag SAMA PERSIS**, cek tabel lengkap di sana. Ringkasan cepat akun yang paling sering dipakai di suite ini:

| Kode | Nama                                | Tipe                     | Flag                                                                                                                                        |
| ---- | ----------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1101 | Kas Kecil                           | Aset Lancar              | `is_cash_account`                                                                                                                           |
| 1102 | Bank BCA                            | Aset Lancar              | `is_cash_account`                                                                                                                           |
| 1103 | Piutang Dagang                      | Aset Lancar              | `is_ar_control_account`                                                                                                                     |
| 1104 | Persediaan Barang Dagang            | Aset Lancar              | —                                                                                                                                           |
| 1105 | PPN Masukan                         | Aset Lancar              | `is_tax`, Tax: PPN 11%                                                                                                                      |
| 1201 | Peralatan Toko                      | Aset Tetap               | —                                                                                                                                           |
| 1202 | Akumulasi Penyusutan Peralatan Toko | Aset Tetap               | Kontra-aset                                                                                                                                 |
| 2101 | Utang Dagang                        | Liabilitas Jangka Pendek | `is_ap_control_account`                                                                                                                     |
| 2102 | PPN Keluaran                        | Liabilitas Jangka Pendek | `is_tax`, Tax: PPN 11%                                                                                                                      |
| 2103 | Utang PPh 21 Karyawan               | Liabilitas Jangka Pendek | —                                                                                                                                           |
| 3101 | Modal Pemilik                       | Ekuitas                  | `is_opening_balance_equity_account` (tetap diaktifkan untuk jaga-jaga, TIDAK dipakai fitur Saldo Awal di suite ini — lihat catatan di atas) |
| 3102 | Laba Ditahan                        | Ekuitas                  | `is_retained_earnings_account` — **dipakai sungguhan di file 04** (Close Fiscal Year FY2025)                                                |
| 4101 | Penjualan Barang Dagang             | Pendapatan               | —                                                                                                                                           |
| 5101 | Harga Pokok Penjualan               | Beban                    | **Dipakai aktif tiap bulan di suite ini** (tidak seperti `accounting/` yang HPP-nya kosong — lihat §10 di bawah)                            |
| 5201 | Beban Sewa Toko                     | Beban                    | —                                                                                                                                           |
| 5202 | Beban Gaji Karyawan                 | Beban                    | —                                                                                                                                           |
| 5203 | Beban Listrik & Air                 | Beban                    | —                                                                                                                                           |
| 5204 | Beban Penyusutan Peralatan Toko     | Beban                    | —                                                                                                                                           |
| 5205 | Beban Selisih Kas                   | Beban                    | —                                                                                                                                           |

## 9. Modal Awal — Jurnal Manual (BUKAN Fitur Opening Balance)

**Halaman:** `accounting/journals` (sama seperti transaksi biasa, BUKAN `client-master/chart-of-accounts-balances`).

**Sebab-akibat:** lihat catatan narasi di atas — fitur Opening Balance dikunci ke tanggal hari ini, jadi tidak cocok untuk mensimulasikan "perusahaan berdiri 2 Januari 2025". Modal awal & pengisian kas kecil di sini murni jurnal manual biasa, persis pola `../accounting/01-jurnal-manual.id.md` §1.1, cuma nilainya beda dan tanggalnya jadi awal cerita (bukan pertengahan tahun).

| Skenario                     | Langkah di UI                                                                                                                                                                                                                                                                              | Hasil                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Positif — setoran modal      | Buka **Journals** → **+ Create Journal** → Code auto, Date `2025-01-02`, Description "Setoran modal awal pemilik — pendirian usaha" → baris 1: Account `<Bank BCA>` Debit `300.000.000`; baris 2: Account `<Modal Pemilik>` Credit `300.000.000` → pastikan Balanced → **Save** → **Post** | Jurnal `JRN-2025-...` Posted, saldo Bank BCA jadi 300.000.000 |
| Positif — isi kas kecil awal | Create Journal baru, Date `2025-01-02`, Description "Isi kas kecil awal dari Bank BCA" → baris 1: Account `<Kas Kecil>` Debit `10.000.000`; baris 2: Account `<Bank BCA>` Credit `10.000.000` → Save → Post                                                                                | Saldo Kas Kecil jadi 10.000.000, Bank BCA jadi 290.000.000    |
| Netralisasi                  | Reverse kedua jurnal ini (dari halaman detail) HANYA kalau mau reset total suite — kalau tidak, JANGAN dihapus/reverse, keduanya jadi fondasi seluruh 20 bulan berikutnya                                                                                                                  |

## 10. Perbedaan Desain Penting vs Suite `accounting/` (baca sebelum lanjut ke file 01/02)

**Kenapa bagian ini perlu:** supaya kamu tidak bingung kenapa suite ini "terasa beda" dari `accounting/` walau perusahaannya sama.

| Aspek                                             | Suite `accounting/` (1 tahun)                                                             | Suite ini (`accounting-retail-tahun-berjalan/`, 20 bulan)                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Saldo awal                                        | Pakai fitur Opening Balance (§9 file asli)                                                | Pakai jurnal manual biasa (lihat §9 di atas) — fitur Opening Balance TIDAK disentuh sama sekali di suite ini                                                                                                                                                                                                                                                  |
| Harga Pokok Penjualan (5101)                      | Tidak pernah dipakai (kosong)                                                             | **Dipakai tiap bulan** — tiap kali ada rekap penjualan bulanan, ada juga 1 jurnal terpisah "Pengakuan HPP" (Debit HPP, Credit Persediaan) supaya Laba Rugi mencerminkan margin kotor sungguhan, dan saldo Persediaan tidak menggelembung tanpa batas selama 20 bulan                                                                                          |
| Pinjaman bank                                     | Tidak ada                                                                                 | **Baru** — akun 2105 Pinjaman Bank Jangka Pendek, dicairkan Januari 2025, dicicil tiap bulan (pokok+bunga) sampai Agustus 2026                                                                                                                                                                                                                                |
| Beban Iklan & Promosi, Beban Administrasi Bank    | Tidak ada                                                                                 | **Baru** — akun 5208 & 5209, muncul beberapa kali sebagai variasi transaksi                                                                                                                                                                                                                                                                                   |
| Nilai transaksi fundamental (penjualan/sewa/gaji) | Snapshot 1 hari/bulan yang berdiri sendiri (angka besar, tidak didesain utk berulang 20x) | **Didesain ulang supaya sustainable kalau berulang 20 bulan** — kalau angka asli `accounting/` (gaji 80jt + sewa 20jt/bulan vs omzet cuma 80jt/bulan) dipakai apa adanya tiap bulan, Bank BCA akan minus dalam hitungan bulan (rugi terus-menerus, tidak masuk akal buat skenario "perusahaan berjalan"). Nilai final ada di file 01 §Ringkasan Angka Bulanan |
| Fiscal Year                                       | FY2026 saja, 12 periode                                                                   | **FY2025 (12 periode) + FY2026 (12 periode digenerate, tapi transaksi cuma sampai Agustus)**                                                                                                                                                                                                                                                                  |

## 11. 4 Akun Chart of Accounts BARU (khusus suite ini)

**Sebab-akibat:** dipakai untuk siklus pinjaman bank & 2 variasi beban baru yang tidak ada skenarionya di `accounting/` — kalau akun ini belum dibuat, transaksi terkait di file 01/02 tidak akan punya akun tujuan yang tepat.

| Kode | Nama Akun                   | Tipe                     | Flag khusus | Dipakai di                                            |
| ---- | --------------------------- | ------------------------ | ----------- | ----------------------------------------------------- |
| 2105 | Pinjaman Bank Jangka Pendek | Liabilitas Jangka Pendek | —           | Pencairan Jan 2025, cicilan bulanan Feb 2025-Ags 2026 |
| 5208 | Beban Iklan & Promosi       | Beban                    | —           | Kampanye akhir tahun 2025, iklan Jul 2026             |
| 5209 | Beban Administrasi Bank     | Beban                    | —           | Biaya admin bank Mei 2026                             |
| 5210 | Beban Bunga Pinjaman        | Beban                    | —           | Komponen bunga tiap cicilan pinjaman bulanan          |

| Skenario    | Langkah di UI                                                                                                                                | Hasil                                             |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Positif     | Buka **Chart of Accounts** → create ke-4 akun di atas satu-satu (Type sesuai kolom Tipe, tidak ada flag toggle khusus yang perlu diaktifkan) | Muncul di list, siap dipakai di jurnal file 01/02 |
| Netralisasi | Klik ikon delete akun test — cek dulu tidak ada Journal/General Ledger yang mereferensikannya                                                |

## 12. Fiscal Year & Accounting Period — FY2025 + FY2026

**Halaman:** `client-master/fiscal-year` + `client-master/accounting-period` (sama seperti `../accounting/00-...md` §4-§5, cuma sekarang dibuat 2 tahun fiskal berurutan).

**Sebab-akibat:** FY2026 WAJIB digenerate juga (bukan cuma FY2025) walau transaksi baru masuk sampai Agustus — Accounting Period Sep-Des 2026 tetap ada, cuma belum ada transaksi apapun di dalamnya (ini realistis, kebanyakan sistem akuntansi men-generate periode setahun di muka sebelum dipakai).

| Skenario         | Langkah di UI                                                                                                                                                                                               | Hasil                                                                                                                          |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Positif — FY2025 | Buka **Fiscal Year** → **+ Add** → Code: "FY2025", Name: "Tahun Buku 2025", Start Date: 2025-01-01, End Date: 2025-12-31 → **Create** → klik **Generate** di row ini, Duration Type: "Monthly" → konfirmasi | 12 periode Jan-Des 2025 ter-generate, semua `is_closed:false, is_locked:false`                                                 |
| Positif — FY2026 | **+ Add** → Code: "FY2026", Name: "Tahun Buku 2026", Start Date: 2026-01-01, End Date: 2026-12-31 → **Create** → **Generate**, Duration Type: "Monthly"                                                     | 12 periode Jan-Des 2026 ter-generate — Sep-Des 2026 akan tetap kosong sampai suite ini "mengejar" bulan berjalan di masa depan |
| Negatif          | Generate ulang untuk fiscal year yang sama (FY2025 atau FY2026)                                                                                                                                             | Ditolak/duplikat — cek behavior aktual, sama seperti catatan di `../accounting/00-...md` §5                                    |
| Netralisasi      | Hapus periode/fiscal year test satu-satu, urutan mundur dari periode terakhir                                                                                                                               |

## Ringkasan Data Master yang Harus Sudah Ada Sebelum Lanjut

- [ ] Semua master data §1-8 (reuse dari `../accounting/00-...md`): Currency, Chart of Account Type, 24 Chart of Accounts lama, Business Unit (2 toko), Tax PPN 11%, Contact (1 customer + 1 supplier)
- [ ] 4 Chart of Accounts BARU (§11): 2105, 5208, 5209, 5210
- [ ] Fiscal Year FY2025 (12 periode) + FY2026 (12 periode) — §12
- [ ] Modal awal terposting via jurnal manual (§9): Dr Bank BCA 300.000.000 / Cr Modal Pemilik 300.000.000, lalu Dr Kas Kecil 10.000.000 / Cr Bank BCA 10.000.000 — saldo awal siap dipakai bulan berjalan pertama (Januari 2025)

## Referensi Silang

- [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) — sumber Konsep Dasar & master data yang direuse
- [`01-jurnal-transaksi-2025.id.md`](./01-jurnal-transaksi-2025.id.md) — transaksi bulanan Januari-Desember 2025 (12 bulan, 104 jurnal)
- [`02-jurnal-transaksi-2026.id.md`](./02-jurnal-transaksi-2026.id.md) — transaksi bulanan Januari-Agustus 2026 (8 bulan, 72 jurnal)
- [`03-general-ledger-trial-balance.id.md`](./03-general-ledger-trial-balance.id.md) — angka acuan Trial Balance per checkpoint kuartal
- [`04-tutup-periode-dan-tahun-fiskal.id.md`](./04-tutup-periode-dan-tahun-fiskal.id.md) — Close FY2025 dengan closing entry presisi ke Laba Ditahan
- [`05-laporan-keuangan.id.md`](./05-laporan-keuangan.id.md) — Neraca/Laba Rugi/Arus Kas FY2025 penuh vs FY2026 year-to-date Agustus
