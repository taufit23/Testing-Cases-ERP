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
| Positif — Konfigurasi Wilayah (draf) | Membuat territory Jakarta, menugaskan salesperson A ke wilayah tersebut, dan membuat rute kunjungan ke 5 outlet mitra | Salesperson A dapat beraktivitas di wilayah Jakarta dengan rute yang telah disusun |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Modul Sales Canvassing dipakai untuk mengelola sales/salesman lapangan yang berkeliling ke outlet/toko. Sebelum sales bisa mulai kerja, dua hal wajib disiapkan dulu: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Route (Rute) — daftar outlet yang harus dikunjungi sales tersebut, beserta jadwalnya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Target Penjualan — Modul Sales Canvassing

Bab manual: [`canvassing/02-target-penjualan.md`](../../erpApiServices/docs/manualBook/canvassing/02-target-penjualan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Target Penjualan (draf) | Sales Bandung membuat target penjualan 500 SKU OBT-001 untuk wilayah Bandung | Target penjualan berhasil dibuat dan terlihat di daftar target |
| Negatif — Input Wilayah Tidak Ditemukan (draf) | Sales Surabaya mencoba membuat target penjualan tanpa memilih wilayah | Sistem menolak input dan memberikan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Minimal salah satu dari Target Quantity atau Target Amount harus diisi — tidak boleh keduanya kosong |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Titipan Stock Sales — Modul Sales Canvassing

Bab manual: [`canvassing/03-titipan-stock-sales.md`](../../erpApiServices/docs/manualBook/canvassing/03-titipan-stock-sales.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menitipkan Stock (draf) | Sales Jakarta meminta 100 box Masker Medis box 50 (ALK-001) dari gudang; Gudang mengirim ke sales; Status titipan tercatat dengan benar | Status titipan ALK-001 di sales Jakarta berubah menjadi 100 box, sisa stok di gudang berkurang sesuai yang ditempatkan |
| Negatif — Input Salah (draf) | Sales Surabaya meminta 200 box Masker Medis (input salah SKU) dari gudang; Sistem menolak pesan penolakan yang jelas | Input di tolak dan muncul pesan kesalahan yang jelas tentang kesalahan input SKU |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Di halaman detail custody, klik "Record Return", lalu untuk tiap item isi jumlah yang dikembalikan (tidak boleh melebihi sisa Outstanding item tersebut). Klik Save untuk menyimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Halaman ini berguna untuk cek cepat "sales A masih pegang stock apa saja" tanpa harus membuka satu per satu dokumen custody-nya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Kunjungan dan Order Lapangan — Modul Sales Canvassing

Bab manual: [`canvassing/04-kunjungan-dan-order-lapangan.md`](../../erpApiServices/docs/manualBook/canvassing/04-kunjungan-dan-order-lapangan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Kunjungan Harian (draf) | Check-in dengan nomor kunjungan; Buat order cepat obat Paracetamol 500 mg strip; Kumpulkan pembayaran QRIS; Simpan bukti kunjungan; Check-out | Proses kunjungan berhasil dilakukan, data tercatat dengan benar |
| Negatif — Input Nomor Kunjungan Salah (draf) | Check-in dengan nomor kunjungan yang tidak valid; Sistem menolak dan memberikan pesan penolakan yang jelas | Kunjungan ditolak karena nomor kunjungan salah, perlu diulangi dengan nomor yang benar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Pilih mode: Sales (order barang biasa) atau Rental (sewa aset — hanya bisa dibuat saat online, karena kantor perlu cek ketersediaan aset) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Fitur ini butuh koneksi internet aktif — tidak bisa dipakai saat offline |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau outlet tidak bisa dikunjungi, klik "Skip" dan isi alasan — status berubah menjadi Skipped |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Penagihan Lapangan — Modul Sales Canvassing

Bab manual: [`canvassing/05-penagihan-lapangan.md`](../../erpApiServices/docs/manualBook/canvassing/05-penagihan-lapangan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Penagihan Lapangan (draf) | Sales mencatat pembayaran OBT-001 dari Apotek Mitra Sehat, kantor setor ke bank | Pembayaran tercatat dan setoran dilakukan dengan benar |
| Negatif — Penagihan Lapangan (draf) | Sales mencatat pembayaran OBT-002 tanpa resep, ditolak karena pelanggaran aturan QRIS | Tidak dapat mencatat pembayaran, sistem menunjukkan pesan kesalahan dan menyebutkan syarat yang tidak terpenuhi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Competitor Tracking — Modul Sales Canvassing

Bab manual: [`canvassing/06-competitor-tracking.md`](../../erpApiServices/docs/manualBook/canvassing/06-competitor-tracking.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambahkan Data Competitor (draf) | Sales mencatat informasi kompetitor di Apotek Mitra Sehat; memasukkan nama, alamat, dan produk yang ditawarkan | Data kompetitor tercatat dengan benar dalam sistem |
| Negatif — Input Alamat Tidak Valid (draf) | Sales mencoba menyimpan data kompetitor dengan alamat tidak valid; sistem menolak input pesan penolakan yang jelas | Input gagal dan sales diberi notifikasi kesalahan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Kunjungan ke Calon Pelanggan — Modul Sales Canvassing

Bab manual: [`canvassing/07-kunjungan-ke-calon-pelanggan.md`](../../erpApiServices/docs/manualBook/canvassing/07-kunjungan-ke-calon-pelanggan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Kunjungan ke Calon Pelanggan (draf) | Sales mengunjungi Apotek Mitra Sehat, mencatat calon, check-in otomatis, isi hasil kunjungan, membuat penawaran produk Paracetamol 500 mg strip (SKU OBT-001) dan Amoxicillin 500 mg (OBT-002), tindak lanjut dengan presentasi kembali | Calon menjadi pelanggan yang diteruskan ke proses penjualan lebih lanjut |
| Negatif — Kunjungan ke Calon Pelanggan (draf) | Sales mencoba mengunjungi Klinik Pratama tanpa check-in, input data calon tidak lengkap, hasil kunjungan kosong, penawaran produk tidak valid | Kunjungan ditolak karena data calon dan hasil kunjungan tidak memenuhi syarat, harus diulangi dengan data yang lengkap dan valid |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Calon yang sudah menjadi pelanggan tidak dapat dihapus |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Konfigurasi Canvassing — Hasil Kunjungan, Calon Pelanggan, dan Pengaturan Cabang

Bab manual: [`canvassing/08-konfigurasi-canvassing.md`](../../erpApiServices/docs/manualBook/canvassing/08-konfigurasi-canvassing.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi sukses (draf) | Menambahkan hasil kunjungan ke klinik Pratama, menandai calon pelanggan Apotek Mitra sebagai potensial, mengatur awalan nomor 081 dan batas kredit 2.5jt | Daftar hasil kunjungan terperinci, calon pelanggan dengan status yang jelas, pengaturan cabang sesuai kebutuhan |
| Negatif — Input salah (draf) | Menambahkan alasan kunjungan tanpa tindak lanjut wajib, menandai calon pelanggan tanpa konversi, mengatur awalan nomor 081234567890 dan batas kredit -1jt | Tampilan error validasi, pesan kesalahan yang jelas tentang input tidak sesuai syarat |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menambah hasil sendiri: klik Create, isi kode dan nama, tentukan aturan alasan/tindak lanjut, lalu simpan. Hasil yang sudah dipakai kunjungan tidak dapat dihapus; nonaktifkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Pelacakan Gerak dan Klaim Biaya Sales — Modul Sales Canvassing

Bab manual: [`canvassing/09-pelacakan-gerak-dan-klaim-biaya.md`](../../erpApiServices/docs/manualBook/canvassing/09-pelacakan-gerak-dan-klaim-biaya.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Skenario Pelacakan Gerak dan Klaim Biaya Sales (draf) | Sales memulai hari dengan checklist perhentian, memberi tujuan pada kunjungan, mengajukan klaim biaya operasional; atasan menyetujui & membayar; admin memantau | Proses pelacakan gerak dan klaim biaya berjalan lancar, sales terarah, keuangan terkontrol |
| Negatif — Skenario Pelacakan Gerak dan Klaim Biaya Sales (draf) | Sales lupa checklist perhentian, tujuan kunjungan tidak jelas, klaim biaya operasional tidak valid; atasan menolak klaim, admin meminta penjelasan | Proses pelacakan gerak dan klaim biaya terhambat, sales diarahkan ulang, keuangan dipertanyakan validitasnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Buka My Day, tekan Mulai Hari Kerja. Absen dari rumah atau di mana saja tetap dimungkinkan bila HRM mengizinkan; cabang dapat mewajibkan absen terlebih dulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 5. Klaim yang ditolak dapat dibuka kembali sebagai draf dan diperbaiki |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pengaturan Klaim: wajib persetujuan, jendela pengajuan, akun utang karyawan, pusat biaya bawaan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tujuan Perhentian: daftar alasan perhentian, apakah dihitung sebagai kerja, pribadi, dan wajib catatan/foto |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Konfigurasi Klaim Biaya Sales Lapangan

Bab manual: [`canvassing/10-konfigurasi-klaim-biaya.md`](../../erpApiServices/docs/manualBook/canvassing/10-konfigurasi-klaim-biaya.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi berhasil (draf) | Persetujuan Direktur, batas 5 hari, periode Jan-Mar, kendaraan bawaan iya, biaya manual Rp100.000, transfer bank, akun 23456789 | Aturan klaim disetujui dengan detail yang diberikan |
| Negatif — Penolakan konfigurasi (draf) | Persetujuan tidak ada, batas luar jangka waktu, periode di luar rentang, kendaraan bawaan tidak iya, biaya manual negatif, pembayaran tunai, akun tidak valid | Konfigurasi ditolak karena syarat-syarat tidak terpenuhi, periksa kembali detail yang diberikan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila Klaim wajib disetujui dimatikan, klaim yang diajukan langsung disetujui otomatis |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila dibayar bersama gaji: biaya riil keluar bersama transfer gaji tanpa pajak, sedangkan tunjangan tetap menjadi penghasilan kena pajak; akun kas atau bank untuk penyelesaian payroll wajib diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Atur Klaim wajib disetujui, Batas hari pengajuan, dan Periode klaim terpanjang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Konfigurasi Pelacakan Lapangan (GPS)

Bab manual: [`canvassing/11-konfigurasi-pelacakan-lapangan.md`](../../erpApiServices/docs/manualBook/canvassing/11-konfigurasi-pelacakan-lapangan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Konfigurasi mode pelacakan GPS, input lokasi sales valid, kualitas GPS baik, deteksi perhentian otomatis, data simpan 30 hari | Sukses konfigurasi, tampilan konfirmasi dengan detail setting yang diterapkan |
| Negatif — input salah (draf) | Input lokasi sales tidak valid, kualitas GPS buruk, tidak ada deteksi perhentian, masa simpan data kurang dari 15 hari | Gagal konfigurasi, muncul pesan galat pesan yang jelas, pesan yang jelas, pesan yang jelas, pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila wajib absen sebelum sesi kerja menyala, sales tidak bisa memulai sesi tanpa absen |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Atur sesi kerja: wajib absen, interval saat bergerak (detik), interval saat diam (detik), maksimum titik per unggahan, dan lama sesi maksimum (jam) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Sesi Kerja, Tujuan Perhentian, Pelacakan Langsung, dan Harga Pesaing

Bab manual: [`canvassing/12-sesi-kerja-perhentian-dan-harga-pesaing.md`](../../erpApiServices/docs/manualBook/canvassing/12-sesi-kerja-perhentian-dan-harga-pesaing.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Skenario (draf) | Memantau sesi kerja sales kantor pusat, mencatat posisi langsung di gudang, dan memperbarui daftar tujuan perhentian apotek mitra | Data sesi kerja lengkap, posisi barang akurat, tujuan perhentian terupdate dengan benar |
| Negatif — Skenario (draf) | Input data tujuan perhentian salah atau tidak ada harga pesaing ditemukan di lapangan | Tolakan dengan pesan jelas pesan yang jelas atau pesan yang jelas, meminta input ulang |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Stop Purposes (tujuan perhentian) memiliki kode, nama, penanda dihitung sebagai pekerjaan atau perhentian pribadi, kewajiban catatan, kewajiban foto, urutan, dan status aktif. Perhentian pribadi tidak dihitung sebagai pekerjaan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Master yang sudah dipakai tidak boleh dihapus; nonaktifkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi kode, nama, tandai dihitung sebagai pekerjaan atau pribadi, tandai catatan dan foto wajib bila perlu, atur urutan, lalu simpan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Diagram Alur Canvassing — Modul Canvassing

Bab manual: [`canvassing/13-diagram-alur-canvassing.md`](../../erpApiServices/docs/manualBook/canvassing/13-diagram-alur-canvassing.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal bab ini | Ikuti langkah di bab manual dengan data acuan file `00` (draf Ollama tidak dapat dipakai, isi manual) | Hasil sesuai uraian bab |
| Negatif — input tidak valid | Kosongkan field wajib atau isi di luar batas | Ditolak dengan pesan yang jelas, tidak ada data tersimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Skip dan Cancel bisa dilakukan dari status mana pun selain Completed dan Cancelled. Kunjungan yang sudah Completed atau Cancelled tidak bisa diubah lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | New -- Lost: Tidak jadi, alasan wajib |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Contacted -- Lost: Tidak jadi, alasan wajib |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Interested -- Lost: Tidak jadi, alasan wajib |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 14. Kebijakan Kerja Sales, Kepemilikan Pelanggan, dan Kolam Lead — Modul Canvassing

Bab manual: [`canvassing/14-kepemilikan-pelanggan-dan-kolam-lead.md`](../../erpApiServices/docs/manualBook/canvassing/14-kepemilikan-pelanggan-dan-kolam-lead.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengatur kebijakan kerja (draf) | Salesman mendefinisikan wilayah dan rute; memilih kepemilikan akun; menambahkan kolam lead | Kebijakan berhasil ditetapkan dengan wilayah, rute, kepemilikan akun, dan kolam lead yang jelas |
| Negatif — Memasukkan wilayah duplikat (draf) | Salesman mencoba mengatur wilayah yang sama untuk sales lain; sistem menolak | Wilayah sudah ditempati oleh salesman lain, silakan pilih wilayah lain |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Lead harus dikonversi menjadi pelanggan sebelum menerima order lapangan atau penagihan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Lead yang sudah dikonversi menjadi pelanggan tidak bisa diambil dari kolam maupun dilepas ke kolam |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sistem menolak transfer bila pemilik baru sama dengan pemilik sekarang, atau bila sudah ada transfer yang menunggu keputusan. Approve ditolak bila pemilik sudah berubah sejak transfer diajukan, dan Anda perlu mengajukan ulang |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Di Leads, salesperson klik Claim Lead pada lead di kolam. Sistem menolak bila: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
