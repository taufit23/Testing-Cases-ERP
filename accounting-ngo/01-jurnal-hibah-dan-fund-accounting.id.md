---
title: (Nonprofit / NGO) — 01. Jurnal Hibah & Dimensi Program
category: accounting-ngo
description: Jurnal manual penerimaan hibah/donasi dan realisasi beban per program, memakai Business Unit sebagai dimensi — bukan fitur "fund accounting" bawaan (tidak ada di sistem).
visibility: internal
---

# 01. Jurnal Hibah & Dimensi Program

> Prasyarat: [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) sudah lengkap — Fiscal Year FY2026 + periode Januari 2026 open, EKT-01 otomatis bersaldo kredit 70.000.000, Trial Balance saldo awal balanced di 180.000.000. Endpoint jurnal: **Journals — `create`** (lihat `Accounting\Journal` controller). `PurchaseConfig.requires_journal_approval` diasumsikan **false** (auto-approve, sama pola dengan suite lain) kecuali disebutkan lain.
>
> Field request nyata: `code` (unique per branch — pakai **Journals — `next-code`** untuk generate), `date` (`Y-m-d`), `descriptions`, `lines[]` (min 2) masing-masing `account_id`, `business_unit_id` (nullable), `debit`, `credit`. Header baru dibuat berstatus `draft`; kalau baris balance (total debit = total kredit) langsung naik ke `JRN_PENDING_REVIEW` (approval off → auto-post berikutnya lewat **Journals — `post`**).

## 1.1 Terima Hibah Terikat Pendidikan (Dr Bank BCA Donor / Cr Pendapatan Hibah Pendidikan)

| Skenario    | Payload kunci                                                                                                                             | Hasil                                |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| Positif     | `date:"2026-01-05"`, `lines:[{AST-02, debit:50000000, business_unit_id:<PRG-EDU>},{PDT-01, credit:50000000, business_unit_id:<PRG-EDU>}]` | 201, balanced → `JRN_PENDING_REVIEW` |
| Netralisasi | `POST accounting/journals/post` lalu `reverse` kalau ingin reset — dibiarkan posted sebagai baseline file 02-06                           |

## 1.2 Terima Hibah Terikat Bencana (Dr Bank Mandiri Umum / Cr Pendapatan Hibah Bencana)

Yayasan tidak punya rekening bank khusus per donor bencana — dana masuk ke Bank Mandiri Umum (AST-01), dipisahkan lewat dimensi PRG-DIS saja (bukan lewat akun bank terpisah).

| Skenario | Payload kunci                                                                                                                             | Hasil        |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Positif  | `date:"2026-01-10"`, `lines:[{AST-01, debit:40000000, business_unit_id:<PRG-DIS>},{PDT-02, credit:40000000, business_unit_id:<PRG-DIS>}]` | 201 → posted |

## 1.3 Terima Donasi Publik Tidak Terikat (Dr Bank Mandiri Umum / Cr Pendapatan Donasi Publik)

| Skenario | Payload kunci                                                                                                                             | Hasil        |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Positif  | `date:"2026-01-08"`, `lines:[{AST-01, debit:10000000, business_unit_id:<PRG-GEN>},{PDT-03, credit:10000000, business_unit_id:<PRG-GEN>}]` | 201 → posted |

## 1.4 Realisasi Beban Program Pendidikan

| Skenario | Payload kunci                                                                                                                             | Hasil                                                                                                      |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Positif  | `date:"2026-01-15"`, `lines:[{BBN-01, debit:15000000, business_unit_id:<PRG-EDU>},{AST-02, credit:15000000, business_unit_id:<PRG-EDU>}]` | 201 → posted — saldo AST-02 setelah posted: 100.000.000 + 50.000.000 (§1.1) − 15.000.000 = **135.000.000** |

## 1.5 Realisasi Beban Program Bantuan Bencana

| Skenario | Payload kunci                                                                                                                             | Hasil        |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Positif  | `date:"2026-01-20"`, `lines:[{BBN-02, debit:12000000, business_unit_id:<PRG-DIS>},{AST-01, credit:12000000, business_unit_id:<PRG-DIS>}]` | 201 → posted |

## 1.6 Beban Operasional Kantor (Tidak Terikat)

| Skenario | Payload kunci                                                                                                                           | Hasil                                                                                                                                           |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `date:"2026-01-22"`, `lines:[{BBN-03, debit:5000000, business_unit_id:<PRG-GEN>},{AST-01, credit:5000000, business_unit_id:<PRG-GEN>}]` | 201 → posted — saldo AST-01 setelah posted: 50.000.000 + 40.000.000 (§1.2) + 10.000.000 (§1.3) − 12.000.000 (§1.5) − 5.000.000 = **83.000.000** |

## 1.7 Pakai Bank Donor Pendidikan untuk Beban Operasional Umum (Negatif — Sistem TIDAK Menolak)

Klaim di draf lama ("seharusnya ditolak jika ada validasi restriksi bank vs dimensi") **TIDAK akurat** — sudah dicek, tidak ada validasi seperti itu di `Accounting\Journal` controller maupun di model `ChartOfAccounts`/`BusinessUnit`. `default_business_units_id` pada COA (§2 file 00) hanya nilai default UI, bukan constraint hard-block.

| Skenario                                         | Payload kunci                                                                                                                                                                                                                                         | Hasil                                                                                                                                                                                                                                                               |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif (perilaku aktual, bukan validasi sistem) | `date:"2026-01-25"`, `lines:[{BBN-03, debit:3000000, business_unit_id:<PRG-GEN>},{AST-02, credit:3000000, business_unit_id:<PRG-GEN>}]` — pakai Bank BCA (khusus Donor Pendidikan) untuk beban PRG-GEN yang seharusnya tidak terikat donor pendidikan | 201, **tetap diterima & posted** — TIDAK ada penolakan. 🔧 **Gap fitur (bukan bug)**: kalau yayasan butuh "restricted fund enforcement" sungguhan (menolak transaksi lintas dana), ini belum diimplementasikan; saat ini murni disiplin operasional user saat input |
| Netralisasi — WAJIB reverse                      | `POST accounting/journals/reverse {slug}` segera setelah verifikasi di atas, supaya saldo AST-02 tidak ikut tercemar ke baseline file 02-06                                                                                                           | Saldo AST-02 balik ke 135.000.000 (§1.4)                                                                                                                                                                                                                            |

## 1.8 Jurnal Tidak Balance (Negatif — Validasi Dasar)

| Skenario | Payload kunci                                                                                          | Hasil                                                                                                                                                                                                                 |
| -------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negatif  | `date:"2026-01-26"`, `lines:[{BBN-03, debit:2000000},{AST-01, credit:1000000}]` (total debit ≠ kredit) | 422/validator error, atau tersimpan `draft` tapi tidak naik ke `JRN_PENDING_REVIEW` (tidak bisa di-post) — cek behavior aktual, jangan asumsikan 422 murni kalau ternyata sistem menyimpan sebagai draft tak seimbang |

## 1.9 Post-Bulk & Verifikasi Trial Balance

| Skenario | Detail                                                                                                  | Hasil                                                                               |
| -------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Positif  | `PUT accounting/journals/post-bulk` untuk semua jurnal balance §1.1-1.6 yang masih `JRN_PENDING_REVIEW` | Semua posted, GL entries terbentuk                                                  |
| Positif  | `POST accounting/general-ledger/trial-balance`                                                          | Balanced: total Debit = total Kredit = **280.000.000** (lihat rincian di Ringkasan) |

## Ringkasan Saldo Akun Kunci Setelah File 01 (Baseline untuk File 02-06)

| Akun                               |                                                          Saldo Setelah File 01 |
| ---------------------------------- | -----------------------------------------------------------------------------: |
| AST-01 Bank Mandiri Yayasan (Umum) | 50.000.000 + 40.000.000 + 10.000.000 − 12.000.000 − 5.000.000 = **83.000.000** |
| AST-02 Bank BCA (Donor Pendidikan) |                        100.000.000 + 50.000.000 − 15.000.000 = **135.000.000** |
| AST-03 Piutang Komitmen Hibah      |                                         30.000.000 (tidak berubah di file ini) |
| LIA-01 Utang Program               |                                                     10.000.000 (tidak berubah) |
| EKT-01 Aset Netto Tidak Terikat    |                 70.000.000 (saldo awal, closing entry baru terjadi di file 03) |
| EKT-02 Aset Netto Terikat          |                                                    100.000.000 (tidak berubah) |
| PDT-01 Pendapatan Hibah Pendidikan |                                                                     50.000.000 |
| PDT-02 Pendapatan Hibah Bencana    |                                                                     40.000.000 |
| PDT-03 Pendapatan Donasi Publik    |                                                                     10.000.000 |
| BBN-01 Beban Program Pendidikan    |                                                                     15.000.000 |
| BBN-02 Beban Program Bencana       |                                                                     12.000.000 |
| BBN-03 Beban Operasional Kantor    |                                                                      5.000.000 |

Cek silang: Aset (83.000.000+135.000.000+30.000.000=**248.000.000**) + Beban (15.000.000+12.000.000+5.000.000=**32.000.000**) = **280.000.000** = Liabilitas (10.000.000) + Ekuitas (70.000.000+100.000.000=170.000.000) + Pendapatan (50.000.000+40.000.000+10.000.000=100.000.000) = **280.000.000** ✅

## Netralisasi

- Jurnal §1.1-1.6 dibiarkan posted sebagai baseline file 02-06.
- Jurnal §1.7 WAJIB direverse (lihat instruksi di baris itu).
- Jurnal §1.8 (kalau sempat tersimpan) dihapus lewat `accounting/journals/delete` selama masih `draft` (belum posted, hard-delete diperbolehkan).
