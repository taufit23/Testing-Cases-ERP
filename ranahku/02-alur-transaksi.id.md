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

> **Status Tahap A: Selesai sebagian (2026-09-14), terhambat 2 kendala aplikasi.** Rincian
> lengkap ada di tiga catatan berikut, semuanya di
> `erpApiServices/docs/TemuanTestCase/Canvassing/Ranahku/`:
> `01-quick-order-katalog-selalu-gagal-dimuat.id.md`,
> `02-banyak-teks-belum-diterjemahkan.id.md`, dan
> `03-tidak-ada-cara-buat-kunjungan-satuan-untuk-tanggal-tertentu.id.md`.
>
> Ringkasnya:
> - Tidak ada tombol langsung untuk menjadwalkan satu kunjungan ke pelanggan tertentu pada
>   tanggal tertentu. Jalan yang tersedia adalah lewat menu **Sales Routes**: buat rute untuk
>   petugas kanvasing (Andi Saputra / Rizal Kurnia), tambahkan pelanggan sebagai tujuan
>   kunjungan, tentukan hari aktifnya dalam seminggu, lalu tombol "Generate Planned Visits"
>   membuat data kunjungannya. Karena tanggal 2 September 2026 di spesifikasi sudah lewat dari
>   tanggal berjalan sistem (14 September 2026), kunjungan yang berhasil dibuat memakai tanggal
>   berjalan (14 September 2026, hari Senin), bukan tanggal 2 September.
> - Kunjungan berhasil dibuat dan diproses sampai **Check In** (status berubah ke "sedang
>   berlangsung") untuk kedua petugas, dengan lancar.
> - **Kendala utama**: tombol untuk membuat pesanan saat kunjungan berlangsung ("Order")
>   selalu gagal memuat daftar produk (pesan error "kolom ini melebihi batas maksimum"),
>   untuk pesanan jenis Sales maupun Rental. Karena itu, pesanan PKT-USAHA + PKT-DAMPING
>   (Toko Bangunan Sumber Rejeki) dan PKT-DASAR (Bengkel Motor Laju Jaya) **tidak berhasil
>   dibuat**. Sebagai gantinya, kedua kunjungan tetap diselesaikan sampai **Check Out** dengan
>   hasil "Tidak Ada Pesanan", supaya alur status kunjungan (terjadwal → berlangsung → selesai)
>   tetap terverifikasi berjalan normal.
> - Karena tidak ada pesanan yang terbentuk dari kunjungan kanvasing, langkah A.4 (lanjutkan
>   Sales Order sampai lunas) tidak bisa dijalankan. Pengujian alur "pesan → Sales Order →
>   Invoice → Pembayaran" untuk paket sewa aplikasi tetap dilanjutkan lewat Tahap B (jalur
>   penjualan langsung, tidak melalui Canvassing), yang tidak terkena dampak kendala di atas.
> - Ditemukan juga beberapa label tampilan yang belum diterjemahkan (tampil sebagai kode
>   program, bukan kalimat biasa) di halaman Sales Routes dan Canvassing Field — tidak
>   mengganggu jalannya fitur, sudah dicatat detailnya di file terpisah.

> **Status Tahap B: Selesai dengan penyesuaian (2026-09-14), 3 skenario berjalan sampai
> Sales Order & Invoice, tapi ketiganya sama-sama terhambat oleh 3 bug aplikasi.**
>
> **B.1 — Apotek Sehat Bersama:** Quotation `QUO/2026/09/0001` (8.325.000) dibuat → disetujui
> pelanggan → dikonversi ke SO `SO/2026/09/0001` (otomatis `Confirmed`) → dibuat Invoice
> `INV-S/2026/09/0001` → `Submit` (otomatis `Unpaid`). Total sesuai spesifikasi.
>
> **B.2 — Distributor Minuman Segar Nusantara:** Quotation `QUO/2026/09/0002` dibuat dengan 2
> pajak (PPN 11% + PPh 23 Dipotong 2%) → disetujui pelanggan → dikonversi ke SO
> `SO/2026/09/0002` → Invoice `INV-S/2026/09/0002`. **Perhatian:** total yang dihasilkan sistem
> adalah **8.475.000**, bukan 8.175.000 seperti perhitungan manual yang benar (7.500.000 +
> 825.000 PPN − 150.000 PPh 23) — sistem menjumlahkan kedua pajak alih-alih mengurangi PPh 23.
> Pengujian tetap dilanjutkan pakai nilai sistem supaya alur bisa selesai diuji. Detail lengkap
> di temuan terpisah.
>
> **B.3 — CV Katering Nikmat Rasa:** Percobaan pertama sengaja pakai quantity 2 hari (di bawah
> minimal 3 hari sesuai catatan paket) untuk menguji validasi negatif — **tidak ada penolakan
> sama sekali**, baik di tampilan maupun di server, quotation tetap tersimpan. Ini dicatat
> sebagai temuan gap validasi tersendiri. Quotation yang sama kemudian diedit ke quantity yang
> benar (5 hari, sesuai spesifikasi) → disimpan ulang (total 500.000) → `Submit` → dicatat
> "Customer Accepted" dengan Agreed Due Date 19 September 2026 → dikonversi ke SO
> `SO/2026/09/0003` (otomatis `Confirmed`) → dibuat Invoice `INV-S/2026/09/0003` sebelum masa
> sewa dimulai (sesuai catatan "bayar di muka") → `Submit` (otomatis `Unpaid`).
>
> **Kendala yang menghambat ketiga skenario di tahap ini:**
> 1. Tombol **Export To Journal** gagal untuk `INV-S/2026/09/0001` dengan pesan "Sales Journal
>    Type Is Not Seeded For This Branch", walau data master "Sales Journal" sudah ada — dicurigai
>    masalah data seeding di backend, bukan sesuatu yang bisa diperbaiki dari tampilan. Karena
>    kemungkinan besar bug ini sistemik (bukan spesifik satu invoice), Export To Journal tidak
>    dicoba ulang satu-satu untuk `INV-S/2026/09/0002` dan `INV-S/2026/09/0003` — dianggap akan
>    mengalami hal yang sama sampai perbaikan backend dilakukan.
> 2. Fitur **Create Payment** untuk invoice penjualan tidak berfungsi sama sekali di kedua mode
>    yang tersedia: mode "Single Payment" selalu gagal dengan pesan "This Field Is Required"
>    walau semua kolom (termasuk tanggal) tampil terisi benar di layar, dan mode "Multi Payment"
>    gagal total karena endpoint backend-nya belum terdaftar. Bug ini dikonfirmasi berulang di
>    tiga invoice berbeda (`INV-S/2026/09/0001`, dan diuji ulang di `INV-S/2026/09/0003`),
>    membuktikan ini masalah sistemik pada fitur, bukan kasus khusus satu dokumen. Akibatnya,
>    ketiga invoice di Tahap B ini **tetap berstatus "Unpaid"** — tidak ada satu pun yang bisa
>    dilunasi lewat tampilan aplikasi saat ini.
> 3. Paket sewa harian "Sewa Jangka Pendek" tidak punya validasi minimal durasi (3 hari) sama
>    sekali di sistem — baik di tampilan maupun di server — jadi siapa pun bisa memesan untuk
>    durasi 1 hari saja tanpa dicegah.
>
> Detail lengkap ketiga temuan ada di
> `erpApiServices/docs/TemuanTestCase/Sales/Ranahku/`:
> `01-export-to-journal-gagal-sales-journal-type-tidak-diseed.id.md`,
> `02-create-payment-sales-invoice-gagal-total.id.md`,
> `03-pph23-dipotong-malah-menambah-total-bukan-mengurangi.id.md`, dan
> `04-paket-sewa-harian-tidak-ada-validasi-minimal-durasi.id.md`.

### Ringkasan Sebelum Lanjut

- [x] Tahap A: 2 kunjungan kanvasing berhasil dibuat & diproses (check-in, check-out hasil "Tidak Ada Pesanan") — pembuatan Sales Order terhambat bug "Quick Order", lihat catatan di atas
- [x] Tahap B: 3 Quotation → SO → Invoice selesai dibuat — Pro tahunan (8.325.000, sesuai spesifikasi), Pro tahunan potong PPh23 (8.475.000, salah hitung karena bug PPh23 nambah bukan kurang — seharusnya 8.175.000), sewa harian 5 hari (500.000 tanpa pajak). Semua invoice tetap "Unpaid" (fitur Create Payment gagal total) dan tidak ter-export ke jurnal (bug seeding Sales Journal Type). Ditemukan juga gap validasi minimal durasi sewa harian. Lihat catatan di atas untuk rincian.
- [ ] Semua Invoice ter-`export-to-journal`, cek akun 1-120 (AR), 4-101/4-102 (Pendapatan), 2-120 (PPN Keluaran), 1-170 (kredit pajak PPh23) — **diblokir bug**, tidak bisa diverifikasi sampai bug seeding jurnal diperbaiki

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

> **Status Tahap C: Selesai dengan catatan (2026-09-14), semua skenario utama berhasil dijalankan
> sampai akhir, dengan 1 prasyarat tersembunyi dan beberapa bug ditemukan sepanjang jalan.**
>
> **Prasyarat tambahan yang ditemukan sebelum Tahap C bisa mulai:** seluruh saldo awal stok
> (Tahap 10) ternyata hanya masuk ke Gudang Utama, sedangkan Gudang Toko Retail kosong sama
> sekali. Sistem sudah benar menolak pembukaan sesi kasir dari warehouse kosong (tombol "Open
> Session" otomatis nonaktif), tapi ini bukan bagian dari alur setup resmi yang terdokumentasi.
> Ditambahkan langkah manual: Stock Transfer `TRF/2026/09/0001` (Gudang Utama → Gudang Toko
> Retail, 5 SKU) sebelum melanjutkan. Detail di
> `erpApiServices/docs/TemuanTestCase/Inventory/Ranahku/01-warehouse-baru-perlu-transfer-stok-manual-dari-gudang-utama.id.md`.
>
> **C.1 — Kasir Toko (POS):** Sesi kasir `CS/2026/09/14/001` dibuka di Gudang Toko Retail dengan
> modal awal Rp 1.000.000. Transaksi `POS/2026/09/14/0001` (2× Beras + 1× Galon, Rp 166.000)
> berhasil ditahan lalu dilanjutkan (Hold → Resume), dibayar tunai, lalu sebagian barangnya
> diretur lewat fitur Refund POS (bukan Sales Return) — stok kembali masuk dengan benar. Transaksi
> `POS/2026/09/14/0002` sengaja dipakai untuk menguji batas stok (klik beli Air Mineral Galon
> melebihi stok tersedia) — sistem **berhasil mencegah** dengan pesan stok tidak cukup dan
> otomatis membatasi jumlah maksimal, lalu transaksi ini dibatalkan lewat Void — stok & kas
> kembali seperti semula. Sesi ditutup dengan hitungan fisik kas Rp 1.080.000 vs sistem
> Rp 1.094.000 (selisih kurang Rp 14.000), tercatat otomatis sebagai jurnal selisih kas. Catatan
> baik: seluruh transaksi kasir (penjualan, refund, void, selisih kas) **otomatis tercatat ke
> jurnal akuntansi dengan benar dan langsung**, tidak seperti tombol "Export To Journal" di modul
> Sales yang bermasalah — bagian POS ini terbukti berfungsi baik secara independen.
>
> **C.2 — Penjualan Kredit B2B (Toko Bangunan Sumber Rejeki, Buku Tulis & Pulpen):** Quotation
> `QUO/2026/09/0004` (Rp 1.398.600 termasuk PPN) dibuat → disetujui pelanggan → dikonversi ke SO
> `SO/2026/09/0004` (otomatis `Confirmed`). Skenario negatif sengaja dicoba: klik langsung "Create
> Sales Invoice" dari SO **tanpa** membuat Sales Delivery lebih dulu — ternyata **berhasil
> tersimpan tanpa penolakan apa pun** (`INV-S/2026/09/0004`), padahal barang belum tercatat
> terkirim. Diverifikasi lewat Stock History bahwa stok BRG-007/BRG-008 memang benar-benar belum
> berkurang. Ditemukan juga bug kecil: Due Date invoice otomatis terisi 14 Oktober 2026, padahal
> halaman yang sama menyebutkan batas tanggal SO cuma sampai 28 September 2026. Kedua temuan ini
> dicatat detail di
> `erpApiServices/docs/TemuanTestCase/Sales/Ranahku/05-invoice-barang-fisik-bisa-dibuat-tanpa-delivery-lebih-dulu.id.md`.
>
> **C.3 — Retur Penjualan Toko:** Dokumen retur `RTN/2026/09/0001` dibuat untuk 5 Pulpen (BRG-008)
> dari `INV-S/2026/09/0004`, lalu di-Submit sampai status `Approved`. Meski halaman retur sendiri
> menjanjikan "Returned Items Will Be Added Back To Stock Once Approved", **stok BRG-008 di
> Stock History tidak bertambah sama sekali** setelah retur disetujui — dikonfirmasi ini murni
> fitur yang belum berfungsi, bukan karena sistem sengaja menghindari dobel-hitung akibat temuan
> C.2 di atas. Tombol "Export To Journal" di halaman retur juga gagal dengan pesan error yang
> sama seperti bug di modul Sales Invoice ("Sales Journal Type Is Not Seeded For This Branch").
> Detail lengkap di
> `erpApiServices/docs/TemuanTestCase/Sales/Ranahku/06-retur-penjualan-tidak-mengembalikan-stok-meski-status-approved.id.md`.

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

> **Status Tahap D: Selesai dengan catatan (2026-09-15), kedua skenario utama (kasir meja dan
> pesanan katering via Sales) berhasil dijalankan sampai akhir, dengan beberapa prasyarat data
> yang harus disiapkan manual lebih dulu dan beberapa bug ditemukan sepanjang jalan.**
>
> **Prasyarat tambahan yang ditemukan sebelum Tahap D bisa mulai:** menu Restaurant > Areas,
> Tables, dan Kitchen Stations semuanya masih kosong (belum pernah diisi di tahap master data
> sebelumnya), jadi dibuat dulu 1 Area ("Area Utama"), 1 Kitchen Station ("Dapur Utama"), dan 2
> Meja ("M01", "M02") sebelum pengujian kasir meja bisa dimulai. Ini gap yang sama jenisnya
> dengan gap Stock Transfer yang ditemukan sebelum Tahap C — lihat catatan Task terpisah soal
> menambahkan langkah ini ke test case master data.
>
> **D.1 — Kasir Meja (Restaurant):** setelah data pendukung siap, order `ORD/2026/09/0001`
> dibuka di Meja M01 dan diisi 4 baris item (Nasi Goreng, Es Teh Manis, Ayam Bakar). Ditemukan
> bug besar: semua item tersimpan dengan harga satuan Rp 0 walau harga di master Menu sudah
> benar (lihat temuan detail di dokumen TemuanTestCase Restaurant). Karena Total tagihan ikut
> jadi Rp 0, tombol Pay Bill sempat tidak bisa diklik sama sekali (validasi tampilan menolak
> nominal bayar Rp 0) — diuji tetap bisa lanjut dengan memasukkan nominal bayar Rp 1 secara
> manual, hanya untuk memverifikasi mekanisme Split Bill dan Close Bill berjalan benar secara
> alur, BUKAN untuk memverifikasi angka uangnya (yang memang belum bisa dipercaya sampai bug
> harga ini diperbaiki). Fitur **Transfer Table** dan **Split Bill** sendiri (ditemukan lewat
> menu titik tiga di halaman pesanan) berfungsi baik secara alur, begitu juga **Void Order**
> yang diuji terpisah di order kedua. Menu daftar Meja dan daftar Pesanan juga ditemukan selalu
> tampil "No data" walau datanya benar-benar ada di server (bug tampilan, lihat temuan
> terpisah) — pengujian tetap dilanjutkan dengan membuka halaman detail secara langsung. Fitur
> **Booking (reservasi meja)** ditemukan gagal total dibuat karena data yang dikirim halaman
> tidak cocok sama sekali dengan yang diminta server — bagian ini sepenuhnya terblokir dan
> belum bisa diuji sampai bug ini diperbaiki (lihat temuan detail).
>
> **D.2 — Pesanan Katering via Sales:** sempat terhambat karena produk menu yang mau dipakai
> (Paket Nasi Ayam Komplit) belum diberi kanal penjualan (Sales Channel) sama sekali di master
> data, jadi ditambahkan dulu secara manual sebelum quotation bisa disimpan (lihat temuan
> detail). Setelah itu, jalur Quotation → Customer Accepted → Sales Order → Invoice berhasil
> dilalui sampai selesai dengan angka yang benar (subtotal Rp 1.900.000, pajak PB1 10% Rp
> 190.000, total Rp 2.090.000) — ini juga membuktikan bahwa modul Sales generik **BISA** memakai
> pajak PB1 per baris, bukan cuma PPN seperti yang dikhawatirkan di catatan spesifikasi test
> case. Langkah **Export To Journal** dan **Create Payment** masing-masing gagal dengan pesan
> error yang sudah pernah ditemukan sebelumnya di modul Sales lain ("Sales Journal Type Is Not
> Seeded For This Branch" dan "This Field Is Required") — jadi bukan bug baru, hanya reproduksi
> ulang bug lama di dokumen yang berbeda. Invoice tetap berstatus "Unpaid" karena pembayaran
> tidak berhasil disimpan.
>
> **Temuan tambahan yang tidak menghalangi jalannya pengujian** (dicatat terpisah): sebuah bug
> penting ditemukan bahwa fitur cari/filter di halaman daftar Sales Invoice, Sales Order, Sales
> Quotation, dan Purchase Order selalu gagal dengan error server — ini kemungkinan besar
> penyebab tersembunyi di balik beberapa halaman daftar yang terlihat "kosong" di modul lain.
> Selain itu ada beberapa bug tampilan kecil (judul halaman belum diisi dengan benar, tanggal
> yang tampil "Invalid Date", kode status yang tampil mentah di riwayat) — semuanya tidak
> menghalangi proses, hanya kurang rapi.

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

> **Status Tahap E: Selesai dengan catatan (2026-09-15), ketiga sub-tahap (restock termin,
> restock tunai cepat, retur pembelian) berhasil dijalankan sampai akhir, dengan beberapa
> bug dan satu gap data ditemukan sepanjang jalan.**
>
> **E.1 — Restock Toko (CV Grosir Sembako Makmur, termin 21 hari):** alur lengkap PR → PO → GR
> → PI → PPB berhasil dijalankan sampai selesai dengan angka yang benar (Total Rp 6.000.000,
> 100×Minyak Goreng + 200×Gula Pasir). PR dan PO otomatis disetujui begitu di-submit. Uji
> negatif over-receipt (mencoba terima 999 padahal sisa cuma 40 di skenario lain) berhasil
> ditolak tampilan sebelum sempat disimpan — validasinya bekerja dengan baik. Purchase Payment
> Bill (pembayaran H+21) berhasil dibuat, disetujui, ditandai lunas, sampai PO berstatus
> "Paid" — **berbeda dari Sales**, fitur Create Payment di Purchasing ini ternyata berfungsi
> normal (lihat catatan pembaruan di temuan bug pembayaran Sales). Export To Journal gagal
> dengan pesan "Purchase Journal Type Is Not Seeded For This Branch" — reproduksi bug seeding
> jurnal yang sama seperti di Sales, kali ini untuk tipe jurnal Pembelian.
>
> **E.2 — Restock Dapur (UD Pasar Segar, tunai cepat):** ditemukan gap data — produk bahan
> baku dapur segar (sayur, ayam, telur) yang diminta skenario ternyata belum pernah dibuat di
> master data Products sama sekali. Pengujian tetap dilanjutkan memakai produk pengganti yang
> sudah ada (Beras Premium, Rp 2.000.000) hanya untuk menguji mekanisme alur cepat tunai —
> bukan untuk memverifikasi kesesuaian jenis barang. Uji negatif over-receipt (qty 999 vs sisa
> 40) berhasil ditolak dengan benar. Alur PO → GR → PI → Pembayaran tunai berhasil selesai
> hari yang sama, invoice langsung lunas.
>
> **E.3 — Retur Pembelian:** ditemukan bug — halaman Create Purchase Return otomatis
> menampilkan semua produk dari satu penerimaan sebagai baris retur, dan tidak bisa
> menyimpan kalau ada baris yang sengaja dibiarkan kuantitas 0 (untuk produk yang tidak ingin
> diretur) — selalu ditolak dengan pesan "This Field Must Be At Least Min" (teks errornya
> sendiri juga belum diisi angka yang benar). Diakali dengan terpaksa mengikutsertakan 1 unit
> produk yang sebenarnya tidak rusak (Minyak Goreng) supaya retur Gula Pasir yang rusak
> (10 unit) tetap bisa disimpan. Retur berhasil diproses sampai status "Completed".
>
> **Temuan lain yang tidak menghalangi jalannya pengujian**: beberapa halaman "Create
> {Dokumen}" di modul Purchasing (Create Purchase Order, Create Goods Receipt) menampilkan
> judul halaman mentah yang belum diterjemahkan, dan Status History beberapa dokumen
> menampilkan kode status mentah (`po_created`, `gr_created`) — pola yang sama dengan temuan
> serupa di Sales. Juga ditemukan bahwa tombol "Create Goods Receipt" pada Purchase Order yang
> sudah berstatus "Paid" tidak melakukan apa-apa saat diklik (seharusnya nonaktif dengan
> keterangan, bukan diam saja) — dampaknya kecil karena PO memang sudah tidak perlu Goods
> Receipt baru pada titik itu.

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

> **Status Tahap F (2026-09-14): Selesai sebagian, dengan beberapa bug penting ditemukan.**
>
> **F.1** — semua skenario berhasil dijalankan: absensi sampel untuk 3 karyawan (Fitri Handayani,
> Novi Ramadhani, Andi Saputra) dibuat tanpa jam Check In/Check Out karena bug format jam
> (dijadikan workaround, lihat catatan Tahap sebelumnya); 1 pengajuan cuti Wati Suryani (2 hari,
> Cuti Tahunan) berhasil dibuat dan otomatis "Approved" (bukan lewat langkah approval manual
> karena bug `requires_approval` tidak ditegakkan); uji negatif pengajuan cuti tanpa saldo cukup
> berhasil ditolak dengan benar; 1 Attendance Adjustment untuk Trisno Aji berhasil dibuat, dan
> observer yang menerapkan perubahan ke data absensi asli terbukti berfungsi benar — hanya langkah
> approval-nya yang dilewati (pola bug yang sama dengan cuti). Dalam proses ini juga ditemukan
> bug toggle Leave Type saat Create (harus diperbaiki lewat Edit) dan master data Leave Types yang
> sebelumnya kosong sama sekali.
>
> **F.2** — periode payroll September 2026 berhasil dibuat, tapi tombol **Process, Approve, dan
> Mark As Paid di halaman detail semuanya gagal/terkunci** karena halaman tidak mengirim data
> yang benar ke server (bug tingkat tinggi, lihat catatan terpisah). Diakali dengan memanggil API
> langsung: Process berhasil membuat 25 Payroll Item sesuai jumlah karyawan aktif, tapi **semua
> potongan BPJS dan PPh21 tampil Rp 0** untuk seluruh karyawan karena data acuan BPJS dan pajak
> (PTKP/TER) tahun 2026 ternyata belum diisi sama sekali (bug tingkat tinggi terpisah). Approve
> berhasil dilakukan (lewat API). Mark As Paid **gagal** dengan pesan "Hrm Journal Type Is Not
> Seeded For This Branch" — bug seeding jurnal yang sama yang sudah ditemukan di modul Sales dan
> Purchasing, sekarang terbukti juga menimpa modul SDM. Uji negatif memanggil `generate` dua kali
> untuk bulan yang sama berhasil ditolak dengan benar (mengembalikan periode yang sudah ada, tidak
> membuat duplikat). Ditemukan juga 6 kode kunci terjemahan mentah (`content.payroll_functionality_*`)
> di halaman Payroll Journal Configuration.
>
> Karena bug seeding jurnal SDM, periode payroll September 2026 di lingkungan ini **tidak bisa
> mencapai status "paid"**, sehingga jurnal penyelesaian (settlement) yang seharusnya mengurangi
> Bank 1-110 tidak bisa diverifikasi datanya secara nyata sampai bug ini diperbaiki.

### Ringkasan Sebelum Lanjut

- [x] Tahap C: sesi kasir toko lengkap selesai (open→transaksi (hold/resume, uji batas stok, void, refund)→close dengan selisih kas Rp 14.000), 1 SO kredit B2B selesai sampai Invoice (tapi tanpa Delivery — gap validasi, lihat catatan), 1 retur dibuat & disetujui tapi stok tidak kembali (bug). Perlu Stock Transfer manual dulu sebagai prasyarat tersembunyi. Lihat catatan di atas untuk rincian.
- [x] Tahap D: 1 siklus meja lengkap selesai (open→add-item→kitchen→transfer table→split bill→close bill), tapi item tersimpan harga Rp 0 (bug) sehingga nominal uang tidak bisa dipakai sebagai acuan; Booking gagal total (bug field tidak cocok, belum bisa diuji). 1 SO katering via Sales selesai sampai Invoice (Export To Journal dan Create Payment gagal dengan bug lama yang sudah tercatat di modul Sales lain). Lihat catatan di atas untuk rincian.
- [x] Tahap E: 1 siklus PO→GR→PI→PPB termin (Grosir Sembako) selesai sampai lunas, uji negatif over-receipt berhasil ditolak dengan benar; 1 siklus tunai same-day (Pasar Segar, pakai produk pengganti karena bahan baku dapur segar belum ada di master data) selesai lunas hari yang sama; 1 retur pembelian selesai (tapi terpaksa ikut sertakan 1 item yang tidak rusak karena bug validasi kuantitas 0). Lihat catatan di atas untuk rincian.
- [x] Tahap F: absensi sampel + 1 cuti (auto-approved, bug enforcement) + 1 attendance adjustment selesai (F.1); payroll September berhasil `process`+`approve` lewat API (tombol halaman gagal, bug tinggi) dengan potongan BPJS/PPh21 Rp 0 (data acuan pajak 2026 belum diisi, bug tinggi); `mark-paid` gagal karena bug seeding jurnal SDM (sama seperti Sales/Purchasing); uji negatif generate 2× berhasil ditolak dengan benar. Lihat catatan di atas untuk rincian.

---

## Referensi Silang

- [`00-profil-perusahaan-dan-master-data.id.md`](00-profil-perusahaan-dan-master-data.id.md)
- [`01-urutan-input-master-data.id.md`](01-urutan-input-master-data.id.md)
- [[project_sales_canvassing_module]], [[project_gr_over_receipt_validation]], [[project_pi_payment_requires_approval_gate]], [[project_payment_bill_termin_ordering]]
- [`../../erpApiServices/routes/canvassing.php`](../../erpApiServices/routes/canvassing.php), [`../../erpApiServices/routes/sales.php`](../../erpApiServices/routes/sales.php), [`../../erpApiServices/routes/pos.php`](../../erpApiServices/routes/pos.php), [`../../erpApiServices/routes/restaurant.php`](../../erpApiServices/routes/restaurant.php), [`../../erpApiServices/routes/purchasing.php`](../../erpApiServices/routes/purchasing.php), [`../../erpApiServices/routes/hrm.php`](../../erpApiServices/routes/hrm.php)
