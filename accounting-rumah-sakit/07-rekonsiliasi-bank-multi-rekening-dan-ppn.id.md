---
title: (Rumah Sakit) — 07. Rekonsiliasi Bank Multi-Rekening & Laporan PPN
category: accounting-rumah-sakit
description: Rekonsiliasi 2 rekening bank sekaligus — Bank BCA Operasional (kompleks, 1 item harus "ditemukan sendiri", transfer BPJS nyasar ke rekening umum) dan Bank Mandiri Khusus BPJS (sederhana, admin fee saja) — plus laporan PPN Keluaran/Masukan yang SELEKTIF hanya dari lini obat OTC. Penutup suite.
visibility: internal
---

# 07. Rekonsiliasi Bank Multi-Rekening & Laporan PPN

> Prasyarat: file [`06-aset-tetap-alat-medis-besar.id.md`](./06-aset-tetap-alat-medis-besar.id.md) sudah selesai. Saldo buku per 2026-03-31: Bank BCA Operasional (1102) = **710.700.000**, Bank Mandiri Khusus BPJS (1103) = **3.300.000.000** (tidak ada transaksi baru ke 1103 sejak file 01).
>
> **Kenapa 2 rekening di file ini (kasus baru, belum pernah dites di suite lain)**: RS besar SELALU punya rekening khusus terverifikasi untuk pencairan BPJS (`1103`), terpisah dari rekening operasional umum (`1102`) — dua rekening ini punya profil risiko rekonsiliasi yang beda: `1102` menampung banyak transaksi kecil-besar campuran (rawan salah input), `1103` relatif "bersih" (hanya menampung pencairan BPJS resmi, tapi tetap perlu dicek biaya administrasi bank).

## 1. Rekonsiliasi Bank BCA Operasional — kompleks, 1 item harus ditemukan sendiri

### 1.1 Transaksi tambahan Maret yang memicu selisih (buat dulu sebelum rekonsiliasi)

| #   | Tanggal    | Deskripsi                                                                                                                                                                                   | Jurnal                                                                                                     |                                             Nilai |
| --- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------: |
| a   | 2026-03-28 | Setoran kas kecil ke Bank BCA, sudah dicatat di buku tapi baru kliring rekening koran bulan berikutnya (setoran dalam perjalanan)                                                           | Dr 1102 Bank BCA 5.000.000 / Cr 1101 Kas Kecil 5.000.000                                                   |                                         5.000.000 |
| b   | 2026-03-27 | Pembayaran ke supplier obat (cek), belum sempat dicairkan sampai tanggal statement (cek belum cair)                                                                                         | Dr 2101 Utang Dagang Supplier 40.000.000 / Cr 1102 Bank BCA 40.000.000                                     |                                        40.000.000 |
| c   | 2026-03-25 | Pembayaran sebagian fee dokter spesialis — **staf salah input** Rp15.000.000 padahal nominal sebenarnya di rekening koran Rp51.000.000 (kesalahan transposisi/salah baca dokumen otorisasi) | Dr 2103 Utang Fee Dokter Spesialis 15.000.000 / Cr 1102 Bank BCA 15.000.000 (SALAH, seharusnya 51.000.000) | 15.000.000 (tercatat) vs 51.000.000 (aktual bank) |

Setelah (a)+(b)+(c) tercatat, saldo buku 1102 = 710.700.000 + 5.000.000 − 40.000.000 − 15.000.000 = **660.700.000**. Biaya admin bank Rp150.000 BELUM dicatat sama sekali di buku (baru diketahui dari rekening koran).

### 1.2 Rekening Koran (Bank Statement) per 2026-03-31

**Saldo rekening koran = Rp 734.550.000** (data dari bank, dianggap sudah benar/final).

### 1.3 Perhitungan Rekonsiliasi (WAJIB dihitung manual dulu sebelum eksekusi endpoint)

```
SISI BANK
  Saldo Rekening Koran (2026-03-31)                734.550.000
  + Setoran dalam perjalanan (butir a)                5.000.000
  − Cek/pembayaran belum cair (butir b)             (40.000.000)
  = Saldo Bank Disesuaikan                          699.550.000

SISI BUKU
  Saldo Buku (1102, setelah butir a+b+c)             660.700.000
  − Biaya Administrasi Bank (belum dicatat)             (150.000)
  − Koreksi salah input butir c (15.000.000 → 51.000.000,
    kurang dicatat 36.000.000 sebagai pengeluaran)     (36.000.000)
  = Saldo Buku Disesuaikan (SEMENTARA)               624.550.000
```

**⚠️ TIDAK BALANCE pada percobaan pertama** (699.550.000 ≠ 624.550.000, selisih **75.000.000**) — INI DISENGAJA. Staf rekonsiliasi harus MENYELIDIKI mutasi bank sebesar 75.000.000 yang tidak ada di buku sama sekali.

| Skenario                                                                                       | Detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **Positif — temukan item hilang (skill utama rekonsiliasi, kasus baru: BPJS nyasar rekening)** | Untuk keperluan test case ini, anggap ditemukan: **transfer masuk otomatis dari BPJS Kesehatan Rp75.000.000 yang SALAH masuk ke rekening operasional umum (1102) alih-alih rekening khusus BPJS (1103)** — verifikator BPJS keliru memasukkan nomor rekening tujuan saat pencairan sisa klaim (khas human-error di sisi BPJS, bukan kesalahan RS), belum pernah dijurnal sama sekali                                                                                                     | Buat jurnal baru: `Dr 1102 Bank BCA 75.000.000 / Cr 1105 Piutang Klaim BPJS Kesehatan 75.000.000`, tanggal 2026-03-30. **Catatan operasional (di luar sistem)**: RS SEHARUSNYA memindahbukukan dana ini ke rekening khusus BPJS (1103) sesuai kebijakan internal, tapi pemindahan itu adalah transaksi bank terpisah (transfer antar rekening sendiri) — di luar scope pembuktian rekonsiliasi kali ini, cukup dicatat sebagai penerimaan piutang yang sah dulu |
| Positif — rekonsiliasi ulang setelah item ditemukan                                            | Saldo Buku Disesuaikan = 624.550.000 + 75.000.000 = **699.550.000**                                                                                                                                                                                                                                                                                                                                                                                                                      | **COCOK PERSIS dengan Saldo Bank Disesuaikan (699.550.000) → rekonsiliasi BALANCE**                                                                                                                                                                                                                                                                                                                                                                             |
| Positif — eksekusi endpoint                                                                    | `POST finance/bank-reconciliations/create {bank_account_id:<Bank BCA>, statement_date:"2026-03-31", statement_balance:734550000, book_balance:710700000}` (nilai `book_balance` sebelum butir a/b/c kalau kontrak endpoint minta saldo AWAL periode, sesuaikan dengan kontrak aktual) lalu tambahkan item penyesuai (setoran dalam perjalanan +5.000.000, cek belum cair −40.000.000, biaya admin −150.000, koreksi transposisi −36.000.000, transfer BPJS nyasar ditemukan +75.000.000) | 201, status akhir `is_balanced:true`/`reconciled_balance` sama antara sisi bank & buku (699.550.000)                                                                                                                                                                                                                                                                                                                                                            |
| Negatif                                                                                        | Submit rekonsiliasi TANPA menemukan item 75.000.000 (selisih dibiarkan tidak dijelaskan)                                                                                                                                                                                                                                                                                                                                                                                                 | Endpoint SEHARUSNYA menolak/menandai `is_balanced:false` selama ada selisih — kalau sistem izinkan "selesai" walau selisih belum nol, itu gap kontrol. Belum diverifikasi ke kode                                                                                                                                                                                                                                                                               | Belum diverifikasi ke kode |
| Netralisasi                                                                                    | Pastikan saldo GL akun 1102 aktual = **699.550.000** setelah semua jurnal koreksi di atas (a, b sudah terjurnal di §1.1; admin fee, koreksi transposisi, dan penemuan BPJS harus dijurnal terpisah sesuai temuan di atas)                                                                                                                                                                                                                                                                |

## 2. Rekonsiliasi Bank Mandiri — Rekening Khusus BPJS — sederhana, kontras dengan §1

### 2.1 Rekening Koran per 2026-03-31

**Saldo rekening koran = Rp 3.299.500.000** — HANYA selisih 1 item: biaya administrasi bulanan rekening khusus BPJS Rp500.000 yang belum dicatat di buku.

### 2.2 Perhitungan Rekonsiliasi

```
Saldo Buku (1103)                     3.300.000.000
− Biaya Administrasi Bank (belum dicatat)  (500.000)
= Saldo Buku Disesuaikan             3.299.500.000

Saldo Rekening Koran                  3.299.500.000
```

**BALANCE LANGSUNG pada percobaan pertama** — kontras tegas dengan §1 (yang butuh investigasi 1 item hilang). Ini demonstrasi bahwa rekening khusus BPJS, karena fungsinya tunggal (hanya menampung pencairan resmi BPJS), jauh lebih mudah direkonsiliasi dibanding rekening operasional umum yang menampung ratusan jenis transaksi harian.

| Skenario                                                                          | Detail                                                                                                                                                                                                         | Hasil                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                                           | Jurnal koreksi: `Dr 5112 Beban Administrasi Bank 500.000 / Cr 1103 Bank Mandiri BPJS 500.000`, tanggal 2026-03-31                                                                                              | Saldo 1103 akhir = **3.299.500.000**                                                                                                                                                                                                                              |
| Positif — eksekusi endpoint                                                       | `POST finance/bank-reconciliations/create {bank_account_id:<Bank Mandiri BPJS>, statement_date:"2026-03-31", statement_balance:3299500000, book_balance:3300000000}` + 1 item penyesuai (biaya admin −500.000) | 201, `is_balanced:true` LANGSUNG (tanpa perlu investigasi tambahan)                                                                                                                                                                                               |
| **Positif — kontras kompleksitas 2 rekening dalam 1 file (kasus baru suite ini)** | Bandingkan jumlah item penyesuai: §1 (Bank BCA) = 5 item (2 timing + 2 error + 1 penemuan), §2 (Bank Mandiri BPJS) = 1 item                                                                                    | Verifikasi laporan/dashboard rekonsiliasi (kalau ada) bisa menampilkan KEDUA rekening secara terpisah dengan status masing-masing, bukan digabung jadi 1 angka "total kas" yang menyembunyikan bahwa 1 rekening butuh investigasi jauh lebih dalam dari yang lain |
| Netralisasi                                                                       | Simpan hasil rekonsiliasi 1103 — dipakai sebagai saldo akhir kas suite ini                                                                                                                                     |

## 3. Laporan PPN (**Tax Summary**)

Tema utama section ini: RS besar **sebagian besar jasanya BEBAS PPN** (10 dari 11 akun pendapatan), HANYA lini obat bebas/OTC (`4111`) yang kena PPN — sama filosofi dengan suite klinik gigi, tapi rasio "akun bebas PPN vs kena PPN" jauh lebih ekstrem di suite ini (10:1 vs klinik gigi 3:1).

| Skenario                                                                | Detail                                                                                                                                                                                                                          | Hasil                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — PPN Keluaran                                                  | `POST reports/tax-summary {date_from:"2026-01-01", date_to:"2026-03-31", type:"output"}`                                                                                                                                        | **220.000** — HANYA dari T9 (penjualan obat bebas/OTC, file 01). Pastikan T1-T8, T12, T13 (semua pendapatan jasa medis/piutang, total 238.000.000 − 2.000.000 = 236.000.000) **TIDAK muncul sebagai basis PPN Keluaran sama sekali**                                                                                                                                                                |
| Positif — PPN Masukan                                                   | `POST reports/tax-summary {..., type:"input"}`                                                                                                                                                                                  | **46.200.000** — dari T10 (pembelian obat & alkes dari supplier PKP, file 01). Tidak ada pembelian ber-PPN tambahan di file 06/07 (akuisisi/pelepasan aset tetap tidak dimodelkan dengan PPN di suite ini, konsisten dengan suite lain)                                                                                                                                                             |
| **Positif — posisi PPN bersih (lebih bayar signifikan, kasus khas RS)** | Hitung manual: `PPN Keluaran − PPN Masukan = 220.000 − 46.200.000 = (45.980.000)`                                                                                                                                               | Posisi **LEBIH BAYAR (restitusi/kompensasi) 45.980.000** — rasio lebih bayar jauh lebih ekstrem dari suite klinik gigi (517.000) karena RS ini nyaris seluruhnya jasa kesehatan bebas PPN tapi tetap harus beli obat/alkes ber-PPN dalam volume besar. Verifikasi laporan menampilkan tanda negatif/label "lebih bayar" dengan benar pada NILAI PULUHAN JUTA (bukan nilai kecil seperti suite lain) |
| **Catatan keterbatasan (bukan bug, dari file 00 §7)**                   | Laporan ini TIDAK memodelkan mekanisme kompensasi PPN lebih bayar ke masa pajak berikutnya (Pasal 9 ayat 4 UU PPN), PPh 23 jasa dokter mitra, maupun PPh Badan tahunan RS — murni angka mentah PPN Keluaran/Masukan per periode | —                                                                                                                                                                                                                                                                                                                                                                                                   |
| Negatif                                                                 | Filter `date_from`/`date_to` di luar rentang ada transaksi (mis. April-Desember 2026)                                                                                                                                           | PPN Keluaran & Masukan = 0, bukan error                                                                                                                                                                                                                                                                                                                                                             |

## Ringkasan Akhir Suite — Saldo Kunci untuk Referensi Silang

| Item                                                                       |                  Nilai |
| -------------------------------------------------------------------------- | ---------------------: |
| Modal Pemilik awal (file 00)                                               |         49.100.000.000 |
| Trial Balance total debit=kredit (file 02, per 2026-01-28)                 |         66.333.170.000 |
| Laba (Rugi) berjalan per 2026-01-28 (file 04)                              |        (2.142.985.000) |
| Total NBV Aset Tetap akhir Maret (file 06)                                 |         56.950.833.333 |
| Rugi Pelepasan Ambulans (file 06)                                          |             18.000.000 |
| Bank BCA setelah rekonsiliasi (file 07)                                    |            699.550.000 |
| Bank Mandiri Khusus BPJS setelah rekonsiliasi (file 07)                    |          3.299.500.000 |
| Sisa Piutang Klaim BPJS setelah semua penyesuaian (240.000.000−75.000.000) |            165.000.000 |
| PPN Keluaran kumulatif                                                     |                220.000 |
| PPN Masukan kumulatif                                                      |             46.200.000 |
| Posisi PPN bersih                                                          | Lebih bayar 45.980.000 |

## Referensi Silang

- File [`06-aset-tetap-alat-medis-besar.id.md`](./06-aset-tetap-alat-medis-besar.id.md) — saldo awal Bank BCA file ini
- File [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) §3 & §7 — desain PPN selektif per akun yang diverifikasi di §3, dan desain 2 rekening bank terpisah yang diverifikasi di §1-2
- Suite klinik gigi [`../accounting-klinik-gigi/06-rekonsiliasi-bank-dan-ppn.id.md`](../accounting-klinik-gigi/06-rekonsiliasi-bank-dan-ppn.id.md) — pola dasar "1 item harus ditemukan sendiri" yang direplikasi, dengan tambahan kasus baru rekonsiliasi 2 rekening sekaligus (belum pernah dites di suite manapun)
