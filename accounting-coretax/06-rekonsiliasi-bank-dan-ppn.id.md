---
title: (CORETAX) — 06. Rekonsiliasi Bank & PPN
category: accounting-coretax
description: Bank Reconciliation untuk BCA Operasional dan rekap PPN Keluaran/Masukan, menutup suite accounting-coretax.
visibility: internal
---

# 06. Rekonsiliasi Bank & PPN

> Prasyarat: [`01`](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md) (10 dari 14 transaksi menyentuh akun `1101` yang jadi basis rekening BCA Operasional & Mandiri sekaligus — lihat catatan §1 di bawah soal ini bukan per-rekening).
>
> **Sudah di-seed otomatis**: `database/seeders/CoretaxBankReconciliationSeeder.php` sudah membuat 1 Bank Reconciliation untuk BCA Operasional, Agustus 2026, status `completed`, **difference = 0** (kasus bersih, TANPA selisih) — lihat §2 kenapa sengaja begitu (bukan versi "ada selisih 50.000" yang didokumentasikan sebelumnya di file ini, itu ternyata TIDAK cocok dengan struktur endpoint asli, sudah dikoreksi).

## 1. Catatan Penting: `1101` Dipakai BERSAMA oleh 2 Bank Account

File 00 §6 menunjukkan **BCA Operasional** dan **Mandiri Rekening Giro** SAMA-SAMA memakai `chart_of_account_id = 1101` (Kas dan Setara Kas). Transaksi jurnal manual di file 01 (T1, T3, T4, T5) memposting ke `1101` tanpa menyebut bank account SPESIFIK yang mana. Akibatnya: **rekonsiliasi per-bank-account tidak bisa membedakan mana transaksi milik BCA vs Mandiri** — endpoint `finance/bank-reconciliations/*` kemungkinan besar menarik SEMUA mutasi `1101` untuk direkonsiliasi, terlepas rekening mana yang dipilih. Verifikasi ini sebagai bagian dari testing, bukan diasumsikan:

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Verifikasi** — cek dasar pencocokan | `finance/bank-reconciliations/create` untuk BCA Operasional, periode Agustus 2026 | Amati apakah daftar mutasi yang ditawarkan untuk dicocokkan mencakup SEMUA baris `1101` (termasuk yang "harusnya" milik Mandiri) atau ada mekanisme lain (`bank_account_id` di journal line?) yang memisahkan. Kalau ternyata tercampur, itu keterbatasan struktural COA seeder (2 bank pakai 1 akun kas), bukan bug modul rekonsiliasi — laporkan sebagai catatan, bukan bug |

## 2. Bank Reconciliation — BCA Operasional, Agustus 2026

> **Koreksi struktur payload** (terverifikasi dari `App\Http\Controllers\Finance\BankReconciliations.php`): `create` terima `bank_account_id`, `period_start`, `period_end` (BUKAN `period_date` tunggal), `opening_balance`, `closing_balance`, `statement_balance`, `notes` — SEMUA dalam satu payload flat. **TIDAK ADA endpoint/mekanisme "item penyesuai"/baris adjustment sama sekali** — model `BankReconciliationLine` ADA di codebase tapi controller-nya TIDAK PERNAH menyentuhnya. `difference` dihitung otomatis (`statement_balance − closing_balance`) saat create, itu saja.

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| **Positif — sudah di-seed, difference=0** | `finance/bank-reconciliations/create {bank_account_id:<BCA Operasional>, period_start:"2026-08-01", period_end:"2026-08-31", opening_balance:50000000, closing_balance:50000000, statement_balance:50000000}` | 201, `difference:0` — **sengaja dibuat "sudah cocok"** (lihat alasan di bawah), bukan skenario ada selisih |
| **Complete** | `POST finance/bank-reconciliations/complete {slug}` | 200, `status:"completed"` — karena `difference:0`, jalur `response()->json()->warn(...)` TIDAK ke-trigger |
| **Negatif — dites manual, BUKAN via seeder** — buat reconciliation KEDUA dengan `closing_balance` ≠ `statement_balance` (selisih sengaja, mis. 50.000) | `finance/bank-reconciliations/create {..., closing_balance:50000000, statement_balance:49950000}` lalu `complete` | **Dikonfirmasi dari kode** (bukan dugaan lagi): `complete()` manggil `response()->json()->warn([...])`, dan macro `warn` **TIDAK terdaftar di mana pun** di codebase ini (`grep -r "macro('warn'" app/` nihil hasil) — akan throw `BadMethodCallException`, **500 murni**, bukan 422 terstruktur. Ini KONFIRMASI langsung (bukan cuma dugaan berdasar pola suite lain — `accounting-ecommerce`, `accounting-ngo`, `accounting-service-agency` yang sebelumnya cuma menduga dari pola berulang) |
| Kenapa seeder tidak pakai skenario selisih | — | Seeder (`migrate:fresh --seed`) HARUS berhasil sampai akhir — kalau seeder memicu bug 500 di atas, seluruh proses seeding gagal/abort. Skenario "ada selisih" karena itu SENGAJA dites manual terpisah (baris di atas), bukan di-bake ke seeder |

## 3. Rekap PPN Keluaran/Masukan

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Rekap PPN Agustus 2026 | Endpoint laporan PPN (cek nama pasti — kemungkinan `reports/tax-summary` atau sejenis, lihat `FEAccounting/app/pages/reports/tax-summary.vue`) | PPN Keluaran (T3+T6−T7, net) = 1.100.000+1.650.000−330.000 = **2.420.000** — semua tercatat manual di akun `2190` (BUKAN dari akun PPN Keluaran terpisah karena belum ada, lihat file 00 §16). PPh 21 (T4) = 1.500.000 numpuk di akun yang sama, JANGAN ikut terhitung sebagai PPN kalau laporan cuma agregat polos per-akun |
| **Verifikasi laporan tidak bisa deteksi otomatis** | Karena tidak ada akun `is_tax:true` (temuan #2), cek apakah laporan PPN ini membaca dari `journal_taxs` (yang butuh `is_tax` di COA untuk auto-create) atau murni agregat manual dari akun tertentu | Kemungkinan besar laporan PPN akan **kosong** untuk transaksi T3/T4/T6/T7 karena tidak pernah tercatat lewat mekanisme `JournalTaxs` (itu cuma jalan kalau baris punya `account_id` yang `is_tax=true` — lihat pola di `GeneralJournalTypees` controller). Ini KONSEKUENSI LANGSUNG dari temuan #2, dokumentasikan sebagai bukti nyata dampaknya, bukan bug laporan PPN itu sendiri |

## Ringkasan Penutup Suite `accounting-coretax`

Bank Reconciliation file 06 TIDAK menambah entri GL apa pun (header-only, difference=0, tidak ada jurnal biaya admin) — angka di bawah murni dari file 01 (jurnal) + file 05 (aset tetap), tidak berubah dari situ.

| Akun | Saldo akhir (delta dari file 01+05, DI LUAR saldo seeder yang belum tentu masuk GL) |
| --- | ---: |
| `1101` Kas dan Setara Kas | **+35.100.000** |
| `1102` Kas Kecil | **−150.000** |
| `1121` Piutang Usaha | **−16.680.000** |
| `1422` Uang Muka | **+10.000.000** |
| `1600`/`1601`/`5503` Aset Tetap & Penyusutan (dari file 05) | +250.000.000 aset baru, −3.750.000 akumulasi penyusutan, +3.750.000 beban penyusutan |
| `2102` Utang Usaha | **+4.000.000** |
| `2190` Utang Pajak | **+3.920.000** |
| `3101` Modal Disetor | **+45.000.000** |
| `4001` Penjualan | **+22.000.000** |
| `4501` Pendapatan Lain-lain | **+3.000.000** |
| `5001` Pembelian | **+27.000.000** |
| `5501` Beban Gaji | **+20.000.000** |
| `5502` Beban Operasional Lainnya | **+2.650.000** |

## Referensi Silang

- [`00-master-data-tersedia-dari-seeder.id.md`](./00-master-data-tersedia-dari-seeder.id.md) — daftar bank account & gap akun pajak
- [`TemuanTestCase/Accounting/CoretaxCompany/`](../../TemuanTestCase/Accounting/CoretaxCompany/) — semua temuan struktural yang mendasari catatan di file ini
