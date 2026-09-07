---
title: (Klinik Gigi) — 00. Profil Perusahaan & Master Data
category: accounting-klinik-gigi
description: Skenario baru berdiri sendiri — Klinik Ceria Medika, jaringan klinik gigi 3 cabang dengan volume transaksi harian kecil-kecil (tindakan pasien, komisi dokter, kas kecil), piutang BPJS/asuransi, dan periode fiskal mingguan. Fondasi seluruh file di folder ini, TIDAK terhubung ke suite testing/accounting/ maupun testing/accounting-manufaktur/.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

> **Suite ini berdiri SENDIRI**, terpisah total dari [`../accounting/`](../accounting/) (retail — PT Retail Nusantara Jaya) dan [`../accounting-manufaktur/`](../accounting-manufaktur/) (manufaktur — CV Sumber Makmur Abadi) — beda perusahaan, beda kode akun, beda tahun buku, beda tipe periode (**mingguan**, belum pernah dites di 2 suite sebelumnya). Jangan campur data/kode akun antar suite.
>
> **Kenapa industri jasa (klinik gigi), bukan lagi barang dagang/manufaktur**: dipilih spesifik karena punya kombinasi kasus akuntansi yang belum tersentuh 2 suite lain — **volume transaksi HARIAN yang sangat banyak tapi nilainya kecil** (tindakan gigi Rp 150rb-3jt, kas kecil operasional harian per cabang), **piutang jasa ke pihak ketiga (BPJS/asuransi)** yang beda karakter dari piutang dagang B2B biasa, dan **komisi tenaga profesional (dokter)** yang dihitung persentase per tindakan — bukan gaji tetap. Kombinasi ini didesain untuk menguji **akurasi angka** ERP saat banyak baris kecil diakumulasi — kalau ada pembulatan/rounding yang salah di satu baris, dampaknya baru kelihatan setelah puluhan transaksi diakumulasi, bukan di transaksi tunggal bernilai besar.
>
> **Pola tiap skenario**: **Positif** (jalur normal, harus sukses dengan nilai output PERSIS seperti yang tertera) / **Negatif** (input/urutan salah, harus DITOLAK dengan pesan jelas) / **Netralisasi** (cara mengembalikan state ke semula). Kolom **Label temuan** (🆕 fitur baru/gap desain, 🔧 improvement kecil, ✅ sudah tercover) dipakai HANYA kalau ada indikasi kuat dari pembacaan kode — kalau tidak sempat diverifikasi ke kode sungguhan, ditulis eksplisit **"belum diverifikasi ke kode"**, BUKAN diklaim sebagai bug pasti.
>
> **Kerjakan urutan file**: 00 → 01 → 02 → 03 → 04 → 05 → 06. Tiap file mengasumsikan file sebelumnya sudah dikerjakan — angka-angka di seluruh suite ini SALING TERKAIT (satu sumber kebenaran), jangan lompat urutan.

## Profil Perusahaan (Skenario)

**Klinik Ceria Medika** — jaringan klinik gigi swasta dengan 3 cabang di area Jabodetabek, melayani tindakan gigi umum, ortodonti (behel), dan estetika gigi (whitening/veneer), serta menjual produk perawatan gigi ritel (pasta gigi, mouthwash) di resepsionis. **Belum PKP** untuk jasa medis (jasa kesehatan/medis dibebaskan PPN sesuai ketentuan umum di Indonesia), TAPI terdaftar PKP khusus untuk penjualan produk ritel non-medis — sehingga PPN 11% HANYA dipungut di lini pendapatan produk ritel (akun 4104), TIDAK pernah muncul di pendapatan jasa tindakan (4101-4103). Ini kondisi disengaja untuk menguji bahwa akun `tax_id` dipasang selektif per-akun, bukan otomatis berlaku ke semua pendapatan.

Tiga cabang dijadikan dimensi Business Unit:

- **Klinik Ceria Kelapa Gading** (KG) — cabang flagship, volume pasien terbesar.
- **Klinik Ceria BSD** (BSD) — cabang kedua, area Tangerang Selatan.
- **Klinik Ceria Bekasi** (BKS) — cabang ketiga, dibuka pertengahan 2025, masih kecil.

Ciri yang membedakan dari 2 suite sebelumnya (sengaja, supaya menguji jalur kode/kasus yang belum pernah disentuh):

1. **Periode fiskal MINGGUAN** (`duration_type:"weekly"`) — belum pernah dites sama sekali di suite retail (bulanan) maupun manufaktur (kuartalan). Klinik tutup buku kas kecil tiap minggu untuk kontrol ketat arus kas harian.
2. **Piutang jasa pihak ketiga (BPJS/Asuransi)**, bukan piutang dagang B2B — dicatat di 1 akun kontrol AR yang sama (`is_ar_control_account`), tapi dites dengan pola pelunasan bertahap/parsial (klaim BPJS sering cair sebagian & telat) — variasi yang belum ada di 2 suite lain.
3. **Komisi dokter berbasis persentase per tindakan** (bukan gaji tetap) — dicatat sebagai **liability** (utang komisi) saat tindakan terjadi, baru jadi kas keluar saat dibayarkan periodik — mirip pola akrual beban yang belum pernah dites lengkap di suite lain.
4. **Kas kecil HARIAN per kasir/cabang** dengan banyak transaksi nilai kecil (Rp 50rb-500rb) dalam 1 hari — didesain supaya total akumulasi jadi alat uji akurasi angka (kalau ada satu baris salah hitung, total di Trial Balance file 02 akan MELESET dari angka yang dihitung manual di file ini).
5. **Persediaan Bahan Habis Pakai (BHP) gigi** (jarum suntik, kapas, sarung tangan, resin tambal) — nilai kecil per unit tapi frekuensi pakai tinggi, dicatat sebagai beban langsung per tindakan (bukan lewat metode persediaan perpetual/FIFO — modul Inventory di luar scope suite Accounting berdiri sendiri).

Tahun buku: **FY2026** (2026-01-01 s/d 2026-12-31), kalender. Mata uang operasional: **IDR** saja (tidak ada transaksi valas di suite ini — sudah dites lengkap di suite manufaktur).

> **Simplifikasi yang disengaja** (supaya file 03 Tutup Tahun Fiskal bisa langsung dites tanpa menunggu 52 minggu penuh): SELURUH transaksi jurnal manual di suite ini sengaja dikumpulkan di **4 minggu pertama Januari 2026** (Minggu 1 s/d Minggu 4) — minggu ke-5 dan seterusnya sengaja dibiarkan kosong. Ini bukan keterbatasan sistem, cuma strategi supaya file 03 §3.2 (Close Accounting Period mingguan) dan §3.3 (Close Fiscal Year) bisa dihitung manual dengan pasti.

## 1. Currency (**Currencies**)

| Skenario    | Payload                                                      | Hasil                                          |
| ----------- | ------------------------------------------------------------ | ---------------------------------------------- |
| Positif     | Pastikan `IDR` sudah ada (base, biasanya ter-seed dari Core) | Tersedia di `client-master/currencies/options` |
| Netralisasi | — (master global, jangan dihapus)                            |

## 2. Chart of Account Type (**Chart of Account Type**)

Sama struktur generik dengan 2 suite sebelumnya — kalau branch test ini share instance, boleh reuse, tidak perlu dibuat ulang:

| #   | Kode | Nama                     | `category` | `normal_balance` | `cash_flow_section` | Grup Laporan (`report_group`) |
| --- | ---- | ------------------------ | ---------- | ---------------- | ------------------- | ----------------------------- |
| 1   | AL   | Aset Lancar              | asset      | debit            | operating           | Balance Sheet                 |
| 2   | AT   | Aset Tetap               | asset      | debit            | investing           | Balance Sheet                 |
| 3   | LJP  | Liabilitas Jangka Pendek | liability  | credit           | operating           | Balance Sheet                 |
| 4   | EK   | Ekuitas                  | equity     | credit           | financing           | Balance Sheet                 |
| 5   | PD   | Pendapatan               | revenue    | credit           | operating           | Income Statement              |
| 6   | BB   | Beban                    | expense    | debit            | operating           | Income Statement              |

Kalau branch test ini TERPISAH (direkomendasikan supaya benar-benar independen dari 2 suite lain), create ke-6 tipe ini dari 0 — validasi sama persis seperti [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) §2, tidak diulang di sini.

## 3. Chart of Accounts (**Chart of Accounts**)

**28 akun**, kode numerik 4-digit (sama gaya dengan suite retail, beda rentang angka biar jelas kelihatan data berbeda).

### Aset Lancar (11xx)

| Kode | Nama Akun                               | Flag khusus                                                                               |
| ---- | --------------------------------------- | ----------------------------------------------------------------------------------------- |
| 1101 | Kas Kecil Klinik (Harian)               | `is_cash_account:true`, `balance_required:true` — dipakai transaksi harian file 01        |
| 1102 | Bank BCA Operasional                    | `is_cash_account:true` (saldo awal via `finance/bank-accounts`)                           |
| 1103 | Piutang Pasien — BPJS & Asuransi        | `is_ar_control_account:true`, `balance_required:true`                                     |
| 1104 | Persediaan Bahan Habis Pakai (BHP) Gigi | `balance_required:true`                                                                   |
| 1105 | PPN Masukan                             | `is_tax:true`, `tax_id:<PPN 11%>` — dipakai saat beli produk ritel kena PPN dari supplier |

### Aset Tetap (12xx)

| Kode | Nama Akun                              | Flag khusus                                                                                           |
| ---- | -------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 1201 | Unit Dental Chair & Peralatan          | — (dipakai file 05, garis lurus)                                                                      |
| 1202 | Akumulasi Penyusutan Unit Dental Chair | Kontra-aset, `normal_balance` tetap ikut tipe induk (debit), bersaldo negatif karena selalu di-kredit |
| 1203 | Kendaraan Operasional Klinik           | — (dipakai file 05, saldo menurun — 1 mobil untuk kunjungan pasien lansia/homecare)                   |
| 1204 | Akumulasi Penyusutan Kendaraan         | Kontra-aset, sama pola dengan 1202                                                                    |

### Liabilitas Jangka Pendek (21xx)

| Kode | Nama Akun                          | Flag khusus                                                                     |
| ---- | ---------------------------------- | ------------------------------------------------------------------------------- |
| 2101 | Utang Dagang — Supplier Bahan Gigi | `is_ap_control_account:true`, `balance_required:true`                           |
| 2102 | PPN Keluaran                       | `is_tax:true`, `tax_id:<PPN 11%>` — HANYA dipakai penjualan produk ritel (4104) |
| 2103 | Utang Komisi Dokter                | `balance_required:true` — akrual komisi belum dibayar, akun kunci file 01       |
| 2104 | Utang PPh 21 Karyawan              | `balance_required:true`                                                         |

### Ekuitas (31xx)

| Kode | Nama Akun     | Flag khusus                                                                |
| ---- | ------------- | -------------------------------------------------------------------------- |
| 3101 | Modal Pemilik | `is_opening_balance_equity_account:true` — WAJIB tepat 1 akun ber-flag ini |
| 3102 | Laba Ditahan  | `is_retained_earnings_account:true` — WAJIB tepat 1 akun ber-flag ini      |

### Pendapatan (41xx)

| Kode | Nama Akun                                          | Catatan                                                                            |
| ---- | -------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 4101 | Pendapatan Jasa Gigi Umum (tambal, cabut, scaling) | Bebas PPN (jasa medis)                                                             |
| 4102 | Pendapatan Jasa Ortodonti (Behel)                  | Bebas PPN (jasa medis)                                                             |
| 4103 | Pendapatan Jasa Estetika Gigi (Whitening/Veneer)   | Bebas PPN (jasa medis)                                                             |
| 4104 | Pendapatan Penjualan Produk Perawatan Gigi (Ritel) | `tax_id:<PPN 11%>` di sisi jual — **satu-satunya lini kena PPN**, dites di file 06 |

### Beban (51xx-52xx)

| Kode | Nama Akun                                            | Catatan                                                         |
| ---- | ---------------------------------------------------- | --------------------------------------------------------------- |
| 5101 | Beban Komisi Dokter                                  | Lawan akrual 2103, dites lengkap file 01                        |
| 5102 | Beban Bahan Habis Pakai (BHP) Gigi                   | Beban langsung per tindakan (bukan metode persediaan perpetual) |
| 5201 | Beban Sewa Klinik                                    | —                                                               |
| 5202 | Beban Gaji Karyawan Non-Dokter (Resepsionis/Perawat) | —                                                               |
| 5203 | Beban Listrik & Air                                  | —                                                               |
| 5204 | Beban Penyusutan Unit Dental Chair                   | —                                                               |
| 5205 | Beban Penyusutan Kendaraan                           | —                                                               |
| 5206 | Beban Selisih Kas Kasir Harian                       | Dipakai skenario opname kas kasir tiap cabang, file 01          |
| 5207 | Beban Sterilisasi & Limbah Medis                     | Biaya rutin wajib klinik gigi (autoclave, limbah B3 medis)      |

| Skenario                                                   | Detail                                                                                           | Hasil                                                                                                                                                                         |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                    | Create ke-28 akun di atas (satu-satu atau `create-bulk`)                                         | 201 semua, flag tersimpan **benar-benar** — `GET .../show` ulang untuk verifikasi, bukan cuma percaya response create (regression check yang sama seperti 2 suite sebelumnya) |
| Negatif                                                    | Create akun ke-2 ber-flag `is_opening_balance_equity_account:true`                               | Tidak ada validasi silang yang menolak (konsisten dengan temuan 2 suite sebelumnya, belum diverifikasi ulang kodenya di sesi ini — anggap masih berlaku sampai ada perbaikan) |
| **Positif — kontra-aset**                                  | Setelah ada transaksi penyusutan (file 05) yang men-kredit 1202/1204, cek saldo di Trial Balance | Saldo harus **negatif** (mengurangi Aset Tetap), bukan ditambahkan positif                                                                                                    |
| **Positif — PPN selektif per akun (kasus unik suite ini)** | Pastikan 4101/4102/4103 **TIDAK** diisi `tax_id` sama sekali, hanya 4104 yang diisi              | Setelah file 06, cek `reports/tax-summary` (atau endpoint sejenis) — hanya transaksi yang menyentuh 4104 yang muncul sebagai basis PPN Keluaran, bukan seluruh pendapatan     |
| Netralisasi                                                | `delete` akun test yang belum dipakai transaksi                                                  |

## 4. Fiscal Year (**Fiscal Year**)

| Skenario    | Payload                                                                                   | Hasil |
| ----------- | ----------------------------------------------------------------------------------------- | ----- |
| Positif     | `{code:"FY2026", name:"Tahun Buku 2026", start_date:"2026-01-01", end_date:"2026-12-31"}` | 201   |
| Netralisasi | `delete` — pastikan tidak ada `accounting_periods` di bawahnya                            |

## 5. Accounting Period — MINGGUAN (**Accounting Period**)

Beda dari 2 suite sebelumnya (bulanan/kuartalan) — pakai `duration_type:"weekly"`, belum pernah dites sama sekali.

| Skenario                          | Detail                                                                                                       | Hasil                                                                                                                                                                                                                                                   | Label temuan                                                                                                                                                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — generate mingguan       | `PUT client-master/fiscal-year/generate-accounting-period {fiscal_year_id:<FY2026>, duration_type:"weekly"}` | Sejumlah periode mingguan ter-generate dari 2026-01-01. **2026 punya 365 hari** → kemungkinan 52 periode 7-hari penuh + 1 periode sisa 1 hari (2026-12-31 sendirian), ATAU periode terakhir digabung jadi 8 hari — catat perilaku AKTUAL, jangan asumsi | Kalau periode terakhir malah HILANG (31 Desember tidak masuk periode manapun) → 🆕 bug generator, laporkan prioritas tinggi karena bisa bikin transaksi akhir tahun tidak bisa diposting. Kalau digabung/periode pendek terpisah, itu perilaku wajar → ✅ |
| Positif — periode pertama presisi | Cek periode pertama                                                                                          | Harus `start_date:"2026-01-01"`, `end_date:"2026-01-07"` (Kamis 1 Jan s/d Rabu 7 Jan) — inilah "Minggu 1" yang dipakai file 01                                                                                                                          | ✅ kalau sesuai                                                                                                                                                                                                                                           |
| Negatif                           | Generate lagi untuk fiscal year yang sama                                                                    | Ditolak/duplikat (tergantung guard — cek behavior aktual, sama seperti temuan suite retail §5)                                                                                                                                                          | Belum diverifikasi ke kode                                                                                                                                                                                                                                |
| Netralisasi                       | `delete` periode test satu-satu (banyak — pertimbangkan cuma hapus 4-5 periode awal yang dipakai testing)    |

**Referensi periode yang dipakai suite ini** (asumsi periode presisi 7 hari dari 1 Januari, verifikasi ulang di §5 baris pertama sebelum lanjut):

| Periode  | Rentang Tanggal           | Dipakai di file |
| -------- | ------------------------- | --------------- |
| Minggu 1 | 2026-01-01 s/d 2026-01-07 | 01, 02, 03      |
| Minggu 2 | 2026-01-08 s/d 2026-01-14 | 01, 02, 03      |
| Minggu 3 | 2026-01-15 s/d 2026-01-21 | 01, 02, 03      |
| Minggu 4 | 2026-01-22 s/d 2026-01-28 | 01, 02, 03      |

## 6. Business Unit — Cabang Klinik (**Business Units**)

| Skenario                | Payload                                                                    | Hasil                                                                                            |
| ----------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Positif — Kelapa Gading | `{code:"KG", name:"Klinik Ceria Kelapa Gading", default_unit_type:"both"}` | 201 — cabang flagship, volume terbesar                                                           |
| Positif — BSD           | `{code:"BSD", name:"Klinik Ceria BSD", default_unit_type:"both"}`          | 201                                                                                              |
| Positif — Bekasi        | `{code:"BKS", name:"Klinik Ceria Bekasi", default_unit_type:"both"}`       | 201 — cabang termuda, dipakai file 04 untuk banding kinerja antar cabang (masih kecil vs 2 lain) |
| Negatif                 | `default_unit_type` di luar enum (`cost/profit/both`)                      | 422                                                                                              |
| Netralisasi             | `delete` — pastikan tidak dipakai `journals.business_unit_id` manapun      |

## 7. Tax — PPN (**Taxes**)

| Skenario                             | Payload                                                                                                                                                                                                                                 | Hasil                                                                                                 |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Positif                              | `{name:"PPN 11%", code:"PPN11", rate:11, effect:"increase"}`                                                                                                                                                                            | 201 — HANYA dipasang ke akun 4104/1105/2102 (lihat §3), TIDAK ke akun pendapatan jasa medis 4101-4103 |
| **Catatan keterbatasan (bukan bug)** | PPh Final UMKM/Badan atas jasa klinik, serta PPh 23 jasa dokter yang berpraktik sebagai mitra (bukan karyawan tetap), TIDAK dimodelkan di suite ini — hanya PPN produk ritel dan PPh 21 karyawan tetap (resepsionis/perawat) yang dites | —                                                                                                     |
| Netralisasi                          | `delete` — pastikan tidak dipakai                                                                                                                                                                                                       |

## 8. Contact (**Contacts**) — DI-SKIP, TIDAK DIPERLUKAN UNTUK SUITE INI

> **Keputusan sesi ini, konsisten dengan suite manufaktur**: suite ini fokus MURNI ke modul Accounting (jurnal manual, saldo awal, GL, laporan keuangan, tutup periode/tahun, anggaran, aset tetap, rekonsiliasi bank) — TIDAK menyentuh modul Purchasing/Sales sama sekali. `Contact` (customer/supplier/pasien) di project ini HANYA dipakai sebagai FK di dokumen `purchase_orders`/`sales_orders`/turunannya — dikonfirmasi tidak ada satupun endpoint accounting murni (`journals`, `chart-of-accounts-balances`, **Bank Accounts**, **Bank Reconciliations**, **Budgets**, **Assets**) yang mensyaratkan `contact_id`. "Pasien BPJS/Asuransi" di suite ini murni **nama/keterangan bebas di deskripsi baris jurnal** (field teks), BUKAN entitas `Contact` — piutang tetap satu akun kontrol (1103), rincian per klaim BPJS dilacak lewat deskripsi jurnal, bukan sub-ledger per pasien (di luar scope Accounting berdiri sendiri; kalau butuh AR aging per pasien, itu scope modul lain).

Section ini **SENGAJA DI-SKIP** — tidak perlu create Contact apapun untuk melanjutkan suite ini.

## 9. Saldo Awal / Opening Balance (**Chart of Accounts Balances**, **Bank Accounts**)

**⚠️ Bagian paling kritis di file ini — fondasi seluruh laporan keuangan di file berikutnya. Hitung dengan sangat teliti.** Mengikuti kontrak field yang sama dengan 2 suite sebelumnya:

| Endpoint                                   | Field tersedia                                                                                                                                                                                                                                                                                                           | Dipakai untuk akun                 |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| `finance/bank-accounts`                    | `opening_balance` saja                                                                                                                                                                                                                                                                                                   | 1102                               |
| `client-master/chart-of-accounts-balances` | `opening_balance` (+ `debit_total`/`credit_total`, TIDAK dipakai di sini — nilai polos saja, konsisten pola "regression check standar" seperti §10.4 suite manufaktur, supaya suite ini fokus ke tema utamanya sendiri yaitu volume transaksi kecil harian, bukan mengulang bug yang sudah tercatat di suite manufaktur) | 1101, 1103, 1104, 2101, 2103, 2104 |

**Saldo awal yang dipakai** (angka disengaja kecil-kecil, khas kas harian klinik — total HARUS balance, dihitung manual di bawah):

| Akun                                    | Saldo Awal (IDR) | Jalur                        |
| --------------------------------------- | ---------------: | ---------------------------- |
| 1101 Kas Kecil Klinik (Harian)          |        3.000.000 | `chart-of-accounts-balances` |
| 1102 Bank BCA Operasional               |      150.000.000 | `finance/bank-accounts`      |
| 1103 Piutang Pasien — BPJS & Asuransi   |       28.500.000 | `chart-of-accounts-balances` |
| 1104 Persediaan BHP Gigi                |       22.750.000 | `chart-of-accounts-balances` |
| 2101 Utang Dagang — Supplier Bahan Gigi |       14.300.000 | `chart-of-accounts-balances` |
| 2103 Utang Komisi Dokter                |        6.750.000 | `chart-of-accounts-balances` |
| 2104 Utang PPh 21 Karyawan              |        1.850.000 | `chart-of-accounts-balances` |

**Perhitungan manual (WAJIB cocok persis dengan hasil Trial Balance di §9.4 dan file 02):**

```
Total Aset       = 3.000.000 + 150.000.000 + 28.500.000 + 22.750.000
                  = 204.250.000
Total Liabilitas = 14.300.000 + 6.750.000 + 1.850.000
                  = 22.900.000
Modal Pemilik (3101) = Total Aset − Total Liabilitas
                      = 204.250.000 − 22.900.000
                      = 181.350.000  (KREDIT)
```

### 9.1 Guard — coba isi saldo awal SEBELUM akun equity ber-flag ada

| Skenario | Detail                                                                                                                                                                          | Hasil                                                                                                    |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Negatif  | Pastikan dulu BELUM ada akun ber-flag `is_opening_balance_equity_account:true`, lalu `POST .../create {chart_of_account_id:<1101>, currency_id:<IDR>, opening_balance:3000000}` | Ditolak `no_opening_balance_equity_account_configured_for_this_branch` — bukan 500, bukan silent-success |
| Negatif  | `chart_of_account_id` menunjuk akun `balance_required:false` (mis. 4101)                                                                                                        | Ditolak, pesan sejenis "This COA does not require a balance record."                                     |

### 9.2 Flag Modal Pemilik jadi akun offset saldo awal

| Skenario | Payload                                                                                          | Hasil                                                |
| -------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Positif  | `PUT client-master/chart-of-accounts/update {id:<3101>, is_opening_balance_equity_account:true}` | 200, `GET .../show` akun 3101 konfirmasi flag `true` |

### 9.3 Saldo Awal Bank — Bank BCA Operasional (**Bank Accounts**)

| Skenario    | Payload                                                                                                                                                                                                           | Hasil                                                                                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif     | `POST finance/bank-accounts/create {account_name:"BCA Operasional Klinik", bank_name:"Bank Central Asia", account_number:"5560012233", currency_id:<IDR>, chart_of_account_id:<1102>, opening_balance:150000000}` | 201 — `opening_balance_journal_header_id` terisi, `accounting/journals/list` filter kode `JRN-OB-*` menunjukkan Dr 1102 150.000.000 / Cr 3101 150.000.000, status `JRN_POSTED` |
| Netralisasi | Simpan bank account ini untuk dipakai file `06-rekonsiliasi-bank-dan-ppn.id.md` — JANGAN dihapus sampai file itu selesai                                                                                          |

### 9.4 Saldo Awal via Chart of Account Balances — akun sisanya

| Skenario                                    | Payload                                                                                    | Hasil                                                                                                                           |
| ------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Positif — Kas Kecil Klinik                  | `POST .../create {chart_of_account_id:<1101>, currency_id:<IDR>, opening_balance:3000000}` | Dr 1101 / Cr 3101, 3.000.000                                                                                                    |
| Positif — Piutang Pasien BPJS/Asuransi      | sama, `chart_of_account_id:<1103>, opening_balance:28500000`                               | Dr 1103 / Cr 3101, 28.500.000                                                                                                   |
| Positif — Persediaan BHP Gigi               | sama, `chart_of_account_id:<1104>, opening_balance:22750000`                               | Dr 1104 / Cr 3101, 22.750.000                                                                                                   |
| Positif — Utang Dagang Supplier (liability) | sama, `chart_of_account_id:<2101>, opening_balance:14300000`                               | **Arah kebalikan** (`normal_balance` akun ini `credit`) — Cr 2101 / Dr 3101, 14.300.000 — jangan asumsi selalu Dr-akun/Cr-modal |
| Positif — Utang Komisi Dokter               | sama, `chart_of_account_id:<2103>, opening_balance:6750000`                                | Cr 2103 / Dr 3101, 6.750.000                                                                                                    |
| Positif — Utang PPh 21 Karyawan             | sama, `chart_of_account_id:<2104>, opening_balance:1850000`                                | Cr 2104 / Dr 3101, 1.850.000                                                                                                    |
| Negatif                                     | `opening_balance` sebagai string bukan angka, atau `currency_id` yang tidak ada            | 422                                                                                                                             |
| Negatif                                     | `chart_of_account_id` dari branch lain                                                     | 422 `not_found_in_branch`                                                                                                       |

### 9.5 Verifikasi ke General Ledger / Trial Balance

| Skenario | Detail                                                                  | Hasil                                                                                                                                                                           |
| -------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/trial-balance` setelah §9.3+9.4 lengkap | `total_debit = total_credit` (balanced). Saldo 3101 Modal Pemilik = **kredit 181.350.000** persis (lihat perhitungan manual di atas) — kalau beda, ada entri salah arah/kelewat |
| Positif  | Cek `accounting/journals/list` filter kode `JRN-OB-*`                   | Total 7 jurnal (6 dari §9.4 + 1 dari §9.3), semua `status:JRN_POSTED`, `is_reversed:false`                                                                                      |

## Ringkasan Data Master yang Harus Sudah Ada Sebelum Lanjut ke File 01

- [ ] Currency IDR
- [ ] 6 Chart of Account Type
- [ ] 28 Chart of Accounts (§3), flag tersimpan benar — termasuk PPN yang SELEKTIF hanya di 4104/1105/2102, TIDAK di 4101-4103
- [ ] Fiscal Year FY2026 + periode **MINGGUAN** (verifikasi periode 1 = 2026-01-01 s/d 2026-01-07)
- [ ] 3 Business Unit (KG, BSD, BKS)
- [ ] Tax PPN 11%
- [ ] ~~Contact~~ — **DI-SKIP** (§8, tidak dibutuhkan modul Accounting murni)
- [ ] Saldo awal 7 akun terposting — Modal Pemilik final **181.350.000**, Trial Balance balanced

## Referensi Silang

- [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) — suite retail, pola dasar struktur tabel
- [`../accounting-manufaktur/00-profil-perusahaan-dan-master-data.id.md`](../accounting-manufaktur/00-profil-perusahaan-dan-master-data.id.md) — suite manufaktur, sumber temuan bug `debit_total`/`credit_total` & currency saldo awal yang DISENGAJA tidak diulang di suite ini (lihat §9 header) supaya fokus ke tema baru (volume transaksi kecil)
- `App\Services\JournalPostingService::syncOpeningBalance()` — implementasi posting saldo awal, sama seperti 2 suite lain
- `App\Http\Controllers\ClientMaster\AccountingPeriod.php` — validasi `duration_type` mendukung `monthly,quarterly,weekly` (baris ~106/157/219/282), `weekly` baru dipakai pertama kali di suite ini
