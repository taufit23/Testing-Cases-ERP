---
title: (PT Medika Nusantara Sejahtera) — 10. Restoran (Kafe Sehat)
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul restaurant untuk skenario PT Medika Nusantara Sejahtera. Pesanan meja, dapur, tagihan dan pembayaran.
visibility: internal
---

# 10. Restoran (Kafe Sehat)

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji restoran dan kafe: meja, pesanan, dapur, bahan baku, dan pembayaran.
>
> **Kalau semuanya benar, artinya:** Pesanan sampai ke dapur, bahan baku berkurang sesuai resep, dan meja serta tagihan tidak tertukar.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Pesanan per meja, kirim ke dapur (KDS), pisah tagihan, reservasi dan pesanan mandiri lewat QR.
- Pembayaran tagihan (tunai/QRIS) menutup pesanan dan membebaskan meja.
- Stok bahan menu berkurang sesuai resep bila diaktifkan.

## 1. Konfigurasi Restoran — Modul Restaurant

Bab manual: [`restaurant/01-konfigurasi-restoran.md`](../../erpApiServices/docs/manualBook/restaurant/01-konfigurasi-restoran.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi area duduk (draf) | Masuk ke menu `Restoran → Areas`, klik "+ Buat Daerah", isikan nama "Lantai 1", kapasitas 50, dan simpan. | Area "Lantai 1" muncul dalam daftar dengan status aktif. |
| Negatif — Konfigurasi area duduk tanpa nama (draf) | Masuk ke menu `Restoran → Areas`, klik "+ Buat Daerah", isikan hanya kapasitas 50, dan simpan. | Sistem menolak pengisian data karena nama area wajib diisi dan menampilkan pesan kesalahan. |
| Positif — Membuat meja satuan (draf) | Masuk ke menu `Restoran → Tabel`, klik "+ Buat Tabel", pilih area "Lantai 1", isikan nomor meja "A1", dan simpan. | Meja dengan nomor "A1" di area "Lantai 1" muncul dalam daftar meja. |
| Negatif — Membuat meja tanpa area (draf) | Masuk ke menu `Restoran → Tabel`, klik "+ Buat Tabel", isikan hanya nomor meja "A1" dan simpan. | Sistem menolak pengisian data karena area wajib diisi dan menampilkan pesan kesalahan. |
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
| Positif — Menandai menu tidak tersedia (draf) | Di halaman Menu, klik switch ketersediaan pada baris produk Paracetamol 500 mg strip (SKU OBT-001) | Produk Paracetamol 500 mg strip (SKU OBT-001) tampil pudar di daftar dan tidak bisa dipilih saat menambah item order |
| Negatif — Menu tidak muncul di daftar (draf) | Produk Vitamin C 1000 mg botol (SUP-001) di Client-Master Products belum aktif atau kategori kosong | Muncul pesan penolakan yang jelas saat mencoba menambah item order dengan produk tersebut |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau bahan suatu menu habis di tengah jam operasional, staf bisa langsung menonaktifkan menu itu tanpa harus masuk ke halaman Products: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Pemesanan dan Order Meja — Modul Restaurant

Bab manual: [`restaurant/03-pemesanan-dan-order-meja.md`](../../erpApiServices/docs/manualBook/restaurant/03-pemesanan-dan-order-meja.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuka Order Baru (draf) | Klik "+ Pesanan Baru"; Area: "Kafe Sehat", Table: "T102", Pax: 4, Order Type: Dine In; Open Order | Meja T102 berubah status menjadi Occupied dan otomatis pindah ke halaman detail order |
| Negatif — Menambah Item ke Order (draf) | Area: "Kafe Sehat", Table: "T102" (Occupied), Pax: 4, Order Type: Dine In; Pilih Paracetamol 500 mg strip (SKU OBT-001) di dropdown, isi Qty: 3, Unit Price: 8000, Notes: "tanpa efek samping"; Klik Add | Tombol Add disabled pesan penolakan yang jelas karena channel penjualan restaurant dimatikan untuk cabang ini |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Table — meja yang dipakai (wajib). Meja berstatus Occupied akan tampil disabled di daftar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pax — jumlah tamu (wajib, minimal 1) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item yang berasal dari QR Self-Order pelanggan (badge "Perlu Konfirmasi") harus dikonfirmasi waiter dulu sebelum bisa masuk proses dapur — lihat chapter 06. QR Self-Order |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Setiap item wajib di-assign ke salah satu grup tagihan (klik nomor grup di sebelah item). Tambah grup baru dengan "+ Tambah Tagihan" kalau perlu lebih dari 2 tagihan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Kitchen Display System dan Order Items — Modul Restaurant

Bab manual: [`restaurant/04-kitchen-display-dan-order-items.md`](../../erpApiServices/docs/manualBook/restaurant/04-kitchen-display-dan-order-items.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengonfirmasi pesanan self-order (draf) | Pilih order OBT-001 dari dropdown; klik "Konfirmasikan Semua" | Semua item pesanan OBT-001 berubah status menjadi served, panel konfirmasi hilang, KDS menampilkan tiket OBT-001 |
| Negatif — Menolak item self-order yang sudah ready (draf) | Pilih order ALK-002; klik ikon X pada item yang ready; pesan "Tidak bisa tolak item ready" muncul | Item tetap berstatus ready, status tidak berubah, pesan error jelas muncul di halaman |
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
| Positif — Membuat Reservasi Baru (draf) | Klik "+ Buat Pemesanan"; Pilih Table ALK-001; Isi Guest Name "John Doe", Guest Count 2, Booking Date & Time 2023-10-05 18:00; Klik Save | Reservasi dikonfirmasi dengan status pending |
| Negatif — Tidak Bisa Save Reservasi (draf) | Klik "+ Buat Pemesanan"; Meja kosong; Isi Guest Name "Jane Doe", Guest Count 4, Booking Date & Time 2023-10-05 19:00 tanpa pilih meja; Coba Save | Tampilan error pesan yang jelas dan tidak bisa Save |
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
| Positif — Tamu memesan menu lewat QR self-order (draf) | Tamu scan QR meja OBT-001; memilih Paracetamol 500 mg strip, mengonfirmasi pesanan | Pesanan masuk antrian konfirmasi waiter; meja OBT-001 menampilkan ikon QR berkedip |
| Negatif — Wajib konfirmasi waiter diaktifkan dan channel penjualan restaurant dimatikan (draf) | Tamu scan QR meja ALK-002; memilih Masker Medis box 50; pesanan masuk antrian konfirmasi waiter | Muncul pesan penolakan yang jelas pada halaman menu tamu; meja ALK-002 tidak menampilkan ikon QR berkedip |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Diagram Alur Restaurant — Modul Restaurant

Bab manual: [`restaurant/07-diagram-alur-restaurant.md`](../../erpApiServices/docs/manualBook/restaurant/07-diagram-alur-restaurant.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pola Pesanan Bayar Dulu (draf) | Pilih menu Paracetamol 500 mg strip (SKU OBT-001), bayar dulu, pilih meja 2, cek out di POS; Status pesanan: Paid; Item: Ordered, Served | Meja 2 dibayar dan item siap jual langsung |
| Negatif — Pembatalan Item Ready (draf) | Pilih menu Amoxicillin 500 mg (OBT-002), bayar dulu, pilih meja 3, cek out di POS; Batal pesanan sebelum Ready; Status pesanan: Cancelled; Item: Ordered | Meja 3 dibatalkan dan item tidak diproses lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item yang sudah Served tidak bisa dimajukan lagi, kecuali dikembalikan ke Preparing |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | B --/"Belum"/ C["Complete ditolak<br/pesanan belum dibayar"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | D --/"Ya"/ E["Complete ditolak<br/masih ada item belum dihidangkan"] |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Pencatatan Bahan dan Estimasi Porsi — Modul Restaurant

Bab manual: [`restaurant/08-pencatatan-bahan-dan-estimasi-porsi.md`](../../erpApiServices/docs/manualBook/restaurant/08-pencatatan-bahan-dan-estimasi-porsi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengatur estimasi bahan (draf) | Buka Ingredient Forecast Settings; pilih Gudang bahan = gudang cabang, Metode pembagian bahan bersama = By Sales Share, Jendela laju pemakaian = Today, Batas persen persetujuan = 5%, Tawarkan Purchase Request = checked, Save | Estimasi berhasil disimpan dengan pengaturan yang ditentukan |
| Negatif — Input alasan salah (draf) | Buka Ingredient Stock Recording; pilih Addition untuk bahan Paracetamol 500 mg strip (SKU OBT-001), qty = 200, alasan = Failed Cooking, Save | Muncul pesan galat pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hanya produk yang menjadi bahan di sebuah resep yang bisa dicatat. Produk lain ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi qty (tidak boleh negatif) dan, bila perlu, biaya per unit dan catatan. Satu pencatatan boleh memuat sampai 200 baris |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Restoran di Terminal POS: Denah, Booking, Pesanan QR, dan Panggilan Siap — Modul Restaurant

Bab manual: [`restaurant/09-restoran-di-terminal-pos.md`](../../erpApiServices/docs/manualBook/restaurant/09-restoran-di-terminal-pos.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Memulai Pesanan di Meja Kosong (draf) | 1. Klik Denah; 2. Pilih meja kosong; 3. Tambahkan item pesanan; 4. Konfirmasi pesanan | Meja berubah ke status terisi, item muncul dalam pesanan, dan notifikasi dikirim ke dapur |
| Negatif — Pesanan QR Ditolak Karena Bahan Kurang (draf) | 1. Coba konfirmasi pesanan QR; 2. Pilih meja dengan pesanan QR; 3. Tambahkan item yang tidak tersedia | Pesanan ditolak, pesan penolakan yang jelas, dan status pesanan tetap menunggu konfirmasi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pesanan ditolak bila bahan tidak cukup, bila pengaturan penolakan penjualan saat bahan kurang aktif |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Makanan yang sudah siap tidak bisa dibatalkan dari terminal. Dapur bisa mengembalikannya ke preparing |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
