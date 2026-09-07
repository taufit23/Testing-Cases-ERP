---
title: — 03. General Ledger & Trial Balance (20 Bulan)
category: Accounting 2
description: Verifikasi Trial Balance, Detail Ledger, dan Summary by Account per dimensi toko untuk PT Retail Nusantara Jaya setelah 176 jurnal (Januari 2025-Agustus 2026) posted — semua angka acuan sudah dihitung manual di luar sistem sebagai pembanding.
visibility: internal
---

# 03. General Ledger & Trial Balance (20 Bulan)

> Prasyarat: [`01-jurnal-transaksi-2025.id.md`](./01-jurnal-transaksi-2025.id.md) dan [`02-jurnal-transaksi-2026.id.md`](./02-jurnal-transaksi-2026.id.md) sudah selesai — semua 176 jurnal harus sudah **Posted** (bukan draft/pending) sebelum Trial Balance dicek, karena hanya jurnal posted yang masuk ke `general_ledgers` (lihat "Konsep Dasar" di `../accounting/00-...md`).

## 1. Trial Balance Final (s/d 31 Agustus 2026)

**Halaman:** `accounting/general-ledger` tab Trial Balance (atau `accounting/reports/trial-balance` kalau ada halaman terpisah — lihat catatan di `../accounting/00-...md` §9.5 soal 2 implementasi terpisah, cek keduanya kalau tersedia).

**Angka acuan** (dihitung manual dari seluruh 176 jurnal di file 01+02, di luar sistem, sebelum ditulis di sini — inilah "jawaban benar" untuk dibandingkan):

| Kode | Akun                                | Saldo (Debit) |                                         Saldo (Kredit) |
| ---- | ----------------------------------- | ------------: | -----------------------------------------------------: |
| 1101 | Kas Kecil                           |     9.700.000 |                                                        |
| 1102 | Bank BCA                            |   355.365.000 |                                                        |
| 1103 | Piutang Dagang                      |             0 |                                                        |
| 1104 | Persediaan Barang Dagang            |    90.000.000 |                                                        |
| 1105 | PPN Masukan                         |   130.900.000 |                                                        |
| 1201 | Peralatan Toko                      |    60.000.000 |                                                        |
| 1202 | Akumulasi Penyusutan Peralatan Toko |  (23.750.000) |                                                        |
| 2101 | Utang Dagang                        |               |                                             55.500.000 |
| 2102 | PPN Keluaran                        |               |                                            185.240.000 |
| 2103 | Utang PPh 21 Karyawan               |               |                                                825.000 |
| 2104 | Utang Poin Loyalitas Pelanggan      |               |                                                      0 |
| 2105 | Pinjaman Bank Jangka Pendek         |               |                                             24.000.000 |
| 3101 | Modal Pemilik                       |               |                                            290.000.000 |
| 3102 | Laba Ditahan                        |               | 0 *(baru terisi setelah Close FY2025 — lihat file 04)* |
| 4101 | Penjualan Barang Dagang             |               |                                          1.684.000.000 |
| 4102 | Potongan Penjualan                  |               |                                                      0 |
| 4103 | Pendapatan Lain-lain — Ongkos Kirim |               |                                                      0 |
| 5101 | Harga Pokok Penjualan               | 1.040.000.000 |                                                        |
| 5201 | Beban Sewa Toko                     |   166.400.000 |                                                        |
| 5202 | Beban Gaji Karyawan                 |   312.000.000 |                                                        |
| 5203 | Beban Listrik & Air                 |    41.600.000 |                                                        |
| 5204 | Beban Penyusutan Peralatan Toko     |    23.750.000 |                                                        |
| 5205 | Beban Selisih Kas                   |       300.000 |                                                        |
| 5206 | Beban Susut/Selisih Stok Opname     |             0 |                                                        |
| 5207 | Beban Sampel/Barang Promosi         |             0 |                                                        |
| 5208 | Beban Iklan & Promosi               |    14.000.000 |                                                        |
| 5209 | Beban Administrasi Bank             |       300.000 |                                                        |
| 5210 | Beban Bunga Pinjaman                |    19.000.000 |                                                        |
| 6101 | Selisih Pembulatan Kas              |               |                                                      0 |

**Jangan jumlahkan kolom saldo tabel di atas langsung** — itu saldo NET per akun (setelah dikurangi sisi lawannya), bukan total sisi Debit/Kredit mentah. Angka yang WAJIB dicek di Trial Balance sistem adalah **total Debit vs total Kredit versi sistem sendiri** (menjumlah sisi asli tiap baris GL sebelum di-net-kan per akun) — itu harus persis **8.400.705.000 = 8.400.705.000** (total seluruh sisi Debit dan Kredit dari 176 jurnal, lihat rincian di file 01 §Checkpoint dan file 02 §Checkpoint Final).

| Skenario                                         | Langkah di UI                                                                                                                                        | Hasil                                                                                                                                                                                                                                   |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — Trial Balance total                    | Buka **General Ledger** tab **Trial Balance**, filter tanggal s/d 2026-08-31 (atau tanpa filter kalau semua transaksi ada di rentang ini) → jalankan | Total Debit = Total Kredit = **8.400.705.000**, tidak ada selisih                                                                                                                                                                       |
| **Positif — verifikasi saldo per akun**          | Bandingkan saldo tiap akun di tabel hasil UI dengan tabel acuan di atas, akun per akun                                                               | Semua harus persis sama — kalau ada yang beda, cek dulu apakah semua 176 jurnal benar-benar sudah Posted (bukan masih draft), baru curigai bug                                                                                          |
| **Positif — akumulasi penyusutan (kontra-aset)** | Cek baris 1202 di Trial Balance                                                                                                                      | Saldo **negatif 23.750.000** (mengurangi Aset Tetap), BUKAN ditambahkan positif — pembuktian `normal_balance:debit` pada akun kontra tetap bekerja benar walau isinya selalu dikredit (lihat "Kontra-akun" di `../accounting/00-...md`) |
| Netralisasi                                      | — (laporan read-only, tidak ada state yang perlu dikembalikan)                                                                                       |                                                                                                                                                                                                                                         |

## 2. Trial Balance FY2025 Saja (s/d 31 Desember 2025) — untuk Close Fiscal Year

**Kenapa perlu snapshot terpisah:** Close Fiscal Year (file 04) butuh angka Trial Balance PERSIS di titik 31 Desember 2025, SEBELUM transaksi Januari 2026 masuk — kalau kamu kerjakan file 04 SETELAH semua transaksi 2026 sudah posted (urutan normal kalau ikuti suite ini urut), filter tanggal `Date To: 2025-12-31` di laporan ini WAJIB dipakai supaya tidak ketercampur.

| Kode                                 | Akun    |        Saldo |
| ------------------------------------ | ------- | -----------: |
| 1101 Kas Kecil                       | Debit   |    9.800.000 |
| 1102 Bank BCA                        | Debit   |  344.450.000 |
| 1103 Piutang Dagang                  | Debit   |            0 |
| 1104 Persediaan Barang Dagang        | Debit   |   60.000.000 |
| 1105 PPN Masukan                     | Debit   |   79.200.000 |
| 1201 Peralatan Toko                  | Debit   |   60.000.000 |
| 1202 Akum. Penyusutan                | (Debit) | (13.750.000) |
| 2101 Utang Dagang                    | Kredit  |   61.050.000 |
| 2102 PPN Keluaran                    | Kredit  |  105.600.000 |
| 2103 Utang PPh 21 Karyawan           | Kredit  |            0 |
| 2105 Pinjaman Bank Jangka Pendek     | Kredit  |   56.000.000 |
| 3101 Modal Pemilik                   | Kredit  |  290.000.000 |
| 4101 Penjualan Barang Dagang         | Kredit  |  960.000.000 |
| 5101 Harga Pokok Penjualan           | Debit   |  600.000.000 |
| 5201 Beban Sewa Toko                 | Debit   |   96.000.000 |
| 5202 Beban Gaji Karyawan             | Debit   |  180.000.000 |
| 5203 Beban Listrik & Air             | Debit   |   24.000.000 |
| 5204 Beban Penyusutan Peralatan Toko | Debit   |   13.750.000 |
| 5205 Beban Selisih Kas               | Debit   |      200.000 |
| 5208 Beban Iklan & Promosi           | Debit   |    8.000.000 |
| 5210 Beban Bunga Pinjaman            | Debit   |   11.000.000 |

Total Debit = Total Kredit = **5.003.400.000**. Total Pendapatan FY2025 = 960.000.000, Total Beban FY2025 = 932.950.000 (rincian: 600.000.000 + 96.000.000 + 180.000.000 + 24.000.000 + 13.750.000 + 200.000 + 8.000.000 + 11.000.000) → **Laba Bersih FY2025 = 27.050.000**.

| Skenario | Langkah di UI                                                                                                                          | Hasil                                                                                                                                                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif  | Buka **General Ledger** tab **Trial Balance**, isi filter **Date To: 2025-12-31** (kosongkan Date From atau isi 2025-01-01) → jalankan | Hasil harus persis sama dengan tabel di atas — kalau filter tanggal ini malah ikut menampilkan saldo Januari 2026, catat sebagai temuan (filter tanggal Trial Balance tidak bekerja benar) |

## 3. Detail Ledger — Utang Dagang (2101), Contoh Running Balance Lintas Bulan

**Halaman:** `accounting/general-ledger` tab Detail Ledger, filter Account `<Utang Dagang>`.

**Kenapa akun ini dipilih sebagai contoh:** saldo Utang Dagang BERUBAH tiap bulan (naik saat ada pembelian kredit baru, turun saat dibayar) — bagus untuk membuktikan `running_balance` per baris dihitung benar secara berurutan, bukan cuma total akhir yang kebetulan benar.

| Tanggal    | Jurnal                          |      Debit |     Kredit | Running Balance (harus urut begini) |
| ---------- | ------------------------------- | ---------: | ---------: | ----------------------------------: |
| 2025-01-10 | Pembelian persediaan kredit Jan |            | 61.050.000 |                          61.050.000 |
| 2025-02-10 | Pembelian persediaan kredit Feb |            | 61.050.000 |                         122.100.000 |
| 2025-02-15 | Pembayaran utang dagang Feb     | 61.050.000 |            |                          61.050.000 |
| 2025-03-10 | Pembelian persediaan kredit Mar |            | 61.050.000 |                         122.100.000 |
| 2025-03-15 | Pembayaran utang dagang Mar     | 61.050.000 |            |                          61.050.000 |
| 2025-04-10 | Pembelian persediaan kredit Apr |            | 61.050.000 |                         122.100.000 |
| 2025-04-15 | Pembayaran utang dagang Apr     | 61.050.000 |            |                          61.050.000 |

**Pola berulang ini bertahan sampai Desember 2025** (saldo akhir tiap bulan selalu balik ke 61.050.000, "gigi gergaji" naik-turun) — sengaja didesain steady-state supaya gampang diverifikasi manual. **Pola berubah di 2 titik penting**, jadikan ini verifikasi tambahan:

1. **Januari 2026**: pembayaran (15 Jan) masih melunasi pembelian **Desember 2025** (61.050.000, rate lama), sementara pembelian BARU bulan itu (10 Jan) sudah pakai rate FY2026 (66.600.000) — jadi running balance akhir Januari 2026 = 66.600.000 (BUKAN 61.050.000 lagi).
2. **April 2026**: ada baris tambahan Retur Pembelian (12 April, Debit 11.100.000) DI ANTARA siklus pembelian-pembayaran normal — running balance turun sesaat sebelum pembayaran rutin bulan itu jalan.

| Skenario                           | Langkah di UI                                                                                                               | Hasil                                                                                                                                                                                                                                                                            |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                            | Buka **General Ledger** tab **Detail Ledger**, filter Account `<Utang Dagang>`, Date From `2025-01-01` Date To `2025-04-30` | Baris & `running_balance` persis seperti tabel di atas                                                                                                                                                                                                                           |
| **Positif — titik transisi tahun** | Ganti filter Date To jadi `2026-01-31`                                                                                      | Baris terakhir (pembayaran 15 Jan 2026) running balance turun ke 61.050.000 dulu, lalu baris pembelian 10 Jan (yang tanggalnya lebih awal — cek urutan SORT by date, bukan sort by ID) naik ke 66.600.000 — verifikasi urutan baris sesuai TANGGAL transaksi, bukan urutan input |
| Netralisasi                        | — (laporan read-only)                                                                                                       |                                                                                                                                                                                                                                                                                  |

## 4. Summary by Account — Filter Dimensi Business Unit (Toko Pusat vs Toko Cabang)

**Halaman:** `accounting/general-ledger` tab Summary by Account, filter `business_unit_id`.

**Angka acuan** (akumulasi seluruh 20 bulan, Januari 2025-Agustus 2026):

| Business Unit     | Akun                    | Total Kredit (Omzet) | Perhitungan                                                                              |
| ----------------- | ----------------------- | -------------------: | ---------------------------------------------------------------------------------------- |
| Toko Pusat        | Penjualan Barang Dagang |        1.040.000.000 | 50jt × 12 bulan (2025) + 55jt × 8 bulan (2026) = 600jt + 440jt                           |
| Toko Cabang       | Penjualan Barang Dagang |          624.000.000 | 30jt × 12 bulan (2025) + 33jt × 8 bulan (2026) = 360jt + 264jt                           |
| *(tanpa dimensi)* | Penjualan Barang Dagang |           20.000.000 | Penjualan kredit customer korporat Jan 2026 — sengaja TIDAK didimensikan ke toko manapun |
| **Total**         |                         |    **1.684.000.000** | Harus persis sama dengan saldo 4101 di Trial Balance §1                                  |

| Skenario                                                                  | Langkah di UI                                                                                                                | Hasil                                                                                                                    |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Positif                                                                   | Buka **General Ledger** tab **Summary by Account**, filter Business Unit `<Toko Pusat>`, Account `<Penjualan Barang Dagang>` | Total = 1.040.000.000                                                                                                    |
| Positif                                                                   | Ulangi filter Business Unit `<Toko Cabang>`                                                                                  | Total = 624.000.000                                                                                                      |
| **Positif — verifikasi total 2 toko + tanpa dimensi = total konsolidasi** | Jumlahkan hasil 2 baris di atas + 20.000.000 (transaksi tanpa BU)                                                            | Harus persis 1.684.000.000, sama dengan Trial Balance tanpa filter                                                       |
| Positif                                                                   | Filter Business Unit `<Toko Pusat>`, Account `<Beban Sewa Toko>`                                                             | Total = 166.400.000 (SEMUA baris Beban Sewa Toko didimensikan ke Toko Pusat di suite ini, lihat catatan dimensi file 01) |
| Netralisasi                                                               | — (laporan read-only)                                                                                                        |                                                                                                                          |

## Referensi Silang

- [`01-jurnal-transaksi-2025.id.md`](./01-jurnal-transaksi-2025.id.md) / [`02-jurnal-transaksi-2026.id.md`](./02-jurnal-transaksi-2026.id.md) — sumber seluruh 176 jurnal & checkpoint kuartalan
- [`04-tutup-periode-dan-tahun-fiskal.id.md`](./04-tutup-periode-dan-tahun-fiskal.id.md) — pakai angka §2 file ini (Trial Balance FY2025) sebagai acuan closing entry
- [`05-laporan-keuangan.id.md`](./05-laporan-keuangan.id.md) — Neraca/Laba Rugi/Arus Kas, angka bersumber dari Trial Balance §1 & §2 file ini
- [`../accounting/02-general-ledger-neraca-saldo.id.md`](../accounting/02-general-ledger-neraca-saldo.id.md) — pola dasar pengujian GL/Trial Balance yang direuse di sini
