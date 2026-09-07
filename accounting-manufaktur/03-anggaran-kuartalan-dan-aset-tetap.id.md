---
title: (Manufaktur) — 03. Anggaran Kuartalan & Aset Tetap
category: accounting-manufaktur
description: Budget vs Actual per kuartal (termasuk stress-test pembulatan split 4-kuartal), penyusutan Mesin Produksi (garis lurus) & Kendaraan (saldo menurun) dari file 01 §1.8, dijalankan SEBELUM tutup periode Q1 (urutan sengaja, lihat catatan).
visibility: internal
---

# 03. Anggaran Kuartalan & Aset Tetap

> Prasyarat: [`01`](./01-jurnal-manual-arus-biaya-produksi-dan-pinjaman.id.md) §1.8 (Mesin Produksi & Kendaraan sudah terdaftar + jurnal akuisisi posted).
>
> **⚠️ Urutan file ini SENGAJA sebelum [`04-tutup-periode-kuartalan-dan-tahun-fiskal.id.md`](./04-tutup-periode-kuartalan-dan-tahun-fiskal.id.md)** — penyusutan bulanan HARUS dijalankan sebelum periode yang menaunginya di-close, karena setelah closed, `runDepreciation()` (yang auto-post jurnal) akan gagal dengan guard periode yang sama seperti jurnal manual biasa. File 04 nanti punya 1 skenario KHUSUS yang sengaja membuktikan ini (lupa jalankan penyusutan Februari sebelum Q1 ditutup), jadi urutan di sini juga bagian dari desain testing, bukan kebetulan.

## 3.1 Anggaran Kuartalan (`client-master/budgets`)

### 3.1.1 Budget vs Actual — Angka Bersih (Verifikasi Fungsional)

Anggaran tahunan BBN-02 (Beban Overhead Pabrik Non-Produksi) Rp 20.000.000, dibagi rata 4 kuartal.

| Skenario                          | Payload kunci                                                                                                                                                                                                   | Hasil                                                                                                                                                           |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — buat anggaran tahunan   | `POST client-master/budgets/create {fiscal_year_id:<FY2026>, chart_of_account_id:<BBN-02>, name:"Anggaran Overhead Pabrik 2026", total_amount:20000000}`                                                        | 201                                                                                                                                                             |
| Positif — baris per kuartal       | 4× `POST client-master/budgets/lines/create {budget_id, period_label:"Q1"/"Q2"/"Q3"/"Q4", amount:5000000}` (atau endpoint sejenis — sesuaikan dengan struktur aktual, cek FE `client-master/budget/create.vue`) | 201 tiap baris, total 4×5.000.000 = **20.000.000 tepat** (habis dibagi rata, tidak ada sisa pembulatan di skenario ini)                                         |
| **Positif — Budget vs Actual Q1** | `POST client-master/budgets/vs-actual` (atau endpoint sejenis) filter Q1-2026                                                                                                                                   | Budget Q1 = 5.000.000, Actual Q1 = 5.000.000 (dari [`01`](./01-jurnal-manual-arus-biaya-produksi-dan-pinjaman.id.md) §1.4) → **variance = 0, on-budget persis** |
| Netralisasi                       | Hapus anggaran test setelah selesai                                                                                                                                                                             |

### 3.1.2 Stress-Test Pembulatan Split 4-Kuartal

Anggaran tahunan senilai Rp 100.000.001 (sengaja TIDAK habis dibagi 4) untuk BBN-03 (Beban Gaji Non-Produksi, akun yang belum dipakai transaksi apapun di suite ini — aman dipakai eksperimen murni).

| Skenario                                                                      | Detail                                    | Hasil                                                                                                                                                                      | Label temuan                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — buat & split otomatis (kalau fitur "split rata" ada di FE/endpoint) | Total Rp 100.000.001 displit ke 4 kuartal | Cek behavior aktual: idealnya Q1=Q2=Q3=25.000.000 dan Q4=25.000.001 (sisa pembulatan dibebankan ke baris TERAKHIR), sehingga jumlah ke-4 baris balik PERSIS ke 100.000.001 | Kalau totalnya meleset dari 100.000.001 (mis. jadi 100.000.000 genap, kehilangan Rp 1) → 🆕 **fitur baru**: split perlu logic "sisa pembulatan ke baris terakhir". Kalau TIDAK ada fitur split otomatis sama sekali (harus input 4 baris manual satu-satu) → bukan bug, cukup catat sebagai keterbatasan (⚠️ bukan gap, User HARUS jumlah sendiri 4 baris manual supaya totalnya pas) |
| Netralisasi                                                                   | Hapus anggaran test ini                   |

## 3.2 Penyusutan Bulanan — Mesin Produksi (Garis Lurus)

Mesin Pengiris & Penggorengan Otomatis (`MSN-001`, dari file 01 §1.8): akuisisi Rp 180.000.000, residu Rp 18.000.000, umur 60 bulan. Penyusutan bulanan = (180.000.000 − 18.000.000) / 60 = **Rp 2.700.000/bulan**.

| Skenario                                | Detail                                                             | Hasil                                                                                                                                                                                                                                                                                  |
| --------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — Januari                       | Jalankan `runDepreciation()` untuk periode Januari 2026, `MSN-001` | 1 baris `asset_depreciations` baru, nominal **2.700.000 tepat**, `journal_header_id` terisi (jurnal `Dr BBN-04 Beban Penyusutan Mesin Produksi 2.700.000 / Cr AST-10 Akumulasi Penyusutan Mesin Produksi 2.700.000`), `current_book_value` = 180.000.000 − 2.700.000 = **177.300.000** |
| **Negatif — double posting bulan sama** | Jalankan lagi untuk Januari 2026                                   | Ditolak/di-skip, TIDAK ada baris kedua                                                                                                                                                                                                                                                 |
| Netralisasi                             | — (biarkan posted, jadi baseline file 04)                          |

## 3.3 Penyusutan Bulanan — Kendaraan Operasional (Saldo Menurun)

Truck Box Pengiriman (`KND-001`, file 01 §1.8): akuisisi Rp 250.000.000, residu Rp 40.000.000, umur 96 bulan, metode saldo menurun. Untuk test ini pakai tarif bulanan tetap **1,6%** dari book value berjalan (parameter internal implementasi — kalau formula aktual beda dari asumsi ini, sesuaikan angka Hasil di bawah dengan formula sebenarnya, JANGAN paksa cocok ke angka di sini).

| Skenario          | Detail                                               | Hasil                                                                                                                                                                                  |
| ----------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — Januari | Jalankan `runDepreciation()` Januari 2026, `KND-001` | Nominal bulan 1 = 250.000.000 × 1,6% = **Rp 4.000.000** (kalau tarif aktual beda, catat tarif sebenarnya dari hasil), `current_book_value` = 250.000.000 − 4.000.000 = **246.000.000** |
| Netralisasi       | —                                                    |

> **JANGAN jalankan Februari di sini** — file 04 §4.3 sengaja memakai "penyusutan Februari yang belum pernah dijalankan" sebagai skenario negatif (coba jalankan SETELAH Q1 closed). Kalau penasaran ingin memverifikasi ciri saldo-menurun (nominal bulan berjalan makin kecil) SEBELUM Q1 closed, lakukan itu di aset test TERPISAH (bukan `KND-001`), supaya baseline close-year §4.13 tidak berubah. Ekspektasi kalau dites: nominal bulan 2 dihitung dari book value baru (246.000.000 × 1,6% ≈ 3.936.000) — HARUS lebih kecil dari bulan 1, kalau sama persis berarti formula-nya diam-diam garis lurus, bukan saldo menurun sungguhan.

## 3.4 Verifikasi Silang — Akumulasi Penyusutan Bersaldo Kontra

| Skenario    | Detail                                                                                                                                                                                      | Hasil                                                                                                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif     | Setelah §3.2-3.3, cek saldo AST-10 & AST-12 di Trial Balance ([`05-general-ledger-trial-balance-dan-laporan-keuangan.id.md`](./05-general-ledger-trial-balance-dan-laporan-keuangan.id.md)) | Keduanya bersaldo NEGATIF (mengurangi total Aset Tetap) — AST-10 = -2.700.000, AST-12 = -4.000.000 (setelah Januari saja; kalau Februari kendaraan juga sudah dijalankan per §3.3, AST-12 jadi lebih negatif lagi) |
| Netralisasi | —                                                                                                                                                                                           |

## Ringkasan Beban Penyusutan Januari (Dipakai File 04 §4.11 Close Fiscal Year)

| Akun                                   | Nominal Januari |
| -------------------------------------- | --------------: |
| BBN-04 Beban Penyusutan Mesin Produksi |       2.700.000 |
| BBN-05 Beban Penyusutan Kendaraan      |       4.000.000 |

> **Catatan scope**: untuk keperluan close-year di file 04, CUKUP jalankan penyusutan **Januari saja** untuk kedua aset (jangan jalankan Februari/Maret dulu) — file 04 §4.3 sengaja menguji skenario "lupa jalankan penyusutan bulan berikutnya sebelum quarter closed", jadi Februari/Maret harus tetap "belum dijalankan" sampai ke titik itu.

## Referensi Silang

- [`01-jurnal-manual-arus-biaya-produksi-dan-pinjaman.id.md`](./01-jurnal-manual-arus-biaya-produksi-dan-pinjaman.id.md) §1.8 — registrasi & akuisisi kedua aset
- [`04-tutup-periode-kuartalan-dan-tahun-fiskal.id.md`](./04-tutup-periode-kuartalan-dan-tahun-fiskal.id.md) §4.3 — skenario "penyusutan terlambat setelah periode closed"
- [`../accounting/06-aset-tetap-dan-penyusutan.id.md`](../accounting/06-aset-tetap-dan-penyusutan.id.md) — dasar pola penyusutan di suite lama (COGS retail, bukan manufaktur — data TIDAK terkait)
