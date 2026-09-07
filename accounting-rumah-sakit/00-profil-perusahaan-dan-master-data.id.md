---
title: (Rumah Sakit) — 00. Profil Perusahaan & Master Data
category: accounting-rumah-sakit
description: Skenario baru berdiri sendiri — RS Sentosa Medika Utama, rumah sakit swasta besar dengan rawat inap multi-kelas, rawat jalan multi-poli, farmasi, lab/radiologi, klaim BPJS & asuransi swasta, fee dokter spesialis, dan pinjaman bank ekspansi gedung. Fondasi seluruh file di folder ini, TIDAK terhubung ke suite testing/accounting/, testing/accounting-manufaktur/, testing/accounting-fnb-kafe/, testing/accounting-klinik-gigi/, maupun suite klinik umum yang dibuat paralel.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

> **Suite ini berdiri SENDIRI**, terpisah total dari 4 suite Accounting lain yang sudah ada (retail, manufaktur x2, F&B kafe, klinik gigi) — beda perusahaan, beda kode akun, beda tahun buku. Jangan campur data/kode akun antar suite.
>
> **Beda dari suite "klinik umum" yang dibuat paralel oleh sesi lain**: suite ini fokus KHUSUS ke **rumah sakit skala besar** (bukan klinik kecil/menengah) — rawat inap multi-kelas (3/2/1/VIP/ICU), rawat jalan multi-poli/spesialis, farmasi/apotek dengan HPP obat, laboratorium & radiologi, dua jalur piutang pihak ketiga (BPJS Kesehatan DAN asuransi swasta) dengan kasus **klaim BPJS ditolak sebagian (dispute)**, fee dokter spesialis fee-for-service (beda dari dokter umum bergaji tetap), aset medis besar bernilai miliaran (Gedung, CT-Scan, MRI, Radiologi, Ambulans), dan pinjaman bank jangka panjang untuk ekspansi gedung. Jangan duplikasi skenario klinik kecil di sini — kompleksitas & skala nilai transaksi di suite ini SENGAJA jauh lebih besar.
>
> **Pola tiap skenario**: **Positif** (jalur normal, harus sukses dengan nilai output PERSIS seperti yang tertera) / **Negatif** (input/urutan salah, harus DITOLAK dengan pesan jelas) / **Netralisasi** (cara mengembalikan state ke semula). Kolom **Label temuan** (🆕 fitur baru/gap desain, 🔧 improvement kecil, ✅ sudah tercover) dipakai HANYA kalau ada indikasi kuat dari pembacaan kode — kalau tidak sempat diverifikasi ke kode sungguhan, ditulis eksplisit **"belum diverifikasi ke kode"**, BUKAN diklaim sebagai bug pasti.
>
> **Endpoint Fixed Assets — WAJIB dipakai versi yang BENAR**: **Assets — `{list|show|create|update|delete|calculate-depreciation|run-depreciation}`** dan **Disposals — `{list|show|create}`** — **BUKAN** `finance/fixed-assets/*` (beberapa suite lama salah tulis prefix ini, sedang diperbaiki di sesi paralel lain). Seluruh referensi endpoint aset tetap di suite ini sudah pakai prefix yang benar sejak awal.
>
> **Kerjakan urutan file**: 00 → 01 → 02 → 03 → 04 → 05 → 06 → 07. Tiap file mengasumsikan file sebelumnya sudah dikerjakan — angka-angka di seluruh suite ini SALING TERKAIT (satu sumber kebenaran), jangan lompat urutan.

## Profil Perusahaan (Skenario)

**RS Sentosa Medika Utama** — rumah sakit swasta tipe B (fiktif), berlokasi di Jakarta Timur, beroperasi lebih dari 10 tahun (bukan startup — sengaja dipilih supaya aset tetap besar SUDAH punya akumulasi penyusutan dari opening balance, bukan mulai dari nol seperti 4 suite lain). Melayani rawat inap (5 kelas kamar), rawat jalan multi-spesialis, farmasi/apotek, laboratorium, dan radiologi (CT-Scan, MRI, X-Ray, USG). Sudah PKP.

Empat unit/departemen dijadikan dimensi Business Unit (BUKAN cabang lokasi seperti 2 suite lain — di suite ini gedung RS cuma satu, dimensinya per DEPARTEMEN):

- **Rawat Inap (RI)** — unit dengan pendapatan terbesar, kamar kelas 3/2/1/VIP/ICU.
- **Rawat Jalan (RJ)** — poliklinik umum & spesialis.
- **Farmasi (FAR)** — apotek rawat inap/jalan + penjualan obat bebas (OTC).
- **Penunjang Medis (PJG)** — laboratorium & radiologi.

Ciri yang membedakan dari 4 suite Accounting lain (sengaja, supaya menguji jalur kode/kasus yang belum pernah disentuh):

1. **Piutang pihak ketiga GANDA** — BPJS Kesehatan (akun terpisah dari piutang pasien umum) DAN asuransi swasta (akun terpisah lagi) — 3 jalur pembayaran pasien sekaligus (tunai/kartu, BPJS, asuransi swasta), dengan **kasus klaim BPJS ditolak SEBAGIAN (dispute)** yang harus dihapusbukukan sebagai piutang tak tertagih — belum pernah dites di suite klinik gigi (yang hanya BPJS parsial-cair, bukan ditolak).
2. **Rekening bank KHUSUS BPJS terpisah dari rekening operasional umum** — pola nyata rumah sakit besar di Indonesia (BPJS mencairkan dana ke rekening tervalidasi khusus), dites di file 07 (rekonsiliasi multi-rekening).
3. **Fee dokter spesialis fee-for-service** (persentase per tindakan, diakru sebagai liability `2103`) — BEDA dari dokter umum/perawat/staf non-medis yang bergaji tetap bulanan (`5102`, dibayar langsung, tidak lewat akrual per-tindakan). Dua model kompensasi tenaga medis dalam satu suite, kontras yang belum pernah dites.
4. **Aset medis besar dengan saldo awal SUDAH ADA akumulasi penyusutan** (Gedung, CT-Scan, MRI, Peralatan Radiologi) — beda dari 4 suite lain yang aset tetapnya mulai dari nol. Mencerminkan RS yang migrasi ke sistem baru setelah bertahun-tahun beroperasi: opening balance aset tetap dicatat di LEVEL AKUN (`chart-of-accounts-balances`), bukan sebagai baris individual di modul `fixed-assets/assets` — keterbatasan migrasi data yang realistis dan disengaja diuji di file 06.
5. **Pinjaman bank jangka panjang untuk ekspansi gedung**, dengan cicilan pokok+bunga bulanan — skala nilai jauh lebih besar dari pinjaman mesin produksi di suite manufaktur.
6. **PPN selektif** (pola yang sama filosofinya dengan suite klinik gigi, tapi kasusnya beda): jasa kesehatan (rawat inap, rawat jalan, lab, radiologi) dan obat RESEP (bagian pengobatan) **bebas PPN**, HANYA penjualan obat bebas/OTC di apotek luar (`4111`) yang kena PPN 11% — sengaja dibuat mirip pola klinik gigi supaya bisa dibandingkan konsistensi hasil, tapi dengan kombinasi akun yang jauh lebih banyak.

Tahun buku: **FY2026** (2026-01-01 s/d 2026-12-31), kalender, periode **BULANAN** (`duration_type:"monthly"` — standar untuk RS besar, kontrol kas ketat tapi tidak sampai mingguan seperti klinik gigi). Mata uang operasional: **IDR** saja.

> **Simplifikasi yang disengaja** (supaya file 03 Tutup Tahun Fiskal bisa dites tanpa menunggu 12 bulan penuh): SELURUH transaksi jurnal manual harian di file 01 sengaja dikumpulkan di **bulan Januari 2026 (Periode 1)** — Februari dipakai khusus file 06 (aset tetap), Maret dipakai file 06 lanjutan (pelepasan/upgrade aset) dan file 07 (rekonsiliasi bank). April-Desember sengaja dibiarkan kosong. ini bukan keterbatasan sistem, cuma strategi supaya file 03 §2 (Close Fiscal Year) bisa dihitung manual dengan pasti.

## 1. Currency (**Currencies**)

| Skenario    | Payload                                                      | Hasil                                          |
| ----------- | ------------------------------------------------------------ | ---------------------------------------------- |
| Positif     | Pastikan `IDR` sudah ada (base, biasanya ter-seed dari Core) | Tersedia di `client-master/currencies/options` |
| Netralisasi | — (master global, jangan dihapus)                            |

## 2. Chart of Account Type (**Chart of Account Type**)

Struktur generik sama dengan suite lain — kalau branch test ini share instance, boleh reuse:

| #   | Kode | Nama                      | `category` | `normal_balance` | `cash_flow_section` | Grup Laporan (`report_group`) |
| --- | ---- | ------------------------- | ---------- | ---------------- | ------------------- | ----------------------------- |
| 1   | AL   | Aset Lancar               | asset      | debit            | operating           | Balance Sheet                 |
| 2   | AT   | Aset Tetap                | asset      | debit            | investing           | Balance Sheet                 |
| 3   | LJP  | Liabilitas Jangka Pendek  | liability  | credit           | operating           | Balance Sheet                 |
| 4   | LJPJ | Liabilitas Jangka Panjang | liability  | credit           | financing           | Balance Sheet                 |
| 5   | EK   | Ekuitas                   | equity     | credit           | financing           | Balance Sheet                 |
| 6   | PD   | Pendapatan                | revenue    | credit           | operating           | Income Statement              |
| 7   | BB   | Beban                     | expense    | debit            | operating           | Income Statement              |

Kalau branch test ini TERPISAH (direkomendasikan), create ke-7 tipe ini dari 0 — validasi sama persis seperti suite lain, tidak diulang di sini. **Beda dari 4 suite lain**: suite ini punya tipe `LJPJ` (Liabilitas Jangka Panjang) TERPISAH dari `LJP` — dipakai khusus untuk pinjaman bank ekspansi gedung (`2201`), supaya laporan neraca membedakan liabilitas lancar vs tidak lancar (belum pernah dites terpisah di suite lain, yang semua liabilitasnya jangka pendek).

## 3. Chart of Accounts (**Chart of Accounts**)

**51 akun** — jauh lebih banyak & kompleks dari suite klinik gigi (28 akun), mencerminkan skala operasional rumah sakit besar dengan banyak lini pendapatan & beban spesifik medis.

### Aset Lancar (11xx)

| Kode | Nama Akun                                        | Flag khusus                                                                                                                         |
| ---- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| 1101 | Kas Kecil Operasional RS                         | `is_cash_account:true`, `balance_required:true`                                                                                     |
| 1102 | Bank BCA Operasional (Umum)                      | `is_cash_account:true` (saldo awal via `finance/bank-accounts`)                                                                     |
| 1103 | Bank Mandiri — Rekening Khusus BPJS Kesehatan    | `is_cash_account:true` (saldo awal via `finance/bank-accounts`) — pencairan dana BPJS HANYA masuk ke rekening ini, dites di file 07 |
| 1104 | Piutang Pasien Umum (non-BPJS/non-asuransi)      | `is_ar_control_account:true`, `balance_required:true`                                                                               |
| 1105 | Piutang Klaim BPJS Kesehatan                     | `is_ar_control_account:true`, `balance_required:true` — dipakai kasus dispute di file 01                                            |
| 1106 | Piutang Klaim Asuransi Swasta                    | `is_ar_control_account:true`, `balance_required:true` — kontras BPJS, dicairkan penuh tanpa sengketa                                |
| 1107 | Persediaan Obat, Alkes & Bahan Medis Habis Pakai | `balance_required:true`                                                                                                             |
| 1108 | PPN Masukan                                      | `is_tax:true`, `tax_id:<PPN 11%>`                                                                                                   |

### Aset Tetap (12xx)

| Kode | Nama Akun                                | Flag khusus                                                  |
| ---- | ---------------------------------------- | ------------------------------------------------------------ |
| 1201 | Gedung Rumah Sakit                       | — (garis lurus, opening SUDAH ada akumulasi — lihat file 06) |
| 1202 | Akumulasi Penyusutan Gedung              | Kontra-aset, bersaldo kredit (ditampilkan negatif di Neraca) |
| 1203 | Mesin CT-Scan                            | — (garis lurus)                                              |
| 1204 | Akumulasi Penyusutan Mesin CT-Scan       | Kontra-aset                                                  |
| 1205 | Mesin MRI                                | — (garis lurus)                                              |
| 1206 | Akumulasi Penyusutan Mesin MRI           | Kontra-aset                                                  |
| 1207 | Peralatan Radiologi (X-Ray & USG)        | — (saldo menurun/declining balance)                          |
| 1208 | Akumulasi Penyusutan Peralatan Radiologi | Kontra-aset                                                  |

> Akun **Kendaraan Ambulans** (`1209`/`1210`) BELUM ada di daftar ini — sengaja ditambahkan BARU di file 06 saat RS membeli ambulans baru, mendemonstrasikan alur "tambah akun COA baru di tengah suite" (pola yang sama dipakai suite klinik gigi untuk `5208`).

### Liabilitas Jangka Pendek (21xx)

| Kode | Nama Akun                               | Flag khusus                                                                                               |
| ---- | --------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 2101 | Utang Dagang — Supplier Farmasi & Alkes | `is_ap_control_account:true`, `balance_required:true`                                                     |
| 2102 | PPN Keluaran                            | `is_tax:true`, `tax_id:<PPN 11%>` — HANYA dipakai penjualan obat bebas/OTC (4111)                         |
| 2103 | Utang Fee Dokter Spesialis              | `balance_required:true` — akrual fee-for-service, akun kunci file 01                                      |
| 2104 | Utang Gaji Karyawan Tetap               | `balance_required:true` — akrual gaji periode sebelumnya yang belum dibayar                               |
| 2105 | Utang PPh 21 Karyawan                   | `balance_required:true`                                                                                   |
| 2106 | Uang Muka Pasien Rawat Inap             | `balance_required:true` — DP pasien rawat inap sebelum keluar, liability sampai tagihan final diterbitkan |

### Liabilitas Jangka Panjang (22xx)

| Kode | Nama Akun                                   | Flag khusus                                                                                    |
| ---- | ------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 2201 | Utang Bank Jangka Panjang — Ekspansi Gedung | `balance_required:true`, `chart_of_account_type_id:<LJPJ>` — cicilan pokok+bunga dites file 01 |

### Ekuitas (31xx)

| Kode | Nama Akun     | Flag khusus                                                                                                                                                                                    |
| ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3101 | Modal Pemilik | `is_opening_balance_equity_account:true` — WAJIB tepat 1 akun ber-flag ini                                                                                                                     |
| 3102 | Laba Ditahan  | `is_retained_earnings_account:true` — WAJIB tepat 1 akun ber-flag ini, opening 0 (konsisten pola suite lain — semua opening balance HANYA dihitung lewat 3101, bukan diinjeksi manual ke 3102) |

### Pendapatan (41xx)

| Kode | Nama Akun                                           | Catatan                                                            |
| ---- | --------------------------------------------------- | ------------------------------------------------------------------ |
| 4101 | Pendapatan Rawat Inap Kelas 3                       | Bebas PPN (jasa kesehatan)                                         |
| 4102 | Pendapatan Rawat Inap Kelas 2                       | Bebas PPN — tidak ada transaksi di file 01 (lihat catatan file 01) |
| 4103 | Pendapatan Rawat Inap Kelas 1                       | Bebas PPN — tidak ada transaksi di file 01                         |
| 4104 | Pendapatan Rawat Inap VIP                           | Bebas PPN                                                          |
| 4105 | Pendapatan Rawat Inap ICU                           | Bebas PPN                                                          |
| 4106 | Pendapatan Rawat Jalan Poli Umum                    | Bebas PPN                                                          |
| 4107 | Pendapatan Rawat Jalan Poli Spesialis               | Bebas PPN                                                          |
| 4108 | Pendapatan Laboratorium                             | Bebas PPN                                                          |
| 4109 | Pendapatan Radiologi (CT-Scan/MRI/X-Ray/USG)        | Bebas PPN                                                          |
| 4110 | Pendapatan Farmasi — Obat Resep (bagian pengobatan) | Bebas PPN (bundled jasa kesehatan)                                 |
| 4111 | Pendapatan Farmasi — Obat Bebas/OTC (Apotek Luar)   | `tax_id:<PPN 11%>` — **satu-satunya lini kena PPN**, dites file 07 |

### Beban (51xx)

| Kode | Nama Akun                                            | Catatan                                                              |
| ---- | ---------------------------------------------------- | -------------------------------------------------------------------- |
| 5101 | Beban Fee Dokter Spesialis                           | Lawan akrual 2103                                                    |
| 5102 | Beban Gaji Karyawan Tetap (Dokter Umum/Perawat/Staf) | Beda model kompensasi dari 5101 — gaji tetap, bukan fee per tindakan |
| 5103 | Beban HPP Obat & Alkes (Farmasi)                     | Harga pokok obat terjual                                             |
| 5104 | Beban Bahan Medis Habis Pakai (Non-Farmasi)          | Dipakai lab/rawat inap langsung                                      |
| 5105 | Beban Listrik, Air & Pemeliharaan Gedung             | —                                                                    |
| 5106 | Beban Penyusutan Gedung                              | Dipakai file 06                                                      |
| 5107 | Beban Penyusutan Mesin CT-Scan                       | Dipakai file 06                                                      |
| 5108 | Beban Penyusutan Mesin MRI                           | Dipakai file 06                                                      |
| 5109 | Beban Penyusutan Peralatan Radiologi                 | Dipakai file 06                                                      |
| 5110 | Beban Penyusutan Kendaraan Ambulans                  | Dipakai file 06 (akun baru bersama 1209/1210)                        |
| 5111 | Beban Piutang Tak Tertagih (Klaim BPJS Ditolak)      | Kasus dispute kunci suite ini, dipakai file 01                       |
| 5112 | Beban Administrasi Bank                              | Dipakai file 01 (demo reverse) & file 07 (rekonsiliasi)              |
| 5113 | Beban Bunga Pinjaman Bank                            | Lawan cicilan 2201                                                   |
| 5114 | Beban Selisih Kas Kasir                              | Opname kas kecil                                                     |
| 5115 | Beban Sterilisasi & Limbah Medis                     | Biaya rutin wajib RS (limbah B3 medis, incinerator)                  |

| Skenario                                                      | Detail                                                                             | Hasil                                                                                                                                                                                |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif                                                       | Create ke-51 akun di atas (satu-satu atau `create-bulk`)                           | 201 semua, flag tersimpan **benar-benar** — `GET .../show` ulang untuk verifikasi, bukan cuma percaya response create                                                                |
| **Positif — kontra-aset (4 pasang sekaligus)**                | Setelah opening balance §9 terposting, cek Trial Balance untuk 1202/1204/1206/1208 | Semua HARUS **negatif** (mengurangi Aset Tetap gross), bukan ditambahkan positif — regression check di skala lebih besar dari suite lain (4 pasang kontra sekaligus, bukan cuma 1-2) |
| **Positif — PPN selektif (10 dari 11 akun pendapatan BEBAS)** | Pastikan 4101-4110 **TIDAK** diisi `tax_id` sama sekali, hanya 4111 yang diisi     | Setelah file 07, cek `reports/tax-summary` — hanya transaksi yang menyentuh 4111 yang muncul sebagai basis PPN Keluaran                                                              |
| Netralisasi                                                   | `delete` akun test yang belum dipakai transaksi                                    |

## 4. Fiscal Year (**Fiscal Year**)

| Skenario    | Payload                                                                                   | Hasil |
| ----------- | ----------------------------------------------------------------------------------------- | ----- |
| Positif     | `{code:"FY2026", name:"Tahun Buku 2026", start_date:"2026-01-01", end_date:"2026-12-31"}` | 201   |
| Netralisasi | `delete` — pastikan tidak ada `accounting_periods` di bawahnya                            |

## 5. Accounting Period — BULANAN (**Accounting Period**)

| Skenario                   | Detail                                                                                                        | Hasil                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Positif — generate bulanan | `PUT client-master/fiscal-year/generate-accounting-period {fiscal_year_id:<FY2026>, duration_type:"monthly"}` | 12 periode ter-generate, `Periode 1 = 2026-01-01 s/d 2026-01-31`, ..., `Periode 12 = 2026-12-01 s/d 2026-12-31` |
| Negatif                    | Generate lagi untuk fiscal year yang sama                                                                     | Ditolak/duplikat — konsisten dengan temuan suite lain                                                           |
| Netralisasi                | `delete` periode test satu-satu di akhir suite                                                                |

**Referensi periode yang dipakai suite ini:**

| Periode         | Rentang Tanggal           | Dipakai di file                                             |
| --------------- | ------------------------- | ----------------------------------------------------------- |
| Periode 1 (Jan) | 2026-01-01 s/d 2026-01-31 | 01, 02, 03                                                  |
| Periode 2 (Feb) | 2026-02-01 s/d 2026-02-28 | 06                                                          |
| Periode 3 (Mar) | 2026-03-01 s/d 2026-03-31 | 06, 07                                                      |
| Periode 4-12    | Apr-Des 2026              | Kosong (dites khusus di file 03 §2 guard Close Fiscal Year) |

## 6. Business Unit — Departemen RS (**Business Units**)

| Skenario                  | Payload                                                                            | Hasil                                 |
| ------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------- |
| Positif — Rawat Inap      | `{code:"RI", name:"Rawat Inap", default_unit_type:"both"}`                         | 201 — unit dengan pendapatan terbesar |
| Positif — Rawat Jalan     | `{code:"RJ", name:"Rawat Jalan", default_unit_type:"both"}`                        | 201                                   |
| Positif — Farmasi         | `{code:"FAR", name:"Farmasi", default_unit_type:"both"}`                           | 201                                   |
| Positif — Penunjang Medis | `{code:"PJG", name:"Penunjang Medis (Lab & Radiologi)", default_unit_type:"both"}` | 201                                   |
| Negatif                   | `default_unit_type` di luar enum (`cost/profit/both`)                              | 422                                   |
| Netralisasi               | `delete` — pastikan tidak dipakai `journals.business_unit_id` manapun              |

## 7. Tax — PPN (**Taxes**)

| Skenario                             | Payload                                                                                                                                                                                                                                                              | Hasil                                                                                       |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Positif                              | `{name:"PPN 11%", code:"PPN11", rate:11, effect:"increase"}`                                                                                                                                                                                                         | 201 — HANYA dipasang ke akun 4111/1108/2102, TIDAK ke 10 akun pendapatan jasa medis lainnya |
| **Catatan keterbatasan (bukan bug)** | PPh 23 jasa dokter spesialis yang berpraktik sebagai mitra (bukan karyawan tetap), PPh Badan tahunan RS, serta mekanisme kompensasi PPN lebih bayar ke masa pajak berikutnya TIDAK dimodelkan di suite ini — hanya PPN obat OTC dan PPh 21 karyawan tetap yang dites | —                                                                                           |
| Netralisasi                          | `delete` — pastikan tidak dipakai                                                                                                                                                                                                                                    |

## 8. Contact (**Contacts**) — DI-SKIP, TIDAK DIPERLUKAN UNTUK SUITE INI

> **Keputusan sesi ini, konsisten dengan 4 suite Accounting lain**: suite ini fokus MURNI ke modul Accounting — TIDAK menyentuh modul Purchasing/Sales sama sekali. `Contact` di project ini HANYA dipakai sebagai FK di dokumen `purchase_orders`/`sales_orders`/turunannya — dikonfirmasi tidak ada satupun endpoint accounting murni (`journals`, `chart-of-accounts-balances`, **Bank Accounts**, **Bank Reconciliations**, **Budgets**, **Assets**, **Disposals**) yang mensyaratkan `contact_id`. "BPJS Kesehatan" dan "Asuransi Swasta" (nama perusahaan asuransi rekanan) di suite ini murni **nama/keterangan bebas di deskripsi baris jurnal** (field teks), BUKAN entitas `Contact` — piutang tetap 2 akun kontrol terpisah (1105 BPJS, 1106 Asuransi Swasta), rincian per klaim/per pasien dilacak lewat deskripsi jurnal, bukan sub-ledger per pasien/per asuransi (di luar scope Accounting berdiri sendiri).

Section ini **SENGAJA DI-SKIP** — tidak perlu create Contact apapun untuk melanjutkan suite ini.

## 9. Saldo Awal / Opening Balance (**Chart of Accounts Balances**, **Bank Accounts**)

**⚠️ Bagian paling kritis di file ini — fondasi seluruh laporan keuangan di file berikutnya. Hitung dengan sangat teliti.** 23 posting saldo awal — jauh lebih banyak dari suite lain, mencerminkan skala RS besar dengan aset tetap yang sudah punya akumulasi penyusutan.

| Endpoint                                   | Field tersedia                                                                                                                                                                                              | Dipakai untuk akun |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `finance/bank-accounts`                    | `opening_balance` saja                                                                                                                                                                                      | 1102, 1103         |
| `client-master/chart-of-accounts-balances` | `opening_balance` (nilai polos saja, konsisten pola "regression check standar" — fokus suite ini ke tema barunya sendiri, bukan mengulang bug currency/debit_total yang sudah tercatat di suite manufaktur) | 21 akun sisanya    |

**Saldo awal yang dipakai (per 2026-01-01, IDR):**

### Aset Lancar

| Akun                                     | Saldo Awal (IDR) | Jalur                        |
| ---------------------------------------- | ---------------: | ---------------------------- |
| 1101 Kas Kecil Operasional RS            |       25.000.000 | `chart-of-accounts-balances` |
| 1102 Bank BCA Operasional (Umum)         |    3.500.000.000 | `finance/bank-accounts`      |
| 1103 Bank Mandiri — Rekening Khusus BPJS |    1.200.000.000 | `finance/bank-accounts`      |
| 1104 Piutang Pasien Umum                 |      180.000.000 | `chart-of-accounts-balances` |
| 1105 Piutang Klaim BPJS Kesehatan        |    2.450.000.000 | `chart-of-accounts-balances` |
| 1106 Piutang Klaim Asuransi Swasta       |      620.000.000 | `chart-of-accounts-balances` |
| 1107 Persediaan Obat, Alkes & BMHP       |      950.000.000 | `chart-of-accounts-balances` |
| 1108 PPN Masukan                         |       45.000.000 | `chart-of-accounts-balances` |

Total Aset Lancar = **8.970.000.000**

### Aset Tetap (gross & akumulasi penyusutan terpisah — WAJIB 2 posting per aset)

| Akun                                          |   Saldo Awal (IDR) | Jalur                        |
| --------------------------------------------- | -----------------: | ---------------------------- |
| 1201 Gedung Rumah Sakit (gross)               |     40.000.000.000 | `chart-of-accounts-balances` |
| 1202 Akumulasi Penyusutan Gedung              | 8.000.000.000 (Cr) | `chart-of-accounts-balances` |
| 1203 Mesin CT-Scan (gross)                    |     12.000.000.000 | `chart-of-accounts-balances` |
| 1204 Akumulasi Penyusutan Mesin CT-Scan       | 4.000.000.000 (Cr) | `chart-of-accounts-balances` |
| 1205 Mesin MRI (gross)                        |     18.000.000.000 | `chart-of-accounts-balances` |
| 1206 Akumulasi Penyusutan Mesin MRI           | 3.000.000.000 (Cr) | `chart-of-accounts-balances` |
| 1207 Peralatan Radiologi (X-Ray & USG, gross) |      5.000.000.000 | `chart-of-accounts-balances` |
| 1208 Akumulasi Penyusutan Peralatan Radiologi | 2.000.000.000 (Cr) | `chart-of-accounts-balances` |

Gross Aset Tetap = 75.000.000.000, Akumulasi = 17.000.000.000, **Net Aset Tetap = 58.000.000.000**

### Liabilitas Jangka Pendek & Panjang

| Akun                                             | Saldo Awal (IDR) | Jalur                        |
| ------------------------------------------------ | ---------------: | ---------------------------- |
| 2101 Utang Dagang — Supplier Farmasi & Alkes     |      780.000.000 | `chart-of-accounts-balances` |
| 2102 PPN Keluaran                                |       15.000.000 | `chart-of-accounts-balances` |
| 2103 Utang Fee Dokter Spesialis                  |    1.350.000.000 | `chart-of-accounts-balances` |
| 2104 Utang Gaji Karyawan Tetap                   |      420.000.000 | `chart-of-accounts-balances` |
| 2105 Utang PPh 21 Karyawan                       |       95.000.000 | `chart-of-accounts-balances` |
| 2106 Uang Muka Pasien Rawat Inap                 |      210.000.000 | `chart-of-accounts-balances` |
| 2201 Utang Bank Jangka Panjang — Ekspansi Gedung |   15.000.000.000 | `chart-of-accounts-balances` |

Total Liabilitas Jangka Pendek = 2.870.000.000, Jangka Panjang = 15.000.000.000, **Total Liabilitas = 17.870.000.000**

**Perhitungan manual (WAJIB cocok persis dengan hasil Trial Balance di §9.4 dan file 02):**

```
Total Aset       = 8.970.000.000 (lancar) + 58.000.000.000 (tetap, net)
                  = 66.970.000.000
Total Liabilitas = 2.870.000.000 (pendek) + 15.000.000.000 (panjang)
                  = 17.870.000.000
Modal Pemilik (3101) = Total Aset − Total Liabilitas
                      = 66.970.000.000 − 17.870.000.000
                      = 49.100.000.000  (KREDIT)
```

### 9.1 Guard — coba isi saldo awal SEBELUM akun equity ber-flag ada

| Skenario | Detail                                                                                                                                                                           | Hasil                                                                  |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Negatif  | Pastikan dulu BELUM ada akun ber-flag `is_opening_balance_equity_account:true`, lalu `POST .../create {chart_of_account_id:<1101>, currency_id:<IDR>, opening_balance:25000000}` | Ditolak `no_opening_balance_equity_account_configured_for_this_branch` |
| Negatif  | `chart_of_account_id` menunjuk akun `balance_required:false` (mis. 4101)                                                                                                         | Ditolak, pesan sejenis "This COA does not require a balance record."   |

### 9.2 Flag Modal Pemilik jadi akun offset saldo awal

| Skenario | Payload                                                                                          | Hasil                                                |
| -------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Positif  | `PUT client-master/chart-of-accounts/update {id:<3101>, is_opening_balance_equity_account:true}` | 200, `GET .../show` akun 3101 konfirmasi flag `true` |

### 9.3 Saldo Awal Bank — 2 rekening sekaligus (**Bank Accounts**)

| Skenario                                                      | Payload                                                                                                                                                                                                             | Hasil                                                                                                                                                                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif — Bank BCA Operasional                                | `POST finance/bank-accounts/create {account_name:"BCA Operasional RS", bank_name:"Bank Central Asia", account_number:"7710099887", currency_id:<IDR>, chart_of_account_id:<1102>, opening_balance:3500000000}`      | 201 — jurnal `JRN-OB-*`: Dr 1102 3.500.000.000 / Cr 3101 3.500.000.000, status `JRN_POSTED`                                                                                                            |
| **Positif — Bank Mandiri Khusus BPJS (kasus unik suite ini)** | `POST finance/bank-accounts/create {account_name:"Mandiri Rekening Khusus BPJS", bank_name:"Bank Mandiri", account_number:"1330077665", currency_id:<IDR>, chart_of_account_id:<1103>, opening_balance:1200000000}` | 201 — jurnal `JRN-OB-*`: Dr 1103 1.200.000.000 / Cr 3101 1.200.000.000 — dua bank account TERPISAH dites sekaligus di 1 file, belum pernah dites di suite lain (semua suite lain cuma 1 rekening bank) |
| Netralisasi                                                   | Simpan KEDUA bank account ini — dipakai file `07-rekonsiliasi-bank-multi-rekening-dan-ppn.id.md` — JANGAN dihapus sampai file itu selesai                                                                           |

### 9.4 Saldo Awal via Chart of Account Balances — 21 akun sisanya

| Skenario                                                              | Payload                                                                                     | Hasil                                                                                             |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Positif — Kas Kecil                                                   | `POST .../create {chart_of_account_id:<1101>, currency_id:<IDR>, opening_balance:25000000}` | Dr 1101 / Cr 3101, 25.000.000                                                                     |
| Positif — Piutang Pasien Umum                                         | sama, `chart_of_account_id:<1104>, opening_balance:180000000`                               | Dr 1104 / Cr 3101, 180.000.000                                                                    |
| Positif — Piutang BPJS                                                | sama, `chart_of_account_id:<1105>, opening_balance:2450000000`                              | Dr 1105 / Cr 3101, 2.450.000.000                                                                  |
| Positif — Piutang Asuransi Swasta                                     | sama, `chart_of_account_id:<1106>, opening_balance:620000000`                               | Dr 1106 / Cr 3101, 620.000.000                                                                    |
| Positif — Persediaan Obat/Alkes/BMHP                                  | sama, `chart_of_account_id:<1107>, opening_balance:950000000`                               | Dr 1107 / Cr 3101, 950.000.000                                                                    |
| Positif — PPN Masukan                                                 | sama, `chart_of_account_id:<1108>, opening_balance:45000000`                                | Dr 1108 / Cr 3101, 45.000.000                                                                     |
| Positif — Gedung (gross)                                              | sama, `chart_of_account_id:<1201>, opening_balance:40000000000`                             | Dr 1201 / Cr 3101, 40.000.000.000                                                                 |
| **Positif — Akumulasi Penyusutan Gedung (kontra)**                    | sama, `chart_of_account_id:<1202>, opening_balance:8000000000`                              | **Arah kebalikan** (akun kontra-aset, `normal_balance` kredit) — Cr 1202 / Dr 3101, 8.000.000.000 |
| Positif — Mesin CT-Scan (gross)                                       | sama, `chart_of_account_id:<1203>, opening_balance:12000000000`                             | Dr 1203 / Cr 3101, 12.000.000.000                                                                 |
| Positif — Akumulasi Penyusutan CT-Scan                                | sama, `chart_of_account_id:<1204>, opening_balance:4000000000`                              | Cr 1204 / Dr 3101, 4.000.000.000                                                                  |
| Positif — Mesin MRI (gross)                                           | sama, `chart_of_account_id:<1205>, opening_balance:18000000000`                             | Dr 1205 / Cr 3101, 18.000.000.000                                                                 |
| Positif — Akumulasi Penyusutan MRI                                    | sama, `chart_of_account_id:<1206>, opening_balance:3000000000`                              | Cr 1206 / Dr 3101, 3.000.000.000                                                                  |
| Positif — Peralatan Radiologi (gross)                                 | sama, `chart_of_account_id:<1207>, opening_balance:5000000000`                              | Dr 1207 / Cr 3101, 5.000.000.000                                                                  |
| Positif — Akumulasi Penyusutan Radiologi                              | sama, `chart_of_account_id:<1208>, opening_balance:2000000000`                              | Cr 1208 / Dr 3101, 2.000.000.000                                                                  |
| Positif — Utang Dagang Supplier (liability)                           | sama, `chart_of_account_id:<2101>, opening_balance:780000000`                               | Cr 2101 / Dr 3101, 780.000.000                                                                    |
| Positif — PPN Keluaran                                                | sama, `chart_of_account_id:<2102>, opening_balance:15000000`                                | Cr 2102 / Dr 3101, 15.000.000                                                                     |
| Positif — Utang Fee Dokter Spesialis                                  | sama, `chart_of_account_id:<2103>, opening_balance:1350000000`                              | Cr 2103 / Dr 3101, 1.350.000.000                                                                  |
| Positif — Utang Gaji Karyawan Tetap                                   | sama, `chart_of_account_id:<2104>, opening_balance:420000000`                               | Cr 2104 / Dr 3101, 420.000.000                                                                    |
| Positif — Utang PPh 21 Karyawan                                       | sama, `chart_of_account_id:<2105>, opening_balance:95000000`                                | Cr 2105 / Dr 3101, 95.000.000                                                                     |
| Positif — Uang Muka Pasien Rawat Inap                                 | sama, `chart_of_account_id:<2106>, opening_balance:210000000`                               | Cr 2106 / Dr 3101, 210.000.000                                                                    |
| **Positif — Utang Bank Jangka Panjang (nilai terbesar di suite ini)** | sama, `chart_of_account_id:<2201>, opening_balance:15000000000`                             | Cr 2201 / Dr 3101, 15.000.000.000                                                                 |
| Negatif                                                               | `opening_balance` sebagai string bukan angka, atau `currency_id` yang tidak ada             | 422                                                                                               |
| Negatif                                                               | `chart_of_account_id` dari branch lain                                                      | 422 `not_found_in_branch`                                                                         |

### 9.5 Verifikasi ke General Ledger / Trial Balance

| Skenario | Detail                                                                               | Hasil                                                                                                                                                                             |
| -------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/trial-balance` setelah §9.3+9.4 lengkap (23 posting) | `total_debit = total_credit` (balanced). Saldo 3101 Modal Pemilik = **kredit 49.100.000.000** persis (lihat perhitungan manual di atas)                                           |
| Positif  | Cek `accounting/journals/list` filter kode `JRN-OB-*`                                | Total **23 jurnal** (21 dari §9.4 + 2 dari §9.3), semua `status:JRN_POSTED`, `is_reversed:false` — jumlah jurnal opening balance terbanyak dari seluruh suite Accounting yang ada |

## Ringkasan Data Master yang Harus Sudah Ada Sebelum Lanjut ke File 01

- [ ] Currency IDR
- [ ] 7 Chart of Account Type (termasuk `LJPJ` — Liabilitas Jangka Panjang, baru di suite ini)
- [ ] 51 Chart of Accounts (§3), flag tersimpan benar — termasuk PPN yang SELEKTIF hanya di 4111/1108/2102
- [ ] Fiscal Year FY2026 + 12 periode **BULANAN**
- [ ] 4 Business Unit (RI, RJ, FAR, PJG) — dimensi DEPARTEMEN, bukan cabang lokasi
- [ ] Tax PPN 11%
- [ ] ~~Contact~~ — **DI-SKIP** (§8, tidak dibutuhkan modul Accounting murni)
- [ ] Saldo awal 23 posting terposting (21 chart-of-accounts-balances + 2 bank-accounts) — Modal Pemilik final **49.100.000.000**, Trial Balance balanced

## Referensi Silang

- [`../accounting-klinik-gigi/00-profil-perusahaan-dan-master-data.id.md`](../accounting-klinik-gigi/00-profil-perusahaan-dan-master-data.id.md) — pola PPN selektif per akun yang direplikasi filosofinya (bukan datanya) di suite ini
- [`../accounting-manufaktur/00-profil-perusahaan-dan-master-data.id.md`](../accounting-manufaktur/00-profil-perusahaan-dan-master-data.id.md) — pola pinjaman bank & cicilan pokok+bunga yang direplikasi di skala lebih besar
- `App\Services\JournalPostingService::syncOpeningBalance()` — implementasi posting saldo awal, sama seperti suite lain
- `App\Http\Controllers\ClientMaster\AccountingPeriod.php` — validasi `duration_type` mendukung `monthly,quarterly,weekly`
- `fixed-assets/assets/*`, `fixed-assets/disposals/*` — endpoint aset tetap yang BENAR (bukan `finance/fixed-assets/*`), dipakai file 06
