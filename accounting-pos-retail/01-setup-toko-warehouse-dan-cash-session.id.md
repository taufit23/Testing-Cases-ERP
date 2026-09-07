---
title: — 01. Setup Toko (Warehouse) & Cash Session
category: Accounting + POS
description: Warehouse pusat (type central) + 2 warehouse toko (type store, terikat Business Unit), transfer stok pusat→toko, dan siklus buka/tutup Cash Session per toko sebagai prasyarat wajib sebelum transaksi POS bisa dibuat.
visibility: internal
---

# 01. Setup Toko (Warehouse) & Cash Session

> Mengasumsikan master data [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) sudah ada.
>
> **Sebab-akibat penting (dari migrasi `2026_08_13_..._add_type_and_business_unit_id_to_warehouses_table`):** kolom `warehouses.type` (enum `central`/`store`, default `central`) dan `warehouses.business_unit_id` (nullable) baru ditambahkan — **Cash Session HANYA BISA dibuka terhadap warehouse `type = store`**, ditolak dengan pesan `content.pos_cash_sessions_can_only_open_against_a_store_warehouse` kalau dicoba ke warehouse `central`. Warehouse lama (dibuat sebelum migrasi ini) default `central`, jadi warehouse toko HARUS dibuat/diedit eksplisit jadi `store` dulu.

## 1. Warehouse Pusat & Warehouse Toko

| Nama Warehouse | Type | Business Unit | Fungsi |
| --- | --- | --- | --- |
| Gudang Pusat | `central` | — (kosong) | Titik masuk stok awal (§7 file 00), TIDAK bisa dipakai buka Cash Session |
| Toko Cempaka Putih | `store` | BU-CP | Tempat Cash Session & transaksi POS toko 1 |
| Toko Kelapa Dua | `store` | BU-KD | Tempat Cash Session & transaksi POS toko 2 |

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif — Gudang Pusat | **Warehouses** → **+ Create** → Name "Gudang Pusat", Type "Central" (default), Business Unit kosongkan → Save | Warehouse `type:central` tercatat |
| Positif — Toko Cempaka Putih | Create → Name "Toko Cempaka Putih", Type **"Store"**, Business Unit `<BU-CP>` → Save | Warehouse `type:store`, `business_unit_id` terisi |
| Positif — Toko Kelapa Dua | Create → Name "Toko Kelapa Dua", Type **"Store"**, Business Unit `<BU-KD>` → Save | Warehouse `type:store`, `business_unit_id` terisi |
| Negatif | Buka Cash Session langsung ke "Gudang Pusat" (§3 di bawah) sebelum baca peringatan ini | Ditolak — `content.pos_cash_sessions_can_only_open_against_a_store_warehouse` |
| Netralisasi | Hapus warehouse test HANYA kalau tidak ada stok/Cash Session yang mereferensikannya | |

## 2. Produk & Stok Awal di Gudang Pusat, lalu Transfer ke Toko

**Sebab-akibat:** dokumentasi resmi menyatakan **tidak ada jalur direct-receiving ke warehouse `type:store`** — stok toko HARUS masuk lewat `stock_transfers` (draft → ship → receive) dari Gudang Pusat. Karena tidak berlangganan Purchasing, stok awal di Gudang Pusat sendiri diisi manual via **Stock Adjustment** (bukan Goods Receipt).

Produk contoh (buat minimal 3 SKU sembako):

| SKU | Nama Produk | Harga Jual | Qty Awal di Gudang Pusat |
| --- | --- | --- | --- |
| SMB-001 | Beras 5kg | Rp 65.000 | 100 |
| SMB-002 | Minyak Goreng 1L | Rp 18.000 | 200 |
| SMB-003 | Indomie Goreng (renceng isi 5) | Rp 13.500 | 150 |

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif — buat produk | **Product Catalog** → create 3 SKU di atas, harga sesuai tabel | 3 produk muncul di list |
| Positif — stok awal Gudang Pusat | **Inventory → Stock Adjustment** → pilih Warehouse "Gudang Pusat", tambahkan qty sesuai tabel (alasan "Stok awal pengadaan dari distributor") → Save | `sku_stocks` Gudang Pusat terisi sesuai qty |
| Positif — transfer ke Toko Cempaka Putih | **Inventory → Stock Transfer** → From "Gudang Pusat" → To "Toko Cempaka Putih" → qty: 50 Beras, 100 Minyak Goreng, 80 Indomie → Save (draft) → **Ship** → **Receive** di sisi tujuan | Stok Gudang Pusat berkurang, stok Toko Cempaka Putih bertambah sesuai qty dikirim |
| Positif — transfer ke Toko Kelapa Dua | Stock Transfer serupa → To "Toko Kelapa Dua" → qty: 50 Beras, 100 Minyak Goreng, 70 Indomie → Ship → Receive | Stok Toko Kelapa Dua terisi, Gudang Pusat tersisa 0 semua SKU |
| Negatif | Coba Stock Transfer dengan qty melebihi stok tersedia di Gudang Pusat | Ditolak validasi qty > stok tersedia |
| Netralisasi | Reverse stock adjustment/transfer test HANYA sebelum ada transaksi POS yang memakai stok itu | |

## 3. Buka Cash Session per Toko

**Halaman:** `pos/cash-sessions` (`open`). **Wajib** sebelum transaksi POS apapun bisa dibuat di toko tsb — `pos-transactions/create` mensyaratkan `cash_session_id` yang `status:open`.

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif — buka sesi Cempaka Putih | **Cash Sessions** → **+ Open Session** → Warehouse "Toko Cempaka Putih", Opening Balance `500.000` (modal kasir awal shift) → **Open** | Session baru `status:open`, `session_number` ter-generate, `warehouse_id` terisi |
| Positif — buka sesi Kelapa Dua | Open Session serupa → Warehouse "Toko Kelapa Dua", Opening Balance `500.000` | Session kedua `status:open`, independen dari sesi toko pertama |
| Negatif — warehouse central | Open Session → Warehouse "Gudang Pusat" | Ditolak `content.pos_cash_sessions_can_only_open_against_a_store_warehouse` |
| Negatif — warehouse branch lain | Open Session dengan `warehouse_id` milik branch lain (kalau ada multi-branch di environment testing) | Ditolak — warehouse harus milik branch aktif |
| Negatif — sesi ganda | Coba Open Session KEDUA untuk warehouse "Toko Cempaka Putih" padahal sesi pertama masih `open` | Verifikasi behavior aktual: harus ditolak (1 warehouse cuma boleh 1 sesi aktif), catat sebagai temuan kalau ternyata sistem membolehkan 2 sesi `open` bersamaan di warehouse yang sama |
| Netralisasi | **Close** kedua sesi ini di akhir file 02 (§ terakhir) sebelum lanjut ke file 03 | |

## 4. Tutup Cash Session (dikerjakan SETELAH transaksi POS di file 02 selesai)

**Halaman:** `pos/cash-sessions` (`close`). Bagian ini didokumentasikan di sini supaya alurnya utuh 1 file, tapi EKSEKUSI-nya nanti di akhir file 02 setelah ada transaksi tunai untuk dihitung.

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif — tutup pas | **Close Session** pada sesi Cempaka Putih → Closing Balance (hitung fisik) diisi PERSIS sama dengan `expected_balance` yang ditampilkan sistem (opening + total tunai masuk dari transaksi POS tunai selama sesi) → **Close** | `status:closed`, selisih (`closing_balance` − `expected_balance`) = 0, TIDAK ada jurnal Beban Selisih Kas |
| Positif — tutup dengan selisih kurang (shortage) | Pada sesi Kelapa Dua, isi Closing Balance **lebih kecil** dari `expected_balance` (mis. selisih Rp 15.000, kasir kurang setor) → Close | `status:closed`, sistem catat selisih negatif → verifikasi apakah otomatis posting jurnal `<Beban Selisih Kas>` Debit / `<Kas Hasil Penjualan POS>` Credit, atau ini murni pencatatan tanpa jurnal (dokumentasikan mana yang benar sebagai temuan) |
| Negatif | Coba **Close** sesi yang sudah `status:closed` | Ditolak/idempoten — cek behavior aktual |
| Negatif | Coba buat transaksi POS baru dengan `cash_session_id` yang sudah `closed` | Ditolak |
| Netralisasi | Tidak perlu di-reverse — Cash Session yang closed adalah state akhir wajar (siklus harian toko sungguhan) | |
