---
title: — 01. Jurnal Transaksi Tahun 2025 (Januari-Desember)
category: Accounting 2
description: 104 jurnal manual selama FY2025 penuh untuk PT Retail Nusantara Jaya — tiap bulan minimal 2 transaksi fundamental (pendapatan + beban operasional) plus minimal 3 transaksi lain (siklus utang dagang, penyusutan, cicilan pinjaman bank, dan variasi khusus: prive, selisih kas, PPh 21, iklan). Angka checkpoint kuartalan disertakan sebagai acuan pembanding saat testing.
visibility: internal
---

# 01. Jurnal Transaksi Tahun 2025 (Januari-Desember)

> Prasyarat: master data & modal awal di [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) sudah ada, termasuk Fiscal Year FY2025 (12 periode bulanan) dan 2 jurnal modal awal (2025-01-02).

## Cara Baca File Ini

Semua transaksi di bawah dikerjakan lewat halaman **Journals → + Create Journal** (sama seperti `../accounting/01-jurnal-manual.id.md`): isi Code (auto)/Date/Description di header, masukkan tiap baris "Baris Jurnal" ke tabel form (pilih Account dari dropdown, isi Debit atau Kredit, isi Business Unit kalau baris itu Penjualan atau Beban Sewa — lihat catatan dimensi di bawah), pastikan badge **Balanced**, klik **Save**, lalu **Post** (kalau branch kamu `requires_journal_approval:false`) atau lewati proses approval dulu (kalau `true`, lihat pola di `../accounting/01-jurnal-manual.id.md` §1.5).

**Dimensi Business Unit** — setiap baris "Rekap penjualan tunai bulanan" sebenarnya berisi **2 baris kredit Penjualan terpisah** dengan `business_unit_id` berbeda (Toko Pusat untuk baris pertama, Toko Cabang untuk baris kedua) — kolom "Baris Jurnal" di tabel bawah menuliskan keduanya berurutan. Baris **Beban Sewa Toko** dimensikan ke **Toko Pusat** (konsisten dengan `../accounting/01-jurnal-manual.id.md` §1.4). Baris lain TIDAK perlu Business Unit kecuali disebutkan.

**Setiap bulan berisi minimal 5 transaksi** (2 fundamental: rekap penjualan + beban operasional; 3 tambahan tetap: setor kas ke bank, pengakuan HPP, pembelian persediaan kredit — DITAMBAH pembayaran utang dagang mulai Februari, penyusutan mulai Februari, cicilan pinjaman mulai Februari) — total 6-9 transaksi/bulan tergantung ada tidaknya variasi khusus (PPh 21 kuartalan, prive, selisih kas, iklan). Lihat ringkasan jumlah di bagian akhir file ini.

## Ringkasan Angka Bulanan (Formula Tetap FY2025)

| Komponen                          |                      Nilai FY2025 | Catatan                                                                  |
| --------------------------------- | --------------------------------: | ------------------------------------------------------------------------ |
| Penjualan Toko Pusat (bulanan)    |                        50.000.000 | + PPN Keluaran 11% = 5.500.000                                           |
| Penjualan Toko Cabang (bulanan)   |                        30.000.000 | + PPN Keluaran 11% = 3.300.000                                           |
| Total kas diterima/bulan          |                        88.800.000 | Debit Kas Kecil, langsung disetor penuh ke Bank BCA (transaksi terpisah) |
| HPP diakui/bulan                  |                        50.000.000 | Margin kotor ≈ 30.000.000/bulan (37,5%)                                  |
| Beban Sewa Toko/bulan             |                         8.000.000 | Business Unit: Toko Pusat                                                |
| Beban Gaji Karyawan (gross)/bulan |                        15.000.000 | Potongan PPh 21 2,5% = 375.000, net dibayar 14.625.000                   |
| Beban Listrik & Air/bulan         |                         2.000.000 | —                                                                        |
| Pembelian persediaan kredit/bulan |                        55.000.000 | + PPN Masukan 11% = 6.050.000 → total Utang Dagang 61.050.000            |
| Penyusutan Peralatan Toko/bulan   |                         1.250.000 | Mulai Februari (aset dibeli Januari, umur 48 bulan)                      |
| Cicilan pinjaman bank/bulan       | pokok 4.000.000 + bunga 1.000.000 | Mulai Februari (pinjaman dicairkan Januari)                              |


## Januari 2025 (2025-01)

| Tanggal    | Transaksi                                                      | Baris Jurnal                                                                                                                                                                                                    | Total       |
| ---------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| 2025-01-02 | Setoran modal awal pemilik                                     | Bank BCA (1102) Debit 300,000,000; Modal Pemilik (3101) Credit 300,000,000                                                                                                                                      | 300,000,000 |
| 2025-01-02 | Isi kas kecil awal dari Bank BCA                               | Kas Kecil (1101) Debit 10,000,000; Bank BCA (1102) Credit 10,000,000                                                                                                                                            | 10,000,000  |
| 2025-01-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-01 | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000  |
| 2025-01-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-01          | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000  |
| 2025-01-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-01                | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000  |
| 2025-01-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-01          | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000  |
| 2025-01-10 | Pembelian persediaan kredit 2025-01                            | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000  |
| 2025-01-20 | Pembelian Peralatan Toko (aset tetap)                          | Peralatan Toko (1201) Debit 60,000,000; PPN Masukan (1105) Debit 6,600,000; Bank BCA (1102) Credit 66,600,000                                                                                                   | 66,600,000  |
| 2025-01-25 | Pencairan pinjaman bank modal kerja                            | Bank BCA (1102) Debit 100,000,000; Pinjaman Bank Jangka Pendek (2105) Credit 100,000,000                                                                                                                        | 100,000,000 |

## Februari 2025 (2025-02)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-02-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-02   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-02-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-02            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-02-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-02                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-02-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-02            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-02-10 | Pembelian persediaan kredit 2025-02                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-02-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-02 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-02-27 | Penyusutan bulanan Peralatan Toko 2025-02                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-02-26 | Cicilan pinjaman bank (pokok+bunga) 2025-02                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |

## Maret 2025 (2025-03)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-03-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-03   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-03-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-03            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-03-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-03                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-03-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-03            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-03-10 | Pembelian persediaan kredit 2025-03                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-03-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-03 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-03-27 | Penyusutan bulanan Peralatan Toko 2025-03                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-03-26 | Cicilan pinjaman bank (pokok+bunga) 2025-03                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2025-03-30 | Setor PPh 21 karyawan ke kas negara (akumulasi kuartal) 2025-03  | Utang PPh 21 Karyawan (2103) Debit 1,125,000; Bank BCA (1102) Credit 1,125,000                                                                                                                                  | 1,125,000  |

> **Checkpoint Q1 2025 (s/d 31 Maret 2025, 26 jurnal kumulatif sejak awal)** — bandingkan dengan Trial Balance kamu di UI setelah posting semua jurnal Januari-Maret:
>
> | Akun | Saldo | Akun | Saldo |
> | ---- | ----: | ---- | ----: |
> | 1101 Kas Kecil | 10.000.000 | 2101 Utang Dagang | 61.050.000 |
> | 1102 Bank BCA | 382.700.000 | 2102 PPN Keluaran | 26.400.000 |
> | 1103 Piutang Dagang | 0 | 2103 Utang PPh 21 | 0 |
> | 1104 Persediaan | 15.000.000 | 2105 Pinjaman Bank | 92.000.000 |
> | 1105 PPN Masukan | 24.750.000 | 3101 Modal Pemilik | 300.000.000 |
> | 1201 Peralatan Toko | 60.000.000 | | |
> | 1202 Akum. Penyusutan | (2.500.000) | | |
>
> Total Debit = Total Kredit = **1.553.275.000**. Total Pendapatan kumulatif 240.000.000, Total Beban kumulatif 229.500.000 → **Laba Berjalan 10.500.000**.

## April 2025 (2025-04)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-04-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-04   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-04-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-04            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-04-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-04                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-04-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-04            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-04-10 | Pembelian persediaan kredit 2025-04                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-04-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-04 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-04-27 | Penyusutan bulanan Peralatan Toko 2025-04                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-04-26 | Cicilan pinjaman bank (pokok+bunga) 2025-04                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |

## Mei 2025 (2025-05)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-05-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-05   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-05-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-05            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-05-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-05                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-05-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-05            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-05-10 | Pembelian persediaan kredit 2025-05                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-05-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-05 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-05-27 | Penyusutan bulanan Peralatan Toko 2025-05                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-05-26 | Cicilan pinjaman bank (pokok+bunga) 2025-05                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |

## Juni 2025 (2025-06)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-06-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-06   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-06-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-06            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-06-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-06                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-06-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-06            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-06-10 | Pembelian persediaan kredit 2025-06                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-06-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-06 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-06-27 | Penyusutan bulanan Peralatan Toko 2025-06                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-06-26 | Cicilan pinjaman bank (pokok+bunga) 2025-06                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2025-06-30 | Setor PPh 21 karyawan ke kas negara (akumulasi kuartal) 2025-06  | Utang PPh 21 Karyawan (2103) Debit 1,125,000; Bank BCA (1102) Credit 1,125,000                                                                                                                                  | 1,125,000  |

> **Checkpoint Q2 2025 (s/d 30 Juni 2025, 51 jurnal kumulatif)**:
>
> | Akun | Saldo | Akun | Saldo |
> | ---- | ----: | ---- | ----: |
> | 1101 Kas Kecil | 10.000.000 | 2101 Utang Dagang | 61.050.000 |
> | 1102 Bank BCA | 375.950.000 | 2102 PPN Keluaran | 52.800.000 |
> | 1103 Piutang Dagang | 0 | 2103 Utang PPh 21 | 0 |
> | 1104 Persediaan | 30.000.000 | 2105 Pinjaman Bank | 80.000.000 |
> | 1105 PPN Masukan | 42.900.000 | 3101 Modal Pemilik | 300.000.000 |
> | 1201 Peralatan Toko | 60.000.000 | | |
> | 1202 Akum. Penyusutan | (6.250.000) | | |
>
> Total Debit = Total Kredit = **2.697.250.000**. Total Pendapatan kumulatif 480.000.000, Total Beban kumulatif 461.250.000 → **Laba Berjalan 18.750.000**. Catatan: PPh 21 Q2 (Apr-Jun = 1.125.000) sudah disetor via jurnal 30 Juni, makanya saldo 2103 kembali 0.

## Juli 2025 (2025-07)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-07-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-07   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-07-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-07            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-07-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-07                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-07-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-07            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-07-10 | Pembelian persediaan kredit 2025-07                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-07-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-07 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-07-27 | Penyusutan bulanan Peralatan Toko 2025-07                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-07-26 | Cicilan pinjaman bank (pokok+bunga) 2025-07                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2025-07-18 | Prive - pengambilan pribadi pemilik                              | Modal Pemilik (3101) Debit 10,000,000; Bank BCA (1102) Credit 10,000,000                                                                                                                                        | 10,000,000 |

## Agustus 2025 (2025-08)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-08-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-08   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-08-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-08            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-08-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-08                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-08-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-08            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-08-10 | Pembelian persediaan kredit 2025-08                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-08-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-08 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-08-27 | Penyusutan bulanan Peralatan Toko 2025-08                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-08-26 | Cicilan pinjaman bank (pokok+bunga) 2025-08                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |

## September 2025 (2025-09)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-09-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-09   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-09-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-09            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-09-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-09                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-09-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-09            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-09-10 | Pembelian persediaan kredit 2025-09                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-09-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-09 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-09-27 | Penyusutan bulanan Peralatan Toko 2025-09                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-09-26 | Cicilan pinjaman bank (pokok+bunga) 2025-09                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2025-09-30 | Setor PPh 21 karyawan ke kas negara (akumulasi kuartal) 2025-09  | Utang PPh 21 Karyawan (2103) Debit 1,125,000; Bank BCA (1102) Credit 1,125,000                                                                                                                                  | 1,125,000  |

> **Checkpoint Q3 2025 (s/d 30 September 2025, 77 jurnal kumulatif)**:
>
> | Akun | Saldo | Akun | Saldo |
> | ---- | ----: | ---- | ----: |
> | 1101 Kas Kecil | 10.000.000 | 2101 Utang Dagang | 61.050.000 |
> | 1102 Bank BCA | 359.200.000 | 2102 PPN Keluaran | 79.200.000 |
> | 1103 Piutang Dagang | 0 | 2103 Utang PPh 21 | 0 |
> | 1104 Persediaan | 45.000.000 | 2105 Pinjaman Bank | 68.000.000 |
> | 1105 PPN Masukan | 61.050.000 | 3101 Modal Pemilik | 290.000.000 |
> | 1201 Peralatan Toko | 60.000.000 | | |
> | 1202 Akum. Penyusutan | (10.000.000) | | |
>
> Total Debit = Total Kredit = **3.851.225.000**. Total Pendapatan kumulatif 720.000.000, Total Beban kumulatif 693.000.000 → **Laba Berjalan 27.000.000**. Modal Pemilik turun jadi 290.000.000 karena Prive Juli (10.000.000) — verifikasi ini di file 05.

## Oktober 2025 (2025-10)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-10-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-10   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-10-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-10            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-10-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-10                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-10-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-10            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-10-10 | Pembelian persediaan kredit 2025-10                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-10-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-10 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-10-27 | Penyusutan bulanan Peralatan Toko 2025-10                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-10-26 | Cicilan pinjaman bank (pokok+bunga) 2025-10                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2025-10-31 | Selisih kas opname kasir (kurang)                                | Beban Selisih Kas (5205) Debit 200,000; Kas Kecil (1101) Credit 200,000                                                                                                                                         | 200,000    |

## November 2025 (2025-11)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-11-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-11   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-11-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-11            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-11-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-11                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-11-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-11            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-11-10 | Pembelian persediaan kredit 2025-11                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-11-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-11 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-11-27 | Penyusutan bulanan Peralatan Toko 2025-11                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-11-26 | Cicilan pinjaman bank (pokok+bunga) 2025-11                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |

## Desember 2025 (2025-12)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2025-12-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2025-12   | Kas Kecil (1101) Debit 88,800,000; Penjualan Barang Dagang (4101) Credit 50,000,000; Penjualan Barang Dagang (4101) Credit 30,000,000; PPN Keluaran (2102) Credit 8,800,000                                     | 88,800,000 |
| 2025-12-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2025-12            | Bank BCA (1102) Debit 88,800,000; Kas Kecil (1101) Credit 88,800,000                                                                                                                                            | 88,800,000 |
| 2025-12-06 | Pengakuan Harga Pokok Penjualan bulanan 2025-12                  | Harga Pokok Penjualan (5101) Debit 50,000,000; Persediaan Barang Dagang (1104) Credit 50,000,000                                                                                                                | 50,000,000 |
| 2025-12-28 | Beban operasional bulanan (sewa+gaji+listrik) 2025-12            | Beban Sewa Toko (5201) Debit 8,000,000; Beban Gaji Karyawan (5202) Debit 15,000,000; Beban Listrik & Air (5203) Debit 2,000,000; Bank BCA (1102) Credit 24,625,000; Utang PPh 21 Karyawan (2103) Credit 375,000 | 25,000,000 |
| 2025-12-10 | Pembelian persediaan kredit 2025-12                              | Persediaan Barang Dagang (1104) Debit 55,000,000; PPN Masukan (1105) Debit 6,050,000; Utang Dagang (2101) Credit 61,050,000                                                                                     | 61,050,000 |
| 2025-12-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2025-12 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2025-12-27 | Penyusutan bulanan Peralatan Toko 2025-12                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2025-12-26 | Cicilan pinjaman bank (pokok+bunga) 2025-12                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2025-12-30 | Setor PPh 21 karyawan ke kas negara (akumulasi kuartal) 2025-12  | Utang PPh 21 Karyawan (2103) Debit 1,125,000; Bank BCA (1102) Credit 1,125,000                                                                                                                                  | 1,125,000  |
| 2025-12-20 | Beban iklan & promosi akhir tahun                                | Beban Iklan & Promosi (5208) Debit 8,000,000; Bank BCA (1102) Credit 8,000,000                                                                                                                                  | 8,000,000  |

> **Checkpoint FY2025 PENUH (s/d 31 Desember 2025, 104 jurnal kumulatif sejak 2 Januari 2025)** — angka acuan utama untuk file `03-general-ledger-trial-balance.id.md` dan Close Fiscal Year di file `04-tutup-periode-dan-tahun-fiskal.id.md`:
>
> | Akun | Saldo | Akun | Saldo |
> | ---- | ----: | ---- | ----: |
> | 1101 Kas Kecil | 9.800.000 | 2101 Utang Dagang | 61.050.000 |
> | 1102 Bank BCA | 344.450.000 | 2102 PPN Keluaran | 105.600.000 |
> | 1103 Piutang Dagang | 0 | 2103 Utang PPh 21 | 0 |
> | 1104 Persediaan | 60.000.000 | 2105 Pinjaman Bank | 56.000.000 |
> | 1105 PPN Masukan | 79.200.000 | 3101 Modal Pemilik | 290.000.000 |
> | 1201 Peralatan Toko | 60.000.000 | 3102 Laba Ditahan | 0 (belum ada closing entry) |
> | 1202 Akum. Penyusutan | (13.750.000) | | |
>
> Total Debit = Total Kredit = **5.003.400.000** (balanced). **Total Pendapatan FY2025 = 960.000.000, Total Beban FY2025 = 932.950.000 → Laba Bersih FY2025 = 27.050.000.** Angka Laba Bersih ini WAJIB persis sama dengan closing entry yang dites di file 04 (masuk ke Laba Ditahan).

## Ringkasan Jumlah Transaksi per Bulan

| Bulan            | Jumlah Jurnal | Catatan                                                                                                                                                                |
| ---------------- | ------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Januari 2025     |             9 | Termasuk 2 jurnal modal awal (di file 00) + pembelian aset tetap + pencairan pinjaman (bulan kickoff, belum ada pembayaran utang/penyusutan/cicilan karena baru mulai) |
| Februari 2025    |             8 | Mulai steady-state: fundamental (2) + setor kas + HPP + pembelian + **pembayaran utang bulan lalu** + **penyusutan pertama** + **cicilan pinjaman pertama**            |
| Maret 2025       |             9 | Steady-state (8) + setor PPh 21 kuartalan                                                                                                                              |
| April 2025       |             8 | Steady-state                                                                                                                                                           |
| Mei 2025         |             8 | Steady-state                                                                                                                                                           |
| Juni 2025        |             9 | Steady-state + setor PPh 21 kuartalan                                                                                                                                  |
| Juli 2025        |             9 | Steady-state + Prive pemilik                                                                                                                                           |
| Agustus 2025     |             8 | Steady-state                                                                                                                                                           |
| September 2025   |             9 | Steady-state + setor PPh 21 kuartalan                                                                                                                                  |
| Oktober 2025     |             9 | Steady-state + Selisih kas opname kasir                                                                                                                                |
| November 2025    |             8 | Steady-state                                                                                                                                                           |
| Desember 2025    |            10 | Steady-state + setor PPh 21 kuartalan + Beban iklan & promosi akhir tahun                                                                                              |
| **Total FY2025** |       **104** | **Semua bulan ≥ 5 transaksi (2 fundamental + minimal 3 tambahan) — syarat minimum terpenuhi di seluruh 12 bulan**                                                      |

## Referensi Silang

- [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) — master data & modal awal
- [`02-jurnal-transaksi-2026.id.md`](./02-jurnal-transaksi-2026.id.md) — lanjutan Januari-Agustus 2026
- [`03-general-ledger-trial-balance.id.md`](./03-general-ledger-trial-balance.id.md) — verifikasi Trial Balance & Detail Ledger dengan angka checkpoint di atas
- [`04-tutup-periode-dan-tahun-fiskal.id.md`](./04-tutup-periode-dan-tahun-fiskal.id.md) — Close Fiscal Year FY2025 (closing entry Laba Bersih 27.050.000 ke Laba Ditahan)
