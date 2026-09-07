---
title: (Klinik Umum Besar) — 02. General Ledger & Trial Balance per Cabang
category: accounting-klinik-umum
description: Trial Balance presisi per 2026-01-31, Detail Ledger, dan Summary by Account dengan filter dimensi 6 cabang — fokus verifikasi breakdown Pendapatan Kapitasi per cabang (satu-satunya lini yang didimensikan penuh di file 01).
visibility: internal
---

# 02. General Ledger & Trial Balance per Cabang

> Prasyarat: file [`01-jurnal-manual-kapitasi-mcu-dan-operasional.id.md`](./01-jurnal-manual-kapitasi-mcu-dan-operasional.id.md) sudah selesai (T1-T21 + T20 reverse/repost lengkap terposting). Seluruh angka di file ini adalah **akumulasi saldo awal (file 00) + seluruh transaksi Januari (file 01)**, per 2026-01-31.

## 1. Trial Balance (**General Ledger — `trial-balance`**)

| Skenario | Payload                                                                                                                                     | Hasil                                                                                                           |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/trial-balance {date_from:"2026-01-01", date_to:"2026-01-31"}` (atau `as_of_date`, sesuaikan kontrak aktual) | `total_debit = total_credit = **1.931.980.000**` — kalau beda, ada jurnal yang belum ke-posting atau salah arah |
| Negatif  | Filter tanggal SEBELUM saldo awal ada (mis. 2025-12-01)                                                                                     | Semua saldo 0 atau tidak ada baris — bukan error                                                                |

### 1.1 Rincian Trial Balance Lengkap (35 akun, per 2026-01-31)

| Kode | Akun                                                         |       Saldo Debit |      Saldo Kredit |
| ---- | ------------------------------------------------------------ | ----------------: | ----------------: |
| 1101 | Kas Kecil Klinik Pusat                                       |        14.650.000 |                   |
| 1102 | Bank Mandiri Operasional                                     |       479.030.000 |                   |
| 1103 | Bank BCA Penampungan Kapitasi BPJS                           |       157.000.000 |                   |
| 1104 | Piutang Kapitasi BPJS Kesehatan (FKTP)                       |       244.000.000 |                   |
| 1105 | Piutang MCU Korporat & Asuransi Swasta                       |       164.500.000 |                   |
| 1106 | Persediaan Obat (Generik & Paten)                            |       195.000.000 |                   |
| 1107 | Persediaan BHP Medis & Lab                                   |        80.250.000 |                   |
| 1108 | PPN Masukan                                                  |         4.400.000 |                   |
| 1201 | Peralatan Medis & Lab                                        |                 0 |                   |
| 1202 | Akumulasi Penyusutan Peralatan Medis & Lab                   |                   |                 0 |
| 1203 | Kendaraan Ambulans Klinik                                    |                 0 |                   |
| 1204 | Akumulasi Penyusutan Kendaraan Ambulans                      |                   |                 0 |
| 2101 | Utang Dagang — Distributor Farmasi/Alkes                     |                   |       110.800.000 |
| 2102 | PPN Keluaran                                                 |                   |         1.980.000 |
| 2103 | Utang Gaji Dokter Umum Tetap                                 |                   |        18.000.000 |
| 2104 | Utang Fee Dokter Spesialis Paruh Waktu                       |                   |                 0 |
| 2105 | Utang Gaji Karyawan Non-Dokter                               |                   |                 0 |
| 2106 | Utang PPh 21 Karyawan                                        |                   |        12.600.000 |
| 3101 | Modal Pemilik                                                |                   |       801.500.000 |
| 3102 | Laba Ditahan                                                 |                   |                 0 |
| 4101 | Pendapatan Kapitasi BPJS Kesehatan (FKTP)                    |                   |       544.000.000 |
| 4102 | Pendapatan Jasa Non-Kapitasi/FFS Umum                        |                   |       166.500.000 |
| 4103 | Pendapatan MCU Korporat                                      |                   |       137.000.000 |
| 4104 | Pendapatan Laboratorium                                      |                   |        24.800.000 |
| 4105 | Pendapatan Penjualan Obat & Farmasi                          |                   |        96.800.000 |
| 4106 | Pendapatan Penjualan Produk Non-Obat Ritel                   |                   |        18.000.000 |
| 5101 | Beban Gaji Dokter Umum Tetap                                 |       156.000.000 |                   |
| 5102 | Beban Fee Dokter Spesialis Paruh Waktu                       |        48.000.000 |                   |
| 5103 | Beban Gaji Karyawan Non-Dokter                               |       210.000.000 |                   |
| 5104 | Beban HPP Obat & BHP Medis Terpakai                          |        88.500.000 |                   |
| 5105 | Beban Sewa Klinik/Gedung                                     |        66.000.000 |                   |
| 5106 | Beban Listrik, Air & Internet                                |        24.300.000 |                   |
| 5107 | Beban Penyusutan Peralatan Medis & Lab                       |                 0 |                   |
| 5108 | Beban Penyusutan Kendaraan Ambulans                          |                 0 |                   |
| 5109 | Beban Operasional Lain-lain (Sterilisasi/Limbah/Selisih Kas) |           350.000 |                   |
|      | **TOTAL**                                                    | **1.931.980.000** | **1.931.980.000** |

**Perhitungan manual pembuktian (2 arah):**

```
Sisi Debit  = Total Aset akhir (1.338.830.000, dari file 01 §20)
              + Total Beban Januari (593.150.000, dari file 01 §20)
            = 1.931.980.000

Sisi Kredit = Total Liabilitas akhir (143.380.000)
              + Modal Pemilik (801.500.000, BELUM berubah — laba berjalan belum di-closing)
              + Total Pendapatan Januari (987.100.000)
            = 143.380.000 + 801.500.000 + 987.100.000 = 1.931.980.000  ✓ BALANCE
```

| Skenario                                                               | Detail                                      | Hasil                                                                                                                                    |
| ---------------------------------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — kontra-aset masih nol (belum ada aset tetap)**             | Cek 1202 & 1204                             | Saldo **0** (bukan negatif, bukan positif) — aset tetap baru diakuisisi file 05, konsisten karena belum ada transaksi menyentuh akun ini |
| Positif — akun tidak tersentuh sama sekali tetap muncul dengan saldo 0 | Cek 2104 (fully paid) dan 2105 (fully paid) | Muncul di Trial Balance dengan saldo 0, TIDAK hilang dari daftar (regression check baris-nol, konsisten suite lain)                      |

## 2. Detail Ledger per Akun (**General Ledger — `detail`**)

### 2.1 Akun 4101 — Pendapatan Kapitasi BPJS (running balance)

| Tanggal    | Deskripsi           | Debit |      Kredit | Running Balance (Kredit) |
| ---------- | ------------------- | ----: | ----------: | -----------------------: |
| 2026-01-01 | Akrual Kapitasi JKP |       | 144.000.000 |              144.000.000 |
| 2026-01-01 | Akrual Kapitasi BKS |       | 120.000.000 |              264.000.000 |
| 2026-01-01 | Akrual Kapitasi TGR |       | 100.000.000 |              364.000.000 |
| 2026-01-01 | Akrual Kapitasi DPK |       |  80.000.000 |              444.000.000 |
| 2026-01-01 | Akrual Kapitasi BGR |       |  64.000.000 |              508.000.000 |
| 2026-01-01 | Akrual Kapitasi BDG |       |  36.000.000 |              544.000.000 |

| Skenario | Detail                                                                                                             | Hasil                                                               |
| -------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/detail {chart_of_account_id:<4101>, date_from:"2026-01-01", date_to:"2026-01-31"}` | 6 baris PERSIS seperti tabel, running balance akhir **544.000.000** |
| Negatif  | `chart_of_account_id` tidak ada di branch aktif                                                                    | 422 `not_found_in_branch`                                           |

### 2.2 Akun 1102 — Bank Mandiri Operasional (running balance, 13 transaksi menyentuh akun ini)

| Skenario                                                           | Detail                                                                                                             | Hasil                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                            | `POST accounting/general-ledger/detail {chart_of_account_id:<1102>, date_from:"2026-01-01", date_to:"2026-01-31"}` | 13 baris (opening + Setoran×4 + T5 + T6(3x: awal, reverse, repost) + T21 + T13 + T14 + T15a + T15b + T15c + T16 + T17 + T18), running balance akhir **479.030.000** — cek urutan tanggal & tanda debit/kredit PERSIS sesuai file 01 §19 |
| **Positif — jejak reverse tetap terlihat (additive, bukan hapus)** | Cek 3 baris terkait T6 (posting awal 28.400.000, reverse −28.400.000, repost 24.800.000)                           | SEMUA 3 baris HARUS tetap muncul di Detail Ledger (audit trail lengkap) — kalau baris reverse/awal HILANG dari ledger (bukan cuma di-flag `is_reversed`), itu 🆕 gap audit trail serius, laporkan                                       |

## 3. Summary by Account dengan Filter Dimensi Cabang (**General Ledger — `summary`**)

### 3.1 Pendapatan Kapitasi per Cabang — verifikasi breakdown penuh

| Skenario                                                                  | Payload                                                                                                                                     | Hasil                                                                                                                                                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — filter JKP                                                      | `POST accounting/general-ledger/summary {chart_of_account_id:<4101>, business_unit_id:<JKP>, date_from:"2026-01-01", date_to:"2026-01-31"}` | **144.000.000** — persis sesuai file 01 §1                                                                                                                                                         |
| Positif — filter BKS                                                      | Sama, `business_unit_id:<BKS>`                                                                                                              | **120.000.000**                                                                                                                                                                                    |
| Positif — filter TGR                                                      | Sama, `business_unit_id:<TGR>`                                                                                                              | **100.000.000**                                                                                                                                                                                    |
| Positif — filter DPK                                                      | Sama, `business_unit_id:<DPK>`                                                                                                              | **80.000.000**                                                                                                                                                                                     |
| Positif — filter BGR                                                      | Sama, `business_unit_id:<BGR>`                                                                                                              | **64.000.000**                                                                                                                                                                                     |
| Positif — filter BDG                                                      | Sama, `business_unit_id:<BDG>`                                                                                                              | **36.000.000**                                                                                                                                                                                     |
| **Positif — total 6 cabang = total konsolidasi (regression check wajib)** | Jumlahkan 6 hasil di atas: 144+120+100+80+64+36 (juta)                                                                                      | **544.000.000** — HARUS sama persis dengan hasil `summary` tanpa filter `business_unit_id` (§1.1 baris 4101). Kalau tidak sama, ada baris jurnal yang lolos tanpa dimensi cabang atau salah assign |
| Negatif                                                                   | `business_unit_id` yang tidak dipakai sama sekali di 4101 (mis. cabang fiktif lain)                                                         | 0, bukan error                                                                                                                                                                                     |

### 3.2 Pendapatan MCU Korporat per Cabang (partial dimension, hanya T4a & T4b)

| Skenario                                       | Payload                            | Hasil                                                                                                                                           |
| ---------------------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — filter JKP                           | `business_unit_id:<JKP>` pada 4103 | **85.000.000** (hanya T4a)                                                                                                                      |
| Positif — filter BKS                           | `business_unit_id:<BKS>` pada 4103 | **52.000.000** (hanya T4b)                                                                                                                      |
| Positif — filter cabang lain (TGR/DPK/BGR/BDG) | Sama pola                          | **0** — WAJAR, karena hanya 2 dari 6 cabang punya kontrak MCU korporat aktif di Januari (lihat file 01 §22 catatan desain dimensi tidak merata) |

## 4. Verifikasi Persamaan Akuntansi Dasar (Ulangan, Cross-Check Akhir)

| Skenario | Detail                                                                                                       | Hasil                                                                                           |
| -------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| Positif  | `Aset = Liabilitas + Ekuitas` per 2026-01-31, dengan Ekuitas = Modal Pemilik + Laba Berjalan (belum closing) | 1.338.830.000 = 143.380.000 + (801.500.000 + 393.950.000) = 1.338.830.000 ✓                     |
| Positif  | Laba Berjalan dari Trial Balance = Total Pendapatan − Total Beban                                            | 987.100.000 − 593.150.000 = **393.950.000**, HARUS sama dengan yang dipakai di §4 baris pertama |

## Referensi Silang

- File [`01-jurnal-manual-kapitasi-mcu-dan-operasional.id.md`](./01-jurnal-manual-kapitasi-mcu-dan-operasional.id.md) — sumber seluruh angka di file ini
- File [`03-tutup-periode-bulanan-dan-tahun-fiskal.id.md`](./03-tutup-periode-bulanan-dan-tahun-fiskal.id.md) — lanjutan, tutup periode Januari dengan Trial Balance ini sebagai basis
- File [`04-laporan-keuangan-konsolidasi-dan-per-cabang.id.md`](./04-laporan-keuangan-konsolidasi-dan-per-cabang.id.md) — Neraca & Laba Rugi disusun dari Trial Balance ini
