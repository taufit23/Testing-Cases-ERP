---
title: (Klinik Umum Besar) — 00. Profil Perusahaan & Master Data
category: accounting-klinik-umum
description: Skenario baru berdiri sendiri — PT Graha Medika Sentosa (Klinik Graha Medika), jaringan klinik umum rawat jalan skala besar 6 cabang lintas kota dengan kapitasi BPJS FKTP, MCU korporat B2B, farmasi/apotek, dan payroll dokter tetap vs paruh waktu. Fondasi seluruh file di folder ini, TIDAK terhubung ke suite testing/accounting/, testing/accounting-manufaktur/, testing/accounting-fnb-kafe/, testing/accounting-klinik-gigi/, maupun suite rumah sakit yang dibuat terpisah.
visibility: internal
---

# 00. Profil Perusahaan & Master Data

> **Suite ini berdiri SENDIRI**, terpisah total dari [`../accounting/`](../accounting/) (retail), [`../accounting-manufaktur/`](../accounting-manufaktur/) & [`../accounting-manufaktur-2/`](../accounting-manufaktur-2/) (manufaktur), [`../accounting-fnb-kafe/`](../accounting-fnb-kafe/) (kafe), dan [`../accounting-klinik-gigi/`](../accounting-klinik-gigi/) (klinik gigi kecil spesialisasi tunggal, periode mingguan). Suite ini JUGA berbeda dari suite "rumah sakit besar" yang sedang dibuat terpisah (rawat inap, ICU, alat medis besar, klaim BPJS per-kasus) — fokus suite ini murni **klinik umum rawat jalan skala besar/jaringan** (BUKAN rumah sakit), dengan ciri BPJS **kapitasi FKTP bulanan** (bukan klaim per-kasus), lab sederhana in-house, dan apotek klinik. Jangan campur data/kode akun antar suite mana pun.
>
> **Kenapa klinik umum besar, bukan klinik gigi/rumah sakit**: dipilih spesifik untuk menguji kombinasi kasus yang belum tersentuh suite mana pun — **pendapatan kapitasi BPJS FKTP** (tarif flat per peserta terdaftar per bulan, TIDAK bergantung jumlah kunjungan aktual — logika akuntansi 180° berbeda dari fee-for-service atau klaim per-kasus rumah sakit), **piutang korporat B2B untuk MCU (Medical Check-Up) karyawan** dengan termin pembayaran (beda karakter dari piutang BPJS), dan **payroll dua pola sekaligus** — dokter umum tetap (gaji flat bulanan) vs dokter spesialis paruh waktu (fee per kunjungan, akrual liability lalu dibayar periodik). Kombinasi ini didesain untuk menguji **akurasi pengakuan pendapatan kapitasi** (revenue harus tetap flat walau jumlah kunjungan aktual naik/turun) — titik uji paling penting di suite ini.
>
> **Pola tiap skenario**: **Positif** (jalur normal, harus sukses dengan nilai output PERSIS seperti yang tertera) / **Negatif** (input/urutan salah, harus DITOLAK dengan pesan jelas) / **Netralisasi** (cara mengembalikan state ke semula). Kolom **Label temuan** (🆕 fitur baru/gap desain, 🔧 improvement kecil, ✅ sudah tercover) dipakai HANYA kalau ada indikasi kuat dari pembacaan kode — kalau tidak sempat diverifikasi ke kode sungguhan, ditulis eksplisit **"belum diverifikasi ke kode"**, BUKAN diklaim sebagai bug pasti.
>
> **Kerjakan urutan file**: 00 → 01 → 02 → 03 → 04 → 05 → 06. Tiap file mengasumsikan file sebelumnya sudah dikerjakan — angka-angka di seluruh suite ini SALING TERKAIT (satu sumber kebenaran, sudah diverifikasi manual 2 arah: penjumlahan per transaksi DAN akumulasi net per akun, lihat §9), jangan lompat urutan.
>
> **Catatan endpoint Fixed Assets (penting)**: endpoint yang BENAR di project ini adalah **Assets — `{action}`** dan **Disposals — `{action}`** — BUKAN `finance/fixed-assets/*`. Seluruh referensi endpoint aset tetap di suite ini (file 05) sudah pakai path yang benar sejak awal.

## Profil Perusahaan (Skenario, FIKTIF)

**PT Graha Medika Sentosa**, beroperasi dengan merek **Klinik Graha Medika** — jaringan klinik umum rawat jalan swasta skala besar dengan **6 cabang lintas kota** di area Jabodetabek + Bandung, melayani poli umum, poli anak, poli kandungan (obgyn dasar), dan **Medical Check-Up (MCU)** korporat, dilengkapi **laboratorium sederhana in-house** (darah rutin, urine, gula darah) dan **apotek/farmasi klinik** (obat generik, obat paten, produk kesehatan ritel). **Sudah PKP** (omzet gabungan 6 cabang dari farmasi & produk ritel melewati ambang batas PKP), namun PPN 11% dipungut **SELEKTIF**: jasa medis (kapitasi, konsultasi umum, MCU, laboratorium) dan obat-obatan (termasuk kategori barang kena pajak tertentu yang dibebaskan PPN sesuai ketentuan umum barang strategis) **DIBEBASKAN PPN**, sementara **produk kesehatan non-obat ritel** (vitamin/suplemen OTC, alat kesehatan ritel seperti termometer/tensimeter rumahan) **DIKENAKAN PPN 11%**. Pola ini serupa tema "PPN selektif per akun" di suite klinik gigi, tapi diterapkan ke kasus berbeda (produk kesehatan non-obat, bukan produk perawatan gigi) — sengaja diulang temanya karena representatif untuk hampir semua bisnis jasa kesehatan campuran di Indonesia.

Enam cabang dijadikan dimensi Business Unit:

- **Klinik Graha Medika Jakarta Pusat** (JKP) — cabang flagship, volume peserta BPJS terbesar, pusat MCU korporat & lab rujukan internal.
- **Klinik Graha Medika Bekasi** (BKS) — cabang kedua, area padat penduduk.
- **Klinik Graha Medika Tangerang** (TGR) — cabang ketiga.
- **Klinik Graha Medika Depok** (DPK) — cabang keempat.
- **Klinik Graha Medika Bogor** (BGR) — cabang kelima.
- **Klinik Graha Medika Bandung** (BDG) — cabang keenam, dibuka pertengahan 2025, masih kecil (dipakai file 05 untuk kasus under-budget cabang baru).

Ciri yang membedakan dari suite lain (sengaja, supaya menguji jalur kode/kasus yang belum pernah disentuh):

1. **Pendapatan kapitasi BPJS Kesehatan tingkat FKTP** — diakui **flat per bulan = jumlah peserta terdaftar × tarif kapitasi per peserta**, TIDAK dikoreksi naik/turun oleh jumlah kunjungan aktual pasien pada bulan berjalan. Ini titik uji akurasi paling penting suite ini: kalau ERP/staf keliru mengikat pendapatan kapitasi ke volume kunjungan (pola fee-for-service), angkanya PASTI salah. Riset singkat: skema kapitasi FKTP BPJS Kesehatan di Indonesia memang membayar puskesmas/klinik/dokter praktik mitra berdasarkan jumlah peserta terdaftar per bulan (bukan per kunjungan) — FKTP menanggung risiko biaya pelayanan (jumlah kunjungan tinggi = margin klinik menipis, kunjungan rendah = margin lebih besar), berbeda total dari klaim INA-CBG rumah sakit yang dibayar per kasus/episode rawat inap.
2. **Dua bank berbeda untuk 2 arus kas berbeda** — 1102 Bank Mandiri Operasional (kas operasional harian) dan 1103 Bank BCA Penampungan Kapitasi BPJS (rekening khusus penampungan dana transfer BPJS, baru dipindahkan ke operasional secara periodik) — belum pernah dites pola "2 bank dengan fungsi berbeda dalam 1 entitas" di suite manapun.
3. **Piutang jasa dipecah 2 karakter berbeda**: 1104 Piutang Kapitasi BPJS (pencairan bulanan, sering ada lag/parsial) TERPISAH dari 1105 Piutang MCU Korporat & Asuransi Swasta (piutang dagang B2B biasa dengan termin pembayaran, mirip AR dagang biasa) — desain ini WAJIB dipisah supaya laporan aging/analisa piutang tidak mencampur 2 karakter risiko berbeda.
4. **Payroll dua pola sekaligus**: 2103/5101 (Gaji Dokter Umum Tetap — flat bulanan, mirip gaji karyawan biasa) vs 2104/5102 (Fee Dokter Spesialis Paruh Waktu — akrual liability dihitung dari `jumlah kunjungan × tarif fee per kunjungan`, baru jadi kas keluar saat dibayarkan) — kombinasi payroll tetap+variable dalam 1 entitas belum pernah dites lengkap sebelumnya.
5. **Farmasi/apotek klinik dengan 2 kategori persediaan** (1106 Obat Generik & Paten — dijual bebas PPN, 1107 BHP Medis & Lab — dipakai internal jadi beban HPP) dan PPN Masukan hanya muncul dari pembelian alat kesehatan/BHP (bukan dari pembelian obat, yang notabene juga dibebaskan PPN di sisi beli) — kasus PPN Masukan selektif yang belum pernah dites (di suite gigi, PPN Masukan muncul dari SEMUA pembelian BHP; di sini HANYA dari kategori tertentu).
6. **Aset kesehatan menengah** — Peralatan Medis & Lab (USG portable, alat lab sederhana, EKG — garis lurus) dan Kendaraan Ambulans Klinik (saldo menurun) — skala "menengah" sesuai arahan (klinik umum besar, BUKAN rumah sakit dengan alat radiologi/CT-Scan besar).

Tahun buku: **FY2026** (2026-01-01 s/d 2026-12-31), kalender. Mata uang operasional: **IDR** saja (tidak ada transaksi valas — sudah dites lengkap di suite manufaktur).

**Periode akuntansi: BULANAN** (`duration_type:"monthly"`). Catatan pemilihan: kode `AccountingPeriod` hanya mendukung 3 tipe (`monthly`, `quarterly`, `weekly`) dan ketiganya sudah pernah dites (bulanan di suite retail & F&B kafe, kuartalan di suite manufaktur, mingguan di suite klinik gigi) — tidak ada opsi ke-4 yang benar-benar baru. **Bulanan dipilih secara sengaja** (bukan asal reuse) karena paling merepresentasikan siklus bisnis nyata klinik jaringan besar: kapitasi BPJS dibayarkan **bulanan** oleh BPJS Kesehatan, sehingga siklus tutup buku bulanan selaras persis dengan siklus pengakuan pendapatan utama entitas ini — beda alasan dari suite retail/F&B yang pakai bulanan karena itu default umum.

> **Simplifikasi yang disengaja** (supaya file 03 Tutup Tahun Fiskal bisa langsung didemonstrasikan tanpa menunggu 12 bulan penuh): SELURUH transaksi jurnal manual inti di suite ini sengaja dikumpulkan di **bulan Januari 2026** — Februari 2026 dipakai HANYA untuk transaksi lanjutan non-inti (akuisisi aset tetap file 05, rekonsiliasi bank file 06) yang sengaja ditanggal SETELAH periode Januari ditutup, supaya Trial Balance/Neraca Januari yang sudah diverifikasi di file 02/04 TIDAK berubah retroaktif. Bulan Maret dst sengaja dibiarkan kosong. Ini bukan keterbatasan sistem, murni strategi supaya file 03 §Close Fiscal Year bisa didemonstrasikan (ditolak, karena 11 periode lain masih terbuka) tanpa harus mengisi 12 bulan penuh.

## 1. Currency (**Currencies**)

| Skenario    | Payload                                                      | Hasil                                          |
| ----------- | ------------------------------------------------------------ | ---------------------------------------------- |
| Positif     | Pastikan `IDR` sudah ada (base, biasanya ter-seed dari Core) | Tersedia di `client-master/currencies/options` |
| Netralisasi | — (master global, jangan dihapus)                            |

## 2. Chart of Account Type (**Chart of Account Type**)

Sama struktur generik dengan suite lain — kalau branch test ini share instance, boleh reuse, tidak perlu dibuat ulang:

| #   | Kode | Nama                     | `category` | `normal_balance` | `cash_flow_section` | Grup Laporan (`report_group`) |
| --- | ---- | ------------------------ | ---------- | ---------------- | ------------------- | ----------------------------- |
| 1   | AL   | Aset Lancar              | asset      | debit            | operating           | Balance Sheet                 |
| 2   | AT   | Aset Tetap               | asset      | debit            | investing           | Balance Sheet                 |
| 3   | LJP  | Liabilitas Jangka Pendek | liability  | credit           | operating           | Balance Sheet                 |
| 4   | EK   | Ekuitas                  | equity     | credit           | financing           | Balance Sheet                 |
| 5   | PD   | Pendapatan               | revenue    | credit           | operating           | Income Statement              |
| 6   | BB   | Beban                    | expense    | debit            | operating           | Income Statement              |

Kalau branch test ini TERPISAH (direkomendasikan supaya benar-benar independen dari suite lain), create ke-6 tipe ini dari 0 — validasi sama persis seperti [`../accounting/00-profil-perusahaan-dan-master-data.id.md`](../accounting/00-profil-perusahaan-dan-master-data.id.md) §2, tidak diulang di sini.

## 3. Chart of Accounts (**Chart of Accounts**)

**35 akun**, kode numerik 4-digit.

### Aset Lancar (11xx)

| Kode | Nama Akun                              | Flag khusus                                                                                                                       |
| ---- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1101 | Kas Kecil Klinik Pusat                 | `is_cash_account:true`, `balance_required:true` — kontrol kas kecil, disetor rutin ke bank (file 01)                              |
| 1102 | Bank Mandiri Operasional               | `is_cash_account:true` (saldo awal via `finance/bank-accounts`) — kas operasional harian                                          |
| 1103 | Bank BCA Penampungan Kapitasi BPJS     | `is_cash_account:true` (saldo awal via `finance/bank-accounts`) — rekening KHUSUS terima transfer BPJS, dipindah periodik ke 1102 |
| 1104 | Piutang Kapitasi BPJS Kesehatan (FKTP) | `is_ar_control_account:true`, `balance_required:true` — TERPISAH dari 1105, karakter pencairan beda                               |
| 1105 | Piutang MCU Korporat & Asuransi Swasta | `is_ar_control_account:true`, `balance_required:true` — piutang dagang B2B biasa, termin pembayaran                               |
| 1106 | Persediaan Obat (Generik & Paten)      | `balance_required:true` — dijual di apotek klinik, bebas PPN                                                                      |
| 1107 | Persediaan BHP Medis & Lab             | `balance_required:true` — dipakai internal tindakan/lab, jadi beban HPP                                                           |
| 1108 | PPN Masukan                            | `is_tax:true`, `tax_id:<PPN 11%>` — HANYA dari pembelian alat kesehatan/BHP kategori kena PPN                                     |

### Aset Tetap (12xx)

| Kode | Nama Akun                                  | Flag khusus                                                                                           |
| ---- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| 1201 | Peralatan Medis & Lab                      | — (USG portable, alat lab sederhana, EKG; dipakai file 05, garis lurus)                               |
| 1202 | Akumulasi Penyusutan Peralatan Medis & Lab | Kontra-aset, `normal_balance` tetap ikut tipe induk (debit), bersaldo negatif karena selalu di-kredit |
| 1203 | Kendaraan Ambulans Klinik                  | — (dipakai file 05, saldo menurun)                                                                    |
| 1204 | Akumulasi Penyusutan Kendaraan Ambulans    | Kontra-aset, sama pola dengan 1202                                                                    |

### Liabilitas Jangka Pendek (21xx)

| Kode | Nama Akun                                | Flag khusus                                                                               |
| ---- | ---------------------------------------- | ----------------------------------------------------------------------------------------- |
| 2101 | Utang Dagang — Distributor Farmasi/Alkes | `is_ap_control_account:true`, `balance_required:true`                                     |
| 2102 | PPN Keluaran                             | `is_tax:true`, `tax_id:<PPN 11%>` — HANYA dari penjualan produk kesehatan non-obat (4106) |
| 2103 | Utang Gaji Dokter Umum Tetap             | `balance_required:true` — akrual gaji tetap belum dibayar                                 |
| 2104 | Utang Fee Dokter Spesialis Paruh Waktu   | `balance_required:true` — akrual fee per kunjungan belum dibayar, akun kunci file 01      |
| 2105 | Utang Gaji Karyawan Non-Dokter           | `balance_required:true` — perawat, admin, apoteker, driver ambulans                       |
| 2106 | Utang PPh 21 Karyawan                    | `balance_required:true`                                                                   |

### Ekuitas (31xx)

| Kode | Nama Akun     | Flag khusus                                                                |
| ---- | ------------- | -------------------------------------------------------------------------- |
| 3101 | Modal Pemilik | `is_opening_balance_equity_account:true` — WAJIB tepat 1 akun ber-flag ini |
| 3102 | Laba Ditahan  | `is_retained_earnings_account:true` — WAJIB tepat 1 akun ber-flag ini      |

### Pendapatan (41xx)

| Kode | Nama Akun                                              | Catatan                                                                                                       |
| ---- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| 4101 | Pendapatan Kapitasi BPJS Kesehatan (FKTP)              | Bebas PPN (jasa medis) — **flat per peserta terdaftar**, TIDAK terikat kunjungan aktual, tema utama suite ini |
| 4102 | Pendapatan Jasa Non-Kapitasi / Fee-for-Service Umum    | Bebas PPN — pasien umum bayar langsung, asuransi swasta non-kapitasi                                          |
| 4103 | Pendapatan MCU Korporat                                | Bebas PPN — piutang B2B, termin pembayaran                                                                    |
| 4104 | Pendapatan Laboratorium                                | Bebas PPN — walk-in maupun bundel MCU                                                                         |
| 4105 | Pendapatan Penjualan Obat & Farmasi                    | Bebas PPN (obat kategori barang strategis)                                                                    |
| 4106 | Pendapatan Penjualan Produk Kesehatan Non-Obat (Ritel) | `tax_id:<PPN 11%>` di sisi jual — **satu-satunya lini kena PPN**, dites di file 06                            |

### Beban (51xx)

| Kode | Nama Akun                                                             | Catatan                                                                                 |
| ---- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 5101 | Beban Gaji Dokter Umum Tetap                                          | Lawan akrual 2103 — flat bulanan                                                        |
| 5102 | Beban Fee Dokter Spesialis Paruh Waktu                                | Lawan akrual 2104 — `jumlah kunjungan × tarif fee`, dites lengkap file 01               |
| 5103 | Beban Gaji Karyawan Non-Dokter                                        | Perawat, admin, apoteker, driver ambulans                                               |
| 5104 | Beban HPP Obat & BHP Medis Terpakai                                   | Beban langsung (bukan metode persediaan perpetual/FIFO — modul Inventory di luar scope) |
| 5105 | Beban Sewa Klinik/Gedung                                              | —                                                                                       |
| 5106 | Beban Listrik, Air & Internet                                         | —                                                                                       |
| 5107 | Beban Penyusutan Peralatan Medis & Lab                                | Dipakai file 05                                                                         |
| 5108 | Beban Penyusutan Kendaraan Ambulans                                   | Dipakai file 05                                                                         |
| 5109 | Beban Operasional Lain-lain (Sterilisasi, Limbah Medis & Selisih Kas) | Biaya rutin klinik (autoclave, limbah B3 medis) + selisih opname kas kecil              |

| Skenario                                                      | Detail                                                                                                                                             | Hasil                                                                                                                                                                 |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                       | Create ke-35 akun di atas (satu-satu atau `create-bulk`)                                                                                           | 201 semua, flag tersimpan **benar-benar** — `GET .../show` ulang untuk verifikasi, bukan cuma percaya response create (regression check konsisten dengan suite lain)  |
| Negatif                                                       | Create akun ke-2 ber-flag `is_opening_balance_equity_account:true`                                                                                 | Tidak ada validasi silang yang menolak (konsisten dengan temuan suite lain, belum diverifikasi ulang kodenya di sesi ini — anggap masih berlaku sampai ada perbaikan) |
| **Positif — kontra-aset**                                     | Setelah ada transaksi penyusutan (file 05) yang men-kredit 1202/1204, cek saldo di Trial Balance                                                   | Saldo harus **negatif** (mengurangi Aset Tetap), bukan ditambahkan positif                                                                                            |
| **Positif — PPN selektif per akun pendapatan (kasus unik)**   | Pastikan 4101/4102/4103/4104/4105 **TIDAK** diisi `tax_id` sama sekali, hanya 4106 yang diisi                                                      | Setelah file 06, cek `reports/tax-summary` — hanya transaksi yang menyentuh 4106 yang muncul sebagai basis PPN Keluaran                                               |
| **Positif — PPN Masukan selektif per pembelian (kasus baru)** | Pembelian obat (1106) TIDAK memicu PPN Masukan, HANYA pembelian BHP medis/alkes kategori kena PPN (1107, sebagian) yang memicu PPN Masukan di 1108 | Beda dari suite gigi di mana SEMUA pembelian BHP memicu PPN Masukan — di sini dipecah lebih granular per jenis barang, dites di file 01 §pembelian                    |
| Netralisasi                                                   | `delete` akun test yang belum dipakai transaksi                                                                                                    |

## 4. Fiscal Year (**Fiscal Year**)

| Skenario    | Payload                                                                                   | Hasil |
| ----------- | ----------------------------------------------------------------------------------------- | ----- |
| Positif     | `{code:"FY2026", name:"Tahun Buku 2026", start_date:"2026-01-01", end_date:"2026-12-31"}` | 201   |
| Netralisasi | `delete` — pastikan tidak ada `accounting_periods` di bawahnya                            |

## 5. Accounting Period — BULANAN (**Accounting Period**)

| Skenario                          | Detail                                                                                                        | Hasil                                                                                                                                                                                | Label temuan               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| Positif — generate bulanan        | `PUT client-master/fiscal-year/generate-accounting-period {fiscal_year_id:<FY2026>, duration_type:"monthly"}` | 12 periode ter-generate (Januari s/d Desember 2026), masing-masing sesuai jumlah hari kalender bulan itu (Januari 31 hari, Februari 28 hari di 2026 karena bukan tahun kabisat, dst) | ✅ kalau sesuai            |
| Positif — periode pertama presisi | Cek periode pertama                                                                                           | Harus `start_date:"2026-01-01"`, `end_date:"2026-01-31"` — inilah "Januari 2026" yang dipakai file 01-04                                                                             | ✅ kalau sesuai            |
| Positif — periode kedua presisi   | Cek periode kedua                                                                                             | Harus `start_date:"2026-02-01"`, `end_date:"2026-02-28"` (2026 bukan kabisat) — dipakai file 05-06 untuk transaksi lanjutan pasca-close Januari                                      | ✅ kalau sesuai            |
| Negatif                           | Generate lagi untuk fiscal year yang sama                                                                     | Ditolak/duplikat (tergantung guard — cek behavior aktual, sama seperti temuan suite lain)                                                                                            | Belum diverifikasi ke kode |
| Netralisasi                       | `delete` periode test satu-satu (pertimbangkan cuma hapus yang benar-benar dipakai testing: Jan & Feb)        |

## 6. Business Unit — Cabang Klinik (**Business Units**)

| Skenario                | Payload                                                                            | Hasil                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Positif — Jakarta Pusat | `{code:"JKP", name:"Klinik Graha Medika Jakarta Pusat", default_unit_type:"both"}` | 201 — cabang flagship, volume peserta BPJS terbesar, pusat MCU & lab rujukan             |
| Positif — Bekasi        | `{code:"BKS", name:"Klinik Graha Medika Bekasi", default_unit_type:"both"}`        | 201                                                                                      |
| Positif — Tangerang     | `{code:"TGR", name:"Klinik Graha Medika Tangerang", default_unit_type:"both"}`     | 201                                                                                      |
| Positif — Depok         | `{code:"DPK", name:"Klinik Graha Medika Depok", default_unit_type:"both"}`         | 201                                                                                      |
| Positif — Bogor         | `{code:"BGR", name:"Klinik Graha Medika Bogor", default_unit_type:"both"}`         | 201                                                                                      |
| Positif — Bandung       | `{code:"BDG", name:"Klinik Graha Medika Bandung", default_unit_type:"both"}`       | 201 — cabang termuda (dibuka pertengahan 2025), dipakai file 05 untuk kasus under-budget |
| Negatif                 | `default_unit_type` di luar enum (`cost/profit/both`)                              | 422                                                                                      |
| Netralisasi             | `delete` — pastikan tidak dipakai `journals.business_unit_id` manapun              |

## 7. Tax — PPN (**Taxes**)

| Skenario                             | Payload                                                                                                                                                                                                                                        | Hasil                                                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Positif                              | `{name:"PPN 11%", code:"PPN11", rate:11, effect:"increase"}`                                                                                                                                                                                   | 201 — dipasang selektif hanya di akun 4106 (pendapatan)/2102 (keluaran)/1108 (masukan), TIDAK di jasa medis atau obat (lihat §3) |
| **Catatan keterbatasan (bukan bug)** | Pajak final atas jasa dokter mitra (PPh 21/23 tergantung status kemitraan), pajak final UMKM, serta administrasi klaim kapitasi lewat aplikasi P-Care/BPJS TIDAK dimodelkan — suite ini hanya menguji PPN produk ritel & PPh 21 karyawan tetap | —                                                                                                                                |
| Netralisasi                          | `delete` — pastikan tidak dipakai                                                                                                                                                                                                              |

## 8. Contact (**Contacts**) — DI-SKIP, TIDAK DIPERLUKAN UNTUK SUITE INI

> **Keputusan sesi ini, konsisten dengan suite manufaktur/gigi**: suite ini fokus MURNI ke modul Accounting (jurnal manual, saldo awal, GL, laporan keuangan, tutup periode/tahun, anggaran, aset tetap, rekonsiliasi bank) — TIDAK menyentuh modul Purchasing/Sales sama sekali. `Contact` di project ini HANYA dipakai sebagai FK di dokumen `purchase_orders`/`sales_orders`/turunannya — dikonfirmasi tidak ada satupun endpoint accounting murni (`journals`, `chart-of-accounts-balances`, **Bank Accounts**, **Bank Reconciliations**, **Budgets**, **Assets**) yang mensyaratkan `contact_id`. "BPJS Kesehatan", nama distributor farmasi, dan nama perusahaan korporat MCU (mis. PT Nusantara Logistik Indonesia) di suite ini murni **nama/keterangan bebas di deskripsi baris jurnal** (field teks), BUKAN entitas `Contact` — piutang tetap 2 akun kontrol (1104, 1105), rincian per klaim/kontrak dilacak lewat deskripsi jurnal, bukan sub-ledger per debitur (di luar scope Accounting berdiri sendiri).

Section ini **SENGAJA DI-SKIP** — tidak perlu create Contact apapun untuk melanjutkan suite ini.

## 9. Saldo Awal / Opening Balance (**Chart of Accounts Balances**, **Bank Accounts**)

**⚠️ Bagian paling kritis di file ini — fondasi seluruh laporan keuangan di file berikutnya. Hitung dengan sangat teliti.** Mengikuti kontrak field yang sama dengan suite lain:

| Endpoint                                   | Field tersedia                                                                                                                                                                                                                             | Dipakai untuk akun                                         |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| `finance/bank-accounts`                    | `opening_balance` saja                                                                                                                                                                                                                     | 1102, 1103                                                 |
| `client-master/chart-of-accounts-balances` | `opening_balance` (nilai polos saja — `debit_total`/`credit_total` TIDAK dipakai, konsisten pola "regression check standar" seperti suite gigi/manufaktur, supaya suite ini fokus ke tema utamanya sendiri yaitu kapitasi & payroll ganda) | 1101, 1104, 1105, 1106, 1107, 2101, 2103, 2104, 2105, 2106 |

**Saldo awal yang dipakai** (total HARUS balance, dihitung manual di bawah):

| Akun                                          | Saldo Awal (IDR) | Jalur                        |
| --------------------------------------------- | ---------------: | ---------------------------- |
| 1101 Kas Kecil Klinik Pusat                   |       15.000.000 | `chart-of-accounts-balances` |
| 1102 Bank Mandiri Operasional                 |      480.000.000 | `finance/bank-accounts`      |
| 1103 Bank BCA Penampungan Kapitasi BPJS       |       95.000.000 | `finance/bank-accounts`      |
| 1104 Piutang Kapitasi BPJS Kesehatan (FKTP)   |      162.000.000 | `chart-of-accounts-balances` |
| 1105 Piutang MCU Korporat & Asuransi Swasta   |       87.500.000 | `chart-of-accounts-balances` |
| 1106 Persediaan Obat (Generik & Paten)        |      145.000.000 | `chart-of-accounts-balances` |
| 1107 Persediaan BHP Medis & Lab               |       58.750.000 | `chart-of-accounts-balances` |
| 2101 Utang Dagang — Distributor Farmasi/Alkes |       96.400.000 | `chart-of-accounts-balances` |
| 2103 Utang Gaji Dokter Umum Tetap             |       42.000.000 | `chart-of-accounts-balances` |
| 2104 Utang Fee Dokter Spesialis Paruh Waktu   |       28.600.000 | `chart-of-accounts-balances` |
| 2105 Utang Gaji Karyawan Non-Dokter           |       65.000.000 | `chart-of-accounts-balances` |
| 2106 Utang PPh 21 Karyawan                    |        9.750.000 | `chart-of-accounts-balances` |

**Perhitungan manual (WAJIB cocok persis dengan hasil Trial Balance di §9.4 dan file 02):**

```
Total Aset       = 15.000.000 + 480.000.000 + 95.000.000 + 162.000.000 + 87.500.000
                    + 145.000.000 + 58.750.000
                  = 1.043.250.000

Total Liabilitas = 96.400.000 + 42.000.000 + 28.600.000 + 65.000.000 + 9.750.000
                  = 241.750.000

Modal Pemilik (3101) = Total Aset − Total Liabilitas
                      = 1.043.250.000 − 241.750.000
                      = 801.500.000  (KREDIT)
```

### 9.1 Guard — coba isi saldo awal SEBELUM akun equity ber-flag ada

| Skenario | Detail                                                                                                                                                                           | Hasil                                                                                                    |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Negatif  | Pastikan dulu BELUM ada akun ber-flag `is_opening_balance_equity_account:true`, lalu `POST .../create {chart_of_account_id:<1101>, currency_id:<IDR>, opening_balance:15000000}` | Ditolak `no_opening_balance_equity_account_configured_for_this_branch` — bukan 500, bukan silent-success |
| Negatif  | `chart_of_account_id` menunjuk akun `balance_required:false` (mis. 4101)                                                                                                         | Ditolak, pesan sejenis "This COA does not require a balance record."                                     |

### 9.2 Flag Modal Pemilik jadi akun offset saldo awal

| Skenario | Payload                                                                                          | Hasil                                                |
| -------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Positif  | `PUT client-master/chart-of-accounts/update {id:<3101>, is_opening_balance_equity_account:true}` | 200, `GET .../show` akun 3101 konfirmasi flag `true` |

### 9.3 Saldo Awal Bank — Mandiri Operasional & BCA Penampungan Kapitasi (**Bank Accounts**)

| Skenario                       | Payload                                                                                                                                                                                                                    | Hasil                                                                                                                                                                          |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif — Bank Mandiri         | `POST finance/bank-accounts/create {account_name:"Mandiri Operasional Klinik", bank_name:"Bank Mandiri", account_number:"1210099887766", currency_id:<IDR>, chart_of_account_id:<1102>, opening_balance:480000000}`        | 201 — `opening_balance_journal_header_id` terisi, `accounting/journals/list` filter kode `JRN-OB-*` menunjukkan Dr 1102 480.000.000 / Cr 3101 480.000.000, status `JRN_POSTED` |
| Positif — Bank BCA Penampungan | `POST finance/bank-accounts/create {account_name:"BCA Penampungan Kapitasi BPJS", bank_name:"Bank Central Asia", account_number:"5570044556677", currency_id:<IDR>, chart_of_account_id:<1103>, opening_balance:95000000}` | 201 — Dr 1103 95.000.000 / Cr 3101 95.000.000, status `JRN_POSTED`                                                                                                             |
| Netralisasi                    | Simpan 2 bank account ini — dipakai file `05-anggaran-dan-aset-tetap.id.md` (akuisisi aset) dan `06-rekonsiliasi-bank-dan-ppn.id.md` (rekonsiliasi) — JANGAN dihapus sampai file itu selesai                               |

### 9.4 Saldo Awal via Chart of Account Balances — akun sisanya

| Skenario                                         | Payload                                                                                     | Hasil                                                                                                                           |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Positif — Kas Kecil Klinik Pusat                 | `POST .../create {chart_of_account_id:<1101>, currency_id:<IDR>, opening_balance:15000000}` | Dr 1101 / Cr 3101, 15.000.000                                                                                                   |
| Positif — Piutang Kapitasi BPJS                  | sama, `chart_of_account_id:<1104>, opening_balance:162000000`                               | Dr 1104 / Cr 3101, 162.000.000                                                                                                  |
| Positif — Piutang MCU Korporat & Asuransi Swasta | sama, `chart_of_account_id:<1105>, opening_balance:87500000`                                | Dr 1105 / Cr 3101, 87.500.000                                                                                                   |
| Positif — Persediaan Obat                        | sama, `chart_of_account_id:<1106>, opening_balance:145000000`                               | Dr 1106 / Cr 3101, 145.000.000                                                                                                  |
| Positif — Persediaan BHP Medis & Lab             | sama, `chart_of_account_id:<1107>, opening_balance:58750000`                                | Dr 1107 / Cr 3101, 58.750.000                                                                                                   |
| Positif — Utang Dagang Distributor (liability)   | sama, `chart_of_account_id:<2101>, opening_balance:96400000`                                | **Arah kebalikan** (`normal_balance` akun ini `credit`) — Cr 2101 / Dr 3101, 96.400.000 — jangan asumsi selalu Dr-akun/Cr-modal |
| Positif — Utang Gaji Dokter Umum Tetap           | sama, `chart_of_account_id:<2103>, opening_balance:42000000`                                | Cr 2103 / Dr 3101, 42.000.000                                                                                                   |
| Positif — Utang Fee Dokter Spesialis Paruh Waktu | sama, `chart_of_account_id:<2104>, opening_balance:28600000`                                | Cr 2104 / Dr 3101, 28.600.000                                                                                                   |
| Positif — Utang Gaji Karyawan Non-Dokter         | sama, `chart_of_account_id:<2105>, opening_balance:65000000`                                | Cr 2105 / Dr 3101, 65.000.000                                                                                                   |
| Positif — Utang PPh 21 Karyawan                  | sama, `chart_of_account_id:<2106>, opening_balance:9750000`                                 | Cr 2106 / Dr 3101, 9.750.000                                                                                                    |
| Negatif                                          | `opening_balance` sebagai string bukan angka, atau `currency_id` yang tidak ada             | 422                                                                                                                             |
| Negatif                                          | `chart_of_account_id` dari branch lain                                                      | 422 `not_found_in_branch`                                                                                                       |

### 9.5 Verifikasi ke General Ledger / Trial Balance

| Skenario | Detail                                                                  | Hasil                                                                                                                                                                           |
| -------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger/trial-balance` setelah §9.3+9.4 lengkap | `total_debit = total_credit` (balanced). Saldo 3101 Modal Pemilik = **kredit 801.500.000** persis (lihat perhitungan manual di atas) — kalau beda, ada entri salah arah/kelewat |
| Positif  | Cek `accounting/journals/list` filter kode `JRN-OB-*`                   | Total 12 jurnal (10 dari §9.4 + 2 dari §9.3), semua `status:JRN_POSTED`, `is_reversed:false`                                                                                    |

## Ringkasan Data Master yang Harus Sudah Ada Sebelum Lanjut ke File 01

- [ ] Currency IDR
- [ ] 6 Chart of Account Type
- [ ] 35 Chart of Accounts (§3), flag tersimpan benar — termasuk PPN Keluaran SELEKTIF hanya di 4106, PPN Masukan SELEKTIF hanya sebagian pembelian BHP/alkes
- [ ] Fiscal Year FY2026 + periode **BULANAN** (verifikasi periode 1 = 2026-01-01 s/d 2026-01-31, periode 2 = 2026-02-01 s/d 2026-02-28)
- [ ] 6 Business Unit (JKP, BKS, TGR, DPK, BGR, BDG)
- [ ] Tax PPN 11%
- [ ] ~~Contact~~ — **DI-SKIP** (§8, tidak dibutuhkan modul Accounting murni)
- [ ] Saldo awal 12 akun terposting (10 via `chart-of-accounts-balances` + 2 via `finance/bank-accounts`) — Modal Pemilik final **801.500.000**, Trial Balance balanced

## Referensi Silang

- [`../accounting-klinik-gigi/00-profil-perusahaan-dan-master-data.id.md`](../accounting-klinik-gigi/00-profil-perusahaan-dan-master-data.id.md) — suite klinik gigi (kecil, mingguan, spesialisasi tunggal), pola dasar tema "PPN selektif per akun" yang direplikasi ke kasus berbeda di sini
- [`../accounting-fnb-kafe/00-profil-perusahaan-dan-master-data.id.md`](../accounting-fnb-kafe/00-profil-perusahaan-dan-master-data.id.md) — pola dasar dimensi Business Unit sebagai profit center per cabang/outlet
- `App\Services\JournalPostingService::syncOpeningBalance()` — implementasi posting saldo awal, sama seperti suite lain
- `App\Http\Controllers\ClientMaster\AccountingPeriod.php` — validasi `duration_type` mendukung `monthly,quarterly,weekly`
- Endpoint Fixed Assets yang benar: `fixed-assets/assets/{action}` dan `fixed-assets/disposals/{action}` (dipakai file 05)
