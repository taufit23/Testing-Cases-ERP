---
title: (F&B Kafe) — 05. Aset Tetap — Peralatan Dapur & Renovasi Interior
category: accounting-fnb-kafe
description: Penyusutan bulanan Peralatan Dapur (garis lurus) dan Renovasi Interior Outlet BSD (saldo menurun) dari file 01 §1.14-1.15, dijalankan SEBELUM tutup periode Februari — urutan sengaja, sama pola dengan suite manufaktur.
visibility: internal
---

# 05. Aset Tetap — Peralatan Dapur & Renovasi Interior

> Prasyarat: [`01`](./01-jurnal-harian-penjualan-dan-akumulasi.id.md) §1.14-1.15 (Peralatan Dapur & Renovasi Interior sudah terdaftar + jurnal akuisisi posted).
>
> **⚠️ Urutan file ini SENGAJA sebelum §3.3 (close Februari) di [`03-tutup-periode-bulanan-dan-tahun-fiskal.id.md`](./03-tutup-periode-bulanan-dan-tahun-fiskal.id.md)** — penyusutan Februari HARUS dijalankan sebelum periode Februari di-close, karena setelah closed, `run-depreciation` (yang auto-post jurnal) akan gagal dengan guard periode yang sama seperti jurnal manual biasa. File `03` §3.4 punya skenario KHUSUS yang membuktikan ini.
>
> Endpoint terkonfirmasi via `routes/fixed_assets.php`: **Assets** (BUKAN `finance/fixed-assets/*`).

## 5.1 Registrasi Aset (Regression Check dari File 01)

| Skenario | Detail                                                                                                                                                    | Hasil                                                                                                                                                                              |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST fixed-assets/assets/list` filter `category:"Peralatan Dapur"` atau `"Renovasi/Leasehold Improvement"`                                               | 2 aset muncul: `KDP-001` (48.000.000, straight_line, 60 bulan) dan `REN-001` (36.000.000, declining_balance, 36 bulan) — keduanya `status:active`, `acquisition_date:"2026-02-06"` |
| Positif  | `POST fixed-assets/assets/calculate-depreciation {id:<KDP-001>, period:"2026-02"}` (kalkulasi tanpa posting, kalau endpoint ini tersedia sebagai preview) | Preview nominal **750.000**, TIDAK membuat baris `asset_depreciations` atau jurnal apapun — murni simulasi                                                                         |

## 5.2 Penyusutan Bulanan — Peralatan Dapur & Mesin Kopi (Garis Lurus)

`KDP-001`: akuisisi Rp 48.000.000, residu Rp 3.000.000, umur 60 bulan. Penyusutan bulanan = (48.000.000 − 3.000.000) / 60 = **Rp 750.000/bulan** (flat, tidak berubah tiap bulan — ciri khas garis lurus).

| Skenario                                                         | Detail                                                                       | Hasil                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif — Februari                                               | `POST fixed-assets/assets/run-depreciation` periode Februari 2026, `KDP-001` | 1 baris `asset_depreciations` baru, nominal **750.000 tepat**, `journal_header_id` terisi (jurnal `Dr BBN-05 Beban Penyusutan Peralatan Dapur 750.000 / Cr AST-09 Akumulasi Penyusutan Peralatan Dapur 750.000`), `current_book_value` = 48.000.000 − 750.000 = **47.250.000** |
| **Negatif — double posting bulan sama**                          | Jalankan lagi untuk Februari 2026                                            | Ditolak/di-skip, TIDAK ada baris kedua, `current_book_value` TIDAK berubah lagi                                                                                                                                                                                                |
| Positif — Maret (dites lagi di file `03` §3.4, opsional di sini) | `run-depreciation` Maret 2026, `KDP-001`                                     | Nominal bulan 2 = **750.000 lagi** (tetap flat, ciri garis lurus — beda dari REN-001 di bawah) — `current_book_value` = 47.250.000 − 750.000 = **46.500.000**                                                                                                                  |
| Netralisasi                                                      | — (biarkan posted, jadi baseline file `03` §3.11 close-year)                 |

## 5.3 Penyusutan Bulanan — Renovasi Interior Outlet BSD (Saldo Menurun)

`REN-001`: akuisisi Rp 36.000.000, residu Rp 0, umur 36 bulan, metode saldo menurun. Untuk test ini pakai tarif bulanan tetap **2%** dari book value berjalan (parameter internal implementasi — kalau formula aktual beda dari asumsi ini, sesuaikan angka Hasil di bawah dengan formula sebenarnya, JANGAN paksa cocok ke angka di sini).

| Skenario                                                              | Detail                                            | Hasil                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — Februari                                                    | `run-depreciation` Februari 2026, `REN-001`       | Nominal bulan 1 = 36.000.000 × 2% = **Rp 720.000** (kalau tarif aktual beda, catat tarif sebenarnya dari hasil), `current_book_value` = 36.000.000 − 720.000 = **35.280.000**                                                                                                         |
| **Positif — Maret (verifikasi ciri saldo-menurun, nominal MENGECIL)** | `run-depreciation` Maret 2026, `REN-001`          | Nominal bulan 2 dihitung dari book value BARU = 35.280.000 × 2% = **Rp 705.600** — HARUS lebih kecil dari bulan 1 (720.000), kalau sama persis berarti formula-nya diam-diam garis lurus, bukan saldo menurun sungguhan. `current_book_value` = 35.280.000 − 705.600 = **34.574.400** |
| Netralisasi                                                           | — (biarkan posted, jadi baseline file `03` §3.11) |

## 5.4 Verifikasi Silang — Akumulasi Penyusutan Bersaldo Kontra

| Skenario                               | Detail                                                                        | Hasil                                                                                                                                                                                                        |
| -------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif                                | Setelah §5.2-5.3 (Februari+Maret), cek saldo AST-09 & AST-11 di Trial Balance | Keduanya bersaldo NEGATIF (mengurangi total Aset Tetap) — AST-09 = **-1.500.000** (750.000×2), AST-11 = **-1.425.600** (720.000+705.600)                                                                     |
| **Positif — Neraca Aset Tetap Bersih** | `reports/balance-sheet` setelah §5.2-5.3                                      | Nilai buku bersih Peralatan Dapur = 48.000.000 − 1.500.000 = **46.500.000**, Renovasi Interior = 36.000.000 − 1.425.600 = **34.574.400** — cocok dengan `current_book_value` masing-masing aset di §5.2/§5.3 |

## 5.5 Pelepasan Aset (**Disposals**) — Skenario Opsional

Skenario tambahan untuk verifikasi jalur disposal (tidak dipakai baseline close-year §3.11, aset test TERPISAH supaya baseline tidak berubah).

| Skenario    | Detail                                                                                                                                                                             | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persiapan   | Daftar aset test `KDP-TEST-DISPOSAL`, kecil saja: cost 3.000.000, residu 0, useful_life 12 bulan, straight_line, `acquisition_date:"2026-01-01"`                                   | 201                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Positif     | Jalankan `run-depreciation` 1 bulan (250.000), lalu `POST fixed-assets/disposals/create {asset_id, disposal_date:"2026-02-06", disposal_proceeds:2500000, disposal_method:"sold"}` | 201 — cek jurnal otomatis: `Dr Kas/Bank 2.500.000, Dr Akumulasi Penyusutan 250.000, Cr Aset Tetap 3.000.000` (menghapus nilai buku), selisih book value (2.750.000) vs proceeds (2.500.000) = **rugi pelepasan 250.000** harus tercatat di akun gain/loss disposal — cek akun apa yang dipakai sistem untuk baris ini (kalau tidak eksplisit disebutkan di `AssetDisposals`, catat sebagai temuan dokumentasi kalau membingungkan) |
| **Negatif** | Disposal untuk aset yang sudah pernah didisposal                                                                                                                                   | Ditolak, tidak bisa disposal 2x                                                                                                                                                                                                                                                                                                                                                                                                    |
| Netralisasi | Hapus aset test & disposal-nya setelah selesai — TIDAK memengaruhi `KDP-001`/`REN-001`                                                                                             |

## Ringkasan Beban Penyusutan (Dipakai File `03` §3.11 Close Fiscal Year)

| Akun                                      | Februari |   Maret | Total (kalau §3.4 Maret dijalankan) |
| ----------------------------------------- | -------: | ------: | ----------------------------------: |
| BBN-05 Beban Penyusutan Peralatan Dapur   |  750.000 | 750.000 |                           1.500.000 |
| BBN-06 Beban Penyusutan Renovasi Interior |  720.000 | 705.600 |                           1.425.600 |

## Referensi Silang

- [`01-jurnal-harian-penjualan-dan-akumulasi.id.md`](./01-jurnal-harian-penjualan-dan-akumulasi.id.md) §1.14-1.15 — registrasi & akuisisi kedua aset
- [`03-tutup-periode-bulanan-dan-tahun-fiskal.id.md`](./03-tutup-periode-bulanan-dan-tahun-fiskal.id.md) §3.4 — skenario "penyusutan susulan setelah periode closed"
- [`../accounting-manufaktur/03-anggaran-kuartalan-dan-aset-tetap.id.md`](../accounting-manufaktur/03-anggaran-kuartalan-dan-aset-tetap.id.md) — dasar pola penyusutan garis lurus vs saldo menurun, dites ulang dengan tarif & aset berbeda di file ini
