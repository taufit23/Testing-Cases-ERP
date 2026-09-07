---
title: (CORETAX) — 01. Jurnal Manual & Verifikasi Saldo Awal
category: accounting-coretax
description: 14 transaksi jurnal manual variatif (tunai, kredit, retur, prive, dimensi Business Unit) di atas master data CORETAX yang sudah ada dari seeder, plus verifikasi gap saldo awal yang belum ter-sinkron ke General Ledger.
visibility: internal
---

# 01. Jurnal Manual & Verifikasi Saldo Awal

> Prasyarat: [`00`](./00-master-data-tersedia-dari-seeder.id.md) sudah dibaca — terutama soal duplikasi `accounting_periods`. **Semua transaksi di file ini pakai periode "August 2026" (`FY2026-08`)** — kedua baris duplikat untuk bulan ini SAMA-SAMA `is_closed:false`, jadi risiko salah pilih ID lebih rendah dibanding Jan-Jun (yang kontradiktif). Tetap jalankan `accounting-periods/list` dulu, catat SATU `id` yang dipakai, dan pakai `id` yang sama itu konsisten di seluruh suite ini.
>
> **Sudah di-seed otomatis**: seluruh 14 transaksi di file ini (T1-T14, plus reverse T2) SUDAH ADA di database begitu `php artisan migrate:fresh --seed` selesai — lihat `database/seeders/CoretaxAccountingTransactionsSeeder.php`. File ini tetap berfungsi sebagai dokumentasi/referensi angka (dan panduan kalau mau reproduksi manual via API untuk verifikasi seeder-nya benar), bukan langkah yang perlu dieksekusi ulang dari nol.

## 0. Verifikasi Gap Saldo Awal (baca dulu sebelum lanjut)

Lihat [temuan #3](../../TemuanTestCase/Accounting/CoretaxCompany/01-seeder-dan-master-data.id.md) — saldo di tabel `chart_of_accounts_balances` (lihat file 00 §2) TIDAK otomatis masuk `general_ledgers`.

| Skenario | Detail | Hasil |
| --- | --- | --- |
| **Verifikasi gap** | `accounting/general-ledger/trial-balance` untuk branch Pusat, di periode SEBELUM Agustus 2026 (mis. `as_of:"2026-07-31"`) | Ekspektasi: **kosong atau 0** untuk semua akun (transaksi seeder T1-T14 semua bertanggal Agustus), MESKIPUN `chart-of-accounts/show` per akun (mis. `1101`) menampilkan `opening_balance: 500000000` dari `chart_of_accounts_balances`. Kalau ternyata Trial Balance per Juli SUDAH menunjukkan angka besar, berarti asumsi "seeder bypass GL" di temuan #3 SALAH — laporkan sebagai koreksi temuan |

## 1. Transaksi Jurnal Manual (T1-T14)

Semua baris pakai akun dari [file 00 §2](./00-master-data-tersedia-dari-seeder.id.md#2-chart-of-accounts-35-baris--13-groupsubgroup--22-akun-leaf). Tanggal `2026-08-10` s/d `2026-08-27` (dalam periode Agustus 2026). Kolom "Cek" = tiap baris SUDAH diverifikasi manual balanced (total debit = total credit) sebelum dimasukkan ke seeder.

| # | Skenario | Payload / baris jurnal | Cek |
| - | --- | --- | --- |
| **T1** | Setoran modal tambahan pemilik ke BCA Operasional | `Dr 1101 50.000.000 / Cr 3101 50.000.000` | 50.000.000 = 50.000.000 ✓ |
| **T2** | Beli ATK tunai dari Kas Kecil *(akan di-reverse di §3)* | `Dr 5502 800.000 / Cr 1102 800.000` | 800.000 = 800.000 ✓ |
| **T3** | Penjualan tunai barang dagang + PPN Keluaran (akun sementara `2190`) | `Dr 1101 11.100.000 / Cr 4001 10.000.000 / Cr 2190 1.100.000` | 11.100.000 = 11.100.000 ✓ |
| **T4** | Bayar gaji karyawan + potong PPh 21 | `Dr 5501 20.000.000 / Cr 1101 18.500.000 / Cr 2190 1.500.000` | 20.000.000 = 20.000.000 ✓ |
| **T5** | Pelunasan piutang usaha dari PT Cahaya Abadi Sejahtera, dimensi BU `BU-RTL` | `Dr 1101 30.000.000 (BU-RTL) / Cr 1121 30.000.000 (BU-RTL)` | 30.000.000 = 30.000.000 ✓ |
| **T6** | Penjualan KREDIT ke CV Mitra Sentosa + PPN | `Dr 1121 16.650.000 / Cr 4001 15.000.000 / Cr 2190 1.650.000` | 16.650.000 = 16.650.000 ✓ |
| **T7** | Retur sebagian penjualan T6 dari CV Mitra Sentosa (1/5 dari nilai barang + PPN proporsional) — jurnal manual net-off langsung ke `4001` (BEDA dari suite `sales-coretax` yang punya akun `4002` sendiri — di sini sengaja disederhanakan sebagai demonstrasi pola "jurnal manual polos tanpa modul Sales Return") | `Dr 4001 3.000.000 / Dr 2190 330.000 / Cr 1121 3.330.000` | 3.330.000 = 3.330.000 ✓ |
| **T8** | Prive — pengambilan pribadi pemilik dari kas | `Dr 3101 5.000.000 / Cr 1101 5.000.000` | 5.000.000 = 5.000.000 ✓ |
| **T9** | Pembelian tunai barang dagang tambahan | `Dr 5001 15.000.000 / Cr 1101 15.000.000` | 15.000.000 = 15.000.000 ✓ |
| **T10a** | Pembelian KREDIT dari supplier (utang usaha bertambah) | `Dr 5001 12.000.000 / Cr 2102 12.000.000` | 12.000.000 = 12.000.000 ✓ |
| **T10b** | Bayar sebagian utang usaha T10a | `Dr 2102 8.000.000 / Cr 1101 8.000.000` | 8.000.000 = 8.000.000 ✓ |
| **T11** | Bayar uang muka ke supplier | `Dr 1422 10.000.000 / Cr 1101 10.000.000` | 10.000.000 = 10.000.000 ✓ |
| **T12** | Pendapatan lain-lain — sewa sebagian gudang | `Dr 1101 3.000.000 / Cr 4501 3.000.000` | 3.000.000 = 3.000.000 ✓ |
| **T13** | Selisih kas kecil saat opname (kekurangan fisik, akun `5502` dipakai lagi karena tidak ada akun "Selisih Kas" khusus — simplifikasi disengaja, bukan gap) | `Dr 5502 150.000 / Cr 1102 150.000` | 150.000 = 150.000 ✓ |
| **T14** | Beban operasional Dept IT (lisensi software), dimensi BU `BU-IT` | `Dr 5502 2.500.000 (BU-IT) / Cr 1101 2.500.000 (BU-IT)` | 2.500.000 = 2.500.000 ✓ |

Status seeder untuk T1-T14: **semua langsung `JRN_POSTED`** (dibuat lewat `JournalHeader::create()` + `createLines()` + `JournalPostingService::createGlEntries()`, mereplikasi persis alur `Journal::create()` → `Journal::post()` di controller — bukan insert polos ke tabel). `requires_journal_approval` untuk branch Pusat bernilai `false` (tidak di-set eksplisit di `PurchaseConfigSeeder`, default kolom), jadi tidak ada approval workflow yang nyangkut.

## 2. Negatif (bukan bagian dari seeder — dites manual via API)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Jurnal tidak balance** | `lines:[{account_id:<5502>, debit:500000},{account_id:<1102>, credit:400000}]` (selisih 100.000) | Cek behavior aktual: `validateBalanced()` return false → status `default_not_balance_journal_status_id` (`JRN_DRAFT`), BUKAN ditolak 422. Jurnal tetap ter-create tapi mengendap di draft |
| **Tanggal di luar semua periode ter-seed** | `date:"2028-01-15"` (tidak ada fiscal year 2028) | Ditolak — `dateHasOpenAccountingPeriod()` return false, validator error `no_accounting_period_covers_this_fiscal_date...` |

## 3. Reverse (T2, sudah termasuk di seeder)

| Skenario | Detail | Hasil |
| --- | --- | --- |
| Reverse T2 | Seeder juga membuat jurnal `REV-<kode T2>` — replikasi persis `Journal::reverse()`: baris dibalik (debit↔credit), `is_reversed:true` di T2 asli, GL tambahan additive (BUKAN hapus GL asli — lihat [`project_journal_reverse_nets_wrong_bug`], sudah diperbaiki per 2026-08-01) | Saldo `5502` & `1102` dari T2 netral (0), tapi T2 TETAP TERLIHAT di `general-ledger/detail-ledger` sebagai 2 baris (asli + pembalik) |

## Ringkasan Saldo Setelah File 01 (T1-T14 posted, T2 di-reverse) — dari seeder

| Akun | Delta (arah alami akun) |
| --- | ---: |
| `1101` Kas dan Setara Kas | +50.000.000(T1) +11.100.000(T3) −18.500.000(T4) +30.000.000(T5) −5.000.000(T8) −15.000.000(T9) −8.000.000(T10b) −10.000.000(T11) +3.000.000(T12) −2.500.000(T14) = **+35.100.000** |
| `1102` Kas Kecil | T2 net 0, −150.000(T13) = **−150.000** |
| `1121` Piutang Usaha | −30.000.000(T5) +16.650.000(T6) −3.330.000(T7) = **−16.680.000** |
| `1422` Uang Muka | +10.000.000(T11) |
| `2102` Utang Usaha | +12.000.000(T10a) −8.000.000(T10b) = **+4.000.000** |
| `2190` Utang Pajak | +1.100.000(T3) +1.500.000(T4) +1.650.000(T6) −330.000(T7) = **+3.920.000** |
| `3101` Modal Disetor | +50.000.000(T1) −5.000.000(T8) = **+45.000.000** |
| `4001` Penjualan | +10.000.000(T3) +15.000.000(T6) −3.000.000(T7) = **+22.000.000** |
| `4501` Pendapatan Lain-lain | +3.000.000(T12) |
| `5001` Pembelian | +15.000.000(T9) +12.000.000(T10a) = **+27.000.000** |
| `5501` Beban Gaji | +20.000.000(T4) |
| `5502` Beban Operasional Lainnya | T2 net 0, +150.000(T13) +2.500.000(T14) = **+2.650.000** |

**Catatan**: angka di atas adalah delta MURNI dari transaksi seeder ini terhadap GL (`general_ledgers`) — TIDAK termasuk saldo `chart_of_accounts_balances` dari `ChartOfAccountsSeeder` (lihat §0, belum tentu masuk GL). **Verifikasi dua arah sudah dilakukan manual**: jumlah seluruh sisi Debit T1-T14 = jumlah seluruh sisi Credit T1-T14 = **187.530.000** — cocok persis, aman dikodekan ke seeder.

## Referensi Silang

- [`00-master-data-tersedia-dari-seeder.id.md`](./00-master-data-tersedia-dari-seeder.id.md) — kode akun, periode, business unit yang dipakai di sini
- [`TemuanTestCase/Accounting/CoretaxCompany/01-seeder-dan-master-data.id.md`](../../TemuanTestCase/Accounting/CoretaxCompany/01-seeder-dan-master-data.id.md) — detail gap saldo awal & duplikasi periode
- [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) — verifikasi Trial Balance pakai baseline di atas
- `database/seeders/CoretaxAccountingTransactionsSeeder.php` — implementasi seeder dari transaksi di file ini
