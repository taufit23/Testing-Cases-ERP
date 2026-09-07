---
title: (CORETAX) — 03. Tutup Periode & Tahun Fiskal
category: accounting-coretax
description: Close/Lock/Reopen Accounting Period bulanan untuk branch Pusat, termasuk demonstrasi langsung dampak duplikasi accounting_periods dari seeder.
visibility: internal
---

# 03. Tutup Periode & Tahun Fiskal

> Prasyarat: [`01`](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md) & [`02`](./02-general-ledger-dan-trial-balance.id.md) selesai (transaksi Agustus 2026 sudah posted).
>
> **Sudah di-seed otomatis**: `database/seeders/CoretaxPeriodCloseSeeder.php` sudah close+lock KEDUA baris duplikat "Juli 2026" (FY2026-07) untuk branch Pusat. **Agustus 2026 sengaja TIDAK di-seed close** — dibiarkan terbuka supaya transaksi CRTX-T1..T14 (file 01) dan eksplorasi manual lanjutan tetap bisa dilakukan tanpa perlu reopen dulu. §2 di bawah karena itu jadi PANDUAN MANUAL (belum ter-seed) untuk siapa yang mau lanjut close Agustus sendiri.

## 1. Demonstrasi Langsung Dampak Duplikasi Periode (WAJIB dijalankan dulu)

Lihat [temuan #1](../../TemuanTestCase/Accounting/CoretaxCompany/01-seeder-dan-master-data.id.md).

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| List semua periode kode `FY2026-01` | `accounting-periods/list {filters:{code:"FY2026-01"}}` | Ekspektasi **2 baris** untuk "January 2026" branch Pusat — satu `is_closed:true`, satu `is_closed:false`. Kalau cuma 1 baris muncul, berarti duplikasi sudah dibersihkan (koreksi temuan) |
| Close periode yang MASIH `is_closed:false` (baris kedua) | `PUT accounting-periods/close {id:<periode Jan yang belum closed>}` | 200 (harusnya berhasil, karena secara individual baris ini valid & belum closed) — **tapi** sekarang ADA 2 baris "Januari 2026" branch Pusat yang SAMA-SAMA `is_closed:true`, dari 2 `id` berbeda. Verifikasi apakah UI/report manapun bingung menampilkan 2 "Januari 2026 (Closed)" |

## 2. Close Periode September 2026 (giliran berikutnya setelah Juli yang sudah di-seed closed)

Juli 2026 sudah closed+locked lewat seeder (§0 di atas). Agustus 2026 sengaja dibiarkan terbuka. Bagian ini menguji guard "harus berurutan" pakai September — bulan SETELAH Agustus yang masih terbuka.

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Negatif — close periode dengan periode sebelumnya masih terbuka** | `PUT accounting-periods/close {id:<September 2026>}`, TANPA close Agustus 2026 dulu | Cek behavior aktual: apakah sistem WAJIB close berurutan (Agustus dulu baru September), atau boleh lompat. Kalau boleh lompat, catat sebagai temuan (tidak ada guard next-period) |
| **Positif** — Close Agustus 2026 | `PUT accounting-periods/close {id:<Agustus 2026>}` | 200, `is_closed:true` — dari titik ini transaksi baru di Agustus (termasuk reverse jurnal T1-T14) mulai kena guard periode closed |
| **Negatif — jurnal baru di periode closed** | Coba `accounting/journals/create` dengan `date:"2026-08-28"` (masuk range Agustus yang sudah closed) | Ditolak — periode closed |
| **Negatif — reverse jurnal CRTX-T1..T14 (file 01) setelah periode closed** | `accounting/journals/reverse {id:<salah satu CRTX-T#>}` | Cek behavior: reverse jurnal LAMA (dibuat sebelum closed) yang sekarang periodenya sudah closed — ditolak atau diizinkan? (immutability period vs reverse sebagai transaksi baru di tanggal reverse, bukan tanggal asli) |
| Netralisasi | Kalau mau lanjut testing manual lain di Agustus setelah eksperimen ini, `reopen` dulu (§3) — jangan biarkan Agustus closed permanen kalau masih mau eksplorasi | — |

## 3. Lock & Reopen

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Reopen Juli 2026** (yang sudah di-seed closed+locked) | `PUT accounting-periods/reopen {id:<salah satu baris Juli 2026>, reason:"Verifikasi reopen"}` (endpoint sebenarnya cek dulu — mungkin nama beda) | 200 — `is_closed` DAN `is_locked` sama-sama balik `false` sekaligus (lihat komentar kode `AccountingPeriod::reopen()`: selalu clear kedua flag bareng, walau cuma salah satu yang di-set). **Ingat ada 2 baris duplikat Juli** — reopen salah satu TIDAK otomatis reopen baris satunya, jalankan manual untuk kedua `id` kalau mau benar-benar konsisten |
| Lock periode Agustus (setelah closed di §2) | `PUT accounting-periods/lock {id:<Agustus 2026>}` | 200, `is_locked:true` |
| Reopen periode Agustus | `PUT accounting-periods/reopen {id:<Agustus 2026>}` | Cek apakah `is_locked` dan `is_closed` beda gate (locked = extra-protected walau sudah reopened dari closed) |

## 4. Close Fiscal Year — Negatif Dulu (banyak periode lain masih terbuka)

FY2026 punya (berkat duplikasi) sampai **24 baris periode** (12 asli × 2 duplikat) — dari situ baru 2 yang closed+locked oleh seeder (kedua baris Juli 2026), sisanya masih terbuka.

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Negatif** — Close FY2026 padahal masih banyak periode terbuka | `POST fiscal-years/close {id:<FY2026>}` | Ditolak — guard "semua periode anak harus closed dulu". Catat pesan error persis, dan apakah pesan itu menyebut jumlah periode yang masih terbuka (kalau iya, angkanya akan janggal karena duplikasi — 22 bukan 11, potensi UX confusing) |
| Netralisasi | Jangan benar-benar close FY2026 di file ini — biarkan untuk baseline file 04/05 (laporan keuangan & anggaran butuh FY masih aktif) |

## Referensi Silang

- [`TemuanTestCase/Accounting/CoretaxCompany/01-seeder-dan-master-data.id.md`](../../TemuanTestCase/Accounting/CoretaxCompany/01-seeder-dan-master-data.id.md) — akar masalah duplikasi periode
- [`01-jurnal-manual-dan-verifikasi-saldo-awal.id.md`](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md) — transaksi yang guard-nya diuji di sini
