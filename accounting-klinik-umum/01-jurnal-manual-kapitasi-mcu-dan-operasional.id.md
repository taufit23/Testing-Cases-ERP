---
title: (Klinik Umum Besar) — 01. Jurnal Manual — Kapitasi, MCU, Farmasi & Payroll Ganda
category: accounting-klinik-umum
description: 25 transaksi jurnal manual bulan Januari 2026 — inti suite ini. Pendapatan kapitasi BPJS flat per peserta terdaftar (6 cabang), piutang MCU korporat B2B, penjualan farmasi & produk ritel (PPN selektif), payroll dokter tetap vs paruh waktu, dan koreksi/reverse jurnal.
visibility: internal
---

# 01. Jurnal Manual — Kapitasi, MCU, Farmasi & Payroll Ganda

> Prasyarat: file [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) sudah selesai — 35 akun, Fiscal Year FY2026 + periode bulanan, 6 Business Unit, saldo awal terposting (Modal Pemilik **801.500.000**). Seluruh transaksi di file ini bertanggal **Januari 2026** (**Journals — `create`** via **Accounting Period** Januari, `status` awal draft lalu di-post — sesuaikan dengan alur approval aktif/nonaktif di branch test).
>
> **Verifikasi akhir file ini (dihitung 2 arah — per transaksi & akumulasi per akun, WAJIB cocok persis dengan file 02):**
>
> - Total Debit = Total Credit seluruh jurnal transaksi (T1-T25, tidak termasuk saldo awal) = **Rp 3.490.060.000**
> - Modal Pemilik TETAP 801.500.000 (belum ada transaksi yang menyentuh 3101 langsung — laba berjalan baru masuk equity saat Close Fiscal Year, file 03)
> - Laba (Rugi) berjalan per 2026-01-31 = **Pendapatan 987.100.000 − Beban 593.150.000 = Laba 393.950.000**
> - Total Aset akhir Januari = Total Liabilitas akhir + (Modal Pemilik + Laba berjalan) = **1.338.830.000 = 143.380.000 + 1.195.450.000**

## 1. Pendapatan Kapitasi BPJS Kesehatan (FKTP) — T1

**Titik uji paling penting di suite ini.** Kapitasi diakui **flat per bulan = jumlah peserta terdaftar per cabang × tarif kapitasi Rp 8.000/peserta/bulan** — TIDAK dikoreksi oleh jumlah kunjungan aktual. Jurnal ini WAJIB dibuat 1x di awal bulan (accrual), bukan diakumulasi harian dari kunjungan pasien seperti pola fee-for-service di §2.

| Cabang    | Peserta Terdaftar | Tarif/Peserta | Pendapatan Kapitasi |
| --------- | ----------------: | ------------: | ------------------: |
| JKP       |            18.000 |         8.000 |         144.000.000 |
| BKS       |            15.000 |         8.000 |         120.000.000 |
| TGR       |            12.500 |         8.000 |         100.000.000 |
| DPK       |            10.000 |         8.000 |          80.000.000 |
| BGR       |             8.000 |         8.000 |          64.000.000 |
| BDG       |             4.500 |         8.000 |          36.000.000 |
| **Total** |                   |               |     **544.000.000** |

| Skenario                                                             | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Hasil                                                                                                                                                                                                   |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — T1 accrual kapitasi                                        | `POST accounting/journals/create {date:"2026-01-01", description:"Akrual Pendapatan Kapitasi BPJS Kesehatan Januari 2026 - 6 cabang", lines:[{account_id:<1104>, debit:544000000}, {account_id:<4101>, credit:144000000, business_unit_id:<JKP>}, {account_id:<4101>, credit:120000000, business_unit_id:<BKS>}, {account_id:<4101>, credit:100000000, business_unit_id:<TGR>}, {account_id:<4101>, credit:80000000, business_unit_id:<DPK>}, {account_id:<4101>, credit:64000000, business_unit_id:<BGR>}, {account_id:<4101>, credit:36000000, business_unit_id:<BDG>}]}` lalu `post` | 201 lalu posted — Dr 1104 544.000.000 = jumlah 6 baris Cr 4101 per cabang                                                                                                                               |
| **Positif — pembuktian "flat, bukan fee-for-service" (kasus kunci)** | Asumsikan sepanjang Januari cabang JKP hanya dikunjungi 3.200 kali (bukan 18.000×rata-rata kunjungan bulanan wajar) — TIDAK ada penyesuaian ke bawah pada 4101 JKP                                                                                                                                                                                                                                                                                                                                                                                                                      | Pendapatan Kapitasi JKP tetap **144.000.000** persis — kalau ERP/staf keliru menghitung ulang berdasarkan kunjungan aktual, angka ini PASTI berubah dan salah. Catat hasil aktual sebagai bukti akurasi |
| Negatif                                                              | Baris Dr tidak sama dengan total baris Cr (mis. sengaja pasang Dr 1104 500.000.000 padahal total Cr tetap 544.000.000)                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Ditolak `unbalanced_journal_entry` atau sejenis — jurnal tidak boleh posted timpang                                                                                                                     |
| Netralisasi                                                          | Simpan T1 — dipakai §2 (transfer BPJS) dan seluruh file berikutnya                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## 2. Pencairan Dana Kapitasi BPJS ke Bank BCA Penampungan — T2 & T2b

| #   | Tanggal    | Deskripsi                                                                                                                                                                       | Jurnal                                                       |       Nilai |
| --- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------: |
| T2  | 2026-01-10 | Pelunasan PENUH piutang kapitasi Desember 2025 (saldo awal 1104) — BPJS transfer bulan berjalan untuk klaim bulan sebelumnya (lag 1 bulan, wajar)                               | Dr 1103 Bank BCA Penampungan / Cr 1104 Piutang Kapitasi BPJS | 162.000.000 |
| T2b | 2026-01-25 | Transfer PARSIAL kapitasi Januari 2026 (dari T1, 544.000.000) — BPJS mencairkan sebagian lebih awal, sisanya menyusul bulan depan (pola realistis, BUKAN keterlambatan/masalah) | Dr 1103 Bank BCA Penampungan / Cr 1104 Piutang Kapitasi BPJS | 300.000.000 |

| Skenario      | Detail                                                                                                       | Hasil                                                                                                                                                                                                                                                                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — T2  | `POST accounting/journals/create` sesuai tabel, `post`                                                       | Piutang Kapitasi BPJS (1104) turun 162.000.000, Bank BCA Penampungan naik jadi 257.000.000                                                                                                                                                                                                                                            |
| Positif — T2b | Sama, `post`                                                                                                 | Piutang Kapitasi BPJS (1104) sisa = 162.000.000 (awal) + 544.000.000 (T1) − 162.000.000 (T2) − 300.000.000 (T2b) = **244.000.000** — SEMENTARA masih outstanding, mencerminkan lag pencairan bulanan BPJS yang wajar (BUKAN piutang macet)                                                                                            |
| Negatif       | Transfer BPJS melebihi saldo piutang yang ada (mis. Cr 1104 700.000.000 padahal saldo cuma 544.000.000+sisa) | Sistem TIDAK otomatis menolak nilai jurnal manual melebihi saldo akun tertentu (jurnal manual bebas nilai, bukan seperti pembayaran invoice berbasis dokumen) — cek behavior aktual, kalau tidak ada guard catat sebagai keterbatasan wajar untuk jurnal manual bebas (bukan gap desain, karena `accounting/journals` memang generik) |
| Netralisasi   | Simpan sisa piutang 244.000.000 — dipakai §10 rangkuman                                                      |

## 3. Pendapatan Jasa Non-Kapitasi / Fee-for-Service Umum — T3a-T3d

Rekap pendapatan kas harian pasien umum bayar langsung + asuransi swasta non-kapitasi, dikumpulkan mingguan ke Kas Kecil Klinik Pusat (kontrol tunggal, dimensi per cabang di luar scope pemisahan detail suite ini — lihat §11 catatan desain).

| #   | Tanggal    | Jurnal                                              |           Nilai |
| --- | ---------- | --------------------------------------------------- | --------------: |
| T3a | 2026-01-07 | Dr 1101 Kas Kecil / Cr 4102 Pendapatan Non-Kapitasi |      42.500.000 |
| T3b | 2026-01-14 | Dr 1101 Kas Kecil / Cr 4102 Pendapatan Non-Kapitasi |      38.700.000 |
| T3c | 2026-01-21 | Dr 1101 Kas Kecil / Cr 4102 Pendapatan Non-Kapitasi |      45.200.000 |
| T3d | 2026-01-28 | Dr 1101 Kas Kecil / Cr 4102 Pendapatan Non-Kapitasi |      40.100.000 |
|     |            | **Total Januari**                                   | **166.500.000** |

| Skenario    | Detail                              | Hasil                                                                             |
| ----------- | ----------------------------------- | --------------------------------------------------------------------------------- |
| Positif     | 4 jurnal di atas, `post` semua      | Kas Kecil (1101) naik kumulatif, 4102 akumulasi jadi 166.500.000 pada akhir bulan |
| Netralisasi | Simpan — dipakai §7 (setoran kasir) |

## 4. Pendapatan MCU Korporat (Piutang B2B, Termin) — T4a & T4b

| #   | Tanggal    | Klien Korporat (nama bebas, bukan `Contact`)                                   | Jurnal                                                                           |           Nilai |
| --- | ---------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | --------------: |
| T4a | 2026-01-05 | PT Nusantara Logistik Indonesia — MCU 100 karyawan, termin 30 hari, cabang JKP | Dr 1105 Piutang MCU Korporat & Asuransi Swasta / Cr 4103 Pendapatan MCU Korporat |      85.000.000 |
| T4b | 2026-01-18 | PT Cipta Mandiri Sejahtera — MCU 60 karyawan, termin 30 hari, cabang BKS       | Dr 1105 Piutang MCU Korporat & Asuransi Swasta / Cr 4103 Pendapatan MCU Korporat |      52.000.000 |
|     |            | **Total**                                                                      |                                                                                  | **137.000.000** |

| Skenario    | Detail                                                                      | Hasil                                     |
| ----------- | --------------------------------------------------------------------------- | ----------------------------------------- |
| Positif     | 2 jurnal di atas, `post`                                                    | 1105 naik 137.000.000, 4103 = 137.000.000 |
| Negatif     | Nilai jurnal negatif atau `date` di luar periode Januari yang sudah terbuka | 422/ditolak sesuai validasi periode       |
| Netralisasi | Simpan — dipakai §5 (pelunasan sebagian)                                    |

## 5. Pelunasan Sebagian Piutang MCU dari Saldo Awal — T5

Termin pembayaran MCU korporat dari saldo awal (87.500.000, kontrak sebelum Januari) jatuh tempo dan dibayar SEBAGIAN.

| Skenario                                      | Payload                                                                                                                                                                                                            | Hasil                                                                                                                                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                       | `POST accounting/journals/create {date:"2026-01-20", description:"Pelunasan sebagian piutang MCU korporat saldo awal", lines:[{account_id:<1102>, debit:60000000}, {account_id:<1105>, credit:60000000}]}`, `post` | Bank Mandiri (1102) naik 60.000.000, Piutang MCU (1105) turun 60.000.000                                                                                         |
| **Positif — sisa piutang B2B (kasus termin)** | Hitung manual: 87.500.000 (awal) + 85.000.000 (T4a) + 52.000.000 (T4b) − 60.000.000 (T5)                                                                                                                           | Sisa Piutang MCU Korporat & Asuransi Swasta akhir Januari = **164.500.000** — masih outstanding sesuai termin masing-masing kontrak (wajar, bukan piutang macet) |
| Netralisasi                                   | Simpan sisa 164.500.000 — dipakai §10 rangkuman dan file 06 (item ditemukan saat rekonsiliasi)                                                                                                                     |

## 6. Pendapatan Laboratorium (Walk-in) — T6 (dengan demonstrasi koreksi/reverse) — T20

| Skenario                           | Detail                                                                                                                                                                                                                        | Hasil                                                                                                                                                                                                                                            |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif — T6 awal (SALAH, sengaja) | `POST accounting/journals/create {date:"2026-01-15", description:"Pendapatan Laboratorium walk-in Januari (via EDC/transfer)", lines:[{account_id:<1102>, debit:28400000}, {account_id:<4104>, credit:28400000}]}`, `post`    | 201 posted, Bank Mandiri +28.400.000, 4104 = 28.400.000                                                                                                                                                                                          |
| **Negatif/Koreksi — T20 reverse**  | Belakangan diketahui staf salah input — nilai sebenarnya di bukti EDC adalah Rp 24.800.000, bukan Rp 28.400.000 (transposisi angka). `POST accounting/journals/reverse {id:<T6>}`                                             | 200 — jurnal pembalik terpost (Cr 1102 28.400.000 / Dr 4104 28.400.000), `is_reversed:true` di T6, saldo Bank Mandiri & 4104 kembali ke posisi sebelum T6 (additive, bukan hapus — konsisten dengan fix `Journal::reverse()` project 2026-08-01) |
| Positif — T20 repost nilai benar   | `POST accounting/journals/create {date:"2026-01-15", description:"Pendapatan Laboratorium walk-in Januari (koreksi nilai benar)", lines:[{account_id:<1102>, debit:24800000}, {account_id:<4104>, credit:24800000}]}`, `post` | 201 posted — 4104 akhir Januari = **24.800.000** (bukan 28.400.000), Bank Mandiri net dari rangkaian T6+reverse+repost = **+24.800.000**                                                                                                         |
| Netralisasi                        | Simpan nilai akhir 24.800.000 sebagai acuan file 02                                                                                                                                                                           |

## 7. Setoran Kasir Harian ke Bank — T-Setoran (4x)

Kas Kecil Klinik Pusat dikontrol ketat — hasil pendapatan tunai (§3, §8, §9) disetor periodik ke Bank Mandiri, bukan dibiarkan menumpuk (pola sama dengan suite F&B kafe).

| #         | Tanggal    | Jurnal                                   |           Nilai |
| --------- | ---------- | ---------------------------------------- | --------------: |
| Setoran-1 | 2026-01-08 | Dr 1102 Bank Mandiri / Cr 1101 Kas Kecil |      65.000.000 |
| Setoran-2 | 2026-01-15 | Dr 1102 Bank Mandiri / Cr 1101 Kas Kecil |      70.000.000 |
| Setoran-3 | 2026-01-22 | Dr 1102 Bank Mandiri / Cr 1101 Kas Kecil |      75.000.000 |
| Setoran-4 | 2026-01-31 | Dr 1102 Bank Mandiri / Cr 1101 Kas Kecil |      73.280.000 |
|           |            | **Total**                                | **283.280.000** |

| Skenario    | Detail                                   | Hasil                                                                                                                                                                                                                                                  |
| ----------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif     | 4 jurnal di atas, `post` semua           | Total setoran 283.280.000 PERSIS = total pendapatan tunai terkumpul di Kas Kecil (T3: 166.500.000 + T7 farmasi: 96.800.000 + T8 ritel: 19.980.000, lihat §8-9) — kalau tidak persis, ada baris pendapatan tunai yang lupa disetorkan atau salah hitung |
| Netralisasi | Simpan — Kas Kecil sisa untuk opname §12 |

## 8. Penjualan Obat & Farmasi (Bebas PPN) — T7

| Skenario    | Payload                                                                                                                                                                                                                               | Hasil                                                                                        |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Positif     | `POST accounting/journals/create {date:"2026-01-31", description:"Rekap penjualan obat & farmasi apotek klinik Januari 2026 (bebas PPN)", lines:[{account_id:<1101>, debit:96800000}, {account_id:<4105>, credit:96800000}]}`, `post` | Kas Kecil +96.800.000, 4105 = 96.800.000, **TIDAK ada baris PPN Keluaran** (obat dibebaskan) |
| Netralisasi | Simpan — dipakai §7 (setoran) dan §10                                                                                                                                                                                                 |

## 9. Penjualan Produk Kesehatan Non-Obat Ritel (Kena PPN 11%) — T8

DPP (harga sebelum pajak) = Rp 18.000.000, PPN 11% = Rp 1.980.000, total diterima Rp 19.980.000.

| Skenario                                                                                             | Payload                                                                                                                                                                                                                                                                          | Hasil                                                                                                                             |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                                                              | `POST accounting/journals/create {date:"2026-01-31", description:"Rekap penjualan produk kesehatan non-obat ritel Januari 2026 (kena PPN 11%)", lines:[{account_id:<1101>, debit:19980000}, {account_id:<4106>, credit:18000000}, {account_id:<2102>, credit:1980000}]}`, `post` | Kas Kecil +19.980.000, 4106 = 18.000.000, PPN Keluaran (2102) = 1.980.000                                                         |
| **Positif — pembuktian PPN selektif (kasus kunci, ulangan tema klinik gigi dengan konteks berbeda)** | Bandingkan dengan T7 (obat, bebas PPN) yang bertanggal & bernilai mirip                                                                                                                                                                                                          | Hanya T8 yang memicu PPN Keluaran — T7 dan seluruh transaksi jasa medis (T1, T3, T4, T6) TIDAK — verifikasi ulang di file 06 §PPN |
| Netralisasi                                                                                          | Simpan — dipakai §7 (setoran) dan file 06                                                                                                                                                                                                                                        |

## 10. Pembelian Farmasi & BHP Medis dari Distributor (Kredit) — T9a & T9b

Kasus baru: PPN Masukan **selektif** per jenis barang — pembelian obat TIDAK memicu PPN Masukan (obat dibebaskan), sedangkan pembelian BHP medis/alat kesehatan MEMICU PPN Masukan.

| #   | Tanggal    | Deskripsi                                                                                                | Jurnal                                                                                                         |       Nilai |
| --- | ---------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------: |
| T9a | 2026-01-08 | Beli obat generik & paten dari PT Distrifarma Nusantara, kredit, **bebas PPN**                           | Dr 1106 Persediaan Obat 120.000.000 / Cr 2101 Utang Dagang 120.000.000                                         | 120.000.000 |
| T9b | 2026-01-12 | Beli BHP medis & alkes dari PT Alkes Prima Distribusi, kredit, **kena PPN Masukan 11%** (DPP 40.000.000) | Dr 1107 Persediaan BHP Medis & Lab 40.000.000, Dr 1108 PPN Masukan 4.400.000 / Cr 2101 Utang Dagang 44.400.000 |  44.400.000 |

| Skenario                                        | Detail                                                | Hasil                                                                                                                                                              |
| ----------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif T9a                                     | `post`                                                | 1106 naik 120.000.000, 2101 naik 120.000.000, **TIDAK ada baris 1108**                                                                                             |
| Positif T9b                                     | `post`                                                | 1107 naik 40.000.000, 1108 (PPN Masukan) naik 4.400.000, 2101 naik 44.400.000                                                                                      |
| **Positif — verifikasi selektif (kasus kunci)** | Bandingkan T9a vs T9b                                 | Hanya T9b yang menyentuh 1108 — bukti bahwa PPN Masukan tergantung KATEGORI BARANG (alkes/BHP) bukan otomatis dari SEMUA pembelian kredit dari distributor sejenis |
| Netralisasi                                     | Simpan — dipakai §13 (pembayaran utang) dan §11 (HPP) |

## 11. HPP Obat & BHP Medis Terpakai (Akhir Bulan) — T10

Beban langsung berdasarkan estimasi pemakaian bulan berjalan (bukan metode persediaan perpetual/FIFO — di luar scope modul Inventory).

| Skenario                         | Payload                                                                                                                                                                                                                                          | Hasil                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Positif                          | `POST accounting/journals/create {date:"2026-01-31", description:"HPP Obat & BHP Medis terpakai Januari 2026", lines:[{account_id:<5104>, debit:88500000}, {account_id:<1106>, credit:70000000}, {account_id:<1107>, credit:18500000}]}`, `post` | 5104 = 88.500.000, Persediaan Obat (1106) turun 70.000.000, Persediaan BHP (1107) turun 18.500.000 |
| Positif — saldo akhir persediaan | Hitung manual: 1106 = 145.000.000 + 120.000.000 (T9a) − 70.000.000 = **195.000.000**; 1107 = 58.750.000 + 40.000.000 (T9b) − 18.500.000 = **80.250.000**                                                                                         | Cocok dengan Trial Balance file 02                                                                 |
| Netralisasi                      | Simpan angka akhir persediaan                                                                                                                                                                                                                    |

## 12. Akrual Payroll Dokter — Dua Pola Berbeda (T11 & T12)

**Kasus kunci kedua suite ini**: gaji dokter umum tetap FLAT bulanan (tidak terikat kunjungan) vs fee dokter spesialis paruh waktu VARIABEL per kunjungan.

| #   | Tanggal    | Detail                                                                                                                                                    | Jurnal                                                                                          |       Nilai |
| --- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------: |
| T11 | 2026-01-31 | Akrual gaji dokter umum tetap 6 cabang, flat bulanan sesuai kontrak (TIDAK terikat jumlah kunjungan)                                                      | Dr 5101 Beban Gaji Dokter Umum Tetap / Cr 2103 Utang Gaji Dokter Umum Tetap                     | 156.000.000 |
| T12 | 2026-01-31 | Akrual fee dokter spesialis paruh waktu — 3 spesialis (anak, kandungan, umum lanjutan), total 640 kunjungan gabungan 6 cabang × tarif Rp 75.000/kunjungan | Dr 5102 Beban Fee Dokter Spesialis Paruh Waktu / Cr 2104 Utang Fee Dokter Spesialis Paruh Waktu |  48.000.000 |

| Skenario                                        | Detail                                                                                                                                                                  | Hasil                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif T11                                     | `post`                                                                                                                                                                  | 2103 = 42.000.000 (awal) + 156.000.000 = 198.000.000 sebelum dibayar (§13)                                                                                                                                                                                                                 |
| Positif T12                                     | `post`                                                                                                                                                                  | 2104 = 28.600.000 (awal) + 48.000.000 = 76.600.000 sebelum dibayar (§13)                                                                                                                                                                                                                   |
| **Positif — kontras pola akrual (kasus kunci)** | Bandingkan T11 (flat, tidak ada variabel "jumlah kunjungan" di payload/perhitungan) vs T12 (`640 × 75.000 = 48.000.000`, WAJIB linear terhadap jumlah kunjungan aktual) | Kalau jumlah kunjungan spesialis paruh waktu naik jadi 700 bulan depan, fee HARUS naik proporsional (700×75.000=52.500.000) — SEBALIKNYA kapitasi (§1) harus tetap flat walau kunjungan naik. Dua logika ini harus dijaga TIDAK tertukar di implementasi manapun yang mereplikasi pola ini |
| Netralisasi                                     | Simpan — dipakai §13                                                                                                                                                    |

## 13. Pembayaran Payroll Dokter (Parsial vs Lunas) — T13 & T14

| #   | Tanggal    | Detail                                                                                                                   | Jurnal                                                                |       Nilai |
| --- | ---------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- | ----------: |
| T13 | 2026-01-31 | Bayar gaji dokter umum tetap — SEBAGIAN dari total utang 198.000.000 (sisa dibayar awal Februari, siklus payroll normal) | Dr 2103 Utang Gaji Dokter Umum Tetap / Cr 1102 Bank Mandiri           | 180.000.000 |
| T14 | 2026-01-31 | Bayar fee dokter spesialis paruh waktu — LUNAS dari total utang 76.600.000                                               | Dr 2104 Utang Fee Dokter Spesialis Paruh Waktu / Cr 1102 Bank Mandiri |  76.600.000 |

| Skenario    | Detail                        | Hasil                                                                                     |
| ----------- | ----------------------------- | ----------------------------------------------------------------------------------------- |
| Positif T13 | `post`                        | 2103 sisa = 198.000.000 − 180.000.000 = **18.000.000** (carry forward ke Februari, wajar) |
| Positif T14 | `post`                        | 2104 sisa = **0** (lunas)                                                                 |
| Netralisasi | Simpan sisa 2103 = 18.000.000 |

## 14. Pelunasan Utang Awal Non-Dokter & PPh 21, Gaji Karyawan Non-Dokter Januari — T15a-T15c

| #    | Tanggal    | Detail                                                                                                                                 | Jurnal                                                                                                                          |       Nilai |
| ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------: |
| T15a | 2026-01-05 | Bayar LUNAS utang gaji karyawan non-dokter saldo awal                                                                                  | Dr 2105 Utang Gaji Karyawan Non-Dokter / Cr 1102 Bank Mandiri                                                                   |  65.000.000 |
| T15b | 2026-01-15 | Setor LUNAS utang PPh 21 karyawan saldo awal ke kas negara                                                                             | Dr 2106 Utang PPh 21 Karyawan / Cr 1102 Bank Mandiri                                                                            |   9.750.000 |
| T15c | 2026-01-31 | Gaji karyawan non-dokter (perawat, admin, apoteker, driver ambulans) Januari — dibayar netto langsung, PPh 21 dipotong jadi utang baru | Dr 5103 Beban Gaji Karyawan Non-Dokter 210.000.000 / Cr 1102 Bank Mandiri 197.400.000, Cr 2106 Utang PPh 21 Karyawan 12.600.000 | 210.000.000 |

| Skenario     | Detail                   | Hasil                                                                                         |
| ------------ | ------------------------ | --------------------------------------------------------------------------------------------- |
| Positif T15a | `post`                   | 2105 = 0                                                                                      |
| Positif T15b | `post`                   | 2106 sementara = 0 (sebelum T15c)                                                             |
| Positif T15c | `post`                   | 5103 = 210.000.000, 2106 akhir Januari = **12.600.000** (utang PPh 21 baru, disetor Februari) |
| Netralisasi  | Simpan — dipakai file 02 |

## 15. Beban Operasional Rutin — T16 & T17

| #   | Tanggal    | Jurnal                                                                  |      Nilai |
| --- | ---------- | ----------------------------------------------------------------------- | ---------: |
| T16 | 2026-01-03 | Dr 5105 Beban Sewa Klinik/Gedung / Cr 1102 Bank Mandiri (6 cabang)      | 66.000.000 |
| T17 | 2026-01-31 | Dr 5106 Beban Listrik, Air & Internet / Cr 1102 Bank Mandiri (6 cabang) | 24.300.000 |

| Skenario    | Detail           | Hasil                                                       |
| ----------- | ---------------- | ----------------------------------------------------------- |
| Positif     | 2 jurnal, `post` | 5105=66.000.000, 5106=24.300.000, Bank Mandiri turun sesuai |
| Netralisasi | Simpan           |

## 16. Pemindahan Dana Kapitasi ke Rekening Operasional — T21

| Skenario                        | Payload                                                                                                                                                                                                                                                                                | Hasil                                                                                                                                               |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                         | `POST accounting/journals/create {date:"2026-01-29", description:"Pemindahan dana kapitasi BPJS dari BCA Penampungan ke Mandiri Operasional untuk kebutuhan operasional bulan berjalan", lines:[{account_id:<1102>, debit:400000000}, {account_id:<1103>, credit:400000000}]}`, `post` | Bank Mandiri +400.000.000, Bank BCA Penampungan −400.000.000                                                                                        |
| Positif — saldo BCA Penampungan | Hitung manual: 95.000.000 (awal) + 162.000.000 (T2) + 300.000.000 (T2b) − 400.000.000 (T21)                                                                                                                                                                                            | Sisa Bank BCA Penampungan akhir Januari = **157.000.000** (buffer, belum semua dipindahkan — realistis, tidak semua dana kapitasi langsung dikuras) |
| Netralisasi                     | Simpan angka akhir 157.000.000                                                                                                                                                                                                                                                         |

## 17. Pembayaran Sebagian Utang Dagang Distributor — T18

| Skenario             | Payload                                                                                                                                                                                                                              | Hasil                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Positif              | `POST accounting/journals/create {date:"2026-01-25", description:"Pembayaran sebagian utang dagang distributor farmasi/alkes Januari", lines:[{account_id:<2101>, debit:150000000}, {account_id:<1102>, credit:150000000}]}`, `post` | Utang Dagang (2101) turun 150.000.000, Bank Mandiri turun 150.000.000 |
| Positif — sisa utang | Hitung manual: 96.400.000 (awal) + 120.000.000 (T9a) + 44.400.000 (T9b) − 150.000.000 (T18)                                                                                                                                          | Sisa Utang Dagang akhir Januari = **110.800.000** (termin, wajar)     |
| Netralisasi          | Simpan angka akhir                                                                                                                                                                                                                   |

## 18. Opname Kas Kecil Akhir Bulan — T19

| Skenario                        | Payload                                                                                                                                                                                                             | Hasil                                                                                                                  |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Positif — selisih kurang        | `POST accounting/journals/create {date:"2026-01-31", description:"Opname kas kecil akhir bulan - selisih kurang ditemukan", lines:[{account_id:<5109>, debit:350000}, {account_id:<1101>, credit:350000}]}`, `post` | 5109 = 350.000, Kas Kecil turun 350.000                                                                                |
| Positif — saldo akhir Kas Kecil | Hitung manual: 15.000.000 (awal) + 283.280.000 (T3+T7+T8, total masuk) − 283.280.000 (setoran §7) − 350.000 (T19)                                                                                                   | **14.650.000** — sangat dekat saldo awal, membuktikan kontrol kas kecil ketat berjalan (bukan menumpuk tak terkendali) |
| Netralisasi                     | Simpan angka akhir 14.650.000                                                                                                                                                                                       |

## 19. Bank Mandiri Operasional — Ringkasan Pergerakan

| Komponen                                  |           Nilai |
| ----------------------------------------- | --------------: |
| Saldo awal                                |     480.000.000 |
| + Setoran kasir (§7)                      |     283.280.000 |
| + Pelunasan piutang MCU (T5)              |      60.000.000 |
| + Pendapatan Laboratorium net (T6+T20)    |      24.800.000 |
| + Pemindahan dana kapitasi (T21)          |     400.000.000 |
| − Bayar gaji dokter tetap (T13)           |   (180.000.000) |
| − Bayar fee dokter paruh waktu (T14)      |    (76.600.000) |
| − Bayar utang gaji non-dokter awal (T15a) |    (65.000.000) |
| − Setor PPh 21 awal (T15b)                |     (9.750.000) |
| − Gaji non-dokter Januari netto (T15c)    |   (197.400.000) |
| − Sewa klinik (T16)                       |    (66.000.000) |
| − Listrik/air/internet (T17)              |    (24.300.000) |
| − Bayar utang dagang (T18)                |   (150.000.000) |
| **Saldo akhir 31 Jan 2026**               | **479.030.000** |

## 20. Ringkasan Verifikasi Akhir File 01

| Akun                                        |  Saldo Awal | Pergerakan Bersih | Saldo Akhir 31 Jan 2026 |
| ------------------------------------------- | ----------: | ----------------: | ----------------------: |
| 1101 Kas Kecil Klinik Pusat                 |  15.000.000 |          −350.000 |              14.650.000 |
| 1102 Bank Mandiri Operasional               | 480.000.000 |          −950.000 |             479.030.000 |
| 1103 Bank BCA Penampungan Kapitasi          |  95.000.000 |       +62.000.000 |             157.000.000 |
| 1104 Piutang Kapitasi BPJS                  | 162.000.000 |       +82.000.000 |             244.000.000 |
| 1105 Piutang MCU Korporat & Asuransi Swasta |  87.500.000 |       +77.000.000 |             164.500.000 |
| 1106 Persediaan Obat                        | 145.000.000 |       +50.000.000 |             195.000.000 |
| 1107 Persediaan BHP Medis & Lab             |  58.750.000 |       +21.500.000 |              80.250.000 |
| 1108 PPN Masukan                            |           0 |        +4.400.000 |               4.400.000 |
| 2101 Utang Dagang Distributor               |  96.400.000 |       +14.400.000 |             110.800.000 |
| 2102 PPN Keluaran                           |           0 |        +1.980.000 |               1.980.000 |
| 2103 Utang Gaji Dokter Umum Tetap           |  42.000.000 |       −24.000.000 |              18.000.000 |
| 2104 Utang Fee Dokter Spesialis Paruh Waktu |  28.600.000 |       −28.600.000 |                       0 |
| 2105 Utang Gaji Karyawan Non-Dokter         |  65.000.000 |       −65.000.000 |                       0 |
| 2106 Utang PPh 21 Karyawan                  |   9.750.000 |        +2.850.000 |              12.600.000 |
| 4101 Pendapatan Kapitasi BPJS               |           — |                 — |             544.000.000 |
| 4102 Pendapatan Non-Kapitasi/FFS            |           — |                 — |             166.500.000 |
| 4103 Pendapatan MCU Korporat                |           — |                 — |             137.000.000 |
| 4104 Pendapatan Laboratorium                |           — |                 — |              24.800.000 |
| 4105 Pendapatan Obat & Farmasi              |           — |                 — |              96.800.000 |
| 4106 Pendapatan Produk Non-Obat Ritel       |           — |                 — |              18.000.000 |
| 5101-5109 (total Beban)                     |           — |                 — |             593.150.000 |

**Verifikasi persamaan akuntansi dasar (WAJIB balance, dipakai file 02):**

```
Total Aset akhir Januari  = 14.650.000 + 479.030.000 + 157.000.000 + 244.000.000 + 164.500.000
                             + 195.000.000 + 80.250.000 + 4.400.000
                           = 1.338.830.000

Total Liabilitas akhir    = 110.800.000 + 1.980.000 + 18.000.000 + 0 + 0 + 12.600.000
                           = 143.380.000

Total Pendapatan Januari  = 544.000.000 + 166.500.000 + 137.000.000 + 24.800.000 + 96.800.000 + 18.000.000
                           = 987.100.000

Total Beban Januari       = 156.000.000 + 48.000.000 + 210.000.000 + 88.500.000 + 66.000.000
                             + 24.300.000 + 0 + 0 + 350.000
                           = 593.150.000

Laba Berjalan              = 987.100.000 − 593.150.000 = 393.950.000

Cek: Total Aset (1.338.830.000) = Total Liabilitas (143.380.000)
                                  + Modal Pemilik (801.500.000) + Laba Berjalan (393.950.000)
                                = 143.380.000 + 1.195.450.000 = 1.338.830.000 ✓ BALANCE
```

## 21. Catatan Desain — Margin Tinggi Bulan Ini (Bukan Anomali)

Margin laba Januari (393.950.000 / 987.100.000 ≈ 40%) sengaja terlihat tinggi — ini justru **ciri ekonomi kapitasi yang realistis**: pendapatan kapitasi (544.000.000, 55% dari total pendapatan) bersifat FLAT dan sudah diterima terlepas dari biaya layanan aktual, sementara biaya variabel (fee dokter spesialis, HPP obat) hanya terikat ke pemanfaatan riil yang lebih rendah dari kapasitas peserta terdaftar. Dalam praktik nyata, klinik FKTP menanggung **risiko biaya** — kalau utilisasi peserta naik tajam (wabah, musim penyakit tertentu), margin bisa menipis drastis di bulan lain tanpa kapitasi ikut naik. Suite ini tidak memodelkan skenario utilisasi tinggi (di luar scope, bisa jadi kasus lanjutan kalau dibutuhkan).

## 22. Catatan Desain — Dimensi Business Unit Tidak Merata di Semua Transaksi

Hanya T1 (Pendapatan Kapitasi) yang didemonstrasikan dengan pemisahan `business_unit_id` penuh ke 6 cabang — ini SENGAJA dipilih sebagai transaksi utama untuk dimensi cabang (konsisten dengan tema utama suite: kapitasi per cabang). Transaksi lain (T3-T19) dicatat konsolidasi pusat TANPA breakdown cabang, kecuali disebutkan eksplisit (T4a=JKP, T4b=BKS) — keputusan ini menjaga suite tetap fokus dan tidak membengkak jadi puluhan baris per transaksi. File 04 (Laporan Keuangan per cabang) akan menampilkan breakdown cabang HANYA untuk lini kapitasi, sisanya konsolidasi — dicatat eksplisit di sana juga.

## Referensi Silang

- File [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) — saldo awal & Modal Pemilik 801.500.000
- File [`02-general-ledger-dan-trial-balance-per-cabang.id.md`](./02-general-ledger-dan-trial-balance-per-cabang.id.md) — Trial Balance total debit=kredit **1.931.980.000**, dihitung dari saldo akhir file ini
- `App\Services\JournalPostingService` & `Accounting\Journal::reverse()`/`reverseBulk()` — implementasi posting & reverse additive (fix 2026-08-01), didemonstrasikan di §6 (T6+T20)
