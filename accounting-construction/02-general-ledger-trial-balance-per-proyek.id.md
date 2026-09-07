---
title: (Construction / Project Based) — 02. GL & Trial Balance per Proyek
category: accounting-construction
description: Verifikasi Detail Ledger, Summary by Account, dan Trial Balance PT Bangun Persada setelah T1-T7 (file 01) diposting — termasuk filter dimensi per proyek (business_unit_id).
visibility: internal
---

# 02. GL & Trial Balance per Proyek

> Prasyarat: seluruh jurnal T1-T7 di file `01-jurnal-progres-dan-retensi.id.md` sudah **posted** (T4 sudah direverse sebagai demonstrasi, net efek T4+reversal = 0). Endpoint dasar: **General Ledger — `{list|show|by-account|by-period|detail-ledger|summary-by-account|trial-balance}`** — semua `POST`.
>
> **Kenapa file ini penting:** file 01 membuktikan jurnal T1-T7 BISA dibuat & di-post. File ini membuktikan angka-angka itu benar-benar TERHITUNG dengan benar setelah digabung per akun maupun per proyek — kalau ada baris yang salah arah/salah nominal di file 01, di sinilah biasanya baru ketahuan (Trial Balance jadi timpang, atau breakdown per proyek di §2 tidak masuk akal).

## 1. Saldo Berjalan (Hitung Manual) Setelah T1-T7

Saldo awal (file 00 §6) + efek T1-T7 (T4+reversal net 0):

| Akun                               |  Saldo Awal | Mutasi Bersih | Saldo Akhir |
| ---------------------------------- | ----------: | ------------: | ----------: |
| AST-01 Bank Mandiri Proyek         | 500.000.000 |  +350.200.000 | 850.200.000 |
| AST-02 Piutang Progres Proyek      | 120.000.000 |  +225.000.000 | 345.000.000 |
| AST-03 Piutang Retensi             |  30.000.000 |   +15.000.000 |  45.000.000 |
| AST-04 Persediaan Bahan Material   |  80.000.000 |   −40.000.000 |  40.000.000 |
| LIA-01 Utang Subkontraktor         |  50.000.000 |   +95.000.000 | 145.000.000 |
| LIA-02 Uang Muka Proyek Diterima   | 100.000.000 |  +260.000.000 | 360.000.000 |
| LIA-03 Utang Retensi Subkontraktor |  15.000.000 |             0 |  15.000.000 |
| LIA-04 PPN Keluaran                |           0 |   +35.200.000 |  35.200.000 |
| EKT-01 Modal Pemilik               | 565.000.000 |             0 | 565.000.000 |
| EKT-02 Laba Ditahan                |           0 |             0 |           0 |
| PDT-01 Pendapatan Progres Proyek   |           0 |  +300.000.000 | 300.000.000 |
| BBN-01 Beban Pokok Proyek          |           0 |   +40.000.000 |  40.000.000 |
| BBN-02 Beban Subkontraktor         |           0 |  +100.000.000 | 100.000.000 |

Mutasi Bank rinci: T1 +222.000.000, T6 +133.200.000, T5 −5.000.000 (T4+reversal saling meniadakan) = **+350.200.000**. ✓
Mutasi Uang Muka: T1 +200.000.000, T2 −60.000.000, T6 +120.000.000 = **+260.000.000**. ✓

**Verifikasi Total Debit = Total Kredit** (jumlah 2 arah — per baris jurnal DAN akumulasi saldo akhir):

- Sisi debit (Aset+Beban): 850.200.000 + 345.000.000 + 45.000.000 + 40.000.000 + 40.000.000 + 100.000.000 = **1.420.200.000**
- Sisi kredit (Liabilitas+Ekuitas+Pendapatan): 145.000.000 + 360.000.000 + 15.000.000 + 35.200.000 + 565.000.000 + 300.000.000 = **1.420.200.000**

✓ Balance — angka ini jadi acuan mutlak Trial Balance §2 dan Laporan Keuangan file 04.

## 2. Breakdown per Proyek (dimensi `business_unit_id`)

| Proyek                    | Jurnal terkait        |  Pendapatan | Beban Pokok + Subkon |                                                     Kas masuk bersih (Bank) |
| ------------------------- | --------------------- | ----------: | -------------------: | --------------------------------------------------------------------------: |
| PRJ-GDA (Gedung Kantor A) | T1,T2,T3,T4+rev,T5,T7 | 300.000.000 |          140.000.000 | 217.000.000 (T1 +222.000.000 − T5 5.000.000; T4+reversal saling meniadakan) |
| PRJ-JMB (Jembatan B)      | T6                    |           0 |                    0 |                                                                 133.200.000 |

217.000.000 + 133.200.000 = 350.200.000, cocok dengan total mutasi Bank konsolidasi di §1.

**Sebab-akibat:** breakdown per proyek ini yang jadi ALASAN UTAMA dimensi `business_unit_id` dipakai konsisten di semua jurnal file 01 — tanpa breakdown ini, pemilik usaha tidak bisa tahu proyek MANA yang sebenarnya menguntungkan (PRJ-GDA sudah ada Pendapatan+Beban, PRJ-JMB baru terima uang muka doang, belum ada progres/beban sama sekali) kalau semua transaksi cuma dilihat gabungan.

## 3. Skenario Pengujian

| Skenario | Detail                                                                                                                                                                  | Hasil                                                                                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `accounting/general-ledger/detail-ledger` dengan `chart_of_account_id` = AST-01 Bank, `business_unit_id` = PRJ-GDA, `date_from`/`date_to` mencakup semua tanggal T1-T7. | `opening_debit` sesuai saldo awal Bank, `lines` berisi T1, T5, T4, reversal-T4 (bukan T6 — beda proyek), `closing_debit` = saldo akhir Bank porsi PRJ-GDA saja. |
| Positif  | `accounting/general-ledger/summary-by-account` tanpa `business_unit_id` (semua proyek).                                                                                 | Baris AST-01 Bank `closing_debit − closing_credit` = 850.200.000 (gabungan PRJ-GDA + PRJ-JMB).                                                                  |
| Positif  | `accounting/general-ledger/summary-by-account` dengan `business_unit_id` = PRJ-JMB, `chart_of_account_id` = AST-01.                                                     | Hanya mutasi T6 (+133.200.000) — memverifikasi total 2 proyek = total konsolidasi (850.200.000 = mutasi PRJ-GDA + mutasi PRJ-JMB + saldo awal).                 |
| Positif  | `accounting/general-ledger/trial-balance` dengan `date_to` = tanggal T7 (semua jurnal sudah posted).                                                                    | `total_debit` = `total_credit` = **1.420.200.000**, tiap baris akun cocok dengan tabel §1.                                                                      |
| Positif  | `accounting/general-ledger/by-period` dengan `accounting_period_id` bulan berjalan (FY2026-0X).                                                                         | Hanya menampilkan baris GL dengan `trans_date` di rentang periode itu.                                                                                          |
| Negatif  | `trial-balance`/`detail-ledger` dengan `chart_of_account_id` yang tidak ada di `chart_of_accounts`.                                                                     | 422, `chart_of_account_id` invalid (`exists:chart_of_accounts,id`).                                                                                             |
| Negatif  | `detail-ledger` dengan `date_to` sebelum `date_from`.                                                                                                                   | 422, `date_to` gagal validasi `after_or_equal:date_from`.                                                                                                       |
| Negatif  | Filter dengan `business_unit_id` yang tidak ada di `business_units`.                                                                                                    | 422, `business_unit_id` invalid.                                                                                                                                |

## Netralisasi

- Tidak ada perubahan state di file ini (semua endpoint read-only `GET`-style via `POST`) — tidak perlu netralisasi khusus, cukup pastikan jurnal test file 01 sudah dinetralisasi sesuai catatannya sendiri.
