---
title: (Klinik Umum Besar) — 03. Tutup Periode Bulanan & Tahun Fiskal
category: accounting-klinik-umum
description: Close/Lock/Reopen Accounting Period Januari 2026 (bulanan), guard next-period untuk transaksi susulan file 05-06, dan guard Close Fiscal Year yang ditolak karena 11 periode lain masih terbuka.
visibility: internal
---

# 03. Tutup Periode Bulanan & Tahun Fiskal

> Prasyarat: file [`02-general-ledger-dan-trial-balance-per-cabang.id.md`](./02-general-ledger-dan-trial-balance-per-cabang.id.md) sudah selesai — Trial Balance Januari balance di **1.931.980.000**.

## 1. Close Accounting Period — Januari 2026 (**Accounting Period**)

| Skenario                                            | Payload                                                                                                         | Hasil                                                                                                                                                                                                                |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif — close sebelum semua jurnal posted         | Pastikan dulu tidak ada jurnal Januari berstatus `draft`, baru lanjut                                           | Kalau masih ada draft, `close` HARUS ditolak atau otomatis exclude — cek behavior aktual                                                                                                                             |
| Positif — close Januari                             | `POST client-master/accounting-period/close {id:<Periode Januari>}`                                             | 200, `status:"closed"` — Trial Balance Januari terkunci di 1.931.980.000                                                                                                                                             |
| Negatif — posting jurnal baru ke periode closed     | `POST accounting/journals/create {date:"2026-01-20", ...}` (tanggal MASIH di rentang Januari yang sudah closed) | Ditolak `accounting_period_is_closed` atau sejenis — bukti immutability periode tertutup                                                                                                                             |
| Negatif — reverse jurnal di periode closed          | `POST accounting/journals/reverse {id:<jurnal Januari manapun>}` setelah close                                  | Ditolak dengan alasan sama (periode closed) — kalau ternyata BISA di-reverse setelah closed, itu 🆕 gap immutability serius (laporan keuangan yang sudah dikunci bisa berubah retroaktif), laporkan prioritas tinggi |
| Positif — lock (kalau endpoint terpisah dari close) | `POST client-master/accounting-period/lock {id:<Periode Januari>}`                                              | 200 — cek apakah `lock` beda perilaku dari `close` (mis. `lock` lebih permanen, `close` masih bisa `reopen`) — dokumentasikan hasil aktual                                                                           |

## 2. Guard Next-Period — Buka Februari Sebelum Januari Closed

| Skenario                                        | Detail                                                                 | Hasil                                                                                                                                                           |
| ----------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif (test SEBELUM §1 dieksekusi, opsional)  | Posting jurnal ke Februari 2026 SAAT Januari MASIH `open`              | Tidak ada guard yang menghalangi — periode berbeda independen (perilaku wajar, bukan bug)                                                                       |
| Positif — urutan yang benar (dipakai suite ini) | Close Januari (§1) DULU, baru posting transaksi file 05/06 ke Februari | Konsisten dengan strategi file 00 (transaksi lanjutan sengaja ditanggal Februari SETELAH Januari closed, supaya Trial Balance Januari tidak berubah retroaktif) |

## 3. Reopen Periode Januari (Opsional, Demonstrasi Saja — JANGAN Dieksekusi Permanen)

| Skenario         | Detail                                                                                                                                                                                                                 | Hasil                                                                                                                                           |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — reopen | `POST client-master/accounting-period/reopen {id:<Periode Januari>}`                                                                                                                                                   | 200, `status` kembali `"open"` — HANYA untuk demonstrasi fitur, **segera `close` ulang setelah dites** supaya file 04-06 tidak terganggu urutan |
| Netralisasi      | WAJIB `close` ulang Periode Januari sebelum lanjut ke file 04 — cek Trial Balance TIDAK berubah dari 1.931.980.000 setelah reopen+close ulang (kalau berubah, ada efek samping reopen yang tidak diharapkan, laporkan) |

## 4. Close Fiscal Year FY2026 — HARUS DITOLAK (Guard Utama File Ini)

| Skenario                                                          | Payload                                                                                                                                                             | Hasil                                                                                                                                                                                                           | Label temuan                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Negatif — close FY dengan 11 periode masih terbuka**            | `POST client-master/fiscal-year/close {id:<FY2026>}` (Januari closed, Februari-Desember masih `open`, sebagian malah belum ada transaksi sama sekali)               | HARUS ditolak — pesan sejenis "there are still open accounting periods" atau daftar periode yang menghalangi                                                                                                    | ✅ kalau ditolak dengan jelas — kalau ternyata BISA closed padahal 11 periode masih terbuka, itu 🆕 gap validasi serius (closing entry ke Laba Ditahan bisa salah karena transaksi periode belakangan yang belum terjadi ikut "dianggap selesai"), laporkan prioritas tinggi |
| Negatif — close FY yang belum ada Fiscal Year berikutnya (FY2027) | Kalaupun seluruh 12 periode FY2026 closed (skenario hipotetis, TIDAK dieksekusi di suite ini karena hanya Januari-Februari yang diisi), coba close tanpa FY2027 ada | Cek behavior aktual — apakah closing tetap jalan (closing entry ke Laba Ditahan FY2026, FY2027 dibuat manual terpisah) atau ditolak. Belum diverifikasi ke kode, dokumentasikan hasil aktual kalau sempat dites |
| Netralisasi                                                       | Tidak perlu — FY2026 TETAP terbuka sampai akhir suite ini (sengaja, sesuai simplifikasi file 00)                                                                    |

## 5. Ringkasan Status Setelah File Ini

| Item                        | Status                                                                                                                                       |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Periode Januari 2026        | `closed` (setelah §3 reopen demonstrasi, di-close ulang)                                                                                     |
| Periode Februari 2026       | `open` — dipakai file 05 (aset tetap) dan file 06 (rekonsiliasi bank)                                                                        |
| Periode Maret-Desember 2026 | `open`, tidak ada transaksi — sengaja dibiarkan kosong (file 00)                                                                             |
| Fiscal Year FY2026          | TETAP `open` — Close Fiscal Year hanya didemonstrasikan sebagai NEGATIF (ditolak), tidak benar-benar dieksekusi sampai selesai               |
| Laba Ditahan (3102)         | TETAP 0 — belum ada closing entry (closing entry hanya terjadi saat Close Fiscal Year sukses, yang di suite ini sengaja tidak pernah sukses) |

## Referensi Silang

- File [`02-general-ledger-dan-trial-balance-per-cabang.id.md`](./02-general-ledger-dan-trial-balance-per-cabang.id.md) — Trial Balance Januari yang dikunci di file ini
- File [`04-laporan-keuangan-konsolidasi-dan-per-cabang.id.md`](./04-laporan-keuangan-konsolidasi-dan-per-cabang.id.md) — Laporan Keuangan disusun SETELAH periode Januari closed (Laba Berjalan 393.950.000 tetap tampil di Laba Rugi walau closing entry ke 3102 belum terjadi — beda konsep antara "periode closed" [kontrol input] dan "fiscal year closed" [closing entry ke equity])
- Suite lain: pola guard Close Fiscal Year yang sama direplikasi dari [`../accounting-fnb-kafe/03-tutup-periode-bulanan-dan-tahun-fiskal.id.md`](../accounting-fnb-kafe/03-tutup-periode-bulanan-dan-tahun-fiskal.id.md) dan [`../accounting-klinik-gigi/03-tutup-periode-mingguan-dan-tahun-fiskal.id.md`](../accounting-klinik-gigi/03-tutup-periode-mingguan-dan-tahun-fiskal.id.md)
