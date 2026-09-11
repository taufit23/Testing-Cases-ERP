---
title: Ranahku — Alur Transaksi Step by Step
description: Skenario transaksi Ranahku setelah master data (file 01) selesai — kanvasing & penjualan langsung sewa aplikasi, kasir toko & rumah makan (POS + Sales/SO), pembelian restock, sampai payroll SDM. Satu cabang, periode uji September 2026.
---

# Ranahku — Alur Transaksi Step by Step

> Prasyarat: **seluruh Tahap 1–12** di [`01-urutan-input-master-data.id.md`](01-urutan-input-master-data.id.md)
> sudah selesai & Daftar Periksa Cepat-nya tercentang semua. Data pelanggan/pemasok/produk/karyawan
> yang dipakai di sini mengacu ke file itu.
>
> Tanggal transaksi: **1–30 September 2026**. Semua nominal contoh, boleh disesuaikan asal proporsional.

---

## Ringkasan Tahap Transaksi

| #   | Tahap                            | Modul Backend              | Prasyarat                    |
| --- | -------------------------------- | -------------------------- | ---------------------------- |
| A   | Kanvasing → Sewa Aplikasi        | `canvassing/*` → `sales/*` | 01 Tahap 5, 8, 9             |
| B   | Penjualan Langsung Sewa Aplikasi | `sales/*`                  | 01 Tahap 5, 8                |
| C   | Toko Retail (POS + SO)           | `pos/*`, `sales/*`         | 01 Tahap 4, 5, 6, 11.2, 11.3 |
| D   | Rumah Makan (kasir meja + SO)    | `restaurant/*`, `sales/*`  | 01 Tahap 4, 7, 11.4          |
| E   | Pembelian Restock                | `purchasing/*`             | 01 Tahap 5, 6, 11.6          |
| F   | Payroll SDM                      | `hrm/*`                    | 01 Tahap 9, 11.7             |

> **Catatan struktural penting** (dari riset kode langsung, bukan asumsi): modul **Rental**
> (`rental/*`) di backend adalah sewa **aset fisik** bertarif harian (`rate_per_day` × durasi),
> **BUKAN** engine langganan SaaS bulanan/tahunan. Karena itu "Paket Dasar/Usaha/Pro" di Tahap 8
> file 01 sudah benar dimodelkan sebagai **Products jasa non-stok**, dijual lewat modul **Sales**
> biasa (Quotation → SO → Invoice) — bukan lewat `rental/*`. Jangan salah pakai modul saat testing.

---

## TAHAP A — Kanvasing → Sewa Aplikasi

**Petugas:** Andi Saputra, Rizal Kurnia, Sari Melati (Petugas Kanvasing). **Target:** Toko Bangunan
Sumber Rejeki (Paket Usaha), Bengkel Motor Laju Jaya (Paket Dasar) — keduanya sudah jadi Contact
di 01 Tahap 5.2, dengan catatan "Sewa aplikasi via kanvasing".

> Alur nyata di kode: `SalesVisit` **tidak** punya status approval — murni enum
> `planned → in_progress → completed` (sisi `skipped`/`cancelled`). Dokumen transaksi baru lahir
> saat `canvassing/orders/quick-order` dipanggil (biasanya saat `check-out`), dengan `intent=sales`
> → langsung membuat **Sales Order** `draft`, `source=canvassing`, tertaut ke `sales_visit_id`.
> SO ini lalu mengikuti alur approval SO **yang sama persis** dengan SO non-kanvasing.

### A.1 Kunjungan Kanvasing — Toko Bangunan Sumber Rejeki (Andi Saputra)

| Skenario | Detail                                                                                                     | Hasil                                                         |
| -------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Positif  | `visits/create` — kunjungan terjadwal ke Toko Bangunan Sumber Rejeki, tgl 2 Sep 2026                       | Status `planned`                                              |
| Positif  | `visits/check-in` di lokasi toko                                                                           | Status `in_progress`, jarak geofence tercatat                 |
| Positif  | `orders/catalog` — lihat katalog paket sewa yang bisa ditawarkan                                           | Daftar Products jasa sewa (PKT-DASAR…PKT-DAMPING)             |
| Positif  | `orders/quick-order`, `intent=sales`, item **PKT-USAHA** qty 1 (350.000) + **PKT-DAMPING** qty 1 (500.000) | SO baru `draft`, `source=canvassing`, total 850.000 + PPN 11% |
| Positif  | `visits/check-out`, `outcome=order_placed`                                                                 | Visit `completed`, `outcome_document` tertaut ke SO di atas   |
| Negatif  | `check-out` sebelum `check-in`                                                                             | Ditolak — urutan status                                       |
| Negatif  | `quick-order` dengan qty 0 / SKU sewa yang tidak ada di katalog                                            | 422                                                           |

### A.2 Kunjungan Kanvasing — Bengkel Motor Laju Jaya (Rizal Kurnia)

| Skenario    | Detail                                                                                            | Hasil                                                |
| ----------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Positif     | `visits/create` → `check-in` → `orders/quick-order` `intent=sales`, **PKT-DASAR** qty 1 (150.000) | SO `draft`, `source=canvassing`, total 150.000 + PPN |
| Positif     | `visits/check-out`, `outcome=order_placed`                                                        | Visit `completed`                                    |
| Netralisasi | `visits/skip` dipakai untuk 1 kunjungan latihan (mis. toko tutup)                                 | Butuh `skip_reason`, status `skipped`                |

### A.3 Kunjungan Tanpa Order (latihan negatif/edge case)

| Skenario | Detail                                                                                        | Hasil                                                                 |
| -------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Positif  | `visits/check-out` dengan `outcome=no_order` atau `store_closed`                              | Visit `completed`, TIDAK ada `outcome_document`                       |
| Positif  | `customers/quick-register` — daftar outlet baru ditemukan di lapangan (belum ada di Contacts) | Contact baru langsung **ACTIVE** tanpa approval (per keputusan owner) |
| Negatif  | `visits/create` dengan `contact_id` yang belum terdaftar sama sekali                          | 422 — visit harus mengacu Contact yang sudah ada                      |

### A.4 Lanjutkan SO Kanvasing sampai Terbayar

Dari titik ini, SO hasil kanvasing (A.1, A.2) diproses **persis seperti SO biasa** — office/admin
yang lanjutkan, bukan petugas lapangan.

| Skenario  | Detail                                                                                                                                                                                        | Hasil                                                                       |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Positif   | `sales-orders/customer-credit-status` untuk Toko Bangunan Sumber Rejeki sebelum approve                                                                                                       | Preview status kredit                                                       |
| Positif   | `sales-orders/submit` → `approve` (kedua SO A.1 & A.2)                                                                                                                                        | Status `approved`                                                           |
| Positif   | `sales-invoices/create` dari masing-masing SO → `submit` → `approve` → `export-to-journal`                                                                                                    | Jurnal AR (1-120) / Pendapatan Sewa (4-101/4-102)                           |
| Positif   | Toko Bangunan Sumber Rejeki: `sales-payment-bills/create` **tunai** (sesuai termin "Tunai lalu bulanan" — bulan pertama tunai) → `submit` → `approve` → `mark-received` → `export-to-journal` | Kas/Bank bertambah, AR lunas                                                |
| Positif   | Bengkel Motor Laju Jaya: `sales-payment-bills/create` (termin bulanan) jatuh tempo akhir September                                                                                            | Payment bill `submitted`/`pending`, belum dibayar (uji piutang belum lunas) |
| ⚠️ Catatan | Sama seperti pola nusatech: **tidak ada auto-generate SO/Invoice bulanan** — tagihan bulan Oktober untuk kedua pelanggan ini harus dibuat manual (Quotation/SO/Invoice baru) bulan depan.     | Jangan uji "auto-renewal" yang tidak ada                                    |

---

## TAHAP B — Penjualan Langsung Sewa Aplikasi (non-kanvasing)

**Petugas:** Nadia Puspita, Bagas Wicaksono (Eksekutif Penjualan), dibantu Intan Permata (Admin
Kontrak & Sewa) untuk dokumen. Alur murni `sales/quotations` → `sales/sales-orders`.

### B.1 Apotek Sehat Bersama — Paket Pro Tahunan

| Skenario | Detail                                                                                           | Hasil                                                         |
| -------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Positif  | `quotations/create` — 1 baris **PKT-TAHUN-PRO** qty 1, harga 7.500.000                           | 201, subtotal 7.500.000 + PPN 11% = 8.325.000                 |
| Positif  | `submit` → `resend-to-customer` → `customer-accept`                                              | Status `accepted`                                             |
| Positif  | `convert-to-so`                                                                                  | SO `draft`, item sama persis dengan quotation                 |
| Positif  | `sales-orders/customer-credit-status` → `submit` → `approve`                                     | Status `approved` (termin 14 hari)                            |
| Positif  | `sales-invoices/create` → `submit` → `approve` → `export-to-journal`                             | AR 1-120 naik, Pendapatan Sewa 4-101 naik, PPN Keluaran 2-120 |
| Positif  | `sales-payment-bills/create` H+14 → `submit` → `approve` → `mark-received` → `export-to-journal` | AR lunas dalam termin                                         |
| Negatif  | `customer-accept` pada Quotation yang belum `sent`                                               | 422/403 — urutan status                                       |

### B.2 Distributor Minuman Segar Nusantara — Badan Usaha, Potong PPh 23

| Skenario    | Detail                                                                                                                            | Hasil                                                                                                                                                                                                                                      |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif     | `quotations/create` — **PKT-TAHUN-PRO** qty 1, harga 7.500.000, baris kena `tax_id` **PPH23** (`effect: decrease`, 2%) selain PPN | Subtotal 7.500.000, PPN 11% = +825.000, PPh 23 2% = **-150.000** (dipotong pelanggan), total tagih 8.175.000                                                                                                                               |
| Positif     | `submit` → `resend-to-customer` → `customer-accept` → `convert-to-so` → `submit` → `approve`                                      | SO `approved`, termin 30 hari                                                                                                                                                                                                              |
| Positif     | `sales-invoices/create` → `submit` → `approve` → `export-to-journal`                                                              | Jurnal: AR (net setelah potongan) di 1-120, PPh 23 dipotong tercermin sebagai pengurang piutang — cocokkan ke akun **1-170 Uang Muka PPh 23** kalau dicatat perusahaan sebagai kredit pajak dibayar dimuka, BUKAN dicatat ganda di penjual |
| Netralisasi | Simpan bukti potong PPh 23 dari pelanggan sebagai lampiran invoice (Attachment engine, bukan storage ad-hoc)                      | —                                                                                                                                                                                                                                          |

### B.3 CV Katering Nikmat Rasa — Sewa Jangka Pendek, Bayar di Muka

| Skenario | Detail                                                                                                                  | Hasil                                                                                                                                                                                         |
| -------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `quotations/create` — **PKT-SEWA-HARI** qty 5 hari (min. 3 hari), harga 100.000/hari = 500.000                          | Subtotal 500.000 + PPN 11% = 555.000                                                                                                                                                          |
| Positif  | `submit` → `customer-accept` → `convert-to-so` → `submit` → `approve`                                                   | SO `approved`, termin "Bayar di muka"                                                                                                                                                         |
| Negatif  | `quick-order`/`create` dengan qty hari < 3                                                                              | Harus ditolak di validasi FE/BE sesuai catatan paket (min. 3 hari)*(catat di layer mana validasi ini benar-benar ada — kalau belum ada di BE, ini gap untuk didaftarkan, bukan asumsi lolos)* |
| Positif  | `sales-invoices/create` **sebelum** masa sewa mulai (karena bayar di muka) → `submit` → `approve` → `export-to-journal` | Diinvoice duluan, beda urutan dengan B.1/B.2 (invoice setelah approve, sebelum masa berjalan)                                                                                                 |
| Positif  | `sales-payment-bills/create` langsung (tunai/transfer) → `submit` → `approve` → `mark-received`                         | Lunas di muka sebelum layanan berjalan                                                                                                                                                        |

### Ringkasan Sebelum Lanjut

- [ ] Tahap A: 2 SO kanvasing `approved` (850.000+PPN, 150.000+PPN), 1 sudah lunas tunai, 1 masih piutang bulanan
- [ ] Tahap B: 3 SO penjualan langsung `approved` — Pro tahunan (8.325.000), Pro tahunan potong PPh23 (8.175.000 net), sewa harian 5 hari (555.000)
- [ ] Semua Invoice ter-`export-to-journal`, cek akun 1-120 (AR), 4-101/4-102 (Pendapatan), 2-120 (PPN Keluaran), 1-170 (kredit pajak PPh23)

---

## TAHAP C — Toko Retail

### C.1 Kasir Toko (POS) — Transaksi Tunai Harian

**Petugas:** Fitri Handayani (Kasir Toko), diawasi Dodi Herlambang (Supervisor Toko).

| Skenario | Detail                                                                                                 | Hasil                                                               |
| -------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Positif  | `pos/cash-sessions/open` — buka shift kasir toko, modal awal 1.000.000 dari 1-102 Kas Toko Retail      | Sesi `open`                                                         |
| Positif  | `pos/pos-transactions/create` — Pembeli Umum, 2× BRG-001 (Beras 5kg) + 1× BRG-004 (Galon), bayar tunai | Stok BRG-001/BRG-004 turun, kas bertambah, PPN 11% dari 4-201/2-120 |
| Positif  | `pos-transactions/hold` lalu `resume` — pelanggan lupa bawa uang, transaksi ditahan dulu               | Transaksi `held` lalu balik `pending` saat di-resume                |
| Negatif  | `create` transaksi dengan qty BRG melebihi stok tersedia                                               | Ditolak, pesan stok tidak cukup                                     |
| Positif  | `pos-transactions/void` untuk 1 transaksi salah input                                                  | Status `voided`, stok & kas dikembalikan                            |
| Positif  | `pos-transactions/refund` untuk 1 transaksi yang sudah selesai (barang dikembalikan customer)          | Refund tercatat, stok BRG kembali masuk                             |
| Positif  | `cash-sessions/warehouse-stock-check` sebelum tutup shift                                              | Preview stok gudang toko real-time                                  |
| Positif  | `cash-sessions/close` — hitung fisik kas vs sistem                                                     | `cash_over_short` tercermin ke akun 6-190/6-111 sesuai Tahap 11.3   |
| Positif  | `cash-sessions/report` untuk shift yang baru ditutup                                                   | Ringkasan penjualan, PPN, HPP                                       |

### C.2 Penjualan Kredit B2B (Sales module) — Toko Bangunan Sumber Rejeki Beli Partai Besar

> Reuse Contact yang sama dengan Tahap A (satu Contact boleh transaksi lintas unit usaha — tidak
> ada larangan sistem). Skenario ini menguji jalur **Quotation → SO → Delivery → Invoice** untuk
> barang fisik, beda dari alur POS yang langsung tunai tanpa Delivery.

| Skenario | Detail                                                                                              | Hasil                                                                                                                                       |
| -------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `quotations/create` — 20× BRG-007 (Buku Tulis) + 10× BRG-008 (Pulpen), harga sesuai Harga Toko 2026 | Subtotal = 20×48.000 + 10×30.000 = 960.000+300.000 = 1.260.000 + PPN 11%                                                                    |
| Positif  | `submit` → `customer-accept` → `convert-to-so` → `submit` → `approve`                               | SO `approved`, termin "Tunai lalu bulanan"                                                                                                  |
| Positif  | `sales-deliveries/create` dari SO → `submit` → `approve`                                            | Stok BRG-007/BRG-008 di Gudang Toko Retail berkurang sesuai qty dikirim                                                                     |
| Positif  | `sales-invoices/create` dari Delivery → `submit` → `approve` → `export-to-journal`                  | AR naik, HPP (5-201) & Persediaan (1-130) tercatat, PPN Keluaran (2-120)                                                                    |
| Positif  | `sales-payment-bills/create` → `submit` → `approve` → `mark-received` → `export-to-journal`         | AR lunas                                                                                                                                    |
| Negatif  | `sales-invoices/create` langsung dari SO **tanpa** Delivery lebih dulu (untuk barang fisik)         | Cek apakah backend memang mewajibkan Delivery dulu — kalau lolos tanpa Delivery, catat sebagai temuan (gap validasi), bukan asumsikan benar |

### C.3 Retur Penjualan Toko

| Skenario | Detail                                                              | Hasil                                                           |
| -------- | ------------------------------------------------------------------- | --------------------------------------------------------------- |
| Positif  | `sales-returns/create` — 5× BRG-008 dari transaksi C.2 dikembalikan | Stok BRG-008 masuk lagi, AR/Pendapatan dikoreksi (kontra 4-201) |

---

## TAHAP D — Rumah Makan

### D.1 Alur Kasir Meja (Restaurant module)

**Petugas:** Agus Setiawan (Pelayan), Novi Ramadhani (Kasir Rumah Makan), Trisno Aji/Sumarni (Juru Masak).

| Skenario | Detail                                                                                           | Hasil                                                                   |
| -------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| Positif  | `restaurant/tables/list` — pilih meja kosong                                                     | Status meja `available`                                                 |
| Positif  | `restaurant/orders/open` — buka pesanan di meja terpilih                                         | Order `open`, tertaut meja                                              |
| Positif  | `orders/add-item` — 2× MNU-001 (Nasi Goreng), 1× MNU-006 (Es Teh Manis), 1× MNU-002 (Ayam Bakar) | Item masuk order, status per-item `pending`                             |
| Positif  | `kds/tickets` (via `restaurant/kds`) — dapur terima tiket dari `send-to-kitchen`                 | Ticket muncul di KDS, Juru Masak update status masak                    |
| Positif  | `orders/transfer-table` — tamu pindah meja sebelum bill ditutup                                  | Order tertaut ke meja baru                                              |
| Positif  | `orders/split-bill` — tamu bayar terpisah (misal 2 kelompok pesanan)                             | Bill terbagi sesuai item                                                |
| Positif  | `bills/close-bill` — bayar tunai via Kas Rumah Makan (1-103) + PB1 10%                           | Pendapatan 4-301, PB1 ke 2-121 (BUKAN PPN), HPP 5-301, Persediaan 1-131 |
| Negatif  | `orders/add-item` pada order yang sudah `closed`                                                 | Ditolak — urutan status                                                 |
| Positif  | `bookings/create` untuk reservasi rombongan malam ini → `confirm` → `mark-seated`                | Booking lifecycle, meja teralokasi                                      |
| Negatif  | `bookings/pay-deposit` dengan nominal melebihi total booking                                     | 422/ditolak                                                             |

### D.2 Pesanan Katering Partai Besar (Sales module — Quotation→SO)

> Untuk menguji jalur non-kasir di RESTO. Karena Tahap 5 tidak punya Contact khusus "pelanggan
> katering RESTO", gunakan **Pembeli Umum** atau **CV Katering Nikmat Rasa** (sudah ada, walau
> awalnya untuk konteks sewa aplikasi) — satu Contact bisa lintas transaksi.

| Skenario | Detail                                                                                                   | Hasil                                                                                                                                                                                                                                                                   |
| -------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `quotations/create` — 50× MNU-005 (Paket Nasi Ayam Komplit) untuk acara kantor, harga 38.000             | Subtotal 1.900.000, PB1 10% (bukan PPN — pastikan `tax_id` yang dipasang ke baris ini PB1, cek Tahap 11.4 `restaurant_tax_output` vs jalur Sales biasa pakai PPN Keluaran — **catat sebagai temuan** kalau modul Sales generik cuma bisa PPN, tidak bisa PB1 per baris) | Perlu verifikasi tax_id yang tersedia untuk dipilih di Sales Quotation |
| Positif  | `submit` → `customer-accept` → `convert-to-so` → `submit` → `approve`                                    | SO `approved`                                                                                                                                                                                                                                                           |
| Positif  | `sales-invoices/create` → `submit` → `approve` → `export-to-journal` → `sales-payment-bills` lunas tunai | Pendapatan Rumah Makan tercatat via jalur Sales (bukan kasir meja)                                                                                                                                                                                                      |

---

## TAHAP E — Pembelian Restock

### E.1 Restock Toko — CV Grosir Sembako Makmur (termin 21 hari)

| Skenario | Detail                                                                                                      | Hasil                                                                                             |
| -------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Positif  | `purchase-requests/create` — 100× BRG-002 (Minyak Goreng), 200× BRG-003 (Gula) → `submit` → `approve`       | PR `approved`                                                                                     |
| Positif  | `purchase-orders/create` dari PR (atau langsung) → `submit` → `approve`                                     | PO `approved`, total = 100×32.000+200×14.000 = 3.200.000+2.800.000 = 6.000.000                    |
| Positif  | `purchase-receipts/create` — barang diterima lengkap sesuai PO → `submit` → `approve` → `export-to-journal` | Stok BRG-002/BRG-003 di Gudang Toko Retail bertambah, Persediaan 1-130 naik, GR/IR clearing beres |
| Negatif  | `purchase-receipts/create` dengan qty terima **melebihi** sisa qty PO                                       | Ditolak — validasi over-receipt ([[project_gr_over_receipt_validation]])                          |
| Positif  | `purchase-invoices/create` dari GR → `submit` → `approve` → `export-to-journal`                             | Utang Usaha 2-101 naik                                                                            |
| Positif  | `purchase-payment-bills/create` H+21 → `submit` → `approve` → `mark-paid` → `export-to-journal`             | Utang lunas via Bank Operasional 1-110                                                            |

### E.2 Restock Dapur — UD Pasar Segar (tunai, cepat)

| Skenario | Detail                                                                                                                                                          | Hasil                                   |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Positif  | `purchase-orders/create` langsung (tanpa PR, karena tunai & mendadak) — sayur/ayam/telur, total 2.000.000 → `submit` → `approve`                                | PO `approved`                           |
| Positif  | `purchase-receipts/create` hari yang sama → `submit` → `approve` → `export-to-journal`                                                                          | Persediaan Bahan Rumah Makan 1-131 naik |
| Positif  | `purchase-invoices/create` → `submit` → `approve` → `export-to-journal` → `purchase-payment-bills` lunas tunai hari itu juga (Kas Kecil Kantor 1-101 atau Bank) | Utang langsung lunas, tidak menginap    |

### E.3 Retur Pembelian

| Skenario | Detail                                                              | Hasil                                                   |
| -------- | ------------------------------------------------------------------- | ------------------------------------------------------- |
| Positif  | `purchase-returns/create` — sebagian Gula Pasir rusak saat diterima | Stok BRG-003 dikurangi lagi, Utang/Persediaan dikoreksi |

---

## TAHAP F — Payroll SDM (Periode September 2026)

### F.1 Absensi & Cuti (sampel, tidak perlu 25 karyawan penuh — cukup representasi tiap departemen)

| Skenario | Detail                                                                                                                                                | Hasil                                                        |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Positif  | `attendances/create` — beberapa entri harian untuk Fitri Handayani (Kasir Toko), Novi Ramadhani (Kasir Rumah Makan), Andi Saputra (Petugas Kanvasing) | Rekap kehadiran September                                    |
| Positif  | `leave-requests/create` — Wati Suryani (Pramuniaga) cuti 2 hari → `approve`                                                                           | Status `approved`, potong saldo cuti (`leave-balances`)      |
| Negatif  | `leave-requests/approve` pada pengajuan yang belum ada saldo cuti cukup                                                                               | Ditolak/butuh override eksplisit                             |
| Positif  | `attendance-adjustments/create` — koreksi jam masuk Trisno Aji (lupa absen) → approval flow                                                           | Attendance ter-update otomatis via observer setelah approved |

### F.2 Generate & Proses Payroll

| Skenario | Detail                                                                                   | Hasil                                                                                                                        |
| -------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `payroll-periods/generate` untuk September 2026 (one-click)                              | Periode terbentuk, `payroll-items/browse` menampilkan 25 baris karyawan                                                      |
| Positif  | `payroll-periods/process` — hitung gaji pokok, PPh 21 5% (`content` pajak Tahap 3), BPJS | Item payroll terisi per karyawan, potongan sesuai `payroll-tax-reference` (PTKP/TER)                                         |
| Positif  | `payroll-periods/approve`                                                                | Status `approved`, siap dibayar                                                                                              |
| Positif  | `payroll-periods/mark-paid` → cek `payroll-journal-configuration` (Tahap 11.7)           | Jurnal: Beban Gaji 6-101 naik, Utang PPh21 2-122 & Utang BPJS 2-131 terbentuk, Bank 1-110 berkurang saat benar-benar dibayar |
| Negatif  | `payroll-periods/generate` dipanggil 2× untuk bulan yang sama                            | Harus ditolak/idempotent — jangan sampai dobel periode                                                                       |

### Ringkasan Sebelum Lanjut

- [ ] Tahap C: minimal 1 sesi kasir toko lengkap (open→transaksi→close), 1 SO kredit B2B lunas, 1 retur
- [ ] Tahap D: minimal 1 siklus meja lengkap (open→add-item→kitchen→close-bill), 1 SO katering via Sales
- [ ] Tahap E: 1 siklus PO→GR→PI→PPB termin (Grosir Sembako), 1 siklus tunai same-day (Pasar Segar), 1 retur
- [ ] Tahap F: absensi sampel + 1 cuti approved, payroll September `mark-paid`, cek jurnal PPh21/BPJS

---

## Referensi Silang

- [`00-profil-perusahaan-dan-master-data.id.md`](00-profil-perusahaan-dan-master-data.id.md)
- [`01-urutan-input-master-data.id.md`](01-urutan-input-master-data.id.md)
- [[project_sales_canvassing_module]], [[project_gr_over_receipt_validation]], [[project_pi_payment_requires_approval_gate]], [[project_payment_bill_termin_ordering]]
- [`../../erpApiServices/routes/canvassing.php`](../../erpApiServices/routes/canvassing.php), [`../../erpApiServices/routes/sales.php`](../../erpApiServices/routes/sales.php), [`../../erpApiServices/routes/pos.php`](../../erpApiServices/routes/pos.php), [`../../erpApiServices/routes/restaurant.php`](../../erpApiServices/routes/restaurant.php), [`../../erpApiServices/routes/purchasing.php`](../../erpApiServices/routes/purchasing.php), [`../../erpApiServices/routes/hrm.php`](../../erpApiServices/routes/hrm.php)
