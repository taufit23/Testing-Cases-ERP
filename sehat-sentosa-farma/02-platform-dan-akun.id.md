---
title: (PT Sehat Sentosa Farma) — 02. Platform Owner, Mulai Menggunakan dan Pengaturan Akun
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul platform-owner, mulai-menggunakan, pengaturan-akun untuk skenario PT Sehat Sentosa Farma. Dari penjualan aplikasi ke klien sampai pengguna pertama masuk.
visibility: internal
---

# 02. Platform Owner, Mulai Menggunakan dan Pengaturan Akun

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** Bagian 1 sampai 8: **Pemilik Platform** (login akun owner, bukan akun Dr. Rahmat). Bagian 9: siapa saja, termasuk tanpa login. Bagian 10: **Dr. Rahmat**.

**Cabang aktif:** tidak berlaku (tingkat platform); bagian 10 di cabang mana saja.

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- Paket menentukan modul dan batas (cabang, pengguna, karyawan); modul di luar paket hilang dari menu dan endpoint-nya 403.
- Onboard Client membuat provider, cabang pertama, peran dan pengguna awal; data klien tidak pernah terlihat klien lain.
- Penangguhan klien menutup login dan semua API (kecuali keluar) serta halaman publik klien; pemulihan mengembalikan semuanya tanpa kehilangan data.
- Ganti role Admin wajib PIN owner; role yang baru ditambahkan belum aktif sampai diaktifkan (izin hanya dihitung dari role aktif).
- Kata sandi, 2FA dan batas percobaan masuk.

## 1. Provider, Cabang, Pengguna, Peran, Izin, dan Lisensi

Bab manual: [`platform-owner/01-provider-cabang-pengguna-dan-peran.md`](../../erpApiServices/docs/manualBook/platform-owner/01-provider-cabang-pengguna-dan-peran.md)

**Input di:** `Core → Providers` (`/core/providers`) · `Core → Branch Offices` (`/core/branches`) · `Core → Users` (`/core/users`) · `Core → Roles` (`/core/roles`) · `Core → Permissions` (`/core/permissions`) · `Core → Licenses` (`/core/licenses`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Cabang (draf) | Tambah cabang "Surabaya", alamat "Jl. Surabaya", tipe klinik | Cabang "Surabaya" ditambahkan dengan detail yang benar |
| Negatif — Input Alamat Kosong (draf) | Tambah cabang "Malang", alamat kosong, tipe klinik | Input ditolak karena alamat tidak boleh kosong, pesan: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kolom wajib yang kosong menghasilkan pesan seperti Please fill all required provider fields atau Role name is required |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Customer Name (wajib) dan Email pelanggan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Pilih jenis lisensi: Subscription (berbatas waktu; wajib diberi tanggal kedaluwarsa, kalau tidak muncul A subscription license needs an expiry date) atau Perpetual (tanpa kedaluwarsa) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Klik Download License File pada baris untuk mengunduh berkas lisensi, lalu kirim ke pelanggan untuk dipasang. Edit Or Renew mengubah atau memperpanjang lisensi, tetapi setiap perubahan menandatangani ulang lisensi sehingga pelanggan harus memasang berkas baru |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Paket, Langganan, Harga, Modul, dan Mitra

Bab manual: [`platform-owner/02-paket-langganan-dan-mitra.md`](../../erpApiServices/docs/manualBook/platform-owner/02-paket-langganan-dan-mitra.md)

**Input di:** `Core → Subscription Plans` (`/core/subscription-plans`) · `Core → Subscriptions` (`/core/subscriptions`) · `Core → Billing Prices` (`/core/billing-prices`) · `Core → Module Packages` (`/core/module-packages`) · `Core → Modules` (`/core/modules`) · `Core → Partners` (`/core/partners`) · `Core → Partner Verification` (`/core/partner-overview`) · `Core → Partner Statements` (`/core/partner-statements`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Paket (draf) | Input data lengkap untuk paket baru; konfirmasi berhasil membuat paket | Paket baru terdaftar dengan detail sesuai input |
| Negatif — Input Harga Nol (draf) | Masukkan harga nol pada modul; pesan kesalahan karena harga tidak boleh nol | Tidak dapat menyimpan paket, muncul notifikasi pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Name (wajib), Icon, Order (urutan tampil), dan Description. Atur Active In Catalog agar paket muncul di pilihan onboarding |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Modul infrastruktur yang selalu aktif ditampilkan terpisah (Always-on infrastructure modules) dan tidak bisa dimatikan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Name (wajib), Contact Person, Email, Phone, dan Notes |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mitra yang masih punya klien, atau sudah punya riwayat tagihan, tidak bisa dihapus; nonaktifkan saja. Rekap bulanan tiap mitra ada di Partner Statements, dan pemeriksaan angka bersama mitra di Partner Verification |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Template Master Data: Keuangan dan Akuntansi

Bab manual: [`platform-owner/03-template-keuangan-dan-akuntansi.md`](../../erpApiServices/docs/manualBook/platform-owner/03-template-keuangan-dan-akuntansi.md)

**Input di:** `Core → Chart Of Accounts Templates` (`/core/chart-of-account-templates`) · `Core → Chart Of Accounts Type Templates` (`/core/chart-of-account-type-templates`) · `Core → Taxes Templates` (`/core/taxes-templates`) · `Core → Payment Method Templates` (`/core/payment-method-templates`) · `Core → Price List Templates` (`/core/price-list-templates`) · `Core → Charge Type Templates` (`/core/charge-type-templates`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Template Bagan Akun (draf) | Inputkan kode akun, nama, dan type; Simpan | Tampilan template baru di Chart Of Accounts Templates |
| Negatif — Input Kode Akun Sama (draf) | Masukkan kode yang sudah ada; Coba Simpan | Pesan pesan yang jelas muncul |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Template Master Data: Operasional, Status, dan Menu

Bab manual: [`platform-owner/04-template-operasional.md`](../../erpApiServices/docs/manualBook/platform-owner/04-template-operasional.md)

**Input di:** `Core → Status Templates` (`/core/status-templates`) · `Core → Approval Workflow Templates` (`/core/approval-workflow-templates`) · `Core → Branch Menu Template` (`/core/branch-menu-templates`) · `Core → Contact Templates` (`/core/contact-templates`) · `Core → Order Type Templates` (`/core/order-type-templates`) · `Core → Product Unit Templates` (`/core/product-unit-templates`) · `Core → Stock Adjustment Reason Templates` (`/core/stock-adjustment-reason-templates`) · `Core → Attendance Status Templates` (`/core/attendance-status-templates`) · `Core → Employment Type Templates` (`/core/employment-type-templates`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Template Status (draf) | Masukkan nama "Stok Habispesan yang jelasProduksi", klik simpan | Berhasil menambahkan template status baru |
| Negatif — Menghapus Template Alur Persetujuan Tanpa Konfirmasi (draf) | Coba hapus tanpa konfirmasi, tidak memilih template | Muncul pesan kesalahan tentang perlunya konfirmasi terlebih dahulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pastikan untuk mengisi semua field wajib sebelum menambahkan template status |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kode tidak dapat diubah setelah template dibuat karena logika absensi, penggajian, dan cuti bergantung pada kode tersebut |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Code tidak dapat diubah setelah template dibuat. Cabang memakai kode ini sebagai titik awal untuk tipe kepegawaian dalam HRM |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Konten Landing Page

Bab manual: [`platform-owner/05-konten-landing-page.md`](../../erpApiServices/docs/manualBook/platform-owner/05-konten-landing-page.md)

**Input di:** `Core → Landing Settings` (`/core/landing-settings`) · `Core → Landing Banners` (`/core/landing-banners`) · `Core → Landing Features` (`/core/landing-features`) · `Core → Landing Pricing Plans` (`/core/landing-pricing-plans`) · `Core → Landing Products` (`/core/landing-products`) · `Core → Landing Testimonials` (`/core/landing-testimonials`) · `Core → Landing Clients` (`/core/landing-clients`) · `Core → Landing Faqs` (`/core/landing-faqs`) · `Core → Landing Team Members` (`/core/landing-team-members`) · `Core → Landing Owner Profile` (`/core/landing-owner-profile`) · `Core → Landing Leads` (`/core/landing-leads`) · `Core → Landing Seo Pages` (`/core/landing-seo-pages`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengubah Pengaturan (draf) | Mengubah domain menjadi sehatfarma.id; menyimpan perubahan | Domain Landing Page berubah menjadi sehatfarma.id |
| Negatif — Menambah Banner dengan URL kosong (draf) | Menambah banner tanpa URL; mendapatkan pesan kesalahan | Harus mengisi URL untuk banner yang ditambahkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Unggah Gambar Banner (wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 6. Pilih Search Engine Instruction: boleh diindeks dan diikuti tautannya, atau salah satu kombinasi yang melarang indeks atau pengikutan tautan. Halaman yang dilarang diindeks tidak masuk sitemap dan ditutup di robots.txt |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 7. Isi Structured Data (JSON-LD) bila Anda memakainya. Isinya harus JSON yang valid; kalau tidak, penyimpanan ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Sistem: Terjemahan, Bahasa, Data Acuan, Lampiran, dan Log

Bab manual: [`platform-owner/06-sistem-bahasa-data-acuan-dan-log.md`](../../erpApiServices/docs/manualBook/platform-owner/06-sistem-bahasa-data-acuan-dan-log.md)

**Input di:** `Core → Translations` (`/core/translations`) · `Core → Languages` (`/core/languages`) · `Core → Page Educations` (`/core/page-educations`) · `Core → Attachments` (`/core/attachment`) · `Core → Banks` (`/core/banks`) · `Core → Currencies` (`/core/currencies`) · `Core → Family Relationships` (`/core/family-relationships`) · `Core → Failed Request Logs` (`/core/fail-logs`) · `Core → Login Logs` (`/core/login-logs`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Terjemahan (draf) | Menambahkan terjemahan "English" untuk halaman "About Us" di Sentosa Farma | Terjemahan berhasil ditambahkan dan dapat dilihat di panel admin |
| Negatif — Bahasa Sudah Ada (draf) | Mencoba menambahkan bahasa "Indonesia" yang sudah ada | Pesan kesalahan pesan yang jelas muncul dan tidak dapat disimpan ulang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Dashboard Platform, Langganan, dan Monitor Notifikasi

Bab manual: [`platform-owner/07-dashboard-platform-owner-dan-langganan.md`](../../erpApiServices/docs/manualBook/platform-owner/07-dashboard-platform-owner-dan-langganan.md)

**Input di:** `Dashboard → Platform Dashboard` (`/dashboard/core`) · `Dashboard → Subscription dashboard` (`/dashboard/subscriptions`) · `Dashboard → Notifications Monitor` (`/dashboard/notifications`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Dashboard Platform (draf) | Memeriksa angka utama, grafik penjualan, daftar langganan aktif | Angka utama akurat, grafik menunjukkan tren penjualan, langganan terdaftar dengan benar |
| Negatif — Notifications Monitor (draf) | Menginput notifikasi tidak relevan | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Klik Approve untuk menyetujui, atau Reject untuk menolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Akun Gateway Platform dan Kode Kanal Transfer Bank

Bab manual: [`platform-owner/08-akun-gateway-platform-dan-kode-kanal-bank.md`](../../erpApiServices/docs/manualBook/platform-owner/08-akun-gateway-platform-dan-kode-kanal-bank.md)

**Input di:** `Core → Platform Gateway Accounts` (`/core/platform-gateway-accounts`) · `Core → Bank Gateway Codes` (`/core/bank-gateway-codes`) · hanya untuk **pemilik platform**..

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Input akun gateway platform dan kode kanal bank yang benar; cek manual pembayaran berhasil; transfer keluar sesuai kebutuhan | Proses pembayaran berjalan lancar; notifikasi sukses diterima |
| Negatif — input salah (draf) | Input akun gateway atau kode kanal bank salah; sistem menolak transaksi dengan pesan kesalahan validasi | Sistem menampilkan pesan error dan tidak memproses transfer, mengarahkan untuk memeriksa kembali data yang dimasukkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penting: bank yang belum punya kode kanal tidak dapat menerima transfer dari penyedia itu; baris transfer ke bank tersebut diblokir. Kolom Banks linked menunjukkan berapa bank yang sudah terhubung |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Masuk ke Aplikasi, Pusat Bantuan, dan Riwayat Perubahan

Bab manual: [`mulai-menggunakan/01-login-bantuan-dan-riwayat-perubahan.md`](../../erpApiServices/docs/manualBook/mulai-menggunakan/01-login-bantuan-dan-riwayat-perubahan.md)

**Input di:** `Login → Login` (`/auth/login`) · `Help → Support` (`/help`) · `Changelog → Changelog` (`/changelog`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Masuk ke Aplikasi (draf) | Login dengan akun valid; Verifikasi dua langkah berhasil; Sesi berakhir setelah waktu tertentu | Berhasil masuk dan menggunakan aplikasi sesuai hak akses akun |
| Negatif — Masuk ke Aplikasi (draf) | Input password salah; Tidak ada verifikasi dua langkah; Waktu login melebihi batas | Ditolak pesan penolakan yang jelas atau pesan yang jelas dan diminta untuk login kembali |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Pengaturan Akun Saya: Tampilan, Keamanan, dan Langganan

Bab manual: [`pengaturan-akun/01-pengaturan-akun-saya.md`](../../erpApiServices/docs/manualBook/pengaturan-akun/01-pengaturan-akun-saya.md)

**Input di:** `Settings → Settings` (`/settings`) · `Settings → Appearance` (`/settings/appearance`) · `Settings → Security` (`/settings/security`) · `Settings → Subscription` (`/settings/subscription`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengaturan Akun Saya (draf) | Mengakses halaman Settings, mengubah password, memverifikasi dua langkah, dan menyimpan perubahan dengan sukses | Perubahan disimpan, tampilan akun diperbarui, verifikasi dua langkah aktif |
| Negatif — Keamanan Sentosa Farma (draf) | Mengganti password dengan kata sandi yang terlalu pendek atau tidak memenuhi syarat keamanan, menerima pesan kesalahan | Pengubahan ditolak, tetap menggunakan password lama, tampilan error menunjukkan syarat yang belum terpenuhi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Ubah Name (minimal 2 karakter) dan Email (harus berformat email yang valid) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi New Password (minimal 8 karakter, harus berbeda dari yang lama) dan Confirm Password (harus sama) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Save these recovery codes now: tiap kode hanya bisa dipakai sekali dan satu-satunya jalan masuk bila ponsel hilang; kode tidak ditampilkan lagi. Gunakan Copy all, lalu klik I saved them |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
