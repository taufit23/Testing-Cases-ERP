---
title: — 02. Jurnal Transaksi Tahun 2026 (Januari-Agustus, Berjalan)
category: Accounting 2
description: 72 jurnal manual Januari-Agustus 2026 (bulan berjalan/current) untuk PT Retail Nusantara Jaya, lanjutan langsung dari FY2025 — omzet & beban naik 10% dari FY2025 (kenaikan tahunan), plus variasi transaksi baru (penjualan kredit & pelunasan piutang, retur pembelian, beban administrasi bank).
visibility: internal
---

# 02. Jurnal Transaksi Tahun 2026 (Januari-Agustus, Berjalan)

> Prasyarat: [`01-jurnal-transaksi-2025.id.md`](./01-jurnal-transaksi-2025.id.md) sudah selesai — file ini melanjutkan LANGSUNG dari saldo akhir Desember 2025 (lihat checkpoint FY2025 di file itu). Fiscal Year FY2026 (12 periode) harus sudah digenerate di file 00 §12, walau baru dipakai sampai Agustus.

## Perubahan Angka FY2026 vs FY2025 (+10%)

**Sebab-akibat:** kenaikan 10% ini mensimulasikan bisnis retail yang tumbuh tahun kedua — omzet, HPP, dan beban operasional utama naik proporsional, TAPI beban penyusutan (aset sama, umur sama) dan cicilan pinjaman (jadwal tetap) TIDAK ikut naik karena keduanya independen dari omzet.

| Komponen                          |                FY2025 |                FY2026 | Kenaikan                     |
| --------------------------------- | --------------------: | --------------------: | ---------------------------- |
| Penjualan Toko Pusat/bulan        |            50.000.000 |            55.000.000 | +10%                         |
| Penjualan Toko Cabang/bulan       |            30.000.000 |            33.000.000 | +10%                         |
| HPP/bulan                         |            50.000.000 |            55.000.000 | +10%                         |
| Beban Sewa Toko/bulan             |             8.000.000 |             8.800.000 | +10%                         |
| Beban Gaji Karyawan (gross)/bulan |            15.000.000 |            16.500.000 | +10%                         |
| Beban Listrik & Air/bulan         |             2.000.000 |             2.200.000 | +10%                         |
| Pembelian persediaan kredit/bulan |            55.000.000 |            60.000.000 | +9% (dibulatkan)             |
| Penyusutan Peralatan Toko/bulan   |             1.250.000 |             1.250.000 | Tetap (aset sama)            |
| Cicilan pinjaman bank/bulan       | pokok 4jt + bunga 1jt | pokok 4jt + bunga 1jt | Tetap (jadwal cicilan tetap) |

**Catatan siklus utang dagang di batas tahun**: pembayaran utang Januari 2026 (`61.050.000`) masih melunasi pembelian **Desember 2025** (rate FY2025 lama) — baru mulai Februari 2026 siklus pembayaran memakai rate FY2026 baru (`66.600.000`). Ini bukti Detail Ledger `2101 Utang Dagang` tetap konsisten dilacak lintas tahun fiskal, bukan direset ke 0 pas ganti tahun.


## Januari 2026 (2026-01)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2026-01-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2026-01   | Kas Kecil (1101) Debit 97,680,000; Penjualan Barang Dagang (4101) Credit 55,000,000; Penjualan Barang Dagang (4101) Credit 33,000,000; PPN Keluaran (2102) Credit 9,680,000                                     | 97,680,000 |
| 2026-01-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2026-01            | Bank BCA (1102) Debit 97,680,000; Kas Kecil (1101) Credit 97,680,000                                                                                                                                            | 97,680,000 |
| 2026-01-06 | Pengakuan Harga Pokok Penjualan bulanan 2026-01                  | Harga Pokok Penjualan (5101) Debit 55,000,000; Persediaan Barang Dagang (1104) Credit 55,000,000                                                                                                                | 55,000,000 |
| 2026-01-28 | Beban operasional bulanan (sewa+gaji+listrik) 2026-01            | Beban Sewa Toko (5201) Debit 8,800,000; Beban Gaji Karyawan (5202) Debit 16,500,000; Beban Listrik & Air (5203) Debit 2,200,000; Bank BCA (1102) Credit 27,087,500; Utang PPh 21 Karyawan (2103) Credit 412,500 | 27,500,000 |
| 2026-01-10 | Pembelian persediaan kredit 2026-01                              | Persediaan Barang Dagang (1104) Debit 60,000,000; PPN Masukan (1105) Debit 6,600,000; Utang Dagang (2101) Credit 66,600,000                                                                                     | 66,600,000 |
| 2026-01-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2026-01 | Utang Dagang (2101) Debit 61,050,000; Bank BCA (1102) Credit 61,050,000                                                                                                                                         | 61,050,000 |
| 2026-01-27 | Penyusutan bulanan Peralatan Toko 2026-01                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2026-01-26 | Cicilan pinjaman bank (pokok+bunga) 2026-01                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2026-01-22 | Penjualan kredit customer korporat                               | Piutang Dagang (1103) Debit 22,200,000; Penjualan Barang Dagang (4101) Credit 20,000,000; PPN Keluaran (2102) Credit 2,200,000                                                                                  | 22,200,000 |

## Februari 2026 (2026-02)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2026-02-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2026-02   | Kas Kecil (1101) Debit 97,680,000; Penjualan Barang Dagang (4101) Credit 55,000,000; Penjualan Barang Dagang (4101) Credit 33,000,000; PPN Keluaran (2102) Credit 9,680,000                                     | 97,680,000 |
| 2026-02-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2026-02            | Bank BCA (1102) Debit 97,680,000; Kas Kecil (1101) Credit 97,680,000                                                                                                                                            | 97,680,000 |
| 2026-02-06 | Pengakuan Harga Pokok Penjualan bulanan 2026-02                  | Harga Pokok Penjualan (5101) Debit 55,000,000; Persediaan Barang Dagang (1104) Credit 55,000,000                                                                                                                | 55,000,000 |
| 2026-02-28 | Beban operasional bulanan (sewa+gaji+listrik) 2026-02            | Beban Sewa Toko (5201) Debit 8,800,000; Beban Gaji Karyawan (5202) Debit 16,500,000; Beban Listrik & Air (5203) Debit 2,200,000; Bank BCA (1102) Credit 27,087,500; Utang PPh 21 Karyawan (2103) Credit 412,500 | 27,500,000 |
| 2026-02-10 | Pembelian persediaan kredit 2026-02                              | Persediaan Barang Dagang (1104) Debit 60,000,000; PPN Masukan (1105) Debit 6,600,000; Utang Dagang (2101) Credit 66,600,000                                                                                     | 66,600,000 |
| 2026-02-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2026-02 | Utang Dagang (2101) Debit 66,600,000; Bank BCA (1102) Credit 66,600,000                                                                                                                                         | 66,600,000 |
| 2026-02-27 | Penyusutan bulanan Peralatan Toko 2026-02                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2026-02-26 | Cicilan pinjaman bank (pokok+bunga) 2026-02                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2026-02-20 | Penerimaan piutang (pelunasan Jan 2026)                          | Bank BCA (1102) Debit 22,200,000; Piutang Dagang (1103) Credit 22,200,000                                                                                                                                       | 22,200,000 |

## Maret 2026 (2026-03)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2026-03-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2026-03   | Kas Kecil (1101) Debit 97,680,000; Penjualan Barang Dagang (4101) Credit 55,000,000; Penjualan Barang Dagang (4101) Credit 33,000,000; PPN Keluaran (2102) Credit 9,680,000                                     | 97,680,000 |
| 2026-03-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2026-03            | Bank BCA (1102) Debit 97,680,000; Kas Kecil (1101) Credit 97,680,000                                                                                                                                            | 97,680,000 |
| 2026-03-06 | Pengakuan Harga Pokok Penjualan bulanan 2026-03                  | Harga Pokok Penjualan (5101) Debit 55,000,000; Persediaan Barang Dagang (1104) Credit 55,000,000                                                                                                                | 55,000,000 |
| 2026-03-28 | Beban operasional bulanan (sewa+gaji+listrik) 2026-03            | Beban Sewa Toko (5201) Debit 8,800,000; Beban Gaji Karyawan (5202) Debit 16,500,000; Beban Listrik & Air (5203) Debit 2,200,000; Bank BCA (1102) Credit 27,087,500; Utang PPh 21 Karyawan (2103) Credit 412,500 | 27,500,000 |
| 2026-03-10 | Pembelian persediaan kredit 2026-03                              | Persediaan Barang Dagang (1104) Debit 60,000,000; PPN Masukan (1105) Debit 6,600,000; Utang Dagang (2101) Credit 66,600,000                                                                                     | 66,600,000 |
| 2026-03-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2026-03 | Utang Dagang (2101) Debit 66,600,000; Bank BCA (1102) Credit 66,600,000                                                                                                                                         | 66,600,000 |
| 2026-03-27 | Penyusutan bulanan Peralatan Toko 2026-03                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2026-03-26 | Cicilan pinjaman bank (pokok+bunga) 2026-03                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2026-03-30 | Setor PPh 21 karyawan ke kas negara (akumulasi kuartal) 2026-03  | Utang PPh 21 Karyawan (2103) Debit 1,237,500; Bank BCA (1102) Credit 1,237,500                                                                                                                                  | 1,237,500  |

> **Checkpoint Q1 2026 (s/d 31 Maret 2026, 131 jurnal kumulatif sejak 2 Januari 2025)**:
>
> | Akun | Saldo | Akun | Saldo |
> | ---- | ----: | ---- | ----: |
> | 1101 Kas Kecil | 9.800.000 | 2101 Utang Dagang | 66.600.000 |
> | 1102 Bank BCA | 367.940.000 | 2102 PPN Keluaran | 136.840.000 |
> | 1103 Piutang Dagang | 0 | 2103 Utang PPh 21 | 0 |
> | 1104 Persediaan | 75.000.000 | 2105 Pinjaman Bank | 44.000.000 |
> | 1105 PPN Masukan | 99.000.000 | 3101 Modal Pemilik | 290.000.000 |
> | 1201 Peralatan Toko | 60.000.000 | | |
> | 1202 Akum. Penyusutan | (17.500.000) | | |
>
> Total Debit = Total Kredit = **6.295.417.500**. Total Pendapatan kumulatif (sejak Jan 2025) 1.244.000.000, Total Beban kumulatif 1.187.200.000 → **Laba Berjalan kumulatif 56.800.000** (ini laba KUMULATIF 15 bulan, BUKAN laba FY2026 saja — laba FY2026 murni ada di file 05).

## April 2026 (2026-04)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2026-04-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2026-04   | Kas Kecil (1101) Debit 97,680,000; Penjualan Barang Dagang (4101) Credit 55,000,000; Penjualan Barang Dagang (4101) Credit 33,000,000; PPN Keluaran (2102) Credit 9,680,000                                     | 97,680,000 |
| 2026-04-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2026-04            | Bank BCA (1102) Debit 97,680,000; Kas Kecil (1101) Credit 97,680,000                                                                                                                                            | 97,680,000 |
| 2026-04-06 | Pengakuan Harga Pokok Penjualan bulanan 2026-04                  | Harga Pokok Penjualan (5101) Debit 55,000,000; Persediaan Barang Dagang (1104) Credit 55,000,000                                                                                                                | 55,000,000 |
| 2026-04-28 | Beban operasional bulanan (sewa+gaji+listrik) 2026-04            | Beban Sewa Toko (5201) Debit 8,800,000; Beban Gaji Karyawan (5202) Debit 16,500,000; Beban Listrik & Air (5203) Debit 2,200,000; Bank BCA (1102) Credit 27,087,500; Utang PPh 21 Karyawan (2103) Credit 412,500 | 27,500,000 |
| 2026-04-10 | Pembelian persediaan kredit 2026-04                              | Persediaan Barang Dagang (1104) Debit 60,000,000; PPN Masukan (1105) Debit 6,600,000; Utang Dagang (2101) Credit 66,600,000                                                                                     | 66,600,000 |
| 2026-04-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2026-04 | Utang Dagang (2101) Debit 66,600,000; Bank BCA (1102) Credit 66,600,000                                                                                                                                         | 66,600,000 |
| 2026-04-27 | Penyusutan bulanan Peralatan Toko 2026-04                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2026-04-26 | Cicilan pinjaman bank (pokok+bunga) 2026-04                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2026-04-12 | Retur pembelian ke supplier                                      | Utang Dagang (2101) Debit 11,100,000; Persediaan Barang Dagang (1104) Credit 10,000,000; PPN Masukan (1105) Credit 1,100,000                                                                                    | 11,100,000 |

## Mei 2026 (2026-05)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2026-05-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2026-05   | Kas Kecil (1101) Debit 97,680,000; Penjualan Barang Dagang (4101) Credit 55,000,000; Penjualan Barang Dagang (4101) Credit 33,000,000; PPN Keluaran (2102) Credit 9,680,000                                     | 97,680,000 |
| 2026-05-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2026-05            | Bank BCA (1102) Debit 97,680,000; Kas Kecil (1101) Credit 97,680,000                                                                                                                                            | 97,680,000 |
| 2026-05-06 | Pengakuan Harga Pokok Penjualan bulanan 2026-05                  | Harga Pokok Penjualan (5101) Debit 55,000,000; Persediaan Barang Dagang (1104) Credit 55,000,000                                                                                                                | 55,000,000 |
| 2026-05-28 | Beban operasional bulanan (sewa+gaji+listrik) 2026-05            | Beban Sewa Toko (5201) Debit 8,800,000; Beban Gaji Karyawan (5202) Debit 16,500,000; Beban Listrik & Air (5203) Debit 2,200,000; Bank BCA (1102) Credit 27,087,500; Utang PPh 21 Karyawan (2103) Credit 412,500 | 27,500,000 |
| 2026-05-10 | Pembelian persediaan kredit 2026-05                              | Persediaan Barang Dagang (1104) Debit 60,000,000; PPN Masukan (1105) Debit 6,600,000; Utang Dagang (2101) Credit 66,600,000                                                                                     | 66,600,000 |
| 2026-05-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2026-05 | Utang Dagang (2101) Debit 66,600,000; Bank BCA (1102) Credit 66,600,000                                                                                                                                         | 66,600,000 |
| 2026-05-27 | Penyusutan bulanan Peralatan Toko 2026-05                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2026-05-26 | Cicilan pinjaman bank (pokok+bunga) 2026-05                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2026-05-05 | Beban administrasi bank                                          | Beban Administrasi Bank (5209) Debit 300,000; Bank BCA (1102) Credit 300,000                                                                                                                                    | 300,000    |

## Juni 2026 (2026-06)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2026-06-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2026-06   | Kas Kecil (1101) Debit 97,680,000; Penjualan Barang Dagang (4101) Credit 55,000,000; Penjualan Barang Dagang (4101) Credit 33,000,000; PPN Keluaran (2102) Credit 9,680,000                                     | 97,680,000 |
| 2026-06-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2026-06            | Bank BCA (1102) Debit 97,680,000; Kas Kecil (1101) Credit 97,680,000                                                                                                                                            | 97,680,000 |
| 2026-06-06 | Pengakuan Harga Pokok Penjualan bulanan 2026-06                  | Harga Pokok Penjualan (5101) Debit 55,000,000; Persediaan Barang Dagang (1104) Credit 55,000,000                                                                                                                | 55,000,000 |
| 2026-06-28 | Beban operasional bulanan (sewa+gaji+listrik) 2026-06            | Beban Sewa Toko (5201) Debit 8,800,000; Beban Gaji Karyawan (5202) Debit 16,500,000; Beban Listrik & Air (5203) Debit 2,200,000; Bank BCA (1102) Credit 27,087,500; Utang PPh 21 Karyawan (2103) Credit 412,500 | 27,500,000 |
| 2026-06-10 | Pembelian persediaan kredit 2026-06                              | Persediaan Barang Dagang (1104) Debit 60,000,000; PPN Masukan (1105) Debit 6,600,000; Utang Dagang (2101) Credit 66,600,000                                                                                     | 66,600,000 |
| 2026-06-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2026-06 | Utang Dagang (2101) Debit 66,600,000; Bank BCA (1102) Credit 66,600,000                                                                                                                                         | 66,600,000 |
| 2026-06-27 | Penyusutan bulanan Peralatan Toko 2026-06                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2026-06-26 | Cicilan pinjaman bank (pokok+bunga) 2026-06                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2026-06-30 | Setor PPh 21 karyawan ke kas negara (akumulasi kuartal) 2026-06  | Utang PPh 21 Karyawan (2103) Debit 1,237,500; Bank BCA (1102) Credit 1,237,500                                                                                                                                  | 1,237,500  |

> **Checkpoint Q2 2026 (s/d 30 Juni 2026, 158 jurnal kumulatif)**:
>
> | Akun | Saldo | Akun | Saldo |
> | ---- | ----: | ---- | ----: |
> | 1101 Kas Kecil | 9.800.000 | 2101 Utang Dagang | 55.500.000 |
> | 1102 Bank BCA | 363.380.000 | 2102 PPN Keluaran | 165.880.000 |
> | 1103 Piutang Dagang | 0 | 2103 Utang PPh 21 | 0 |
> | 1104 Persediaan | 80.000.000 | 2105 Pinjaman Bank | 32.000.000 |
> | 1105 PPN Masukan | 117.700.000 | 3101 Modal Pemilik | 290.000.000 |
> | 1201 Peralatan Toko | 60.000.000 | | |
> | 1202 Akum. Penyusutan | (21.250.000) | | |
>
> Total Debit = Total Kredit = **7.559.985.000**. Total Pendapatan kumulatif 1.508.000.000, Total Beban kumulatif 1.441.750.000 → **Laba Berjalan kumulatif 66.250.000**. Saldo Utang Dagang turun jadi 55.500.000 karena efek Retur Pembelian April (11.100.000) — bukti retur mempengaruhi saldo real, bukan sekadar dicatat lalu diabaikan.

## Juli 2026 (2026-07)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2026-07-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2026-07   | Kas Kecil (1101) Debit 97,680,000; Penjualan Barang Dagang (4101) Credit 55,000,000; Penjualan Barang Dagang (4101) Credit 33,000,000; PPN Keluaran (2102) Credit 9,680,000                                     | 97,680,000 |
| 2026-07-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2026-07            | Bank BCA (1102) Debit 97,680,000; Kas Kecil (1101) Credit 97,680,000                                                                                                                                            | 97,680,000 |
| 2026-07-06 | Pengakuan Harga Pokok Penjualan bulanan 2026-07                  | Harga Pokok Penjualan (5101) Debit 55,000,000; Persediaan Barang Dagang (1104) Credit 55,000,000                                                                                                                | 55,000,000 |
| 2026-07-28 | Beban operasional bulanan (sewa+gaji+listrik) 2026-07            | Beban Sewa Toko (5201) Debit 8,800,000; Beban Gaji Karyawan (5202) Debit 16,500,000; Beban Listrik & Air (5203) Debit 2,200,000; Bank BCA (1102) Credit 27,087,500; Utang PPh 21 Karyawan (2103) Credit 412,500 | 27,500,000 |
| 2026-07-10 | Pembelian persediaan kredit 2026-07                              | Persediaan Barang Dagang (1104) Debit 60,000,000; PPN Masukan (1105) Debit 6,600,000; Utang Dagang (2101) Credit 66,600,000                                                                                     | 66,600,000 |
| 2026-07-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2026-07 | Utang Dagang (2101) Debit 66,600,000; Bank BCA (1102) Credit 66,600,000                                                                                                                                         | 66,600,000 |
| 2026-07-27 | Penyusutan bulanan Peralatan Toko 2026-07                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2026-07-26 | Cicilan pinjaman bank (pokok+bunga) 2026-07                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2026-07-15 | Beban iklan & promosi                                            | Beban Iklan & Promosi (5208) Debit 6,000,000; Bank BCA (1102) Credit 6,000,000                                                                                                                                  | 6,000,000  |

## Agustus 2026 (bulan berjalan/current) (2026-08)

| Tanggal    | Transaksi                                                        | Baris Jurnal                                                                                                                                                                                                    | Total      |
| ---------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 2026-08-05 | Rekap penjualan tunai bulanan Toko Pusat & Toko Cabang 2026-08   | Kas Kecil (1101) Debit 97,680,000; Penjualan Barang Dagang (4101) Credit 55,000,000; Penjualan Barang Dagang (4101) Credit 33,000,000; PPN Keluaran (2102) Credit 9,680,000                                     | 97,680,000 |
| 2026-08-06 | Setor kas hasil penjualan bulanan ke Bank BCA 2026-08            | Bank BCA (1102) Debit 97,680,000; Kas Kecil (1101) Credit 97,680,000                                                                                                                                            | 97,680,000 |
| 2026-08-06 | Pengakuan Harga Pokok Penjualan bulanan 2026-08                  | Harga Pokok Penjualan (5101) Debit 55,000,000; Persediaan Barang Dagang (1104) Credit 55,000,000                                                                                                                | 55,000,000 |
| 2026-08-28 | Beban operasional bulanan (sewa+gaji+listrik) 2026-08            | Beban Sewa Toko (5201) Debit 8,800,000; Beban Gaji Karyawan (5202) Debit 16,500,000; Beban Listrik & Air (5203) Debit 2,200,000; Bank BCA (1102) Credit 27,087,500; Utang PPh 21 Karyawan (2103) Credit 412,500 | 27,500,000 |
| 2026-08-10 | Pembelian persediaan kredit 2026-08                              | Persediaan Barang Dagang (1104) Debit 60,000,000; PPN Masukan (1105) Debit 6,600,000; Utang Dagang (2101) Credit 66,600,000                                                                                     | 66,600,000 |
| 2026-08-15 | Pembayaran utang dagang (pelunasan pembelian bulan lalu) 2026-08 | Utang Dagang (2101) Debit 66,600,000; Bank BCA (1102) Credit 66,600,000                                                                                                                                         | 66,600,000 |
| 2026-08-27 | Penyusutan bulanan Peralatan Toko 2026-08                        | Beban Penyusutan Peralatan Toko (5204) Debit 1,250,000; Akumulasi Penyusutan Peralatan Toko (1202) Credit 1,250,000                                                                                             | 1,250,000  |
| 2026-08-26 | Cicilan pinjaman bank (pokok+bunga) 2026-08                      | Pinjaman Bank Jangka Pendek (2105) Debit 4,000,000; Beban Bunga Pinjaman (5210) Debit 1,000,000; Bank BCA (1102) Credit 5,000,000                                                                               | 5,000,000  |
| 2026-08-10 | Selisih kas opname kasir (kurang)                                | Beban Selisih Kas (5205) Debit 100,000; Kas Kecil (1101) Credit 100,000                                                                                                                                         | 100,000    |

> **Checkpoint FINAL — s/d 31 Agustus 2026, bulan berjalan (176 jurnal, TOTAL SELURUH SUITE)** — angka acuan utama file `03` dan `05`:
>
> | Akun | Saldo | Akun | Saldo |
> | ---- | ----: | ---- | ----: |
> | 1101 Kas Kecil | 9.700.000 | 2101 Utang Dagang | 55.500.000 |
> | 1102 Bank BCA | 355.365.000 | 2102 PPN Keluaran | 185.240.000 |
> | 1103 Piutang Dagang | 0 | 2103 Utang PPh 21 | 825.000 |
> | 1104 Persediaan | 90.000.000 | 2105 Pinjaman Bank | 24.000.000 |
> | 1105 PPN Masukan | 130.900.000 | 3101 Modal Pemilik | 290.000.000 |
> | 1201 Peralatan Toko | 60.000.000 | 3102 Laba Ditahan | 27.050.000 (setelah Close FY2025 di file 04) |
> | 1202 Akum. Penyusutan | (23.750.000) | | |
>
> Total Debit = Total Kredit = **8.400.705.000** (balanced). Total Pendapatan kumulatif sejak awal 1.684.000.000, Total Beban kumulatif 1.617.350.000 → **Laba Berjalan kumulatif 66.650.000** (= Laba Ditahan FY2025 27.050.000 + Laba Berjalan FY2026 Jan-Ags 39.600.000).

## Ringkasan Jumlah Transaksi per Bulan

| Bulan                         | Jumlah Jurnal | Catatan                                                    |
| ----------------------------- | ------------: | ---------------------------------------------------------- |
| Januari 2026                  |             9 | Steady-state (7) + Penjualan kredit customer korporat      |
| Februari 2026                 |             9 | Steady-state (7) + Penerimaan piutang (pelunasan Jan 2026) |
| Maret 2026                    |             9 | Steady-state (7) + setor PPh 21 kuartalan                  |
| April 2026                    |             9 | Steady-state (7) + Retur pembelian ke supplier             |
| Mei 2026                      |             9 | Steady-state (7) + Beban administrasi bank                 |
| Juni 2026                     |             9 | Steady-state (7) + setor PPh 21 kuartalan                  |
| Juli 2026                     |             9 | Steady-state (7) + Beban iklan & promosi                   |
| Agustus 2026 (bulan berjalan) |             9 | Steady-state (7) + Selisih kas opname kasir                |
| **Total FY2026 (Jan-Ags)**    |        **72** | Semua bulan ≥ 5 transaksi — syarat minimum tetap terpenuhi |

**Total keseluruhan suite (2025-01 s/d 2026-08): 176 jurnal, 20 bulan berturut-turut, semua balanced.**

## Referensi Silang

- [`01-jurnal-transaksi-2025.id.md`](./01-jurnal-transaksi-2025.id.md) — FY2025 penuh (checkpoint saldo akhir tahun)
- [`03-general-ledger-trial-balance.id.md`](./03-general-ledger-trial-balance.id.md) — Trial Balance final s/d Agustus 2026
- [`04-tutup-periode-dan-tahun-fiskal.id.md`](./04-tutup-periode-dan-tahun-fiskal.id.md) — Close FY2025 (dikerjakan setelah file ini, supaya FY2026 tetap terbuka untuk lanjut transaksi)
- [`05-laporan-keuangan.id.md`](./05-laporan-keuangan.id.md) — Neraca/Laba Rugi/Arus Kas FY2025 penuh vs FY2026 year-to-date Agustus
