---
title: (Yayasan Pendidikan) — 03. Tutup Periode Bulanan & Tahun Fiskal
category: accounting-education
description: Close/Lock/Reopen periode akuntansi Maret 2026 (guard jurnal belum posted, guard periode berikutnya), immutability jurnal setelah closed, dan simulasi closeYear() tahun fiskal (guard retained earnings account, guard periode masih terbuka).
visibility: internal
---

# 03. Tutup Periode Bulanan & Tahun Fiskal

> Prasyarat: [`01-jurnal-spp-dan-beasiswa.id.md`](./01-jurnal-spp-dan-beasiswa.id.md) §1.15 selesai (semua 14 jurnal `JRN_POSTED`). Endpoint dikonfirmasi dari `routes/client_master.php` prefix **Accounting Period**: `close` (PUT), `lock` (PUT), `reopen` (PUT), dan **Fiscal Year**: `close-year` (POST) — controller `App\Http\Controllers\ClientMaster\AccountingPeriod` dan `FiscalYear`.

## 3.1 Guard — Close Periode dengan Jurnal Belum Posted

| Skenario    | Detail                                                                                                                                                                                              | Hasil                                                                                                                                                                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif     | Buat 1 jurnal draft baru bertanggal Maret 2026 (`code:"JRN-EDU-015"`, `date:"2026-03-15"`, 2 baris apa saja, JANGAN di-post), lalu `PUT client-master/accounting-period/close {id:<Periode Maret>}` | 422 `accounting_period_has_unposted_journals_post_or_void_them_first` — dikonfirmasi dari `AccountingPeriod::hasUnpostedJournalsInPeriod()`, mengecek `journals` (JournalHeader) dengan `posted_at IS NULL` dan `date` di rentang periode |
| Netralisasi | `DELETE accounting/journals/delete` jurnal test `JRN-EDU-015` (masih draft, aman langsung dihapus — hard-delete)                                                                                    |

## 3.2 Guard — Close Periode Sebelum Periode Berikutnya Ada

| Skenario                                      | Detail                                                                                                                                                                                                                              | Hasil                                                                                                            |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Negatif                                       | Pastikan Periode April 2026 SUDAH ada (di-generate bareng §5 file `00`) tapi coba `close` periode Februari 2026 (yang tidak dipakai transaksi apapun di suite ini) SAAT periode Maret belum closed — tidak relevan untuk urutan ini | Skip — cukup verifikasi via §3.3 (periode Maret) karena Periode April 2026 sudah pasti ada dari generate bulanan |
| Positif — verifikasi guard tidak salah blokir | Periode Maret 2026 boleh di-close karena Periode April 2026 sudah ada dan masih `is_closed:false`                                                                                                                                   | Guard `cannot_close_period_the_next_period_has_not_been_created_yet` TIDAK muncul                                |

## 3.3 Close Periode Maret 2026 (Jalur Sukses)

| Skenario | Payload                                                               | Hasil                                                                                      |
| -------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Positif  | `PUT client-master/accounting-period/close {id:<Periode Maret 2026>}` | 200, `is_closed:true`, `is_locked:false` — `content.accounting_period_closed_successfully` |
| Negatif  | `close` lagi periode yang sama                                        | 422 `accounting_period_already_closed`                                                     |

## 3.4 Guard — Posting Jurnal Baru ke Periode yang Sudah Closed

| Skenario    | Detail                                                                                                                       | Hasil                                                                                                                                                                                                                                         |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif     | Coba `POST accounting/journals/create {date:"2026-03-20", ...}` (tanggal MASIH di dalam periode Maret yang baru saja closed) | Cek behavior aktual `JournalPostingService`/validasi create — idealnya ditolak karena periode sudah closed; kalau create MASIH berhasil (hanya `post` yang diblokir, bukan `create`) → catat sebagai gap, laporkan behavior aktual apa adanya |
| Netralisasi | Kalau jurnal test terlanjur dibuat, `delete` selama masih draft                                                              |

## 3.5 Lock Periode Maret 2026

| Skenario | Payload                                                                                               | Hasil                                                                   |
| -------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Negatif  | `PUT client-master/accounting-period/lock {id:<Periode Februari 2026>}` (periode yang BELUM di-close) | 422 `accounting_period_must_be_closed_before_it_can_be_locked`          |
| Positif  | `PUT client-master/accounting-period/lock {id:<Periode Maret 2026>}` (sudah closed di §3.3)           | 200, `is_locked:true` — `content.accounting_period_locked_successfully` |
| Negatif  | `lock` lagi periode yang sama                                                                         | 422 `accounting_period_already_locked`                                  |

## 3.6 Immutability Setelah Locked — Reverse Jurnal Historis

| Skenario | Detail                                                                                                         | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif  | Coba `POST accounting/journals/reverse {id:<salah satu jurnal JRN-EDU-001..014>}` setelah periode Maret locked | Cek behavior aktual — apakah `JournalPostingService`/`Journal::reverse()` menolak reverse ke periode locked, atau tetap lolos (reverse membuat jurnal BARU bertanggal hari ini, bukan bertanggal Maret, jadi kemungkinan besar TETAP LOLOS karena jurnal reversal-nya sendiri jatuh di periode berjalan, bukan periode locked) — laporkan behavior aktual, JANGAN asumsikan ditolak hanya karena "terasa seharusnya" |

## 3.7 Reopen Periode Maret 2026

| Skenario | Payload                                                                                                            | Hasil                                                                                                                                                                          |
| -------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Negatif  | `PUT client-master/accounting-period/reopen {id:<Periode Januari 2026>}` (periode yang tidak pernah di-close/lock) | 422 `accounting_period_is_not_closed_or_locked`                                                                                                                                |
| Positif  | `PUT client-master/accounting-period/reopen {id:<Periode Maret 2026>, reason:"Koreksi jurnal beasiswa"}`           | 200, `is_closed:false, is_locked:false` sekaligus (reopen SELALU clear kedua flag bersamaan, walau yang di-pass cuma `id`) — `content.accounting_period_reopened_successfully` |

## 3.8 Simulasi Close Tahun Fiskal — Guard Retained Earnings Account

**Prasyarat**: SEMUA 12 periode Accounting Period 2026 harus `is_closed:true` sebelum `close-year` bisa jalan — di suite ini, HANYA Maret yang benar-benar ditransaksikan; untuk menguji guard ini SECARA ISOLATED tanpa merusak baseline, kerjakan simulasi di branch/tahun fiskal TERPISAH (jangan close FY2026 asli sampai semua 12 periode benar-benar ditutup, karena file `04`-`06` masih butuh periode Maret dalam keadaan reopened).

| Skenario                                                   | Detail                                                                                                                                                                                                                                                                                                                                                                          | Hasil                                                                                                             |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Negatif — periode belum semua closed                       | `POST client-master/fiscal-year/close-year {id:<FY2026>}` SAAT masih ada periode `is_closed:false` (mis. Januari, Februari, April-Desember)                                                                                                                                                                                                                                     | 422 `all_accounting_periods_in_this_fiscal_year_must_be_closed_first`                                             |
| Negatif — retained earnings account tidak ada/lebih dari 1 | (Simulasi terpisah) Hapus flag `is_retained_earnings_account` dari EKT-02 dulu, lalu coba `close-year`                                                                                                                                                                                                                                                                          | 422 `flag_exactly_one_account_as_the_retained_earnings_account_in_chart_of_accounts_before_closing_a_fiscal_year` |
| Negatif — 2 akun ber-flag retained earnings                | (Simulasi terpisah) Flag `is_retained_earnings_account:true` ke akun kedua selain EKT-02                                                                                                                                                                                                                                                                                        | 422 `more_than_one_account_is_flagged_as_retained_earnings_account_only_one_is_allowed`                           |
| Netralisasi                                                | Pastikan HANYA EKT-02 yang ber-flag `is_retained_earnings_account:true` sebelum lanjut ke file `04`; JANGAN benar-benar jalankan `close-year` sukses di branch aktif — itu akan membuat closing entry yang mengunci saldo PDT-01/PDT-02/PDT-03/BBN-01..04 ke EKT-02, merusak asumsi baseline file `04`-`06` yang masih butuh saldo pendapatan/beban berjalan (belum di-closing) |

## 3.9 Ringkasan Perilaku Guard yang Terkonfirmasi

| Guard                                                                       | Pesan                                                                                                                                 | Lokasi kode                                       |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Close periode dengan jurnal draft di dalamnya                               | `accounting_period_has_unposted_journals_post_or_void_them_first`                                                                     | `AccountingPeriod::hasUnpostedJournalsInPeriod()` |
| Close periode tanpa periode berikutnya (bukan periode terakhir fiscal year) | `cannot_close_period_the_next_period_has_not_been_created_yet`                                                                        | `AccountingPeriod::close()`                       |
| Close periode yang sudah closed                                             | `accounting_period_already_closed`                                                                                                    | `AccountingPeriod::close()`                       |
| Lock periode yang belum closed                                              | `accounting_period_must_be_closed_before_it_can_be_locked`                                                                            | `AccountingPeriod::lock()`                        |
| Reopen periode yang belum closed/locked                                     | `accounting_period_is_not_closed_or_locked`                                                                                           | `AccountingPeriod::reopen()`                      |
| Close tahun fiskal dengan periode masih terbuka                             | `all_accounting_periods_in_this_fiscal_year_must_be_closed_first`                                                                     | `FiscalYear::closeYear()`                         |
| Close tahun fiskal tanpa/lebih dari 1 retained earnings account             | `flag_exactly_one_account_as_the_retained_earnings_account_...` / `more_than_one_account_is_flagged_as_retained_earnings_account_...` | `FiscalYear::closeYear()`                         |

## Netralisasi Akhir File

- Pastikan Periode Maret 2026 kembali `is_closed:false, is_locked:false` (via §3.7) sebelum lanjut ke file `04`-`06` — file-file tersebut masih memakai jurnal Maret sebagai baseline dan mungkin perlu menambah jurnal susulan.
- Pastikan HANYA EKT-02 yang ber-flag `is_retained_earnings_account:true` dan HANYA EKT-01 yang ber-flag `is_opening_balance_equity_account:true`.
- JANGAN benar-benar men-`close-year` FY2026 di branch aktif suite ini.

## Referensi Silang

- [`01-jurnal-spp-dan-beasiswa.id.md`](./01-jurnal-spp-dan-beasiswa.id.md) — baseline jurnal yang dipakai menguji guard unposted journal
- [`../accounting-fnb-kafe/03-tutup-periode-bulanan-dan-tahun-fiskal.id.md`](../accounting-fnb-kafe/03-tutup-periode-bulanan-dan-tahun-fiskal.id.md) — pola guard yang sama (bulanan), dipakai dasar penulisan file ini
