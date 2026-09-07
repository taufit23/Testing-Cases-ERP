---
title: (Klinik Gigi) — 02. General Ledger & Trial Balance
category: accounting-klinik-gigi
description: Verifikasi Detail Ledger, Summary by Account (dengan filter dimensi cabang), dan Trial Balance terhadap angka yang sudah dihitung manual di file 01 — total 20 transaksi, harus cocok persis sampai ke rupiah terakhir.
visibility: internal
---

# 02. General Ledger & Trial Balance

> Prasyarat: file [`01-jurnal-manual-transaksi-harian-klinik.id.md`](./01-jurnal-manual-transaksi-harian-klinik.id.md) sudah selesai — 20 transaksi (T1-T20, termasuk 1 reversal di T18) sudah terposting.

## 1. Trial Balance (**General Ledger — `trial-balance`**)

| Skenario                          | Detail                                                                                                                                           | Hasil                                                                                                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Positif — trial balance lengkap   | `POST accounting/general-ledger/trial-balance {as_of_date:"2026-01-28"}` (atau tanpa filter tanggal kalau endpoint defaultnya "sampai hari ini") | `total_debit = total_credit = 215.433.000` (lihat §Rekonsiliasi Akhir file 01)                             |
| **Positif — cocokkan tiap baris** | Bandingkan tiap akun di response dengan tabel di bawah                                                                                           | Semua HARUS persis sama — kalau ada 1 akun beda, itu bug posting atau transaksi file 01 yang belum lengkap |

**Tabel acuan (WAJIB cocok persis dengan hasil endpoint):**

| Kode | Akun                                    |             Saldo (Debit/Kredit) |
| ---- | --------------------------------------- | -------------------------------: |
| 1101 | Kas Kecil Klinik (Harian)               |                     Dr 5.338.000 |
| 1102 | Bank BCA Operasional                    |                   Dr 131.713.000 |
| 1103 | Piutang Pasien — BPJS & Asuransi        |                    Dr 29.380.000 |
| 1104 | Persediaan Bahan Habis Pakai (BHP) Gigi |                    Dr 27.470.000 |
| 1105 | PPN Masukan                             |                       Dr 550.000 |
| 1201 | Unit Dental Chair & Peralatan           |        Dr 0 (belum ada, file 05) |
| 1202 | Akumulasi Penyusutan Unit Dental Chair  |           0 (belum ada, file 05) |
| 1203 | Kendaraan Operasional Klinik            |        Dr 0 (belum ada, file 05) |
| 1204 | Akumulasi Penyusutan Kendaraan          |           0 (belum ada, file 05) |
| 2101 | Utang Dagang — Supplier Bahan Gigi      |                    Cr 16.850.000 |
| 2102 | PPN Keluaran                            |                        Cr 33.000 |
| 2103 | Utang Komisi Dokter                     |                     Cr 6.750.000 |
| 2104 | Utang PPh 21 Karyawan                   |                     Cr 2.300.000 |
| 3101 | Modal Pemilik                           |                   Cr 181.350.000 |
| 3102 | Laba Ditahan                            |         Cr 0 (belum tutup tahun) |
| 4101 | Pendapatan Jasa Gigi Umum               |                     Cr 3.550.000 |
| 4102 | Pendapatan Jasa Ortodonti               |                     Cr 2.500.000 |
| 4103 | Pendapatan Jasa Estetika Gigi           |                     Cr 1.800.000 |
| 4104 | Pendapatan Penjualan Produk Ritel       |                       Cr 300.000 |
| 5101 | Beban Komisi Dokter                     |                     Dr 2.487.000 |
| 5102 | Beban BHP Gigi                          |                       Dr 730.000 |
| 5201 | Beban Sewa Klinik                       |                     Dr 6.000.000 |
| 5202 | Beban Gaji Karyawan Non-Dokter          |                     Dr 9.000.000 |
| 5203 | Beban Listrik & Air                     |                     Dr 2.750.000 |
| 5204 | Beban Penyusutan Unit Dental Chair      |        Dr 0 (belum ada, file 05) |
| 5205 | Beban Penyusutan Kendaraan              |        Dr 0 (belum ada, file 05) |
| 5206 | Beban Selisih Kas Kasir Harian          |                        Dr 15.000 |
| 5207 | Beban Sterilisasi & Limbah Medis        | Dr 0 (net 0 setelah reverse T18) |

| Total Debit | Total Kredit |
| ----------: | -----------: |
| 215.433.000 |  215.433.000 |

| Skenario                                     | Detail                                                                                                                                       | Hasil                                                                                                                                                                                                                                                                               | Label temuan               |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **Positif — dua implementasi trial balance** | Ada JUGA `reports/trial-balance` (kalau tersedia di `ReportController`) selain `accounting/general-ledger/trial-balance` — jalankan keduanya | Harus hasilnya identik (sama-sama baca `general_ledgers`). Kalau beda, itu temuan konsistensi — belum diverifikasi ke kode apakah keduanya benar-benar 1 sumber data yang sama, laporkan hasil aktual apa adanya                                                                    | Belum diverifikasi ke kode |
| Negatif                                      | `as_of_date` sebelum ada transaksi apapun (mis. `2025-12-31`)                                                                                | Semua saldo 0 KECUALI belum ada saldo awal juga (saldo awal ter-tanggal hari jurnal diposting, ingat catatan file 00 §9 soal opening balance bertanggal "hari ini saat tombol ditekan") — perilaku ini sudah dites detail di suite retail/manufaktur, regression check saja di sini |

## 2. Detail Ledger per Akun (**General Ledger**)

### 2.1 Kas Kecil Klinik (1101) — akun paling sering "disentuh", cocok untuk uji urutan & akurasi baris

| Skenario                                         | Detail                                                                                                                                             | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                          | `POST accounting/general-ledger {chart_of_account_id:<1101>, date_from:"2026-01-01", date_to:"2026-01-28"}`                                        | 9 baris mutasi (di luar saldo awal): +750.000(T1), +2.500.000(T3), +333.000(T4), −2.000.000(T5), +1.800.000(T8), −15.000(T10), +920.000(T13), −450.000(T18a), +450.000(reverse T18a), −450.000(T18b), −1.500.000(T20) — **11 baris kalau reversal dihitung 1 baris terpisah**, urut kronologis sesuai `date`+waktu create. Saldo berjalan (running balance) akhir baris terakhir = **5.338.000**, cocok §Rekonsiliasi Akhir file 01 |
| **Positif — running balance tiap baris presisi** | Cek 3 baris pertama saja secara manual: Saldo awal 3.000.000 → +750.000 (T1) = 3.750.000 → +2.500.000 (T3) = 6.250.000 → +333.000 (T4) = 6.583.000 | Kalau `running_balance` di response beda dari perhitungan manual di baris manapun, itu bug akumulasi — prioritas tinggi karena inilah tema utama suite ini                                                                                                                                                                                                                                                                          |

### 2.2 Utang Komisi Dokter (2103) — siklus akrual penuh, saldo kembali ke awal

| Skenario                                                              | Detail                                                                                                      | Hasil                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                               | `POST accounting/general-ledger {chart_of_account_id:<2103>, date_from:"2026-01-01", date_to:"2026-01-28"}` | 8 baris: +300.000(T1), +360.000(T2), +625.000(T3), −1.285.000(T7), +630.000(T8), +368.000(T13), +204.000(T14), −1.202.000(T16) — saldo awal 6.750.000, saldo akhir **6.750.000 lagi (persis sama)** — bukan kebetulan, tapi karena SEMUA akrual periode ini sudah lunas dibayar (lihat catatan T16 di file 01) |
| **Positif — bukti "saldo balik ke awal" BUKAN "tidak ada aktivitas"** | Pastikan cek jumlah BARIS mutasi (8 baris, bukan 0 baris) meski saldo akhir = saldo awal                    | Kalau ada bug yang membuat GL "menghilangkan" pasangan mutasi yang saling menutup (net 0), harusnya tetap 8 baris tercatat, bukan 0 — verifikasi ini bukan cuma percaya saldo akhir yang kebetulan sama                                                                                                        |

## 3. Summary by Account dengan Filter Dimensi Cabang (Business Unit)

| Skenario                                                     | Detail                                                                                                                 | Hasil                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif — filter KG                                          | `POST accounting/general-ledger/summary` (atau endpoint sejenis) dengan filter `business_unit_id:<KG>`, akun 4101+4104 | Pendapatan tercatat dengan tag KG: T1 750.000 (4101) + T4 300.000 (4104) + T13 920.000 (4101) = **1.970.000** — cek response persis angka ini                                                                                                                                                                                              |
| Positif — filter BSD                                         | Sama, `business_unit_id:<BSD>`, akun 4101+4102+4103                                                                    | T2 1.200.000 (4101) + T8 1.800.000 (4103) + T14 680.000 (4101) = **3.680.000**                                                                                                                                                                                                                                                             |
| Positif — filter BKS                                         | Sama, `business_unit_id:<BKS>`, akun 4102                                                                              | T3 2.500.000 (4102, ortodonti DP) = **2.500.000**                                                                                                                                                                                                                                                                                          |
| **Positif — transaksi TANPA dimensi cabang tetap harus ada** | Cek total keseluruhan (tanpa filter `business_unit_id`) akun 4101+4102+4103+4104                                       | Harus tetap **8.150.000** (3.550.000+2.500.000+1.800.000+300.000) — transaksi seperti T9 (pelunasan BPJS) dan T15 (listrik gabungan 3 cabang) sengaja TIDAK ditag `business_unit_id`, verifikasi filter dimensi tidak diam-diam MENGHILANGKAN transaksi tanpa tag dari total keseluruhan, hanya menyembunyikannya dari hasil YANG DIFILTER |
| Negatif                                                      | `business_unit_id` yang tidak ada di branch aktif                                                                      | 422 `not_found_in_branch`                                                                                                                                                                                                                                                                                                                  |

## 4. Verifikasi Silang Persamaan Akuntansi Dasar

| Skenario    | Detail                                                           | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | Aset = Liabilitas + Ekuitas + (Pendapatan − Beban) berjalan      | `194.451.000 = 25.933.000 + 181.350.000 + (8.150.000 − 20.982.000)` → `194.451.000 = 25.933.000 + 181.350.000 + (−12.832.000)` → `194.451.000 = 194.451.000` ✓ — klinik sedang **rugi berjalan** 12.832.000 di 4 minggu pertama ini (wajar, banyak beban tetap bulanan seperti sewa/gaji dibebankan penuh di awal periode sementara pendapatan baru terkumpul dari transaksi kecil harian — bukan indikasi bug, murni timing) |
| Netralisasi | — (tidak ada state yang perlu dibalikkan, hanya query read-only) |

## Referensi Silang

- File [`01-jurnal-manual-transaksi-harian-klinik.id.md`](./01-jurnal-manual-transaksi-harian-klinik.id.md) — sumber seluruh angka acuan di file ini
- File [`04-laporan-keuangan.id.md`](./04-laporan-keuangan.id.md) — Neraca & Laba Rugi memakai angka Trial Balance yang sama persis
