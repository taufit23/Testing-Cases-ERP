---
title: (Nonprofit / NGO) — 00. Profil Perusahaan & Master Data
category: accounting-ngo
description: Skenario Yayasan Peduli Bangsa (NGO). Sistem TIDAK punya entitas "fund"/"donor" terpisah — dana terikat/tidak terikat disimulasikan lewat Chart of Accounts (akun ekuitas terpisah) + Business Unit sebagai dimensi Program.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

## Profil Perusahaan (Skenario)

**Yayasan Peduli Bangsa** — organisasi non-pemerintah/nirlaba (fiktif), fokus program pendidikan anak jalanan dan bantuan bencana alam. Bebas PPN untuk seluruh kegiatan (sosial non-komersial, tidak ada transaksi kena pajak di suite ini).

> **Catatan penting soal "fund accounting"**: sistem ERP ini **TIDAK punya tabel/model "Fund" atau "Donor"** (sudah dicek — tidak ada di `database/migrations/`, `app/Models/`, `app/Http/Controllers/`). Tidak ada juga validasi otomatis yang "mengunci" suatu akun kas/bank supaya hanya boleh dipakai untuk dimensi tertentu. Maka skenario "dana terikat vs tidak terikat" di suite ini disimulasikan dengan 2 mekanisme yang BENAR-BENAR ada di sistem:
>
> 1. **Business Unit** (Business Units) dipakai sebagai dimensi **Program**, bukan lini produksi/cabang seperti suite lain — field `business_unit_id` dilekatkan per baris jurnal.
> 2. **Chart of Accounts terpisah** untuk ekuitas terikat vs tidak terikat (`EKT-01` vs `EKT-02` di bawah) — pemisahan saldo terjadi karena akunnya beda, bukan karena sistem mem-validasi "restriksi dana".
>
> Disiplin "dana Donor A hanya boleh dipakai untuk Program Pendidikan" adalah **disiplin operasional yayasan**, BUKAN constraint yang ditegakkan sistem — lihat kasus Negatif di file [`01`](./01-jurnal-hibah-dan-fund-accounting.id.md) yang membuktikan sistem tidak menolak kombinasi akun/dimensi yang "salah" secara donor.

2 program utama + 1 unit operasional, dipetakan ke **Business Unit** (tipe `cost` — cost center, bukan profit center, karena yayasan tidak mengejar laba):

- **Program Pendidikan Anak** — didanai oleh Donor A (disimulasikan lewat EKT-02 + dimensi PRG-EDU).
- **Program Bantuan Bencana** — didanai oleh Donor B (disimulasikan lewat EKT-02 + dimensi PRG-DIS).
- **Operasional Umum** — didanai dari donasi publik tidak terikat (EKT-01 + dimensi PRG-GEN).

## 1. Chart of Account Type (`client-master/chart-of-account-types`)

Standar 5 tipe dipakai (Aset, Liabilitas, Ekuitas, Pendapatan, Beban) — pakai yang sudah tersedia dari `ChartOfAccountTypeTemplateSeeder`/`use-template` di endpoint `client-master/chart-of-accounts/use-template`, jangan create manual dari nol kalau template branch sudah ada.

## 2. Chart of Accounts (**Chart of Accounts — `create`**)

Field request nyata (dari `ChartOfAccounts` controller): `type_id` (required, exists di `chart_of_accounts_types`), `code` (required, max:50), `name` (required, max:255), `level` (required, int), `is_active`, `balance_required`, `is_cash_account`, `is_ar_control_account`, `is_ap_control_account`, `is_retained_earnings_account`, `is_opening_balance_equity_account` (semua boolean nullable), `default_business_units_id` (nullable, exists `business_units`).

| Kode   | Nama Akun                                    | Tipe                | Field khusus di payload                                                                                                                                           |
| ------ | -------------------------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AST-01 | Bank Mandiri Yayasan (Umum)                  | Aset Lancar         | `is_cash_account: true`                                                                                                                                           |
| AST-02 | Bank BCA (Khusus Donor Pendidikan)           | Aset Lancar         | `is_cash_account: true`, `default_business_units_id: <PRG-EDU>`                                                                                                   |
| AST-03 | Piutang Komitmen Hibah Donor                 | Aset Lancar         | `is_ar_control_account: true`, `balance_required: true`                                                                                                           |
| LIA-01 | Utang Program                                | Liabilitas          | `is_ap_control_account: true`, `balance_required: true`                                                                                                           |
| EKT-01 | Aset Netto Tidak Terikat (Unrestricted)      | Ekuitas             | `is_opening_balance_equity_account: true` — **HANYA BOLEH 1 akun per branch** ber-flag ini (validasi server, dipakai `JournalPostingService::syncOpeningBalance`) |
| EKT-02 | Aset Netto Terikat (Restricted Fund Balance) | Ekuitas             | `balance_required: true` — saldo dana terikat, tanpa flag khusus lain                                                                                             |
| EKT-03 | Laba Ditahan (Sisa Hasil Usaha/SHU)          | Ekuitas             | `is_retained_earnings_account: true` — **HANYA BOLEH 1 akun per branch**, dipakai `FiscalYear::closeYear()`                                                       |
| PDT-01 | Pendapatan Hibah Terikat - Pendidikan        | Pendapatan          | —                                                                                                                                                                 |
| PDT-02 | Pendapatan Hibah Terikat - Bencana           | Pendapatan          | —                                                                                                                                                                 |
| PDT-03 | Pendapatan Donasi Tidak Terikat - Publik     | Pendapatan          | —                                                                                                                                                                 |
| BBN-01 | Beban Program Pendidikan                     | Beban               | —                                                                                                                                                                 |
| BBN-02 | Beban Program Bantuan Bencana                | Beban               | —                                                                                                                                                                 |
| BBN-03 | Beban Operasional Kantor                     | Beban               | —                                                                                                                                                                 |
| AST-04 | Kendaraan Operasional Bencana                | Aset Tetap          | — dipakai file 05 (Fixed Assets)                                                                                                                                  |
| AST-05 | Akumulasi Penyusutan Kendaraan               | Aset Tetap (kontra) | — dipakai file 05 (Fixed Assets)                                                                                                                                  |
| BBN-04 | Beban Penyusutan Aset Tetap                  | Beban               | — dipakai file 05 (Fixed Assets)                                                                                                                                  |

> Ditambah `PDT-02` (Pendapatan Hibah Terikat - Bencana) dan `BBN-02` (Beban Program Bantuan Bencana) dibanding draf lama — draf sebelumnya cuma punya 1 akun pendapatan/beban program, padahal skenario menyebut 2 program (Pendidikan & Bencana) yang saling terpisah pelaporannya di file 04. Tanpa akun ini, Program Bantuan Bencana tidak bisa diuji karena tidak ada akun pendapatan/bebannya sendiri. `AST-04`/`AST-05`/`BBN-04` ditambahkan untuk mendukung skenario Fixed Assets di file 05 (kendaraan operasional bencana + akumulasi penyusutan + beban penyusutan) — draf lama tidak menyediakan akun aset tetap sama sekali padahal file 05 butuh itu.

## 3. Fiscal Year & Accounting Period (**Fiscal Year**, **Accounting Period**)

**WAJIB ada sebelum saldo awal bisa dibuat** — `chart-of-accounts-balances/create` menolak dengan error `"No active accounting period found for today's date"` kalau tidak ada periode aktif (`is_closed:false`, `is_locked:false`) yang mencakup tanggal hari ini. Draf sebelumnya tidak punya bagian ini sama sekali — gap kritis.

| Skenario                           | Payload kunci                                                                                           | Hasil                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Positif — buat Fiscal Year         | `POST client-master/fiscal-year/create {name:"FY2026", start_date:"2026-01-01", end_date:"2026-12-31"}` | 201                                                                             |
| Positif — generate periode bulanan | `POST client-master/fiscal-year/generate-accounting-period {fiscal_year_id, duration_type:"monthly"}`   | 201, 12 `AccountingPeriod` (Jan-Des 2026) ter-generate, semua `is_closed:false` |

## 4. Business Unit / Dimensi Program (**Business Units — `create`**)

Field nyata: `code` (required, max:50), `name` (required, max:150), `parent_id` (nullable), `is_active`, `default_unit_type` (nullable, `in:cost,profit,both`).

- **Program Pendidikan Anak** — `code:"PRG-EDU"`, `default_unit_type:"cost"`
- **Program Bantuan Bencana** — `code:"PRG-DIS"`, `default_unit_type:"cost"`
- **Operasional Umum** — `code:"PRG-GEN"`, `default_unit_type:"cost"`

## 5. Saldo Awal Perusahaan (**Chart of Accounts Balances — `create`**, **Bank Accounts — `create`**)

Prasyarat: Fiscal Year + periode Januari 2026 sudah ada (§3), akun EKT-01 sudah ditandai `is_opening_balance_equity_account:true` (§2) — kalau lupa, `JournalPostingService::syncOpeningBalance()` tidak tahu mau nge-lawan-kan saldo awal ke akun ekuitas mana dan opening balance tetap "mengambang" (tidak masuk GL walau row `chart_of_accounts_balances` sukses dibuat).

| Akun                               |  Saldo Awal | Endpoint & field kunci                                                                                               |
| ---------------------------------- | ----------: | -------------------------------------------------------------------------------------------------------------------- |
| AST-01 Bank Mandiri Yayasan (Umum) |  50.000.000 | `finance/bank-accounts/create {chart_of_account_id, opening_balance:50000000, ...}`                                  |
| AST-02 Bank BCA (Donor Pendidikan) | 100.000.000 | `finance/bank-accounts/create {chart_of_account_id, opening_balance:100000000, ...}`                                 |
| AST-03 Piutang Komitmen Hibah      |  30.000.000 | `chart-of-accounts-balances/create {chart_of_account_id, opening_balance:30000000, accounting_period_id:<Jan 2026>}` |
| LIA-01 Utang Program               |  10.000.000 | `chart-of-accounts-balances/create {..., opening_balance:10000000}`                                                  |
| EKT-02 Aset Netto Terikat          | 100.000.000 | `chart-of-accounts-balances/create {..., opening_balance:100000000}` — saldo awal dana terikat donor                 |

Total Aset = 50.000.000 + 100.000.000 + 30.000.000 = **180.000.000**
Total Liabilitas & Dana Terikat = 10.000.000 (LIA-01) + 100.000.000 (EKT-02) = **110.000.000**
→ **EKT-01 (Aset Netto Tidak Terikat) otomatis bersaldo kredit 70.000.000** (dihitung sistem via `syncOpeningBalance`, tidak diinput manual — konsisten dengan pola opening balance di suite `accounting`/`accounting-manufaktur-2`).

| Skenario                                              | Detail                                                                        | Hasil                                                                                                                                                                                 |
| ----------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — verifikasi posting ke GL                    | Setelah semua baris §5 dibuat, `POST accounting/general-ledger/trial-balance` | Trial Balance saldo awal balanced: Debit 180.000.000 = Kredit 180.000.000 (10jt LIA-01 + 100jt EKT-02 + 70jt EKT-01)                                                                  |
| Negatif — buat saldo awal sebelum periode Januari ada | `chart-of-accounts-balances/create` dipanggil sebelum §3 dikerjakan           | Ditolak — error "No active accounting period found for today's date" (asumsi tanggal server dalam rentang Jan 2026 test; kalau tidak, gunakan periode yang mencakup tanggal hari ini) |

## Netralisasi

- Hapus (`delete`) seluruh baris `chart-of-accounts-balances` & `bank-accounts` test lewat endpoint masing-masing (hard-delete, tidak ada soft-delete di sistem ini) — journal opening-balance otomatis yang sudah ke-posting ke GL tidak ikut terhapus otomatis, harus di-reverse manual lewat `accounting/journals/reverse` kalau perlu reset total.
- Business Unit, Chart of Accounts, Fiscal Year/Accounting Period boleh dibiarkan sebagai master data baseline untuk file 01-06.
