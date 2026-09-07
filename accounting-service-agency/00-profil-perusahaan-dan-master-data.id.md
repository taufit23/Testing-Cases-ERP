---
title: (Service Business / Agency) — 00. Profil Perusahaan & Master Data
category: accounting-service-agency
description: Skenario PT Kreatif Digital Solusi (Agency) berbasis revenue invoice & recurring billing tanpa inventory. Setup COA, Business Unit (Divisi), dan Saldo Awal.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

## Profil Perusahaan (Skenario)

**PT Kreatif Digital Solusi** — agensi pemasaran digital dan pengembangan software (fiktif). Fokus bisnis pada penyediaan jasa konsultasi, retainer bulanan (recurring billing), dan proyek pengembangan software. Tidak memiliki persediaan barang dagang (inventory-free).

Sudah menjadi **PKP** (PPN 11%). Memiliki 2 divisi utama (Business Unit):

- **Divisi Digital Marketing** — jasa retainer bulanan (SEO, Ads Management).
- **Divisi Software Development** — jasa pembuatan aplikasi berbasis proyek.

## 1. Chart of Accounts (**Chart of Accounts**)

| Kode   | Nama Akun                                    | Tipe                     | Flag khusus                                             |
| ------ | -------------------------------------------- | ------------------------ | ------------------------------------------------------- |
| AST-01 | Kas Kecil Kantor                             | Aset Lancar              | `is_cash_account: true`, `balance_required: true`       |
| AST-02 | Bank Mandiri Operasional                     | Aset Lancar              | `is_cash_account: true`                                 |
| AST-03 | Piutang Usaha                                | Aset Lancar              | `is_ar_control_account: true`, `balance_required: true` |
| AST-04 | PPN Masukan                                  | Aset Lancar              | `is_tax: true`, `tax_id: <PPN 11%>`                     |
| LIA-01 | Utang Usaha                                  | Liabilitas Jangka Pendek | `is_ap_control_account: true`, `balance_required: true` |
| LIA-02 | PPN Keluaran                                 | Liabilitas Jangka Pendek | `is_tax: true`, `tax_id: <PPN 11%>`                     |
| LIA-03 | Pendapatan Diterima Dimuka (Retainer Client) | Liabilitas Jangka Pendek | `balance_required: true`                                |
| EKT-01 | Modal Pemilik                                | Ekuitas                  | `is_opening_balance_equity_account: true`               |
| EKT-02 | Laba Ditahan                                 | Ekuitas                  | `is_retained_earnings_account: true`                    |
| PDT-01 | Pendapatan Jasa Digital Marketing            | Pendapatan               | —                                                       |
| PDT-02 | Pendapatan Jasa Software Development         | Pendapatan               | —                                                       |
| BBN-01 | Beban Gaji Karyawan                          | Beban                    | —                                                       |
| BBN-02 | Beban Sewa Cloud Server (AWS/GCP)            | Beban                    | —                                                       |

## 2. Business Unit / Dimensi Divisi (**Business Units**)

- **Divisi Digital Marketing** (`code: DIV-MKT`)
- **Divisi Software Development** (`code: DIV-DEV`)

## 3. Saldo Awal Perusahaan (**Chart of Accounts Balances**, **Bank Accounts**)

| Akun                              |  Saldo Awal | Jalur                        |
| --------------------------------- | ----------: | ---------------------------- |
| AST-01 Kas Kecil Kantor           |   5.000.000 | `chart-of-accounts-balances` |
| AST-02 Bank Mandiri Operasional   | 150.000.000 | `finance/bank-accounts`      |
| AST-03 Piutang Usaha              |  25.000.000 | `chart-of-accounts-balances` |
| LIA-01 Utang Usaha                |  10.000.000 | `chart-of-accounts-balances` |
| LIA-03 Pendapatan Diterima Dimuka |  20.000.000 | `chart-of-accounts-balances` |

Total Aset = 5.000.000 + 150.000.000 + 25.000.000 = **180.000.000**
Total Liabilitas = 10.000.000 + 20.000.000 = **30.000.000**
→ **Modal Pemilik (EKT-01) otomatis bersaldo kredit 150.000.000**
