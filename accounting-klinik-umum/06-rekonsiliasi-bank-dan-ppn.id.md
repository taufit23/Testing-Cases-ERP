---
title: (Klinik Umum Besar) — 06. Rekonsiliasi Bank & Laporan PPN
category: accounting-klinik-umum
description: Rekonsiliasi Bank Mandiri Operasional dengan 4 item penyesuai (termasuk 1 item yang harus "ditemukan sendiri" — autopay asuransi swasta langsung ke bank), plus verifikasi PPN Keluaran/Masukan yang SELEKTIF per akun pendapatan maupun jenis pembelian — penutup suite klinik umum besar ini.
visibility: internal
---

# 06. Rekonsiliasi Bank & Laporan PPN

> Prasyarat: file [`05-anggaran-dan-aset-tetap.id.md`](./05-anggaran-dan-aset-tetap.id.md) sudah selesai (§4 pelepasan aset TIDAK dieksekusi). Saldo buku Bank Mandiri Operasional (1102) per 2026-02-28 = **95.030.000**.
>
> **Prasyarat tambahan**: tambahkan 1 akun baru ke Chart of Accounts sebelum mulai — `5110 Beban Administrasi Bank` (tipe Beban, tidak ada flag khusus). Akun ini belum ada di file 00 karena biaya admin bank baru relevan mulai file ini.

## 1. Rekonsiliasi Bank Mandiri Operasional (**Bank Reconciliations**)

### 1.1 Transaksi tambahan Februari yang memicu selisih (buat dulu sebelum rekonsiliasi)

| #   | Tanggal    | Deskripsi                                                                                                                                                                                                              | Jurnal                                                                                                                  |                                           Nilai |
| --- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------: |
| a   | 2026-02-27 | Pemindahan sebagian dana kapitasi dari BCA Penampungan ke Mandiri Operasional, **sudah dicatat di buku** tapi baru kliring di rekening koran awal Maret (setoran/transfer antar-bank dalam perjalanan)                 | Dr 1102 Bank Mandiri 50.000.000 / Cr 1103 Bank BCA Penampungan 50.000.000                                               |                                      50.000.000 |
| b   | 2026-02-26 | Cek pembayaran ke distributor farmasi/alkes yang belum sempat dicairkan sampai tanggal statement (cek belum cair)                                                                                                      | Dr 2101 Utang Dagang 30.000.000 / Cr 1102 Bank Mandiri 30.000.000                                                       |                                      30.000.000 |
| c   | 2026-02-25 | Pembayaran fee dokter spesialis paruh waktu (transaksi kecil terpisah dari siklus file 01) — **staf salah input** Rp 4.200.000 padahal nominal sebenarnya di rekening koran Rp 4.700.000 (kesalahan transposisi angka) | Dr 2104 Utang Fee Dokter Spesialis Paruh Waktu 4.200.000 / Cr 1102 Bank Mandiri 4.200.000 (SALAH, seharusnya 4.700.000) | 4.200.000 (tercatat) vs 4.700.000 (aktual bank) |

Setelah (a)+(b)+(c) tercatat, saldo buku 1102 = 95.030.000 + 50.000.000 − 30.000.000 − 4.200.000 = **110.830.000**. Biaya admin bank Rp 75.000 BELUM dicatat sama sekali di buku (baru diketahui dari rekening koran).

### 1.2 Rekening Koran (Bank Statement) per 2026-02-28

**Saldo rekening koran = Rp 90.870.000** (data dari bank, dianggap sudah benar/final — tugas rekonsiliasi adalah menjelaskan SEMUA selisih terhadap saldo buku).

### 1.3 Perhitungan Rekonsiliasi (WAJIB dihitung manual dulu sebelum eksekusi endpoint)

```
SISI BANK
  Saldo Rekening Koran (2026-02-28)                 90.870.000
  + Transfer antar-bank dalam perjalanan (butir a)   50.000.000
  − Cek/pembayaran belum cair (butir b)             (30.000.000)
  = Saldo Bank Disesuaikan                          110.870.000

SISI BUKU
  Saldo Buku (1102, setelah butir a+b+c)             110.830.000
  − Biaya Administrasi Bank (belum dicatat)              (75.000)
  − Koreksi salah input butir c (4.200.000 → 4.700.000,
    kurang dicatat 500.000 sebagai pengeluaran)          (500.000)
  = Saldo Buku Disesuaikan                           110.255.000
```

**⚠️ TIDAK BALANCE pada percobaan pertama** (110.870.000 ≠ 110.255.000, selisih 615.000) — INI DISENGAJA, sama seperti pola di suite klinik gigi. Staf yang melakukan rekonsiliasi harus **MENYELIDIKI** mutasi bank yang tidak ada di buku sebesar 615.000 — untuk keperluan test case ini, ditemukan: **transfer masuk otomatis dari 1 perusahaan asuransi swasta (autopay langsung ke rekening bank tanpa notifikasi manual ke kasir)** sebesar Rp 615.000, pelunasan sisa piutang non-kapitasi kecil dari saldo awal 1105 yang belum pernah dijurnal sama sekali.

```
Item yang ditemukan: Dr 1102 Bank Mandiri 615.000 / Cr 1105 Piutang MCU Korporat & Asuransi Swasta 615.000
                      tanggal 2026-02-24

Saldo Buku Disesuaikan (setelah item ditemukan) = 110.255.000 + 615.000 = 110.870.000
Saldo Bank Disesuaikan (dari sisi bank, tidak berubah)                  = 110.870.000

  → COCOK PERSIS → rekonsiliasi BALANCE
```

| Skenario                                                     | Detail                                                                                                                                                                                                                                                                                                                                                                                                         | Hasil                                                                                                                                                                                                                        |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — temukan item hilang (skill utama rekonsiliasi)** | Staf menemukan transfer autopay asuransi swasta 615.000 yang belum terjurnal                                                                                                                                                                                                                                                                                                                                   | Buat jurnal baru sesuai di atas, tanggal 2026-02-24                                                                                                                                                                          |
| Positif — rekonsiliasi ulang setelah item ditemukan          | Saldo Buku Disesuaikan = 110.255.000 + 615.000 = **110.870.000**                                                                                                                                                                                                                                                                                                                                               | **COCOK PERSIS dengan Saldo Bank Disesuaikan (110.870.000) → rekonsiliasi BALANCE**                                                                                                                                          |
| Positif — eksekusi endpoint                                  | `POST finance/bank-reconciliations/create {bank_account_id:<Bank Mandiri>, statement_date:"2026-02-28", statement_balance:90870000, book_balance:95030000}` lalu tambahkan item penyesuai (transfer antar-bank dalam perjalanan +50.000.000, cek belum cair −30.000.000, koreksi transposisi butir c −500.000, biaya admin −75.000, transfer asuransi ditemukan +615.000) sesuai kontrak field endpoint aktual | 201, status akhir `is_balanced:true` atau `reconciled_balance` sama antara sisi bank & buku (110.870.000)                                                                                                                    |
| Negatif                                                      | Submit rekonsiliasi TANPA menemukan item 615.000 (selisih dibiarkan tidak dijelaskan)                                                                                                                                                                                                                                                                                                                          | Endpoint SEHARUSNYA menolak/menandai `is_balanced:false` selama ada selisih — kalau ternyata sistem izinkan "selesai" rekonsiliasi walau selisih belum nol, itu gap kontrol — belum diverifikasi ke kode, tulis hasil aktual |
| Netralisasi                                                  | Pastikan saldo GL akun 1102 aktual = **110.870.000** setelah semua jurnal koreksi di atas (a, b, c, biaya admin, transfer asuransi ditemukan) diposting                                                                                                                                                                                                                                                        |

## 2. Laporan PPN (**Tax Summary** atau sejenis)

Tema utama section ini: klinik umum besar **sebagian besar pendapatannya (kapitasi, non-kapitasi, MCU, lab, obat) BEBAS PPN**, hanya lini produk kesehatan non-obat ritel (4106) yang kena PPN — dan PPN Masukan HANYA dari pembelian alkes/BHP kategori tertentu (bukan obat) — laporan PPN HARUS mencerminkan pemisahan ganda ini secara otomatis dari flag `tax_id` per akun (file 00 §3), bukan dari jenis dokumen.

| Skenario                                                                  | Detail                                                                                                                                                                                                                                                                                                                                            | Hasil                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — PPN Keluaran                                                    | `POST reports/tax-summary {date_from:"2026-01-01", date_to:"2026-01-31", type:"output"}` (PPN Keluaran)                                                                                                                                                                                                                                           | **1.980.000** — HANYA dari T8 (penjualan produk kesehatan non-obat ritel). Pastikan T1, T2/T2b, T3, T4, T6, T7 (kapitasi, non-kapitasi, MCU, lab, obat) **TIDAK muncul sebagai basis PPN Keluaran sama sekali**                                                                                      |
| Positif — PPN Masukan                                                     | `POST reports/tax-summary {..., type:"input"}` (PPN Masukan)                                                                                                                                                                                                                                                                                      | **4.400.000** — HANYA dari T9b (pembelian BHP medis/alkes). T9a (pembelian obat, bebas PPN) **TIDAK muncul sama sekali sebagai basis PPN Masukan** — ini kasus baru yang lebih granular dari suite klinik gigi (di sana SEMUA pembelian BHP memicu PPN Masukan, di sini hanya sebagian jenis barang) |
| **Positif — posisi PPN bersih (kasus khas bisnis campuran PKP-sebagian)** | Hitung manual: `PPN Keluaran − PPN Masukan = 1.980.000 − 4.400.000 = (2.420.000)`                                                                                                                                                                                                                                                                 | Posisi **LEBIH BAYAR (restitusi/kompensasi) 2.420.000** — wajar untuk klinik yang mayoritas pendapatannya bebas PPN tapi tetap beli alkes/BHP kena PPN Masukan. Verifikasi laporan menampilkan tanda negatif/label "lebih bayar" dengan benar, BUKAN memaksa angka jadi 0 atau positif keliru        |
| **Catatan keterbatasan (bukan bug, dari file 00 §7)**                     | Laporan ini TIDAK memodelkan mekanisme kompensasi PPN lebih bayar ke masa pajak berikutnya (Pasal 9 ayat 4 UU PPN), maupun pajak final atas jasa dokter mitra (bukan karyawan tetap) — murni angka mentah `PPN Keluaran` dan `PPN Masukan` per periode, keputusan restitusi/kompensasi & kepatuhan pajak dokter mitra tetap manual di luar sistem | —                                                                                                                                                                                                                                                                                                    |
| Negatif                                                                   | Filter `date_from`/`date_to` di luar rentang ada transaksi (mis. Desember 2025)                                                                                                                                                                                                                                                                   | PPN Keluaran & Masukan = 0, bukan error                                                                                                                                                                                                                                                              |

## Ringkasan Akhir Suite — Saldo Kunci untuk Referensi Silang

| Item                                                                 |                 Nilai |
| -------------------------------------------------------------------- | --------------------: |
| Modal Pemilik awal (file 00)                                         |           801.500.000 |
| Trial Balance total debit=kredit (file 02, per 2026-01-31)           |         1.931.980.000 |
| Laba (Rugi) berjalan per 2026-01-31 (file 04)                        |           393.950.000 |
| Total Pendapatan Kapitasi BPJS 6 cabang (file 01/04)                 |           544.000.000 |
| Total Piutang Kapitasi BPJS akhir Januari (file 01)                  |           244.000.000 |
| Total Piutang MCU Korporat & Asuransi Swasta akhir Januari (file 01) |           164.500.000 |
| Bank Mandiri setelah aset tetap (file 05, per 2026-02-28)            |            95.030.000 |
| Bank Mandiri setelah rekonsiliasi (file 06)                          |           110.870.000 |
| PPN Keluaran kumulatif                                               |             1.980.000 |
| PPN Masukan kumulatif                                                |             4.400.000 |
| Posisi PPN bersih                                                    | Lebih bayar 2.420.000 |

## Referensi Silang

- File [`05-anggaran-dan-aset-tetap.id.md`](./05-anggaran-dan-aset-tetap.id.md) — saldo awal Bank Mandiri file ini
- File [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) §3 & §7 — desain PPN selektif ganda (Keluaran per akun pendapatan, Masukan per jenis pembelian) yang diverifikasi di §2
- Suite klinik gigi [`../accounting-klinik-gigi/06-rekonsiliasi-bank-dan-ppn.id.md`](../accounting-klinik-gigi/06-rekonsiliasi-bank-dan-ppn.id.md) — pola dasar yang direplikasi strukturnya (item "harus ditemukan sendiri" saat rekonsiliasi)
