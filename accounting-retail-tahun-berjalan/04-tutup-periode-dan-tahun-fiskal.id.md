---
title: — 04. Tutup Periode & Tahun Fiskal (Close FY2025, Lanjut FY2026)
category: Accounting 2
description: Close 12 Accounting Period FY2025, Close Fiscal Year FY2025 dengan closing entry presisi (net income 27.050.000) ke Laba Ditahan, lalu verifikasi FY2026 tetap terbuka untuk transaksi berjalan — skenario "perusahaan pindah tahun buku sambil tetap operasional".
visibility: internal
---

# 04. Tutup Periode & Tahun Fiskal (Close FY2025, Lanjut FY2026)

> Prasyarat: [`01-jurnal-transaksi-2025.id.md`](./01-jurnal-transaksi-2025.id.md) selesai (semua 104 jurnal FY2025 Posted) dan angka acuan Trial Balance FY2025 di [`03-general-ledger-trial-balance.id.md`](./03-general-ledger-trial-balance.id.md) §2 sudah dicek cocok. Istilah "Close vs Lock", "Closing entry", "Kenapa harus tepat 1 akun Laba Ditahan" sudah dijelaskan di `../accounting/03-tutup-periode-dan-tahun-fiskal.id.md` — tidak diulang di sini.

## Kenapa Suite Ini Bagus untuk Menguji Close Fiscal Year Secara Realistis

**Beda dengan suite `accounting/`** (yang cuma 1 fiscal year, jadi "tutup tahun" itu langkah akhir cerita) — di suite ini, **Close FY2025 terjadi DI TENGAH cerita**: FY2026 sudah punya 1-8 bulan transaksi berjalan SEBELUM kamu menutup FY2025. Ini pola yang sungguhan terjadi di dunia nyata (perusahaan tidak berhenti beroperasi menunggu tutup buku tahun lalu selesai) — jadi test case ini sekaligus membuktikan 2 hal:

1. Close Fiscal Year FY2025 **tidak mengganggu** transaksi FY2026 yang sudah posted duluan (periode berbeda, harusnya independen)
2. Setelah FY2025 closed, transaksi BARU tetap bisa masuk ke FY2026 tanpa halangan

## 4.1 Tutup 12 Accounting Period FY2025

**Sebab-akibat:** guard `all_accounting_periods_in_this_fiscal_year_must_be_closed_first` (lihat `../accounting/03-...md` §3.3) berarti KE-12 periode FY2025 harus closed dulu, satu-satu, sebelum Close Fiscal Year bisa jalan — tidak ada jalan pintas "close tahun sekaligus tanpa close bulan".

| Skenario                                                           | Langkah di UI                                                                                                                                                                                              | Hasil                                                                                                                             |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                            | Pastikan semua 104 jurnal FY2025 (file 01) sudah **Posted** → buka **Accounting Period**, filter Fiscal Year `FY2025` → untuk tiap bulan Januari-Desember 2025: menu **⋮** → **Close Period** → konfirmasi | Ke-12 baris FY2025 berbadge **Closed** — cek satu-satu, jangan asumsi kalau 1 gagal yang lain otomatis batal                      |
| **Negatif — coba close FY2025 padahal ada 1 periode belum closed** | Sengaja lewati close periode Desember 2025 → lanjut ke §4.2 (Close Fiscal Year) langsung                                                                                                                   | Ditolak `all_accounting_periods_in_this_fiscal_year_must_be_closed_first` — kembali ke sini, close Desember 2025 dulu baru lanjut |
| Netralisasi                                                        | Menu **⋮** tiap periode → **Reopen Period** kalau perlu koreksi jurnal FY2025 lagi setelah ini (HARUS reopen dulu sebelum bisa post/edit jurnal ke bulan itu)                                              |                                                                                                                                   |

## 4.2 Close Fiscal Year FY2025 — Closing Entry Presisi

**Prasyarat:** §4.1 selesai (12/12 periode FY2025 closed) + tepat 1 akun ber-flag `is_retained_earnings_account` (akun 3102 Laba Ditahan, dari file 00).

**Angka acuan closing entry** (dihitung manual dari Trial Balance FY2025 di file 03 §2 — inilah yang WAJIB persis sama dengan response sistem):

| Baris Jurnal Penutup (`CLOSE-FY2025`)  |           Debit |          Kredit |
| -------------------------------------- | --------------: | --------------: |
| Penjualan Barang Dagang (4101)         |     960.000.000 |                 |
| Harga Pokok Penjualan (5101)           |                 |     600.000.000 |
| Beban Sewa Toko (5201)                 |                 |      96.000.000 |
| Beban Gaji Karyawan (5202)             |                 |     180.000.000 |
| Beban Listrik & Air (5203)             |                 |      24.000.000 |
| Beban Penyusutan Peralatan Toko (5204) |                 |      13.750.000 |
| Beban Selisih Kas (5205)               |                 |         200.000 |
| Beban Iklan & Promosi (5208)           |                 |       8.000.000 |
| Beban Bunga Pinjaman (5210)            |                 |      11.000.000 |
| **Laba Ditahan (3102)**                |                 |  **27.050.000** |
| **Total**                              | **960.000.000** | **960.000.000** |

**Cara verifikasi cepat:** 960.000.000 (Penjualan) − (600.000.000 + 96.000.000 + 180.000.000 + 24.000.000 + 13.750.000 + 200.000 + 8.000.000 + 11.000.000 = 932.950.000 total Beban) = **27.050.000** → itulah `net_income` yang harus muncul di response.

| Skenario                               | Langkah di UI                                                                                                                                                                                                         | Hasil                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Negatif — 0 akun retained earnings** | Buka **Chart of Accounts**, edit akun 3102 → matikan `is_retained_earnings_account` → Save → buka **Fiscal Year** → menu **⋮** FY2025 → **Close Fiscal Year** → konfirmasi                                            | Ditolak `flag_exactly_one_account_as_the_retained_earnings_account_in_chart_of_accounts_before_closing_a_fiscal_year` — kembalikan lagi toggle 3102 ke aktif sebelum lanjut                                                                                                                                                                                                     |
| **Negatif — 2 akun retained earnings** | Aktifkan `is_retained_earnings_account` juga di akun lain (mis. 3101 Modal Pemilik) → Close Fiscal Year lagi                                                                                                          | Ditolak `more_than_one_account_is_flagged_as_retained_earnings_account_only_one_is_allowed` — matikan lagi toggle di akun tambahan itu                                                                                                                                                                                                                                          |
| Positif                                | Semua prasyarat terpenuhi (hanya 3102 yang ber-flag) → **Fiscal Year** → menu **⋮** FY2025 → **Close Fiscal Year** → modal warning ireversibel → konfirmasi                                                           | Toast sukses, `net_income: 27050000`, `closing_journal` kode `CLOSE-FY2025` — badge FY2025 jadi **Closed**                                                                                                                                                                                                                                                                      |
| **Positif — verifikasi Laba Ditahan**  | Buka **Trial Balance** lagi (tanpa filter tanggal, atau Date To 2025-12-31)                                                                                                                                           | Saldo 3102 Laba Ditahan sekarang **27.050.000** (sebelumnya 0), dan SEMUA akun Pendapatan (4101) & Beban (5101-5210) yang tersentuh FY2025 sekarang **kembali 0 per tanggal 31 Desember 2025** — kalau dicek TANPA filter tanggal (termasuk FY2026), akun-akun ini akan tampil terisi lagi karena transaksi Januari-Agustus 2026 baru dimulai dari nol lagi di tahun berikutnya |
| **Positif — FY2026 tidak terganggu**   | Buka **Trial Balance** dengan filter Date From `2026-01-01` Date To `2026-08-31`                                                                                                                                      | Saldo TIDAK berubah dari sebelum Close FY2025 — closing entry FY2025 murni jurnal tanggal 31 Desember 2025, tidak menyentuh baris manapun di FY2026                                                                                                                                                                                                                             |
| Netralisasi                            | TIDAK ADA cara "un-close" fiscal year langsung — kalau perlu koreksi, harus reopen periode-periode terkait dulu (kalau sistem mendukung reopen fiscal year; kalau tidak ada endpoint itu, catat sebagai keterbatasan) |                                                                                                                                                                                                                                                                                                                                                                                 |

## 4.3 FY2026 Tetap Berjalan Setelah FY2025 Ditutup

**Sebab-akibat:** ini poin pembeda utama suite ini — membuktikan siklus tutup-buku TIDAK memaksa perusahaan berhenti transaksi menunggu proses administratif selesai.

| Skenario    | Langkah di UI                                                                                                                                                                                        | Hasil                                                                                                                                  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | Setelah §4.2 selesai (FY2025 closed), buka **Journals** → **+ Create Journal** → Date `2026-09-05`, transaksi apa saja (mis. rekap penjualan bulanan September, lanjutan pola file 02) → Save → Post | Jurnal baru berhasil posting normal ke Accounting Period September 2026 — FY2026 sama sekali tidak terpengaruh status Closed di FY2025 |
| Netralisasi | Reverse/hapus jurnal test September 2026 ini kalau tidak mau melanjutkan suite lebih jauh dari Agustus 2026                                                                                          |                                                                                                                                        |

## Referensi Silang

- [`../accounting/03-tutup-periode-dan-tahun-fiskal.id.md`](../accounting/03-tutup-periode-dan-tahun-fiskal.id.md) — Konsep Dasar Close/Lock/Closing Entry, dan versi test case Close Fiscal Year yang lebih sederhana (1 tahun saja)
- [`03-general-ledger-trial-balance.id.md`](./03-general-ledger-trial-balance.id.md) §2 — sumber angka Trial Balance FY2025 yang dipakai closing entry di atas
- [`05-laporan-keuangan.id.md`](./05-laporan-keuangan.id.md) — Neraca setelah Close FY2025 harus menampilkan Laba Ditahan 27.050.000, BUKAN lagi laba berjalan di akun Pendapatan/Beban
