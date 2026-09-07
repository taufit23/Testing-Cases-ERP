---
title: (Nonprofit / NGO) — 03. Tutup Periode Bulanan & Tahun Fiskal
category: accounting-ngo
description: Close/Lock/Reopen Accounting Period bulanan dan Close Fiscal Year, endpoint nyata client-master/accounting-period & client-master/fiscal-year.
visibility: internal
---

# 03. Tutup Periode Bulanan & Tahun Fiskal

> Prasyarat: [`01`](./01-jurnal-hibah-dan-fund-accounting.id.md) semua jurnal Januari 2026 sudah posted (§1.1-1.6), jurnal §1.7 sudah direverse, tidak ada jurnal `draft`/belum-posted lain bertanggal Januari 2026 — `AccountingPeriod::close()` menolak kalau masih ada jurnal `posted_at IS NULL` dalam rentang tanggal periode. Endpoint: `client-master/accounting-period/{close,lock,reopen}`, **Fiscal Year — `close-year`**.

## 1. Close Periode Januari 2026

| Skenario                          | Payload kunci                                                                                                                                                                                         | Hasil                                                                         |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Negatif — ada jurnal belum posted | Buat 1 jurnal draft baru bertanggal Januari 2026 (mis. `lines:[{BBN-03, debit:1000000},{AST-01, credit:1000000}]`, JANGAN di-post), lalu `POST client-master/accounting-period/close {id:<Jan 2026>}` | Ditolak — pesan mengandung info jurnal belum posted (unposted journals exist) |
| Netralisasi sebelum lanjut        | Post atau delete jurnal draft di atas                                                                                                                                                                 | —                                                                             |
| Positif                           | `POST client-master/accounting-period/close {id:<Jan 2026>}` (semua jurnal Jan sudah posted)                                                                                                          | 200, periode Januari `is_closed:true`                                         |
| Negatif — close 2x                | Ulangi `close` pada periode yang sama                                                                                                                                                                 | Ditolak — periode sudah closed                                                |

## 2. Lock Periode Januari 2026

| Skenario                      | Payload kunci                                                                                                  | Hasil                                                       |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Negatif — lock sebelum closed | `POST client-master/accounting-period/lock {id:<Februari 2026>}` (periode Februari masih open, belum di-close) | Ditolak — `lock()` mensyaratkan `is_closed:true` lebih dulu |
| Positif                       | `POST client-master/accounting-period/lock {id:<Jan 2026>}` (Januari sudah closed di §1)                       | 200, `is_locked:true`                                       |

## 3. Jurnal Susulan Setelah Periode Locked (Negatif — Immutability)

| Skenario | Payload kunci                                                                          | Hasil                                                                                                                                                                                                                                                             |
| -------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif  | Coba buat jurnal baru bertanggal `2026-01-20` (dalam periode yang sudah closed+locked) | Cek behavior aktual — kalau `Journal::create()` tidak melakukan pengecekan periode locked sama sekali, jurnal baru akan lolos dibuat & posted padahal periodenya sudah dikunci; ini finding penting untuk dilaporkan (🔧 gap), bukan diasumsikan otomatis ditolak |

## 4. Reopen Periode Januari 2026

| Skenario | Payload kunci                                                                             | Hasil                                                                                        |
| -------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Positif  | `POST client-master/accounting-period/reopen {id:<Jan 2026>, reason:"Koreksi test case"}` | 200 — `reopen()` melepas `is_closed` DAN `is_locked` sekaligus (satu langkah, bukan 2 tahap) |

## 5. Close Fiscal Year FY2026 (Guard Periode Lain Masih Terbuka)

Setelah §4, Januari kembali open sehingga 11 dari 12 periode FY2026 masih open (Feb-Des belum pernah di-close di suite ini).

| Skenario                             | Payload kunci                                                                                                                                        | Hasil                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif                              | `POST client-master/fiscal-year/close-year {fiscal_year_id:<FY2026>}`                                                                                | Ditolak — `FiscalYear::closeYear()` mensyaratkan SEMUA periode dalam fiscal year sudah `is_closed:true`; 11 periode (Feb-Des) masih open                                                                                                                                                                                           |
| Netralisasi untuk lanjut test        | Close ulang Januari (§1) lalu close Feb-Des satu per satu (asumsi tidak ada jurnal lain di bulan-bulan itu, jadi bisa langsung close tanpa hambatan) | Semua 12 periode `is_closed:true`                                                                                                                                                                                                                                                                                                  |
| Positif                              | `POST client-master/fiscal-year/close-year {fiscal_year_id:<FY2026>}`                                                                                | 200 — dihitung net revenue/expense dari `general_ledgers` sepanjang FY2026: Pendapatan 100.000.000 − Beban 32.000.000 = **68.000.000**, diposting sebagai closing entry `Dr PDT-01/02/03 (total 100jt) / Cr BBN-01/02/03 (total 32jt) / Cr EKT-03 Laba Ditahan 68jt` ke akun ber-flag `is_retained_earnings_account:true` (EKT-03) |
| Positif — verifikasi setelah closing | `POST accounting/general-ledger/trial-balance {as_of_date:"2026-12-31"}`                                                                             | Akun Pendapatan & Beban bersaldo nol (sudah di-nol-kan closing entry), EKT-03 bersaldo kredit **68.000.000**                                                                                                                                                                                                                       |
| Negatif — close 2x                   | Ulangi `close-year` pada FY2026 yang sama                                                                                                            | Ditolak — fiscal year sudah closed                                                                                                                                                                                                                                                                                                 |

## Netralisasi

- Kalau perlu mengembalikan state untuk lanjut testing lain: `reopen` semua periode yang di-close di §5 (kecuali sengaja mau membiarkan FY2026 closed sebagai baseline final).
- Closing entry hasil `close-year` adalah jurnal biasa — bisa direverse lewat `accounting/journals/reverse` kalau perlu dibatalkan total.
