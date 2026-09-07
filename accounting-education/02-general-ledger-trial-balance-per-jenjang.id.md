---
title: (Yayasan Pendidikan) — 02. GL & Trial Balance per Jenjang
category: accounting-education
description: Verifikasi General Ledger detail per akun, Summary by Account, dan Trial Balance konsolidasi + filter dimensi per jenjang (SD/SMP) dari seluruh jurnal file 01, direkonsiliasi via T-account.
visibility: internal
---

# 02. GL & Trial Balance per Jenjang

> Prasyarat: [`01-jurnal-spp-dan-beasiswa.id.md`](./01-jurnal-spp-dan-beasiswa.id.md) §1.15 (post-bulk) sudah selesai — semua 14 jurnal `JRN-EDU-001`..`014` berstatus `JRN_POSTED`. File ini TIDAK menambah transaksi baru, murni verifikasi laporan terhadap baseline yang sudah dihitung manual di file `01`.
>
> Endpoint dikonfirmasi dari `routes/accounting.php` prefix **General Ledger**: `list`, `show`, `by-account`, `by-period`, `detail-ledger`, `summary-by-account`, `trial-balance` — semua `POST`, controller `App\Http\Controllers\Accounting\GeneralLedger`.

## 2.1 Trial Balance Konsolidasi

| Skenario | Payload                                                                                                     | Hasil                                                                           |
| -------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/trial-balance {as_of_date:"2026-03-31"}` (tanpa filter `business_units_id`) | `total_debit = total_credit`, seluruh saldo per akun sesuai Ringkasan file `01` |

Rekap saldo per akun yang HARUS muncul persis (dari T-account file `01`):

| Akun                                             |       Saldo | Posisi                                                      |
| ------------------------------------------------ | ----------: | ----------------------------------------------------------- |
| AST-01 Kas Bendahara SD                          |  12.988.000 | Debit                                                       |
| AST-02 Kas Bendahara SMP                         |   2.500.000 | Debit                                                       |
| AST-03 Bank BNI Operasional                      |  60.125.000 | Debit                                                       |
| AST-04 Piutang SPP                               |  34.500.000 | Debit                                                       |
| AST-05 Perlengkapan Belajar & ATK                |  11.000.000 | Debit                                                       |
| AST-06 Gedung Sekolah                            | 120.000.000 | Debit                                                       |
| AST-08 Peralatan Laboratorium IPA                |  18.000.000 | Debit                                                       |
| LIA-01 Utang Usaha                               |  12.000.000 | Kredit                                                      |
| LIA-02 Utang PPh 21 Guru & Karyawan              |   1.725.000 | Kredit                                                      |
| LIA-03 Pendapatan Diterima Dimuka — Uang Pangkal |  16.500.000 | Kredit                                                      |
| EKT-01 Modal/Aset Bersih Yayasan                 | 140.300.000 | Kredit                                                      |
| PDT-01 Pendapatan SPP                            | 140.000.000 | Kredit                                                      |
| PDT-02 Pendapatan Uang Pangkal                   |   1.500.000 | Kredit                                                      |
| PDT-03 Potongan/Beasiswa SPP (kontra-pendapatan) |   2.500.000 | **Debit** (mengurangi total kredit Pendapatan saat direkap) |
| BBN-01 Beban Gaji Guru & Karyawan                |  45.000.000 | Debit                                                       |
| BBN-02 Beban Listrik & Air                       |   2.400.000 | Debit                                                       |
| BBN-03 Beban Perlengkapan Belajar                |   3.000.000 | Debit                                                       |
| BBN-04 Beban Selisih Kas Bendahara               |      12.000 | Debit                                                       |

Total Debit = 12.988.000+2.500.000+60.125.000+34.500.000+11.000.000+120.000.000+18.000.000+2.500.000+45.000.000+2.400.000+3.000.000+12.000 = **312.025.000**
Total Kredit = 12.000.000+1.725.000+16.500.000+140.300.000+140.000.000+1.500.000 = **312.025.000**
→ **HARUS balanced tepat 312.025.000 = 312.025.000** — kalau tidak sama, ada jurnal §1.1-1.14 yang belum ter-post atau salah baris.

| Skenario                                            | Detail                                                     | Hasil                                                                                                                                               |
| --------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — kontra-akun tampil dengan tanda benar** | Cek baris PDT-03 di response `trial-balance`               | Muncul di kolom **debit** (bukan negatif di kolom kredit) — konsisten dengan pola kontra-aset AST-07/AST-09 di file `05`                            |
| Negatif                                             | `as_of_date` sebelum ada jurnal apapun (mis. `2026-01-01`) | Hanya saldo opening balance (file `00` §8) yang muncul, tidak termasuk jurnal file `01` — bukan error, tapi verifikasi filter tanggal bekerja benar |

## 2.2 Trial Balance / GL Filter Dimensi Jenjang SD

| Skenario | Payload                                                                                               | Hasil                                                                                                                                                                                                              |
| -------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif  | `POST accounting/general-ledger/summary-by-account {business_units_id:<SD>, as_of_date:"2026-03-31"}` | Hanya baris berdimensi `business_unit_id = SD` yang muncul — akun tanpa dimensi (LIA-02, LIA-03, EKT-01, AST-05, AST-06, AST-08) TIDAK tampil di filter ini karena baris jurnalnya tidak diberi `business_unit_id` |

Saldo dimensi SD (dari baris jurnal ber-`bu:SD` saja):

| Akun                                |   Saldo SD | Sumber                                                   |
| ----------------------------------- | ---------: | -------------------------------------------------------- |
| AST-01 Kas Bendahara SD             | 12.988.000 | §1.3, §1.10, §1.11                                       |
| AST-04 Piutang SPP (porsi SD)       | 12.500.000 | 75.000.000 (§1.1) − 2.500.000 (§1.2) − 60.000.000 (§1.3) |
| PDT-01 Pendapatan SPP (SD)          | 75.000.000 | §1.1                                                     |
| PDT-02 Pendapatan Uang Pangkal (SD) |    900.000 | §1.4                                                     |
| PDT-03 Potongan Beasiswa (SD)       |  2.500.000 | §1.2                                                     |
| BBN-01 Beban Gaji (SD)              | 25.000.000 | §1.5                                                     |
| BBN-02 Beban Listrik & Air (SD)     |  1.400.000 | §1.9                                                     |
| BBN-03 Beban ATK (SD)               |  1.800.000 | §1.8                                                     |
| BBN-04 Beban Selisih Kas (SD)       |     12.000 | §1.11                                                    |

Pendapatan neto SD = 75.000.000 + 900.000 − 2.500.000 = **73.400.000**
Beban SD = 25.000.000 + 1.400.000 + 1.800.000 + 12.000 = **28.212.000**
→ **Laba Berjalan SD = 73.400.000 − 28.212.000 = 45.188.000**

## 2.3 Trial Balance / GL Filter Dimensi Jenjang SMP

| Skenario | Payload                                                                                                | Hasil                                                       |
| -------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/summary-by-account {business_units_id:<SMP>, as_of_date:"2026-03-31"}` | Hanya baris berdimensi `business_unit_id = SMP` yang muncul |

Saldo dimensi SMP:

| Akun                                 |  Saldo SMP | Sumber                                                                                             |
| ------------------------------------ | ---------: | -------------------------------------------------------------------------------------------------- |
| AST-02 Kas Bendahara SMP             |  2.500.000 | Opening — tidak tersentuh transaksi §1.1-1.14 (penerimaan SMP §1.3 langsung ke Bank tanpa dimensi) |
| AST-04 Piutang SPP (porsi SMP)       | 10.000.000 | 65.000.000 (§1.1) − 55.000.000 (§1.3)                                                              |
| PDT-01 Pendapatan SPP (SMP)          | 65.000.000 | §1.1                                                                                               |
| PDT-02 Pendapatan Uang Pangkal (SMP) |    600.000 | §1.4                                                                                               |
| BBN-01 Beban Gaji (SMP)              | 20.000.000 | §1.5                                                                                               |
| BBN-02 Beban Listrik & Air (SMP)     |  1.000.000 | §1.9                                                                                               |
| BBN-03 Beban ATK (SMP)               |  1.200.000 | §1.8                                                                                               |

Pendapatan neto SMP = 65.000.000 + 600.000 = **65.600.000**
Beban SMP = 20.000.000 + 1.000.000 + 1.200.000 = **22.200.000**
→ **Laba Berjalan SMP = 65.600.000 − 22.200.000 = 43.400.000**

## 2.4 Verifikasi Silang SD + SMP = Konsolidasi

| Item            |         SD |        SMP |           Total | Cocok dengan §2.1?                                                                   |
| --------------- | ---------: | ---------: | --------------: | ------------------------------------------------------------------------------------ |
| Pendapatan neto | 73.400.000 | 65.600.000 | **139.000.000** | PDT-01(140.000.000)+PDT-02(1.500.000)−PDT-03(2.500.000) = 139.000.000 ✓              |
| Beban           | 28.212.000 | 22.200.000 |  **50.412.000** | BBN-01(45.000.000)+BBN-02(2.400.000)+BBN-03(3.000.000)+BBN-04(12.000) = 50.412.000 ✓ |
| Laba Berjalan   | 45.188.000 | 43.400.000 |  **88.588.000** | Cocok dengan Ringkasan file `01` §Ringkasan Saldo Akun Kunci                         |

| Skenario                   | Detail                                                                          | Hasil                                                                                                                                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — WAJIB dijalankan | Bandingkan hasil §2.2 + §2.3 dijumlah manual vs §2.1 (konsolidasi tanpa filter) | Total per akun HARUS sama persis — kalau SD+SMP < konsolidasi, ada baris jurnal yang lolos tanpa `business_unit_id` padahal seharusnya ada (gap dimensi); kalau SD+SMP > konsolidasi, ada duplikasi filter |

## 2.5 General Ledger Detail (`detail-ledger`, `by-account`)

| Skenario | Payload                                                                                                                     | Hasil                                                                                                                                                                                                                              |
| -------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/detail-ledger {chart_of_account_id:<AST-04>, date_from:"2026-03-01", date_to:"2026-03-31"}` | Menampilkan seluruh mutasi Piutang SPP baris-per-baris: opening 12.000.000, +75.000.000 (§1.1 SD), +65.000.000 (§1.1 SMP), −2.500.000 (§1.2), −60.000.000 (§1.3 SD), −55.000.000 (§1.3 SMP) — running balance akhir **34.500.000** |
| Positif  | `POST accounting/general-ledger/by-account {chart_of_account_id:<PDT-03>}`                                                  | Menampilkan 1 baris mutasi (§1.2), running balance 2.500.000 di sisi debit meski akun bertipe Pendapatan (kontra)                                                                                                                  |
| Negatif  | `chart_of_account_id` milik branch lain                                                                                     | 422/`not_found_in_branch` (perilaku sama seperti endpoint `show` client-master lain)                                                                                                                                               |

## Netralisasi

File ini murni read-only (semua endpoint `list`/`show`/`by-account`/`by-period`/`detail-ledger`/`summary-by-account`/`trial-balance` tidak mengubah data) — tidak ada state yang perlu dinetralisasi. Kalau ada jurnal test tambahan dibuat saat eksplorasi manual, ikuti pola netralisasi §1.16 di file `01`.

## Referensi Silang

- [`01-jurnal-spp-dan-beasiswa.id.md`](./01-jurnal-spp-dan-beasiswa.id.md) — sumber seluruh angka baseline di file ini
- [`04-laporan-keuangan-konsolidasi-dan-per-jenjang.id.md`](./04-laporan-keuangan-konsolidasi-dan-per-jenjang.id.md) — Neraca & Laba Rugi dari trial balance yang sama
