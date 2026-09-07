---
title: (Manufaktur) — Varian 2 — 03. Anggaran Kuartalan & Aset Tetap
category: accounting-manufaktur-2
description: Budget vs Actual per kuartal (termasuk stress-test pembulatan split 4-kuartal), penyusutan Mesin Produksi (garis lurus) & Kendaraan (saldo menurun) dari file 01 §1.8, dijalankan SEBELUM tutup periode Q1 (urutan sengaja, lihat catatan).
visibility: internal
---

# 03. Anggaran Kuartalan & Aset Tetap

> Prasyarat: [`01`](./01-jurnal-manual-arus-biaya-produksi-dan-pinjaman.id.md) §1.8 (Mesin Produksi & Kendaraan sudah terdaftar + jurnal akuisisi posted).
>
> **⚠️ Urutan file ini SENGAJA sebelum [`04-tutup-periode-kuartalan-dan-tahun-fiskal.id.md`](./04-tutup-periode-kuartalan-dan-tahun-fiskal.id.md)** — penyusutan bulanan HARUS dijalankan sebelum periode yang menaunginya di-close, karena setelah closed, `runDepreciation()` (yang auto-post jurnal) akan gagal dengan guard periode yang sama seperti jurnal manual biasa. File 04 nanti punya 1 skenario KHUSUS yang sengaja membuktikan ini (lupa jalankan penyusutan Februari sebelum Q1 ditutup), jadi urutan di sini juga bagian dari desain testing, bukan kebetulan.

## 3.1 Anggaran Kuartalan (**Budgets**)

> **⚠️ Koreksi struktur payload (terverifikasi dari `App\Http\Controllers\Accounting\Budgets.php`)**: prefix route yang benar adalah **Budgets** (BUKAN `client-master/budgets/*`). Tidak ada endpoint terpisah untuk baris — `create` menerima SEKALIGUS header (`fiscal_year_id`, `name`, `description`) dan array `lines[]` (`account_id`, `business_unit_id` nullable, `accounting_period_id`, `budgeted_amount`) dalam SATU payload. Tidak ada field `chart_of_account_id`/`total_amount` di level header. Tidak ada `period_label:"Q1"` — wajib `accounting_period_id` (ID periode kuartalan asli; backend validasi periode itu harus milik `fiscal_year_id` yang sama).

### 3.1.1 Budget vs Actual — Angka Bersih (Verifikasi Fungsional)

Anggaran tahunan BBN-02 (Beban Overhead Pabrik Non-Produksi) Rp 20.000.000, dibagi rata 4 kuartal.

| Skenario                          | Payload kunci                                                                                                                                                                                                   | Hasil                                                                                                                                                           |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — buat anggaran + 4 baris | `POST accounting/budgets/create {fiscal_year_id:<FY2026>, name:"Anggaran Overhead Pabrik 2026", lines:[{account_id:<BBN-02>, accounting_period_id:<Q1>, budgeted_amount:5000000},{...Q2...},{...Q3...},{...Q4...}]}` (4 baris sekaligus dalam SATU request) | 201, total 4×5.000.000 = **20.000.000 tepat** (habis dibagi rata, tidak ada sisa pembulatan di skenario ini)                                         |
| **Positif — Budget vs Actual Q1** | `POST accounting/budgets/vs-actual {slug:<budget dari create>}` — TIDAK ada param filter kuartal, response balikin SEMUA baris (`rows[]`) untuk 4 kuartal sekaligus                                                                                                                                   | Cari baris dengan `accounting_period.id = <Q1>` di `rows[]`: `budgeted_amount` = 5.000.000, `actual_amount` = 5.000.000 (dari [`01`](./01-jurnal-manual-arus-biaya-produksi-dan-pinjaman.id.md) §1.4) → **variance = 0, on-budget persis** |
| Netralisasi                       | Hapus anggaran test setelah selesai                                                                                                                                                                             |

### 3.1.2 Stress-Test Pembulatan Split 4-Kuartal

Anggaran tahunan senilai Rp 100.000.001 (sengaja TIDAK habis dibagi 4) untuk BBN-03 (Beban Gaji Non-Produksi, akun yang belum dipakai transaksi apapun di suite ini — aman dipakai eksperimen murni).

> **Dikonfirmasi dari kode**: tidak ada fitur split rata otomatis — `create` cuma menerima `lines[]` mentah, tidak ada logic pembagian di backend. Bukan gap/bug, ini keterbatasan yang memang harus dihitung manual oleh user.

| Skenario                                                                      | Detail                                    | Hasil                                                                                                                                                                      | Label temuan                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — kirim 4 baris manual | `lines:[{...Q1, budgeted_amount:25000000},{...Q2, budgeted_amount:25000000},{...Q3, budgeted_amount:25000000},{...Q4, budgeted_amount:25000001}]` | 201, total 4 baris = **100.000.001 tepat** (backend tidak validasi "harus sama rata", terima nominal custom apa adanya per baris) | ⚠️ Bukan gap — tidak ada endpoint split otomatis, ini murni keterbatasan yang sudah sesuai desain |
| Netralisasi                                                                   | Hapus anggaran test ini                   |

## 3.2 Penyusutan Bulanan — Mesin Produksi (Garis Lurus)

Mesin Pengiris & Penggorengan Otomatis (`MSN-001`, dari file 01 §1.8): akuisisi Rp 180.000.000, residu Rp 18.000.000, umur 60 bulan. Penyusutan bulanan = (180.000.000 − 18.000.000) / 60 = **Rp 2.700.000/bulan**.

| Skenario                                | Detail                                                             | Hasil                                                                                                                                                                                                                                                                                  |
| --------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — Januari                       | Jalankan `runDepreciation()` untuk periode Januari 2026, `MSN-001` | 1 baris `asset_depreciations` baru, nominal **2.700.000 tepat**, `journal_header_id` terisi (jurnal `Dr BBN-04 Beban Penyusutan Mesin Produksi 2.700.000 / Cr AST-10 Akumulasi Penyusutan Mesin Produksi 2.700.000`), `current_book_value` = 180.000.000 − 2.700.000 = **177.300.000** |
| **Negatif — double posting bulan sama** | Jalankan lagi untuk Januari 2026                                   | Ditolak/di-skip, TIDAK ada baris kedua                                                                                                                                                                                                                                                 |
| Netralisasi                             | — (biarkan posted, jadi baseline file 04)                          |

## 3.3 Penyusutan Bulanan — Kendaraan Operasional (Saldo Menurun)

Truck Box Pengiriman (`KND-001`, file 01 §1.8): akuisisi Rp 250.000.000, residu Rp 40.000.000, umur 96 bulan, metode saldo menurun.

> **Formula terverifikasi dari kode** (`FixedAssets::buildDepreciationSchedule()`): metode `declining_balance` pakai double-declining balance — `rate = 2 / useful_life_months` diterapkan ke book value BERJALAN tiap bulan (bukan tarif tetap seperti versi lama dokumen ini). Untuk KND-001: `rate = 2/96 = 2,0833%`.

| Skenario          | Detail                                               | Hasil                                                                                                                                                                                  |
| ----------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — Januari | Jalankan `runDepreciation()` Januari 2026, `KND-001` | Nominal bulan 1 = 250.000.000 × (2/96) = **Rp 5.208.333,33**, `current_book_value` = 250.000.000 − 5.208.333,33 = **244.791.666,67** |
| Netralisasi       | —                                                    |

> **JANGAN jalankan Februari di sini** — file 04 §4.3 sengaja memakai "penyusutan Februari yang belum pernah dijalankan" sebagai skenario negatif (coba jalankan SETELAH Q1 closed). Kalau penasaran ingin memverifikasi ciri saldo-menurun (nominal bulan berjalan makin kecil) SEBELUM Q1 closed, lakukan itu di aset test TERPISAH (bukan `KND-001`), supaya baseline close-year §4.13 tidak berubah. Ekspektasi kalau dites: nominal bulan 2 dihitung dari book value baru (244.791.666,67 × 2/96 ≈ **5.099.826,39**) — HARUS lebih kecil dari bulan 1, kalau sama persis berarti formula-nya diam-diam garis lurus, bukan saldo menurun sungguhan.

## 3.4 Verifikasi Silang — Akumulasi Penyusutan Bersaldo Kontra

| Skenario    | Detail                                                                                                                                                                                      | Hasil                                                                                                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif     | Setelah §3.2-3.3, cek saldo AST-10 & AST-12 di Trial Balance ([`05-general-ledger-trial-balance-dan-laporan-keuangan.id.md`](./05-general-ledger-trial-balance-dan-laporan-keuangan.id.md)) | Keduanya bersaldo NEGATIF (mengurangi total Aset Tetap) — AST-10 = -2.700.000, AST-12 = -5.208.333,33 (setelah Januari saja; kalau Februari kendaraan juga sudah dijalankan per §3.3, AST-12 jadi lebih negatif lagi) |
| Netralisasi | —                                                                                                                                                                                           |

## Ringkasan Beban Penyusutan Januari (Dipakai File 04 §4.11 Close Fiscal Year)

| Akun                                   | Nominal Januari |
| -------------------------------------- | --------------: |
| BBN-04 Beban Penyusutan Mesin Produksi |       2.700.000 |
| BBN-05 Beban Penyusutan Kendaraan      |    5.208.333,33 |

> **Catatan scope**: untuk keperluan close-year di file 04, CUKUP jalankan penyusutan **Januari saja** untuk kedua aset (jangan jalankan Februari/Maret dulu) — file 04 §4.3 sengaja menguji skenario "lupa jalankan penyusutan bulan berikutnya sebelum quarter closed", jadi Februari/Maret harus tetap "belum dijalankan" sampai ke titik itu.

## Referensi Silang

- [`../accounting-manufaktur/03-anggaran-kuartalan-dan-aset-tetap.id.md`](../accounting-manufaktur/03-anggaran-kuartalan-dan-aset-tetap.id.md) — file setara di suite manufaktur varian 1 (CV Sumber Makmur Abadi), kasus identik dengan perusahaan berbeda; bandingkan hasil kalau ada penyimpangan tak terduga

- [`01-jurnal-manual-arus-biaya-produksi-dan-pinjaman.id.md`](./01-jurnal-manual-arus-biaya-produksi-dan-pinjaman.id.md) §1.8 — registrasi & akuisisi kedua aset
- [`04-tutup-periode-kuartalan-dan-tahun-fiskal.id.md`](./04-tutup-periode-kuartalan-dan-tahun-fiskal.id.md) §4.3 — skenario "penyusutan terlambat setelah periode closed"
- [`../accounting/06-aset-tetap-dan-penyusutan.id.md`](../accounting/06-aset-tetap-dan-penyusutan.id.md) — dasar pola penyusutan di suite lama (COGS retail, bukan manufaktur — data TIDAK terkait)
