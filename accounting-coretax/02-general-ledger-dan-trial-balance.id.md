---
title: (CORETAX) — 02. General Ledger & Trial Balance
category: accounting-coretax
description: Verifikasi Detail Ledger, Summary by Account (dimensi Business Unit), dan Trial Balance di atas transaksi file 01.
visibility: internal
---

# 02. General Ledger & Trial Balance

> Prasyarat: [`01`](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md) — T1-T14 posted, T2 posted lalu di-reverse. Semua sudah otomatis ter-seed via `CoretaxAccountingTransactionsSeeder.php`.

## 1. Detail Ledger

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Detail Ledger akun `1101` | `general-ledger/detail-ledger {chart_of_account_id:<1101>, date_from:"2026-08-01", date_to:"2026-08-31"}` | 10 baris (T1, T3, T4, T5, T8, T9, T10b, T11, T12, T14) + running balance berurutan tanggal, saldo akhir period = **+35.100.000** dari nol (asumsi §0 file 01 confirmed GL kosong sebelum ini) |
| Detail Ledger akun `2190` | Filter akun `2190` | 4 baris (T3 credit 1.1jt PPN, T4 credit 1.5jt PPh21, T6 credit 1.65jt PPN, T7 debit 330rb retur PPN) — **verifikasi manual**: apakah tampilan baris membedakan sumber PPN vs PPh21, atau cuma angka polos tanpa keterangan jenis pajak (karena keduanya numpuk di 1 akun, lihat temuan file 00 §16). Saldo akhir = +3.920.000 |
| Detail Ledger akun `1102` (Kas Kecil, kena reverse + T13) | Filter akun `1102` | 3 baris: T2 asli (credit 800rb, `is_reversed` di header journal) + baris pembalik (debit 800rb) + T13 (credit 150rb) — saldo akhir period = **−150.000** |
| Detail Ledger akun `1121` (Piutang) | Filter akun `1121` | 3 baris (T5 credit 30jt, T6 debit 16,65jt, T7 credit 3,33jt) — saldo akhir = **−16.680.000** |

## 2. Summary by Account — Filter Dimensi Business Unit

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Summary akun `1101`, tanpa filter | `general-ledger/summary-by-account {chart_of_account_id:<1101>}` | Total movement = +35.100.000 |
| Summary akun `1101`/`1121`, filter `business_unit_id:<BU-RTL>` | Sama endpoint + filter BU | Cuma T5 yang punya dimensi BU-RTL (30jt) — T1/T3/T4/dst TIDAK punya `business_unit_id` (null) → **verifikasi**: apakah baris tanpa BU ikut ke-exclude dari filter (ekspektasi ya, exclude) atau malah ikut ke-include (bug) |
| Summary akun `5502`, filter `business_unit_id:<BU-IT>` | Sama endpoint + filter BU-IT | Cuma T14 yang punya dimensi BU-IT (2,5jt) — T2/T13 (juga di akun `5502`) TIDAK punya BU, harus ke-exclude dari hasil filter ini |

## 3. Trial Balance

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Trial Balance per 2026-08-31 | `general-ledger/trial-balance {as_of:"2026-08-31"}` | Debit = Kredit, cocokkan dengan [ringkasan file 01](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md#ringkasan-saldo-setelah-file-01-t1-t14-posted-t2-di-reverse--dari-seeder) baris per baris |
| Trial Balance per 2026-07-31 (sebelum transaksi file ini) | Sama endpoint, `as_of:"2026-07-31"` | Ekspektasi kosong/nol semua akun (transaksi file 01 semua di Agustus) — **kecuali** kalau ternyata saldo seeder ADA masuk GL (lihat catatan §0 file 01), baru akan tampil di sini |

## Referensi Silang

- [`01-jurnal-manual-dan-verifikasi-saldo-awal.id.md`](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md) — sumber transaksi & baseline saldo
- [`04-laporan-keuangan.id.md`](./04-laporan-keuangan.id.md) — Neraca/Laba Rugi harus konsisten dengan Trial Balance di file ini
