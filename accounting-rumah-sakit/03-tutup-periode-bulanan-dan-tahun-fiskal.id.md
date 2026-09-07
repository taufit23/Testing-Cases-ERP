---
title: (Rumah Sakit) — 03. Tutup Periode Bulanan & Tahun Fiskal
category: accounting-rumah-sakit
description: Close/Lock/Reopen Accounting Period BULANAN untuk Periode 1 (Januari), plus guard Close Fiscal Year saat masih ada 11 periode lain yang belum ditutup, dan skenario opsional close tahun penuh dengan closing entry presisi.
visibility: internal
---

# 03. Tutup Periode Bulanan & Tahun Fiskal

> Prasyarat: file [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) sudah selesai — Trial Balance sudah balance 66.333.170.000.

## 1. Close Accounting Period — Periode 1 (Januari 2026)

| Skenario                                                       | Detail                                                                                                      | Hasil                                                                                                             |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Positif — close normal                                         | `PUT client-master/accounting-period/close {id:<Periode 1>}`                                                | 200, `is_closed:true`. Semua jurnal T1-T17 (tanggal 2026-01-05 s/d 2026-01-28) sudah terposting sebelum close ini |
| **Negatif — posting jurnal baru ke periode yang sudah closed** | Coba `POST accounting/journals/create {date:"2026-01-15", ...}` (tanggal masuk Periode 1 yang sudah closed) | Ditolak dengan pesan jelas (mis. "accounting_period_is_closed") — BUKAN 500, BUKAN silent-success                 |
| Positif — reopen                                               | `PUT client-master/accounting-period/reopen {id:<Periode 1>}` (kalau endpoint ini ada)                      | 200, `is_closed:false` — dipakai HANYA untuk uji kemampuan reopen                                                 |
| Netralisasi                                                    | Close ulang Periode 1 setelah selesai uji reopen                                                            | `is_closed:true` lagi                                                                                             |

## 2. Guard "Tutup Bulan Berurutan" & Lock

| Skenario                                          | Detail                                                                                                                                | Hasil                                                                                                                                                                                                                                        |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Negatif — lompat urutan close**                 | Coba close Periode 3 (Maret) SEBELUM Periode 2 (Februari) di-close, padahal Periode 2 juga sudah punya transaksi (file 06 aset tetap) | Kalau ada guard "next period only": ditolak, harus close berurutan. Kalau TIDAK ada guard: berhasil closed di luar urutan — catat sebagai 🆕 gap kontrol kalau ternyata BISA, tapi tulis "belum diverifikasi ke kode" kalau tidak sempat cek |
| Positif — Lock (kalau endpoint terpisah tersedia) | `PUT client-master/accounting-period/lock {id:<Periode 1>}`                                                                           | 200, `is_locked:true` — verifikasi behavior aktual: coba reopen periode yang sudah `is_locked:true`                                                                                                                                          |
| Negatif                                           | Reopen periode yang sudah `is_locked:true`                                                                                            | Ditolak — kalau ternyata BISA reopen periode locked, itu gap kontrol, catat sebagai temuan                                                                                                                                                   |
| Netralisasi                                       | Pastikan Periode 1 balik ke state `is_closed:true` sebelum lanjut §3                                                                  |

> **Catatan urutan file**: file [`06-aset-tetap-alat-medis-besar.id.md`](./06-aset-tetap-alat-medis-besar.id.md) mencatat transaksi ke **Periode 2 (Februari)** dan **Periode 3 (Maret)**, sedangkan file [`04-laporan-keuangan-per-departemen.id.md`](./04-laporan-keuangan-per-departemen.id.md) dan [`05-anggaran-departemen.id.md`](./05-anggaran-departemen.id.md) HANYA memakai data Periode 1 — kerjakan file 04 dan 05 SEBELUM meng-close Periode 1 secara permanen di sesi ini kalau closing Periode 1 ternyata mengunci akses laporan terhadap periode tersebut (perilaku aktual bervariasi tergantung implementasi, cek dulu sebelum lanjut kalau ragu).

## 3. Close Fiscal Year — Guard "Masih Ada 11 Periode Lain Belum Ditutup"

**Konteks**: Fiscal Year FY2026 berisi 12 periode bulanan. Suite ini SENGAJA hanya mengisi transaksi di Periode 1 (Januari, file 01) dan sebagian Periode 2-3 (Februari-Maret, file 06-07) — Periode 4-12 (April-Desember) sengaja kosong tanpa transaksi apapun, sehingga percobaan Close Fiscal Year seharusnya DITOLAK karena masih banyak periode `is_closed:false`.

| Skenario                                                              | Detail                                                                                                                                                                 | Hasil                                                                                                                                                                                         |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Negatif — close tahun fiskal padahal masih banyak periode terbuka** | `PUT client-master/fiscal-year/close {id:<FY2026>}` (setelah hanya Periode 1 yang closed, atau Periode 1-3 kalau file 06/07 juga sudah close periodenya masing-masing) | Ditolak dengan pesan jelas (mis. "not_all_accounting_periods_are_closed") — PERILAKU YANG DIHARAPKAN. Kalau ternyata BERHASIL close walau periode lain masih terbuka, itu 🆕 bug guard serius |
| Positif — pesan error mencantumkan detail                             | Baca detail pesan error                                                                                                                                                | Idealnya menyebut jumlah periode yang belum closed (mis. "9 periode belum ditutup") — kalau generik tanpa detail, 🔧 improvement UX kecil                                                     |

**Catatan scope**: suite ini TIDAK melanjutkan sampai benar-benar berhasil Close Fiscal Year (butuh mengisi/menutup 9-11 periode tersisa, di luar scope utama suite ini). Kalau mau menguji jalur sukses penuh, ikuti §3.1 di bawah (opsional).

### 3.1 (Opsional, lanjutan) Close seluruh periode kosong lalu Close Fiscal Year sukses

| Skenario           | Detail                                                                                                                                                                                             | Hasil                                                                                                                                                                                                                                                                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — opsional | Close semua periode sisa (April-Desember, dan Februari-Maret kalau belum di-close dari file 06/07) TANPA transaksi tambahan, lalu `PUT client-master/fiscal-year/close {id:<FY2026>}`              | 200 — closing entry terposting: net Laba/Rugi berjalan TOTAL sampai akhir tahun (bukan cuma file 01 — HARUS termasuk transaksi file 06/07 di Periode 2-3 juga, lihat perhitungan gabungan di §3.2) dipindahkan dari akun Pendapatan/Beban ke 3102 Laba Ditahan. Semua akun Pendapatan (41xx) dan Beban (51xx) kembali ke 0 |
| Negatif            | Close fiscal year 2x                                                                                                                                                                               | Ditolak — sudah closed                                                                                                                                                                                                                                                                                                     |
| Netralisasi        | JANGAN eksekusi di branch yang sama dipakai file 04/05 (asumsi keduanya berjalan sebelum tahun ditutup) — kerjakan §3.1 PALING TERAKHIR setelah 04/05/06/07 selesai, atau di branch/clone terpisah |

### 3.2 Perhitungan Laba/Rugi Berjalan Gabungan (kalau §3.1 dieksekusi setelah file 06/07 selesai)

Total Laba/Rugi berjalan akhir tahun = Laba/Rugi file 01 (Periode 1) + efek tambahan Periode 2-3 dari file 06/07 (penyusutan bulanan, beban administrasi bank, dst — akumulasi ANGKA PASTINYA baru diketahui setelah file 06/07 selesai, hitung ulang manual di sana sebelum eksekusi §3.1). **Jangan asumsikan angka Laba/Rugi file 01 (−2.142.985.000) adalah angka final tahun** — itu HANYA posisi per 2026-01-28, bukan posisi akhir FY2026.

## Referensi Silang

- Suite klinik gigi [`../accounting-klinik-gigi/03-tutup-periode-mingguan-dan-tahun-fiskal.id.md`](../accounting-klinik-gigi/03-tutup-periode-mingguan-dan-tahun-fiskal.id.md) — pola simplifikasi "kumpulkan transaksi di periode awal saja" yang direplikasi strateginya di suite ini
- Suite manufaktur [`../accounting-manufaktur/04-tutup-periode-kuartalan-dan-tahun-fiskal.id.md`](../accounting-manufaktur/04-tutup-periode-kuartalan-dan-tahun-fiskal.id.md) — pola guard next-period close
- `App\Models\ClientMaster\FiscalYear::closeYear()` — guard akun `is_retained_earnings_account` (WAJIB tepat 1) sudah dites di file 00 §3, closing entry logic dipakai §3.1
