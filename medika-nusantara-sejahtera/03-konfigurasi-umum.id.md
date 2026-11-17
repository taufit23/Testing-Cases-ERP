---
title: (PT Medika Nusantara Sejahtera) — 03. Konfigurasi Umum dan Master Data
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul konfigurasi-umum untuk skenario PT Medika Nusantara Sejahtera. Master data dan pengaturan yang dipakai semua modul.
visibility: internal
---

# 03. Konfigurasi Umum dan Master Data

> **Kenapa bagian ini diuji (bahasa sederhana).** Mengisi pengaturan umum yang dipakai semua modul: mata uang, pajak, tahun fiskal, penomoran dokumen, dan sebagainya.
>
> **Kalau semuanya benar, artinya:** Dokumen yang dibuat kemudian bernomor, berpajak, dan berperiode dengan benar tanpa perlu dibetulkan manual.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Nomor dokumen memakai awalan dari pengaturan cabang dan unik per cabang.
- Status dokumen berasal dari master status per cabang dengan nama sesuai bahasa pengguna; mengganti nama status cabang tidak merusak terjemahan.
- Metode pembayaran dapat dipetakan ke akun buku besar sendiri; kosong berarti memakai akun kas/bank modul.
- Dropdown panjang bisa dicari; dropdown modul lain memakai sumber tanpa izin khusus (options), bukan halaman daftar.
- Impor Excel dan unduh template tersedia di master data berbaris banyak; header mengikuti bahasa pengguna dan impor menerima bahasa mana pun.

## 1. Mata Uang (Currencies) — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/01-mata-uang.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/01-mata-uang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah mata uang default IDR (draf) | Klik "+ Buat"; isi Country Name "Indonesia", Currency Name "Rupiah", Currency Code "IDR", Symbol "Rp"; atur Thousand Separator ".", Decimal Separator ",", Decimal Places 0; klik Save | Mata uang IDR ditambahkan dan jadi default |
| Negatif — Mencoba hapus mata uang default (draf) | Cari mata uang IDR, klik menu aksi → Set as Default; coba klik tombol Delete | Tampil pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mata uang yang sedang default tidak bisa dihapus/diubah kodenya secara sembarangan (tombol tertentu otomatis nonaktif) — ganti dulu default ke mata uang lain kalau memang perlu menghapus yang lama |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Warehouse — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/02-warehouse.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/02-warehouse.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Warehouse Store (draf) | Klik "+ Buat"; Isi Name "Apotek Nusantara Bandung", Code "APB", Phone "0221000101"; Pilih Type "Toko"; Pilih Business Unit "Kantor Pusat & Distribusi Jakarta"; Isi alamat; Klik Save | Warehouse APB ditambahkan dan terhubung dengan Business Unit Kantor Pusat & Distribusi Jakarta |
| Negatif — Tidak bisa Save tipe Store (draf) | Tidak memilih Business Unit; Coba klik Save | Muncul pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Warehouse bertipe Store wajib dihubungkan ke Business Unit. Ini bukan cuma label administratif — hubungan ini yang memungkinkan laporan keuangan dipecah per toko (lihat manual book Akuntansi 02. Jurnal Manual, dimensi Business Unit) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Kalau Store, pilih Business Unit (wajib) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Kategori & Satuan Produk — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/03-kategori-dan-satuan-produk.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/03-kategori-dan-satuan-produk.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Buat kategori "Obat" & unit "Pcs"; masukkan produk Paracetamol 500 mg strip (SKU OBT-001) | Produk ditambahkan dengan kategori dan unit yang benar, proses sukses |
| Negatif — input salah (draf) | Mencoba membuat produk tanpa memasukkan kategori/unit; masukkan produk Paracetamol 500 mg strip (SKU OBT-001) | Tampilan pesan error: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Client Master → Product Categories (/client-master/product-categories) dan Client Master → Product Units (/client-master/product-units) · Kerjakan sebelum membuat Product Catalog — kategori dan satuan adalah field wajib saat membuat produk/SKU |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satuan (unit) dipakai per SKU — misalnya "Pcs", "Kg", "Dus", "Box". Setiap SKU wajib punya satu unit dasar |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Metode Pembayaran & Tipe Order — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/04-metode-pembayaran-dan-tipe-order.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/04-metode-pembayaran-dan-tipe-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah metode pembayaran untuk Apotek Nusantara Bandung (draf) | Klik "+ Buat", masukkan "QRIS DANA" sebagai Name, tandai Is Cash false, aktifkan Is Active, klik Save | Metode pembayaran QRIS DANA muncul di halaman Payment Methods |
| Negatif — Mencoba menghapus metode pembayaran kartu debit BCA (draf) | Coba hapus metode "Kartu Debit BCA" tanpa mematikan Is Active | Tidak bisa menghapus, pesan: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Fiscal Year & Accounting Period — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/05-fiscal-year-dan-accounting-period.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/05-fiscal-year-dan-accounting-period.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat FY baru (draf) | Klik "+ Buat"; Code: "FY2026", Name: "Fiscal Year 2026", Start Date: 1 Januari 2026, End Date: 31 Desember 2026; Klik Save | Tampilan Success Message, FY "FY2026" ditambahkan |
| Negatif — Generate Periods untuk FY yang sudah ada (draf) | Cari FY "FY2025", klik Generate Periods; Duration Type: Bulanan | Pesan pesan yang jelas muncul, tidak membuat periode baru |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi Start Date dan End Date — biasanya satu tahun penuh, tapi tidak wajib mengikuti kalender Januari-Desember (bisa Juli-Juni kalau tahun buku perusahaan berbeda) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Generate Periods tidak bisa dijalankan dua kali untuk Fiscal Year yang sama — kalau sudah pernah di-generate, sistem menampilkan pesan bahwa periode sudah ada (beserta jumlahnya), bukan menduplikasi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap jurnal (manual maupun otomatis dari Purchasing/Sales/POS) memerlukan Accounting Period yang aktif dan belum closed/locked untuk tanggal transaksinya — kalau belum ada periode yang meng-cover tanggal tersebut, posting jurnal akan ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Status Setup — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/06-status-setup.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/06-status-setup.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengubah warna status pada Purchase Order (draf) | Buka halaman Statuses; pilih "purchase_orders"; ubah warna menjadi merah; simpan | Warna badge status Purchase Order berubah menjadi merah, tidak mempengaruhi status alur kerja |
| Negatif — Menyebutkan status baru di field status PO (draf) | Masuk ke form PO; masukkan status "Menunggu Persetujuan" yang belum ada; coba simpan | Muncul pesan kesalahan: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Permissions — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/07-permissions.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/07-permissions.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menelusuri permission klinik (draf) | Buka halaman Permissions; Filter Module 'sales' | Daftar permission sales muncul, termasuk URL & tipe aksi |
| Negatif — Mencoba menambah permission baru (draf) | Cari tombol Create/Edit pada halaman Permissions; Klik | Tampilan pesan penolakan yang jelas muncul |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. App Setup & Integration Configs — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/08-app-setup-dan-integration-configs.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/08-app-setup-dan-integration-configs.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah setup default global (draf) | Klik "Tambah Pengaturan"; isi Setup Key "app_name"; pilih Type "String"; masukkan Value "Medika Nusantara Sejahtera"; klik Save. | Nilai default "app_name" Medika Nusantara Sejahtera ditambahkan ke App Setup dan berlaku untuk semua cabang. |
| Negatif — Mengedit setup dengan kredensial salah (draf) | Cari baris "Payment Gateway"; isi API Key dengan string yang tidak valid; aktifkan Active; klik Update. | Muncul pesan kesalahan tentang kredensial tidak valid dan konfigurasi tidak diperbarui. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Setup Key (nama identitas, misalnya "appname") — tidak bisa diubah lagi setelah entri dibuat |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Cost Centers — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/09-cost-centers.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/09-cost-centers.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Cost Center Pabrik (draf) | Klik "+ Buat"; Isi Code: HRB01, Name: Divisi Produksi; Pilih Parent: Divisi Umum; Klik Save | Cost Center baru Divisi Produksi ditambahkan dengan status "Aktif" |
| Negatif — Menambah Cost Center tanpa Parent (draf) | Klik "+ Buat"; Isi Code: HRB02, Name: Divisi Penjualan; Tidak memilih Parent; Klik Save | Muncul pesan error: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Product Catalog — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/10-product-catalog.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/10-product-catalog.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat SKU produk Paracetamol 500 mg strip (draf) | Buka Products; klik "+ Buat"; isi Name "Paracetamol 500 mg strip"; pilih Category; tambah SKU Code "OBT-001", Name "Paracetamol 500 mg strip", Unit "Pcs"; klik Save. | Produk Paracetamol 500 mg strip dengan SKU OBT-001 berhasil dibuat dan tersedia untuk transaksi. |
| Negatif — Mengatur harga produk tanpa membuat SKU terlebih dahulu (draf) | Buka detail produk Paracetamol 500 mg strip; klik "Kelola Harga"; coba atur harga tanpa ada SKU yang dipilih. | Tampil pesan error "SKU is required" dan tidak bisa mengatur harga. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Kontak (Supplier & Customer) — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/11-kontak-supplier-dan-customer.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/11-kontak-supplier-dan-customer.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambahkan supplier baru (draf) | Buka menu Contacts; klik "+ Tambah"; pilih "Tambah Kontak"; isikan Type: Supplier, Name: PT Bintang Farmasi Utama, Email: bintangfarmasi@bfu.com, Phone: 021-5550102, Currency: IDR; klik Save | Kontak PT Bintang Farmasi Utama berhasil ditambahkan dengan data sesuai input |
| Negatif — Menambahkan supplier tanpa email (draf) | Buka menu Contacts; klik "+ Tambah"; pilih "Tambah Kontak"; isikan Type: Supplier, Name: PT Alkes Prima Mandiri, Phone: 021-5550101; coba klik Save tanpa mengisi Email | Muncul pesan kesalahan meminta input email untuk kontak Supplier |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Klik "+ Tambah", pilih Contact yang dituju (wajib), lalu isi: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Account Number, Account Holder — wajib diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Type kontak membatasi kemunculannya di modul lain. Kontak Supplier hanya bisa dipilih sebagai supplier di Purchasing; kontak Customer hanya muncul di Sales/POS; Both muncul di kedua sisi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. User dan Role — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/12-user-dan-role.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/12-user-dan-role.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat role kasir baru (draf) | Buka menu Roles; klik "+ Tambah Peran"; isikan Name "Kasir", Description "Role untuk staf kasir", Status Active; klik Create | Role "Kasir" muncul dalam daftar roles dengan status Active, permission default 0 |
| Negatif — Menambahkan action yang tidak ada (draf) | Buka menu Roles; pilih role "Admin Gudang"; klik Assign Permissions; ceklist Action Permission "Perbarui" pada modul "accounting"; klik Save | Muncul pesan error pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Password dan Password Confirmation — wajib saat membuat user baru |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Status (Active/Inactive) — user Inactive tidak bisa login |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | User Inactive tidak bisa login, tapi datanya (dan riwayat aktivitas yang tercatat atas namanya) tetap tersimpan — pola ini lebih aman dipakai daripada menghapus user |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Pajak & Daftar Harga

Bab manual: [`konfigurasi-umum/13-pajak-dan-daftar-harga.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/13-pajak-dan-daftar-harga.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal bab ini | Ikuti langkah di bab manual dengan data acuan file `00` (draf Ollama tidak dapat dipakai, isi manual) | Hasil sesuai uraian bab |
| Negatif — input tidak valid | Kosongkan field wajib atau isi di luar batas | Ditolak dengan pesan yang jelas, tidak ada data tersimpan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 14. Manajemen Cabang (Branch) — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/14-manajemen-cabang.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/14-manajemen-cabang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat cabang baru (draf) | Buka Client Master → Branch Manage; Klik "+ Tambah Cabang"; Isi Nama Cabang: "Apotek Nusantara Bandung", Alamat: Jl. Bandung 123, Provinsi: DKI Jakarta, Kota/Kabupaten: Jakarta Pusat, Kecamatan: Gambir, Kelurahan/Desa: Gambir, Kode Pos: 10110; Klik Save | Cabang pesan yang jelas ditambahkan dengan status aktif dan tampil di daftar cabang |
| Negatif — Menugaskan staff ke cabang yang belum ada (draf) | Coba menugaskan user "Kasir A" ke cabang "Klinik Pratama", tetapi cabang ini belum dibuat; Klik Assign User, pilih Kasir A, Aktifkan Active in Branch, klik Assign | Muncul pesan kesalahan: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satu cabang tidak bisa sekaligus jadi Main Branch dan melapor ke Main Branch lain — kalau sudah jadi Main Branch, opsi "Melaporkan Ke" otomatis terkunci, begitu juga sebaliknya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Cabang yang sudah punya cabang lain melapor kepadanya tidak bisa diubah untuk melapor ke Main Branch lain (hierarki hanya 1 tingkat, tidak berjenjang) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Atur Active in Branch — kalau dimatikan, user tetap tercatat terhubung ke cabang tapi tidak bisa memilihnya sebagai cabang aktif |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap item/grup punya tombol Edit (ubah nama, ikon, kata kunci pencarian, status collapse default) dan Delete lewat ikon yang muncul saat hover. Grup yang masih berisi item tidak bisa dihapus — pindahkan atau hapus dulu semua isinya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 15. Produk Lanjutan — Varian (SKU), Modifier, dan Resep

Bab manual: [`konfigurasi-umum/15-produk-lanjutan-varian-modifier-dan-resep.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/15-produk-lanjutan-varian-modifier-dan-resep.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah SKU Satuan (draf) | Buka Client Master → Product SKUs; klik "+ Tambah"; pilih Produk induk "Paracetamol 500 mg strip", isi Kode SKU OBT-001, Nama Paracetamol 500 mg, Satuan Botol, upload gambar obat, tandai Status aktif; klik Save | SKU baru OBT-001 ditambahkan dengan detail dan status yang benar |
| Negatif — Menambah Modifier Tanpa Jenis (draf) | Buka Client Master → Product Modifiers; klik "+ Tambah"; isi Nama "Extra Cheese", tanpa memilih Jenis Modifier, masukkan Price Adjustment 5000; coba klik Save | Muncul pesan kesalahan menyebutkan perlu memilih jenis modifier sebelum menyimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 5. Aktifkan Required kalau modifier ini wajib dipilih setiap kali item terkait dijual (misalnya wajib pilih ukuran) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 6. Minimal satu bahan wajib diisi — baris terakhir tidak bisa dihapus kalau cuma tersisa satu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 16. Cash Register & Sales Channel — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/16-cash-register-dan-sales-channel.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/16-cash-register-dan-sales-channel.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah cash register untuk klinik (draf) | Buka Client Master → Cash Registers; klik "+ Tambah"; masukkan Name "Kasir 1", Code "KR01", Store "Klinik Pratama & Laboratorium Bekasi", Cashiers allowed "Kasir A", Notes "Meja utama"; klik Create | Cash register "Kasir 1" ditambahkan dengan status Active, terkunci ke perangkat pertama yang membuka sesi di meja ini |
| Negatif — Menambah cash register melebihi batas paket langganan (draf) | Buka Client Master → Cash Registers; klik "+ Tambah"; masukkan Name "Kasir 2", Code "KR02", lainnya sama; klik Create | Sistem menolak penambahan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Opsional, pilih Store — toko (warehouse bertipe Store) tempat meja ini berjualan. Kalau diisi, sesi di meja ini hanya bisa dibuka untuk toko itu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau jumlah cash register sudah mencapai batas paket langganan, penambahan baru akan ditolak sistem — hubungi admin platform untuk menaikkan paket kalau butuh lebih banyak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau perangkat diganti atau hilang, klik menu pada baris → Release The Locked Device; perangkat berikutnya yang membuka meja itu yang akan terkunci. Meja yang sedang punya sesi terbuka tidak bisa dilepas kuncinya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Usulan hanya usulan. Tidak ada yang tersimpan sebelum Anda menekan Terapkan, dan setiap akun yang diusulkan divalidasi harus salah satu kandidat saluran itu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 17. Kurs Mata Uang per Cabang (Exchange Rates)

Bab manual: [`konfigurasi-umum/17-kurs-mata-uang-per-cabang.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/17-kurs-mata-uang-per-cabang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah kurs baru (draf) | Buka Client Master → Exchange Rates; Pilih Currency: Rupiah; Isi Rate Date 1 Januari 2023; Isi Rate to Base 15000; Aktifkan Active; Klik Create | Kurs baru untuk Rupiah dengan tanggal dan nilai tukar yang dimasukkan ditambahkan, kurs ini menjadi aktif |
| Negatif — Download kurs otomatis tidak bisa diklik (draf) | Buka Client Master → Exchange Rates; Belum memilih Currency; Coba klik ikon download cloud | Muncul pesan penolakan yang jelas pada form |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Klik menu titik tiga pada baris kurs → Edit. Field Currency dan Rate Date terkunci setelah dibuat (tidak bisa diubah) — hanya Rate to Base dan status Active yang bisa diedit |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 18. Pengaturan Tampilan PDF (PDF Layout Settings)

Bab manual: [`konfigurasi-umum/18-pengaturan-tampilan-pdf.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/18-pengaturan-tampilan-pdf.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengatur Tampilan PDF (draf) | Kantor Pusat; A4; Portrait; Nama "Medika Nusantara Sejahtera"; Alamat "Jl. Tebet Blok R No.10 Jakarta"; Logo dari CV Kapur Medika; Warna aksen "#333333"; Menyimpan perubahan | Tampilan PDF dokumen sesuai dengan pengaturan yang diinginkan, logo dan warna aksen teraplikasikan |
| Negatif — Kode Warna Invalid (draf) | Kantor Pusat; Accent Color "FF0000"; Save | Tombol Save gagal, muncul pesan error pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Signature Label — teks label di atas kolom tanda tangan (misalnya "Hormat kami") — hanya bisa diisi kalau Show Signature Block aktif |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 19. Denominasi Uang dan Deposit Kasir

Bab manual: [`konfigurasi-umum/19-denominasi-uang-dan-deposit-kasir.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/19-denominasi-uang-dan-deposit-kasir.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Pecahan Uang (draf) | Klik Add Denomination; Isi Denomination 10000, Type Bill, Sort Order 5, Active checked; Klik Create | Pecahan 10000 ditampilkan di daftar dengan status active dan urutan sesuai |
| Negatif — Menghapus Pecahan Uang yang Pernah Dipakai (draf) | Cek pecahan 10000; Klik Delete; Konfirmasi hapus; Coba hapus kembali | Muncul pesan penolakan yang jelas dan tidak dapat dihapus |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Denomination (nilai pecahan; wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Pilih Type: Bill (uang kertas) atau Coin (koin); wajib |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Edit pada baris membuka dialog Edit Denomination; simpan dengan Update. Delete menghapus setelah konfirmasi, tetapi pecahan yang pernah dipakai dalam penghitungan tidak bisa dihapus; nonaktifkan saja dengan mematikan Active |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Di dialog Refund in Cash, isi Amount (wajib), yaitu jumlah yang dibayarkan kembali. Isi Notes kalau perlu. Dialog menjelaskan bahwa kasir dibayar kembali dari laci kas dan saldo depositnya berkurang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 20. Tipe Dokumen Legal dan Permintaan Data Pribadi

Bab manual: [`konfigurasi-umum/24-dokumen-legal-dan-permintaan-data-pribadi.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/24-dokumen-legal-dan-permintaan-data-pribadi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah jenis dokumen (draf) | Klik Add; isi Name "Perjanjian Layanan", Description "Perjanjian layanan antara perusahaan"; set Status Active; klik Create | Tampilan berhasil menambah Perjanjian Layanan ke daftar Legal Document Types |
| Negatif — Menganonimkan data karyawan (draf) | Klik Anonymize pada baris Direktur Medika Nusantara Sejahtera; cek I understand this cannot be undone, klik Cancel | Muncul pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Dialog Anonymize This Person menjelaskan bahwa nama, kontak, dan data pribadi lain diganti dengan kode netral dan tidak bisa dibatalkan. Centang I understand this cannot be undone |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 21. Tata Letak Menu dan Log Pribadi

Bab manual: [`konfigurasi-umum/25-tata-letak-menu-dan-log-pribadi.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/25-tata-letak-menu-dan-log-pribadi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Grup Menu (draf) | Masuk ke halaman `/client-master/menu-layout`, klik `Grup Baru`, isi nama "Obat", ikon, dan bahasa, lalu klik Create | Grup "Obat" ditambahkan dengan menu yang sesuai |
| Negatif — Menghapus Menu Tidak Aktif (draf) | Coba hapus item "Kafe Sehat" di grup "Layanan Klinik", tanpa mengubah statusnya ke Inactive | Pesan pesan yang jelas muncul |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 22. Pergerakan Stok

Bab manual: [`konfigurasi-umum/26-pergerakan-stok.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/26-pergerakan-stok.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat pergerakan stok (draf) | Klik Record Stock Movement; Pilih Kantor Pusat & Distribusi Jakarta; Pilih Paracetamol 500 mg strip (SKU OBT-001); Pilih In; Isi Quantity 20; Klik Save | Pergerakan stok ditambahkan dengan status saved, jumlah stok berubah sesuai input |
| Negatif — Input quantity kurang dari nol (draf) | Klik Record Stock Movement; Pilih Kantor Pusat & Distribusi Jakarta; Pilih Paracetamol 500 mg strip (SKU OBT-001); Pilih In; Isi Quantity -5; Klik Save | Muncul pesan penolakan yang jelas dan pergerakan stok tidak ditambahkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Pilih Warehouse dan Product Sku (keduanya wajib; kalau kosong muncul pesan Warehouse is required atau Product Sku is required) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Isi Quantity; harus lebih besar dari nol (kalau tidak, muncul pesan Quantity must be greater than zero) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 23. Gambar Produk Massal dan Saran Gambar dari Internet

Bab manual: [`konfigurasi-umum/27-gambar-produk-massal-dan-saran-gambar.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/27-gambar-produk-massal-dan-saran-gambar.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Unggah gambar massal produk baru (draf) | Seret 20 file gambar; isi nama, kategori, satuan, harga; klik konfirmasi | Produk baru dibuat dengan gambar terlekat, stok awal dan buffer stock kosong |
| Negatif — Input kata pencarian tidak sesuai (draf) | Buka "Suggest Images", masukkan kata pencarian yang salah; pilih gambar; klik "Terapkan gambar terpilih" | Pesan galat: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 24. Diagram Urutan Setup Awal Cabang — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/28-diagram-urutan-setup-awal.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/28-diagram-urutan-setup-awal.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Setup cabang baru (draf) | Pilih menu "Setup Cabang", masukkan nama "Kantor Pusat & Distribusi Jakarta"; pilih mata uang Rupiah; klik "Simpan" | Nama cabang muncul di daftar, status menjadi "Siap" |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bab ini merangkum urutan menyiapkan sebuah cabang dalam bentuk gambar. "bab 05" artinya bab 05. Fiscal Year dan Accounting Period. Urutan ini disarankan, dan langkah yang benar-benar wajib sebelum dokumen tertentu bisa dibuat diberi catatan di bawah diagram |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Urutan di atas disarankan. Anda tidak harus mengerjakannya persis berurutan, tetapi syarat di tabel harus terpenuhi sebelum dokumen terkait bisa dibuat atau dibukukan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
