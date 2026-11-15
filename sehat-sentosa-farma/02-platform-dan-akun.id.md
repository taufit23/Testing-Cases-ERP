---
title: (PT Sehat Sentosa Farma) — 02. Platform Owner, Mulai Menggunakan dan Pengaturan Akun
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul platform-owner, mulai-menggunakan, pengaturan-akun untuk skenario PT Sehat Sentosa Farma. Dari penjualan aplikasi ke klien sampai pengguna pertama masuk.
visibility: internal
---

# 02. Platform Owner, Mulai Menggunakan dan Pengaturan Akun

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
| Positif — Menambah Cabang (draf) | Tambah data cabang baru: Klinik Sentosa Depok; Konfirmasi penambahan sukses. | Cabang baru ditambahkan dengan status aktif. |
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
| Positif — Membuat Paket (draf) | Buat paket 'Basic' untuk Sentosa Farma dengan harga Rp100.000/minggu; Aktifkan | Paket 'Basic' berhasil dibuat dan aktif |
| Negatif — Input Harga Nol (draf) | Coba masukkan harga 0 untuk Basic; Simpan | Input gagal, pesan penolakan yang jelas |
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
| Positif — jalur normal (draf) | Menambah template bagan akun untuk cabang baru Klinik Pratama & Laboratorium Bekasi dengan data lengkap dan benar | Template bagan akun berhasil disalin ke cabang Klinik Pratama & Laboratorium Bekasi, siap digunakan |
| Negatif — input salah (draf) | Menggunakan kode bagan akun yang sudah ada tanpa menambah template baru | Input ditolak karena harus menambah template baru sebelum menggunakan kode bagan akun tersebut |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Template Master Data: Operasional, Status, dan Menu

Bab manual: [`platform-owner/04-template-operasional.md`](../../erpApiServices/docs/manualBook/platform-owner/04-template-operasional.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Template Status (draf) | Tambah status 'Sick Leave' dengan alasan penyesuaian stok | Sukses menambahkan template status baru |
| Negatif — Menghapus Template Alur Persetujuan (draf) | Menghapus template yang masih digunakan | Ditolak: Template masih terkait, hapus terlebih dahulu hubungannya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pastikan untuk mengisi semua field wajib sebelum menambahkan template status |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kode tidak dapat diubah setelah template dibuat karena logika absensi, penggajian, dan cuti bergantung pada kode tersebut |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Code tidak dapat diubah setelah template dibuat. Cabang memakai kode ini sebagai titik awal untuk tipe kepegawaian dalam HRM |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Konten Landing Page

Bab manual: [`platform-owner/05-konten-landing-page.md`](../../erpApiServices/docs/manualBook/platform-owner/05-konten-landing-page.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menambah fitur "Hubungi Kami" pada landing page; mengubah nomor telepon menjadi 0812-3456-7890; menyimpan perubahan | Fitur "Hubungi Kami" ditampilkan dengan nomor baru |
| Negatif — input salah (draf) | Menghapus semua banner tanpa alasan; menolak permintaan pesan penolakan yang jelas | Semua banner tetap terpajang, muncul notifikasi untuk memberikan alasan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Unggah Gambar Banner (wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 6. Pilih Search Engine Instruction: boleh diindeks dan diikuti tautannya, atau salah satu kombinasi yang melarang indeks atau pengikutan tautan. Halaman yang dilarang diindeks tidak masuk sitemap dan ditutup di robots.txt |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 7. Isi Structured Data (JSON-LD) bila Anda memakainya. Isinya harus JSON yang valid; kalau tidak, penyimpanan ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Sistem: Terjemahan, Bahasa, Data Acuan, Lampiran, dan Log

Bab manual: [`platform-owner/06-sistem-bahasa-data-acuan-dan-log.md`](../../erpApiServices/docs/manualBook/platform-owner/06-sistem-bahasa-data-acuan-dan-log.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Terjemahan (draf) | Tambah bahasa Inggris untuk produk Paracetamol 500 mg strip (SKU OBT-001) di Sentosa Farma | Berhasil menambah terjemahan dalam bahasa Inggris dengan data yang benar |
| Negatif — Menghapus Bahasa (draf) | Menghapus bahasa Indonesia dari produk Amoxicillin 500 mg (OBT-002) tanpa alasan | Ditolak karena harus ada alasan penghapusan dan konfirmasi ulang sebelum hapus benar |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Dashboard Platform, Langganan, dan Monitor Notifikasi

Bab manual: [`platform-owner/07-dashboard-platform-owner-dan-langganan.md`](../../erpApiServices/docs/manualBook/platform-owner/07-dashboard-platform-owner-dan-langganan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Pemilik membaca dasbor platform, langganan, dan monitor notifikasi; angka utama dan grafik sesuai; permintaan ganti paket diproses; notifikasi diteruskan dengan benar | Semua fitur berfungsi dengan baik; informasi akurat; proses ganti paket lancar; notifikasi diterima dengan tepat |
| Negatif — input salah (draf) | Input status langganan salah; permintaan ganti paket tanpa syarat valid ditolak dengan pesan jelas; notifikasi tidak diteruskan | Permintaan ditolak dengan pesan yang jelas; proses ganti paket tidak diproses; notifikasi gagal dikirim dengan pesan kesalahan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Klik Approve untuk menyetujui, atau Reject untuk menolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Akun Gateway Platform dan Kode Kanal Transfer Bank

Bab manual: [`platform-owner/08-akun-gateway-platform-dan-kode-kanal-bank.md`](../../erpApiServices/docs/manualBook/platform-owner/08-akun-gateway-platform-dan-kode-kanal-bank.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Input akun gateway platform dan kode kanal bank yang benar; cek manual sukses; transfer otomatis terkonfirmasi | Akun berhasil diisi, proses pembayaran lancar, status transfer valid |
| Negatif — input salah (draf) | Input akun salah atau kode kanal bank tidak sesuai; pemberitahuan kesalahan dengan detail masalah | Pendaftaran ditolak, pesan error jelas tentang syarat yang belum terpenuhi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penting: bank yang belum punya kode kanal tidak dapat menerima transfer dari penyedia itu; baris transfer ke bank tersebut diblokir. Kolom Banks linked menunjukkan berapa bank yang sudah terhubung |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Pendaftaran Mandiri Klien dan Persetujuan

Bab manual: [`platform-owner/09-pendaftaran-mandiri-klien.md`](../../erpApiServices/docs/manualBook/platform-owner/09-pendaftaran-mandiri-klien.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pendaftaran Mandiri Klien (draf) | Calon klien Bandung masuk halaman pendaftaran, mengisi data dengan benar, klik setuju syarat & ketentuan, dan submit | Langganan diterapkan secara otomatis untuk Apotek Sentosa Bandung, status menjadi 'aktif' di sistem platform-owner |
| Negatif — Pendaftaran Mandiri Klien (draf) | Calon klien mengisi data tidak lengkap, syarat tidak terpenuhi, klik setuju tetapi tidak submit | Pengajuan ditolak dengan pesan 'data tidak lengkap, silakan periksa kembali', status tetap 'pending' di sistem platform-owner |
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
| Positif — jalur normal (draf) | Klien baru mendaftar, pemilik platform memvalidasi, kirim notifikasi aktivasi, klien mengaktifkan akun, langganan aktif | Langganan klien berstatus aktif sesuai persyaratan |
| Negatif — input salah (draf) | Klien mendaftar tanpa email valid, sistem menolak pendaftaran pesan penolakan yang jelas | Pendaftaran ditolak dan klien diberi informasi tentang kesalahan input |
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
| Positif — Masuk ke Aplikasi (draf) | Login dengan akun valid; masukkan username dan password; verifikasi dua langkah berhasil; akses aplikasi terbuka | Berhasil masuk ke dashboard utama |
| Negatif — Masuk ke Aplikasi (draf) | Login dengan username kosong; klik masuk; menerima pesan kesalahan | Harus mengisi username dan password yang valid untuk dapat login |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Pengaturan Akun Saya: Tampilan, Keamanan, dan Langganan

Bab manual: [`pengaturan-akun/01-pengaturan-akun-saya.md`](../../erpApiServices/docs/manualBook/pengaturan-akun/01-pengaturan-akun-saya.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengaturan Akun (draf) | Ganti password, aktivasi 2FA, override PIN manajer, cek status langganan | Berhasil mengubah pengaturan akun dan memperbarui status langganan |
| Negatif — Input Password Salah (draf) | Masukkan password yang salah berulang kali | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Ubah Name (minimal 2 karakter) dan Email (harus berformat email yang valid) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi New Password (minimal 8 karakter, harus berbeda dari yang lama) dan Confirm Password (harus sama) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Save these recovery codes now: tiap kode hanya bisa dipakai sekali dan satu-satunya jalan masuk bila ponsel hilang; kode tidak ditampilkan lagi. Gunakan Copy all, lalu klik I saved them |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
