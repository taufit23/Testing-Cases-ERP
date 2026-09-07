---
title: (F&B Kafe) — 02. General Ledger, Trial Balance & Verifikasi per Outlet
category: accounting-fnb-kafe
description: Titik verifikasi akhir seluruh transaksi file 01 lewat Trial Balance presisi dan General Ledger dengan filter dimensi Business Unit per outlet — memastikan ribuan rupiah kecil di 5 hari penjualan terakumulasi tepat.
visibility: internal
---

# 02. General Ledger, Trial Balance & Verifikasi per Outlet

> Prasyarat: [`01-jurnal-harian-penjualan-dan-akumulasi.id.md`](./01-jurnal-harian-penjualan-dan-akumulasi.id.md) lengkap dan semua jurnal sudah `JRN_POSTED` (§1.16 post-bulk). File ini adalah **titik verifikasi akhir** — kalau satu angka pun tidak cocok, artinya ada jurnal di file `01` yang terlewat/salah tanggal/salah akun, BUKAN masalah di file ini.

## 2.1 Trial Balance Keseluruhan (**General Ledger — `trial-balance`**)

| Skenario                                                           | Detail                                                                                                                      | Hasil                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                            | `POST accounting/general-ledger/trial-balance {date_to:"2026-02-06"}`                                                       | `total_debit = total_credit`, lihat tabel lengkap di §2.2                                                                                                                                                                                 |
| **Positif — 2 endpoint Trial Balance (regresi dari 2 suite lain)** | Bandingkan dengan `POST reports/trial-balance` (`ReportController::trialBalance`, implementasi terpisah) untuk periode sama | Hasil kedua endpoint HARUS identik — kalau beda, itu bug regresi yang sudah dicatat di suite lain (`../accounting/02-general-ledger-neraca-saldo.id.md` §2.4, `../accounting-manufaktur/05-...` §5.1), laporkan ulang kalau masih terjadi |

## 2.2 Saldo Akhir Tiap Akun (as-of 2026-02-06)

Sama persis dengan tabel Ringkasan di [`01`](./01-jurnal-harian-penjualan-dan-akumulasi.id.md) — dites ulang di sini via endpoint sungguhan sebagai regression check, BUKAN dihitung ulang manual (kalau angka file `01` sudah benar, tabel ini otomatis cocok).

| Akun                                          |                                     Saldo Diharapkan |
| --------------------------------------------- | ---------------------------------------------------: |
| AST-01 Kas Kasir Kemang                       |                                              667.650 |
| AST-02 Kas Kasir Senayan                      |                                              440.050 |
| AST-03 Kas Kasir BSD                          |                                              305.850 |
| AST-04 Bank BCA Operasional                   |                                           27.600.000 |
| AST-05 Piutang Dagang                         |                                           13.550.000 |
| AST-06 Persediaan Bahan Baku                  |                                           25.093.250 |
| AST-07 PPN Masukan                            |                                            2.200.000 |
| AST-08 Peralatan Dapur                        |                                           48.000.000 |
| AST-09 Akumulasi Penyusutan Peralatan Dapur   |            0 (belum ada penyusutan sampai file `05`) |
| AST-10 Renovasi Interior                      |                                           36.000.000 |
| AST-11 Akumulasi Penyusutan Renovasi Interior |                                                    0 |
| LIA-01 Utang Dagang                           |                                           28.200.000 |
| LIA-02 PPN Keluaran                           |                                            3.663.550 |
| LIA-03 Utang PPh 21 Karyawan                  |                                            1.400.000 |
| LIA-04 Pendapatan Diterima Dimuka             |                                            6.000.000 |
| EKT-01 Modal Pemilik                          |                                          107.700.000 |
| EKT-02 Laba Ditahan                           |                                                    0 |
| PDT-01 Pendapatan Minuman                     |                                           23.270.000 |
| PDT-02 Pendapatan Makanan                     |                                            7.035.000 |
| BBN-01 HPP                                    |                                            9.906.750 |
| BBN-02 Beban Gaji Karyawan                    |                                           12.000.000 |
| BBN-03 Beban Listrik & Gas                    |                                            1.500.000 |
| BBN-04 Beban Selisih Kas Kasir                |                                                5.000 |
| BBN-07 Beban Sewa Outlet                      | 0 (tidak dipakai di baseline, lihat catatan `00` §3) |

## 2.3 General Ledger — Detail Ledger per Akun (**General Ledger — `detail-ledger`**)

| Skenario                                                             | Detail                                                                                                | Hasil                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                              | `POST .../detail-ledger {chart_of_account_id:<PDT-01>, date_from:"2026-02-01", date_to:"2026-02-06"}` | **8 baris** muncul: 1 baris per outlet per hari kerja untuk PDT-01 dari §1.1-1.5 (3 outlet × 5 hari = 15 baris, TAPI cek jumlah aktual — kalau ada baris yang hilang, berarti split-per-BU di §1.1 tidak tersimpan benar) + 1 baris redemption voucher §1.11 = **16 baris total**, jumlah kredit = 23.270.000 |
| **Positif — akun dengan baris sangat banyak (stress-test tampilan)** | Sama query untuk `AST-04` Bank BCA (dipakai di hampir semua jurnal §1.8-1.15)                         | Semua baris muncul urut tanggal, running balance per baris benar (kumulatif, bukan cuma saldo akhir) — cek TIDAK ada pagination yang diam-diam memotong baris kalau baris banyak dalam 1 hari                                                                                                                 |

## 2.4 Summary by Account — Filter Dimensi Outlet (**General Ledger — `summary-by-account`**)

Ini bagian PALING PENTING di file ini — membuktikan Business Unit benar-benar memisahkan kontribusi tiap outlet dari akun yang sama.

| Skenario                                                                                                             | Detail                                                                                                                                                             | Hasil                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — Outlet Kemang                                                                                              | `summary-by-account {business_unit_id:<Kemang>, date_from:"2026-02-01", date_to:"2026-02-06"}`                                                                     | PDT-01 (Minuman) Kemang = 10.640.000 (1.850.000+2.100.000+1.960.000+2.250.000+2.480.000 = 10.640.000, + 2.000.000 redemption §1.11 = **12.640.000**), PDT-02 (Makanan) Kemang = 620.000+705.000+640.000+700.000+810.000 = **3.475.000**, BBN-03 (Listrik) Kemang = 700.000                                        |
| Positif — Outlet Senayan                                                                                             | `summary-by-account {business_unit_id:<Senayan>, ...}`                                                                                                             | PDT-01 Senayan = 1.240.000+1.320.000+1.180.000+1.410.000+1.550.000 = **6.700.000**, PDT-02 Senayan = 410.000+455.000+390.000+480.000+520.000 = **2.255.000**, BBN-03 Senayan = 500.000                                                                                                                            |
| Positif — Outlet BSD                                                                                                 | `summary-by-account {business_unit_id:<BSD>, ...}`                                                                                                                 | PDT-01 BSD = 780.000+690.000+810.000+760.000+890.000 = **3.930.000**, PDT-02 BSD = 260.000+230.000+275.000+240.000+300.000 = **1.305.000**, BBN-03 BSD = 300.000, BBN-04 (Selisih Kas) BSD = 5.000                                                                                                                |
| **Positif — verifikasi total 3 outlet = total tanpa filter**                                                         | Jumlahkan PDT-01 ketiga outlet: 12.640.000+6.700.000+3.930.000                                                                                                     | Harus persis **23.270.000** — sama dengan saldo PDT-01 di §2.2 (tanpa filter BU). Sama untuk PDT-02: 3.475.000+2.255.000+1.305.000 = **7.035.000**                                                                                                                                                                |
| **Positif — baris tanpa `business_unit_id` tidak hilang**                                                            | Filter TANPA `business_unit_id` (default/all)                                                                                                                      | Total mencakup SEMUA baris termasuk yang tidak diisi BU sama sekali (AST-04, LIA-01, LIA-02, LIA-03, LIA-04, EKT-01, BBN-01, BBN-02) — pastikan baris tanpa BU tidak hilang dari laporan gabungan (regresi dari suite manufaktur §5.3)                                                                            |
| **Positif — Peralatan Dapur & Renovasi murni Outlet BSD (dimensi implisit via nama akun, bukan `business_unit_id`)** | Catatan: AST-08/AST-10 sengaja TIDAK diberi `business_unit_id` di jurnal akuisisinya (§1.14-1.15 file `01`) walau secara bisnis keduanya untuk ekspansi Outlet BSD | Kalau mau tampil di laporan per-BU BSD, jurnal akuisisi HARUSNYA diberi `business_unit_id:<BSD>` juga — kalau saat ini TIDAK diisi, catat ini sebagai keterbatasan DESAIN test case ini (bukan bug sistem), user bisa memilih isi dimensi di baris aset kalau mau breakdown lengkap per outlet termasuk investasi |

## 2.5 Verifikasi Persediaan Bahan Baku (Tanpa Dimensi Outlet — Persediaan Terpusat)

| Skenario           | Detail                                                                                                                                                                                                                                                                                                                    | Hasil                                                                                                                                                                                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif            | `detail-ledger {chart_of_account_id:<AST-06>}`                                                                                                                                                                                                                                                                            | 3 baris: opening (implisit dari saldo awal file `00`, TIDAK muncul sebagai baris GL biasa — cek apakah jurnal `JRN-OB-...` juga tampil di detail ledger akun ini, seharusnya IYA karena itu jurnal biasa juga), pemakaian §1.6 (kredit 9.906.750), restock §1.7 (debit 20.000.000) |
| **Catatan desain** | Persediaan Bahan Baku sengaja TIDAK dipecah per outlet (satu gudang pusat yang mensuplai ke-3 outlet) — beda dari Kas Kasir yang memang per-outlet secara fisik. Ini keputusan desain data test case, bukan keterbatasan sistem (kalau perlu persediaan per outlet, tinggal tambah `business_unit_id` di baris jurnalnya) | —                                                                                                                                                                                                                                                                                  |

## Referensi Silang

- [`01-jurnal-harian-penjualan-dan-akumulasi.id.md`](./01-jurnal-harian-penjualan-dan-akumulasi.id.md) — sumber seluruh angka di file ini
- [`03-tutup-periode-bulanan-dan-tahun-fiskal.id.md`](./03-tutup-periode-bulanan-dan-tahun-fiskal.id.md) — lanjutan setelah Trial Balance ini dikonfirmasi balanced
- [`../accounting-manufaktur/05-general-ledger-trial-balance-dan-laporan-keuangan.id.md`](../accounting-manufaktur/05-general-ledger-trial-balance-dan-laporan-keuangan.id.md) §5.1/§5.3 — dasar pola regresi 2-endpoint trial balance & filter dimensi BU
