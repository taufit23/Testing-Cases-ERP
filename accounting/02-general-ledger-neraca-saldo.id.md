---
title: — 02. General Ledger & Neraca Saldo
category: Accounting 1
description: Test case Detail Ledger, Summary by Account, dan Trial Balance untuk skenario PT Retail Nusantara Jaya, termasuk verifikasi filter dimensi Business Unit per toko.
visibility: internal
---

# 02. General Ledger & Neraca Saldo

> Prasyarat: jurnal-jurnal di [`01-jurnal-manual.id.md`](./01-jurnal-manual.id.md) sudah di-post (§1.1-1.4, §1.6). Semua endpoint di **General Ledger**.
>
> **Kenapa file ini penting untuk non-akuntan**: file 01 membuktikan jurnal BISA dibuat & di-post. File ini membuktikan jurnal-jurnal itu benar-benar TERHITUNG dengan benar setelah digabung — 3 laporan di sini (Detail Ledger, Summary by Account, Trial Balance) semuanya baca dari tabel `general_ledgers` yang sama (lihat glosarium "General Ledger" & "Trial Balance" di file 00), cuma beda cara meringkasnya: Detail Ledger = riwayat SATU akun baris-per-baris, Summary by Account = rekap SEMUA akun dalam satu rentang tanggal, Trial Balance = rekap SEMUA akun tapi dicek juga apakah totalnya seimbang.

## 2.1 Detail Ledger — Bank BCA

Bank BCA sudah dipakai di beberapa transaksi: terima modal (+Rp 500.000.000), bayar pembelian (-Rp 111.000.000), bayar sewa (-Rp 20.000.000 atau Rp 18.000.000 setelah koreksi §1.7), bayar gaji (-Rp 80.000.000).

| Skenario                        | Langkah di UI                                                                                                                       | Hasil                                                                                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                         | Buka halaman **General Ledger** (tab **Detail Ledger** aktif default) → di filter bar isi Account `<Bank BCA>`, Date From `2026-01-01`, Date To `2026-01-31` → klik **Search** | Kartu "Opening Balance"/"Period Movement"/"Closing Balance" tampil di atas, tabel di bawah menampilkan baris per transaksi urut tanggal dengan kolom Balance (running balance) konsisten tiap baris (saldo berjalan = saldo sebelumnya ± debit/credit baris itu) |
| **Positif — saldo akhir cocok** | Jumlahkan manual semua debit/credit Bank BCA dari §1.1-1.4/1.7                                                                | Angka di kartu **Closing Balance** = hasil hitung manual                                                                                                       |
| Negatif                         | ⚠️ Tidak bisa diuji lewat UI — dropdown Account cuma menampilkan akun branch aktif, tidak mungkin pilih `chart_of_account_id` fiktif dari situ. Testing tetap via API call: `POST accounting/general-ledger/detail-ledger` dengan `chart_of_account_id` acak | 422/404                                                                                                                                                   |
| Netralisasi                     | — (read-only report)                                                                                                          |

**Sebab-akibat:** `running_balance` (saldo berjalan tiap baris) adalah angka yang paling sering dipakai user akhir untuk "percaya" pembukuannya benar — kalau logikanya salah (mis. lupa tambah `opening_balance` dari sebelum rentang tanggal, atau arah debit/kredit ketuker untuk akun tipe kredit seperti liability), SETIAP baris di bawahnya ikut salah berantai (bukan cuma 1 baris), karena tiap baris = saldo sebelumnya ± transaksi baris itu. Ini kenapa baris "saldo akhir cocok" WAJIB dihitung manual dan dibandingkan — satu baris salah di tengah cukup untuk bikin semua baris setelahnya salah tanpa terlihat.

## 2.2 Summary by Account — Semua Akun

| Skenario                                             | Langkah di UI                                                                                            | Hasil                                                                                                                                                                                                                                                 |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                              | Di halaman **General Ledger**, klik tab **Summary by Account** → isi filter Date From `2026-01-01`, Date To `2026-01-31` (kosongkan Account) → klik **Search** | Tiap akun yang pernah dipakai di §1.1-1.4 muncul sebagai baris tabel dengan kolom Opening/Period/Closing Debit & Credit yang benar — akun yang tidak pernah dipakai (mis. PPN Masukan kalau belum ada pembelian) tidak error, cukup tidak muncul |
| **Positif — filter dimensi Toko (business_unit_id)** | Ulangi dengan filter **Business Unit** diisi `<Toko Pusat>` → Search, lalu ganti jadi `<Toko Cabang>` → Search lagi                  | Baris akun `Penjualan Barang Dagang` harus menunjukkan angka BERBEDA sesuai toko (dari §1.3: Toko Pusat Rp 50.000.000, Toko Cabang Rp 30.000.000) — ini fitur backend Phase 3 item #3, verifikasi filter benar-benar memecah data per dimensi               |
| Netralisasi                                          | — (read-only)                                                                                      |

**Sebab-akibat:** filter `business_unit_id` ini murni "menyaring" data yang SUDAH ditandai dari sisi input jurnal (lihat catatan §1.3 di file 01 — `business_unit_id` di baris jurnal itu opsional). Kalau filter di sini terlihat "kosong"/salah padahal kamu yakin sudah pernah input transaksi ke toko itu, akar masalahnya biasanya BUKAN di endpoint ini, tapi di jurnal sumbernya yang lupa diisi dimensi tokonya — cek dulu jurnal asalnya sebelum menuduh laporan ini yang bug.

## 2.3 Trial Balance (Neraca Saldo)

| Skenario                                    | Langkah di UI                                                                                                                  | Hasil                                                                                                         |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Positif                                     | Di halaman **General Ledger**, klik tab **Trial Balance** → filter **Period** pilih `<Januari 2026>` → klik **Search**                                     | Tabel menampilkan kolom Beginning/Period Movement/Ending Balance per akun, baris **Total** di bawah menunjukkan **Total debit = total kredit** di seluruh akun — ini pengecekan paling dasar kesehatan pembukuan double-entry |
| **Negatif (kondisi yang harus diwaspadai)** | Kalau ada jurnal yang di-post tapi ternyata tidak balance (harusnya tidak mungkin lolos validasi create, tapi cek ulang) — buka tab Trial Balance dengan filter periode yang sama | Baris Total timpang (debit ≠ kredit) — kalau ini terjadi, itu bug serius (harus lapor, bukan diabaikan)                      |
| Netralisasi                                 | — (read-only)                                                                                                            |

**Sebab-akibat:** "total debit = total kredit" ini BUKAN sekadar pengecekan tambahan — ini SATU-SATUNYA sinyal otomatis di seluruh sistem yang bisa mendeteksi kalau ada yang salah di pembukuan double-entry (lihat "Balanced" di Konsep Dasar file 00). Kalau Trial Balance timpang, itu artinya ada baris jurnal yang tercatat cuma sebelah (debit tanpa kredit pasangannya, atau sebaliknya) — sesuatu yang SEHARUSNYA mustahil terjadi kalau validasi balanced di file 01 bekerja benar. Makanya baris "Negatif" ditandai "harus lapor, bukan diabaikan": kalau ini kejadian, akar masalahnya ada di endpoint create/post jurnal (file 01), bukan di laporan ini.

## 2.4 Dua Endpoint Trial Balance yang Sengaja Ada (Bukan Bug Duplikat)

Ada 2 cara akses Trial Balance — `accounting/general-ledger/trial-balance` (dipakai internal FE tab) dan `reports/trial-balance` (redirect ke tab yang sama, hasil konsolidasi Phase 1 item D). Verifikasi keduanya menunjukkan angka **identik** untuk periode & branch yang sama — kalau beda, itu bug regresi.

| Skenario    | Detail                                  | Hasil                                                                                |
| ----------- | --------------------------------------- | ------------------------------------------------------------------------------------ |
| Positif     | Buka halaman FE `reports/trial-balance` | Redirect otomatis ke `accounting/general-ledger?view=trial-balance` dengan data sama |
| Netralisasi | —                                       |

## Referensi Silang

- [`01-jurnal-manual.id.md`](./01-jurnal-manual.id.md) — sumber transaksi yang diverifikasi di file ini
- [`04-laporan-keuangan.id.md`](./04-laporan-keuangan.id.md) — Trial Balance yang seimbang adalah prasyarat Neraca (Balance Sheet) yang seimbang
