---
title: (Klinik Gigi) — 04. Laporan Keuangan
category: accounting-klinik-gigi
description: Neraca (Balance Sheet), Laba Rugi (Income Statement per lini jasa & per cabang), dan Arus Kas (Cash Flow) — semua angka dihitung manual dari file 01/02, termasuk breakdown per Business Unit yang jadi ciri khas suite jasa ini.
visibility: internal
---

# 04. Laporan Keuangan

> Prasyarat: file [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) sudah selesai. **JANGAN jalankan Close Fiscal Year (file 03 §3.1) sebelum file ini selesai** — laporan di sini butuh akun Pendapatan/Beban masih ada saldo berjalan (belum di-nol-kan closing entry).

## 1. Neraca / Balance Sheet (**Balance Sheet** atau endpoint sejenis)

| Skenario | Detail                                                 | Hasil                                                                |
| -------- | ------------------------------------------------------ | -------------------------------------------------------------------- |
| Positif  | `POST reports/balance-sheet {as_of_date:"2026-01-28"}` | Struktur sesuai `cash_flow_section`/`category` per akun (file 00 §2) |

**Neraca acuan (WAJIB cocok):**

```
ASET
  Aset Lancar
    Kas Kecil Klinik (Harian)               5.338.000
    Bank BCA Operasional                  131.713.000
    Piutang Pasien BPJS & Asuransi         29.380.000
    Persediaan BHP Gigi                    27.470.000
    PPN Masukan                               550.000
  Total Aset Lancar                       194.451.000
  Aset Tetap                                        0   (belum ada, file 05)
TOTAL ASET                                194.451.000

LIABILITAS
  Liabilitas Jangka Pendek
    Utang Dagang — Supplier Bahan Gigi     16.850.000
    PPN Keluaran                               33.000
    Utang Komisi Dokter                     6.750.000
    Utang PPh 21 Karyawan                   2.300.000
  Total Liabilitas                         25.933.000

EKUITAS
  Modal Pemilik                            181.350.000
  Laba Ditahan                                       0
  Laba (Rugi) Berjalan                     (12.832.000)
  Total Ekuitas                            168.518.000

TOTAL LIABILITAS + EKUITAS                194.451.000
```

**Verifikasi**: `168.518.000 (ekuitas) + 25.933.000 (liabilitas) = 194.451.000 = Total Aset` ✓.

| Skenario                                                           | Detail                                                                       | Hasil                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — Laba/Rugi berjalan muncul di Neraca TANPA close year** | Cek baris "Laba (Rugi) Berjalan"                                             | Harus muncul otomatis dihitung dari `Pendapatan − Beban` akun-akun yang BELUM di-closing-entry-kan (karena Fiscal Year belum ditutup) — kalau baris ini TIDAK muncul/tetap 0, Neraca akan TIMPANG (Aset ≠ Liabilitas+Ekuitas), catat sebagai temuan kalau terjadi |
| Negatif                                                            | `as_of_date` di masa depan jauh (mis. `2027-01-01`) tanpa transaksi tambahan | Sama persis dengan neraca 2026-01-28 (tidak ada mutasi baru) — regression check konsistensi tanggal                                                                                                                                                               |

## 2. Laba Rugi / Income Statement — Per Lini Jasa (**Income Statement**)

| Skenario | Detail                                                                         | Hasil                          |
| -------- | ------------------------------------------------------------------------------ | ------------------------------ |
| Positif  | `POST reports/income-statement {date_from:"2026-01-01", date_to:"2026-01-28"}` | Cocok dengan struktur di bawah |

```
PENDAPATAN
  Pendapatan Jasa Gigi Umum          3.550.000
  Pendapatan Jasa Ortodonti          2.500.000
  Pendapatan Jasa Estetika Gigi      1.800.000
  Pendapatan Penjualan Produk Ritel    300.000
Total Pendapatan                     8.150.000

BEBAN
  Beban Komisi Dokter                2.487.000
  Beban BHP Gigi                       730.000
  Beban Sewa Klinik                  6.000.000
  Beban Gaji Karyawan Non-Dokter     9.000.000
  Beban Listrik & Air                2.750.000
  Beban Selisih Kas Kasir Harian        15.000
  Beban Sterilisasi & Limbah Medis           0
Total Beban                         20.982.000

LABA (RUGI) BERSIH                (12.832.000)
```

| Skenario                                                                                      | Detail                                                                                                                                                                                                   | Hasil                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — margin kotor per lini jasa (perhitungan tambahan manual, bukan dari 1 endpoint)** | Hitung manual: Pendapatan Jasa Gigi Umum (3.550.000) dikurangi porsi Komisi+BHP yang melekat langsung ke lini ini (dari file 01: T1 300k+45k, T2 360k+80k, T13 368k+55k, T14 204k+40k = total 1.452.000) | Margin kotor Jasa Gigi Umum ≈ 3.550.000 − 1.452.000 = **2.098.000** (≈59% dari pendapatan) — endpoint laporan project ini KEMUNGKINAN tidak native menghitung margin per lini otomatis (hanya total Beban gabungan), jadi ini murni perhitungan manual dari data mentah GL untuk verifikasi cross-check, bukan mengklaim ada fitur yang hilang |
| Negatif                                                                                       | `date_from` > `date_to`                                                                                                                                                                                  | 422                                                                                                                                                                                                                                                                                                                                            |

## 3. Laba Rugi Per Cabang — Filter Dimensi Business Unit

Fokus khusus suite ini: Klinik Ceria Bekasi (BKS) adalah cabang termuda — bandingkan kinerjanya dengan 2 cabang lain.

| Skenario                 | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Hasil                                                                                                                                                                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — KG             | Filter `business_unit_id:<KG>` pada laporan/GL summary pendapatan (dari file 02 §3)                                                                                                                                                                                                                                                                                                                                                                                           | Pendapatan KG = 1.970.000 (T1 750k + T4 300k + T13 920k)                                                                                                                                                                                        |
| Positif — BSD            | Filter `business_unit_id:<BSD>`                                                                                                                                                                                                                                                                                                                                                                                                                                               | Pendapatan BSD = 3.680.000 (T2 1.200k + T8 1.800k + T14 680k) — **cabang dengan pendapatan tertagged tertinggi** di 4 minggu ini                                                                                                                |
| Positif — BKS            | Filter `business_unit_id:<BKS>`                                                                                                                                                                                                                                                                                                                                                                                                                                               | Pendapatan BKS = 2.500.000 (T3, DP ortodonti) — cabang termuda TAPI nilai transaksi tunggalnya besar (DP behel), ilustrasi realistis "cabang baru sedikit transaksi tapi bernilai tinggi per transaksi" vs "cabang lama banyak transaksi kecil" |
| **Catatan keterbatasan** | 5.203 (Listrik&Air, 2.750.000) dan T9 (pelunasan piutang, tidak berpengaruh ke P&L) sengaja TIDAK ditag ke cabang manapun — total per-cabang di atas (1.970.000+3.680.000+2.500.000=8.150.000) SUDAH sama dengan Total Pendapatan §2 karena SEMUA baris pendapatan file 01 kebetulan bertag BU, hanya baris beban campuran (T15) yang tidak — jadi rekonsiliasi pendapatan per-cabang otomatis pas, TAPI beban per-cabang TIDAK bisa direkonsiliasi penuh dari filter BU saja | Kalau mau P&L per cabang yang akurat penuh (termasuk alokasi beban bersama), perlu kebijakan alokasi manual di luar sistem — dicatat sebagai keterbatasan desain wajar, bukan bug                                                               |

## 4. Arus Kas / Cash Flow Statement (`reports/cash-flow`)

| Skenario | Detail                                                                  | Hasil                                                                                                         |
| -------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST reports/cash-flow {date_from:"2026-01-01", date_to:"2026-01-28"}` | Dikelompokkan per `cash_flow_section` (operating/investing/financing) sesuai Chart of Account Type file 00 §2 |

**Arus kas acuan (akun kas: 1101 + 1102 gabungan, karena keduanya `is_cash_account:true`):**

```
Saldo Kas Awal (1101+1102)     = 3.000.000 + 150.000.000 = 153.000.000
Saldo Kas Akhir (1101+1102)    = 5.338.000 + 131.713.000 = 137.051.000
Perubahan Kas Bersih           = 137.051.000 − 153.000.000 = (15.949.000)
```

Karena SEMUA transaksi file 01 masuk kategori `operating` (tidak ada investasi/pendanaan di file ini — aset tetap baru muncul file 05, tidak ada setoran modal baru/pinjaman), maka:

```
Arus Kas dari Aktivitas Operasi  = (15.949.000)
Arus Kas dari Aktivitas Investasi =          0
Arus Kas dari Aktivitas Pendanaan =          0
PERUBAHAN KAS BERSIH              = (15.949.000)
```

| Skenario                                                   | Detail                                                                                                                                                                                                                                                                                                                                                                                 | Hasil                                                                                                                                                                                                                                 |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — verifikasi metode tidak langsung vs langsung** | Kalau laporan pakai metode tidak langsung (mulai dari Laba Rugi lalu koreksi non-kas), cek: Laba Rugi (−12.832.000) + kenaikan Piutang (−880.000, piutang naik = kas berkurang) + kenaikan Persediaan (−4.720.000) + kenaikan PPN Masukan (−550.000) + kenaikan Utang Dagang (+2.550.000) + kenaikan PPN Keluaran (+33.000) + kenaikan Utang PPh21 (+450.000) + Utang Komisi tetap (0) | Total = −12.832.000 −880.000 −4.720.000 −550.000 +2.550.000 +33.000 +450.000 = **(15.949.000)** — HARUS cocok persis dengan perhitungan metode langsung di atas, ini pembuktian silang wajib untuk laporan arus kas manapun metodenya |
| Negatif                                                    | Kalau hasil endpoint TIDAK cocok dengan salah satu perhitungan manual di atas                                                                                                                                                                                                                                                                                                          | Catat sebagai temuan — sebutkan metode mana (langsung/tidak langsung) yang dipakai endpoint dan di baris/akun mana penyimpangannya mulai muncul                                                                                       |

## Referensi Silang

- File [`01-jurnal-manual-transaksi-harian-klinik.id.md`](./01-jurnal-manual-transaksi-harian-klinik.id.md) & [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) — sumber seluruh angka
- Suite retail [`../accounting/04-laporan-keuangan.id.md`](../accounting/04-laporan-keuangan.id.md) — pola dasar 3 laporan yang direplikasi strukturnya
