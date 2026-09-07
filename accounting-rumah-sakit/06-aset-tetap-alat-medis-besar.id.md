---
title: (Rumah Sakit) — 06. Aset Tetap & Alat Medis Besar
category: accounting-rumah-sakit
description: Penyusutan bulanan 4 aset medis besar warisan (Gedung, CT-Scan, MRI, Radiologi — via jurnal manual, BUKAN modul fixed-assets, keterbatasan migrasi data yang disengaja), akuisisi Ambulans baru via modul fixed-assets (garis lurus), dan pelepasan Ambulans untuk upgrade (rugi pelepasan). Endpoint yang benar: fixed-assets/assets/* dan fixed-assets/disposals/* — BUKAN finance/fixed-assets/*.
visibility: internal
---

# 06. Aset Tetap & Alat Medis Besar

> Prasyarat: file [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) sudah selesai. **Transaksi di file ini sengaja bertanggal 2026-02-05 dan seterusnya** — SETELAH rentang Januari yang dipakai file 01-05 — supaya Trial Balance/Neraca yang sudah diverifikasi di file 02/04 TIDAK berubah retroaktif. Saldo Bank BCA Operasional AWAL file ini = **750.700.000** (saldo akhir file 01/02).
>
> **⚠️ Endpoint yang BENAR**: **Assets — `{list|show|create|update|delete|calculate-depreciation|run-depreciation}`** dan **Disposals — `{list|show|create}`** — **BUKAN** `finance/fixed-assets/*`.

## 1. Desain Khusus Suite Ini — Aset Warisan (Legacy) vs Aset Baru di Modul `fixed-assets`

**Konteks realistis**: RS Sentosa Medika Utama sudah beroperasi >10 tahun sebelum migrasi ke sistem ERP ini. Saat migrasi, saldo 4 aset medis besar (Gedung, CT-Scan, MRI, Peralatan Radiologi) HANYA dicatat di **level akun** lewat `chart-of-accounts-balances` (file 00 §9.4) — **TIDAK** didaftarkan sebagai baris individual di `fixed-assets/assets`. Ini keterbatasan migrasi data yang umum terjadi di implementasi ERP nyata (histori detail per-unit tidak selalu tersedia/valid untuk dimigrasikan).

Konsekuensinya, penyusutan bulanan untuk 4 aset warisan ini **dicatat via jurnal manual** (`accounting/journals/create`), BUKAN via `fixed-assets/assets/run-depreciation` (karena tidak ada baris `fixed-assets/assets` yang merepresentasikannya). Aset BARU (Ambulans, §3) didaftarkan penuh via modul `fixed-assets/assets` dan pakai `run-depreciation` sungguhan — mendemonstrasikan bahwa KEDUA jalur (manual & modul) harus menghasilkan efek GL yang setara (Dr Beban Penyusutan / Cr Akumulasi Penyusutan), sesuatu yang belum pernah dites eksplisit di 4 suite lain (yang semua aset tetapnya mulai dari nol via modul).

| Skenario                                          | Detail                                               | Hasil                                                                                                                                                                                                                                                                                                                                                                                           | Label temuan                                                                                                                                               |
| ------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — gap arsitektur yang disengaja diuji** | Cek `fixed-assets/assets/list` SEBELUM §3 dieksekusi | Kosong (0 baris) — MESKIPUN Trial Balance/Neraca sudah menunjukkan Aset Tetap net 58.000.000.000 dari 4 akun warisan. Ini BUKAN bug, tapi keterbatasan desain yang harus dipahami staf keuangan: laporan `fixed-assets/assets/list` TIDAK bisa dipakai sebagai sumber kebenaran tunggal nilai Aset Tetap di Neraca untuk RS yang migrasi sistem — Neraca (dari GL) tetap sumber kebenaran utama | Belum diverifikasi ke kode — kemungkinan besar ini memang perilaku standar tanpa fitur import histori aset, dicatat sebagai catatan keterbatasan bukan bug |

## 2. Penyusutan Bulanan Aset Warisan — Februari 2026 (jurnal manual, 2026-02-28)

**Perhitungan manual:**

```
Gedung Rumah Sakit (garis lurus, cost 40.000.000.000, useful_life 200 bulan):
  Penyusutan bulanan = 40.000.000.000 / 200 = 200.000.000/bulan

Mesin CT-Scan (garis lurus, cost 12.000.000.000, useful_life 96 bulan):
  Penyusutan bulanan = 12.000.000.000 / 96 = 125.000.000/bulan

Mesin MRI (garis lurus, cost 18.000.000.000, useful_life 120 bulan):
  Penyusutan bulanan = 18.000.000.000 / 120 = 150.000.000/bulan

Peralatan Radiologi (saldo menurun 20%/tahun):
  NBV awal Februari = 5.000.000.000 − 2.000.000.000 = 3.000.000.000
  Penyusutan Februari = 3.000.000.000 × 20% ÷ 12 = 50.000.000
```

| Baris | Akun                                          |       Debit |      Kredit |
| ----- | --------------------------------------------- | ----------: | ----------: |
| 1     | 5106 Beban Penyusutan Gedung                  | 200.000.000 |             |
| 2     | 1202 Akumulasi Penyusutan Gedung              |             | 200.000.000 |
| 3     | 5107 Beban Penyusutan Mesin CT-Scan           | 125.000.000 |             |
| 4     | 1204 Akumulasi Penyusutan Mesin CT-Scan       |             | 125.000.000 |
| 5     | 5108 Beban Penyusutan Mesin MRI               | 150.000.000 |             |
| 6     | 1206 Akumulasi Penyusutan Mesin MRI           |             | 150.000.000 |
| 7     | 5109 Beban Penyusutan Peralatan Radiologi     |  50.000.000 |             |
| 8     | 1208 Akumulasi Penyusutan Peralatan Radiologi |             |  50.000.000 |

Total Debit = Total Kredit = **525.000.000** ✓.

| Skenario                                                              | Detail                                                   | Hasil                                                                              |
| --------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Positif                                                               | Create + post jurnal 8 baris di atas                     | 201 create, 200 post                                                               |
| **Positif — kontra-aset tetap bersaldo negatif (4 pasang sekaligus)** | Cek Trial Balance 1202/1204/1206/1208 setelah jurnal ini | 1202=−8.200.000.000, 1204=−4.125.000.000, 1206=−3.150.000.000, 1208=−2.050.000.000 |

## 3. Akuisisi Aset Baru — Kendaraan Ambulans (via modul **Assets**, 2026-02-05)

**Prasyarat: tambahkan 2 akun baru ke Chart of Accounts sebelum mulai** — `1209 Kendaraan Ambulans` dan `1210 Akumulasi Penyusutan Kendaraan Ambulans` (tipe Aset Tetap). Akun ini belum ada di file 00 karena ambulans baru dibeli mulai file ini (pola yang sama dengan penambahan akun mid-suite di suite klinik gigi/`5208`).

| Skenario    | Payload                                                                                                                                                                                                                                                                                                                                             | Hasil                                                                                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `POST fixed-assets/assets/create {name:"Ambulans Unit 1 (Isuzu ELF Modifikasi)", chart_of_account_id:<1209>, accumulated_depreciation_account_id:<1210>, depreciation_expense_account_id:<5110>, acquisition_date:"2026-02-05", acquisition_cost:660000000, salvage_value:0, useful_life_months:60, method:"straight_line", business_unit_id:null}` | 201 — jurnal perolehan otomatis: Dr 1209 660.000.000 / Cr 1102 Bank BCA 660.000.000. Saldo Bank BCA turun jadi **90.700.000** (750.700.000 − 660.000.000) |
| Negatif     | `useful_life_months: 0`                                                                                                                                                                                                                                                                                                                             | 422                                                                                                                                                       |
| Negatif     | `acquisition_cost` negatif                                                                                                                                                                                                                                                                                                                          | 422                                                                                                                                                       |
| Netralisasi | Simpan aset ini — dipakai §4 (penyusutan) dan §5 (pelepasan)                                                                                                                                                                                                                                                                                        |

## 4. Penyusutan Ambulans via Modul (Februari + Maret 2026)

```
Penyusutan bulanan (garis lurus) = (660.000.000 − 0) / 60 bulan = 11.000.000/bulan
```

| Skenario                                                                | Detail                                                                                                                                                                                                       | Hasil                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — run Februari                                                  | `POST fixed-assets/assets/run-depreciation {period:"2026-02"}` (atau per-asset kalau tidak ada endpoint batch)                                                                                               | Jurnal terposting: Dr 5110 Beban Penyusutan Kendaraan Ambulans 11.000.000 / Cr 1210 Akumulasi Penyusutan Ambulans 11.000.000                                                                                                                                                                                         |
| Positif — run Maret                                                     | `POST fixed-assets/assets/run-depreciation {period:"2026-03"}`                                                                                                                                               | Jurnal sama, 11.000.000 lagi — NBV Ambulans akhir Maret (sebelum pelepasan §5) = 660.000.000 − 22.000.000 = **638.000.000**                                                                                                                                                                                          |
| Negatif                                                                 | Run penyusutan periode yang SAMA 2x                                                                                                                                                                          | Ditolak/idempoten — kalau ternyata bisa dobel, catat sebagai temuan serius                                                                                                                                                                                                                                           |
| **Positif — bandingkan dengan penyusutan aset warisan Maret**           | Buat juga jurnal manual penyusutan Maret untuk 4 aset warisan (pola sama §2, kecuali Radiologi yang recalculate dari NBV baru: 3.000.000.000−50.000.000=2.950.000.000 × 20%÷12 = **49.166.667**, dibulatkan) | Total penyusutan Maret gabungan (warisan 200.000.000+125.000.000+150.000.000+49.166.667=524.166.667) + Ambulans modul (11.000.000) = **535.166.667** — verifikasi KEDUA jalur (manual & modul) sama-sama muncul di `accounting/general-ledger` akun 51xx terkait, TIDAK ada yang "hilang" karena beda sumber posting |
| **Positif — presisi pembulatan declining balance (kasus presisi baru)** | Cek angka 49.166.667 (Radiologi Maret) di GL — hasil pembagian 2.950.000.000×20%÷12 = 49.166.666,6667                                                                                                        | Verifikasi sistem membulatkan KONSISTEN (mis. selalu ke rupiah terdekat) dan TIDAK menyimpan pecahan desimal yang nanti terakumulasi jadi selisih di Trial Balance — ini tema presisi kunci suite ini pada skala nilai besar, beda dari suite klinik gigi yang semua angkanya sudah bulat dari awal                  |

## 5. Pelepasan Ambulans untuk Upgrade (**Disposals**, 2026-03-31)

**Skenario**: Ambulans Unit 1 dilepas (dijual) untuk upgrade ke model yang lebih baru — penggantian unit baru direncanakan kuartal berikutnya (di luar scope suite ini, fokus pengujian di sini murni endpoint disposal & perhitungan rugi/laba pelepasan).

```
NBV Ambulans saat pelepasan (akhir Maret, setelah §4) = 660.000.000 − 22.000.000 = 638.000.000
Proceeds penjualan (harga jual unit lama ke dealer)    = 620.000.000
Rugi Pelepasan Aset Tetap                              = 638.000.000 − 620.000.000 = 18.000.000
```

**Prasyarat tambahan: tambahkan 1 akun baru** — `5116 Rugi/Laba Pelepasan Aset Tetap` (tipe Beban, saldo bisa negatif kalau untung — belum ada di file 00 karena baru relevan mulai skenario pelepasan ini, pola yang sama dengan suite klinik gigi §2.4 yang juga menemukan akun ini belum ada di COA awal).

| Skenario                                               | Payload                                                                                                                    | Hasil                                                                                                                                                                                                                    |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif — dispose                                      | `POST fixed-assets/disposals/create {asset_id:<Ambulans Unit 1>, disposal_date:"2026-03-31", disposal_proceeds:620000000}` | 201 — jurnal pelepasan: Dr 1102 Bank BCA 620.000.000, Dr 1210 Akumulasi Penyusutan Ambulans 22.000.000, Dr 5116 Rugi Pelepasan Aset Tetap 18.000.000 / Cr 1209 Kendaraan Ambulans 660.000.000. Total Dr=Cr=660.000.000 ✓ |
| Positif — status aset setelah dispose                  | `GET fixed-assets/assets/show {id:<Ambulans Unit 1>}`                                                                      | Status berubah jadi `disposed` (atau field sejenis) — TIDAK boleh lagi muncul di `run-depreciation` bulan berikutnya                                                                                                     |
| Negatif                                                | Dispose aset yang SAMA 2x                                                                                                  | Ditolak — sudah disposed                                                                                                                                                                                                 |
| Negatif                                                | `disposal_date` SEBELUM `acquisition_date`                                                                                 | 422                                                                                                                                                                                                                      |
| **Positif — verifikasi saldo Bank BCA akhir file ini** | Setelah §3 (−660.000.000) dan §5 (+620.000.000)                                                                            | Saldo Bank BCA = 90.700.000 + 620.000.000 = **710.700.000** — jadi saldo awal rekonsiliasi file 07                                                                                                                       |

## 6. Nilai Buku Bersih Aset Tetap Akhir Maret 2026 (setelah semua transaksi file ini)

| Aset                |              Gross | Akumulasi Penyusutan |  Nilai Buku Bersih |
| ------------------- | -----------------: | -------------------: | -----------------: |
| Gedung Rumah Sakit  |     40.000.000.000 |        8.400.000.000 |     31.600.000.000 |
| Mesin CT-Scan       |     12.000.000.000 |        4.250.000.000 |      7.750.000.000 |
| Mesin MRI           |     18.000.000.000 |        3.300.000.000 |     14.700.000.000 |
| Peralatan Radiologi |      5.000.000.000 |        2.099.166.667 |      2.900.833.333 |
| Kendaraan Ambulans  |       0 (disposed) |         0 (disposed) |                  0 |
| **TOTAL**           | **75.000.000.000** |   **18.049.166.667** | **56.950.833.333** |

| Skenario                           | Detail                                                                                                                | Hasil                                                                                                                                         |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — verifikasi Trial Balance | Bandingkan total NBV di atas dengan Trial Balance `accounting/general-ledger/trial-balance {as_of_date:"2026-03-31"}` | Total Aset Tetap net HARUS **56.950.833.333** persis — kalau beda, ada jurnal penyusutan yang salah posting atau pelepasan yang tidak lengkap |

## Referensi Silang

- File [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) — saldo Bank BCA awal file ini (750.700.000)
- File [`07-rekonsiliasi-bank-multi-rekening-dan-ppn.id.md`](./07-rekonsiliasi-bank-multi-rekening-dan-ppn.id.md) — saldo Bank BCA akhir file ini (710.700.000) jadi saldo awal rekonsiliasi
- Suite klinik gigi [`../accounting-klinik-gigi/05-anggaran-dan-aset-tetap.id.md`](../accounting-klinik-gigi/05-anggaran-dan-aset-tetap.id.md) — pola dasar akuisisi/penyusutan/pelepasan yang direplikasi, dengan tambahan kasus baru "aset warisan tanpa baris modul" yang belum pernah dites di suite manapun
- `fixed-assets/assets/*`, `fixed-assets/disposals/*` — endpoint yang BENAR (bukan `finance/fixed-assets/*`)
