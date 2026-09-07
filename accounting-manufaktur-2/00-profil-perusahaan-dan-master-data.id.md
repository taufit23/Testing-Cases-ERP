---
title: (Manufaktur) — Varian 2 — 00. Profil Perusahaan & Master Data
category: accounting-manufaktur-2
description: Skenario baru berdiri sendiri — CV Cahaya Nusantara Sejahtera, manufaktur ringan (minuman kemasan) dengan pinjaman bank, transaksi valas (impor bahan baku), dan periode fiskal kuartalan. Varian kedua dari suite testing/accounting-manufaktur/ (kasus identik, perusahaan berbeda) — fondasi seluruh file di folder ini, TIDAK terhubung ke suite testing/accounting/ (skenario retail).
visibility: internal
---

# 00. Profil Perusahaan & Master Data

> **Suite ini adalah VARIAN KEDUA dari [`../accounting-manufaktur/`](../accounting-manufaktur/)** — logika skenario, jumlah akun, nilai saldo, tanggal, dan temuan bug (§10.0-10.3 dst) SAMA PERSIS dengan suite asli, HANYA nama perusahaan/produk/lokasi/supplier yang berbeda ("CV Sumber Makmur Abadi" → "CV Cahaya Nusantara Sejahtera"). Tujuannya untuk verifikasi konsistensi hasil test di branch/env kedua dengan data berbeda. Kalau nemu penyimpangan hasil antara suite ini dan suite asli padahal langkahnya identik, itu sinyal regresi, bukan variasi skenario yang disengaja.
>
> **Suite ini JUGA berdiri SENDIRI, terpisah total dari [`../accounting/`](../accounting/)** (skenario retail "PT Retail Nusantara Jaya") — beda perusahaan, beda kode akun, beda tahun buku, beda tipe periode (kuartalan, bukan bulanan). Jangan campur data/kode akun dari ketiga suite (`accounting/`, `accounting-manufaktur/`, `accounting-manufaktur-2/`).
>
> **Kenapa suite baru, bukan lanjutan suite lama**: suite retail sudah cukup untuk jalur normal (happy path + validasi dasar). Suite manufaktur (varian 1 & 2 ini) didesain supaya SETIAP skenario menembus kondisi yang lebih berat & realistis: pinjaman bank+bunga, transaksi mata uang asing sungguhan (bukan cuma probe backend), arus biaya produksi (bahan baku→WIP→barang jadi→HPP), dan periode fiskal kuartalan (variasi dari bulanan). Tiap file punya kolom **Label temuan** (🆕 fitur baru / 🔧 improvement kecil / ✅ sudah tercover) di baris yang hasilnya tidak sesuai ekspektasi ideal.
>
> **Pola tiap skenario**: **Positif** (jalur normal, harus sukses dengan nilai output PERSIS seperti yang tertera) / **Negatif** (input/urutan salah, harus DITOLAK dengan pesan jelas) / **Netralisasi** (cara mengembalikan state ke semula).
>
> **Kerjakan urutan file**: 00 → 01 → 02 → 03 → 04 → 05 → 06. Tiap file mengasumsikan file sebelumnya sudah dikerjakan — angka-angka di seluruh suite ini SALING TERKAIT (satu sumber kebenaran), jangan lompat urutan.

## Profil Perusahaan (Skenario)

**CV Cahaya Nusantara Sejahtera** — manufaktur ringan minuman kemasan (minuman sari buah & teh kemasan botol), berlokasi di Sidoarjo. Sudah **PKP**, PPN 11%. Dua lini produksi dijadikan dimensi Business Unit (bukan dimensi cabang/toko seperti suite lama):

- **Lini Produksi A** — Minuman Sari Buah
- **Lini Produksi B** — Teh Kemasan Botol

Ciri yang membedakan dari suite lama (sengaja, supaya menguji jalur kode yang belum pernah tersentuh):

1. **Impor bahan baku kemasan/flavoring dari Singapura** (Emerald Bay Trading Pte Ltd) — dibayar USD, transaksi valas SUNGGUHAN lewat `currency_id`/`foreign_debit`/`foreign_credit`/`exchange_rate` di jurnal (bukan cuma dites di level model seperti probe suite lama).
2. **Pinjaman bank** untuk investasi mesin produksi — liability jangka pendek dengan cicilan pokok+bunga berjalan (belum pernah dites di suite lama sama sekali).
3. **Arus biaya produksi** (bahan baku → barang dalam proses → barang jadi → HPP saat terjual) — lewat jurnal manual (modul Accounting berdiri sendiri, BUKAN modul Manufacturing/MRP karena modul itu belum ada di ERP ini).
4. **Periode fiskal KUARTALAN** (4 periode/tahun), bukan bulanan — variasi `duration_type` yang belum pernah dites.

Tahun buku: **FY2026** (2026-01-01 s/d 2026-12-31), kalender. Mata uang operasional: **IDR**, mata uang transaksi asing: **USD**.

> **Simplifikasi yang disengaja** (supaya file 03 Tutup Tahun Fiskal bisa langsung dites tanpa menunggu transaksi genap 1 tahun): SELURUH transaksi Pendapatan/Beban di suite ini sengaja dikumpulkan di **Kuartal 1 2026** saja — Kuartal 2-4 sengaja dibiarkan kosong. Ini bukan keterbatasan sistem, cuma strategi supaya file 03 §3.3 (Close Fiscal Year) bisa dihitung manual dengan pasti.

## 1. Currency (**Currencies**)

| Skenario    | Payload                                                                                                       | Hasil                                          |
| ----------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Positif     | Pastikan `IDR` sudah ada (base)                                                                               | Tersedia di `client-master/currencies/options` |
| Positif     | `{code:"USD", name:"US Dollar", symbol:"$", thousand_separator:",", decimal_separator:".", decimal_places:2}` | 201 — dipakai transaksi valas di file 02       |
| Netralisasi | — (master global)                                                                                             |

## 2. Chart of Account Type (**Chart of Account Type**)

Sama struktur dengan suite lama (kategori generik akuntansi, bukan spesifik skenario) — kalau branch test ini share instance dengan suite lama, TYPE ini boleh reuse, tidak perlu dibuat ulang:

| #   | Kode | Nama                     | `category` | `normal_balance` | `cash_flow_section` | Grup Laporan (`report_group`) |
| --- | ---- | ------------------------ | ---------- | ---------------- | ------------------- | ----------------------------- |
| 1   | AL   | Aset Lancar              | asset      | debit            | operating           | Balance Sheet                 |
| 2   | AT   | Aset Tetap               | asset      | debit            | investing           | Balance Sheet                 |
| 3   | LJP  | Liabilitas Jangka Pendek | liability  | credit           | operating           | Balance Sheet                 |
| 4   | EK   | Ekuitas                  | equity     | credit           | financing           | Balance Sheet                 |
| 5   | PD   | Pendapatan               | revenue    | credit           | operating           | Income Statement              |
| 6   | BB   | Beban                    | expense    | debit            | operating           | Income Statement              |

Kalau branch test ini TERPISAH (branch baru khusus suite ini, direkomendasikan supaya benar-benar independen), create ke-6 tipe ini dari 0 — validasi sama seperti [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) §2, tidak diulang di sini.

## 3. Chart of Accounts (**Chart of Accounts**)

**30 akun**, kode alfanumerik `AST-*`/`LIA-*`/`EKT-*`/`PDT-*`/`BBN-*` (sengaja beda pola dari suite lama yang numerik 4-digit) — supaya visual jelas kelihatan ini set data berbeda.

### Aset

| Kode   | Nama Akun                            | Tipe        | Flag khusus                                                                                                                 |
| ------ | ------------------------------------ | ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| AST-01 | Kas Kecil Pabrik                     | Aset Lancar | `is_cash_account:true`, `balance_required:true`                                                                             |
| AST-02 | BCA Operasional (IDR)                | Aset Lancar | `is_cash_account:true` (saldo awal via `finance/bank-accounts`)                                                             |
| AST-03 | BCA Valas (USD)                      | Aset Lancar | `is_cash_account:true` (saldo awal via `finance/bank-accounts`, `currency_id:<USD>` — lihat §9, ada temuan penting di sini) |
| AST-04 | Piutang Dagang — Distributor         | Aset Lancar | `is_ar_control_account:true`, `balance_required:true`                                                                       |
| AST-05 | Persediaan Bahan Baku                | Aset Lancar | `balance_required:true`                                                                                                     |
| AST-06 | Persediaan Barang Dalam Proses (WIP) | Aset Lancar | `balance_required:true`                                                                                                     |
| AST-07 | Persediaan Barang Jadi               | Aset Lancar | `balance_required:true`                                                                                                     |
| AST-08 | PPN Masukan                          | Aset Lancar | `is_tax:true`, `tax_id:<PPN 11%>`                                                                                           |
| AST-09 | Mesin Produksi                       | Aset Tetap  | — (dipakai file 05, garis lurus)                                                                                            |
| AST-10 | Akumulasi Penyusutan Mesin Produksi  | Aset Tetap  | Kontra-aset, normal_balance tetap debit (ikut tipe induk), bersaldo negatif karena selalu di-kredit                         |
| AST-11 | Kendaraan Operasional                | Aset Tetap  | — (dipakai file 05, saldo menurun)                                                                                          |
| AST-12 | Akumulasi Penyusutan Kendaraan       | Aset Tetap  | Kontra-aset, sama pola dengan AST-10                                                                                        |

### Liabilitas

| Kode   | Nama Akun                                 | Tipe                     | Flag khusus                                                                                                         |
| ------ | ----------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| LIA-01 | Utang Dagang — Supplier Lokal             | Liabilitas Jangka Pendek | `is_ap_control_account:true`, `balance_required:true`                                                               |
| LIA-02 | Utang Dagang — Supplier Luar Negeri (USD) | Liabilitas Jangka Pendek | `is_ap_control_account:true`, `balance_required:true` — **akun kunci file 02**, saldo dalam IDR hasil translasi USD |
| LIA-03 | PPN Keluaran                              | Liabilitas Jangka Pendek | `is_tax:true`, `tax_id:<PPN 11%>`                                                                                   |
| LIA-04 | Utang PPh 21 Karyawan                     | Liabilitas Jangka Pendek | `balance_required:true`                                                                                             |
| LIA-05 | Utang Bank — Pinjaman Investasi Mesin     | Liabilitas Jangka Pendek | TIDAK `balance_required` (saldo awal 0, baru muncul dari pencairan pinjaman di file 01)                             |

### Ekuitas

| Kode   | Nama Akun        | Tipe    | Flag khusus                                                                |
| ------ | ---------------- | ------- | -------------------------------------------------------------------------- |
| EKT-01 | Modal Pemilik CV | Ekuitas | `is_opening_balance_equity_account:true` — WAJIB tepat 1 akun ber-flag ini |
| EKT-02 | Laba Ditahan     | Ekuitas | `is_retained_earnings_account:true` — WAJIB tepat 1 akun ber-flag ini      |

### Pendapatan

| Kode   | Nama Akun                              | Tipe       |
| ------ | -------------------------------------- | ---------- |
| PDT-01 | Penjualan — Lini A (Minuman Sari Buah) | Pendapatan |
| PDT-02 | Penjualan — Lini B (Teh Kemasan Botol) | Pendapatan |

### Beban

| Kode   | Nama Akun                                     | Tipe                                                                                                         |
| ------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| BBN-01 | Harga Pokok Penjualan                         | Beban                                                                                                        |
| BBN-02 | Beban Overhead Pabrik (Non-Produksi Langsung) | Beban                                                                                                        |
| BBN-03 | Beban Gaji Non-Produksi (Admin/Sales)         | Beban                                                                                                        |
| BBN-04 | Beban Penyusutan Mesin Produksi               | Beban                                                                                                        |
| BBN-05 | Beban Penyusutan Kendaraan                    | Beban                                                                                                        |
| BBN-06 | Beban Bunga Pinjaman Bank                     | Beban                                                                                                        |
| BBN-07 | Beban/Laba Selisih Kurs                       | Beban (bisa bersaldo kredit kalau untung kurs — sama pola kontra seperti AST-10, dicatat manual per file 02) |
| BBN-08 | Beban Susut Bahan Baku                        | Beban                                                                                                        |

| Skenario    | Detail                                                             | Hasil                                                                                                                                                                                    | Label temuan                                              |
| ----------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Positif     | Create ke-30 akun (satu-satu atau `create-bulk`)                   | 201 semua, flag tersimpan **benar-benar** (`GET .../show` ulang untuk verifikasi, bukan cuma percaya response create)                                                                    | ✅                                                         |
| Negatif     | Create akun ke-2 ber-flag `is_opening_balance_equity_account:true` | Tidak ada validasi silang yang menolak (sama seperti suite lama) — kalau ini terjadi, `syncOpeningBalance()` cuma pakai `first()` hasil query, akun kedua diam-diam tidak pernah kepakai | 🔧 sudah dicatat di suite lama, regresi-check saja di sini |
| Netralisasi | `delete` akun test yang belum dipakai transaksi                    |

## 4. Fiscal Year (**Fiscal Year**)

| Skenario    | Payload                                                                                   | Hasil |
| ----------- | ----------------------------------------------------------------------------------------- | ----- |
| Positif     | `{code:"FY2026", name:"Tahun Buku 2026", start_date:"2026-01-01", end_date:"2026-12-31"}` | 201   |
| Netralisasi | `delete` — pastikan tidak ada `accounting_periods` di bawahnya                            |

## 5. Accounting Period — KUARTALAN (**Accounting Period**)

Beda dari suite lama yang generate bulanan — di sini pakai `duration_type:"quarterly"`, belum pernah dites sebelumnya.

| Skenario                     | Detail                                                                                                          | Hasil                                                                                                                                                                                                                                                                                                                                                                   | Label temuan                                                                                                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — generate kuartalan | `PUT client-master/fiscal-year/generate-accounting-period {fiscal_year_id:<FY2026>, duration_type:"quarterly"}` | 4 periode ter-generate: Q1 (2026-01-01 s/d 2026-03-31), Q2 (04-01 s/d 06-30), Q3 (07-01 s/d 09-30), Q4 (10-01 s/d 12-31) — **verifikasi tanggal akhir tiap kuartal benar** (Maret 31 hari, Juni 30 hari, dst — bug umum kalau generator cuma nambah "3 bulan" tanpa hitung hari akhir bulan yang benar)                                                                 | Kalau tanggal akhir kuartal salah (mis. Q1 berakhir 2026-03-30 atau 04-01) → 🆕 bug generator period, laporkan sebagai temuan prioritas tinggi (semua guard next-period di file 03 bergantung pada tanggal ini presisi) |
| Positif — nama periode       | Cek `name` tiap periode                                                                                         | Pastikan label mencerminkan kuartal (`Q1 2026` atau serupa) — kalau generator cuma bikin nama generik "Periode 1", "Periode 2" tanpa konteks kuartal, itu bukan salah secara fungsi tapi kurang informatif di sidebar indicator ([`../../../FEAccounting/app/components/FiscalPeriodIndicator.vue`](../../../../FEAccounting/app/components/FiscalPeriodIndicator.vue)) | Kalau nama generik → 🔧 improvement kecil, tidak blocking                                                                                                                                                               |
| Netralisasi                  | `delete` periode test satu-satu                                                                                 |

## 6. Business Unit — Lini Produksi (**Business Units**)

| Skenario         | Payload                                                                                 | Hasil                                                    |
| ---------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Positif — Lini A | `{code:"LINI-A", name:"Lini Produksi A - Minuman Sari Buah", default_unit_type:"both"}` | 201                                                      |
| Positif — Lini B | `{code:"LINI-B", name:"Lini Produksi B - Teh Kemasan Botol", default_unit_type:"both"}` | 201 — dipakai membedah omzet & biaya per lini di file 04 |
| Netralisasi      | `delete` — pastikan tidak dipakai `journals.business_unit_id` manapun                   |

## 7. Tax — PPN (**Taxes**)

| Skenario                             | Payload                                                                                                                                                                                                                                  | Hasil |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Positif                              | `{name:"PPN 11%", code:"PPN11", rate:11, effect:"increase"}`                                                                                                                                                                             | 201   |
| **Catatan keterbatasan (bukan bug)** | PPN Impor / Bea Masuk atas pembelian bahan baku dari Emerald Bay Trading (file 02) TIDAK dimodelkan di suite ini — hanya nilai barang & utang valas yang dites. Kalau mau test PPN Impor sungguhan, itu scope tambahan di luar suite ini | —     |
| Netralisasi                          | `delete` — pastikan tidak dipakai                                                                                                                                                                                                        |

## 8. Exchange Rates (**Exchange Rates**) — BARU, belum pernah dites di suite lama

| Skenario                                                 | Payload                                                                                                                  | Hasil                                                                                                                                                                              | Label temuan |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Positif — rate awal                                      | `POST client-master/exchange-rates/upsert {currency_id:<USD>, rate_date:"2026-01-01", rate_to_base:15700}`               | 201 — ini rate PERTAMA yang pernah di-upsert untuk kombinasi branch+USD, jadi otomatis `is_active:true`. `1 USD = Rp 15.700` berlaku untuk SEMUA transaksi valas berapapun tanggalnya, TERUS sampai ada rate lain yang di-`activate` secara eksplisit (`ExchangeRate::rateFor()` mengambil row `is_active=true`, bukan berdasar tanggal transaksi — `rate_date` di sini murni metadata pencatatan) | ✅            |
| Positif — rate baru (rupiah melemah)                     | `POST .../upsert {currency_id:<USD>, rate_date:"2026-02-15", rate_to_base:15950}`                                        | 201 — TAPI karena ini rate KEDUA untuk USD, `is_active` TIDAK otomatis true. Rate 15.700 masih yang berlaku sampai ada `POST client-master/exchange-rates/activate {id:<rate 15.950>}` eksplisit (dilakukan di file 02 §2.3, tepat sebelum jurnal pelunasan yang memicu selisih kurs)                                                                                                      | ✅            |
| Negatif                                                  | `rate_to_base: 0` atau negatif                                                                                           | 422 (`min:0.000001`)                                                                                                                                                               | ✅            |
| **Negatif — currency tanpa rate aktif**                  | Jangan upsert rate apapun untuk currency lain (mis. EUR), lalu coba buat jurnal valas dengan `currency_id:<EUR>` (lihat file 02 §2.4)                    | Ditolak: `content.no_active_exchange_rate_found_for_this_currency` — dites lengkap di file 02                                                               | ✅            |
| Netralisasi                                              | `delete` rate test kalau ada yang keliru, TAPI JANGAN hapus 2 rate di atas (15.700 & 15.950) — dipakai lintas file 01/02 |

## 9. Contact (**Contacts**) — DI-SKIP, TIDAK DIPERLUKAN UNTUK SUITE INI

> **Keputusan sesi ini**: suite manufaktur ini fokus MURNI ke modul Accounting (jurnal manual, saldo awal, GL, laporan keuangan, tutup periode/tahun) — TIDAK menyentuh modul Purchasing (Purchase Order) atau Sales (Sales Order) sama sekali. `Contact` (customer/supplier) di project ini HANYA dipakai sebagai FK di dokumen `purchase_orders.contact_id`/`sales_orders.contact_id` dan turunannya (invoice, delivery, dst) — dikonfirmasi TIDAK ADA satupun endpoint accounting murni yang dipakai suite ini (`journals`, `chart-of-accounts-balances`, **Bank Accounts**, **Bank Reconciliations**, **Budgets**, **Assets**) mensyaratkan `contact_id`. Dicek juga: tidak ada satu pun file 01-06 di folder ini yang mereferensikan Contact.

Section ini **SENGAJA DI-SKIP** — tidak perlu create Contact apapun untuk melanjutkan suite ini. Kalau nanti scope diperluas ke Purchasing/Sales (di luar suite manufaktur ini), baru section ini perlu dikerjakan, mengikuti pola [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) yang relevan.

## 10. Saldo Awal — TERMASUK 2 TEMUAN BUG SIGNIFIKAN

**⚠️ Bagian PALING KRITIS di file ini — saldo awal adalah fondasi seluruh laporan keuangan di file-file berikutnya (Trial Balance, Balance Sheet, dst). Kerjakan dengan sangat hati-hati.** Dua endpoint yang terlibat punya kontrak field YANG BERBEDA — perbedaan ini sendiri yang membuka temuan bug baru di §10.0:

| Endpoint                                   | Field tersedia                                                                                                                                                 | Dipakai untuk akun                                |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `finance/bank-accounts`                    | `opening_balance` **SAJA** (1 field numerik)                                                                                                                   | AST-02, AST-03 (akun kas/bank)                    |
| `client-master/chart-of-accounts-balances` | `opening_balance` + `debit_total` + `credit_total` (**3 field terpisah**) — `closing_balance` dihitung SERVER = `opening_balance + debit_total − credit_total` | AST-01, AST-04 s/d AST-07, LIA-01, LIA-02, LIA-04 |

**Kenapa 3 field terpisah di `chart-of-accounts-balances` itu penting** — untuk akun kontrol (AR/AP), saldo awal yang realistis biasanya BUKAN angka bersih tunggal, tapi akumulasi transaksi lama: mis. "total tagihan yang sudah diterbitkan tahun lalu" masuk `debit_total`, "total yang sudah dibayar customer sebelum tanggal cutoff" masuk `credit_total`. Secara akuntansi, `closing_balance` (bukan `opening_balance` mentah) yang SEHARUSNYA jadi saldo riil akun tersebut di Trial Balance hari pertama pembukuan.

Saldo awal yang dipakai (nilai target EKONOMIS, dalam kurung nilai USD kalau relevan):

| Akun                          |           Saldo Awal Target (IDR) | Jalur                                             | Struktur field                                                                                                                                                                                            |
| ----------------------------- | --------------------------------: | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AST-01 Kas Kecil Pabrik       |                        10.000.000 | `chart-of-accounts-balances`, `currency_id:<IDR>` | `opening_balance:10000000`, debit/credit_total: 0                                                                                                                                                         |
| AST-02 BCA Operasional        |                       200.000.000 | `finance/bank-accounts`, `currency_id:<IDR>`      | `opening_balance` saja (endpoint ini tidak punya debit/credit_total)                                                                                                                                      |
| AST-03 BCA Valas              | 78.500.000 (= USD 5.000 × 15.700) | `finance/bank-accounts`, `currency_id:<USD>`      | `opening_balance:5000` — **lihat bug currency §10.2**                                                                                                                                                     |
| AST-04 Piutang Dagang         |                        45.000.000 | `chart-of-accounts-balances`, IDR                 | `opening_balance:0`, `debit_total:45000000`, `credit_total:0` — **lihat bug debit/credit_total §10.1, SENGAJA dipakai sebagai kasus uji karena ini akun kontrol AR yang realistis punya histori tagihan** |
| AST-05 Persediaan Bahan Baku  |                        60.000.000 | `chart-of-accounts-balances`, IDR                 | `opening_balance:60000000`, debit/credit_total: 0                                                                                                                                                         |
| AST-06 Persediaan WIP         |                        15.000.000 | `chart-of-accounts-balances`, IDR                 | `opening_balance:15000000`, debit/credit_total: 0                                                                                                                                                         |
| AST-07 Persediaan Barang Jadi |                        25.000.000 | `chart-of-accounts-balances`, IDR                 | `opening_balance:25000000`, debit/credit_total: 0                                                                                                                                                         |
| LIA-01 Utang Dagang Lokal     |                        30.000.000 | `chart-of-accounts-balances`, IDR                 | `opening_balance:30000000`, debit/credit_total: 0 (lihat catatan ambiguitas di §10.1 kenapa AP TIDAK dipakai sebagai kasus uji `credit_total`)                                                            |
| LIA-02 Utang Dagang LN        | 31.400.000 (= USD 2.000 × 15.700) | `chart-of-accounts-balances`, `currency_id:<USD>` | `opening_balance:2000` — **lihat bug currency §10.3**                                                                                                                                                     |
| LIA-04 Utang PPh 21 Karyawan  |                         3.000.000 | `chart-of-accounts-balances`, IDR                 | `opening_balance:3000000`, debit/credit_total: 0                                                                                                                                                          |

### 10.0 🆕 TEMUAN BARU — `debit_total`/`credit_total` TIDAK PERNAH sampai ke General Ledger

**Dikonfirmasi lewat pembacaan kode langsung** (`App\Http\Controllers\ClientMaster\ChartOfAccountBalances::create()` baris ~122-165, `update()` baris ~198-241, `App\Services\JournalPostingService::syncOpeningBalance()` baris 568-577):

- `syncOpeningBalance()` cuma menerima **satu** parameter numerik: `amount: float`. Tidak ada parameter kedua untuk debit/credit terpisah — kontraknya cuma tahu "satu angka net", tidak tahu konsep `debit_total`/`credit_total` sama sekali.
- `ChartOfAccountBalances::create()` memanggil `syncOpeningBalance(amount: (float) $opening, ...)` — **HANYA `opening_balance`** yang diteruskan. `debit_total`/`credit_total` yang dikirim di payload **tersimpan benar** ke kolom DB, `closing_balance` **terhitung benar** di baris itu (`opening_balance + debit_total − credit_total`) — TAPI journal yang terposting ke GL cuma mencerminkan `opening_balance`, sama sekali tidak mencerminkan `closing_balance`.
- `update()` malah lebih parah: journal HANYA di-refresh kalau request eksplisit mengirim field `opening_balance` (`if ($request->has('opening_balance'))`). Kalau user cuma update `debit_total`/`credit_total` saja (tanpa ikut kirim `opening_balance`), `closing_balance` di baris DB berubah TAPI journal GL **sama sekali tidak di-sync ulang** — GL jadi diam-diam basi (stale) dibanding baris `chart_of_accounts_balances`.

**Akibat nyata**: `client-master/chart-of-accounts-balances/show` (dan turunannya) bisa menampilkan `closing_balance` yang BEDA dengan saldo akun yang sama di Trial Balance/GL (`accounting/general-ledger/trial-balance`, sumbernya GL, bukan tabel balance ini). Ini bug **lebih serius** dari bug currency di §10.2/10.3, karena bisa terjadi di SEMUA akun IDR murni sekalipun (tidak butuh currency asing untuk memicu) — kapan saja ada yang input saldo awal lewat `debit_total`/`credit_total` alih-alih `opening_balance` polos.

**Pertanyaan terbuka (belum terjawab dari kode, dicatat sebagai bagian temuan, bukan diasumsikan)**: `syncOpeningBalance()` sudah membalik sisi debit/credit posting berdasar `normal_balance` akun target (lihat komentar baris 603-613 di kode) untuk parameter `opening_balance` — TAPI kalau nanti `debit_total`/`credit_total` mau ikut diposting, apakah keduanya perlu perlakuan sama (misal utang/AP yang normal_balance-nya kredit, apakah `credit_total` mestinya menambah saldo kredit atau `closing_balance` = `opening_balance + debit_total - credit_total` sudah otomatis "benar" secara tanda buat akun kredit-normal)? Belum ada kode/dokumen yang menjawab ini — makanya §10 tabel di atas SENGAJA tidak menjadikan LIA-01 sebagai kasus uji `credit_total` (supaya reproduksi bug di §10.1 tetap bersih, satu variabel saja: akun debit-normal AR).

### 10.1 Reproduksi bug debit_total/credit_total — Piutang Dagang (AST-04)

| Skenario                                                      | Payload                                                                                                                                                                                                                                                  | Hasil aktual                                                                                                                                                                                                                                                      | Label temuan                                                                                                                                                                        |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Setup**                                                     | `POST client-master/chart-of-accounts-balances/create {chart_of_account_id:<AST-04>, currency_id:<IDR>, opening_balance:0, debit_total:45000000, credit_total:0}`                                                                                        | 201 — baris tersimpan: `opening_balance:0, debit_total:45000000, credit_total:0, closing_balance:45000000` (dihitung BENAR di level row)                                                                                                                          | ✅ row-level benar                                                                                                                                                                   |
| **Negatif (operasional) — cek GL**                            | `GET accounting/general-ledger` untuk akun AST-04 pada tanggal hari ini, ATAU `POST accounting/general-ledger/trial-balance`                                                                                                                             | Saldo AST-04 di GL = **Rp 0**, BUKAN Rp 45.000.000 — karena `syncOpeningBalance()` cuma dikirim `amount:0` (nilai `opening_balance` yang memang sengaja diisi 0, bukan `closing_balance` 45jt)                                                                    | 🆕 **BUG dikonfirmasi**: `chart_of_accounts_balances.closing_balance` (45.000.000) ≠ saldo GL (0) untuk akun yang SAMA PERSIS — dua sumber data yang seharusnya konsisten malah beda |
| **Koreksi manual (workaround sampai bug di atas diperbaiki)** | `PUT client-master/chart-of-accounts-balances/update {id:<balance_id dari step Setup>, opening_balance:45000000, debit_total:0, credit_total:0}` (pindahkan nilai dari `debit_total` ke `opening_balance` supaya `syncOpeningBalance()` ikut memposting) | 201 — GL sekarang Rp 45.000.000, `closing_balance` tetap 45.000.000 (matematis sama seperti sebelum koreksi, tapi representasi datanya jadi "opening_balance polos" — histori "ini dari akumulasi tagihan lama" yang seharusnya ada di `debit_total` jadi hilang) | — (workaround, bukan fix sesungguhnya — dicatat sebagai keterbatasan, bukan solusi ideal)                                                                                           |
| Netralisasi                                                   | Jangan hapus baris ini — dipakai kelanjutan test AR di file-file berikutnya kalau ada                                                                                                                                                                    |

### 10.2 Reproduksi bug currency — BCA Valas

| Skenario                                                      | Payload                                                                                                                                                                             | Hasil aktual                                                                                                                                                                                            | Label temuan                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Negatif (secara operasional, walau technically 201)**       | `POST finance/bank-accounts/create {account_name:"BCA Valas", bank_name:"BCA", account_number:"9988776655", currency_id:<USD>, chart_of_account_id:<AST-03>, opening_balance:5000}` | 201 — TAPI jurnal `JRN-OB-...` yang terposting adalah **Dr AST-03 5.000 / Cr Modal Pemilik 5.000** (dianggap Rp 5.000, BUKAN dikonversi jadi Rp 78.500.000 walau `currency_id` yang dikirim adalah USD) | 🆕 **Fitur baru (gap serius)**: `syncOpeningBalance()` seharusnya menerima parameter `currency_id`+`rate_date`, konversi ke base currency lewat `ExchangeRate::rateFor()`, BUKAN pura-pura opening_balance selalu dalam base currency. Berlaku juga untuk `chart-of-accounts-balances` (lihat §10.3) — akar masalah SAMA di 1 fungsi (`syncOpeningBalance()`), berbeda dari bug §10.0/§10.1 yang akar masalahnya di parameter yang tidak pernah diteruskan sama sekali |
| **Koreksi manual (workaround sampai bug di atas diperbaiki)** | Buat jurnal manual balanced: `POST accounting/journals/create {date:<hari ini>, lines:[{account_id:<AST-03>, debit:78495000},{account_id:<EKT-01>, credit:78495000}]}`, lalu post   | 201 → posted, saldo AST-03 sekarang 5.000 + 78.495.000 = **78.500.000 tepat**                                                                                                                           | — (workaround, bukan fix)                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Netralisasi                                                   | Jangan hapus bank account ini — dipakai file 02/06                                                                                                                                  |

### 10.3 Reproduksi bug currency yang sama — Utang Dagang LN

| Skenario                  | Payload                                                                                                                                                       | Hasil aktual                                                                                                                                                                                                      | Label temuan                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Negatif (operasional)** | `POST client-master/chart-of-accounts-balances/create {chart_of_account_id:<LIA-02>, currency_id:<USD>, opening_balance:2000, debit_total:0, credit_total:0}` | 201 — jurnal `JRN-OB-...`: **Cr LIA-02 2.000 / Dr Modal Pemilik 2.000** (dianggap Rp 2.000, bukan Rp 31.400.000) — bug identik dengan §10.2, konfirmasi ini SYSTEMIC (2 titik kode berbeda, bug yang sama persis) | 🆕 sama seperti di atas — perbaikannya harus di 1 tempat bersama (`JournalPostingService::syncOpeningBalance()`), bukan ditambal di 2 controller terpisah |
| **Koreksi manual**        | `POST accounting/journals/create {lines:[{account_id:<EKT-01>, debit:31398000},{account_id:<LIA-02>, credit:31398000}]}`, post                                | Saldo LIA-02 sekarang 2.000 + 31.398.000 = **31.400.000 tepat**                                                                                                                                                   | —                                                                                                                                                        |
| Netralisasi               | —                                                                                                                                                             |

### 10.4 Sisa Saldo Awal (IDR murni, `opening_balance` polos, tidak ada bug — regression check standar)

| Skenario                                                            | Payload                                                                                                                                                                | Hasil                                                                                                                                                  |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif ×6 (AST-01, AST-02, AST-05, AST-06, AST-07, LIA-01, LIA-04) | Sesuai tabel target di atas — `opening_balance` saja, `debit_total`/`credit_total` dibiarkan 0 (atau tidak dikirim) supaya TIDAK memicu bug §10.0, `currency_id:<IDR>` | 201 tiap satu, jurnal `JRN-OB-...` langsung PAS (tidak butuh koreksi — base currency + opening_balance polos tidak kena bug §10.0/§10.2/§10.3 manapun) |
| Netralisasi                                                         | —                                                                                                                                                                      |

### 10.5 Verifikasi Modal Pemilik (EKT-01) — Total Setelah Semua Koreksi

| Skenario    | Detail                                                                                                                                                                        | Hasil                                                                                                                                                                                                                                                                                                                    |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif     | `POST accounting/general-ledger/trial-balance` setelah §10.0-10.4 lengkap (termasuk koreksi manual §10.1/10.2/10.3 — total 3 koreksi, bukan 2 seperti temuan sesi sebelumnya) | Total Aset = 10.000.000+200.000.000+78.500.000+45.000.000+60.000.000+15.000.000+25.000.000 = **433.500.000**. Total Liabilitas = 30.000.000+31.400.000+3.000.000 = **64.400.000**. EKT-01 Modal Pemilik = 433.500.000 − 64.400.000 = **kredit 369.100.000 tepat**. Trial Balance balanced (`total_debit = total_credit`) |
| Netralisasi | — (data ini adalah fondasi seluruh file berikutnya, JANGAN diubah setelah file 01 mulai dikerjakan)                                                                           |

## Ringkasan Data Master yang Harus Sudah Ada Sebelum Lanjut ke File 01

- [ ] Currency IDR + USD
- [ ] 6 Chart of Account Type
- [ ] 30 Chart of Accounts (lihat §3), flag tersimpan benar
- [ ] Fiscal Year FY2026 + **4 periode KUARTALAN** (bukan 12 bulanan)
- [ ] 2 Business Unit (Lini A, Lini B)
- [ ] Tax PPN 11%
- [ ] 2 Exchange Rate: USD@2026-01-01=15.700, USD@2026-02-15=15.950
- [ ] ~~1 Contact customer + 2 Contact supplier~~ — **DI-SKIP** (§9, tidak dibutuhkan modul Accounting murni)
- [ ] Saldo awal 10 akun terposting + **3 jurnal koreksi manual** (§10.1 AR debit_total, §10.2 bank valas, §10.3 utang LN) — Modal Pemilik final **369.100.000**, Trial Balance balanced
- [ ] Dikonfirmasi 2 kategori bug tercatat: `debit_total`/`credit_total` diabaikan GL (§10.0/10.1) DAN currency diabaikan saat posting saldo awal (§10.2/10.3)

## Referensi Silang

- [`../accounting-manufaktur/00-profil-perusahaan-dan-master-data.id.md`](../accounting-manufaktur/00-profil-perusahaan-dan-master-data.id.md) — file setara di suite manufaktur varian 1 (CV Sumber Makmur Abadi), kasus identik dengan perusahaan berbeda; bandingkan hasil kalau ada penyimpangan tak terduga

- [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) — suite retail terpisah, pola dasar yang direplikasi struktur tabelnya di sini (bukan datanya)
- `App\Http\Controllers\ClientMaster\ChartOfAccountBalances::create()`/`update()` — lokasi kode temuan bug §10.0/§10.1 (parameter `debit_total`/`credit_total` tidak pernah diteruskan ke `syncOpeningBalance()`)
- `App\Services\JournalPostingService::syncOpeningBalance()` — lokasi kode temuan bug §10.0-10.3 sekaligus (signature cuma terima `amount` tunggal, tidak ada `currency_id`/`debit_total`/`credit_total`)
- `App\Models\Accounting\ExchangeRate::rateFor()` — resolusi kurs berdasar flag `is_active` (SATU row aktif per branch+currency, diubah eksplisit lewat endpoint `activate`), BUKAN berdasar tanggal — dasar §8 dan seluruh file 02
