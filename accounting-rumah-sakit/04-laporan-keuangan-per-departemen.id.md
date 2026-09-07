---
title: (Rumah Sakit) — 04. Laporan Keuangan Konsolidasi & Per Departemen
category: accounting-rumah-sakit
description: Neraca, Laba Rugi (konsolidasi & breakdown per departemen RI/RJ/FAR/PJG), dan Arus Kas (metode langsung & tidak langsung, harus cocok silang) — semua angka dihitung manual dari file 01/02, skala nilai miliaran rupiah.
visibility: internal
---

# 04. Laporan Keuangan Konsolidasi & Per Departemen

> Prasyarat: file [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) sudah selesai. **JANGAN jalankan Close Fiscal Year (file 03 §3.1) sebelum file ini selesai.**

## 1. Neraca / Balance Sheet (**Balance Sheet**)

| Skenario | Detail                                                 | Hasil                                                                                                                                                 |
| -------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST reports/balance-sheet {as_of_date:"2026-01-28"}` | Struktur sesuai `cash_flow_section`/`category` per akun (file 00 §2), termasuk pemisahan Liabilitas Jangka Pendek vs Jangka Panjang (`LJP` vs `LJPJ`) |

**Neraca acuan (WAJIB cocok):**

```
ASET
  Aset Lancar
    Kas Kecil Operasional RS                    29.935.000
    Bank BCA Operasional                       750.700.000
    Bank Mandiri Khusus BPJS                 3.300.000.000
    Piutang Pasien Umum                        180.000.000
    Piutang Klaim BPJS Kesehatan               240.000.000
    Piutang Klaim Asuransi Swasta                        0
    Persediaan Obat, Alkes & BMHP             1.360.350.000
    PPN Masukan                                 91.200.000
  Total Aset Lancar                          5.952.185.000

  Aset Tetap
    Gedung Rumah Sakit                      40.000.000.000
    Akumulasi Peny. Gedung                  (8.000.000.000)
    Mesin CT-Scan                           12.000.000.000
    Akumulasi Peny. CT-Scan                 (4.000.000.000)
    Mesin MRI                               18.000.000.000
    Akumulasi Peny. MRI                     (3.000.000.000)
    Peralatan Radiologi                      5.000.000.000
    Akumulasi Peny. Radiologi               (2.000.000.000)
  Total Aset Tetap (net)                    58.000.000.000

TOTAL ASET                                  63.952.185.000

LIABILITAS
  Liabilitas Jangka Pendek
    Utang Dagang Supplier                    1.246.200.000
    PPN Keluaran                                15.220.000
    Utang Fee Dokter Spesialis                 166.250.000
    Utang Gaji Karyawan Tetap                  420.000.000
    Utang PPh 21 Karyawan                      187.500.000
    Uang Muka Pasien Rawat Inap                210.000.000
  Total Liabilitas Jangka Pendek             2.245.170.000

  Liabilitas Jangka Panjang
    Utang Bank — Ekspansi Gedung             14.750.000.000
  Total Liabilitas Jangka Panjang            14.750.000.000

TOTAL LIABILITAS                            16.995.170.000

EKUITAS
  Modal Pemilik                              49.100.000.000
  Laba Ditahan                                          0
  Laba (Rugi) Berjalan                      (2.142.985.000)
  Total Ekuitas                              46.957.015.000

TOTAL LIABILITAS + EKUITAS                  63.952.185.000
```

**Verifikasi**: `46.957.015.000 (ekuitas) + 16.995.170.000 (liabilitas) = 63.952.185.000 = Total Aset` ✓.

| Skenario                                                                                 | Detail                                                                                                             | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — Liabilitas terpisah Jangka Pendek vs Jangka Panjang (kasus unik suite ini)** | Cek response `reports/balance-sheet` mengelompokkan `2201` (Utang Bank) SECARA TERPISAH dari 6 akun `21xx` lainnya | Kalau laporan masih menyamaratakan SEMUA akun tipe `liability` jadi 1 kelompok tanpa membedakan `LJP` vs `LJPJ` (chart_of_account_type), itu 🆕 gap presentasi laporan — Neraca RS besar SEHARUSNYA memisahkan liabilitas lancar vs tidak lancar karena signifikan untuk rasio likuiditas (current ratio) — belum pernah dites di 4 suite lain yang semua liabilitasnya jangka pendek. Belum diverifikasi ke kode, laporkan hasil aktual |
| **Positif — Laba/Rugi berjalan muncul TANPA close year**                                 | Cek baris "Laba (Rugi) Berjalan"                                                                                   | Harus muncul otomatis dari `Pendapatan − Beban` akun yang belum di-closing-entry-kan — kalau tidak muncul/tetap 0, Neraca akan TIMPANG                                                                                                                                                                                                                                                                                                   |
| Negatif                                                                                  | `as_of_date` di masa depan jauh tanpa transaksi tambahan                                                           | Sama persis dengan neraca 2026-01-28                                                                                                                                                                                                                                                                                                                                                                                                     |

## 2. Laba Rugi / Income Statement Konsolidasi (**Income Statement**)

| Skenario | Detail                                                                         | Hasil                   |
| -------- | ------------------------------------------------------------------------------ | ----------------------- |
| Positif  | `POST reports/income-statement {date_from:"2026-01-01", date_to:"2026-01-28"}` | Cocok struktur di bawah |

```
PENDAPATAN
  Pendapatan RI Kelas 3                18.000.000
  Pendapatan RI Kelas 2                         0
  Pendapatan RI Kelas 1                         0
  Pendapatan RI VIP                    85.000.000
  Pendapatan RI ICU                    62.000.000
  Pendapatan RJ Poli Umum               3.600.000
  Pendapatan RJ Poli Spesialis         12.400.000
  Pendapatan Laboratorium               9.800.000
  Pendapatan Radiologi                 38.000.000
  Pendapatan Farmasi Obat Resep         7.200.000
  Pendapatan Farmasi Obat Bebas/OTC     2.000.000
Total Pendapatan                      238.000.000

BEBAN
  Beban Fee Dokter Spesialis           16.250.000
  Beban Gaji Karyawan Tetap         1.850.000.000
  Beban HPP Obat & Alkes                5.800.000
  Beban Bahan Medis Habis Pakai         3.850.000
  Beban Piutang Tak Tertagih (BPJS)   200.000.000
  Beban Administrasi Bank                       0
  Beban Bunga Pinjaman Bank           125.000.000
  Beban Selisih Kas Kasir                  85.000
  Beban Sterilisasi & Limbah Medis    180.000.000
Total Beban                         2.380.985.000

LABA (RUGI) BERSIH                 (2.142.985.000)
```

| Skenario                                                            | Detail                                                                                                                                                                   | Hasil                                                                                                                                                                                                        |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Positif — margin kotor Rawat Inap (perhitungan tambahan manual)** | Pendapatan RI (18.000.000+85.000.000+62.000.000=165.000.000) dikurangi fee dokter & BMHP yang melekat langsung (T2 8.500.000, T3 4.650.000+3.200.000 = total 16.350.000) | Margin kotor RI ≈ 165.000.000 − 16.350.000 = **148.650.000** (≈90%) — endpoint laporan project ini KEMUNGKINAN tidak native menghitung margin per departemen otomatis, murni cross-check manual dari data GL |
| Negatif                                                             | `date_from` > `date_to`                                                                                                                                                  | 422                                                                                                                                                                                                          |

## 3. Laba Rugi Per Departemen — Filter Dimensi Business Unit

| Skenario                 | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Hasil                                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — RI             | Filter `business_unit_id:<RI>` (dari file 02 §3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Pendapatan RI = **165.000.000** — departemen dengan pendapatan tertinggi (rawat inap selalu jadi kontributor terbesar RS besar, realistis)                                                                       |
| Positif — RJ             | Filter `business_unit_id:<RJ>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Pendapatan RJ = **16.000.000**                                                                                                                                                                                   |
| Positif — FAR            | Filter `business_unit_id:<FAR>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Pendapatan FAR = **9.200.000**                                                                                                                                                                                   |
| Positif — PJG            | Filter `business_unit_id:<PJG>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Pendapatan PJG = **47.800.000** — Radiologi (CT-Scan/MRI) mendominasi kontribusi PJG dibanding Laboratorium, mencerminkan nilai tindakan penunjang medis besar yang jauh lebih tinggi dari pemeriksaan lab rutin |
| **Catatan keterbatasan** | T12 (klaim BPJS dispute) dan T13 (pelunasan asuransi) TIDAK ditag ke departemen manapun (klaim gabungan lintas kelas/tindakan) — total pendapatan per-departemen (165.000.000+16.000.000+9.200.000+47.800.000=238.000.000) SUDAH sama dengan Total Pendapatan §2 karena SEMUA baris pendapatan (bukan piutang/pelunasan) di file 01 kebetulan bertag BU. TAPI beban (gaji karyawan, bunga pinjaman, write-off BPJS, dsb) SEBAGIAN BESAR TIDAK ditag departemen (bersifat korporat/lintas unit) — P&L per departemen yang akurat penuh (termasuk alokasi beban bersama/overhead) butuh kebijakan alokasi manual di luar sistem, sama seperti keterbatasan yang dicatat di suite klinik gigi | Dicatat sebagai keterbatasan desain wajar, bukan bug                                                                                                                                                             |

## 4. Arus Kas / Cash Flow Statement (`reports/cash-flow`)

| Skenario | Detail                                                                  | Hasil                                                                 |
| -------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Positif  | `POST reports/cash-flow {date_from:"2026-01-01", date_to:"2026-01-28"}` | Dikelompokkan per `cash_flow_section` (operating/investing/financing) |

**Arus kas acuan (akun kas: 1101+1102+1103 gabungan, ketiganya `is_cash_account:true`):**

```
Saldo Kas Awal (1101+1102+1103) = 25.000.000 + 3.500.000.000 + 1.200.000.000
                                 = 4.725.000.000
Saldo Kas Akhir (1101+1102+1103) = 29.935.000 + 750.700.000 + 3.300.000.000
                                 = 4.080.635.000
Perubahan Kas Bersih             = 4.080.635.000 − 4.725.000.000 = (644.365.000)
```

**Klasifikasi per aktivitas (kasus BARU di suite ini — ada aktivitas Financing sungguhan, beda dari suite lain yang semua transaksinya Operating):**

```
Aktivitas Operasi   = seluruh transaksi klinis/kas (T1-T14, T16-T17) TERMASUK bunga pinjaman (T15 bagian bunga 125.000.000,
                       secara konvensi umum bunga dilaporkan sebagai Operating meski terkait pinjaman)
Aktivitas Investasi = 0 (belum ada akuisisi aset tetap di file ini — file 06 baru mulai Februari)
Aktivitas Pendanaan = T15 bagian POKOK cicilan pinjaman (250.000.000, KELUAR) — SATU-SATUNYA baris Financing di file ini

Arus Kas dari Aktivitas Pendanaan = (250.000.000)
Arus Kas dari Aktivitas Operasi   = (644.365.000) − (250.000.000) = (394.365.000)
Arus Kas dari Aktivitas Investasi =            0
PERUBAHAN KAS BERSIH               = (644.365.000)
```

| Skenario                                                                       | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — pemisahan pokok vs bunga cicilan pinjaman (kasus baru suite ini)** | Cek endpoint MEMISAHKAN baris T15 menjadi 2 klasifikasi arus kas berbeda (pokok=Financing, bunga=Operating) MESKIPUN keduanya berasal dari 1 jurnal manual yang sama                                                                                                                                                                                                                                                                                                                                                                                                    | Kalau sistem TIDAK bisa memisahkan berdasarkan akun per BARIS jurnal (hanya mengklasifikasi PER JURNAL, bukan per baris), maka seluruh T15 (375.000.000) akan salah masuk ke 1 kategori saja — ini **gap arsitektur potensial PRIORITAS TINGGI** kalau ternyata terjadi, karena `cash_flow_section` didefinisikan di level Chart of Account Type (per akun), BUKAN di level jurnal, jadi SEHARUSNYA otomatis benar per baris — belum diverifikasi ke kode, laporkan hasil aktual apa adanya |
| **Positif — verifikasi metode tidak langsung vs langsung**                     | Metode tidak langsung: Laba Rugi (−2.142.985.000) + kenaikan Piutang Pasien Umum (0) + penurunan Piutang BPJS (+2.210.000.000, piutang turun = kas api tidak langsung masuk secara akrual) + penurunan Piutang Asuransi (+620.000.000) + kenaikan Persediaan (−410.350.000) + kenaikan PPN Masukan (−46.200.000) + kenaikan Utang Dagang (+466.200.000) + kenaikan PPN Keluaran (+220.000) + penurunan Utang Fee Dokter (−1.183.750.000) + kenaikan Utang PPh21 (+92.500.000) + penurunan Utang Bank pokok (−250.000.000, reklas ke financing terpisah bukan operating) | Total (murni operating, tanpa pokok pinjaman) = −2.142.985.000 +2.210.000.000 +620.000.000 −410.350.000 −46.200.000 +466.200.000 +220.000 −1.183.750.000 +92.500.000 = **(394.365.000)** — HARUS cocok persis dengan perhitungan metode langsung Operating di atas                                                                                                                                                                                                                          |
| Negatif                                                                        | Hasil endpoint TIDAK cocok dengan salah satu perhitungan manual di atas                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Catat sebagai temuan — sebutkan metode mana yang dipakai endpoint dan di baris/akun mana penyimpangan mulai muncul                                                                                                                                                                                                                                                                                                                                                                          |

## Referensi Silang

- File [`01-jurnal-manual-transaksi-klinis-dan-klaim-bpjs.id.md`](./01-jurnal-manual-transaksi-klinis-dan-klaim-bpjs.id.md) & [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) — sumber seluruh angka
- Suite klinik gigi [`../accounting-klinik-gigi/04-laporan-keuangan.id.md`](../accounting-klinik-gigi/04-laporan-keuangan.id.md) — pola dasar 3 laporan yang direplikasi strukturnya, plus kasus baru pemisahan Financing (pokok pinjaman) yang belum pernah dites di suite manapun sebelumnya
