---
title: (Klinik Gigi) — 06. Rekonsiliasi Bank & Laporan PPN
category: accounting-klinik-gigi
description: Rekonsiliasi Bank BCA Operasional dengan 4 variasi selisih (biaya admin, setoran dalam perjalanan, cek belum cair, salah input transposisi), plus verifikasi PPN Keluaran/Masukan yang SELEKTIF hanya dari lini produk ritel — ciri khas klinik gigi yang sebagian besar jasanya bebas PPN.
visibility: internal
---

# 06. Rekonsiliasi Bank & Laporan PPN

> Prasyarat: file [`05-anggaran-dan-aset-tetap.id.md`](./05-anggaran-dan-aset-tetap.id.md) sudah selesai (§2.4 pelepasan aset TIDAK dieksekusi). Saldo buku Bank BCA Operasional (1102) per 2026-02-28 = **35.713.000**.
>
> **Prasyarat tambahan**: tambahkan 1 akun baru ke Chart of Accounts sebelum mulai — `5208 Beban Administrasi Bank` (tipe Beban, tidak ada flag khusus). Akun ini belum ada di file 00 karena biaya admin bank baru relevan mulai file ini.

## 1. Rekonsiliasi Bank BCA Operasional (**Bank Reconciliations**)

### 1.1 Transaksi tambahan Februari yang memicu selisih (buat dulu sebelum rekonsiliasi)

| #   | Tanggal    | Deskripsi                                                                                                                                                                                     | Jurnal                                                                                     |                                       Nilai |
| --- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------: |
| a   | 2026-02-28 | Setoran kas kecil ke Bank BCA, **sudah dicatat di buku** tapi baru kliring di rekening koran bulan berikutnya (setoran dalam perjalanan)                                                      | Dr 1102 Bank BCA 500.000 / Cr 1101 Kas Kecil 500.000                                       |                                     500.000 |
| b   | 2026-02-27 | Cek pembayaran gaji ke 1 karyawan yang belum sempat dicairkan sampai tanggal statement (cek belum cair)                                                                                       | Dr 5202 Beban Gaji Karyawan Non-Dokter 1.200.000 / Cr 1102 Bank BCA 1.200.000              |                                   1.200.000 |
| c   | 2026-02-25 | Pembayaran komisi dokter (transaksi kecil terpisah dari siklus file 01) — **staf salah input** Rp250.000 padahal nominal sebenarnya di rekening koran Rp520.000 (kesalahan transposisi angka) | Dr 2103 Utang Komisi Dokter 250.000 / Cr 1102 Bank BCA 250.000 (SALAH, seharusnya 520.000) | 250.000 (tercatat) vs 520.000 (aktual bank) |

Setelah (a)+(b)+(c) tercatat, saldo buku 1102 = 35.713.000 + 500.000 − 1.200.000 − 250.000 = **34.763.000**. Biaya admin bank Rp25.000 BELUM dicatat sama sekali di buku (baru diketahui dari rekening koran).

### 1.2 Rekening Koran (Bank Statement) per 2026-02-28

**Saldo rekening koran = Rp 36.118.000** (data dari bank, dianggap sudah benar/final — tugas rekonsiliasi adalah menjelaskan SEMUA selisih terhadap saldo buku).

### 1.3 Perhitungan Rekonsiliasi (WAJIB dihitung manual dulu sebelum eksekusi endpoint)

```
SISI BANK
  Saldo Rekening Koran (2026-02-28)                 36.118.000
  + Setoran dalam perjalanan (butir a)                 500.000
  − Cek/pembayaran belum cair (butir b)             (1.200.000)
  = Saldo Bank Disesuaikan                          35.418.000

SISI BUKU
  Saldo Buku (1102, setelah butir a+b+c)             34.763.000
  − Biaya Administrasi Bank (belum dicatat)             (25.000)
  − Koreksi salah input butir c (250.000 → 520.000,
    kurang dicatat 270.000 sebagai pengeluaran)         (270.000)
  = Saldo Buku Disesuaikan                           34.468.000
```

**⚠️ TIDAK BALANCE pada percobaan pertama** (35.418.000 ≠ 34.468.000, selisih 950.000) — INI DISENGAJA. Cek ulang: saldo buku SETELAH butir a+b+c seharusnya dihitung dari basis 35.713.000, bukan lupa salah satu butir. Hitung ulang dengan teliti:

```
35.713.000 (saldo akhir file 05)
+ 500.000  (butir a, setoran dari kas kecil MASUK ke bank)
− 1.200.000 (butir b, gaji KELUAR dari bank)
− 250.000   (butir c, komisi KELUAR dari bank, versi tercatat)
= 34.763.000   ← saldo buku SEBELUM koreksi rekonsiliasi, cocok dengan §1.1
```

```
Saldo Buku (sebelum koreksi)        34.763.000
− Biaya Admin Bank (baru diketahui)   (25.000)
− Koreksi kurang catat butir c        (270.000)
= Saldo Buku Disesuaikan            34.468.000

Saldo Bank Disesuaikan (dari sisi bank di atas) = 35.418.000
```

**Selisih 950.000 tetap ada — berarti ADA 1 ITEM LAGI yang belum diperhitungkan.** Ini SENGAJA didesain sebagai bagian dari test case: staf yang melakukan rekonsiliasi harus menemukan sendiri bahwa `500.000 (setoran a) − 1.200.000 (cek b) = −700.000` neto dari sisi rekonsiliasi TIMING, sedangkan dari sisi ERROR CORRECTION cuma `25.000 + 270.000 = 295.000`. Total item sisi bank (700.000 neto berlawanan arah) ditambah sisi buku (295.000) TIDAK otomatis saling meniadakan kecuali dihitung ke arah yang benar — **inilah kesalahan umum staf akuntansi pemula saat rekonsiliasi** (salah arah tambah/kurang). Hitung ulang yang BENAR:

```
Saldo Bank Disesuaikan = Saldo Rekening Koran + Setoran Dalam Perjalanan − Cek Belum Cair
                        = 36.118.000 + 500.000 − 1.200.000 = 35.418.000   (tetap sama)

Saldo Buku Disesuaikan = Saldo Buku (34.763.000, SUDAH termasuk butir a & b karena keduanya
                          SUDAH terjurnal di buku) − Biaya Admin (25.000) − Koreksi butir c (270.000)
                        = 34.763.000 − 25.000 − 270.000 = 34.468.000
```

Selisih 950.000 ini **BUKAN salah hitung** dokumen — melainkan bukti bahwa saldo rekening koran 36.118.000 yang diberikan di §1.2 punya SATU LAGI transaksi bank yang TIDAK tercatat di buku sama sekali (bukan sekadar admin fee & error kecil). **Selisih yang belum terjelaskan = 950.000.**

| Skenario                                                     | Detail                                                                                                                                                                                                                                                                                                                                                                                          | Hasil                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — temukan item hilang (skill utama rekonsiliasi)** | Staf harus MENYELIDIKI mutasi bank yang tidak ada di buku sebesar 950.000 — untuk keperluan test case ini, anggap ditemukan: **transfer masuk otomatis dari BPJS Kesehatan Rp950.000** (pelunasan sisa piutang T2/T14 yang masuk LANGSUNG ke rekening bank tanpa notifikasi manual ke kasir, khas pencairan BPJS yang otomatis debet-kredit antar rekening) — belum pernah dijurnal sama sekali | Buat jurnal baru: `Dr 1102 Bank BCA 950.000 / Cr 1103 Piutang Pasien BPJS/Asuransi 950.000`, tanggal 2026-02-26                                                                                                                                                                                                        |
| Positif — rekonsiliasi ulang setelah item ditemukan          | Saldo Buku Disesuaikan = 34.468.000 + 950.000 = **35.418.000**                                                                                                                                                                                                                                                                                                                                  | **COCOK PERSIS dengan Saldo Bank Disesuaikan (35.418.000) → rekonsiliasi BALANCE**                                                                                                                                                                                                                                     |
| Positif — eksekusi endpoint                                  | `POST finance/bank-reconciliations/create {bank_account_id:<Bank BCA>, statement_date:"2026-02-28", statement_balance:36118000, book_balance:35713000}` lalu tambahkan 4 item penyesuai (setoran dalam perjalanan +500.000, cek belum cair −1.200.000, biaya admin −25.000, koreksi transposisi −270.000, transfer BPJS ditemukan +950.000) sesuai kontrak field endpoint aktual                | 201, status akhir `is_balanced:true` atau `reconciled_balance` sama antara sisi bank & buku (35.418.000)                                                                                                                                                                                                               |
| Negatif                                                      | Submit rekonsiliasi TANPA menemukan item 950.000 (selisih dibiarkan tidak dijelaskan)                                                                                                                                                                                                                                                                                                           | Endpoint SEHARUSNYA menolak/menandai `is_balanced:false` selama ada selisih — kalau ternyata sistem izinkan "selesai" rekonsiliasi walau selisih belum nol, itu gap kontrol (rekonsiliasi yang tidak benar-benar balance seharusnya tidak bisa ditutup sebagai final) — belum diverifikasi ke kode, tulis hasil aktual |
| Netralisasi                                                  | Simpan hasil rekonsiliasi ini — saldo Bank BCA final setelah semua koreksi (biaya admin, transfer BPJS, catatan salah input dibetulkan) = **35.418.000 + 25.000 (admin, sudah dikurangkan di atas jadi TIDAK ditambah balik) ...** — cukup pastikan saldo GL akun 1102 aktual = 35.418.000 setelah semua jurnal koreksi di atas diposting                                                       |

## 2. Laporan PPN (**Tax Summary** atau sejenis)

Tema utama section ini: klinik gigi **sebagian besar jasa medisnya BEBAS PPN**, hanya lini produk ritel (4104) yang kena PPN — laporan PPN HARUS mencerminkan pemisahan ini secara otomatis dari flag `tax_id` per akun (file 00 §3), bukan dari jenis dokumen.

| Skenario                                                                  | Detail                                                                                                                                                                                                                                           | Hasil                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — PPN Keluaran                                                    | `POST reports/tax-summary {date_from:"2026-01-01", date_to:"2026-01-28", type:"output"}` (PPN Keluaran)                                                                                                                                          | **33.000** — HANYA dari T4 (penjualan produk ritel). Pastikan T1, T2, T3, T8, T13, T14 (semua pendapatan jasa medis, total 8.150.000 − 300.000 = 7.850.000) **TIDAK muncul sebagai basis PPN Keluaran sama sekali**                                                                                      |
| Positif — PPN Masukan                                                     | `POST reports/tax-summary {..., type:"input"}` (PPN Masukan)                                                                                                                                                                                     | **550.000** — dari T6 (pembelian BHP gigi dari supplier PKP)                                                                                                                                                                                                                                             |
| **Positif — posisi PPN bersih (kasus khas bisnis campuran PKP-sebagian)** | Hitung manual: `PPN Keluaran − PPN Masukan = 33.000 − 550.000 = (517.000)`                                                                                                                                                                       | Posisi **LEBIH BAYAR (restitusi/kompensasi) 517.000** — ini WAJAR untuk klinik yang mayoritas jasanya bebas PPN tapi tetap beli banyak barang kena PPN Masukan (BHP gigi). Verifikasi laporan menampilkan tanda negatif/label "lebih bayar" dengan benar, BUKAN memaksa angka jadi 0 atau positif keliru |
| **Catatan keterbatasan (bukan bug, dari file 00 §7)**                     | Laporan ini TIDAK memodelkan mekanisme kompensasi PPN lebih bayar ke masa pajak berikutnya (Pasal 9 ayat 4 UU PPN) — murni angka mentah `PPN Keluaran` dan `PPN Masukan` per periode, keputusan restitusi/kompensasi tetap manual di luar sistem | —                                                                                                                                                                                                                                                                                                        |
| Negatif                                                                   | Filter `date_from`/`date_to` di luar rentang ada transaksi (mis. Desember 2025)                                                                                                                                                                  | PPN Keluaran & Masukan = 0, bukan error                                                                                                                                                                                                                                                                  |

## Ringkasan Akhir Suite — Saldo Kunci untuk Referensi Silang

| Item                                                       |               Nilai |
| ---------------------------------------------------------- | ------------------: |
| Modal Pemilik awal (file 00)                               |         181.350.000 |
| Trial Balance total debit=kredit (file 02, per 2026-01-28) |         215.433.000 |
| Laba (Rugi) berjalan per 2026-01-28 (file 04)              |        (12.832.000) |
| Bank BCA setelah aset tetap (file 05, per 2026-02-28)      |          35.713.000 |
| Bank BCA setelah rekonsiliasi (file 06)                    |          35.418.000 |
| PPN Keluaran kumulatif                                     |              33.000 |
| PPN Masukan kumulatif                                      |             550.000 |
| Posisi PPN bersih                                          | Lebih bayar 517.000 |

## Referensi Silang

- File [`05-anggaran-dan-aset-tetap.id.md`](./05-anggaran-dan-aset-tetap.id.md) — saldo awal Bank BCA file ini
- File [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) §3 & §7 — desain PPN selektif per akun yang diverifikasi di §2
- Suite retail [`../accounting/07-rekonsiliasi-bank.id.md`](../accounting/07-rekonsiliasi-bank.id.md) & [`../accounting/08-laporan-pajak-ppn.id.md`](../accounting/08-laporan-pajak-ppn.id.md) — pola dasar yang direplikasi strukturnya (4 variasi selisih rekonsiliasi, termasuk 1 kasus "harus ditemukan sendiri" yang lebih menantang dari suite retail)
