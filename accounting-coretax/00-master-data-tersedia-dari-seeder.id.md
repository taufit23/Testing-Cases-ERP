---
title: (CORETAX) — 00. Master Data Tersedia dari Seeder
category: accounting-coretax
description: Referensi lengkap master data yang SUDAH ADA di database untuk provider CORETAX (branch Pusat) setelah `php artisan migrate:fresh --seed` — bukan langkah "buat dari API" seperti suite fiktif lain, murni dokumentasi apa yang sudah tersedia + gotcha yang ditemukan.
visibility: internal
---

# 00. Master Data Tersedia dari Seeder — CORETAX (Branch Pusat)

## Kenapa suite ini beda dari suite `accounting-*` lain

Semua suite `accounting-manufaktur*`, `accounting-fnb-kafe`, dst dibangun di atas **perusahaan fiktif** — file `00` di suite itu isinya LANGKAH membuat COA/fiscal year/dst dari nol lewat API. Suite ini beda: **CORETAX adalah provider utama/riil yang sudah di-seed** (`database/seeders/`, dipanggil dari `DatabaseSeeder.php`). Master data di bawah ini **sudah ada begitu `db:seed` selesai** — tidak perlu dibuat lagi. File ini murni referensi (kode, nama, saldo) supaya test case transaksional (file 01 dst) bisa langsung pakai data riil tanpa tebak-tebakan.

**Provider**: `CORETAX` (slug `coretax-R3fNUj`) — currency dasar IDR.
**Branch**: `Pusat` (slug `pusat-48PEzb`) — Tangerang (dekat UMN), satu-satunya branch aktif.

> ⚠️ Sebelum mulai testing apa pun, baca dulu temuan di [`TemuanTestCase/Accounting/CoretaxCompany/01-seeder-dan-master-data.id.md`](../../TemuanTestCase/Accounting/CoretaxCompany/01-seeder-dan-master-data.id.md) — ada duplikasi `accounting_periods` untuk Jan-Jun 2026 yang WAJIB dipahami sebelum pilih `accounting_period_id`.

## 1. Chart of Account Types (5, tree "Dagang")

| Code               | Name       | Normal Balance | Category  |
| ------------------ | ---------- | -------------- | --------- |
| `DAGANG-ASSET`     | Aset       | debit          | asset     |
| `DAGANG-LIABILITY` | Liabilitas | credit         | liability |
| `DAGANG-EQUITY`    | Ekuitas    | credit         | equity    |
| `DAGANG-REVENUE`   | Pendapatan | credit         | revenue   |
| `DAGANG-EXPENSE`   | Beban      | debit          | expense   |

## 2. Chart of Accounts (35 baris — 13 group/subgroup + 22 akun leaf)

Struktur 3 level: `1-000`/`2-000`/`3-000`/`4-000`/`5-000` (Group) → `GRPxx` (Subgroup) → kode 4-digit (Account/leaf). Saldo di bawah adalah **saldo tetap dari seeder** (opening & closing per akun, `accounting_period_id = null` — bukan hasil transaksi berjalan).

| Code   | Nama                                            | Grup            | Opening        | Closing        | Flag                          |
| ------ | ------------------------------------------------ | --------------- | --------------: | --------------: | ------------------------------ |
| `1101` | Kas dan Setara Kas                                | Kas, Bank & Piutang | 500.000.000  | 600.000.000    | `is_cash_account`             |
| `1102` | Kas Kecil                                         | Kas, Bank & Piutang | 10.000.000   | 10.000.000     | `is_cash_account`             |
| `1103` | Bank *(dibuat `PurchaseModuleCoaMappingSeeder`)*  | Kas, Bank & Piutang | —            | —              | —                              |
| `1121` | Piutang Usaha                                     | Kas, Bank & Piutang | 200.000.000  | 250.000.000    | —                               |
| `1410` | Persediaan Barang Dagang *(dibuat mapping seeder)*| Persediaan & Uang Muka | 500.000.000 | 600.000.000  | —                               |
| `1422` | Uang Muka                                         | Persediaan & Uang Muka | 50.000.000  | 30.000.000    | functionality `dp`             |
| `1424` | PPN Masukan *(dibuat mapping seeder)*             | Persediaan & Uang Muka | 0           | 20.000.000     | —                               |
| `1600` | Aset Tetap                                        | Aset Tetap        | 300.000.000  | 300.000.000    | —                               |
| `1601` | Akumulasi Penyusutan Aset Tetap                   | Aset Tetap        | -50.000.000  | -70.000.000    | kontra-aset                    |
| `2102` | Utang Usaha                                       | Liabilitas        | -150.000.000 | -200.000.000   | functionality `ap`             |
| `2105` | Utang atas Barang Diterima (GR/IR Clearing) *(mapping seeder)* | Liabilitas | 0    | -100.000.000   | —                               |
| `2190` | Utang Pajak                                       | Liabilitas        | 0            | -20.000.000    | —                               |
| `3101` | Modal Disetor                                     | Modal             | 500.000.000  | 500.000.000    | —                               |
| `3102` | Laba Ditahan                                      | Modal             | 100.000.000  | 150.000.000    | `is_retained_earnings_account` (WAJIB unik per branch — `FiscalYear::close()` butuh ini) |
| `4001` | Penjualan                                         | Pendapatan        | —            | —              | —                               |
| `4501` | Pendapatan Lain-lain                              | Pendapatan        | —            | —              | —                               |
| `5001` | Pembelian                                         | HPP               | 0            | 400.000.000    | functionality `purchase_expense` |
| `5002` | Retur Pembelian *(dibuat mapping seeder)*         | HPP               | —            | —              | —                               |
| `5008` | Persediaan - Awal                                 | HPP               | 100.000.000  | 130.000.000    | —                               |
| `5009` | Persediaan - Akhir                                | HPP               | —            | —              | —                               |
| `5501` | Beban Gaji                                        | Beban Operasional | —            | —              | —                               |
| `5502` | Beban Operasional Lainnya                         | Beban Operasional | —            | —              | —                               |

**Akun yang BELUM ADA** (perlu dibuat manual kalau test case butuh): akun kontra-pendapatan untuk Retur Penjualan, akun PPN Keluaran terpisah dari `2190` (lihat temuan `sales_configs`), akun `1423 Pajak Dibayar di Muka` (direferensikan komentar `TaxesSeeder` tapi tidak pernah benar-benar dibuat — lihat temuan #2).

**Mapping COA otomatis Purchasing** (`purchase_config_journals`, sudah terisi lengkap oleh `PurchaseModuleCoaMappingSeeder`): `inventory→1410`, `gr_ir→2105`, `ppn_masukan→1424`, `cash_bank→1103`, `return→5002`, `ap→2102` (reuse), `dp→1422` (reuse), `purchase_expense→5001` (reuse). Ini artinya **PO→GR→PI langsung bisa auto-post ke GL tanpa setup tambahan** — beda dengan Sales (lihat suite `sales-coretax/`).

## 3. Fiscal Year & Accounting Period

| Fiscal Year | Status              | Periode                                                                 |
| ----------- | -------------------- | ------------------------------------------------------------------------ |
| `FY2026`    | **Aktif**, belum closed | 12 bulanan (Januari-Desember 2026) — **⚠️ Jan-Jun ada duplikat, lihat temuan** |
| `FY2027`    | Tidak aktif, belum closed | 11 bulanan (Januari-November 2027, Desember tidak ada di data export) |

Semua `duration_type = monthly`. **Sebelum pilih `accounting_period_id` untuk test case apa pun, jalankan `accounting-periods/list` dulu dan pastikan pilih baris yang `is_closed` sesuai ekspektasi** — jangan asumsikan hanya ada 1 baris per bulan (lihat [temuan #1](../../TemuanTestCase/Accounting/CoretaxCompany/01-seeder-dan-master-data.id.md)).

## 4. Business Unit (5, hierarki 2 level)

| Code     | Nama              | Tipe    | Parent    |
| -------- | ------------------ | ------- | --------- |
| `BU-HO`  | Head Office         | cost    | — (root)  |
| `BU-RTL` | Divisi Retail       | profit  | — (root)  |
| `BU-IT`  | Dept IT             | cost    | BU-HO     |
| `BU-FIN` | Dept Finance        | cost    | BU-HO     |
| `BU-CBG` | Cabang Bandung      | profit  | BU-RTL    |

## 5. Cost Center (9, hierarki 2 level)

| Parent | Nama                     | Children                                                                 |
| ------ | ------------------------- | --------------------------------------------------------------------------- |
| `ADM`  | Administrasi & Umum        | `ADM-FIN` Keuangan & Akuntansi, `ADM-HR` HR & GA, `ADM-IT` IT & Sistem       |
| `OPS`  | Operasional                | `OPS-WH` Gudang & Logistik, `OPS-PROD` Produksi                             |
| `SLM`  | Penjualan & Pemasaran       | `SLM-SLS` Sales Lapangan, `SLM-MKT` Marketing                                |

## 6. Bank Account (3)

| Nama                          | Bank            | No. Rekening    | Opening Balance | COA Terkait |
| ------------------------------ | ---------------- | ---------------- | ---------------: | ----------- |
| BCA - Rekening Operasional      | BCA               | 2110058823        | 50.000.000       | `1101`      |
| Mandiri - Rekening Giro         | Mandiri           | 1270009988776      | 25.000.000       | `1101`      |
| Kas Kecil (Petty Cash)          | Internal          | PETTY-CASH-01      | 2.000.000        | `1102`      |

Semua currency IDR.

## 7. Payment Method (4)

`CASH` (Tunai), `TRF-BCA` (Transfer Bank BCA), `QRIS`, `CASH-NEW` ("Transfer Bank", tanpa deskripsi — sisa dari seeder ganda, aman diabaikan).

## 8. General Journal Type (6)

`General Journal` (dipakai jurnal manual — default), `Adjustment Journal`, `Updated Purchase Journal`, `Updated Adjustment Journal`, `Purchase Journal` (auto-post PO/PI/Payment/Return Purchasing), `Sales Journal` (auto-post Sales, tapi lihat temuan `sales_configs` — belum ter-mapping COA-nya).

## 9. Price List (3, semua IDR)

`Daftar Harga Beli Default` (**id harus = 1**, dipakai `price_list_skus` hardcode dari `PurchasingMasterSeeder` — kalau seed ulang di DB yang tidak kosong, id ini bisa geser dan harga produk "menggantung"), `Daftar Harga Jual Retail`, `Daftar Harga Grosir`.

## 10. Warehouse (1)

`Gudang Cikarang` — satu-satunya warehouse. Semua stock SKU awal **0** (belum ada barang masuk) — bagus untuk test case GR karena before/after jelas.

## 11. Product Unit (12)

`pcs`, `Kilogram`, `Satu paket lengkap` (SET), `Sepasang` (PASANG), `Produk cair dalam botol` (BOTOL), `Berdasarkan volume` (LITER), `Mililiter` (ML), `TUBE`, `Lembar` (LBR), `Roll`, `Box`, `Karton` (KTN).

## 12. Product & SKU (17 produk, ~40 SKU)

Dua kategori besar: **Elektronik** (Laptop Gaming RTX, Laptop Office Slim, Laptop Bag, SSD NVMe M.2, RAM DDR4, Printer Inkjet Multifungsi) dan **Sparepart Motor** (Federal/Enduro Oli Mesin, Busi NGK, Kampas Rem AHM CBS, Filter Oli AHM, V-Belt CVT, Aki GS Astra, Rantai DID Japan, Gasket Set AHM) + **ATK** (Kertas HVS, Sabun Antiseptik). Contoh SKU siap pakai untuk test case:

| SKU Code           | Nama                        | Unit | Harga Beli (price_list_id=1) |
| -------------------- | ----------------------------- | ---- | ----------------------------: |
| `LAPTOP-RTX-3050`     | Laptop RTX 3050 16GB RAM       | pcs  | 8.500.000                     |
| `SSD-512G`            | SSD NVMe 512GB M.2             | pcs  | 480.000                       |
| `SP002`               | Federal Matic 0.8L 10W30       | BOTOL| 32.000                        |
| `BUSI-NGK-STD`        | Busi NGK CR6HSA Standard       | pcs  | 18.000                        |
| `KERTAS-HVS-A4`       | Kertas HVS A4 80gr 500lbr/rim  | LBR  | 45.000                        |

Harga di atas adalah **harga BELI** (price list default) — belum ada harga JUAL ter-set (price list "Retail"/"Grosir" ada headernya tapi `price_list_skus` untuk keduanya KOSONG, cuma default beli yang keisi). Test case Sales yang butuh harga jual per SKU **harus set manual dulu** lewat `client-master/price-lists/skus/*` atau kirim harga custom langsung di baris SO.

## 13. Contact — Supplier (6, untuk Purchasing)

| Nama                          | Credit Limit | Termin  | NPWP |
| ------------------------------- | ------------: | ------- | ---- |
| PT Sumber Makmur                 | 50.000.000    | 30 hari | Ada  |
| CV Berkah Jaya Abadi              | 30.000.000    | 14 hari | Ada  |
| PT Indo Tech Distribusi           | 100.000.000   | 45 hari | Ada  |
| UD Mitra Motor Parts              | 20.000.000    | 7 hari  | Ada  |
| PT Global Supply Indonesia        | 75.000.000    | 30 hari | Ada  |
| Toko Sparepart Agung              | 5.000.000     | 0 hari (COD) | Tidak ada — bagus untuk test case validasi non-PKP |

## 14. Contact — Customer (6, untuk Sales)

| Nama                              | Type     | Credit Limit | Termin  |
| ------------------------------------ | -------- | ------------: | ------- |
| PT Cahaya Abadi Sejahtera              | customer | 25.000.000    | 30 hari |
| CV Mitra Sentosa                       | customer | 15.000.000    | 14 hari |
| Toko Elektronik Jaya                   | customer | 5.000.000     | 0 hari (COD, NPWP kosong) |
| PT Nusantara Perkasa                   | customer | 60.000.000    | 45 hari |
| PT Anugerah Teknologi Mandiri          | **both** | 40.000.000    | 30 hari — bisa dipakai sebagai supplier MAUPUN customer |
| UD Sumber Rejeki                       | **both** | 10.000.000    | 7 hari  |

## 15. Discount (5, untuk Sales)

| Code           | Tipe       | Nilai | Min Order   | Status |
| ---------------- | ---------- | ----: | ------------ | ------ |
| `NEWCUST10`       | percentage | 10%   | 500.000       | Aktif |
| `GROSIR15`        | percentage | 15%   | 5.000.000     | Aktif |
| `MEMBER50K`       | fixed      | 50.000| 300.000 (maks 100x pakai) | Aktif |
| `EOY2026`         | fixed      | 100.000| 1.000.000 (valid Des 2026 saja) | Aktif tapi terjadwal |
| `LEBARAN2026`     | percentage | 20%   | 500.000       | **`is_active:false`** — siap pakai untuk test negatif "diskon nonaktif ditolak" |

## 16. Taxes (26 baris, import mentah lintas-vertical lama)

Yang relevan untuk test case dagang umum: `PPN` (11%, increase — PPN Keluaran), `PPN_MASUKAN` (11%, decrease), `PPH21` (5%, decrease), `PPH23` (2%, decrease). **Ada 2 tax bernama sama "PPN Masukan"** dengan `code` beda (`PPN_MASUKAN` 11% vs `PPN12` 12%) — cari by `code`, jangan by `name`. Sisanya (`PB1`, `SVC`, `BPJS_KES`, `PPN_PROP`, `BBN_KB`, dst) adalah sisa data vertical lain (restoran, kesehatan, properti, otomotif) — valid dipakai kalau relevan, tapi TIDAK dipakai suite ini.

⚠️ **Tidak ada satu pun akun COA yang ter-flag `is_tax=true`** untuk branch Pusat (lihat [temuan #2](../../TemuanTestCase/Accounting/CoretaxCompany/01-seeder-dan-master-data.id.md)) — fitur auto-deteksi pajak per baris jurnal dari flag COA TIDAK akan trigger untuk data CORETAX kecuali di-setup manual.

## 17. Depreciation Method (2)

`Garis Lurus (Straight Line)` (`calculation_type: straight_line`), `Saldo Menurun (Declining Balance)` (`calculation_type: declining_balance`, formula **double-declining**: `rate = 2/useful_life_months` — lihat catatan formula di suite `accounting-manufaktur-2/03-anggaran-kuartalan-dan-aset-tetap.id.md` kalau butuh contoh perhitungan).

## 18. Currency & Exchange Rate

Semua currency global (termasuk USD, EUR, dst) otomatis "dimiliki" branch Pusat (`currency_created_by_branch` di-backfill untuk SEMUA kombinasi branch×currency). **TAPI tidak ada satu pun `exchange_rates` row yang di-seed untuk branch Pusat** — jadi transaksi valas APAPUN (jurnal manual `foreign_debit`/`foreign_credit`, PO/SO multi-currency) akan ditolak `content.no_active_exchange_rate_found_for_this_currency` sampai rate dibuat + di-`activate()` manual lewat `client-master/exchange-rates/upsert` + `.../activate`. **Praktis: IDR-only untuk suite ini**, kecuali ada test case yang secara eksplisit ingin menguji skenario "belum ada rate" (justru jadi skenario negatif siap pakai tanpa setup apa pun).

## Ringkasan Prasyarat Sebelum Testing

- [ ] Login sebagai user CORETAX (`coretax@mail.com` / `coretaxmanagerr@mail.com` / `direkturcoretax@mail.com`), **pilih provider CORETAX secara eksplisit** (ada 2 provider di dropdown, lihat temuan #3)
- [ ] Jalankan `accounting-periods/list`, catat `id` per bulan yang mau dipakai (hati-hati duplikat Jan-Jun 2026)
- [ ] Modul Purchasing: siap pakai langsung (COA mapping sudah lengkap)
- [ ] Modul Sales: **WAJIB** `PUT sales/sales-configs/upsert` dulu sebelum test case integrasi ke Accounting — lihat [temuan Sales](../../TemuanTestCase/Sales/CoretaxCompany/01-sales-config-belum-diseed.id.md)
- [ ] Transaksi valas: tidak didukung sampai exchange rate dibuat manual — default-kan semua test case ke IDR
