---
title: (IT Consultant + Retail Elektronik) — 00. Profil Perusahaan & Master Data
category: accounting-nusatech
description: Skenario PT NUSATECH — perusahaan IT Consultant dengan sub-usaha retail toko elektronik. 1 branch, 3 Business Unit. Setup COA Types, COA, Business Unit, Fiscal Year, dan Saldo Awal.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

## Profil Perusahaan (Skenario)

**PT NUSATECH** — perusahaan konsultan IT (fiktif) dengan bisnis utama jasa konsultasi & implementasi IT: pengembangan software custom, network setup/infrastructure consulting, dan managed services (kontrak maintenance bulanan). 30 karyawan bekerja di kantor. Sebagai unit bisnis kedua, PT NUSATECH juga menjalankan **retail toko elektronik & komputer** (jual laptop, komponen PC, aksesoris, dan jasa servis ringan).

Sudah **PKP** (PPN 11%). Karena menerima pembayaran jasa konsultasi dari klien badan usaha, transaksi jasa konsultasi juga berpotensi kena **PPh 23** (dipotong oleh klien) — dicatat sebagai aset kredit pajak (uang muka pajak).

> **Revisi arsitektur (2026-08-21)**: skenario ini SEBELUMNYA dimodelkan sebagai 2 branch terpisah (Kantor Pusat + Toko Bandung). Diubah jadi **1 branch dengan 3 Business Unit**, karena `Business Unit` justru dimensi yang tepat untuk memisahkan profitabilitas divisi DI DALAM 1 badan usaha yang sama — sementara `Branch` di framework ini adalah unit isolasi penuh (COA, fiscal year, config jurnal semua branch-scoped keras, lihat [[project_centralized_accounting_mode_design]]) yang cocoknya dipakai kalau memang ada BADAN USAHA/LEGAL ENTITY terpisah, bukan sekadar divisi/toko di bawah 1 manajemen keuangan yang sama. Kasus PT NUSATECH — 1 PT, keuangan dikelola terpusat, cuma beda lini bisnis — persis kasus yang seharusnya pakai Business Unit, bukan Branch ganda.

**1 Branch, 3 Business Unit:**

- **Branch: PT NUSATECH** — 1 branch tunggal, menaungi seluruh operasional (jasa IT + retail).
- **BU-CONSULT** — Divisi Konsultasi & Proyek IT (30 karyawan inti).
- **BU-MANAGED** — Divisi Managed Services (kontrak maintenance bulanan).
- **BU-RETAIL** — Divisi Toko Elektronik (Bandung) — retail laptop/komponen PC/aksesoris + jasa servis ringan.

> Catatan: seperti provider fiktif lain di suite ini, PT NUSATECH **TIDAK ada di seeder** — semua master data di bawah dibuat manual lewat endpoint API/FE mengikuti langkah pada file ini. Beda dengan suite `*-coretax` yang datanya sudah ter-seed otomatis.

## 1. Branch (**Branches**)

| Kode/Nama   | Fungsi                                                  |
| ----------- | ------------------------------------------------------- |
| PT NUSATECH | Branch tunggal — jasa IT consulting + retail elektronik |

Dibuat via `client-master/branches/create` (atau di-set sejak awal onboarding tenant). Karena cuma 1 branch, tidak ada isu switch-context antar branch untuk testing suite ini — cukup pastikan user tester `active_branch`-nya branch ini.

## 2. Business Unit (**Business Units**)

Dipakai untuk memisahkan profitabilitas 3 lini bisnis DI DALAM branch yang sama (`business_units.branch_id` tetap wajib diisi = branch PT NUSATECH, tapi ketiganya share branch yang sama):

| Kode         | Nama                           | `default_unit_type` | Catatan                                             |
| ------------ | ------------------------------ | ------------------- | --------------------------------------------------- |
| `BU-CONSULT` | Divisi Konsultasi & Proyek IT  | `profit`            | Jasa konsultasi & pengembangan software custom      |
| `BU-MANAGED` | Divisi Managed Services        | `profit`            | Kontrak maintenance bulanan (recurring revenue)     |
| `BU-RETAIL`  | Divisi Toko Elektronik Bandung | `profit`            | Retail laptop/komponen PC/aksesoris + servis ringan |

Dibuat via `client-master/business-units/create`. Ketiganya sibling (tidak ada `parent_id` — flat, tidak perlu hierarki berjenjang untuk skenario ini).

> **Dimensi ini dipakai di**: `journals.business_unit_id`, `warehouses.business_unit_id`, `budgets.business_unit_id`, dan `chart_of_accounts.default_business_units_id` (default tag business unit per akun, lihat §3). **Batasan yang perlu diketahui**: endpoint laporan (`ReportController` — trial balance/income statement/balance sheet) SAAT INI **tidak** punya filter `business_unit_id` bawaan — breakdown P&L per divisi harus dilakukan manual (query/export lalu group by `business_unit_id` di jurnal), bukan lewat 1 klik laporan siap pakai. Cukup untuk tujuan testing (drill-down manual), tapi dicatat sebagai keterbatasan.

## 3. Chart of Accounts Types (**Chart of Accounts Types**)

Setup dulu SEBELUM bikin akun COA — tiap akun di §4 wajib refer ke salah satu tipe ini (`chart_of_accounts.type_id`). Dibuat via `client-master/chart-of-account-type/create` (atau clone dari template global `IT`/`Dagang`/`Umum` via endpoint `use-template`, lalu edit `report_group` yang perlu disesuaikan).

| #   | Kode         | Nama                     | `category`  | `normal_balance` | `cash_flow_section` | `report_group`   | Dipakai untuk akun (§4) |
| --- | ------------ | ------------------------ | ----------- | ---------------- | ------------------- | ---------------- | ----------------------- |
| 1   | `AST_LANCAR` | Aset Lancar              | `asset`     | `debit`          | `operating`         | Balance Sheet    | AST-01 s/d AST-07       |
| 2   | `AST_TETAP`  | Aset Tetap               | `asset`     | `debit`          | `investing`         | Balance Sheet    | AST-08, AST-09, AST-10  |
| 3   | `LIA_JP`     | Liabilitas Jangka Pendek | `liability` | `credit`         | `operating`         | Balance Sheet    | LIA-01 s/d LIA-04       |
| 4   | `EKUITAS`    | Ekuitas                  | `equity`    | `credit`         | `financing`         | Balance Sheet    | EKT-01, EKT-02          |
| 5   | `PENDAPATAN` | Pendapatan               | `revenue`   | `credit`         | `operating`         | Income Statement | PDT-01 s/d PDT-04       |
| 6   | `HPP`        | Harga Pokok Penjualan    | `expense`   | `debit`          | `operating`         | Income Statement | HPP-01                  |
| 7   | `BEBAN`      | Beban                    | `expense`   | `debit`          | `operating`         | Income Statement | BBN-01 s/d BBN-06       |

> Catatan LIA-04 (Pendapatan Diterima Dimuka) dan AST-10 (Akumulasi Penyusutan) — keduanya tetap ikut `normal_balance` tipe induknya (`credit` utk `LIA_JP`, `debit` utk `AST_TETAP`) walau secara bisnis "terasa" seperti kebalikannya; AST-10 kontra-aset justru SELALU dikredit sehingga bersaldo negatif terhadap saldo normal debit-nya — pola yang sama seperti di [`accounting-manufaktur-2`](../accounting-manufaktur-2/00-profil-perusahaan-dan-master-data.id.md#2-chart-of-account-type-chart-of-account-type).

## 4. Chart of Accounts (**Chart of Accounts**)

Dibuat SEKALI SAJA (tidak perlu duplikasi per branch lagi — beda dari revisi arsitektur sebelumnya). Kolom **BU Default** mengisi `default_business_units_id` — dipakai sebagai default tag business unit saat akun ini dipakai di jurnal (opsional, bisa di-override manual per baris jurnal).

| Kode   | Nama Akun                                             | Tipe (§3)    | BU Default   | Flag khusus                                                                                                                                   |
| ------ | ----------------------------------------------------- | ------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| AST-01 | Kas Kecil Kantor                                      | `AST_LANCAR` | —            | `is_cash_account: true`, `balance_required: true`                                                                                             |
| AST-02 | Bank BCA Operasional (Konsultasi & Managed Services)  | `AST_LANCAR` | —            | `is_cash_account: true`                                                                                                                       |
| AST-03 | Bank Mandiri Operasional (Toko Retail)                | `AST_LANCAR` | `BU-RETAIL`  | `is_cash_account: true`                                                                                                                       |
| AST-04 | Piutang Usaha                                         | `AST_LANCAR` | —            | `is_ar_control_account: true`, `balance_required: true`                                                                                       |
| AST-05 | Persediaan Barang Dagang Elektronik                   | `AST_LANCAR` | `BU-RETAIL`  | `balance_required: true` (dikendalikan Inventory, bukan input manual setelah go-live)                                                         |
| AST-06 | PPN Masukan                                           | `AST_LANCAR` | —            | `is_tax: true`, `tax_id: <PPN 11%>`                                                                                                           |
| AST-07 | Uang Muka PPh 23 Dibayar Dimuka                       | `AST_LANCAR` | —            | Kredit pajak — PPh 23 yang dipotong klien atas jasa kita                                                                                      |
| AST-08 | Peralatan IT Konsultan (Laptop/Server)                | `AST_TETAP`  | `BU-CONSULT` | —                                                                                                                                             |
| AST-09 | Peralatan Toko (Rak/Etalase)                          | `AST_TETAP`  | `BU-RETAIL`  | —                                                                                                                                             |
| AST-10 | Akumulasi Penyusutan Aset Tetap                       | `AST_TETAP`  | —            | Contra-asset                                                                                                                                  |
| LIA-01 | Utang Usaha                                           | `LIA_JP`     | —            | `is_ap_control_account: true`, `balance_required: true`                                                                                       |
| LIA-02 | PPN Keluaran                                          | `LIA_JP`     | —            | `is_tax: true`, `tax_id: <PPN 11%>`                                                                                                           |
| LIA-03 | Utang PPh 23 Dipotong (atas jasa vendor)              | `LIA_JP`     | —            | Kewajiban setor PPh 23 yang kita potong dari vendor jasa                                                                                      |
| LIA-04 | Pendapatan Diterima Dimuka (Kontrak Managed Service)  | `LIA_JP`     | `BU-MANAGED` | `balance_required: true`                                                                                                                      |
| EKT-01 | Modal Pemilik                                         | `EKUITAS`    | —            | `is_opening_balance_equity_account: true`                                                                                                     |
| EKT-02 | Laba Ditahan                                          | `EKUITAS`    | —            | `is_retained_earnings_account: true`                                                                                                          |
| PDT-01 | Pendapatan Jasa Konsultasi & Proyek IT                | `PENDAPATAN` | `BU-CONSULT` | —                                                                                                                                             |
| PDT-02 | Pendapatan Managed Services (Kontrak Bulanan)         | `PENDAPATAN` | `BU-MANAGED` | —                                                                                                                                             |
| PDT-03 | Pendapatan Penjualan Barang Elektronik (Toko)         | `PENDAPATAN` | `BU-RETAIL`  | —                                                                                                                                             |
| PDT-04 | Pendapatan Lain-lain (Selisih Opname)                 | `PENDAPATAN` | `BU-RETAIL`  | Ditambahkan untuk Inventory Journal — lihat §11. Menampung overage Stock Adjustment/Stock Transfer (barang lebih saat opname/terima transfer) |
| HPP-01 | Harga Pokok Penjualan Barang Elektronik               | `HPP`        | `BU-RETAIL`  | —                                                                                                                                             |
| BBN-01 | Beban Gaji Karyawan                                   | `BEBAN`      | —            | Alokasi campuran, tidak di-default ke 1 BU tertentu                                                                                           |
| BBN-02 | Beban Sewa Kantor & Toko                              | `BEBAN`      | —            | Idem                                                                                                                                          |
| BBN-03 | Beban Penyusutan Aset Tetap                           | `BEBAN`      | —            | —                                                                                                                                             |
| BBN-04 | Beban Software License & Cloud Tools (AWS/Azure/M365) | `BEBAN`      | `BU-CONSULT` | —                                                                                                                                             |
| BBN-05 | Beban Administrasi Bank                               | `BEBAN`      | —            | —                                                                                                                                             |
| BBN-06 | Beban Kerugian Persediaan                             | `BEBAN`      | `BU-RETAIL`  | Ditambahkan untuk Inventory Journal — lihat §11. Menampung shrinkage Stock Adjustment/Stock Transfer (barang rusak/hilang)                    |

## 5. Fiscal Year & Accounting Period (**Fiscal Years**, **Accounting Periods**)

| Item               | Detail                                                                           |
| ------------------ | -------------------------------------------------------------------------------- |
| Fiscal Year 2026   | `start_date:2026-01-01`, `end_date:2026-12-31`, 12 periode bulanan auto-generate |
| Periode aktif test | Agustus 2026 (`2026-08-01` s/d `2026-08-31`)                                     |

Cukup 1 kali setup (dulu perlu dipikirkan per branch, sekarang tidak relevan lagi karena 1 branch).

## 6. Warehouse (**Warehouses**) — untuk sisi Toko Retail

| Nama                | Type      | Business Unit | Branch      |
| ------------------- | --------- | ------------- | ----------- |
| Gudang Utama Retail | `central` | `BU-RETAIL`   | PT NUSATECH |

> Tidak perlu warehouse `type:store` terpisah untuk POS di sini — toko elektronik menjual lewat alur Sales biasa (Quotation → SO → Delivery → Invoice), bukan POS kasir walk-in seperti minimarket. Lihat detail di [`../sales-nusatech/`](../sales-nusatech/).

## 7. Currency

Pakai `IDR` sebagai currency utama (auto ter-seed per branch baru via `CurrencyTemplateService` — lihat [[project_currency_branch_template_seeding]]). Tidak ada transaksi multi-currency di skenario ini.

## 8. Kontak (**Contacts**)

| Nama                               | Tipe     | Payment Term | Catatan penggunaan                                                                              |
| ---------------------------------- | -------- | ------------ | ----------------------------------------------------------------------------------------------- |
| PT Solusi Niaga Digital            | customer | 30 hari      | Klien proyek software development (milestone-based) — BU-CONSULT                                |
| PT Sinergi Pangan Nasional         | customer | 14 hari      | Klien kontrak Managed Services bulanan (retainer) — BU-MANAGED                                  |
| PT Distributor Teknologi Nusantara | supplier | 30 hari      | Supplier software license (Microsoft/Antivirus) & hardware server/laptop konsultan — BU-CONSULT |
| PT Grosir Elektronik Jaya          | supplier | 30 hari      | Distributor laptop/komponen PC untuk stok Toko Retail — BU-RETAIL                               |
| CV Reseller Gadget Bandung         | customer | 14 hari      | Reseller yang beli unit dalam jumlah untuk dijual lagi — BU-RETAIL                              |

> `contacts` tidak punya kolom `business_unit_id` di skema — kolom "Catatan penggunaan" di atas murni penanda dokumentasi/testing, bukan field yang benar-benar diisi di form Contact.

## 9. Produk/SKU Retail (untuk BU-RETAIL — lihat detail di `inventory-nusatech/`)

### 9a. Product Category (**Product Categories**)

Setup dulu SEBELUM bikin produk — `products.category_id` refer ke sini. Dibuat via `client-master/product-categories/create`.

| Kode/Slug            | Nama                    |
| -------------------- | ----------------------- |
| `laptop`             | Laptop                  |
| `komponen-aksesoris` | Komponen & Aksesoris PC |

### 9b. Product Unit (**Product Units**)

`product_skus.unit_id` refer ke sini. Dibuat via `client-master/product-units/create`. Cukup 1 unit dasar untuk skenario ini (tidak ada konversi unit — `conversion_unit_id`/`conversion_qty` dibiarkan kosong).

| Nama | `abbreviation` |
| ---- | -------------- |
| Pcs  | `pcs`          |

### 9c. Product & Product SKU

Tiap baris = 1 `Product` (induk, refer ke Category §9a) + 1 `Product SKU` (refer ke Unit §9b) — untuk skenario ini rasio 1:1 (tidak ada varian per produk, mis. Laptop tidak dipecah per warna/RAM).

| SKU     | Nama Produk                       | Kategori (§9a)       | Unit (§9b) | Barcode       | `min_stock` | `max_stock` | `reorder_point` | `reorder_qty` |
| ------- | --------------------------------- | -------------------- | ---------- | ------------- | ----------: | ----------: | --------------: | ------------: |
| LPT-001 | Laptop ASUS Vivobook 14           | `laptop`             | Pcs        | 8991234500011 |           2 |          15 |               3 |             5 |
| KOM-001 | Keyboard Mechanical Logitech G213 | `komponen-aksesoris` | Pcs        | 8991234500028 |           5 |          50 |              10 |            20 |
| KOM-002 | SSD NVMe 512GB Samsung            | `komponen-aksesoris` | Pcs        | 8991234500035 |           5 |          50 |              10 |            20 |

Dibuat via `client-master/products/create` (produk induk) lalu `client-master/product-skus/create` (SKU).

### 9d. Harga Jual — Price List (**Price Lists**, **Price List SKUs**)

Harga jual BUKAN kolom langsung di `product_skus` — disimpan lewat 1 Price List default (`price_lists` + `price_list_skus.price`), dibuat via `client-master/price-lists/create` lalu `client-master/price-list-skus/create`. Tidak ada qty-tiering/diskon bertingkat untuk skenario ini (`min_qty:1` semua, `is_active:true`).

| Price List       | SKU     | `price` (Harga Jual) |
| ---------------- | ------- | -------------------: |
| Retail Umum 2026 | LPT-001 |         Rp 7.800.000 |
| Retail Umum 2026 | KOM-001 |           Rp 650.000 |
| Retail Umum 2026 | KOM-002 |           Rp 750.000 |

### 9e. Harga Beli — Vendor Price (**Contact Product SKU Prices**)

Harga beli (avg) juga bukan field di `product_skus` — dicatat sebagai harga vendor per supplier via `client-master/contact-product-sku-prices/create` (`vendor_price`), terhubung ke supplier §8 **PT Grosir Elektronik Jaya**. Angka ini yang jadi acuan saldo awal persediaan di §10 dan penerimaan barang (Purchase Receipt) di `purchasing-nusatech/`.

| Supplier (§8)             | SKU     | `vendor_price` (Harga Beli avg) |
| ------------------------- | ------- | ------------------------------: |
| PT Grosir Elektronik Jaya | LPT-001 |                    Rp 6.500.000 |
| PT Grosir Elektronik Jaya | KOM-001 |                      Rp 450.000 |
| PT Grosir Elektronik Jaya | KOM-002 |                      Rp 550.000 |

## 10. Saldo Awal Perusahaan (**Chart of Accounts Balances**, **Bank Accounts**)

Karena sekarang 1 branch, saldo awal cukup **1 kali input** per akun (tidak ada lagi duplikasi per branch seperti revisi sebelumnya).

| Akun                                          |                                                       Saldo Awal | BU (§4)      | Jalur                                                                                                        |
| --------------------------------------------- | ---------------------------------------------------------------: | ------------ | ------------------------------------------------------------------------------------------------------------ |
| AST-01 Kas Kecil Kantor                       |                                                        8.000.000 | —            | `chart-of-accounts-balances`                                                                                 |
| AST-02 Bank BCA Operasional                   |                                                      300.000.000 | —            | `finance/bank-accounts`                                                                                      |
| AST-03 Bank Mandiri Operasional (Toko Retail) |                                                       60.000.000 | `BU-RETAIL`  | `finance/bank-accounts`                                                                                      |
| AST-04 Piutang Usaha                          |                                                       45.000.000 | —            | `chart-of-accounts-balances`                                                                                 |
| AST-05 Persediaan Barang Dagang Elektronik    |                            32.500.000 (5 unit Laptop @6.500.000) | `BU-RETAIL`  | `chart-of-accounts-balances`, HARUS konsisten dengan stok awal Inventory §2 file `inventory-nusatech/01-...` |
| LIA-01 Utang Usaha                            | 32.500.000 (20.000.000 + 12.500.000, gabungan Konsultasi & Toko) | —            | `chart-of-accounts-balances`                                                                                 |
| LIA-04 Pendapatan Diterima Dimuka             |                                                       30.000.000 | `BU-MANAGED` | `chart-of-accounts-balances`                                                                                 |

Total Aset = 8.000.000 + 300.000.000 + 60.000.000 + 45.000.000 + 32.500.000 = **445.500.000**
Total Liabilitas = 32.500.000 + 30.000.000 = **62.500.000**
→ Modal Pemilik (EKT-01) otomatis bersaldo kredit **383.000.000**

## 11. Inventory Journal — Chart of Accounts Mapping (**inventory/config**)

Sejak Inventory Journal (auto-posting jurnal Stock Adjustment & Stock Transfer) ditambahkan, `inventory_config_journals` branch ini WAJIB dimapping dulu lewat halaman `inventory/config` sebelum posting jurnal bisa jalan — kalau kosong, jurnalnya di-skip (fail-soft, stok tetap jalan, cuma sisi akuntansi diam). Lihat `docs/inventory-auto-replenishment-plan.id.md` bagian 2 untuk desain lengkapnya.

| `functionality`           | Akun (§4)                                    | Catatan NUSATECH                                                                                                                                                                                                                                                                                      |
| ------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `inventory`               | AST-05 Persediaan Barang Dagang Elektronik   | Sama dengan akun Persediaan yang sudah ada — TIDAK perlu akun baru                                                                                                                                                                                                                                    |
| `inventory_loss`          | BBN-06 Beban Kerugian Persediaan             | Akun baru (§4) — dipakai saat Stock Adjustment shrinkage / Stock Transfer shortage                                                                                                                                                                                                                    |
| `other_income_adjustment` | PDT-04 Pendapatan Lain-lain (Selisih Opname) | Akun baru (§4) — dipakai saat Stock Adjustment overage / Stock Transfer overage                                                                                                                                                                                                                       |
| `transit_clearing`        | — (tidak dimapping)                          | **Tidak relevan** untuk NUSATECH — cuma 1 warehouse (`type:central`), tidak pernah ada Stock Transfer antar-gudang di skenario ini. Boleh dibiarkan kosong; kalau suatu saat nambah warehouse `type:store`, baru wajib dimapping (lihat suite `accounting-pos-retail` sebagai contoh multi-warehouse) |

> `auto_draft_purchase_request_on_reorder` / `auto_draft_stock_transfer_on_reorder` (toggle di halaman yang sama) sengaja **dibiarkan OFF** untuk suite ini — SKU §9c belum di-set `min_stock`/`max_stock`/`reorder_point`/`reorder_qty`, jadi auto-replenishment tidak relevan diuji di sini kecuali skenario itu ditambahkan terpisah.

## Ringkasan Sebelum Lanjut

- [ ] 1 branch dibuat (PT NUSATECH)
- [ ] 3 Business Unit dibuat (BU-CONSULT, BU-MANAGED, BU-RETAIL)
- [ ] 7 COA Types dibuat (§3) — SEBELUM bikin akun COA
- [ ] COA 27 akun dibuat, masing-masing refer ke tipe §3, sebagian di-tag `default_business_units_id` sesuai §4
- [ ] Fiscal Year 2026 + 12 periode ter-generate
- [ ] Warehouse Gudang Utama Retail dibuat, tag `business_unit_id = BU-RETAIL`
- [ ] 5 kontak dibuat (2 customer jasa, 2 supplier, 1 customer/reseller retail)
- [ ] 2 Product Category dibuat (§9a), 1 Product Unit `Pcs` dibuat (§9b) — SEBELUM bikin produk
- [ ] 3 Product + Product SKU retail dibuat (§9c), masing-masing refer ke Category & Unit
- [ ] 1 Price List `Retail Umum 2026` dibuat + 3 `price_list_skus` (§9d) — harga jual
- [ ] 3 `contact_product_sku_prices` dibuat, terhubung ke PT Grosir Elektronik Jaya (§9e) — harga beli
- [ ] Saldo awal ter-input SEKALI (tidak perlu duplikasi lagi), total debit=kredit balance
- [ ] Inventory Journal COA mapping (§11) diisi: `inventory`→AST-05, `inventory_loss`→BBN-06, `other_income_adjustment`→PDT-04 (`transit_clearing` dibiarkan kosong)

## Referensi Silang

- [`../purchasing-nusatech/`](../purchasing-nusatech/) — procurement software/hardware konsultan & stok elektronik toko
- [`../sales-nusatech/`](../sales-nusatech/) — kontrak jasa konsultasi & penjualan retail
- [`../inventory-nusatech/`](../inventory-nusatech/) — stok barang elektronik toko
- [`../hrm-nusatech/`](../hrm-nusatech/) — attendance/payroll/leave/komisi 30 karyawan + staff toko
- [[project_currency_branch_template_seeding]], [[project_scale_and_big_todos]], [[project_centralized_accounting_mode_design]]
