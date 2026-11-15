---
title: (PT Sehat Sentosa Farma) — 10. Restoran (Kafe Sehat)
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul restaurant untuk skenario PT Sehat Sentosa Farma. Pesanan meja, dapur, tagihan dan pembayaran.
visibility: internal
---

# 10. Restoran (Kafe Sehat)

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Pesanan per meja, kirim ke dapur (KDS), pisah tagihan, reservasi dan pesanan mandiri lewat QR.
- Pembayaran tagihan (tunai/QRIS) menutup pesanan dan membebaskan meja.
- Stok bahan menu berkurang sesuai resep bila diaktifkan.

## 1. Konfigurasi Restoran — Modul Restaurant

Bab manual: [`restaurant/01-konfigurasi-restoran.md`](../../erpApiServices/docs/manualBook/restaurant/01-konfigurasi-restoran.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menambahkan area "Kafe Sehat" di lobi klinik; membuat 5 meja duduk; mengimport data meja dari Excel; menyiapkan denah lantai dengan area Kafe Sehat; mengatur stasiun dapur untuk memasak makanan; mengonfigurasi pengaturan umum restoran | Area, meja, dan stasiun dapur berhasil ditambahkan; data meja diimport dengan benar; denah lantai dan pengaturan umum restoran disetup sesuai harapan |
| Negatif — input salah (draf) | Menambahkan area "Kafe Sehat" tanpa memasukkan detail area; mencoba membuat 50 meja sekaligus tanpa template; mengimport data meja dari file PDF; menyiapkan stasiun dapur tanpa bahan masakan; mengonfigurasi pengaturan umum restoran dengan nilai tidak valid | Input area, meja, dan stasiun dapur ditolak karena detail atau format yang salah; proses import data meja gagal karena file yang dimasukkan tidak sesuai; konfigurasi pengaturan umum restoran harus memenuhi syarat tertentu sebelum disetup |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Area adalah pengelompokan meja, misalnya "Lantai 1", "Lantai 2", "Outdoor", "VIP Room". Setiap meja wajib terhubung ke satu area |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Table Number — nomor/kode meja (wajib), contoh A1, B12 |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Status — Available (kosong), Occupied (terisi), Reserved (dipesan), Maintenance (tidak bisa dipakai). Biasanya dibiarkan Available saat pertama dibuat — status berubah otomatis begitu ada order/booking berjalan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Name (wajib) dan Sort Order |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Menu dan Kitchen Routing — Modul Restaurant

Bab manual: [`restaurant/02-menu-dan-kitchen-routing.md`](../../erpApiServices/docs/manualBook/restaurant/02-menu-dan-kitchen-routing.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambahkan Menu (draf) | Tambah menu pesan yang jelas dengan harga dan stok; routing ke stasiun "Pengemasan"; lihat estimasi biaya resep | Menu ditambahkan, otomatis di-86'd, routing ke stasiun yang benar & estimasi biaya muncul |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau bahan suatu menu habis di tengah jam operasional, staf bisa langsung menonaktifkan menu itu tanpa harus masuk ke halaman Products: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Pemesanan dan Order Meja — Modul Restaurant

Bab manual: [`restaurant/03-pemesanan-dan-order-meja.md`](../../erpApiServices/docs/manualBook/restaurant/03-pemesanan-dan-order-meja.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuka Order Baru (draf) | Buka modul Restaurant, klik 'Membuka Order Baru', masukkan data pelanggan, pilih meja 102, tambah item Paracetamol 500 mg strip 2 buah | Order meja 102 terbuka dengan item yang ditambahkan dan status pending di dapur |
| Negatif — Menambah Item ke Order (draf) | Coba tambahkan item tanpa membuka order meja, masukkan data pelanggan dan meja, pilih item Paracetamol 500 mg strip 2 buah, klik 'Tambah' | Tampilan error: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Table — meja yang dipakai (wajib). Meja berstatus Occupied akan tampil disabled di daftar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pax — jumlah tamu (wajib, minimal 1) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item yang berasal dari QR Self-Order pelanggan (badge "Needs Confirmation") harus dikonfirmasi waiter dulu sebelum bisa masuk proses dapur — lihat chapter 06. QR Self-Order |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Setiap item wajib di-assign ke salah satu grup tagihan (klik nomor grup di sebelah item). Tambah grup baru dengan "+ Add Bill" kalau perlu lebih dari 2 tagihan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Kitchen Display System dan Order Items — Modul Restaurant

Bab manual: [`restaurant/04-kitchen-display-dan-order-items.md`](../../erpApiServices/docs/manualBook/restaurant/04-kitchen-display-dan-order-items.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — KDS (draf) | Input pesanan di Apotek Sentosa Bandung; tampilan tiket di kantor pusat | Tampilan tiket sesuai pesanan dan dikirim ke stasiun dapur |
| Negatif — Order Items (draf) | Menambah item yang tidak ada di daftar; input jumlah negatif | Pesan error pesan yang jelas atau pesan yang jelas, input tidak disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Atau klik ikon centang per item untuk konfirmasi satu-satu, atau ikon X untuk menolak item tertentu (misalnya karena bahan sudah habis atau salah pesan) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item yang belum dikonfirmasi tidak akan diproses di dapur/KDS — panel ini adalah gerbang wajib sebelum pesanan pelanggan lanjut ke dapur (kecuali fitur konfirmasi dimatikan di Config, lihat chapter 01 dan 06) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item yang sudah served tidak bisa dimajukan lagi, kecuali dikembalikan ke preparing |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item yang sudah ready atau served untuk menu yang dibuat saat dipesan tidak bisa dibatalkan begitu saja |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Reservasi Meja (Booking) — Modul Restaurant

Bab manual: [`restaurant/05-reservasi-meja.md`](../../erpApiServices/docs/manualBook/restaurant/05-reservasi-meja.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Reservasi Baru (draf) | Input nama tamu, jumlah orang, tanggal dan waktu, pilih meja; klik 'Reservasi' | Meja terbooking, notifikasi tamu dan kasir, status reservasi muncul di daftar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Table — meja yang direservasi (wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Guest Name — nama tamu (wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Guest Count — jumlah tamu, minimal 1 (wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Booking Date & Time — tanggal dan jam reservasi (wajib) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. QR Self-Order — Modul Restaurant

Bab manual: [`restaurant/06-qr-self-order.md`](../../erpApiServices/docs/manualBook/restaurant/06-qr-self-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Tamu scan QR meja, pilih menu Paracetamol 500 mg strip; waiter konfirmasi pesanan | Pesanan masuk ke dapur untuk diproses dan diantarkan |
| Negatif — input salah (draf) | Tamu scan QR meja, pilih menu Jamu Kunyit Asam sachet yang tidak bisa dipesan lewat QR; waiter melihat pesanan tidak valid | Pesanan ditolak dengan notifikasi pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Diagram Alur Restaurant — Modul Restaurant

Bab manual: [`restaurant/07-diagram-alur-restaurant.md`](../../erpApiServices/docs/manualBook/restaurant/07-diagram-alur-restaurant.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Pelanggan memesan makanan di kafe Sehat menggunakan metode bayar belakangan; pesanan masuk ke dapur; status item berubah menjadi diproses, selesai, dan siap; pelanggan membayar dan pesanan ditutup | Proses pesanan berjalan lancar sesuai langkah-langkah yang terdefinisi |
| Negatif — input salah (draf) | Pelanggan memesan makanan tanpa metode bayar dulu atau belakangan; sistem menolak pesanan pesan penolakan yang jelas | Pesanan ditolak karena syarat pembayaran tidak dipenuhi oleh pelanggan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item yang sudah Served tidak bisa dimajukan lagi, kecuali dikembalikan ke Preparing |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | B --/"Belum"/ C["Complete ditolak<br/pesanan belum dibayar"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | D --/"Ya"/ E["Complete ditolak<br/masih ada item belum dihidangkan"] |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Pencatatan Bahan dan Estimasi Porsi — Modul Restaurant

Bab manual: [`restaurant/08-pencatatan-bahan-dan-estimasi-porsi.md`](../../erpApiServices/docs/manualBook/restaurant/08-pencatatan-bahan-dan-estimasi-porsi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menetapkan estimasi porsi untuk Masker Medis box 50 (ALK-001) di Kafe Sehat; mencatat bahan masuk, hitungan fisik, dan terbuang; membaca laporan selisih | Estimasi sisa porsi dan perkiraan habis sesuai input; laporan selisih akurat |
| Negatif — input salah (draf) | Menginput estimasi untuk produk yang tidak ada di Kafe Sehat; mencatat bahan masuk tanpa hitungan fisik atau terbuang | Ditolak pesan penolakan yang jelas dan pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hanya produk yang menjadi bahan di sebuah resep yang bisa dicatat. Produk lain ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi qty (tidak boleh negatif) dan, bila perlu, biaya per unit dan catatan. Satu pencatatan boleh memuat sampai 200 baris |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Restoran di Terminal POS: Denah, Booking, Pesanan QR, dan Panggilan Siap — Modul Restaurant

Bab manual: [`restaurant/09-restoran-di-terminal-pos.md`](../../erpApiServices/docs/manualBook/restaurant/09-restoran-di-terminal-pos.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Memasukkan denah meja (draf) | Input denah meja restoran Kafe Sehat; tampilan meja berwarna sesuai status | Meja terlihat dengan warna yang tepat sesuai status |
| Negatif — Input nomor meja tidak valid (draf) | Masukan nomor meja 9999; sistem menolak | Input nomor meja harus antara 1-50, silakan cek kembali input Anda |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pesanan ditolak bila bahan tidak cukup, bila pengaturan penolakan penjualan saat bahan kurang aktif |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Makanan yang sudah siap tidak bisa dibatalkan dari terminal. Dapur bisa mengembalikannya ke preparing |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
