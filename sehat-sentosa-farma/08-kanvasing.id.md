---
title: (PT Sehat Sentosa Farma) — 08. Kanvasing (Sales Lapangan)
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul canvassing untuk skenario PT Sehat Sentosa Farma. Kunjungan, calon pelanggan, stok titipan dan penagihan lapangan.
visibility: internal
---

# 08. Kanvasing (Sales Lapangan)

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Calon pelanggan terpisah dari master pelanggan; menang hanya lewat konversi; kalah wajib alasan.
- Kunjungan tak terjadwal melakukan check-in GPS otomatis; hasil kunjungan berasal dari master yang bisa dikonfigurasi.
- Stok titipan sales mengurangi gudang dan menjadi dasar order lapangan.
- Penagihan lapangan dan setoran terjurnal; target dan realisasi per wilayah/sales.

## 1. Konfigurasi Wilayah dan Rute — Modul Sales Canvassing

Bab manual: [`canvassing/01-konfigurasi-wilayah-dan-rute.md`](../../erpApiServices/docs/manualBook/canvassing/01-konfigurasi-wilayah-dan-rute.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi Wilayah (draf) | Membuat territory Jakarta, menugaskan salesperson A ke wilayah tersebut, membuat rute kunjungan ke 10 outlet mitra | Salesperson A dapat beroperasi di wilayah dan rute yang telah disusun dengan baik |
| Negatif — Menambah Outlet (draf) | Tambah outlet tanpa ada territory terlebih dahulu, pesan penolakan yang jelas | Input ditolak dengan pesan yang jelas tentang syarat wajib terpenuhi sebelum menambah outlet ke rute kunjungan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Modul Sales Canvassing dipakai untuk mengelola sales/salesman lapangan yang berkeliling ke outlet/toko. Sebelum sales bisa mulai kerja, dua hal wajib disiapkan dulu: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Route (Rute) — daftar outlet yang harus dikunjungi sales tersebut, beserta jadwalnya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Target Penjualan — Modul Sales Canvassing

Bab manual: [`canvassing/02-target-penjualan.md`](../../erpApiServices/docs/manualBook/canvassing/02-target-penjualan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Target Penjualan (draf) | Masuk ke modul Sales Canvassing; Pilih wilayah Jakarta; Isi data penjualan target bulanan 10 juta; Simpan | Target penjualan berhasil dibuat dan terlihat di daftar |
| Negatif — Input Target Nol (draf) | Masuk ke modul Sales Canvassing; Pilih wilayah Jakarta; Isi data penjualan target bulanan nol; Coba simpan | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Minimal salah satu dari Target Quantity atau Target Amount harus diisi — tidak boleh keduanya kosong |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Titipan Stock Sales — Modul Sales Canvassing

Bab manual: [`canvassing/03-titipan-stock-sales.md`](../../erpApiServices/docs/manualBook/canvassing/03-titipan-stock-sales.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menitipkan Stock ke Sales (draf) | Gudang Jakarta menitipkan 100 botol Paracetamol kepada sales Bandung; data: SKU OBT-001, jumlah 100, lokasi gudang A, tanggal 25/10/2023 | Transaksi berhasil dilakukan; stock di gudang berkurang, sisa stock diperbarui; notifikasi pengiriman dikirimkan kepada sales Bandung |
| Negatif — Input Lokasi Salah (draf) | Gudang Jakarta menitipkan 100 botol Paracetamol ke lokasi sales Surabaya (input salah); data: SKU OBT-001, jumlah 100, lokasi gudang A, tanggal 25/10/2023 | Transaksi ditolak; pesan error menunjukkan input lokasi sales tidak valid; stock di gudang tetap sama |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Di halaman detail custody, klik "Record Return", lalu untuk tiap item isi jumlah yang dikembalikan (tidak boleh melebihi sisa Outstanding item tersebut). Klik Save untuk menyimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Halaman ini berguna untuk cek cepat "sales A masih pegang stock apa saja" tanpa harus membuka satu per satu dokumen custody-nya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Kunjungan dan Order Lapangan — Modul Sales Canvassing

Bab manual: [`canvassing/04-kunjungan-dan-order-lapangan.md`](../../erpApiServices/docs/manualBook/canvassing/04-kunjungan-dan-order-lapangan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Check In (draf) | Sales masuk ke aplikasi, memilih lokasi kunjungan dan check-in | Berhasil check-in dengan status kunjungan menjadi pesan yang jelas |
| Negatif — Input Lokasi Salah (draf) | Sales memasukkan alamat yang tidak sesuai dengan rencana kunjungan | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Pilih mode: Sales (order barang biasa) atau Rental (sewa aset — hanya bisa dibuat saat online, karena kantor perlu cek ketersediaan aset) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Fitur ini butuh koneksi internet aktif — tidak bisa dipakai saat offline |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau outlet tidak bisa dikunjungi, klik "Skip" dan isi alasan — status berubah menjadi Skipped |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Penagihan Lapangan — Modul Sales Canvassing

Bab manual: [`canvassing/05-penagihan-lapangan.md`](../../erpApiServices/docs/manualBook/canvassing/05-penagihan-lapangan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Penagihan Lapangan (draf) | Sales mencatat pembayaran OBT-001 dari Apotek Mitra Sehat; kantor menerima setoran; deposit tercatat; status pembayaran valid. | Pembayaran diterima dan dicatat dengan benar, sistem menandai sebagai disetor. |
| Negatif — Penagihan Lapangan (draf) | Sales mencoba memasukkan pembayaran OBT-001 tanpa NPWP; ditolak pesan penolakan yang jelas | Input ditolak dan sales diminta mengisi NPWP yang valid. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Competitor Tracking — Modul Sales Canvassing

Bab manual: [`canvassing/06-competitor-tracking.md`](../../erpApiServices/docs/manualBook/canvassing/06-competitor-tracking.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambahkan Data Competitor (draf) | Sales mencatat informasi kompetitor pada modul, data tersimpan dengan benar | Data kompetitor ditampilkan dengan lengkap dan akurat |
| Negatif — Input nama kompetitor kosong (draf) | Tindakan ditolak karena syarat tidak terpenuhi, pesan penolakan yang jelas | Tindakan ditolak dengan pesan jelas pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Kunjungan ke Calon Pelanggan — Modul Sales Canvassing

Bab manual: [`canvassing/07-kunjungan-ke-calon-pelanggan.md`](../../erpApiServices/docs/manualBook/canvassing/07-kunjungan-ke-calon-pelanggan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Kunjungan ke Calon Pelanggan (draf) | Sales melakukan kunjungan, memasukkan data calon, mengecek pesaing, membuat penawaran, dan mengubah status menjadi pelanggan | Proses berjalan lancar, calon menjadi pelanggan baru |
| Negatif — Input Data Salah (draf) | Sales memasukkan SKU produk yang tidak tersedia, sistem menolak pesan penolakan yang jelas | Kunjungan ditolak, sales diminta memeriksa kembali data produk |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Calon yang sudah menjadi pelanggan tidak dapat dihapus |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Konfigurasi Canvassing — Hasil Kunjungan, Calon Pelanggan, dan Pengaturan Cabang

Bab manual: [`canvassing/08-konfigurasi-canvassing.md`](../../erpApiServices/docs/manualBook/canvassing/08-konfigurasi-canvassing.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi berhasil (draf) | Atur alasan kunjungan pesan yang jelas, tindak lanjut wajib pesan yang jelas; status calon pesan yang jelas, awalan nomor 081, kredit 500jt | Daftar hasil kunjungan dan calon pelanggan diperbarui sesuai settingan; pengaturan cabang terkonfigurasi dengan benar |
| Negatif — Konfigurasi ditolak (draf) | Input alasan pesan yang jelas yang tidak valid, tindak lanjut wajib kosong; status calon "Tidak Tertarik", awalan nomor 082, kredit 1jt diabaikan | Pengaturan ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menambah hasil sendiri: klik Create, isi kode dan nama, tentukan aturan alasan/tindak lanjut, lalu simpan. Hasil yang sudah dipakai kunjungan tidak dapat dihapus; nonaktifkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
