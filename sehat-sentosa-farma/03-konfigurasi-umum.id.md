---
title: (PT Sehat Sentosa Farma) — 03. Konfigurasi Umum dan Master Data
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul konfigurasi-umum untuk skenario PT Sehat Sentosa Farma. Master data dan pengaturan yang dipakai semua modul.
visibility: internal
---

# 03. Konfigurasi Umum dan Master Data

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** **Dr. Rahmat** (admin klien). Bagian ini membuat data master, jadi kerjakan **sebelum** transaksi apa pun. Template yang dipakai datang dari owner (file `02` bagian 3 dan 4).

**Cabang aktif:** Pusat dulu; ulangi bagian yang bersifat per cabang (mata uang, gudang, tahun fiskal, pajak) di tiap cabang lain.

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- Nomor dokumen memakai awalan dari pengaturan cabang dan unik per cabang.
- Status dokumen berasal dari master status per cabang dengan nama sesuai bahasa pengguna; mengganti nama status cabang tidak merusak terjemahan.
- Metode pembayaran dapat dipetakan ke akun buku besar sendiri; kosong berarti memakai akun kas/bank modul.
- Dropdown panjang bisa dicari; dropdown modul lain memakai sumber tanpa izin khusus (options), bukan halaman daftar.
- Impor Excel dan unduh template tersedia di master data berbaris banyak; header mengikuti bahasa pengguna dan impor menerima bahasa mana pun.

## 1. Mata Uang (Currencies) — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/01-mata-uang.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/01-mata-uang.md)

**Input di:** `Client Master → Currencies` (`/client-master/currencies`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi mata uang (draf) | Pilih Rupiah sebagai mata uang default, atur pemisah ribuan dengan koma dan desimal dengan titik | Pengaturan berhasil, tampilan konfirmasi dengan setting yang diubah |
| Negatif — Input mata uang tidak dikenali (draf) | Coba masukkan Yuan China, sistem menolak dan memberikan pesan penolakan yang jelas | Pendaftaran ditolak dengan pesan kesalahan jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mata uang yang sedang default tidak bisa dihapus/diubah kodenya secara sembarangan (tombol tertentu otomatis nonaktif) — ganti dulu default ke mata uang lain kalau memang perlu menghapus yang lama |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Warehouse — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/02-warehouse.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/02-warehouse.md)

**Input di:** `Client Master → Warehouses` (`/client-master/warehouses`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Membuat gudang Sentosa Farma dengan tipe Central, terkait dengan Business Unit Jakarta; menambah lokasi Kantor Pusat & Distribusi Jakarta | Gudang berhasil dibuat dan terkait dengan Business Unit yang benar |
| Negatif — input salah (draf) | Mencoba membuat gudang dengan tipe Store tanpa menghubungkannya ke Business Unit, input lokasi salah | Input ditolak karena harus menentukan tipe Warehouse dan menghubungkannya dengan Business Unit yang tepat, disertai pesan kesalahan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Warehouse bertipe Store wajib dihubungkan ke Business Unit. Ini bukan cuma label administratif — hubungan ini yang memungkinkan laporan keuangan dipecah per toko (lihat manual book Akuntansi 02. Jurnal Manual, dimensi Business Unit) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Kalau Store, pilih Business Unit (wajib) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Kategori & Satuan Produk — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/03-kategori-dan-satuan-produk.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/03-kategori-dan-satuan-produk.md)

**Input di:** `Client Master → Product Categories` (`/client-master/product-categories`) dan `Client Master → Product Units` (`/client-master/product-units`).

**Perhatikan:** **Kerjakan sebelum membuat Product Catalog** — kategori dan satuan adalah field wajib saat membuat produk/SKU.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Membuat kategori "Obat" dan satuan "pcs", "dus"; mengimpor data dari Excel; berhasil membuat kategori & satuan produk | Kategori & satuan produk terkonfigurasi dengan benar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Client Master → Product Categories (/client-master/product-categories) dan Client Master → Product Units (/client-master/product-units) · Kerjakan sebelum membuat Product Catalog — kategori dan satuan adalah field wajib saat membuat produk/SKU |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satuan (unit) dipakai per SKU — misalnya "Pcs", "Kg", "Dus", "Box". Setiap SKU wajib punya satu unit dasar |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Metode Pembayaran & Tipe Order — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/04-metode-pembayaran-dan-tipe-order.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/04-metode-pembayaran-dan-tipe-order.md)

**Input di:** `Client Master → Payment Methods` (`/client-master/payment-methods`) dan `Client Master → Order Types` (`/client-master/order-types`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menambahkan metode pembayaran QRIS dan tipe order dine-in di Apotek Sentosa Bandung | Metode pembayaran QRIS ditampilkan dalam daftar dan tipe order dine-in dapat dipilih saat transaksi |
| Negatif — input salah (draf) | Menghapus kode pos dari alamat pelanggan Klinik Pratama & Laboratorium Bekasi | Input tidak valid, pesan penolakan yang jelas dan tidak dapat disimpan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Fiscal Year & Accounting Period — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/05-fiscal-year-dan-accounting-period.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/05-fiscal-year-dan-accounting-period.md)

**Input di:** `Client Master → Fiscal Year` (`/client-master/fiscal-year`).

**Perhatikan:** **Kerjakan ini SEBELUM ada jurnal/saldo awal apa pun** — lihat manual book Akuntansi _01. Setup Master Data & Saldo Awal_ untuk konteks lebih lengkap, dan _04. Tutup Periode & Tahun Fiskal_ untuk proses closing-nya.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Tahun Fiskal (draf) | Input periode fiskal: 1 April 2023 s/d 31 Maret 2024; Konfirmasi detail; Generate Accounting Period | Accounting Period untuk setiap bulan terbentuk dengan benar |
| Negatif — Input Periode Salah (draf) | Input: 1 Januari 2023 s/d 31 Desember 2022; Konfirmasi | Tahun Fiskal ditolak, pesan: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi Start Date dan End Date — biasanya satu tahun penuh, tapi tidak wajib mengikuti kalender Januari-Desember (bisa Juli-Juni kalau tahun buku perusahaan berbeda) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Generate Periods tidak bisa dijalankan dua kali untuk Fiscal Year yang sama — kalau sudah pernah di-generate, sistem menampilkan pesan bahwa periode sudah ada (beserta jumlahnya), bukan menduplikasi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap jurnal (manual maupun otomatis dari Purchasing/Sales/POS) memerlukan Accounting Period yang aktif dan belum closed/locked untuk tanggal transaksinya — kalau belum ada periode yang meng-cover tanggal tersebut, posting jurnal akan ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Status Setup — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/06-status-setup.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/06-status-setup.md)

**Input di:** `Client Master → Statuses` (`/client-master/statuses`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Status Setup (draf) | Input status draft untuk Paracetamol 500 mg strip (SKU OBT-001) | Berhasil disimpan dengan status draft |
| Negatif — Status Setup (draf) | Mencoba menginput status "Belum Disetujui" pada Paracetamol 500 mg strip (SKU OBT-001) | Tidak bisa diinput, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Permissions — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/07-permissions.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/07-permissions.md)

**Input di:** `Client Master → Permissions` (`/client-master/permissions`).

**Perhatikan:** **Terkait:** manual book _Manual Book New Client → 01. Mendaftarkan Client Baru_ (langkah "Buat Role Akses").

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Memilih permission pesan yang jelas dan menyimpan | Role terkonfigurasi dengan permission yang tepat untuk Apoteker Penanggung Jawab |
| Negatif — input salah (draf) | Menghapus permission "Kepala Gudang" tanpa memilihnya terlebih dahulu | Perubahan role ditolak karena syarat konfigurasi tidak terpenuhi: permission belum dipilih |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. App Setup & Integration Configs — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/08-app-setup-dan-integration-configs.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/08-app-setup-dan-integration-configs.md)

**Input di:** `Core → App Setup` (`/core/app-setup`) dan `Core → Integration Configs` (`/core/integration-configs`).

**Perhatikan:** **Catatan**: dua halaman ini biasanya dikerjakan sekali di awal oleh tim teknis/admin platform, bukan bagian dari operasional harian staff cabang.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Setup (draf) | Tambahkan detail app baru; pilih opsi global; simpan | Konfigurasi berhasil ditambahkan secara default |
| Negatif — Input Kredensial Salah (draf) | Masukkan kredensial tidak valid; coba lagi dengan data yang benar | Pengisian kredensial gagal, muncul pesan kesalahan validasi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Setup Key (nama identitas, misalnya "appname") — tidak bisa diubah lagi setelah entri dibuat |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Cost Centers — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/09-cost-centers.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/09-cost-centers.md)

**Input di:** `Finance → Cost Centers` (`/finance/cost-centers`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal | membuat Cost Center induk 'Operasional', lalu Cost Center 'Gudang' dengan induk 'Operasional' (form berisi kode, nama, induk, deskripsi, status aktif; tidak ada isian Business Unit) | struktur Cost Center terbentuk dengan hierarki induk-anak yang benar |
| Negatif — input salah | mencoba menyimpan Cost Center dengan nama dikosongkan | sistem menolak dan menyatakan nama wajib diisi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Product Catalog — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/10-product-catalog.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/10-product-catalog.md)

**Input di:** `Client Master → Products` (`/client-master/products`).

**Prasyarat:** Product Categories, Product Units, dan Chart of Accounts sudah ada (lihat chapter _03. Kategori & Satuan Produk_).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Membuat produk Paracetamol 500 mg strip (SKU OBT-001), mengatur harga Rp2.000, menambahkan gambar, dan mengatur buffer stock 10-50 | Produk ditambahkan dengan detail benar, harga dan gambar terkait, buffer stock berhasil diset |
| Negatif — input salah (draf) | Mengatur buffer stock tanpa menentukan minimal atau maksimal | Tidak dapat menyimpan buffer stock, muncul pesan kesalahan tentang syarat wajib yang belum terpenuhi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Kontak (Supplier & Customer) — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/11-kontak-supplier-dan-customer.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/11-kontak-supplier-dan-customer.md)

**Input di:** `Client Master → Contacts` (`/client-master/contacts`).

**Prasyarat:** Tidak ada — halaman ini bisa langsung diakses begitu punya akses ke branch.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Kontak Baru (draf) | Buat kontak baru untuk PT Bintang Farmasi Utama; isi data nama, alamat, rekening bank; simpan | Berhasil membuat kontak dengan data lengkap dan valid |
| Negatif — Import Excel Data Salah (draf) | Import file Excel dengan format tidak sesuai; pesan kesalahan muncul mengingatkan tentang format yang benar | Tidak dapat melakukan import karena data tidak sesuai, menerima pesan kesalahan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Klik "+ Add", pilih Contact yang dituju (wajib), lalu isi: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Account Number, Account Holder — wajib diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Type kontak membatasi kemunculannya di modul lain. Kontak Supplier hanya bisa dipilih sebagai supplier di Purchasing; kontak Customer hanya muncul di Sales/POS; Both muncul di kedua sisi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. User dan Role — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/12-user-dan-role.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/12-user-dan-role.md)

**Input di:** `Client Master → Users` (`/client-master/users`) dan `Client Master → Roles` (`/client-master/roles`).

**Prasyarat:** Tidak ada, tapi lihat chapter _07. Permissions_ untuk detail daftar permission per fitur sebelum bikin role baru.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Akun Login (draf) | Buat user baru dengan detail: nama, username, password, role 'Kasir' | User Kasir berhasil dibuat dan memiliki akses sesuai role |
| Negatif — Input Username Duplikat (draf) | Coba buat user dengan username yang sudah digunakan | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Password dan Password Confirmation — wajib saat membuat user baru |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Status (Active/Inactive) — user Inactive tidak bisa login |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | User Inactive tidak bisa login, tapi datanya (dan riwayat aktivitas yang tercatat atas namanya) tetap tersimpan — pola ini lebih aman dipakai daripada menghapus user |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Pajak & Daftar Harga

Bab manual: [`konfigurasi-umum/13-pajak-dan-daftar-harga.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/13-pajak-dan-daftar-harga.md)

**Input di:** `Client Master → Taxes` (`/client-master/taxes`) · `Client Master → Price Lists` (`/client-master/price-lists`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — membuat pajak PPN (draf) | masukkan kode PPN, tarif 10%, sifat penerimaan otomatis | pajak berhasil ditambahkan ke entitas |
| Negatif — input harga produk negatif (draf) | masukkan harga produk sebagai angka negatif | pengisian gagal, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 14. Manajemen Cabang (Branch) — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/14-manajemen-cabang.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/14-manajemen-cabang.md)

**Input di:** `Client Master → Branch Manage` (`/client-master/branch-manage`).

**Prasyarat:** akun sudah login sebagai admin/pemilik provider (yang berhak membuat cabang baru).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Cabang Baru (draf) | Input data cabang baru: Apotek Sentosa Bandung; konfigurasi sukses; tampilan dashboard cabang baru muncul | Cabang pesan yang jelas terdaftar dan dapat diakses |
| Negatif — Menugaskan Staff ke Cabang (draf) | Menginput staff tanpa memilih cabang aktif terlebih dahulu; pesan error: pesan yang jelas | Tidak dapat menugaskan staff ke cabang karena syarat tidak terpenuhi, muncul pesan kesalahan jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satu cabang tidak bisa sekaligus jadi Main Branch dan melapor ke Main Branch lain — kalau sudah jadi Main Branch, opsi "Reports To" otomatis terkunci, begitu juga sebaliknya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Cabang yang sudah punya cabang lain melapor kepadanya tidak bisa diubah untuk melapor ke Main Branch lain (hierarki hanya 1 tingkat, tidak berjenjang) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Atur Active in Branch — kalau dimatikan, user tetap tercatat terhubung ke cabang tapi tidak bisa memilihnya sebagai cabang aktif |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap item/grup punya tombol Edit (ubah nama, ikon, kata kunci pencarian, status collapse default) dan Delete lewat ikon yang muncul saat hover. Grup yang masih berisi item tidak bisa dihapus — pindahkan atau hapus dulu semua isinya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 15. Produk Lanjutan — Varian (SKU), Modifier, dan Resep

Bab manual: [`konfigurasi-umum/15-produk-lanjutan-varian-modifier-dan-resep.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/15-produk-lanjutan-varian-modifier-dan-resep.md)

**Input di:** `Client Master → Product SKUs` (`/client-master/product-skus`), `Client Master → Product Modifiers` (`/client-master/product-modifiers`), `Client Master → Product Recipes` (`/client-master/product-recipes`).

**Prasyarat:** Produk induk dan Satuan Produk sudah dibuat — lihat chapter _10. Product Catalog_ dan _03. Kategori dan Satuan Produk_.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Varian Produk (draf) | Menambah SKU Paracetamol 500 mg strip (OBT-001) dengan ukuran kecil dan besar; atur harga bertingkat; tambah modifier topping alpukat dan stroberi untuk menu kafe | Varian baru ditambahkan dengan harga dan modifier yang sesuai |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 5. Aktifkan Required kalau modifier ini wajib dipilih setiap kali item terkait dijual (misalnya wajib pilih ukuran) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 6. Minimal satu bahan wajib diisi — baris terakhir tidak bisa dihapus kalau cuma tersisa satu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 16. Cash Register & Sales Channel — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/16-cash-register-dan-sales-channel.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/16-cash-register-dan-sales-channel.md)

**Input di:** `Client Master → Cash Registers` (`/client-master/cash-registers`) dan `Client Master → Sales Channels` (`/client-master/sales-channels`).

**Prasyarat:** modul terkait (POS/Penjualan) sudah aktif untuk branch ini.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Cash Register (draf) | Tambahkan "Jakarta1" untuk kantor pusat & distribusi Jakarta; konfigurasi berhasil | Meja kasir "Jakarta1" ditambahkan dengan status aktif |
| Negatif — Mengunci Meja Kasir (draf) | Coba mengunci "Jakarta1" ke perangkat yang sudah terkunci; menerima pesan error | Meja kasir tidak bisa dikunci kembali, tetap terkunci pada perangkat tertentu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Opsional, pilih Store — toko (warehouse bertipe Store) tempat meja ini berjualan. Kalau diisi, sesi di meja ini hanya bisa dibuka untuk toko itu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau jumlah cash register sudah mencapai batas paket langganan, penambahan baru akan ditolak sistem — hubungi admin platform untuk menaikkan paket kalau butuh lebih banyak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau perangkat diganti atau hilang, klik menu pada baris → Release The Locked Device; perangkat berikutnya yang membuka meja itu yang akan terkunci. Meja yang sedang punya sesi terbuka tidak bisa dilepas kuncinya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 17. Kurs Mata Uang per Cabang (Exchange Rates)

Bab manual: [`konfigurasi-umum/17-kurs-mata-uang-per-cabang.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/17-kurs-mata-uang-per-cabang.md)

**Input di:** `Client Master → Exchange Rates` (`/client-master/exchange-rates`).

**Prasyarat:** mata uang asing yang mau dipakai sudah terdaftar di **Client Master → Currencies** (lihat chapter _01. Mata Uang_) dan cabang sudah punya mata uang dasar (base/reporting currency).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Kurs Baru (draf) | Tambah kurs USD dengan tgl 1 Januari 2023, nilai 14500 Rupiah | Kurs baru muncul dalam daftar kurs cabang Sentosa Farma |
| Negatif — Nilai Kurs Salah (draf) | Masukkan nilai kurs USD 14500000, syarat kurang dari 14500 | Tampilan error: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Klik menu titik tiga pada baris kurs → Edit. Field Currency dan Rate Date terkunci setelah dibuat (tidak bisa diubah) — hanya Rate to Base dan status Active yang bisa diedit |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 18. Pengaturan Tampilan PDF (PDF Layout Settings)

Bab manual: [`konfigurasi-umum/18-pengaturan-tampilan-pdf.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/18-pengaturan-tampilan-pdf.md)

**Input di:** `Client Master → PDF Layout Settings` (`/client-master/pdf-layout-settings`).

**Prasyarat:** tidak ada — halaman ini bersifat konfigurasi satu-record per cabang (bukan daftar), langsung menampilkan form pengaturan.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengatur tampilan PDF (draf) | Pilih "Kop Suratpesan yang jelasTampilanpesan yang jelasTotal Harga" di "Tabel Item"; simpan perubahan. | Tampilan PDF sesuai dengan desain Sentosa Farma, termasuk logo, warna biru, dan kolom total harga. |
| Negatif — Input logo tidak valid (draf) | Masukkan file gambar logo yang terlalu besar; pesan penolakan yang jelas. | Pengaturan ditolak dengan pesan ukuran file logo melebihi batas maksimum. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Signature Label — teks label di atas kolom tanda tangan (misalnya "Hormat kami") — hanya bisa diisi kalau Show Signature Block aktif |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 19. Denominasi Uang dan Deposit Kasir

Bab manual: [`konfigurasi-umum/19-denominasi-uang-dan-deposit-kasir.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/19-denominasi-uang-dan-deposit-kasir.md)

**Input di:** `Client Master → Cash Denominations` (`/client-master/cash-denominations`) · `Client Master → Cashier Deposits` (`/client-master/cashier-deposits`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Pecahan (draf) | Tambah denominasi Rp10.000 untuk kasir Apotek Sentosa Bandung; Simpan perubahan | Denominasi baru ditampilkan dalam daftar denominasi |
| Negatif — Input Saldo Negatif (draf) | Masukkan saldo kasir Apotek Sentosa Bandung sebagai -500.000; Simpan perubahan | Muncul pesan kesalahan pesan yang jelas dan input ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Denomination (nilai pecahan; wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Pilih Type: Bill (uang kertas) atau Coin (koin); wajib |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Edit pada baris membuka dialog Edit Denomination; simpan dengan Update. Delete menghapus setelah konfirmasi, tetapi pecahan yang pernah dipakai dalam penghitungan tidak bisa dihapus; nonaktifkan saja dengan mematikan Active |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Di dialog Refund in Cash, isi Amount (wajib), yaitu jumlah yang dibayarkan kembali. Isi Notes kalau perlu. Dialog menjelaskan bahwa kasir dibayar kembali dari laci kas dan saldo depositnya berkurang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 20. Pola Transaksi

Bab manual: [`konfigurasi-umum/23-pola-transaksi.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/23-pola-transaksi.md)

**Input di:** `Client Master → Transaction Patern Types` (`/client-master/transaction-patern-types`) · `Client Master → Transaction Paterns` (`/client-master/transaction-paterns`). **Catatan: bab manual ini menyatakan halamannya sudah tidak ada di aplikasi; kasus di bagian ini kemungkinan tidak berlaku.**

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Tipe Transaksi (draf) | Klik "Tambah Tipe", isi nama "Retur Obatpesan yang jelasPenjualan", konfirmasi | Tampilan berhasil menambahkan tipe transaksi Retur Obat pada Transaction Patern Types |
| Negatif — Menghapus Tipe Tanpa Konfirmasi (draf) | Coba hapus tanpa klik "Hapus" | Muncul notifikasi kesalahan karena syarat menghapus tidak terpenuhi, tidak mengubah data |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 5. Atur Optional Step: User Can Remove (langkah boleh dihapus pengguna) atau Required (wajib ada) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 21. Tipe Dokumen Legal dan Permintaan Data Pribadi

Bab manual: [`konfigurasi-umum/24-dokumen-legal-dan-permintaan-data-pribadi.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/24-dokumen-legal-dan-permintaan-data-pribadi.md)

**Input di:** `Client Master → Legal Document Types` (`/client-master/legal-document-types`) · `Client Master → Personal Data Requests` (`/client-master/data-subject-requests`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Tambah Jenis Dokumen (draf) | Klik "Tambahpesan yang jelasSurat Perintah", pilih tipe dokumen, simpan | Jenis dokumen Surat Perintah ditambahkan dengan benar |
| Negatif — Input Nama Kosong (draf) | Masukkan data tanpa nama, klik "Simpan" | Terjadi kesalahan, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Dialog Anonymize This Person menjelaskan bahwa nama, kontak, dan data pribadi lain diganti dengan kode netral dan tidak bisa dibatalkan. Centang I understand this cannot be undone |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 22. Tata Letak Menu dan Log Pribadi

Bab manual: [`konfigurasi-umum/25-tata-letak-menu-dan-log-pribadi.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/25-tata-letak-menu-dan-log-pribadi.md)

**Input di:** `Client Master → Menu Layout` (`/client-master/menu-layout`) · `Client Master → My Activity Log` (`/client-master/personal-logs`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Tata Letak Menu (draf) | Membuat tata letak, mengatur urutan dan grup, menambah item, mengubah dan menghapus entitas dengan benar; membaca log aktivitas | Tampilan menu sesuai desain, log aktivitas tercatat dengan lengkap |
| Negatif — Log Pribadi (draf) | Mengakses halaman yang dikunci tanpa izin; memasukkan data log yang tidak valid | Halaman terkunci ditolak pesan penolakan yang jelas; input invalid ditolak pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 23. Pergerakan Stok

Bab manual: [`konfigurasi-umum/26-pergerakan-stok.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/26-pergerakan-stok.md)

**Input di:** `Client Master → Inventory` (`/client-master/inventory`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Inputkan SKU OBT-001, jumlah 50 kotak, tanggal 2023-10-01, lakukan penerimaan stok di halaman Inventory | Stok OBT-001 bertambah 50 kotak pada tanggal 2023-10-01 |
| Negatif — input salah (draf) | Inputkan SKU tidak tersedia, jumlah 100 kotak, tanggal 2023-10-01, lakukan penerimaan stok di halaman Inventory | Tidak dapat disimpan, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Pilih Warehouse dan Product Sku (keduanya wajib; kalau kosong muncul pesan Warehouse is required atau Product Sku is required) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Isi Quantity; harus lebih besar dari nol (kalau tidak, muncul pesan Quantity must be greater than zero) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
