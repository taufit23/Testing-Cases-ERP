---
title: (Klinik Umum Besar) — 04. Laporan Keuangan Konsolidasi & per Cabang
category: accounting-klinik-umum
description: Neraca, Laba Rugi (konsolidasi & breakdown kapitasi per cabang), dan Arus Kas per 2026-01-31 — disusun dari Trial Balance file 02, periode Januari sudah closed (file 03).
visibility: internal
---

# 04. Laporan Keuangan Konsolidasi & per Cabang

> Prasyarat: file [`03-tutup-periode-bulanan-dan-tahun-fiskal.id.md`](./03-tutup-periode-bulanan-dan-tahun-fiskal.id.md) sudah selesai — Periode Januari `closed`, Fiscal Year FY2026 TETAP `open` (closing entry ke Laba Ditahan BELUM terjadi, konsisten §5 file 03).

## 1. Neraca / Balance Sheet (`accounting/reports/balance-sheet` atau sejenis)

| Skenario | Payload                                                           | Hasil                               |
| -------- | ----------------------------------------------------------------- | ----------------------------------- |
| Positif  | `POST accounting/reports/balance-sheet {as_of_date:"2026-01-31"}` | Neraca balance — lihat rincian §1.1 |

### 1.1 Neraca per 2026-01-31

```
ASET
  Aset Lancar
    Kas Kecil Klinik Pusat                       14.650.000
    Bank Mandiri Operasional                     479.030.000
    Bank BCA Penampungan Kapitasi BPJS           157.000.000
    Piutang Kapitasi BPJS Kesehatan (FKTP)       244.000.000
    Piutang MCU Korporat & Asuransi Swasta       164.500.000
    Persediaan Obat (Generik & Paten)            195.000.000
    Persediaan BHP Medis & Lab                    80.250.000
    PPN Masukan                                    4.400.000
    Total Aset Lancar                          1.338.830.000

  Aset Tetap
    Peralatan Medis & Lab                                  0
    Akum. Penyusutan Peralatan Medis & Lab                 0
    Kendaraan Ambulans Klinik                              0
    Akum. Penyusutan Kendaraan Ambulans                    0
    Total Aset Tetap (neto)                                0

  TOTAL ASET                                  1.338.830.000

LIABILITAS
  Utang Dagang — Distributor Farmasi/Alkes     110.800.000
  PPN Keluaran                                   1.980.000
  Utang Gaji Dokter Umum Tetap                  18.000.000
  Utang Fee Dokter Spesialis Paruh Waktu                 0
  Utang Gaji Karyawan Non-Dokter                         0
  Utang PPh 21 Karyawan                         12.600.000
  TOTAL LIABILITAS                             143.380.000

EKUITAS
  Modal Pemilik                                801.500.000
  Laba Ditahan                                           0
  Laba Berjalan (belum closing)                393.950.000
  TOTAL EKUITAS                              1.195.450.000

TOTAL LIABILITAS + EKUITAS                   1.338.830.000   ✓ = TOTAL ASET
```

| Skenario                                                      | Detail                              | Hasil                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — Laba Berjalan tampil terpisah dari Laba Ditahan** | Cek baris ekuitas                   | Karena Fiscal Year belum di-closing (file 03 §4), sistem HARUS menampilkan "Laba Berjalan"/`current_year_earnings` sebagai baris ekuitas terpisah dari Laba Ditahan (3102, tetap 0) — kalau sistem malah menjumlahkan otomatis ke 3102 TANPA closing entry resmi, itu gap konsep akrual/closing, belum diverifikasi ke kode, catat hasil aktual |
| Negatif                                                       | `as_of_date` sebelum ada saldo awal | Neraca kosong/nol, bukan error                                                                                                                                                                                                                                                                                                                  |

## 2. Laba Rugi / Income Statement (`accounting/reports/income-statement`)

### 2.1 Konsolidasi (6 cabang)

```
PENDAPATAN
  Pendapatan Kapitasi BPJS Kesehatan (FKTP)     544.000.000
  Pendapatan Jasa Non-Kapitasi/FFS Umum         166.500.000
  Pendapatan MCU Korporat                       137.000.000
  Pendapatan Laboratorium                        24.800.000
  Pendapatan Penjualan Obat & Farmasi            96.800.000
  Pendapatan Penjualan Produk Non-Obat Ritel      18.000.000
  TOTAL PENDAPATAN                              987.100.000

BEBAN
  Beban Gaji Dokter Umum Tetap                  156.000.000
  Beban Fee Dokter Spesialis Paruh Waktu          48.000.000
  Beban Gaji Karyawan Non-Dokter                 210.000.000
  Beban HPP Obat & BHP Medis Terpakai             88.500.000
  Beban Sewa Klinik/Gedung                        66.000.000
  Beban Listrik, Air & Internet                   24.300.000
  Beban Penyusutan Peralatan Medis & Lab                   0
  Beban Penyusutan Kendaraan Ambulans                      0
  Beban Operasional Lain-lain                        350.000
  TOTAL BEBAN                                   593.150.000

LABA BERSIH JANUARI 2026                        393.950.000   (margin ≈ 39,9%)
```

| Skenario | Payload                                                                                   | Hasil                        |
| -------- | ----------------------------------------------------------------------------------------- | ---------------------------- |
| Positif  | `POST accounting/reports/income-statement {date_from:"2026-01-01", date_to:"2026-01-31"}` | Angka PERSIS seperti di atas |

### 2.2 Breakdown Pendapatan Kapitasi per Cabang (dimensi lengkap, lihat file 01 §22)

| Cabang    | Pendapatan Kapitasi | % dari Total Kapitasi |
| --------- | ------------------: | --------------------: |
| JKP       |         144.000.000 |                 26,5% |
| BKS       |         120.000.000 |                 22,1% |
| TGR       |         100.000.000 |                 18,4% |
| DPK       |          80.000.000 |                 14,7% |
| BGR       |          64.000.000 |                 11,8% |
| BDG       |          36.000.000 |                  6,6% |
| **Total** |     **544.000.000** |                  100% |

| Skenario                                   | Payload                                                                                                                                                                                                                                                                                                                                             | Hasil                                                                                                                                                                                                                                    |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                    | `POST accounting/reports/income-statement {date_from:"2026-01-01", date_to:"2026-01-31", business_unit_id:<JKP>}` (kalau laporan mendukung filter dimensi langsung)                                                                                                                                                                                 | Baris 4101 = 144.000.000, baris lain (4102-4106) = 0 (TIDAK didimensikan ke cabang, sesuai keputusan desain file 01 §22) — **JANGAN salah baca 0 di baris lain sebagai bug**, itu konsisten dengan cakupan dimensi yang sengaja dibatasi |
| **Positif — total 6 cabang = konsolidasi** | Jumlahkan Laba Rugi per cabang untuk baris 4101 saja: 144+120+100+80+64+36 (juta)                                                                                                                                                                                                                                                                   | **544.000.000**, sama persis dengan §2.1 baris Pendapatan Kapitasi — regression check wajib                                                                                                                                              |
| **Catatan cakupan (bukan bug)**            | Laba Rugi PENUH per cabang (semua lini pendapatan & beban dipecah per cabang) TIDAK bisa disusun dari data file 01 karena keputusan desain sengaja membatasi dimensi cabang hanya ke kapitasi — kalau suite lanjutan dibutuhkan dengan breakdown P&L penuh per cabang, perlu redesain ulang file 01 dengan `business_unit_id` di SEMUA baris jurnal | —                                                                                                                                                                                                                                        |

## 3. Laporan Arus Kas / Cash Flow Statement — Metode Langsung & Tidak Langsung

### 3.1 Metode Tidak Langsung

```
ARUS KAS DARI AKTIVITAS OPERASI
  Laba Bersih Januari 2026                                     393.950.000
  Penyesuaian:
    (+) Kenaikan Utang Dagang                                   14.400.000
    (+) Kenaikan PPN Keluaran                                    1.980.000
    (−) Kenaikan Utang Gaji Dokter Umum Tetap                  (24.000.000)  [naik neto dari akrual T11 dikurangi bayar T13]
    (−) Penurunan Utang Fee Dokter Spesialis Paruh Waktu       ... lihat catatan di bawah
    (−) Penurunan Utang Gaji Karyawan Non-Dokter               (65.000.000)
    (+) Kenaikan Utang PPh 21 Karyawan                            2.850.000
    (−) Kenaikan Piutang Kapitasi BPJS                        (82.000.000)
    (−) Kenaikan Piutang MCU Korporat & Asuransi Swasta        (77.000.000)
    (−) Kenaikan Persediaan Obat                               (50.000.000)
    (−) Kenaikan Persediaan BHP Medis & Lab                    (21.500.000)
    (−) Kenaikan PPN Masukan                                    (4.400.000)
  Kas Bersih dari Aktivitas Operasi                             ... (hitung manual sebelum eksekusi endpoint, lihat §3.2)

ARUS KAS DARI AKTIVITAS INVESTASI
  (Tidak ada — akuisisi aset tetap baru terjadi Februari, file 05)          0

ARUS KAS DARI AKTIVITAS PENDANAAN
  (Tidak ada transaksi modal/pinjaman baru di Januari)                     0
```

**Perhitungan manual kenaikan/penurunan tiap akun neraca (WAJIB dihitung dulu, cocokkan dengan metode langsung di §3.2 sebelum eksekusi endpoint):**

```
Δ Piutang Kapitasi BPJS         = 244.000.000 − 162.000.000 = +82.000.000 (naik, kurangi kas)
Δ Piutang MCU Korporat          = 164.500.000 − 87.500.000  = +77.000.000 (naik, kurangi kas)
Δ Persediaan Obat               = 195.000.000 − 145.000.000 = +50.000.000 (naik, kurangi kas)
Δ Persediaan BHP Medis & Lab    = 80.250.000  − 58.750.000  = +21.500.000 (naik, kurangi kas)
Δ PPN Masukan                   = 4.400.000   − 0           = +4.400.000  (naik, kurangi kas)
Δ Utang Dagang Distributor      = 110.800.000 − 96.400.000  = +14.400.000 (naik, tambah kas)
Δ PPN Keluaran                  = 1.980.000   − 0           = +1.980.000  (naik, tambah kas)
Δ Utang Gaji Dokter Tetap       = 18.000.000  − 42.000.000  = −24.000.000 (turun, kurangi kas)
Δ Utang Fee Dokter Paruh Waktu  = 0           − 28.600.000  = −28.600.000 (turun, kurangi kas)
Δ Utang Gaji Non-Dokter         = 0           − 65.000.000  = −65.000.000 (turun, kurangi kas)
Δ Utang PPh 21 Karyawan         = 12.600.000  − 9.750.000   = +2.850.000  (naik, tambah kas)

Kas Bersih dari Aktivitas Operasi
  = 393.950.000
    + 14.400.000 + 1.980.000 + 2.850.000                 (kenaikan liabilitas, tambah kas)
    − 24.000.000 − 28.600.000 − 65.000.000                (penurunan liabilitas, kurangi kas)
    − 82.000.000 − 77.000.000 − 50.000.000 − 21.500.000 − 4.400.000   (kenaikan aset non-kas, kurangi kas)
  = 393.950.000 + 19.230.000 − 117.600.000 − 234.900.000
  = 60.680.000
```

### 3.2 Verifikasi Silang — Metode Langsung (Perubahan Kas & Setara Kas Aktual)

```
Kas & Setara Kas Awal (2026-01-01) = 15.000.000 (1101) + 480.000.000 (1102) + 95.000.000 (1103)
                                    = 590.000.000

Kas & Setara Kas Akhir (2026-01-31) = 14.650.000 (1101) + 479.030.000 (1102) + 157.000.000 (1103)
                                     = 650.680.000

Kenaikan Kas Bersih = 650.680.000 − 590.000.000 = 60.680.000
```

| Skenario                                                                         | Detail                                                                                                          | Hasil                                                                                                                                                                              |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — cocok silang metode langsung vs tidak langsung (wajib sama persis)** | Bandingkan hasil §3.1 (60.680.000) dengan §3.2 (60.680.000)                                                     | **COCOK PERSIS** — pembuktian bahwa seluruh perubahan neraca sudah tertangkap benar di rekonsiliasi laba ke kas. Kalau tidak cocok, ada 1+ akun neraca yang lewat dihitung di §3.1 |
| Positif                                                                          | `POST accounting/reports/cash-flow-statement {date_from:"2026-01-01", date_to:"2026-01-31", method:"indirect"}` | Angka Kas Bersih Operasi = **60.680.000**, sesuai §3.1                                                                                                                             |
| Negatif                                                                          | `method` di luar enum (`direct/indirect`)                                                                       | 422                                                                                                                                                                                |

## 4. Ringkasan Angka Kunci File Ini

| Item                                  |         Nilai |
| ------------------------------------- | ------------: |
| Total Aset                            | 1.338.830.000 |
| Total Liabilitas                      |   143.380.000 |
| Modal Pemilik                         |   801.500.000 |
| Laba Berjalan Januari (belum closing) |   393.950.000 |
| Total Ekuitas                         | 1.195.450.000 |
| Kas & Setara Kas awal                 |   590.000.000 |
| Kas & Setara Kas akhir                |   650.680.000 |
| Kenaikan Kas Bersih                   |    60.680.000 |

## Referensi Silang

- File [`02-general-ledger-dan-trial-balance-per-cabang.id.md`](./02-general-ledger-dan-trial-balance-per-cabang.id.md) — Trial Balance sumber seluruh angka
- File [`05-anggaran-dan-aset-tetap.id.md`](./05-anggaran-dan-aset-tetap.id.md) — Budget vs Actual dipakai breakdown kapitasi per cabang §2.2 di atas sebagai basis realisasi, akuisisi aset tetap Februari mengubah Kas & Setara Kas awal file itu
