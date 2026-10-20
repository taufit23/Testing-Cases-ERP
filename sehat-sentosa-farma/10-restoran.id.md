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
| Positif — jalur normal (draf) | Membuat meja satuan di area Zona1 dengan nomor 101; menambahkan stok awal 50 piring | Meja 101 muncul dalam daftar meja dan stok piring ditambahkan ke inventaris |
| Negatif — input salah (draf) | Menambahkan stok negatif pada meja 101 | Tidak dapat disimpan; pesan penolakan yang jelas |
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
| Positif — Menambahkan Menu (draf) | Tambah Paracetamol 500 mg strip (SKU OBT-001) ke daftar menu; routing ke stasiun obat; biaya resep ditampilkan | Menu Paracetamol 500 mg strip terlihat di daftar dan dikirim ke stasiun obat dengan estimasi biaya resep yang benar |
| Negatif — Menandai Menu Tidak Tersedia (draf) | Menandai Vitamin C 1000 mg botol (SUP-001) sebagai tidak tersedia; mencoba memesan | Pesan pesan yang jelas ditampilkan dan pesanan tidak dapat diproses |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau bahan suatu menu habis di tengah jam operasional, staf bisa langsung menonaktifkan menu itu tanpa harus masuk ke halaman Products: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Pemesanan dan Order Meja — Modul Restaurant

Bab manual: [`restaurant/03-pemesanan-dan-order-meja.md`](../../erpApiServices/docs/manualBook/restaurant/03-pemesanan-dan-order-meja.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuka Order Baru (draf) | Buka modul Restaurant, klik "Buat Pesanan", masukkan data meja 123, pilih kafe Sehat, tambah item Paracetamol 500 mg strip 2 buah, konfirmasi. | Order meja 123 terbuka dengan item Paracetamol 500 mg strip 2 buah. |
| Negatif — Menambah Item ke Order (draf) | Buka order meja 123, coba tambah item tanpa login sebagai kasir, pesan penolakan yang jelas. | Pesan error muncul dan tidak dapat menambah item tanpa login. |
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
| Positif — Kitchen Display System (draf) | Memasukkan pesanan ke KDS, memfilter per stasiun, memproses item dengan benar | Tiket pesanan ditampilkan di layar dapur sesuai stasiun dan item diproses dengan akurat |
| Negatif — Order Items (draf) | Input nama item salah, mencoba mengonfirmasi pesanan tanpa item | Sistem menolak input dan memberikan pesan kesalahan yang jelas tentang syarat yang tidak terpenuhi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Atau klik ikon centang per item untuk konfirmasi satu-satu, atau ikon X untuk menolak item tertentu (misalnya karena bahan sudah habis atau salah pesan) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item yang belum dikonfirmasi tidak akan diproses di dapur/KDS — panel ini adalah gerbang wajib sebelum pesanan pelanggan lanjut ke dapur (kecuali fitur konfirmasi dimatikan di Config, lihat chapter 01 dan 06) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Untuk item dari self-order dengan konfirmasi wajib aktif: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Reservasi Meja (Booking) — Modul Restaurant

Bab manual: [`restaurant/05-reservasi-meja.md`](../../erpApiServices/docs/manualBook/restaurant/05-reservasi-meja.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Reservasi Baru (draf) | Klik "Booking", masukkan nama tamu, jumlah orang, tanggal dan waktu, pilih meja, konfirmasi detail, bayar deposit 20% | Reservasi terdaftar dengan status "Pending" |
| Negatif — Tanggal sudah lewat (draf) | Masukkan tanggal di masa lalu, coba kirim | Ditolak: pesan yang jelas |
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
| Positif — Pemesanan Paracetamol (draf) | Tamu scan QR meja, pilih Paracetamol; waiter konfirmasi; pesanan masuk dapur | Pesanan berhasil diteruskan ke dapur |
| Negatif — Pemesanan Amoxicillin tanpa resep (draf) | Tamu scan QR meja, pilih Amoxicillin; sistem menolak & meminta resep dari waiter | Tidak dapat memesan obat resep tanpa resep dokter |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
