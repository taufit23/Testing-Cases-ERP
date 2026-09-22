---
title: Ranahku — Pengujian Modul Lanjutan (Rental, Aset Tetap, Laporan, Akuntansi, Persediaan, Kanvasing, SDM, Administrasi)
description: Lanjutan pengujian setelah 01 (master data) dan 02 (alur transaksi inti) selesai. Berkas ini menguji modul-modul yang belum pernah tersentuh sama sekali oleh kedua berkas sebelumnya — hasil pemetaan menu lengkap aplikasi menunjukkan banyak modul (Rental, Fixed Assets, Reports, Accounting manual, Inventory lanjutan, Canvassing lanjutan, SDM lanjutan, Approval Requests, dan berbagai data pelengkap di Branch Management/Finance) belum pernah diuji.
---

# Ranahku — Pengujian Modul Lanjutan

> Disusun 2026-09-15 setelah peninjauan ulang menu aplikasi menemukan bahwa file `01` dan `02`
> hanya mencakup sebagian modul. Berkas ini melengkapi cakupan pengujian supaya semua modul utama
> pernah disentuh minimal sekali, sebagai bekal fase perbaikan bug berikutnya.

## Ringkasan Tahap

| #   | Tahap                                    | Modul                                                          |
| --- | ----------------------------------------- | --------------------------------------------------------------- |
| G   | Sewa Jangka Pendek (Rental)               | Rental Assets, Quotations, Orders, Invoices, Payment Bills, Returns, Usage Entries |
| H   | Aset Tetap (Fixed Assets)                 | Assets, Disposals                                                |
| I   | Akuntansi Manual & Laporan Keuangan       | Journals (manual), General Ledger, Budgets, 11 halaman Reports  |
| J   | Persediaan Lanjutan                       | Stock Takes, Stock Adjustments, Buffer Stock, Consignment Settlements, Stock Lots/Serials, Warehouse Supply Sources |
| K   | Kanvasing Lanjutan                        | Competitors, Sales Targets, Territories, Routes, Stock Custody, Collections |
| L   | SDM Lanjutan                              | Job Vacancies + Applications (rekrutmen), Shifts, Work Schedules, Employee Transfers, Attendance Statuses, Employment Types, Commission Rules/Commissions |
| M   | Approval Requests (alur approve sungguhan)| Approvals > Approval Requests                                    |
| N   | Finance & Administrasi Cabang             | Bank Reconciliations, Cost Centers, Roles/Permissions/Users, Discounts, Cashback Rules, Member Tiers, Expense Categories/Expenses, dan pelengkap lain |

---

## TAHAP G — Sewa Jangka Pendek (Rental)

**Konteks:** modul `Rental` terpisah dari produk "Layanan Sewa Aplikasi" yang dijual lewat modul
Sales (diuji di file 02 Tahap B). Rental adalah pencatatan sewa berbasis **Asset** dengan tarif
harian dan rentang tanggal — cocok untuk skenario "Sewa jangka pendek" di profil perusahaan
(pelanggan pakai perangkat demo/uji coba beberapa hari, dilayani meja sewa kantor oleh Intan
Permata).

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Master data | Dibuat 1 Rental Asset "Tablet Demo Aplikasi Ranahku" (RTL-001), tarif harian Rp 100.000, lewat Rental > Assets > Add Asset | Berhasil dibuat, status `available` |
| Config | `rental/rental-configs`: Journal Mode diubah ke **Auto** (semula Manual), **Require Rental Order Approval** dan **Require Rental Invoice Approval** diaktifkan untuk menguji alur approval | Tersimpan |
| Quotation | Dibuat Rental Quotation `QUO-R/2026/09/0001` untuk Bengkel Motor Laju Jaya, aset di atas, periode 16–20 September 2026 | Tersimpan, tapi lihat bug di bawah |
| Submit → Customer Accept → Convert to Order | Dijalankan lewat API langsung (karena halaman detail error, lihat bug) | Berhasil sampai terbentuk Rental Order `RNT/2026/09/0001` |
| Activate Order | Dicoba mengaktifkan Rental Order | **Gagal** — "Rental Not Draft" (bug status salah, lihat temuan) |
| Invoice, Payment Bill, Return, Usage Entries | Belum bisa diuji | **Terblokir** — order tidak pernah bisa mencapai status Aktif karena bug di atas |

> **Status Tahap G (2026-09-15): Terhambat bug tinggi sejak langkah awal.** Rental Asset dan
> Rental Quotation berhasil dibuat, tapi ditemukan tiga bug signifikan sekaligus: (1) halaman
> detail Rental Quotation selalu error server (bug tipe argumen fungsi `flexibleShow`), (2)
> jumlah hari sewa yang dihitung halaman (5 hari, inklusif) berbeda dari yang dihitung server
> (4 hari, eksklusif) sehingga nominal Rp 500.000 yang dilihat pengguna sebelum simpan tidak
> sama dengan Rp 400.000 yang benar-benar tersimpan, dan (3) bug paling serius: setiap Rental
> Order hasil Convert to Order selalu diberi status_id milik Rental Quotation (bukan miliknya
> sendiri) akibat salah pemanggilan fungsi di kode backend, sehingga Rental Order **macet
> permanen** dan tidak pernah bisa diaktifkan — memblokir seluruh pengujian lanjutan modul ini
> (Invoice, Payment Bill, Return, Usage Entries tidak sempat diuji sama sekali karena tidak ada
> Order yang bisa mencapai status Aktif). Detail lengkap di
> [`erpApiServices/docs/TemuanTestCase/Rental/Ranahku/01-order-sewa-baru-salah-status-macet-tidak-bisa-diaktifkan.id.md`](../../erpApiServices/docs/TemuanTestCase/Rental/Ranahku/01-order-sewa-baru-salah-status-macet-tidak-bisa-diaktifkan.id.md)
> dan
> [`erpApiServices/docs/TemuanTestCase/Rental/Ranahku/02-halaman-detail-quotation-error-dan-jumlah-hari-sewa-beda-dengan-server.id.md`](../../erpApiServices/docs/TemuanTestCase/Rental/Ranahku/02-halaman-detail-quotation-error-dan-jumlah-hari-sewa-beda-dengan-server.id.md).
> Catatan tambahan: teks modal "Add Asset" di Rental keliru menyebut "Fixed Asset" (seharusnya
> "Rental Asset") — bug kecil, kemungkinan salin-tempel dari modul Fixed Assets.
>
> **Untuk pengujian ulang setelah bug diperbaiki**: uji ulang Activate → Complete pada Rental
> Order baru, baru lanjutkan ke Rental Invoice (biasanya dibuat dari Order Aktif) → Payment Bill
> → Return (pengembalian aset di akhir masa sewa) → Usage Entries (jika ada pemakaian terukur).

---

## TAHAP H — Aset Tetap (Fixed Assets)

**Konteks:** modul untuk mencatat aset jangka panjang milik perusahaan (kendaraan, peralatan,
properti) beserta penyusutan nilainya dari waktu ke waktu, sampai akhirnya dijual/dibuang
(disposal). Belum pernah disentuh test case manapun sebelumnya.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Buat Asset | Dibuat "Mobil Box Operasional" (`FA/2026/0001`), kategori vehicle, akuisisi 1 September 2026 Rp 180.000.000, nilai residu Rp 20.000.000, umur manfaat 96 bulan, metode garis lurus, COA lengkap (Asset 1-202 / Beban Penyusutan 6-106 / Akumulasi Penyusutan 1-209) | Berhasil, kalkulasi estimasi penyusutan bulanan di halaman Create sudah benar |
| Run Depreciation | Dicoba jalankan penyusutan untuk beberapa tanggal (30 Sep, 15 Sep/hari ini, 31 Agustus) | **Gagal total** — selalu ditolak "Cannot Run Depreciation For A Future Period" untuk tanggal apa pun selain tanggal 1 bulan berjalan (bug logika perbandingan tanggal di FE), lihat temuan di bawah |
| Dispose Asset | Dicoba disposal aset lewat tombol **Dispose Asset**: tanggal 15 September 2026, metode Sold, Proceeds Rp 150.000.000 | **Berhasil** — status berubah jadi "Sold", Gain/Loss terhitung benar (Rp -30.000.000 = Proceeds − Book Value saat itu) |

> **Status Tahap H (2026-09-15): Fitur Run Depreciation tidak bisa dipakai sama sekali akibat bug
> logika tanggal, tapi fitur Create Asset dan Dispose Asset sudah berfungsi dengan benar.**
> Penyusutan bulanan — fitur inti modul ini — selalu ditolak dengan pesan "periode masa depan"
> untuk tanggal berapa pun sepanjang bulan kecuali tanggal 1, akibat perbandingan teks tanggal
> yang salah logika di kode frontend (`period_date > startOfThisMonth.value`, seharusnya
> membandingkan bulan-tahun, bukan tanggal lengkap terhadap tanggal 1). Dicek langsung ke server,
> `accumulated_depreciation` aset ini masih Rp 0 dan `current_book_value` masih sama dengan
> `acquisition_cost` — membuktikan penyusutan memang belum pernah benar-benar berjalan.
> Sebaliknya, Dispose Asset diuji terpisah dan berhasil sempurna: status, tanggal disposal,
> metode, proceeds, dan perhitungan Gain/Loss semuanya tampil benar (meski nilai Gain/Loss ini
> ikut terdampak tidak akurat secara bisnis karena Book Value yang dipakai belum pernah
> tersusutkan sama sekali — konsekuensi lanjutan dari bug Run Depreciation, bukan bug baru di
> Disposal itu sendiri). Detail lengkap di
> [`erpApiServices/docs/TemuanTestCase/FixedAssets/Ranahku/01-jalankan-penyusutan-selalu-ditolak-dianggap-periode-masa-depan.id.md`](../../erpApiServices/docs/TemuanTestCase/FixedAssets/Ranahku/01-jalankan-penyusutan-selalu-ditolak-dianggap-periode-masa-depan.id.md).
>
> **Untuk pengujian ulang setelah bug diperbaiki**: buat asset baru (yang ini sudah terlanjur
> berstatus Sold), uji Run Depreciation berkali-kali dengan tanggal berbeda dalam sebulan,
> pastikan jurnal otomatis terbentuk (jika Journal Mode Auto), lalu baru uji Disposal di akhir.

---

## TAHAP I — Akuntansi Manual & Laporan Keuangan

**Konteks:** menguji fitur jurnal manual (Create Journal), buku besar (General Ledger), anggaran
(Budgets), dan 10 halaman laporan di menu Reports — semuanya belum pernah disentuh test case
manapun sebelumnya.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Create Journal | Dicoba buat jurnal manual (Debit Kas Kecil / Kredit Peralatan & Perlengkapan Toko, Rp 500.000) | **Gagal total** — mata uang default salah (CNY, bukan IDR), dan disimpan pun ditolak "No Active Exchange Rate Found For This Currency" untuk mata uang apa pun termasuk IDR |
| General Ledger | Diuji tab Detail Ledger (all accounts & per-akun), Summary By Account, Trial Balance | Semua berfungsi baik, angka konsisten dan balance (Debit = Kredit) |
| Budgets | Dibuat "Anggaran Operasional Head Office September 2026" (akun 6-104 Beban Listrik, Rp 5.000.000), Activate, lalu Run Report Budget vs Actual | **Berhasil sempurna** — status Draft → Active, laporan Budget vs Actual menghitung Variance dengan benar (Rp -5.000.000, -100%, karena belum ada realisasi) |
| Reports — Balance Sheet, Cash Flow Statement, Income Statement, Ap Aging, Ar Aging, Pos Sales Summary, Stock Summary, Tax Summary, Sales Target Realization, Trial Balance, Child Branches | Dijalankan satu per satu | 9 dari 11 laporan berfungsi baik (termasuk Balance Sheet yang balanced dan Cash Flow yang reconciled); **Stock Summary** menampilkan nilai persediaan yang jauh lebih kecil dari Neraca (bug); **Child Branches** 404 (halaman tidak ada) |

> **Status Tahap I (2026-09-15): Fitur jurnal manual (Create Journal) tidak bisa dipakai sama
> sekali, tapi General Ledger, Budgets, dan mayoritas laporan keuangan sudah berfungsi baik.**
> Akar masalah Create Journal ada di data master: tabel Exchange Rates kosong total dan tidak ada
> satu pun mata uang (termasuk IDR, mata uang perusahaan sendiri) yang ditandai sebagai default —
> akibatnya sistem selalu meminta kurs aktif untuk mata uang apa pun, termasuk mata uang sendiri,
> dan jurnal manual tidak pernah bisa tersimpan. General Ledger (Detail Ledger, Summary By
> Account, Trial Balance) dan Budgets (create → activate → Budget vs Actual) sudah diuji lengkap
> dan berfungsi benar. Dari 11 laporan di menu Reports, ditemukan dua bug: **Stock Summary**
> menghitung Average Cost Rp 0 untuk mayoritas produk (kemungkinan besar stok dari proses Saldo
> Awal tidak ikut membuat cost layer), membuat Total Stock Value laporan ini jauh di bawah nilai
> persediaan sebenarnya di Neraca (Rp 9,6 Juta vs Rp 110 Juta); dan **Child Branches** mengarah ke
> halaman 404. Ditemukan juga bug lebih kecil yang berulang di banyak halaman: field tanggal
> default ("hari ini") di Create Journal, Balance Sheet, Cash Flow Statement, Ap Aging, dan Ar
> Aging semuanya mundur satu hari (dugaan bug UTC vs waktu lokal). Catatan tambahan: laporan Ap
> Aging dan Ar Aging sama-sama menampilkan peringatan "Gl Control Account Not Configured" — bukan
> bug, tapi gap konfigurasi data master (belum ada akun COA yang ditandai sebagai akun kontrol
> AP/AR) yang membuat fitur rekonsiliasi GL dari kedua laporan ini belum bisa dipakai. Detail
> lengkap di
> [`erpApiServices/docs/TemuanTestCase/Accounting/Ranahku/01-buat-jurnal-manual-selalu-gagal-tidak-ada-kurs-mata-uang.id.md`](../../erpApiServices/docs/TemuanTestCase/Accounting/Ranahku/01-buat-jurnal-manual-selalu-gagal-tidak-ada-kurs-mata-uang.id.md),
> [`02-laporan-ringkasan-stok-nilai-persediaan-jauh-lebih-kecil-dari-neraca.id.md`](../../erpApiServices/docs/TemuanTestCase/Accounting/Ranahku/02-laporan-ringkasan-stok-nilai-persediaan-jauh-lebih-kecil-dari-neraca.id.md),
> [`03-menu-laporan-child-branches-halaman-tidak-ditemukan.id.md`](../../erpApiServices/docs/TemuanTestCase/Accounting/Ranahku/03-menu-laporan-child-branches-halaman-tidak-ditemukan.id.md),
> dan
> [`04-tanggal-default-di-berbagai-halaman-mundur-satu-hari.id.md`](../../erpApiServices/docs/TemuanTestCase/Accounting/Ranahku/04-tanggal-default-di-berbagai-halaman-mundur-satu-hari.id.md).
>
> **Untuk pengujian ulang setelah bug diperbaiki**: isi seeder default currency + exchange rate
> IDR, lalu uji ulang Create Journal sampai benar-benar tersimpan dan tervalidasi silang ke
> General Ledger.

---

## TAHAP J — Persediaan Lanjutan

**Konteks:** menguji Stock Takes, Stock Adjustments, Buffer Stock, Consignment Settlements,
Stock Lots/Serials, dan Warehouse Supply Sources — semuanya belum pernah disentuh test case
manapun sebelumnya.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Stock Take | Dibuat Stock Take untuk Gudang Utama, satu produk (Minyak Goreng 2L) diisi hasil hitung 340 (sistem 350, variance -10), sisanya dibiarkan otomatis. Complete. | Variance tampil benar (-10) di halaman Stock Take, TAPI **stok sungguhan malah jadi 10** (bukan 340) setelah dicek Stock History — bug kritis |
| Stock Adjustments | Dicek data adjustment awal (`ADJ/2026/09/0001`, opening stock) via API | Ternyata sudah punya `unit_cost` yang benar per SKU — bukti kuat untuk revisi temuan Stock Summary di Tahap I |
| Buffer Stock | Dikonfigurasi Min/Max/Reorder Point untuk 1 SKU (Air Mineral Galon) via Bulk Edit, mode "Sku Wide Default All Warehouses" | Berhasil, status Available/At Minimum Stock terhitung benar di ketiga gudang |
| Warehouse Supply Sources | Ditambahkan 1 relasi (Gudang Toko Retail ← disuplai dari Gudang Utama) | Berhasil; catatan kecil: dropdown Supply Warehouse tidak mengecualikan warehouse yang sama dengan Store Warehouse yang dipilih (berpotensi membuat toko "mensuplai dirinya sendiri") |
| Stock Lots, Stock Serials, Consignment Settlements, Stock Adjustment Reasons, Config | Dicek halaman list & config | Semua halaman terbuka dan berfungsi baik; Stock Serials, Consignment Settlements, dan Stock Adjustment Reasons masih kosong (belum ada data uji terkait fitur lot/serial/consignment/reason di sesi sebelumnya) |

> **Status Tahap J (2026-09-15): Ditemukan bug KRITIS — menyelesaikan Stock Take yang menemukan
> selisih stok justru merusak jumlah stok sungguhan, bukan memperbaikinya.** Saat Stock Take untuk
> Minyak Goreng 2L (Gudang Utama) menemukan hasil hitung 340 dari sistem 350 (variance -10),
> sistem menerapkan pengurangan sebesar 340 (nilai hasil hitung itu sendiri) ke stok, bukan
> sebesar selisihnya (-10) — membuat stok yang seharusnya 340 malah menjadi 10. Halaman Stock Take
> sendiri menampilkan variance dengan benar, jadi bug ini baru terlihat setelah mengecek Stock
> History secara terpisah — artinya siapa pun yang memakai fitur ini secara normal untuk stock
> opname tidak akan sadar datanya rusak. Temuan ini juga menjelaskan lebih jauh bug Stock Summary
> di Tahap I: dicek langsung, Stock Adjustment awal (opening stock) TERNYATA sudah punya
> `unit_cost` yang benar per produk — jadi akar masalah Rp 0 di Stock Summary bukan data yang
> kosong, tapi murni bug perhitungan laporannya yang tidak membaca cost dari sumber Adjustment
> (catatan ini sudah diperbarui di file temuan Tahap I). Di luar itu, Buffer Stock dan Warehouse
> Supply Sources sudah diuji dan berfungsi baik. Detail lengkap di
> [`erpApiServices/docs/TemuanTestCase/Inventory/Ranahku/01-selesaikan-stock-take-merusak-jumlah-stok-sebenarnya.id.md`](../../erpApiServices/docs/TemuanTestCase/Inventory/Ranahku/01-selesaikan-stock-take-merusak-jumlah-stok-sebenarnya.id.md).
>
> **Untuk pengujian ulang setelah bug diperbaiki**: audit dan perbaiki stok Minyak Goreng 2L di
> Gudang Utama yang sudah terlanjur salah (10 → seharusnya 340), lalu uji ulang Stock Take dengan
> berbagai skenario variance sebelum dipakai untuk data produksi sungguhan. Lanjutkan juga
> pengujian Consignment Settlements dan Stock Serials begitu ada data konsinyasi/serial number
> yang bisa dipakai untuk skenario nyata.

---

## TAHAP K — Kanvasing Lanjutan

**Konteks:** menguji Competitors, Sales Targets, Territories, Routes, Stock Custody, dan
Collections — pelengkap modul Canvassing yang sudah diuji sebagian di file 01/02 (kunjungan dasar
dan konversi ke Sales Order), tapi belum pernah menyentuh fitur-fitur pendukungnya.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Competitors | Dibuat 1 data kompetitor "Toko Sembako Makmur Jaya" | Berhasil |
| Sales Territories | Dibuat "Wilayah Ciputat Raya" lengkap dengan titik & radius cakupan di peta (fitur Leaflet/OpenStreetMap) | Berhasil, tampilan peta & radius berfungsi baik |
| Sales Targets | Dibuat target Rp 10.000.000 untuk Wilayah Ciputat Raya, bulan September 2026 | Berhasil, langsung terhubung dengan benar ke laporan Sales Target Realization (Tahap I) — Target Rp 10.000.000, Realized Rp 0, 0% |
| Canvassing Routes, Sales Stock Custodies | Dicek halaman list | Keduanya kosong tapi terbuka normal, tidak diuji create karena butuh setup salesperson+territory lebih lanjut |
| Canvassing Field ("My Day") | Dibuka sebagai akun Taufit (owner/admin) | Muncul error "Your Account Is Not Linked To An Employee Record" — wajar karena akun Taufit bukan salesperson lapangan, bukan bug, tapi fitur ini butuh akun dengan Employee record untuk diuji penuh |
| Canvassing Visits | Dicek daftar 2 kunjungan yang sudah ada dari sesi sebelumnya | Data tersimpan benar, TAPI kolom Outcome menampilkan kunci terjemahan mentah "content.no_order" dan kolom Date menampilkan format ISO mentah, bukan tanggal terformat |
| Canvassing Collections | Dicek halaman list | Kosong tapi terbuka normal |

> **Status Tahap K (2026-09-15): Fitur inti (Competitors, Territories dengan peta, Sales Targets
> terhubung ke laporan realisasi) berfungsi baik.** Ditemukan satu bug tampilan di halaman
> Canvassing Visits: kolom Outcome menampilkan kunci terjemahan mentah `content.no_order`
> alih-alih teks yang sudah diterjemahkan, dan kolom Date menampilkan format ISO mentah
> (`2026-09-14T00:00:00.000000Z`) alih-alih tanggal terformat rapi. Detail di
> [`erpApiServices/docs/TemuanTestCase/Canvassing/Ranahku/01-daftar-canvassing-visits-tampilkan-kunci-terjemahan-dan-tanggal-mentah.id.md`](../../erpApiServices/docs/TemuanTestCase/Canvassing/Ranahku/01-daftar-canvassing-visits-tampilkan-kunci-terjemahan-dan-tanggal-mentah.id.md).
> Canvassing Routes, Sales Stock Custodies, dan Canvassing Collections belum sempat diuji penuh
> (create/transaksi) karena butuh setup salesperson dengan Employee record terlebih dahulu —
> disarankan dilanjutkan di sesi berikutnya dengan akun test khusus salesperson.

---

## TAHAP L — SDM Lanjutan

**Konteks:** melengkapi pengujian modul Human Resource Management dengan fitur-fitur yang belum
disentuh: rekrutmen (Job Vacancies + Applications), penjadwalan kerja (Shifts, Work Schedules),
mutasi karyawan antar cabang (Employee Transfers), master data pendukung absensi/kepegawaian
(Attendance Statuses, Employment Types), dan skema komisi (Commission Rules, Commissions).

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Job Vacancies | Dibuat lowongan "Staf Gudang Utama" (Departemen Toko Retail, Posisi Kasir) | Berhasil dibuat dan tampil di daftar |
| Applications | Ditambahkan lamaran "Fajar Ramadhan" untuk lowongan di atas lewat Add Application | Tersimpan dengan `job_vacancy_id` benar di server, TAPI halaman detail pelamar menampilkan field Job Vacancy kosong ("-") — bug tampilan FE |
| Shifts | Dicek data shift yang sudah ada (mis. "Shift Pagi Toko") | Berfungsi baik, dipakai sebagai referensi pola rotasi di Generate Roster |
| Work Schedules — Generate Roster | Digenerate roster untuk "Andi Saputra", pola 2 hari (Shift Pagi Toko / Day Off), rentang 31 Agustus – 29 September 2026 | Berhasil membuat 15 baris roster **di server** (dikonfirmasi lewat API), TAPI halaman Work Schedules (List maupun Calendar) tetap menampilkan "No Roster Entries For This Month" — bug tampilan/query FE |
| Employee Transfers | Dicoba membuat transfer "Andi Saputra" ke 3 pilihan yang tersedia di dropdown To Branch (Pusat, Kantor Utama, Apbatech Pusat) | **Ketiga-tiganya ditolak server** — dua dengan alasan beda company, satu lagi karena sama dengan cabang saat ini — fitur tidak bisa dipakai sama sekali untuk kasus ini |
| Attendance Statuses | Dicek 8 status bawaan (Hadir, Terlambat, Setengah Hari, Cuti, Sakit, Izin, Libur, Alpa), lalu ditambahkan 1 status baru "Kerja Dari Rumah" (wfh) | Data bawaan lengkap dan benar; status baru berhasil dibuat, cuma pesan toast setelah submit tertulis "Success Update" padahal aksinya Create (bug kecil, salah label pesan) |
| Employment Types | Dicek 9 jenis kepegawaian: 6 aktif berlabel Indonesia (PKWTT, PKWT, Harian Lepas, Borongan, Magang, Paruh Waktu) dan 3 tidak aktif berlabel Inggris (permanent, contract, freelance) | Wajar — data lama dinonaktifkan (bukan dihapus) saat diganti set data berlabel Indonesia, konsisten dengan kebijakan hard-delete-via-Logs proyek; bukan bug |
| Commission Rules | Dicoba membuat "Komisi Sales 5 Persen" (Rule Type Percentage, Rate Percent 5) | **Selalu gagal** dengan pesan generik "This Field Is Required" walau semua field terisi; ditelusuri lewat API, ternyata form mengirim nama field yang tidak cocok dengan yang divalidasi server (`type`/`value` dengan opsi `percent`/`fixed`, bukan `rule_type`/`rate_percent`/`percentage`) |
| Commissions | Dicek halaman list | Kosong, sesuai ekspektasi — komisi baru muncul otomatis dari transaksi yang cocok dengan Commission Rule, dan karena Commission Rules tidak bisa dibuat lewat UI, modul ini tidak bisa diuji lebih lanjut untuk saat ini |

> **Status Tahap L (2026-09-15): Empat bug ditemukan, dua di antaranya menghambat total (fitur
> sama sekali tidak bisa dipakai).** Rekrutmen (Job Vacancies/Applications) dan Shifts berfungsi
> baik dengan satu bug tampilan kecil di detail pelamar. Work Schedules punya bug signifikan:
> proses Generate Roster berhasil di server tapi hasilnya tidak pernah terlihat di halaman List
> maupun Calendar. **Employee Transfers dan Commission Rules sama-sama tidak bisa dipakai sama
> sekali** — Employee Transfers karena dropdown To Branch menampilkan pilihan yang semuanya
> ditolak validasi server, dan Commission Rules karena form mengirim nama field yang tidak cocok
> dengan API. Attendance Statuses dan Employment Types berfungsi baik (cuma satu salah label pesan
> toast). Detail lengkap masing-masing di:
> [`erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/07-halaman-detail-pelamar-tidak-menampilkan-lowongan-yang-dilamar.id.md`](../../erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/07-halaman-detail-pelamar-tidak-menampilkan-lowongan-yang-dilamar.id.md),
> [`erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/08-generate-roster-berhasil-tapi-halaman-work-schedules-tidak-menampilkan-hasilnya.id.md`](../../erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/08-generate-roster-berhasil-tapi-halaman-work-schedules-tidak-menampilkan-hasilnya.id.md),
> [`erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/09-fitur-employee-transfer-tidak-bisa-dipakai-semua-pilihan-to-branch-ditolak.id.md`](../../erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/09-fitur-employee-transfer-tidak-bisa-dipakai-semua-pilihan-to-branch-ditolak.id.md),
> [`erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/10-buat-commission-rule-selalu-gagal-nama-field-form-tidak-cocok-dengan-server.id.md`](../../erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/10-buat-commission-rule-selalu-gagal-nama-field-form-tidak-cocok-dengan-server.id.md).
>
> **Untuk pengujian ulang setelah bug diperbaiki**: uji ulang Work Schedules dengan mengecek
> filter tanggal/bulan yang dikirim halaman list; uji Employee Transfers dengan data cabang yang
> memang satu company (butuh perbaikan filter dropdown dulu); uji Commission Rules dari UI setelah
> nama field diperbaiki, lalu lanjutkan pengujian Commissions dengan transaksi nyata yang cocok
> dengan rule yang dibuat.

---

## TAHAP M — Approval Requests (Alur Approve Sungguhan)

**Konteks:** menguji alur approval sungguhan (bukan cuma melihat halaman Approval Inbox yang
kosong) dengan cara mengaktifkan opsi approval di salah satu modul (HRM > Leave Request),
membuat dokumen yang butuh approval, lalu mencoba menyetujuinya.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Baseline | Dicek halaman Approval Inbox sebelum ada dokumen apa pun yang butuh approval | Kosong ("No data"), filter Module menampilkan 7 modul yang didukung (Purchase Request, Purchase Order, Purchase Quotation, Journal, Expense, Leave Request, Payslip) |
| Buat Leave Request (approval OFF) | Dibuat 1 Leave Request untuk "Arman Halim" saat "Require Leave Approval" masih OFF (default) | Langsung berstatus **Approved** otomatis — sesuai konfigurasi, bukan bug |
| Aktifkan approval | Diaktifkan "Require Leave Approval" di Hrm Configs, disimpan | Berhasil tersimpan |
| Buat Leave Request (approval ON) | Dibuat 1 Leave Request lagi untuk "Dewi Anjani" | Berstatus **Submitted**, muncul 1 approval request baru di Approval Inbox (Leave Request #8, Step 1) |
| Buka detail approval request | Dibuka halaman detail | Status Step 1 = "Manager Approval"; tombol Approve/Reject/Request Revision semuanya **disabled** dengan tooltip "Your Active Role Is Not Authorized For This Step Only The Following Can Act: Manager" — akun Taufit (Admin) tidak punya role "Manager" |
| Telusuri akar masalah | Dicek Settings > Roles milik Taufit, lalu daftar lengkap 21 role cabang Kantor Utama, lalu config approval workflow 19 modul lewat API | **Ditemukan bug KRITIS skala aplikasi**: seluruh 19 approval workflow config (Purchasing, Sales, Accounting, HRM) mensyaratkan role_id 2 ("Manager") dan role_id 3 ("Director") yang **tidak pernah ada di database sama sekali** — dikonfirmasi lewat `roles/show` yang mengembalikan "No query results". 9 dari 19 config juga punya baris step yang terduplikasi persis |
| Coba approve lewat API | Dicoba submit approve langsung ke API dengan akun Taufit | Ditolak dengan "Error Approval Not Authorized For Step" (status 500, seharusnya 403) — otorisasi server-side berfungsi benar, cuma kode statusnya salah |

> **Status Tahap M (2026-09-15): Ditemukan bug KRITIS berskala seluruh aplikasi — bukan cuma
> satu modul.** Alur approval Leave Request tidak bisa diselesaikan sampai akhir karena akun
> mana pun tidak akan pernah bisa memenuhi syarat approver: role "Manager"/"Director" yang
> disyaratkan oleh SEMUA 19 approval workflow config bawaan (mencakup hampir semua modul
> transaksional utama — Purchasing, Sales, Accounting, HRM) **tidak pernah benar-benar dibuat**
> di database. Ini berarti fitur approval, sejak awal, tidak pernah benar-benar bisa dipakai
> end-to-end di modul mana pun yang menyalakan opsi "Require X Approval" — dokumen akan macet
> permanen di Step 1. Ditemukan juga bug tambahan: 9 dari 19 config approval punya baris step
> yang terduplikasi persis, kolom Status di Approval Inbox list menampilkan dash kosong padahal
> detailnya benar "Pending", field Document di halaman detail approval tidak berisi tautan ke
> dokumen aslinya, dan kolom Leave Type di daftar Leave Requests selalu kosong. Detail lengkap di:
> [`erpApiServices/docs/TemuanTestCase/Approvals/Ranahku/02-seluruh-approval-workflow-mengacu-ke-role-manager-dan-director-yang-tidak-pernah-ada.id.md`](../../erpApiServices/docs/TemuanTestCase/Approvals/Ranahku/02-seluruh-approval-workflow-mengacu-ke-role-manager-dan-director-yang-tidak-pernah-ada.id.md)
> (temuan utama),
> [`erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/11-daftar-leave-requests-kolom-leave-type-selalu-kosong.id.md`](../../erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/11-daftar-leave-requests-kolom-leave-type-selalu-kosong.id.md).
> (Catatan: dugaan awal soal halaman Core > Users tidak bisa diakses ternyata salah URL
> pengujian, sudah diralat — halaman Users yang sesungguhnya di `client-master/users` berfungsi
> normal.)
>
> **Untuk pengujian ulang setelah bug diperbaiki**: setelah role "Manager"/"Director" (atau role
> pengganti yang sesuai) benar-benar dibuat dan ditautkan dengan benar ke minimal satu karyawan
> per cabang, uji ulang alur approval Leave Request ini sampai selesai (approve Step 1 → Step 2),
> lalu ulangi pengujian serupa untuk modul lain yang memakai approval (Purchase Request/Order,
> Sales Order/Invoice, Journal, Payslip, Expense) untuk memastikan semuanya benar-benar bisa
> diselesaikan end-to-end, bukan cuma sampai status "Submitted".

---

## TAHAP N — Finance & Administrasi Cabang

**Konteks:** menguji data pelengkap di Finance dan Branch Management yang belum pernah disentuh:
Bank Reconciliations, Cost Centers, Roles/Permissions/Users, Discounts, Cashback Rules, Member
Tiers, Expense Categories, dan Expenses.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Bank Reconciliations | Dibuat 1 rekonsiliasi untuk "Bank Operasional Ranahku — BCA", periode 1-30 September 2026, Opening Rp 5.000.000, Closing/Statement Rp 7.000.000 (Balanced) | Berhasil dibuat (RCN/2026/09/0001), TAPI halaman detail menampilkan "Invalid Date — Invalid Date" untuk Period, dan tombol **Complete selalu gagal** ("This Field Is Required") karena FE mengirim `id` padahal server perlu `slug` — dikonfirmasi berhasil lewat API setelah dikoreksi |
| Cost Centers | Dibuat "CC-OPS — Operasional Toko" | Berhasil, tidak ada bug |
| Roles | Dicek 21 role yang ada, semua role hasil auto-create dari Position menampilkan deskripsi "Auto Created Role For Position **X**" (placeholder huruf X mentah, bukan nama posisi sungguhan) | Bug kosmetik ringan, tidak ada dampak fungsional |
| Permissions | Dicek daftar 1118 permission, terbagi ke 15 modul (accounting, hrm, purchasing, dst) | Berfungsi baik, tidak ada bug |
| Users | Dicek daftar 27 user beserta role masing-masing | Berfungsi baik, tidak ada bug (catatan: sempat salah menguji URL "core/users" yang ternyata tidak ada di navigasi manapun — setelah dikoreksi ke URL yang benar, semua normal) |
| Discounts | Dibuat "Diskon Akhir Tahun" 10% | Berhasil, tidak ada bug |
| Cashback Rules | Dibuat "Cashback Member Setia" 5% | Berhasil, tidak ada bug |
| Member Tiers | Dibuat "Silver" level 1 | Berhasil, tidak ada bug |
| Expense Categories | Dibuat "Biaya Operasional Kantor" | Berhasil, tidak ada bug |
| Expenses | Dicoba buat Expense Rp 150.000 kategori di atas, payment method Cash | **Selalu gagal** — awalnya "This Field Is Required" tanpa detail, ditelusuri lewat API ternyata field `quantity` seharusnya `qty`, `description` per item ternyata wajib (tidak ditandai wajib di UI), dan `category_id`/`payment_method` kemungkinan juga salah nama. Percobaan submit terakhir dari UI bahkan gagal **tanpa notifikasi error sama sekali** |

> **Status Tahap N (2026-09-15): 2 dari 10 area yang diuji punya bug blocking (Bank
> Reconciliation Complete, dan Expenses Create), 1 bug kosmetik ringan (deskripsi Role), sisanya
> (7 area) berfungsi baik tanpa temuan.** Pola bug yang muncul di Bank Reconciliation dan
> Expenses konsisten dengan pola sistemik yang sudah ditemukan berulang kali di sesi pengujian
> hari ini: nama field yang dikirim FE tidak cocok dengan yang divalidasi/disimpan server
> (`id` vs `slug`, `quantity` vs `qty`, dst — lihat juga temuan serupa di Commission Rules
> Tahap L). Detail lengkap di:
> [`erpApiServices/docs/TemuanTestCase/Finance/Ranahku/01-bank-reconciliation-tanggal-invalid-dan-tombol-complete-selalu-gagal.id.md`](../../erpApiServices/docs/TemuanTestCase/Finance/Ranahku/01-bank-reconciliation-tanggal-invalid-dan-tombol-complete-selalu-gagal.id.md),
> [`erpApiServices/docs/TemuanTestCase/ClientMaster/Ranahku/04-buat-expense-selalu-gagal-nama-field-quantity-tidak-cocok-dengan-server.id.md`](../../erpApiServices/docs/TemuanTestCase/ClientMaster/Ranahku/04-buat-expense-selalu-gagal-nama-field-quantity-tidak-cocok-dengan-server.id.md),
> [`erpApiServices/docs/TemuanTestCase/ClientMaster/Ranahku/05-deskripsi-role-otomatis-menampilkan-placeholder-position-x-mentah.id.md`](../../erpApiServices/docs/TemuanTestCase/ClientMaster/Ranahku/05-deskripsi-role-otomatis-menampilkan-placeholder-position-x-mentah.id.md).
>
> **Untuk pengujian ulang setelah bug diperbaiki**: uji ulang alur Complete Bank Reconciliation
> dan Create Expense dari UI sampai berhasil, termasuk cek apakah keduanya memicu jurnal otomatis
> yang benar (Bank Reconciliation untuk selisih, Expense untuk pencatatan biaya ke akun yang
> sesuai). Rekomendasikan juga audit menyeluruh ke SEMUA form transaksional lain di aplikasi
> untuk pola bug "nama field FE tidak cocok server" yang sama, karena sudah ditemukan berulang
> di banyak modul berbeda (Commission Rules, Bank Reconciliation, Expenses) — kemungkinan ada
> lebih banyak lagi yang belum tersentuh pengujian.

---

## TAHAP O — Modul Restaurant Penuh (Config, Areas, Bookings, Orders, Order Items, Tables, KDS, Floor Plan)

**Konteks:** menguji modul Restaurant secara menyeluruh, dari konfigurasi sampai alur transaksi
order meja penuh (buka order → tambah item → kirim ke dapur → sajikan → tutup order/bayar).

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Restaurant Config | Dicek pengaturan service charge, default tax, dll | Berfungsi baik, tidak ada bug |
| Areas | Dicek data Area yang sudah ada ("Area Utama") | Berfungsi baik, tidak ada bug |
| Kitchen Stations | Dicek data Kitchen Station yang sudah ada | Berfungsi baik, tidak ada bug |
| Bookings — Create | Dibuat reservasi meja M01, 20 Sep 19:00, pax 1 | Awalnya selalu gagal "This Field Is Required" — field `table_id`/`booking_datetime`/`guest_count` tidak cocok dengan server (`restaurant_table_id`/`booking_date`+`booking_time`/`pax`); berhasil setelah dikoreksi lewat API |
| Bookings — Daftar | Dibuka halaman daftar Bookings setelah data di atas ada | **Selalu "No data"** — request API minta relasi `restaurantTable.restaurantArea` yang tidak ada di model `TableBooking` (harusnya `table.area`) |
| Orders — New Order | Dibuka Meja M01, pilih Table, klik Open Order → konfirmasi | Berhasil, order `ORD/2026/09/0003` terbuka normal, tidak ada bug field |
| Orders — Add Menu Item | Dipilih produk "Air Mineral Galon 19 L" (harga master Rp 22.000) | Item tersimpan dengan **harga Rp 0** — dropdown pemilihan produk tidak meminta data harga (`with_price` tidak dikirim) dan field response yang benar (`active_price.price`) tidak cocok dengan yang dibaca kode (`selling_price`) |
| Orders — Add Menu Item (harga manual) | Ditambahkan "Nasi Goreng Spesial" dengan harga diisi manual Rp 25.000 | Berhasil, Subtotal/Total ikut terhitung benar (pembuktian bug di atas murni soal auto-fill harga, bukan logika kalkulasi) |
| Orders — Send To Kitchen | Diklik dari halaman Order | Berhasil, status item berubah ordered → preparing |
| Kitchen Display (KDS) | Diakses langsung `restaurant/kds` (tidak ada di menu sidebar) | Berfungsi baik — tiket per meja tampil benar, tombol Start/Done berhasil mengubah status item preparing → served |
| Order Items (halaman menu sidebar) | Dibuka setelah order open dengan item preparing | **Selalu "No Open Orders"** — request API minta relasi `table` yang tidak ada di model `TableOrder` (harusnya `restaurantTable`) |
| Orders — Close Order | Dibayar Rp 25.000 via Bank Transfer, pas tanpa kembalian | Berhasil, status closed, bill `ORD/2026/09/0003-1` berstatus paid |
| Orders — Void Order (setelah closed+paid) | Diklik Void Order pada order yang sudah closed dan lunas | **Berhasil di-void** — order jadi status "voided", bill yang tadinya "paid" ikut jadi "void". Seharusnya order yang sudah lunas tidak bisa di-void begitu saja |
| Orders — Daftar | Dibuka halaman daftar Orders (sebelum dan sesudah order dibuat) | **Selalu "No data"** — request API minta 2 relasi salah sekaligus: `table` dan `openedBy` (harusnya `restaurantTable` dan `createdBy`) |
| Tables — Daftar | Dibuka halaman daftar Tables walau meja M01/M02 aktif dipakai di fitur lain | **Selalu "No data"** — request API minta relasi `restaurantArea` yang tidak ada (harusnya `area`) |
| Floor Plan | Diakses langsung `restaurant/floor-plan` (tidak ada di menu sidebar) | Berfungsi baik — denah meja M01/M02 di Area Utama tampil benar |

> **Status Tahap O (2026-09-15): modul Restaurant punya SATU bug SANGAT TINGGI (harga item
> pesanan selalu Rp 0) dan EMPAT bug TINGGI berpola identik (halaman daftar Bookings, Orders,
> Order Items, dan Tables semuanya selalu "No data"/kosong karena salah nama relasi Eloquent di
> `additionalRelations`), ditambah SATU bug TINGGI soal integritas data (order yang sudah closed
> dan lunas masih bisa di-void). Dua halaman yang sebenarnya sudah berfungsi baik (KDS, Floor
> Plan) ternyata tidak tertaut ke menu sidebar sama sekali.**
>
> Detail lengkap di:
> [`erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/02-item-pesanan-meja-selalu-tersimpan-harga-rp-0.id.md`](../../erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/02-item-pesanan-meja-selalu-tersimpan-harga-rp-0.id.md) (sudah diupdate dengan akar masalah pasti),
> [`erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/05-halaman-order-items-selalu-tampil-no-open-orders-nama-relasi-salah.id.md`](../../erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/05-halaman-order-items-selalu-tampil-no-open-orders-nama-relasi-salah.id.md),
> [`erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/06-halaman-daftar-orders-selalu-no-data-dua-nama-relasi-salah.id.md`](../../erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/06-halaman-daftar-orders-selalu-no-data-dua-nama-relasi-salah.id.md),
> [`erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/07-order-yang-sudah-closed-dan-lunas-masih-bisa-di-void.id.md`](../../erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/07-order-yang-sudah-closed-dan-lunas-masih-bisa-di-void.id.md),
> [`erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/08-halaman-daftar-tables-selalu-no-data-nama-relasi-salah.id.md`](../../erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/08-halaman-daftar-tables-selalu-no-data-nama-relasi-salah.id.md),
> [`erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/09-halaman-daftar-bookings-selalu-no-data-nama-relasi-salah.id.md`](../../erpApiServices/docs/TemuanTestCase/Restaurant/Ranahku/09-halaman-daftar-bookings-selalu-no-data-nama-relasi-salah.id.md).
>
> **Untuk pengujian ulang setelah bug diperbaiki**: audit menyeluruh SEMUA pemanggilan
> `additionalRelations` di modul Restaurant (dan idealnya seluruh aplikasi) terhadap nama relasi
> yang benar-benar ada di model — pola ini terbukti muncul di 4 dari 4 halaman list yang diuji.
> Uji ulang juga alur harga item pesanan dengan berbagai produk setelah `with_price`/pemetaan
> field diperbaiki, dan pastikan guard status ditambahkan supaya order yang sudah closed+paid
> tidak bisa di-void.

---

## TAHAP P — Point of Sale (Config, Cash Session, Transaksi) dan Purchasing Blanket Agreements

**Konteks:** menguji modul POS dari ujung ke ujung (buka sesi kasir → transaksi → tutup sesi),
dan fitur baru Blanket Agreements di Purchasing (kontrak pembelian jangka panjang dengan
mekanisme "release" jadi Purchase Order).

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Pos Configs | Dicek pengaturan approval jurnal, posting timing, offline mode, receipt, journal mapping | Berfungsi baik, semua sudah terkonfigurasi, tidak ada bug |
| Cash Sessions — Open | Dibuka sesi di "Gudang Toko Retail", opening balance Rp 500.000 | Berhasil, tapi kartu ajakan "buka sesi" menampilkan judul **"No Session Open Title"** secara harfiah — key translation memakai suffix `_title` terlarang, terjemahan Indonesia di database juga sudah rusak ("Tidak Ada Judul Terbuka Sesi") |
| Pos Transactions — Katalog | Dibuka POS Terminal, dicek katalog 25 produk | 7 produk kategori "Layanan Sewa Aplikasi" (jasa non-fisik) **selalu "OUT OF STOCK" dan tidak bisa diklik untuk dijual** — sistem tidak punya konsep produk non-stok/jasa sama sekali di skema database |
| Pos Transactions — Checkout | Dijual 1 galon Air Mineral Galon 19L, bayar Cash pas | Berhasil sempurna — transaksi tercatat (POS/2026/09/15/0001), stok warehouse berkurang otomatis dari 29 ke 28, struk tercetak benar |
| Cash Sessions — Close | Ditutup sesi dengan cash count sesuai expected (Rp 522.000) | Berhasil, tidak ada selisih, riwayat sesi tercatat benar |
| Blanket Agreements — Create | Dibuat kontrak `BLA/2026/09/0001` untuk PT Sumber Elektronik Andalan, item Beras Premium 5kg harga Rp 65.000, max 1.000 karung, commitment type Total Value | Berhasil, redirect ke halaman detail sesuai konvensi |
| Blanket Agreements — Activate | Diklik Activate dari status Draft | Berhasil, status jadi Active |
| Blanket Agreements — Release Purchase Order | Dirilis PO 200 karung dari kontrak | Berhasil, `PO/2026/09/0003` dibuat dengan harga terkunci ke kontrak, TAPI baris Status History menampilkan kode mentah **"po_released_from_contract"**, bukan kalimat manusiawi |
| Blanket Agreements — Daftar | Dicek kolom "Commitment" di daftar setelah kontrak dibuat | Menampilkan **"By Quantity"** padahal Commitment Type yang dipilih adalah "Total Value" (bug logika kondisi: nilai 0/unlimited disalahartikan sebagai tipe quantity) |

> **Status Tahap P (2026-09-15): tidak ada bug blocking fungsi inti (transaksi POS dan release PO
> dari kontrak sama-sama berhasil dan datanya akurat), tapi ditemukan 1 bug TINGGI (produk jasa
> tidak bisa dijual lewat POS karena tidak ada konsep non-stok) dan 3 bug RENDAH/SEDANG seputar
> kualitas tampilan (translation key rusak, kode internal bocor ke UI, label kolom salah).**
>
> Detail lengkap di:
> [`erpApiServices/docs/TemuanTestCase/Pos/Ranahku/01-translation-key-no-session-open-title-melanggar-konvensi-hasil-terjemahan-rusak.id.md`](../../erpApiServices/docs/TemuanTestCase/Pos/Ranahku/01-translation-key-no-session-open-title-melanggar-konvensi-hasil-terjemahan-rusak.id.md),
> [`erpApiServices/docs/TemuanTestCase/Pos/Ranahku/02-produk-layanan-jasa-non-stok-selalu-out-of-stock-di-pos-tidak-bisa-dijual.id.md`](../../erpApiServices/docs/TemuanTestCase/Pos/Ranahku/02-produk-layanan-jasa-non-stok-selalu-out-of-stock-di-pos-tidak-bisa-dijual.id.md),
> [`erpApiServices/docs/TemuanTestCase/Purchasing/Ranahku/01-status-history-po-menampilkan-kode-internal-mentah-bukan-teks-manusiawi.id.md`](../../erpApiServices/docs/TemuanTestCase/Purchasing/Ranahku/01-status-history-po-menampilkan-kode-internal-mentah-bukan-teks-manusiawi.id.md),
> [`erpApiServices/docs/TemuanTestCase/Purchasing/Ranahku/02-kolom-commitment-blanket-agreement-salah-label-by-quantity-padahal-tipe-total-value.id.md`](../../erpApiServices/docs/TemuanTestCase/Purchasing/Ranahku/02-kolom-commitment-blanket-agreement-salah-label-by-quantity-padahal-tipe-total-value.id.md).
>
> **Untuk pengujian ulang setelah bug diperbaiki**: tambahkan kolom penanda produk non-stok/jasa
> di skema database supaya jasa bisa dijual lewat POS, lalu uji ulang penjualan jasa sampai
> berhasil checkout. Audit juga semua nilai `trigger_source` yang dipakai `recordStatusChange()`
> di seluruh modul untuk pola "kode internal bocor ke UI" yang sama.

---

## TAHAP Q — Sisa HRM (Payroll Periods, Activity Logs) dan Core Client-Facing (Menu Layout, Sales Channels, Personal Logs, PDF Layout Settings)

**Konteks:** menyapu sisa halaman yang belum tersentuh dari inventaris 199 halaman FE, fokus ke
HRM (Payroll Periods, Activity Logs) dan halaman Branch Management yang belum diuji (Menu Layout,
Sales Channels, Personal Logs, PDF Layout Settings).

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Payroll Periods | Dicek periode "Penggajian September 2026" yang sudah ada | Total Gross = Total Net = Rp 187.900.000 persis sama, konsisten dengan bug lama yang sudah didokumentasikan (potongan BPJS/PPh21 selalu nol) — tidak ditulis temuan baru, sudah tercakup [[../../erpApiServices/docs/TemuanTestCase/Hrm/Ranahku/06-potongan-bpjs-dan-pph21-payroll-selalu-nol-data-master-belum-diisi]] |
| Activity Types (master data) | Dicek, ternyata kosong, dibuat satu ("Pelatihan Keselamatan Kerja") lewat link "Create One" dari halaman Activity Logs | Berhasil, link dan form bekerja normal, tidak ada bug |
| Activity Logs — Create | Dibuat log "Pelatihan K3 Semester 2" untuk karyawan Agus Setiawan | Berhasil, redirect ke detail, status Draft |
| Activity Logs — Submit For Review | Diklik dari status Draft | Berhasil, status berubah jadi Submitted |
| Menu Layout | Dicek peta lengkap seluruh menu aplikasi (15 node, ratusan slug) | Berfungsi baik sebagai alat admin, sekaligus mengonfirmasi ulang bahwa `restaurant/kds` dan `restaurant/floor-plan` memang tidak terdaftar di menu manapun (bukan cuma tidak muncul di sidebar) — memperkuat temuan Tahap O |
| Sales Channels | Dicek 6 channel (POS, Sales, Rental, Restaurant, Canvassing, Online Store), semua enabled | Berfungsi baik, tidak ada bug pada channel enable/disable |
| Personal Logs (My Activity Log) | Dicek 329 baris log aktivitas pribadi dari sesi pengujian ini | Kolom **"Record" selalu menampilkan strip kosong tanpa nomor/ID** ("Purchase Order -", "Table Order -", dst) untuk SEMUA baris — bug kode: string literal `-` tidak pernah diganti nilai `source_id` sebenarnya |
| PDF Layout Settings | Dicek pengaturan letterhead, appearance, item table, footer | Berfungsi baik, semua field ada, tidak ada bug |

> **Status Tahap Q (2026-09-15): 1 bug SEDANG baru ditemukan (kolom Record di Personal Logs
> selalu kosong), sisanya berfungsi baik atau sudah tercakup temuan lama.**
>
> Detail lengkap di:
> [`erpApiServices/docs/TemuanTestCase/ClientMaster/Ranahku/06-kolom-record-di-personal-logs-selalu-tampil-tanda-strip-kosong-tanpa-nomor.id.md`](../../erpApiServices/docs/TemuanTestCase/ClientMaster/Ranahku/06-kolom-record-di-personal-logs-selalu-tampil-tanda-strip-kosong-tanpa-nomor.id.md).
>
> **Catatan cakupan**: halaman `core/family-relationships` sengaja TIDAK diuji — dicek lebih dulu
> lewat `permissionsIsMenu.json` dan ternyata tidak terdaftar sebagai menu untuk peran apa pun
> (bukan cuma tidak ada di sidebar Admin), jadi kemungkinan besar bukan halaman yang benar-benar
> dipakai — mengikuti pelajaran dari koreksi temuan Core/Users sebelumnya (jangan menguji URL yang
> tidak terbukti bisa dijangkau pengguna).

---

## TAHAP R — Sales Penuh (Quotations, Sales Orders, Deliveries, Invoices, Payment Bills, Returns)

**Konteks:** menyapu seluruh modul Sales — sebagian sudah tersentuh sesi sebelumnya
(Quotations, Sales Orders, Sales Invoices sebatas verifikasi list), fokus tahap ini adalah
menyelesaikan alur create/detail yang belum diuji: Sales Payment Bills, Sales Deliveries, Sales
Returns.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Sales Payment Bills — Create | Diisi invoice, tanggal, jumlah, metode bayar lewat UI, klik Save berulang kali | GAGAL terus dengan error generik "This Field Is Required" — ditelusuri sampai akar: FE kirim field `scheduled_date`, BE mewajibkan field `date`. Dikonfirmasi lewat API langsung: payload FE persis → HTTP 422; field diganti `date` → berhasil (`PAY-S/2026/09/0001` dibuat) |
| Sales Deliveries — List | Dicek, kosong (`dataCount: 0`, genuinely empty, bukan bug) | Normal, belum ada delivery dibuat sebelumnya |
| Sales Deliveries — Create | Dropdown "Select Sales Order" dibuka | SEMUA opsi menampilkan **"Invalid Date"** — field `date` dari API sudah ISO datetime lengkap, FE menambah lagi `'T00:00:00'` di belakangnya sehingga hasil parse selalu invalid |
| Sales Deliveries — Create (lanjutan) | Dipilih SO, warehouse, tanggal, klik Save | Modal konfirmasi salah teks: **"Are You Sure Save This Goods Receipt"** (copy-paste dari Purchasing) — setelah dikonfirmasi, delivery `DO/2026/09/0001` tetap berhasil dibuat dengan benar (murni bug teks) |
| Sales Returns — List | Dicek 1 return existing (`RTN/2026/09/0001`) | List berfungsi normal |
| Sales Returns — Detail | Dibuka detail `RTN/2026/09/0001` | Kolom **Product di Return Items selalu tampil strip "—"** — relasi `items.productSku` tidak disertakan di `additionalRelations` panggilan show, padahal data `product_sku_id` tersimpan lengkap di database |
| Sales Returns — Create | Dipilih invoice, item tidak otomatis terisi ("No Items") | Ditelusuri: BUKAN desain, tapi **fitur auto-fill rusak total** — `SalesInvoice` model tidak punya relasi `items()` sama sekali, jadi `res.data.items` selalu `undefined` untuk semua invoice |
| Sales Returns — Create (Add Manual) | Dropdown SKU dibuka | Menampilkan SELURUH katalog produk perusahaan (24 produk), tidak difilter ke invoice yang dipilih — akibat langsung dari fitur auto-fill yang rusak di atas |
| Sales Returns — Verifikasi celah validasi | Dicoba lewat API: retur `INV-S/2026/09/0001` dengan SKU **BRG-001** (tidak pernah ada di invoice ini) qty **999** | **BERHASIL DIBUAT** (`RTN/2026/09/0002`, total Rp 9.990.000) tanpa penolakan apa pun — guard `NotOverReturnedRule` tidak pernah aktif karena field `sales_delivery_item_id` tidak pernah dikirim FE untuk modul Sales (beda dengan Purchase Returns yang mengirimnya dengan benar) |
| Sales Orders, Sales Invoices, Quotations — List | Diverifikasi ulang list masing-masing (5 SO Invoiced, 5 SI Unpaid, 5 Quotation Converted) | Semua list berfungsi normal, tidak ada bug baru |

> **Status Tahap R (2026-09-15): 5 temuan baru ditulis** — 1 **TINGGI** (Sales Return bisa
> dibuat untuk produk yang tidak pernah dijual, tanpa batas kuantitas — celah integritas
> stok/keuangan, sudah diverifikasi lewat API), 1 **TINGGI** (Sales Payment Bill tidak bisa
> dibuat sama sekali lewat UI karena nama field tanggal tidak cocok FE/BE — instance baru dari
> pola sistemik field-name-mismatch), 1 **SEDANG** (kolom Product di detail Sales Return selalu
> kosong — instance baru dari pola sistemik relasi tidak di-preload), 1 **RENDAH-SEDANG**
> (dropdown Select Sales Order di Create Delivery selalu tampil "Invalid Date"), 1 **RENDAH**
> (modal konfirmasi Create Delivery salah menyebut "Goods Receipt").
>
> Detail lengkap di `erpApiServices/docs/TemuanTestCase/Sales/Ranahku/01` sampai `05`.
>
> **Catatan pembersihan data uji**: `PAY-S/2026/09/0001` dan `RTN/2026/09/0002` dibuat lewat API
> langsung sebagai bagian dari verifikasi akar masalah — perlu dihapus dari branch `Kantor Utama`
> sebelum go-live.

---

## Ringkasan Sementara Sesi Pengujian (2026-09-15, per Tahap R — pengujian masih berlanjut)

Sesi ini telah menyelesaikan **Tahap G sampai R**, mencakup seluruh modul utama aplikasi yang
sebelumnya belum pernah diuji sama sekali (Rental, Fixed Assets, Reports, Akuntansi Manual,
Persediaan Lanjutan, Kanvasing Lanjutan, SDM Lanjutan, Approval Requests, Finance & Administrasi
Cabang, Restaurant penuh, Point of Sale, Purchasing Blanket Agreements, sisa halaman HRM/Core
client-facing, dan Sales penuh). Total temuan baru yang ditulis sampai titik ini mencakup 1 bug
**KRITIS** berskala seluruh aplikasi (sistem approval tidak pernah bisa dipakai karena role yang
disyaratkan tidak pernah ada), banyak bug **SANGAT TINGGI/TINGGI** yang memblokir fitur
sepenuhnya atau membuka celah integritas data (Rental Order macet, Stock Take merusak data stok,
Employee Transfer tidak bisa dipakai, Commission Rules tidak bisa dibuat, Work Schedules tidak
menampilkan data, Bank Reconciliation tidak bisa Complete, Expenses tidak bisa dibuat, harga item
pesanan Restaurant selalu Rp 0, empat halaman daftar di modul Restaurant selalu kosong karena
nama relasi salah, order Restaurant yang sudah lunas masih bisa di-void, produk jasa tidak bisa
dijual lewat POS, Sales Payment Bill tidak bisa dibuat lewat UI, dan Sales Return bisa dibuat
untuk produk yang tidak pernah dijual tanpa batas kuantitas), dan sejumlah bug **SEDANG/RENDAH**
berupa masalah tampilan/terjemahan/kode internal bocor/label salah/pesan error yang tidak jelas.
Semua temuan sudah didokumentasikan sebagai file terpisah di
`erpApiServices/docs/TemuanTestCase/{Modul}/Ranahku/`, siap dipakai sebagai acuan pada fase
perbaikan bug berikutnya.

---

## TAHAP S — Inventory Penuh (Stock Transfers, Stock Adjustments, Stock Lots, Stock Serials, Consignment Settlements)

**Konteks:** menyelesaikan sisa alur create/lifecycle Inventory yang di Tahap J baru sebatas
dicek list-nya kosong — sekarang diuji end-to-end dengan data nyata.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Stock Transfers — Create | Dibuat `TRF/2026/09/0002` (MAIN → RNK-RETAIL, Beras Premium 5kg 15 karung), Submit, New Shipment, Receive | Seluruh siklus berhasil (Draft → Approved → In Transit → Received), stok berpindah benar (MAIN -15, RNK-RETAIL +15, dikonfirmasi via Stock History) — mekanisme inti SEHAT, tidak ada corruption seperti bug Stock Take |
| Stock Transfers — Shipment card | Setelah shipment dibuat | Kartu shipment menampilkan **"Shipped: Invalid Date"** dan **"Received Invalid Date"** — instance baru pola sistemik Invalid Date (field `shipped_at`/`received_at` sudah ISO datetime, FE tambah lagi suffix waktu) |
| Stock Adjustments — Create | Dibuat `ADJ/2026/09/0002` (Gudang Utama, Gula Pasir 1kg, actual qty 495 dari sistem 500), Submit → langsung Posted | Variance (-5) diterapkan BENAR ke stok (500→495, dikonfirmasi via Stock History) — beda dengan bug Stock Take, mekanisme Stock Adjustment SEHAT. Reason kosong (master data belum ada) tetap bisa disimpan, tidak masalah |
| Stock Adjustments — Detail page | Setelah dibuat | **"Adjustment Date: Invalid Date"** — instance ketiga pola sistemik yang sama |
| Stock Lots — Create | Dibuat `LOT-BRG001-0001` (id 62, Beras Premium, qty 50, unit cost Rp 130.000) | Create BERHASIL (data lengkap benar di DB), tapi redirect ke halaman detail menampilkan **"Record Not Found"** — ditelusuri: endpoint `inventory/stock-lots/show` SELALU HTTP 500 karena argumen `flexibleShow()` di controller salah total |
| **Pencarian lanjutan pola bug show()** | Grep pola `flexibleShow($request, {Model}::class, ...)` di seluruh controller | Ditemukan **18 controller** di 4 modul (Inventory, ClientMaster, Restaurant, Rental) dengan bug identik — dikonfirmasi live di 6 endpoint, SEMUA gagal 500. Ini pola sistemik terbesar dari sisi cakupan modul di seluruh sesi pengujian |
| Stock Lots — Consignment | Dibuat `LOT-CONSIGN-0001` (id 63, ownership Consigned, direction In, kontak PT Sumber Elektronik Andalan, qty 20) | Berhasil tersimpan lengkap dan benar |
| Consignment Settlements — Create | Settle 8 dari 20 qty lot konsinyasi di atas, lewat halaman standalone (bukan dari detail lot yang rusak) | Berhasil, qty available lot berkurang benar (20→12, dikonfirmasi API) — mekanisme settlement SEHAT |
| Stock Serials — Create | Dibuat `SN-BRG001-0001` (Beras Premium, Gudang Utama, status Available) | Berhasil tersimpan dan tampil benar di list |

> **Status Tahap S (2026-09-15): 1 temuan SANGAT TINGGI berskala 18-controller/4-modul (endpoint
> show() selalu error 500), 1 temuan sistemik Invalid Date (instance ke-3), dan konfirmasi positif
> bahwa mekanisme inti Stock Transfer/Stock Adjustment/Consignment Settlement semuanya SEHAT
> (tidak ada corruption seperti bug Stock Take di Tahap J).**
>
> Detail lengkap di:
> [`erpApiServices/docs/TemuanTestCase/Umum/Ranahku/03-pola-sistemik-flexibleshow-argumen-salah-di-18-controller-halaman-detail-selalu-error-500.id.md`](../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/03-pola-sistemik-flexibleshow-argumen-salah-di-18-controller-halaman-detail-selalu-error-500.id.md),
> [`erpApiServices/docs/TemuanTestCase/Inventory/Ranahku/02-halaman-detail-stock-lot-selalu-error-500-argumen-flexibleshow-salah.id.md`](../../erpApiServices/docs/TemuanTestCase/Inventory/Ranahku/02-halaman-detail-stock-lot-selalu-error-500-argumen-flexibleshow-salah.id.md),
> [`erpApiServices/docs/TemuanTestCase/Umum/Ranahku/02-pola-sistemik-format-tanggal-invalid-date-saat-kolom-backend-datetime-bukan-date.id.md`](../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/02-pola-sistemik-format-tanggal-invalid-date-saat-kolom-backend-datetime-bukan-date.id.md).
>
> **Catatan pembersihan data uji**: `LOT-BRG001-0001` (id 62), `LOT-CONSIGN-0001` (id 63, sudah
> disettle sebagian), dan `SN-BRG001-0001` dibuat sebagai bagian dari pengujian — valid untuk
> dipakai lagi begitu bug show() diperbaiki, tidak wajib dihapus.

---

## TAHAP T — Dashboard Per-Modul dan Core CMS Pages

**Konteks:** meninjau dashboard per-modul (Sales, Inventory, dst) untuk konsistensi data, dan
memverifikasi reachability halaman Core CMS sebelum menguji (mengikuti pelajaran dari retraksi
temuan Core/Users sebelumnya — jangan uji halaman yang memang tidak bisa dijangkau role manapun).

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Dashboard umum (`/dashboard`) | Diklik trigger sidebar "Dashboard" | BUKAN bug — ini expandable group trigger dengan 8 anak dashboard per-modul (Canvassing, Hrm, Accounting, Inventory, Pos, Purchasing, Restaurant, Sales) sesuai 8 permission `dashboard.*` yang dimiliki akun. Fallback generic `/dashboard` cuma tampil kalau role benar-benar tidak punya akses dashboard/menu apa pun — dikonfirmasi lewat `usePermissions.ts` dan `role/my-permissions` |
| Sales Dashboard | Ditinjau seluruh widget | Ditemukan bug **invoice/SO langsung "Paid" walau payment bill masih draft** — lihat [[../../erpApiServices/docs/TemuanTestCase/Sales/Ranahku/06-invoice-langsung-lunas-walau-payment-bill-masih-draft-belum-disetujui]] |
| Inventory Dashboard | Ditinjau seluruh widget (KPI, Inventory Value, Dead Stock, Stock Flow, Top Movers) | Ditemukan bug **SANGAT TINGGI**: widget "Dead Stock" menampilkan Gula Pasir 1kg sebagai "Never Moved" padahal baru saja disentuh Stock Adjustment — ditelusuri lebih dalam dan ternyata akar masalahnya jauh lebih besar: Stock Adjustment tidak pernah mengirim `unit_cost` ke cost-layer ledger (`stock_lots`), sehingga ~87,6% dari total kuantitas stok riil cabang (2.841 dari 3.243 unit) sama sekali tidak tercatat di `stock_lots` — membuat Inventory Value On Hand, Dead Stock, dan COGS/Inventory Turnover di dashboard ini semuanya salah besar |
| Purchasing Dashboard | Ditinjau seluruh widget (Open PO, Spend, AP, PO Pipeline, Top Suppliers, AP Aging) | SEHAT — "Open Purchase Orders: Rp 0" awalnya terlihat janggal (ada 1 PO Draft senilai Rp 13 juta), tapi setelah ditelusuri kode, definisi "Open PO" sengaja mengecualikan status draft & paid — bukan bug. AP Rp 0 juga benar, dikonfirmasi 2 invoice terkait sudah `paid_amount == total`. Field `is_paid` di Purchase Invoice yang tetap `false` walau sudah lunas juga BUKAN bug — field itu representasi terpisah untuk "ditandai lunas saat create", bukan status lunas aktual (yang direpresentasikan oleh `status`+`paid_amount`) |
| POS Dashboard | Ditinjau seluruh widget (Today's Sales, Voids/Refunds, Payment Breakdown, Top Selling, Cash Sessions) | SEHAT — semua angka konsisten dengan Recent Transactions/Recent Voids yang tampil, tidak ada anomali |
| Restaurant Dashboard | Ditinjau seluruh widget | "Top Selling Items 30 Days" menampilkan qty terjual benar tapi **Rp 0** untuk semua omzet — ini KONSISTEN dengan bug yang SUDAH terdokumentasi sebelumnya (harga item pesanan Restaurant selalu Rp 0, ditemukan Tahap O), bukan temuan baru |
| HRM Dashboard | Ditinjau seluruh widget | "Headcount By Department" tampil kosong ("—") — ditelusuri via API, BUKAN bug tampilan: seluruh 25 karyawan uji memang tidak diisi `department_id` saat dibuat (celah data uji, bukan bug kode); chart tetap benar menampilkan 1 bar "—" dengan qty 25 (tersembunyi di tooltip hover, tidak tertangkap ekstraksi teks halaman) |
| Canvassing Dashboard | Ditinjau seluruh widget | Ditemukan pola terjemahan hilang yang SAMA dengan temuan lama (`Canvassing/Ranahku/02`), muncul lagi di lokasi baru ("Visit Outcomes", "Check-in Locations") + 1 key baru yang belum pernah tercatat (`content.outside_area`) — sudah digabung ke temuan lama, bukan file baru |
| Accounting Dashboard | Ditinjau seluruh widget (Cash & Bank, AR/AP, Income Statement, Balance Sheet, Not-Journaled) | Ditemukan bukti konkret dampak finansial dari bug [[../../erpApiServices/docs/TemuanTestCase/Sales/Ranahku/06-invoice-langsung-lunas-walau-payment-bill-masih-draft-belum-disetujui]]: total Accounts Receivable (Rp 20.288.600) PERSIS SAMA dengan jumlah 4 invoice yang benar-benar belum lunas — TIDAK termasuk `INV-S/0003` (Rp 500.000) yang salah tampil "Paid", padahal payment bill-nya sendiri masih draft. Piutang riil seharusnya Rp 20.788.600, bukan Rp 20.288.600 — bukti nyata bug ini "menyembunyikan" piutang dari radar finance |
| Core CMS pages (landing-banners, landing-leads, landing-team-members, landing-testimonials) | Dicek reachability lewat `permissionsIsMenu.json` | **Nol hasil (tidak terdaftar sebagai menu item untuk role manapun)** — diputuskan SKIP, tidak diuji, konsisten dengan pelajaran dari retraksi temuan Core/Users sebelumnya |

> **Status Tahap T (2026-09-15): SELESAI. 1 temuan SANGAT TINGGI baru** (Stock Adjustment tidak
> kirim unit_cost → ~87,6% inventory hilang dari dashboard/cost-ledger), **1 temuan TINGGI**
> diperkuat dengan bukti dampak nyata ke Accounting (invoice prematur "Paid" menyembunyikan
> piutang Rp 500.000), **1 temuan RENDAH** diperluas (translation key hilang muncul lagi di
> lokasi baru + 1 key baru), dan **3 kesimpulan "bukan bug"** setelah ditelusuri (dashboard umum
> `/dashboard`, Purchasing "Open PO"/`is_paid`, HRM "Headcount By Department") — konsisten dengan
> disiplin verifikasi-dulu-sebelum-lapor yang diterapkan sepanjang sesi.
>
> Detail lengkap di:
> [`erpApiServices/docs/TemuanTestCase/Umum/Ranahku/04-stock-adjustment-tidak-pernah-kirim-unit-cost-membuat-87-persen-nilai-inventory-hilang-dari-dashboard.id.md`](../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/04-stock-adjustment-tidak-pernah-kirim-unit-cost-membuat-87-persen-nilai-inventory-hilang-dari-dashboard.id.md),
> [`erpApiServices/docs/TemuanTestCase/Sales/Ranahku/06-invoice-langsung-lunas-walau-payment-bill-masih-draft-belum-disetujui.id.md`](../../erpApiServices/docs/TemuanTestCase/Sales/Ranahku/06-invoice-langsung-lunas-walau-payment-bill-masih-draft-belum-disetujui.id.md),
> [`erpApiServices/docs/TemuanTestCase/Canvassing/Ranahku/02-banyak-teks-belum-diterjemahkan.id.md`](../../erpApiServices/docs/TemuanTestCase/Canvassing/Ranahku/02-banyak-teks-belum-diterjemahkan.id.md).

---

## Ringkasan Sementara Sesi Pengujian (2026-09-15, per Tahap T — pengujian masih berlanjut)

Sesi ini telah menyelesaikan **Tahap G sampai T**, mencakup seluruh modul utama aplikasi
(Rental, Fixed Assets, Reports, Akuntansi Manual, Persediaan Lanjutan, Kanvasing Lanjutan, SDM
Lanjutan, Approval Requests, Finance & Administrasi Cabang, Restaurant penuh, Point of Sale,
Purchasing Blanket Agreements, sisa HRM/Core client-facing, Sales penuh, Inventory penuh, dan
seluruh 6 Dashboard per-modul: Sales, Inventory, Purchasing, POS, Restaurant, HRM, Canvassing,
Accounting). Dua temuan paling berdampak luas dari seluruh sesi:

1. **Endpoint `show()` di 18 controller berbeda (4 modul: Inventory, ClientMaster, Restaurant,
   Rental) SELALU error 500** akibat argumen `flexibleShow()` yang salah — pola kode identik
   tersalin berulang.
2. **Stock Adjustment tidak pernah mengirim `unit_cost` ke cost-layer ledger (`stock_lots`)** —
   ditemukan saat meninjau Inventory Dashboard, ternyata berdampak sampai ~87,6% dari total
   kuantitas stok riil cabang tidak tercatat di `stock_lots`, membuat Inventory Value On Hand,
   Dead Stock, dan COGS/Inventory Turnover di dashboard SEMUANYA salah besar — kemungkinan
   berdampak ke semua cabang yang saldo awal inventory-nya diinput lewat Stock Adjustment (alur
   onboarding standar).

Selain itu, pola **"Invalid Date"** akibat field backend yang sudah ISO datetime lengkap
ditambahi suffix waktu FE terkonfirmasi di 3 lokasi berbeda (Sales Deliveries, Stock Transfer
Shipments, Stock Adjustments), dan pola **suffix `_title`** pada 27+ translation key masih
menjadi temuan sistemik terluas dari sisi jumlah halaman terdampak. Temuan blocking/kritis lain
yang sudah terdokumentasi: sistem approval yang tidak pernah bisa dipakai, Rental Order macet,
Stock Take merusak data stok, Employee Transfer/Commission Rules/Expenses tidak bisa dibuat, Bank
Reconciliation tidak bisa Complete, Sales Payment Bill tidak bisa dibuat lewat UI, Sales Return
bisa dibuat untuk produk yang tidak pernah dijual tanpa batas kuantitas, invoice/SO langsung
"Paid" walau payment bill masih draft, dan produk jasa tidak bisa dijual lewat POS. Semua temuan
sudah didokumentasikan sebagai file terpisah di
`erpApiServices/docs/TemuanTestCase/{Modul}/Ranahku/`. **Pengujian dilanjutkan ke tahap
berikutnya sesuai instruksi untuk terus menguji sampai dinyatakan selesai** — kandidat lanjutan
mencakup audit ulang menyeluruh terhadap 30+ lokasi kandidat pola "Invalid Date" serta 18
controller `flexibleShow()` begitu tim BE mulai memperbaikinya.

---

## TAHAP U — Verifikasi Reachability Sisa Halaman Core System

**Konteks:** mengecek apakah 5 halaman Core system yang belum pernah disentuh (Currencies,
Languages, Permissions, Providers, Translations — semuanya di bawah `/core/*`) benar-benar bisa
dijangkau akun uji ini sebelum diuji, mengikuti disiplin dari pelajaran retraksi temuan
Core/Users sebelumnya.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Cek pendaftaran menu | Grep `permissionsIsMenu.json` untuk `core.currencies.list`, `core.languages.list`, `core.permissions.list`, `core.providers.list`, `core.translations.list` | Kelima slug TERDAFTAR sebagai menu item yang valid (untuk role tertentu) |
| Cek permission akun uji | `role/my-permissions` — dicek apakah kelima slug di atas ada di antara 1.118 permission yang dimiliki akun `lgrtaufit@gmail.com` | **TIDAK ADA satu pun dari kelima slug tersebut** — akun uji ini TIDAK memegang permission untuk 5 halaman Core system ini |
| Cek API langsung | `POST core/{currencies,languages,permissions,providers,translations}/list` | Semua mengembalikan **HTTP 403 "Access denied."** — konsisten dengan tidak adanya permission di atas |
| Cek halaman via URL langsung | Dibuka lewat `navigateTo` URL langsung (bukan lewat klik sidebar) | Halaman tetap RENDER (tombol "Add", kolom tabel) menampilkan "No data" — TAPI ini murni karena diakses lewat URL langsung, bukan bukti halaman ini muncul di sidebar untuk role ini |

> **Kesimpulan Tahap U: kelima halaman ini TIDAK REACHABLE untuk akun uji** (role saat ini
> genuinely tidak memegang permission-nya, bukan bug) — **diputuskan SKIP dari pengujian
> fungsional**, konsisten dengan disiplin reachability yang diterapkan sejak retraksi temuan
> Core/Users. Kode FE (`core/languages/index.vue`) sudah benar menangani error non-401 dengan
> menampilkan toast pesan error — tidak ditemukan bukti kegagalan silent yang bisa dikonfirmasi,
> jadi TIDAK ditulis sebagai temuan bug (sesuai disiplin: jangan lapor tanpa verifikasi pasti).
> `branch-menu-templates` yang disebut di ringkasan sebelumnya ternyata tidak ada sebagai halaman
> terpisah — yang ada hanya "Branch Menu" (`client-master.branch-menu.list`), sudah pernah diuji
> di tahap-tahap sebelumnya.
>
> **Update: Taufit memberikan akun kedua dengan akses Core penuh** (`lgrtaufit2@gmail.com`,
> perusahaan berbeda — "CORETAX", bukan "Ranahku") khusus untuk menguji fitur Core. Dikonfirmasi
> lewat akun ini bahwa kelima endpoint di atas normal (200 OK, ada datanya: Currencies 10 baris,
> Languages 2 baris, Permissions 1.374 baris, Providers 5 baris, Translations 10.570 baris) — jadi
> "No data" yang tampil di akun lama BENAR-BENAR karena tidak ada permission (403), bukan bug data.
> Akses baru ini juga dipakai untuk verifikasi silang beberapa temuan translation key yang sudah
> ada (lihat catatan di [[../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/01-pola-sistemik-translation-key-suffix-title-membuat-27-lebih-judul-halaman-rusak]] dan
> [[../../erpApiServices/docs/TemuanTestCase/Canvassing/Ranahku/02-banyak-teks-belum-diterjemahkan]])
> — hasilnya: temuan `_title` suffix terkonfirmasi nyata untuk versi Inggris (100% rusak di sampel
> yang dicek) dan SEBAGIAN versi Indonesia (beberapa key sudah diperbaiki tim dev, beberapa masih
> rusak dengan pola berbeda); sementara 2 dari 3 "key baru" yang tadinya dikira hilang di
> Canvassing Dashboard ternyata SEHAT di database — kemunculannya sebagai kode mentah cuma
> artefak cache browser sesi uji yang sudah berjalan berhari-hari, bukan bug — sudah dikoreksi di
> temuan terkait.

---

## TAHAP V — Core CMS & App Configuration (Akun Core Baru, Company CORETAX)

**Konteks:** akun `lgrtaufit2@gmail.com` (company berbeda — "CORETAX", bukan "Ranahku") ternyata
punya sidebar "App Configuration" penuh berisi puluhan halaman Core, termasuk 5 halaman Landing
CMS (Banners, Leads, Products, Team Members, Testimonials) yang sebelumnya diputuskan SKIP di
Tahap T karena tidak reachable untuk akun lama. Sesi ini memanfaatkan akses baru untuk menguji
sebagian di antaranya.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Landing Banners — validasi create | Buka "Tambah Banner", isi Judul+Subjudul, submit TANPA upload gambar | Validasi BENAR menolak dengan pesan "This Field Is Required" — gambar memang wajib untuk banner. Modal dibatalkan setelah verifikasi (tidak ada data uji tersisa) |
| Landing Testimonials — create penuh | Buat testimonial "Budi Santoso (QA Test)" tanpa foto (foto opsional di sini) | BERHASIL — record tersimpan dan tampil benar di list dengan status "Active". Data uji ini masih ada di company CORETAX, aman untuk dihapus/dibiarkan |
| Landing Leads, Landing Products, Landing Team Members | Dicek lewat API `list` saja | Ketiganya 200 OK, 0 data — belum sempat diuji create/edit penuh |
| Core Currencies/Languages/Permissions/Providers/Translations | Dicek lewat API `list` dengan akun baru | Semua 200 OK dengan data lengkap (10, 2, 1.374, 5, 10.570 baris) — mengonfirmasi temuan Tahap U bahwa "No data" di akun lama murni karena permission, BUKAN data kosong |
| Puluhan halaman App Configuration lain (Modules, Banks, Charge Type Templates, Family Relationships, App Setup, Approval Workflow Templates, Attachment, Branch Menu Templates, Branches, Chart Of Account Templates, Contact Templates, Fail Logs, Integration Configs, Login Logs, Notifications Monitor, Order Type Templates, Page Educations, Payment Method Templates, Price List Templates, Product Unit Templates, Roles, Status Templates, Stock Adjustment Reason Templates, Taxes Templates, Users, Activity Log Reviews, Module Packages) | — | **Belum sempat diuji** — kandidat lanjutan sesi berikutnya |

> **Status Tahap V (2026-09-15, sebagian — masih berlanjut)**: 2 halaman Landing CMS terverifikasi
> sehat (Banners validasi benar, Testimonials create-flow penuh berhasil). Tidak ada bug baru
> ditemukan di bagian yang sudah diuji. Cakupan App Configuration masih sangat luas dan belum
> selesai — dilanjutkan di sesi berikutnya per instruksi standing untuk terus menguji.

---

## TAHAP W — Audit Fail Logs (Temuan Baru Lewat Log Error Otomatis)

**Konteks:** akun Core (`lgrtaufit2@gmail.com`) punya akses ke halaman **Core > Fail Logs** —
log otomatis SETIAP request API yang gagal (bukan 2xx) di seluruh aplikasi, lebih dari 16.000
baris mencakup 2026-08-30 s.d. 2026-09-15. Alih-alih lanjut klik satu-satu ke puluhan halaman
App Configuration yang tersisa, log ini diaudit langsung lewat API untuk mencari pola error 500
yang belum ditemukan — jauh lebih efisien dan menghasilkan 2 temuan baru yang solid.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Audit status code | Ambil 16.332 baris, kelompokkan per `status_code` | 403: 48, 404: 15.493 (mayoritas bot/scanner eksternal — lihat catatan), 405: 563, 422: 111, **500: 117** |
| Audit unique error 500 | Dedupe 117 baris 500 jadi 48 pesan unik | Sebagian besar sudah cocok dengan temuan yang sudah ada (flexibleShow 18-controller, SalesInvoice items, RentalQuotations) — **5 pola BARU** ditemukan |
| Verifikasi pola baru #1 | Nama relasi salah di `additionalRelations` — Restaurant Orders/Tables/Bookings, Products, Journals | Dikonfirmasi lewat kode model (`TableOrder`, `TableBooking`, `RestaurantTable`, `Product`, `JournalHeader`) — nama relasi yang diminta FE memang tidak ada, ditulis jadi [[../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/05-pola-sistemik-nama-relasi-salah-di-additionalrelations-bikin-list-crash-500]] |
| Verifikasi pola baru #2 | 4 endpoint list (Purchase Orders, Sales Quotations/Orders/Invoices) crash 500 kalau `order_type` tidak valid | **Direproduksi langsung** lewat API (`order_type: "sideways"` → 500 persis sesuai log) — akar masalah ditelusuri sampai ke `IndexLogic::buildIndexQuery()` yang bisa return `JsonResponse` saat validasi gagal, tapi 4 controller pemanggil tidak menangani kemungkinan itu. Ditulis jadi [[../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/06-approvalengine-crash-500-kalau-parameter-sorting-list-tidak-valid]] |
| Pola lain yang dicek tapi TIDAK ditulis sebagai temuan | Beberapa SQL error Postgres lama (Agu 30 - Sep 9: `purchase-order-shipments`, `purchase-orders/show`, `product-skus/low-stock`) dan beberapa 404 rute yang mungkin salah (`sales/canvassing-*`, `hrm/payroll-periods/options`, dll) | SQL error lama sudah TIDAK reproduce lagi saat diuji ulang hari ini (kemungkinan sudah diperbaiki tim dev) — tidak dilaporkan tanpa bisa diverifikasi ulang. 404 rute mencurigakan tidak bisa dipastikan apakah bug FE asli atau sisa percobaan trial-and-error pengujian sendiri di hari-hari sebelumnya (tidak ada bukti kode pendukung) — tidak dilaporkan sesuai disiplin "jangan lapor tanpa verifikasi pasti" |
| Observasi keamanan (bukan bug aplikasi) | 15.493 dari 15.946 baris fail-log 404 adalah traffic scanner/bot eksternal (`config.env`, `wp-content/mysql.sql`, `stripe.js`, probe Kubernetes API `v1/secrets`/`v1/pods`, probe SonicWall `sonicos/*`, path traversal `../../../proc/self/environ`, dll) | Laravel BENAR mengembalikan 404 untuk semuanya (tidak ada yang berhasil dieksploitasi) — bukan bug, tapi worth diketahui Taufit: traffic ini menunjukkan aplikasi rutin di-scan bot otomatis di internet. Rekomendasi non-teknis: pertimbangkan WAF/rate-limiting kalau belum ada, dan pertimbangkan filter status_code di halaman Fail Logs (default cuma tampilkan 500) supaya sinyal bug asli tidak tenggelam di 15 ribu+ baris noise bot |

> **Status Tahap W (2026-09-15, sebagian): 3 temuan SANGAT BERGUNA baru** ditemukan lewat metode
> audit log (bukan klik UI manual) — jauh lebih efisien. Temuan ketiga:
> [[../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/07-error-handler-default-500-untuk-semua-jenis-kegagalan-termasuk-validasi-bisnis-biasa]]
> — helper `response()->json()->error()` default ke HTTP 500 untuk SEMUA jenis kegagalan
> (termasuk penolakan bisnis biasa seperti "Insufficient Leave Balance", "Link Is Invalid Or Has
> Expired"), bukan cuma crash beneran — merusak keandalan monitoring, bukan bug fungsional
> langsung. Metode audit Fail Logs ini direkomendasikan jadi bagian rutin QA ke depan. Puluhan
> halaman App Configuration lain (Modules, Banks, Roles, Users versi Core, Branches, dll) sudah
> dicek lewat API `list()` — semua 200 OK dengan data wajar, tidak ada yang error — tapi belum
> diuji CRUD penuh satu per satu (create/edit/delete). Dilanjutkan sesuai instruksi standing
> untuk terus menguji.

---

## TAHAP X — CRUD Penuh App Configuration (Akun Core) + Audit Kode Sistemik

**Konteks:** melanjutkan Tahap W dengan dua jalur sekaligus — (1) audit kode manual ke seluruh
controller Core App Configuration untuk pola bug sistemik (melanjutkan keberhasilan metode
audit-lewat-kode di Tahap W), dan (2) pengujian CRUD penuh langsung di browser (create/edit/delete
nyata, bukan cuma `list()`) di beberapa halaman representatif.

| Langkah | Detail | Hasil |
| --- | --- | --- |
| Cek banner "fail-open" di halaman Modules | Banner: *"A Provider With No Enabled Modules Is Not Gated And Every Permission Passes"* | **Dikonfirmasi BUKAN bug** — ditelusuri ke `app/Support/ModuleGate.php` dan `Core/Modules.php`, perilaku ini SENGAJA didesain untuk backward-compatibility (docblock eksplisit menjelaskan alasannya, ada design doc rujukan, FE sudah kasih warning sebelum provider di-set ke 0 modul). Tidak ditulis sebagai temuan. |
| Audit `deleteBulk()` di 12 controller Core Template/master-data | `ChargeTypeTemplates`, `OrderTypeTemplates`, `ChartOfAccountTemplates`, `ChartOfAccountTypeTemplates`, `ContactTemplates`, `PriceListTemplates`, `PaymentMethodTemplates`, `StatusTemplate`, `StockAdjustmentReasonTemplates`, `TaxesTemplates`, `ProductUnitTemplates`, `Permissions` | **12/12 TIDAK memanggil `ActivityLogger`** di `deleteBulk()` (mass `whereIn()->delete()` tanpa log), padahal method single `delete()` di file yang SAMA benar memanggilnya — ditulis jadi [[../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/08-endpoint-bulk-di-core-master-data-tidak-pernah-mencatat-activitylogger]]. `createBulk`/`updateBulk` di controller yang sama juga kena pola serupa (dampak lebih ringan). Ditemukan juga manifestasi terkait: `Banks::importCommit()` salah label update sebagai create di audit log. |
| Audit kredensial terenkripsi (`IntegrationConfig`, `IntegrationConfigBranch`) | Field `credentials`/`custom_credentials` di-cast `encrypted:array` dan sengaja di-mask sebelum dikirim ke FE | **Temuan keamanan TINGGI**: `ActivityLogger::log*()` dipanggil SEBELUM proses masking, dan cast `encrypted:array` otomatis mendekripsi nilai saat `toArray()` dipanggil ActivityLogger — akibatnya API key/secret asli (plaintext) tersimpan permanen di tabel `logs`, menembus baik enkripsi kolom maupun masking API. Ditulis jadi [[../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/09-activitylogger-menyimpan-credential-integrasi-plaintext-menembus-enkripsi-dan-masking]]. Rekomendasi rotasi kredensial yang sudah pernah diinput. |
| Uji CRUD penuh live — Core > Banks | Create → Update → Delete lewat UI sungguhan | Create ✅, Update ✅, tapi **Delete GAGAL** — toast "This Field Is Required", record tidak terhapus |
| Root-cause Delete gagal | Trace ke `useApi.ts` (`delete(path, body, options)` — body jadi request body langsung) vs pemanggilan FE `deleteApi(path, { body: { id } })` (pembungkus salah) | Request yang terkirim jadi `{"body":{"id":...}}`, bukan `{"id":...}` — validator BE selalu gagal. **Dikonfirmasi via `grep` pola sama di 10 file**: Banks, Branches, Providers, Currencies, Family Relationships, Landing Banners/Leads/Products/Team Members/Testimonials. Dibuktikan backend-nya sendiri BENAR (delete via API call manual dengan payload benar → sukses). Ditulis jadi [[../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/10-tombol-delete-tidak-berfungsi-di-10-halaman-core-karena-payload-body-salah-bungkus]] |
| Efek samping ditemukan saat uji Delete | Modal konfirmasi ($confirm/AppConfirmModal) menampilkan pesan dua kali | Root cause: `:description` prop UModal DAN slot `#body` sama-sama diisi variabel `message` yang sama. Dipakai di **107 file** lewat composable global — satu perbaikan di 1 komponen membereskan semua. Ditulis jadi [[../../erpApiServices/docs/TemuanTestCase/Umum/Ranahku/11-modal-konfirmasi-global-menampilkan-pesan-dua-kali]] |
| Uji CRUD penuh live — Core > Charge Type Templates | Create → Delete lewat UI sungguhan | Create ✅, Delete ✅ (berhasil, membuktikan bug Delete Banks TIDAK berlaku di semua halaman — cuma 10 file yang polanya salah) |
| Cleanup data uji | Bank test "999QA" (dibuat lewat UI, gagal dihapus lewat UI karena bug) | Dihapus manual lewat API call langsung dengan payload benar (`{id: 75}`) — berhasil, tabel `banks` bersih kembali |

> **Status Tahap X (2026-09-15, sebagian): 4 temuan baru**, dua di antaranya (Umum/09 kredensial
> plaintext, Umum/10 delete rusak total) tergolong **temuan paling signifikan sepanjang sesi
> pengujian ini** — satu isu keamanan nyata (kebocoran API key/secret ke tabel log), satu lagi
> pelumpuhan total fungsi Delete di 10 halaman admin inti. Kombinasi audit-kode-manual +
> reproduksi-langsung-di-browser terbukti sangat efektif: setiap temuan disertai baik root-cause
> di kode maupun bukti langsung (reproduksi UI atau panggilan API). Lanjut menguji sisa halaman
> App Configuration (Family Relationships, App Setup, Branches, Branch Menu Templates, Contact
> Templates, Chart of Account Templates/Types, Currencies, Order Type Templates, Page Educations,
> Payment Method Templates, Price List Templates, Product Unit Templates, Status Templates, Stock
> Adjustment Reason Templates, Taxes Templates, Users Core, Providers) plus Landing
> Leads/Products/Team Members create-flow yang belum sempat diuji di Tahap V — sesuai instruksi
> standing untuk terus lanjut.

---
