---
title: (PT Medika Nusantara Sejahtera) — 02. Platform Owner, Mulai Menggunakan dan Pengaturan Akun
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul platform-owner, mulai-menggunakan, pengaturan-akun untuk skenario PT Medika Nusantara Sejahtera. Dari penjualan aplikasi ke klien sampai pengguna pertama masuk.
visibility: internal
---

# 02. Platform Owner, Mulai Menggunakan dan Pengaturan Akun

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji siapa boleh melakukan apa: akun, peran, izin, dan pindah cabang. Ini pagar keamanan aplikasi.
>
> **Kalau semuanya benar, artinya:** Orang hanya melihat dan mengubah yang menjadi haknya, dan tombol yang tidak boleh dipakai terlihat nonaktif lengkap dengan alasan.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Paket menentukan modul dan batas (cabang, pengguna, karyawan); modul di luar paket hilang dari menu dan endpoint-nya 403.
- Onboard Client membuat provider, cabang pertama, peran dan pengguna awal; data klien tidak pernah terlihat klien lain.
- Penangguhan klien menutup login dan semua API (kecuali keluar) serta halaman publik klien; pemulihan mengembalikan semuanya tanpa kehilangan data.
- Ganti role Admin wajib PIN owner; role yang baru ditambahkan belum aktif sampai diaktifkan (izin hanya dihitung dari role aktif).
- Kata sandi, 2FA dan batas percobaan masuk.

## 1. Provider, Cabang, Pengguna, Peran, Izin, dan Lisensi

Bab manual: [`platform-owner/01-provider-cabang-pengguna-dan-peran.md`](../../erpApiServices/docs/manualBook/platform-owner/01-provider-cabang-pengguna-dan-peran.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Cabang (draf) | Klik Add Branch; Pilih provider Medika Nusantara Sejahtera; Isi Branch Name "Apotek Nusantara Bogor"; Simpan dengan Create | Cabang baru ditambahkan dengan status Active, di bawah provider Medika Nusantara Sejahtera. |
| Negatif — Menghapus Provider (draf) | Klik Delete pada provider Medika Nusantara Sejahtera; Tidak diberikan izin | Tampil pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kolom wajib yang kosong menghasilkan pesan seperti Please fill all required provider fields atau Role name is required |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Customer Name (wajib) dan Email pelanggan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Pilih jenis lisensi: Subscription (berbatas waktu; wajib diberi tanggal kedaluwarsa, kalau tidak muncul A subscription license needs an expiry date) atau Perpetual (tanpa kedaluwarsa) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Klik Download License File pada baris untuk mengunduh berkas lisensi, lalu kirim ke pelanggan untuk dipasang. Edit Or Renew mengubah atau memperpanjang lisensi, tetapi setiap perubahan menandatangani ulang lisensi sehingga pelanggan harus memasang berkas baru |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Paket, Langganan, Harga, Modul, dan Mitra

Bab manual: [`platform-owner/02-paket-langganan-dan-mitra.md`](../../erpApiServices/docs/manualBook/platform-owner/02-paket-langganan-dan-mitra.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Paket Langganan Baru (draf) | Pilih "Add subscription plan"; isi nama "Paket Gold", slug "gold-plan", deskripsi "Paket premium dengan fitur lengkap"; pilih modul preset "All modules", mata uang "IDR", harga bulanan 500.000, tahunan kosong; uji coba gratis 7 hari, masa tenggang 14 hari; batas pengguna maksimal 20, cabang 5, karyawan 30, kasir 10; termasuk bahasa Indonesia dan Inggris; aktifkan fitur AI assistant, WhatsApp, QRIS payment gateway, e-invoice tax, dua faktor autentikasi, logistik, metode valuasi LIFO, layout PDF custom, loyalitas, promosi, dan tampilan dapur, reservasi, dan peta lantai; aktifkan "Tampilkan di halaman harga publik", status "Aktif"; simpan. | Paket "Paket Gold" ditambahkan dengan detail yang diberikan, terlihat dalam daftar paket langganan. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Permintaan ditolak sistem bila perusahaan sudah memakai paket dan siklus itu, atau bila sudah ada permintaan yang masih menunggu. Paket dan siklus yang diminta harus yang ditawarkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Approve langsung mengganti paket (aturan dan pengamannya sama dengan Change Plan oleh pemilik platform, tanpa prorata). Reject tidak mengubah apa pun. Keputusan disertai catatan, dan permintaan yang sudah diputuskan tidak bisa diputuskan lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Name (wajib), Icon, Order (urutan tampil), dan Description. Atur Active In Catalog agar paket muncul di pilihan onboarding |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Modul infrastruktur yang selalu aktif ditampilkan terpisah (Always-on infrastructure modules) dan tidak bisa dimatikan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Template Master Data: Keuangan dan Akuntansi

Bab manual: [`platform-owner/03-template-keuangan-dan-akuntansi.md`](../../erpApiServices/docs/manualBook/platform-owner/03-template-keuangan-dan-akuntansi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Tambah template bagan akun dengan nama "Gudang Jakarta", kode 101, level 2; tambah akun "Stok Obat" dengan kode 101.01; pilih template di cabang Apotek Nusantara Bandung; lihat akun baru tersedia | Status berhasil menambahkan template dan akun, opsi akun baru muncul di cabang |
| Negatif — input salah (draf) | Tambah template bagan akun dengan kode duplikat "101" | Pesan kesalahan tentang kode unik diperlukan muncul, tidak dapat menyimpan template |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Template Master Data: Operasional, Status, dan Menu

Bab manual: [`platform-owner/04-template-operasional.md`](../../erpApiServices/docs/manualBook/platform-owner/04-template-operasional.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah template status (draf) | Pilih "Add Template"; isi Name: "Stok Habis", Code: "STKHABIS", Module Type: "Inventory", Business Type: "Operasional", Sort Order: 3, Color: "#FF0000", Description: "Status stok habis" | Status templates ditambahkan dengan nama dan kode yang dimasukkan |
| Negatif — Menambah template status tanpa mengisi field wajib (draf) | Pilih "Add Template"; klik "Create" tanpa mengisi Name; muncul pesan error "Field Name is required" | Tidak dapat menambahkan template karena field Name tidak boleh kosong |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pastikan untuk mengisi semua field wajib sebelum menambahkan template status |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kode tidak dapat diubah setelah template dibuat karena logika absensi, penggajian, dan cuti bergantung pada kode tersebut |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Code tidak dapat diubah setelah template dibuat. Cabang memakai kode ini sebagai titik awal untuk tipe kepegawaian dalam HRM |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Konten Landing Page

Bab manual: [`platform-owner/05-konten-landing-page.md`](../../erpApiServices/docs/manualBook/platform-owner/05-konten-landing-page.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Banner (draf) | Buka halaman /core/landing-banners; klik Tambah Banner; unggah gambar banner; isi judul, subjudul, teks tombol, link tombol; atur tanggal mulai dan berakhir; nyalakan Aktif; klik simpan. | Banner baru ditampilkan di halaman depan sesuai pengaturan. |
| Negatif — Menghapus Fitur yang Tidak Aktif (draf) | Buka halaman /core/landing-features; pilih fitur yang tidak aktif; klik ikon tempat sampah; konfirmasi hapus. | Pesan error muncul karena fitur tidak aktif dan tidak bisa dihapus. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Unggah Gambar Banner (wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 6. Pilih Search Engine Instruction: boleh diindeks dan diikuti tautannya, atau salah satu kombinasi yang melarang indeks atau pengikutan tautan. Halaman yang dilarang diindeks tidak masuk sitemap dan ditutup di robots.txt |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 7. Isi Structured Data (JSON-LD) bila Anda memakainya. Isinya harus JSON yang valid; kalau tidak, penyimpanan ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Sistem: Terjemahan, Bahasa, Data Acuan, Lampiran, dan Log

Bab manual: [`platform-owner/06-sistem-bahasa-data-acuan-dan-log.md`](../../erpApiServices/docs/manualBook/platform-owner/06-sistem-bahasa-data-acuan-dan-log.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah terjemahan (draf) | Klik Create Translation; masukkan Key "Order", Value "Pesanan", Language "Indonesia"; klik Save | Terjemahan ditambahkan dengan status berhasil, key dan value sesuai input |
| Negatif — Menghapus bahasa tanpa teks (draf) | Klik Add Language; masukkan Name "Sunda", Code "su"; coba hapus tanpa menambahkan teks; lihat pesan peringatan | Tidak dapat menghapus bahasa tanpa teks, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Dashboard Platform, Langganan, dan Monitor Notifikasi

Bab manual: [`platform-owner/07-dashboard-platform-owner-dan-langganan.md`](../../erpApiServices/docs/manualBook/platform-owner/07-dashboard-platform-owner-dan-langganan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membaca dashboard platform (draf) | Log masuk sebagai pemilik platform; kunjungi `/dashboard/core`; baca angka utama, grafik, dan daftar | Dashboard tampil dengan data sesuai entitas perusahaan uji; tombol Manage Branches nonaktif tanpa izin |
| Negatif — Mencoba mengakses dashboard lain sebagai pemilik platform (draf) | Log masuk sebagai pemilik platform; kunjungi `/dashboard/subscriptions` atau `/dashboard/notifications`; cek pesan | Tampil pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Klik Approve untuk menyetujui, atau Reject untuk menolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Akun Gateway Platform dan Kode Kanal Transfer Bank

Bab manual: [`platform-owner/08-akun-gateway-platform-dan-kode-kanal-bank.md`](../../erpApiServices/docs/manualBook/platform-owner/08-akun-gateway-platform-dan-kode-kanal-bank.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambahkan kredensial pembayaran (draf) | Pilih PayPal; Isi email dan ID API; Klik Save Instructions | Akun PayPal terdaftar dengan sukses; Teks konfirmasi muncul |
| Negatif — Transfer ke bank tanpa kode kanal (draf) | Pilih Bank BCA; Tidak mengisi kode kanal; Coba simpan | Tampilan error: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penting: bank yang belum punya kode kanal tidak dapat menerima transfer dari penyedia itu; baris transfer ke bank tersebut diblokir. Kolom Banks linked menunjukkan berapa bank yang sudah terhubung |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Pendaftaran Mandiri Klien dan Persetujuan

Bab manual: [`platform-owner/09-pendaftaran-mandiri-klien.md`](../../erpApiServices/docs/manualBook/platform-owner/09-pendaftaran-mandiri-klien.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pendaftaran mandiri klien berhasil (draf) | Calon klien Medika Nusantara memilih paket Bulanan, menambah layanan HRB, mengisi data perusahaan, akun, dan kata sandi; mengirim pengajuan. | Status pengajuan berubah Menunggu persetujuan; email akun dikirim ke kontak yang ditentukan. |
| Negatif — Pengajuan ditolak karena data tidak lengkap (draf) | Calon klien Medika Nusantara mengisi data perusahaan dan akun, namun lupa menambah layanan; mengirim pengajuan. | Status pengajuan berubah Tidak disetujui; email notifikasi dikirim dengan alasan kekurangan data. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kata sandi hanya disimpan dalam bentuk hash dan dihapus dari pengajuan begitu akun terbentuk. Email yang sudah terdaftar atau sedang diajukan ditolak. Kolom jebakan dan pembatasan 5 pengajuan per menit melindungi dari spam |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Atau klik Tolak pengajuan dan isi alasan (wajib); calon klien melihatnya di halaman status |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tombol berstatus nonaktif dengan penjelasan bila pengajuan bukan pengajuan mandiri atau sudah diputuskan. Provision manual tidak bisa dipakai untuk pengajuan mandiri: persetujuan adalah satu-satunya jalan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pengaturan subscriptionselfserviceenabled mematikan pendaftaran mandiri bila bernilai salah: halaman /subscribe menyatakan tidak tersedia dan pengajuan baru ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Diagram Alur Langganan Klien — Platform Owner

Bab manual: [`platform-owner/10-diagram-alur-langganan-klien.md`](../../erpApiServices/docs/manualBook/platform-owner/10-diagram-alur-langganan-klien.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pendaftaran mandiri klien baru (draf) | Klik "Pendaftaran Mandiri", masukkan data, pilih paket, klik "Ajukan" | Akun klien terbentuk, status pesan yang jelas, kata sandi disimpan dalam hash |
| Negatif — Persetujuan ditolak oleh pemilik platform (draf) | Klik "Persetujuan", pilih "Tolak", masukkan alasan penolakan | Status klien menjadi "Ditolak", pesan penolakan muncul, kata sandi dihapus dari pengajuan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | B --/"Tidak"/ X1["Halaman menyatakan tidak tersedia<br/pengajuan baru ditolak"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | D --/"Ya"/ X2["Pengajuan ditolak"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | F --/"Tolak, alasan wajib"/ G(["Calon klien melihat alasan<br/boleh mengajukan lagi"]) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hanya pemilik platform yang bisa menyetujui atau menolak pengajuan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Masuk ke Aplikasi, Pusat Bantuan, dan Riwayat Perubahan

Bab manual: [`mulai-menggunakan/01-login-bantuan-dan-riwayat-perubahan.md`](../../erpApiServices/docs/manualBook/mulai-menggunakan/01-login-bantuan-dan-riwayat-perubahan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Login ke Aplikasi (draf) | Masuk dengan email "admin@medikanusantara.test", password "MnsUji#2026", centang "Remember me"; klik "Login" | Dibawa ke halaman awal aplikasi sebagai admin, sesi berakhir setelah 30 menit inactivity |
| Negatif — Login Gagal Tanpa Verifikasi Dua Langkah (draf) | Masuk dengan email "admin@medikanusantara.test", password salah; klik "Login" | Muncul pesan kesalahan verifikasi dua langkah, masukkan kode authenticator atau recovery code jika diperlukan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Pengaturan Akun Saya: Tampilan, Keamanan, dan Langganan

Bab manual: [`pengaturan-akun/01-pengaturan-akun-saya.md`](../../erpApiServices/docs/manualBook/pengaturan-akun/01-pengaturan-akun-saya.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengubah password (draf) | Masuk ke akun; isikan Current Password; masukkan New Password dan Confirm Password; klik Update Password | Muncul pesan penolakan yang jelas |
| Negatif — Gagal mengaktifkan verifikasi dua langkah (draf) | Tidak memasukkan Current Password; klik Set up two-factor | Tampil pesan kesalahan yang jelas tentang kebutuhan memasukkan password saat mengatur dua faktor |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Ubah Name (minimal 2 karakter) dan Email (harus berformat email yang valid) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi New Password (minimal 8 karakter, harus berbeda dari yang lama) dan Confirm Password (harus sama) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Save these recovery codes now: tiap kode hanya bisa dipakai sekali dan satu-satunya jalan masuk bila ponsel hilang; kode tidak ditampilkan lagi. Gunakan Copy all, lalu klik I saved them |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
