---
title: (Klinik Umum Besar) — 05. Anggaran (Budget) Kapitasi per Cabang & Aset Tetap
category: accounting-klinik-umum
description: Budget kapitasi Januari 2026 per cabang vs realisasi (kasus over-budget cabang lama & under-budget cabang baru BDG), plus akuisisi & penyusutan bulan pertama 2 aset kesehatan menengah (Peralatan Medis & Lab garis lurus, Kendaraan Ambulans saldo menurun).
visibility: internal
---

# 05. Anggaran (Budget) Kapitasi per Cabang & Aset Tetap

> Prasyarat: file [`04-laporan-keuangan-konsolidasi-dan-per-cabang.id.md`](./04-laporan-keuangan-konsolidasi-dan-per-cabang.id.md) sudah selesai. **Transaksi aset tetap di file ini sengaja bertanggal 2026-02-02 dan seterusnya** — SETELAH Periode Januari `closed` (file 03) — supaya Trial Balance/Neraca Januari yang sudah diverifikasi di file 02/04 TIDAK berubah retroaktif. Bank Mandiri Operasional saldo AWAL file ini = **479.030.000** (saldo akhir file 01/04).

## 1. Anggaran / Budget Kapitasi per Cabang (**Budgets**)

Budget disusun per cabang untuk target **peserta kapitasi terdaftar** Januari 2026 (dikonversi ke nilai rupiah dengan tarif tetap Rp 8.000/peserta), dibandingkan realisasi aktual (file 01 §1) — kasus ini SENGAJA dipilih karena kapitasi satu-satunya lini yang punya breakdown penuh per cabang (lihat file 01 §22, file 04 §2.2).

### 1.1 Target vs Realisasi Kapitasi per Cabang

| Cabang | Target Peserta | Budget (Target × 8.000) | Realisasi (Aktual, file 01) |                   Varian | Keterangan                                                                                                 |
| ------ | -------------: | ----------------------: | --------------------------: | -----------------------: | ---------------------------------------------------------------------------------------------------------- |
| JKP    |         19.000 |             152.000.000 |                 144.000.000 |       −8.000.000 (−5,3%) | Under-budget — target akuisisi peserta baru belum tercapai                                                 |
| BKS    |         14.000 |             112.000.000 |                 120.000.000 |   **+8.000.000 (+7,1%)** | **Over-budget** — akuisisi peserta BKS melampaui target                                                    |
| TGR    |         12.500 |             100.000.000 |                 100.000.000 |                        0 | **Pas persis** — kasus presisi (lihat §1.3)                                                                |
| DPK    |         11.000 |              88.000.000 |                  80.000.000 |       −8.000.000 (−9,1%) | Under-budget                                                                                               |
| BGR    |          8.000 |              64.000.000 |                  64.000.000 |                        0 | Pas persis                                                                                                 |
| BDG    |          6.500 |              52.000.000 |                  36.000.000 | **−16.000.000 (−30,8%)** | **Under-budget terbesar** — cabang baru (dibuka pertengahan 2025) belum capai target akuisisi peserta BPJS |

| Skenario                          | Detail                                                                                                                                                       | Hasil                                                                                                                                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — create budget 6 cabang  | `POST accounting/budgets/create {business_unit_id:<cabang>, period:"2026-01", chart_of_account_id:<4101>, amount:<budget sesuai tabel>}` per cabang (6 kali) | 201 tiap satu                                                                                                                                                                                                                      |
| Positif — Budget vs Actual report | `POST accounting/budgets/vs-actual {period:"2026-01"}`                                                                                                       | Menampilkan 6 baris varian PERSIS seperti tabel di atas — verifikasi tanda (+/−) benar, terutama BKS (over-budget, seharusnya beda visual dari under-budget) dan BDG (under-budget terbesar, cabang baru wajar belum capai target) |
| Negatif                           | Create budget untuk `business_unit_id` yang tidak ada di branch aktif                                                                                        | 422 `not_found_in_branch`                                                                                                                                                                                                          |
| Negatif                           | `amount` negatif                                                                                                                                             | 422 (budget pendapatan tidak masuk akal negatif — kalau sistem tidak menolak, catat sebagai gap validasi kecil, belum diverifikasi ke kode)                                                                                        |
| Netralisasi                       | `delete` budget test                                                                                                                                         | —                                                                                                                                                                                                                                  |

### 1.2 Total Varian Konsolidasi

```
Total Budget Kapitasi     = 152.000.000 + 112.000.000 + 100.000.000 + 88.000.000 + 64.000.000 + 52.000.000
                           = 568.000.000
Total Realisasi Kapitasi  = 544.000.000  (file 01 §1, TIDAK berubah — flat, tidak terikat kunjungan)
Varian Konsolidasi         = 544.000.000 − 568.000.000 = (24.000.000)  → Under-budget 4,2%
```

| Skenario | Detail                                                                           | Hasil                                                                        |
| -------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Positif  | Jumlahkan 6 varian cabang: (−8.000.000)+8.000.000+0+(−8.000.000)+0+(−16.000.000) | **(24.000.000)**, HARUS sama persis dengan varian konsolidasi manual di atas |

### 1.3 Budget Beban Tetap — Kasus "Pas Persis" (regression check presisi)

| Akun                               | Budget Januari 2026 | Realisasi (file 01) | Varian |
| ---------------------------------- | ------------------: | ------------------: | -----: |
| 5105 Beban Sewa Klinik/Gedung      |          66.000.000 |          66.000.000 |      0 |
| 5106 Beban Listrik, Air & Internet |          24.300.000 |          24.300.000 |      0 |

| Skenario | Detail                                                   | Hasil                                                                                                                                                                                                                                                                                      |
| -------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif  | Create 2 budget beban di atas, jalankan Budget vs Actual | Varian **PERSIS 0** untuk keduanya — kasus ini sengaja dipilih untuk menguji tidak ada pembulatan floating-point yang bikin varian muncul angka aneh seperti `0.00000001` atau `-1` — kalau muncul angka bukan-nol untuk kasus yang secara matematis harus 0, catat sebagai temuan presisi |

## 2. Aset Tetap (**Assets**)

### 2.1 Perolehan — Peralatan Medis & Lab (garis lurus)

| Skenario | Payload                                                                                                                                                                                                                                                                                                                                                                              | Hasil                                                                                                                                                 |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST fixed-assets/assets/create {name:"Peralatan Medis & Lab (USG Portable, EKG, Alat Lab Sederhana) - Batch 1", chart_of_account_id:<1201>, accumulated_depreciation_account_id:<1202>, depreciation_expense_account_id:<5107>, acquisition_date:"2026-02-02", acquisition_cost:96000000, salvage_value:0, useful_life_months:48, method:"straight_line", business_unit_id:<JKP>}` | 201 — jurnal perolehan Dr 1201 96.000.000 / Cr 1102 Bank Mandiri 96.000.000. Saldo Bank Mandiri turun jadi **383.030.000** (479.030.000 − 96.000.000) |
| Negatif  | `useful_life_months: 0`                                                                                                                                                                                                                                                                                                                                                              | 422                                                                                                                                                   |
| Negatif  | `acquisition_cost` negatif                                                                                                                                                                                                                                                                                                                                                           | 422                                                                                                                                                   |

### 2.2 Perolehan — Kendaraan Ambulans Klinik (saldo menurun)

| Skenario    | Payload                                                                                                                                                                                                                                                                                                                                                    | Hasil                                                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif     | `POST fixed-assets/assets/create {name:"Kendaraan Ambulans Klinik (Homecare & Rujukan Antar-Cabang)", chart_of_account_id:<1203>, accumulated_depreciation_account_id:<1204>, depreciation_expense_account_id:<5108>, acquisition_date:"2026-02-03", acquisition_cost:288000000, depreciation_rate:25, method:"declining_balance", business_unit_id:null}` | 201 — jurnal perolehan Dr 1203 288.000.000 / Cr 1102 288.000.000. Saldo Bank Mandiri turun jadi **95.030.000** (383.030.000 − 288.000.000) |
| Netralisasi | Simpan 2 aset ini — dipakai §2.3 (penyusutan) dan file 06 (saldo Bank Mandiri awal rekonsiliasi)                                                                                                                                                                                                                                                           |

## 3. Penyusutan Bulan Pertama (2026-02-28)

**Perhitungan manual:**

```
Peralatan Medis & Lab (garis lurus):
  Penyusutan bulanan = (96.000.000 − 0) / 48 bulan = 2.000.000/bulan

Kendaraan Ambulans (saldo menurun 25%/tahun):
  Nilai buku awal bulan 1 = 288.000.000 (belum ada penyusutan sebelumnya)
  Penyusutan bulan 1 = 288.000.000 × 25% ÷ 12 = 6.000.000
```

| Skenario                                         | Detail                                                                                                                          | Hasil                                                                                                                                                                                        |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — run penyusutan                         | `POST fixed-assets/assets/run-depreciation {period:"2026-02"}` (atau endpoint sejenis, per-aset kalau tidak ada endpoint batch) | 2 jurnal terposting: (a) Dr 5107 2.000.000 / Cr 1202 2.000.000, (b) Dr 5108 6.000.000 / Cr 1204 6.000.000 — total beban penyusutan Februari = **8.000.000**                                  |
| **Positif — kontra-aset tetap bersaldo negatif** | Cek Trial Balance akun 1202 dan 1204                                                                                            | 1202 = **−2.000.000**, 1204 = **−6.000.000** (mengurangi nilai Aset Tetap bruto di Neraca), BUKAN muncul sebagai saldo positif menambah Aset — regression check yang sama seperti file 00 §3 |
| Positif — nilai buku bersih                      | Hitung manual: `(96.000.000 − 2.000.000) + (288.000.000 − 6.000.000)`                                                           | Nilai buku bersih Aset Tetap akhir Februari = 94.000.000 + 282.000.000 = **376.000.000**                                                                                                     |
| Negatif                                          | Run penyusutan periode yang SAMA 2x                                                                                             | Ditolak/idempoten (tidak boleh dobel-posting penyusutan bulan yang sama) — kalau ternyata bisa dobel, catat sebagai temuan serius                                                            |

## 4. (Opsional) Pelepasan Aset — TIDAK Dieksekusi di Suite Ini

| Skenario    | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Netralisasi | Berbeda dari suite klinik gigi yang mendemonstrasikan pelepasan aset (§2.4), suite ini SENGAJA tidak mengeksekusi disposal supaya kedua aset (Peralatan Medis & Kendaraan Ambulans) tetap aktif untuk perhitungan rekonsiliasi bank di file 06. Kalau ingin menguji `fixed-assets/disposals/create`, gunakan endpoint yang BENAR: `fixed-assets/disposals/{action}` (BUKAN `finance/fixed-assets/*`) — payload minimal `{id:<asset_id>, disposal_date, disposal_proceeds}`, bandingkan proceeds vs nilai buku saat pelepasan untuk hitung untung/rugi pelepasan (akun "Untung/Rugi Pelepasan Aset" BELUM ada di Chart of Accounts file 00, tambahkan dulu kalau mau eksekusi skenario ini) |

## Referensi Silang

- File [`04-laporan-keuangan-konsolidasi-dan-per-cabang.id.md`](./04-laporan-keuangan-konsolidasi-dan-per-cabang.id.md) — saldo Bank Mandiri awal file ini (479.030.000)
- File [`06-rekonsiliasi-bank-dan-ppn.id.md`](./06-rekonsiliasi-bank-dan-ppn.id.md) — saldo Bank Mandiri akhir file ini (95.030.000) jadi saldo awal rekonsiliasi
- Endpoint Fixed Assets yang BENAR: `fixed-assets/assets/{action}` dan `fixed-assets/disposals/{action}` — BUKAN `finance/fixed-assets/*`
- Suite klinik gigi [`../accounting-klinik-gigi/05-anggaran-dan-aset-tetap.id.md`](../accounting-klinik-gigi/05-anggaran-dan-aset-tetap.id.md) — pola dasar yang direplikasi strukturnya
