---
title: (PT Sehat Sentosa Farma) — 03. Konfigurasi Umum dan Master Data
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul konfigurasi-umum untuk skenario PT Sehat Sentosa Farma. Master data dan pengaturan yang dipakai semua modul.
visibility: internal
---

# 03. Konfigurasi Umum dan Master Data

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
| Positif — Menambah Mata Uang Default (draf) | Tambah mata uang Rupiah sebagai default di kantor pusat; konfirmasi berhasil ditambahkan | Konfigurasi default Rupiah terlihat di semua cabang |
| Negatif — Menggunakan Simbol Mata Uang Salah (draf) | Coba tambahkan yuan China (¥) sebagai default; sistem menolak dan memberikan pesan penolakan yang jelas | Tambahan mata uang ditolak dengan pesan kesalahan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mata uang yang sedang default tidak bisa dihapus/diubah kodenya secara sembarangan (tombol tertentu otomatis nonaktif) — ganti dulu default ke mata uang lain kalau memang perlu menghapus yang lama |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Warehouse — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/02-warehouse.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/02-warehouse.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Membuat gudang Sentosa Farma dengan tipe Central di Jakarta; menghubungkan dengan Business Unit Klinik Pratama Bekasi; menambah lokasi gudang di Sukabumi untuk pabrik herbal | Gudang dan Business Unit terkait berhasil dibuat, lokasi gudang ditambahkan |
| Negatif — input salah (draf) | Mencoba membuat gudang dengan tipe Store tanpa menghubungkannya ke Business Unit; menambah lokasi gudang tanpa memilih tipe | Input gagal, pesan penolakan yang jelas dan pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Warehouse bertipe Store wajib dihubungkan ke Business Unit. Ini bukan cuma label administratif — hubungan ini yang memungkinkan laporan keuangan dipecah per toko (lihat manual book Akuntansi 02. Jurnal Manual, dimensi Business Unit) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Kalau Store, pilih Business Unit (wajib) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Kategori & Satuan Produk — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/03-kategori-dan-satuan-produk.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/03-kategori-dan-satuan-produk.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menambahkan kategori "Obat" dan satuan "pcs", lalu membuat produk Paracetamol 500 mg strip (SKU OBT-001) dengan satuan pcs | Produk berhasil ditambahkan dengan kategori dan satuan yang benar |
| Negatif — input salah (draf) | Mencoba menambahkan kategori tidak ada dan satuan "ton" untuk produk Paracetamol, tanpa membuat kategori terlebih dahulu | Tidak dapat disimpan, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Client Master → Product Categories (/client-master/product-categories) dan Client Master → Product Units (/client-master/product-units) · Kerjakan sebelum membuat Product Catalog — kategori dan satuan adalah field wajib saat membuat produk/SKU |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satuan (unit) dipakai per SKU — misalnya "Pcs", "Kg", "Dus", "Box". Setiap SKU wajib punya satu unit dasar |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Metode Pembayaran & Tipe Order — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/04-metode-pembayaran-dan-tipe-order.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/04-metode-pembayaran-dan-tipe-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menambahkan metode pembayaran QRIS pada POS; mengonfigurasi tipe order dine-in di klinik | Metode pembayaran QRIS terdaftar dan tipe order dine-in aktif untuk transaksi klinik |
| Negatif — input salah (draf) | Menghapus semua metode pembayaran tanpa menyisakan satu; mencoba melakukan transaksi dine-in di apotek | Tampilan error menunjukkan bahwa minimal satu metode pembayaran harus tersedia, transaksi dine-in tidak dapat dilakukan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Fiscal Year & Accounting Period — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/05-fiscal-year-dan-accounting-period.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/05-fiscal-year-dan-accounting-period.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Tahun Fiskal (draf) | Input tahun fiskal 2023-2024, generate period Januari-Desember 2023 | Sukses membuat tahun fiskal 2023-2024 dengan 12 period bulanan. |
| Negatif — Input Tahun Fiskal Sama (draf) | Menginput tahun fiskal 2023-2023, mencoba generate period | Gagal, sistem menolak input dan pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi Start Date dan End Date — biasanya satu tahun penuh, tapi tidak wajib mengikuti kalender Januari-Desember (bisa Juli-Juni kalau tahun buku perusahaan berbeda) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Generate Periods tidak bisa dijalankan dua kali untuk Fiscal Year yang sama — kalau sudah pernah di-generate, sistem menampilkan pesan bahwa periode sudah ada (beserta jumlahnya), bukan menduplikasi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap jurnal (manual maupun otomatis dari Purchasing/Sales/POS) memerlukan Accounting Period yang aktif dan belum closed/locked untuk tanggal transaksinya — kalau belum ada periode yang meng-cover tanggal tersebut, posting jurnal akan ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Status Setup — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/06-status-setup.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/06-status-setup.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Status Setup (draf) | Masukkan "draft" ke kolom status untuk SKU OBT-001 | Status SKU OBT-001 berubah menjadi draft |
| Negatif — Status Setup (draf) | Menginput "belum disetujui" ke kolom status untuk SKU OBT-001 | Input ditolak pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Permissions — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/07-permissions.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/07-permissions.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menyusun role untuk Apoteker Penanggung Jawab dengan memberikan permission "Input Resep" dan pesan yang jelas | Role berhasil disusun dengan permission yang diberikan sesuai harapan |
| Negatif — input salah (draf) | Mencoba menyusun role tanpa memberikan apapun permission | Pemakaian permission kosong ditolak pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. App Setup & Integration Configs — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/08-app-setup-dan-integration-configs.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/08-app-setup-dan-integration-configs.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Setup (draf) | Tambahkan detail App Setup untuk Sentosa Farma; konfigurasi default global | Konfigurasi berhasil ditambahkan dengan detail yang benar |
| Negatif — Input Kredensial Salah (draf) | Masukkan kredensial payment gateway yang salah untuk Sentosa Farma | Tolakan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Setup Key (nama identitas, misalnya "appname") — tidak bisa diubah lagi setelah entri dibuat |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Cost Centers — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/09-cost-centers.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/09-cost-centers.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Membuat Cost Center "Gudangpesan yang jelasKantor Pusat", menambahkan biaya gaji staf gudang; | Struktur Cost Center berjenjang terbentuk dengan benar, biaya terkategorikan sesuai. |
| Negatif — input salah (draf) | Mencoba membuat Cost Center tanpa memilih Cost Center induk; | Tidak dapat membuat Cost Center, pesan penolakan yang jelas. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Product Catalog — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/10-product-catalog.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/10-product-catalog.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Membuat produk Paracetamol 500 mg strip (SKU OBT-001), mengatur harga Rp 4.000, menambahkan gambar, dan menetapkan buffer stock minimal 20, maksimal 50 | Produk berhasil ditambahkan dengan detail sesuai input |
| Negatif — input salah (draf) | Menetapkan harga produk Paracetamol 500 mg strip (SKU OBT-001) di bawah Rp 1.000 tanpa memasukkan alasan | Input harga tidak valid, harus lebih dari Rp 1.000 dan alasan diperlukan untuk penyesuaian harga di bawah batas minimum |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Kontak (Supplier & Customer) — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/11-kontak-supplier-dan-customer.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/11-kontak-supplier-dan-customer.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Kontak Baru (draf) | Buat kontak baru dengan nama PT Bintang Farmasi Utama, alamat Jl. Pahlawan No.10, rekening bank BCA 123456789 | Kontak berhasil ditambahkan dengan data sesuai input |
| Negatif — Input Rekening Tidak Valid (draf) | Coba masukkan rekening bank yang tidak valid untuk PT Alkes Prima Mandiri | Ditolak: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Klik "+ Add", pilih Contact yang dituju (wajib), lalu isi: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Account Number, Account Holder — wajib diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Type kontak membatasi kemunculannya di modul lain. Kontak Supplier hanya bisa dipilih sebagai supplier di Purchasing; kontak Customer hanya muncul di Sales/POS; Both muncul di kedua sisi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. User dan Role — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/12-user-dan-role.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/12-user-dan-role.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Akun Login (draf) | Buat akun baru untuk Kasir dengan detail lengkap; assign role 'Kasir' | Akun Kasir berhasil dibuat dan memiliki permission sesuai role 'Kasir' |
| Negatif — Input Data Salah (draf) | Masukkan username duplikat saat membuat akun baru; pilih role tidak ada | Pendaftaran gagal, pesan penolakan yang jelas atau pesan yang jelas, akun tidak dibuat |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Password dan Password Confirmation — wajib saat membuat user baru |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Status (Active/Inactive) — user Inactive tidak bisa login |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | User Inactive tidak bisa login, tapi datanya (dan riwayat aktivitas yang tercatat atas namanya) tetap tersimpan — pola ini lebih aman dipakai daripada menghapus user |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Pajak & Daftar Harga

Bab manual: [`konfigurasi-umum/13-pajak-dan-daftar-harga.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/13-pajak-dan-daftar-harga.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — membuat pajak PPN (draf) | Buat Pajak: Nama PPN 10%, Sifat Non-Zero, Tarif 10% | Pajak PPN 10% berhasil dibuat dengan sifat non-zero dan tarif 10% |
| Negatif — input nama pajak kosong (draf) | Buat Pajak: Nama PPN, Sifat Non-Zero, Tarif 10% (Nama kosong) | Input nama pajak tidak boleh kosong, harap isi nama pajak terlebih dahulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 14. Manajemen Cabang (Branch) — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/14-manajemen-cabang.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/14-manajemen-cabang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Cabang Baru (draf) | Buat cabang baru Apotek Sentosa Bandung; atur hierarki; tugas staff; konfig sidebar; sinkron menu; setup per cabang; susun menu sidebar | Cabang baru terkonfigurasi dengan benar, aktivitas riwayat tersedia |
| Negatif — Input Nama Cabang Salah (draf) | Masukkan nama cabang tidak sesuai format; syarat hierarki dan staff tidak terpenuhi | Tolak inputan; tampilkan pesan kesalahan yang jelas tentang format nama cabang yang benar serta syarat hierarki dan staff harus dipenuhi terlebih dahulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satu cabang tidak bisa sekaligus jadi Main Branch dan melapor ke Main Branch lain — kalau sudah jadi Main Branch, opsi "Reports To" otomatis terkunci, begitu juga sebaliknya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Cabang yang sudah punya cabang lain melapor kepadanya tidak bisa diubah untuk melapor ke Main Branch lain (hierarki hanya 1 tingkat, tidak berjenjang) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Atur Active in Branch — kalau dimatikan, user tetap tercatat terhubung ke cabang tapi tidak bisa memilihnya sebagai cabang aktif |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap item/grup punya tombol Edit (ubah nama, ikon, kata kunci pencarian, status collapse default) dan Delete lewat ikon yang muncul saat hover. Grup yang masih berisi item tidak bisa dihapus — pindahkan atau hapus dulu semua isinya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 15. Produk Lanjutan — Varian (SKU), Modifier, dan Resep

Bab manual: [`konfigurasi-umum/15-produk-lanjutan-varian-modifier-dan-resep.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/15-produk-lanjutan-varian-modifier-dan-resep.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Varian Produk (draf) | Menambah SKU OBT-001 dengan varian ukuran 500 mg dan 1000 mg; atur harga bertingkat; tambah modifier topping alpukat; buat resep untuk produk olahan | SKU baru terdaftar, harga dan modifier sesuai aturan, resep valid |
| Negatif — Modifier Produk (draf) | Menambah modifier tanpa menentukan jenis; mencoba menyimpan | Tidak disimpan, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 5. Aktifkan Required kalau modifier ini wajib dipilih setiap kali item terkait dijual (misalnya wajib pilih ukuran) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 6. Minimal satu bahan wajib diisi — baris terakhir tidak bisa dihapus kalau cuma tersisa satu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 16. Cash Register & Sales Channel — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/16-cash-register-dan-sales-channel.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/16-cash-register-dan-sales-channel.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Cash Register (draf) | Tambahkan 'Jakarta1' untuk kantor pusat & distribusi Jakarta; konfigurasi berhasil dengan meja kasir default | Meja kasir 'Jakarta1' ditambahkan dan dapat digunakan |
| Negatif — Input Nama Meja Kasir Sama (draf) | Mencoba menambahkan 'Jakarta1' kedua kali; menerima pesan kesalahan 'Nama meja kasir sudah ada' | Tambah meja kasir gagal, nama meja kasir duplikat |
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
| Positif — Menambah Kurs Baru (draf) | Tambah kurs USD dengan tgl 1 Januari 2023, nilai 14500 | Kurs baru muncul dalam daftar kurs cabang |
| Negatif — Input Nilai Kurs Salah (draf) | Masukkan kurs USD dengan tgl 1 Januari 2023, nilai negatif -14500 | Sistem menolak input dan memberikan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Klik menu titik tiga pada baris kurs → Edit. Field Currency dan Rate Date terkunci setelah dibuat (tidak bisa diubah) — hanya Rate to Base dan status Active yang bisa diedit |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 18. Pengaturan Tampilan PDF (PDF Layout Settings)

Bab manual: [`konfigurasi-umum/18-pengaturan-tampilan-pdf.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/18-pengaturan-tampilan-pdf.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Mengatur logo menjadi logo Sentosa Farma, warna latar belakang hitam, menampilkan kop surat kantor pusat, menambahkan kolom jumlah dan harga satuan pada tabel item, menyimpan perubahan, berhasil mencetak PDF dengan tampilan sesuai setting | Sukses mengonfigurasi tampilan PDF untuk cabang kantor pusat |
| Negatif — input salah (draf) | Menghapus semua kolom pada tabel item, hanya menampilkan nama produk dan jumlah, menyimpan perubahan, muncul pesan kesalahan pesan yang jelas dan tidak dapat mencetak PDF | Tidak berhasil mengonfigurasi tampilan PDF karena syarat minimal satu kolom dalam tabel item tidak terpenuhi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Signature Label — teks label di atas kolom tanda tangan (misalnya "Hormat kami") — hanya bisa diisi kalau Show Signature Block aktif |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 19. Denominasi Uang dan Deposit Kasir

Bab manual: [`konfigurasi-umum/19-denominasi-uang-dan-deposit-kasir.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/19-denominasi-uang-dan-deposit-kasir.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Pecahan Uang (draf) | Tambahkan pecahan Rp1000 dan Rp5000 pada layar hitung kasir | Layar hitung kasir menampilkan pecahan baru dengan benar |
| Negatif — Input Deposit Kasir Kosong (draf) | Mencoba membaca saldo kasir tanpa input deposit | Sistem menolak pesan penolakan yang jelas |
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
| Positif — Tambah Jenis Dokumen (draf) | Tambah dokumen pesan yang jelas dengan templat baru; aktivasi otomatis | Berhasil menambahkan dan mengaktifkan jenis dokumen legal baru |
| Negatif — Mengekspor Data Tanpa Filter (draf) | Export data tanpa memilih filter apa pun; menerima pesan kesalahan | Tidak dapat mengekspor data tanpa filter yang ditentukan; diberikan petunjuk untuk memilih filter terlebih dahulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Dialog Anonymize This Person menjelaskan bahwa nama, kontak, dan data pribadi lain diganti dengan kode netral dan tidak bisa dibatalkan. Centang I understand this cannot be undone |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 21. Tata Letak Menu dan Log Pribadi

Bab manual: [`konfigurasi-umum/25-tata-letak-menu-dan-log-pribadi.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/25-tata-letak-menu-dan-log-pribadi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Tata Letak Menu (draf) | Menambah grup "Apotek" dan "Pabrik", menempatkan pesan yang jelas di bawah "Apotekpesan yang jelasApotek", "Pabrik", "Klinik", "Laboratorium", "Sewa Alat Medis" | Tata letak menu teraplikasikan dengan benar, pesan yang jelas berada di bawah "Apotek" dan urutan menu sesuai yang ditentukan |
| Negatif — Log Pribadi (draf) | Mencoba membaca log tanpa login | Harus login terlebih dahulu untuk dapat membaca log pribadi, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 22. Pergerakan Stok

Bab manual: [`konfigurasi-umum/26-pergerakan-stok.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/26-pergerakan-stok.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Inputkan SKU OBT-001 dan jumlah 50 di Inventory; Simpan | Daftar pergerakan stok menunjukkan penambahan 50 unit Paracetamol 500 mg strip pada tanggal dan waktu yang tepat |
| Negatif — input salah (draf) | Inputkan SKU ALK-002 dan jumlah negatif 10 tanpa catatan alasan; Simpan | Tampilan error pesan yang jelas dengan saran memasukkan data yang valid |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Pilih Warehouse dan Product Sku (keduanya wajib; kalau kosong muncul pesan Warehouse is required atau Product Sku is required) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Isi Quantity; harus lebih besar dari nol (kalau tidak, muncul pesan Quantity must be greater than zero) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 23. Gambar Produk Massal dan Saran Gambar dari Internet

Bab manual: [`konfigurasi-umum/27-gambar-produk-massal-dan-saran-gambar.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/27-gambar-produk-massal-dan-saran-gambar.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Unggah Gambar Massal dan Saran Internet (draf) | Unggah 10 gambar produk dengan nama file sesuai SKU; pilih saran gambar dari Wikipedia; proses berhasil dengan semua gambar diterapkan ke produk | Semua gambar diterapkan ke produk sesuai SKU, saran gambar diterapkan ke produk yang sesuai |
| Negatif — Nama File Tidak Sesuai SKU (draf) | Unggah 5 gambar dengan nama file tidak sesuai SKU; proses gagal; muncul pesan galat pesan yang jelas | Proses ditolak dengan pesan jelas bahwa nama file harus sesuai dengan SKU produk |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 24. Diagram Urutan Setup Awal Cabang — Konfigurasi Umum

Bab manual: [`konfigurasi-umum/28-diagram-urutan-setup-awal.md`](../../erpApiServices/docs/manualBook/konfigurasi-umum/28-diagram-urutan-setup-awal.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | cabang: Apotek Sentosa Bandung; mata uang: Rupiah; gudang: Jakarta; produk: Paracetamol 500 mg strip; kontak: PT Bintang Farmasi Utama; tahun fiskal: 1 April - 31 Maret; COA: tersedia; modul: semua; akun jurnal: disetel | cabang baru berhasil disetup dengan data benar, konfigurasi umum lengkap |
| Negatif — input salah (draf) | cabang: Apotek Sentosa Bandung; mata uang: Dollar; produk: Paracetamol 500 mg strip; kontak: PT Bintang Farmasi Utama; tahun fiskal: 1 Mei - 31 April; COA: tidak tersedia; modul: salah; akun jurnal: tidak disetel | konfigurasi umum ditolak karena mata uang, tahun fiskal, COA, dan modul tidak sesuai syarat, muncul pesan kesalahan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bab ini merangkum urutan menyiapkan sebuah cabang dalam bentuk gambar. "bab 05" artinya bab 05. Fiscal Year dan Accounting Period. Urutan ini disarankan, dan langkah yang benar-benar wajib sebelum dokumen tertentu bisa dibuat diberi catatan di bawah diagram |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Urutan di atas disarankan. Anda tidak harus mengerjakannya persis berurutan, tetapi syarat di tabel harus terpenuhi sebelum dokumen terkait bisa dibuat atau dibukukan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
