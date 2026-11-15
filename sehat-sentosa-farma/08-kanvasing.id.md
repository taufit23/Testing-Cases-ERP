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
| Positif — Menambah outlet ke rute (draf) | Buka halaman detail rute pesan yang jelas; pilih pesan yang jelas dari dropdown; klik Add | Outlet pesan yang jelas ditambahkan ke rute dan muncul di bagian Stops |
| Negatif — Menugaskan sales tanpa territory (draf) | Buka form Territory; tidak memilih territory untuk sales "Kepala Gudang"; klik Save | Muncul pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Modul Sales Canvassing dipakai untuk mengelola sales/salesman lapangan yang berkeliling ke outlet/toko. Sebelum sales bisa mulai kerja, dua hal wajib disiapkan dulu: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Route (Rute) — daftar outlet yang harus dikunjungi sales tersebut, beserta jadwalnya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Target Penjualan — Modul Sales Canvassing

Bab manual: [`canvassing/02-target-penjualan.md`](../../erpApiServices/docs/manualBook/canvassing/02-target-penjualan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Pilih Type "Territorypesan yang jelasJakarta"; masukkan target quantity 100; klik Save | Target penjualan berhasil disimpan untuk wilayah Jakarta dengan target kuantitas 100 unit |
| Negatif — input salah (draf) | Tidak memilih Type, hanya mengisi Year dan Month; coba klik Save | Tombol Save tidak aktif/error, pesan penolakan yang jelas atau pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Minimal salah satu dari Target Quantity atau Target Amount harus diisi — tidak boleh keduanya kosong |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Titipan Stock Sales — Modul Sales Canvassing

Bab manual: [`canvassing/03-titipan-stock-sales.md`](../../erpApiServices/docs/manualBook/canvassing/03-titipan-stock-sales.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Klik pesan yang jelas; isi salesperson: Apoteker Penanggung Jawab, warehouse: Gudang Jakarta, tanggal: 10/10/2023, item: Paracetamol 500 mg strip (SKU OBT-001) qty: 10; klik Save | Custody baru terbentuk dengan status "issued", stok gudang berkurang 10 unit Paracetamol 500 mg strip, jurnal Persediaan Titipan Salesperson debit 10.000.000, Persediaan kredit 10.000.000 |
| Negatif — input salah (draf) | Klik pesan yang jelas; tidak memilih salesperson; klik Save | Tampilan pesan error: pesan yang jelas dan tombol Save tetap nonaktif, status custody tidak berubah, stok gudang tidak berpengaruh, jurnal tidak terbentuk |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Di halaman detail custody, klik "Record Return", lalu untuk tiap item isi jumlah yang dikembalikan (tidak boleh melebihi sisa Outstanding item tersebut). Klik Save untuk menyimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Halaman ini berguna untuk cek cepat "sales A masih pegang stock apa saja" tanpa harus membuka satu per satu dokumen custody-nya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Kunjungan dan Order Lapangan — Modul Sales Canvassing

Bab manual: [`canvassing/04-kunjungan-dan-order-lapangan.md`](../../erpApiServices/docs/manualBook/canvassing/04-kunjungan-dan-order-lapangan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Kunjungan Bandung (draf) | Check In; Quick Order (Sales mode) SKU OBT-001 qty 50, Collect Payment tunai Rp200.000; Proof; Check Out Outcome: Order Placed | Status kunjungan menjadi Completed, Sales Order draft dibuat dan terhubung ke kunjungan, kasir APOTek Sentosa Bandung diperbarui dengan pembayaran |
| Negatif — Kunjungan Sukabumi (offline) (draf) | Quick Order (Rental mode) tanpa koneksi internet; Save offline | Draft Rental order disimpan di antrean lokal perangkat, otomatis dikirim saat koneksi pulih, stok aset tidak berubah, limit kredit customer diperiksa setelah koneksi pulih |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Pilih mode: Sales (order barang biasa) atau Rental (sewa aset — hanya bisa dibuat saat online, karena kantor perlu cek ketersediaan aset) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Fitur ini butuh koneksi internet aktif — tidak bisa dipakai saat offline |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau outlet tidak bisa dikunjungi, klik "Skip" dan isi alasan — status berubah menjadi Skipped |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Penagihan Lapangan — Modul Sales Canvassing

Bab manual: [`canvassing/05-penagihan-lapangan.md`](../../erpApiServices/docs/manualBook/canvassing/05-penagihan-lapangan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat pembayaran (draf) | Sales mengakses /canvassing/collections; memilih invoice OBT-001, mengetik jumlah 50.000, pilih metode Cash; klik Record Payment | Pembayaran berhasil dicatat dengan status Collected, total Awaiting Deposit berkurang |
| Negatif — Void pembayaran yang sudah disetor (draf) | Sales mencoba void collection dengan status Deposited: Alkohol Swab (ALK-002) sebesar 100.000 | Tampilan pesan penolakan yang jelas dan status tetap Deposited |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Competitor Tracking — Modul Sales Canvassing

Bab manual: [`canvassing/06-competitor-tracking.md`](../../erpApiServices/docs/manualBook/canvassing/06-competitor-tracking.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal bab ini | Ikuti langkah di bab manual dengan data acuan file `00` (draf Ollama tidak dapat dipakai, isi manual) | Hasil sesuai uraian bab |
| Negatif — input tidak valid | Kosongkan field wajib atau isi di luar batas | Ditolak dengan pesan yang jelas, tidak ada data tersimpan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Kunjungan ke Calon Pelanggan — Modul Sales Canvassing

Bab manual: [`canvassing/07-kunjungan-ke-calon-pelanggan.md`](../../erpApiServices/docs/manualBook/canvassing/07-kunjungan-ke-calon-pelanggan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Kunjungan ke Calon Pelanggan (draf) | My Day; Kunjungan Baru; pilih Calon Baru; isi nama Apotek Mitra Sehat; check-in otomatis dengan GPS; hasil Tertarik; produk Paracetamol 500 mg strip; pesaing PT Bintang Farmasi Utama; catatan penawaran khusus | Calon menjadi pelanggan tertarik, tindak lanjut di My Day, formulir penawaran terbuka dengan Apotek Mitra Sehat |
| Negatif — Kunjungan ke Calon Pelanggan (draf) | My Day; Kunjungan Baru; pilih Calon Baru; isi nama tidak valid; check-in otomatis dengan GPS | Sistem menolak, pesan penolakan yang jelas dan tidak dapat check-in |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Calon yang sudah menjadi pelanggan tidak dapat dihapus |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Konfigurasi Canvassing — Hasil Kunjungan, Calon Pelanggan, dan Pengaturan Cabang

Bab manual: [`canvassing/08-konfigurasi-canvassing.md`](../../erpApiServices/docs/manualBook/canvassing/08-konfigurasi-canvassing.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah hasil kunjungan baru (draf) | Masuk ke `/canvassing/visit-outcomes`, klik Create, masukkan kode "INT", nama "Minta informasipesan yang jelasInterested", isikan alasan dan tanggal tindak lanjut, simpan. | Hasil "Interested" muncul di daftar hasil kunjungan dengan status aktif |
| Negatif — Mencoba menghapus hasil yang digunakan (draf) | Masuk ke `/canvassing/visit-outcomes`, pilih "Tertarik", cek tombol Delete, klik Delete. | Pesan pesan yang jelas muncul |
| Negatif — Mencoba check-out tanpa alasan (draf) | Kunjungi apotek Sentosa Bandung, masuk ke Check-out, pilih hasil "Tertarik" tanpa mengisi alasan. | Pesan pesan yang jelas ditampilkan dan check-out ditolak |
| Negatif — Mencoba check-out tanpa tanggal tindak lanjut (draf) | Kunjungi klinik Pratama Bekasi, masuk ke Check-out, pilih hasil "Minta penawaran", tidak mengisi tanggal tindak lanjut. | Pesan pesan yang jelas ditampilkan dan check-out ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menambah hasil sendiri: klik Create, isi kode dan nama, tentukan aturan alasan/tindak lanjut, lalu simpan. Hasil yang sudah dipakai kunjungan tidak dapat dihapus; nonaktifkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Pelacakan Gerak dan Klaim Biaya Sales — Modul Sales Canvassing

Bab manual: [`canvassing/09-pelacakan-gerak-dan-klaim-biaya.md`](../../erpApiServices/docs/manualBook/canvassing/09-pelacakan-gerak-dan-klaim-biaya.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Untuk sales (draf) | Buka My Day; Mulai Hari Kerja; Absen dari rumah; Kunjungi 3 klien; Berhenti di SPBU untuk belanja perlengkapan; Akhiri Hari Kerja | Perekaman gerak tercatat, perhentian diklaim, klaim biaya dapat dibuat |
| Negatif — Untuk atasan dan keuangan (draf) | Meninjau klaim tanpa persetujuan sales; Setujui klaim tanpa bukti | Tampilan pesan penolakan yang jelas, klaim tidak disetujui, status klaim tetap menunggu persetujuan sales |
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
| Positif — Atur konfigurasi klaim untuk cabang Jakarta (draf) | Buka `Canvassing → Claim Configs`; atur `Klaim wajib disetujui` = Mati, `Batas hari pengajuan` = 30, `Periode klaim terpanjang` = 15; pilih `Mobil` untuk kendaraan bawaan; atur `Cara pembayaran` = Dibayar bersama gaji dan isi akun kas atau bank payroll; klik Simpan | Aturan baru berlaku pada klaim berikutnya |
| Negatif — Tidak memilih akun utang karyawan saat mengatur konfigurasi klaim untuk cabang Bandung (draf) | Buka `Canvassing → Claim Configs`; atur `Akun utang karyawan` = tidak dipilih; coba Simpan | Muncul pesan galat pesan yang jelas dan konfigurasi gagal disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila Klaim wajib disetujui dimatikan, klaim yang diajukan langsung disetujui otomatis |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila dibayar bersama gaji: biaya riil keluar bersama transfer gaji tanpa pajak, sedangkan tunjangan tetap menjadi penghasilan kena pajak; akun kas atau bank untuk penyelesaian payroll wajib diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Atur Klaim wajib disetujui, Batas hari pengajuan, dan Periode klaim terpanjang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Konfigurasi Pelacakan Lapangan (GPS)

Bab manual: [`canvassing/11-konfigurasi-pelacakan-lapangan.md`](../../erpApiServices/docs/manualBook/canvassing/11-konfigurasi-pelacakan-lapangan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengatur mode pelacakan cabang (draf) | Buka Canvassing → Field Tracking Configs; Pilih Mode pelacakan cabang Terus-menerus; Atur wajib absen sebelum sesi Saklar; Simpan | Sesi kerja berikutnya mengikuti aturan baru, tidak ada pesan galat |
| Negatif — Mengatur interval diam negatif (draf) | Buka Canvassing → Field Tracking Configs; Pilih Interval diam -10 detik; Coba Simpan | Muncul pesan galat pesan yang jelas dan tidak disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila wajib absen sebelum sesi kerja menyala, sales tidak bisa memulai sesi tanpa absen |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Atur sesi kerja: wajib absen, interval saat bergerak (detik), interval saat diam (detik), maksimum titik per unggahan, dan lama sesi maksimum (jam) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Sesi Kerja, Tujuan Perhentian, Pelacakan Langsung, dan Harga Pesaing

Bab manual: [`canvassing/12-sesi-kerja-perhentian-dan-harga-pesaing.md`](../../erpApiServices/docs/manualBook/canvassing/12-sesi-kerja-perhentian-dan-harga-pesaing.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Memantau sesi kerja sales (draf) | Buka Work Sessions; atur filter status "aktif" & tanggal 1-30 September; lihat sesi salesperson | Sesi aktif tampil dengan detail sesuai filter, jam mulai, jarak, waktu bergerak, dan perhentian |
| Negatif — Harga pesaing tanpa produk kita (draf) | Buka Competitor Prices; tambah data tanpa memilih produk kita; simpan | Muncul pesan penolakan yang jelas & tidak dapat disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Stop Purposes (tujuan perhentian) memiliki kode, nama, penanda dihitung sebagai pekerjaan atau perhentian pribadi, kewajiban catatan, kewajiban foto, urutan, dan status aktif. Perhentian pribadi tidak dihitung sebagai pekerjaan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Master yang sudah dipakai tidak boleh dihapus; nonaktifkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi kode, nama, tandai dihitung sebagai pekerjaan atau pribadi, tandai catatan dan foto wajib bila perlu, atur urutan, lalu simpan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Diagram Alur Canvassing — Modul Canvassing

Bab manual: [`canvassing/13-diagram-alur-canvassing.md`](../../erpApiServices/docs/manualBook/canvassing/13-diagram-alur-canvassing.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengubah status kunjungan ke Completed (draf) | Kunjungi klinik Pratama & Laboratorium Bekasi; Check in; Upload foto bukti kunjungan; Pilih status Completed | Status kunjungan berubah menjadi Completed, tidak bisa lagi diubah; Foto bukti kunjungan terlampir |
| Negatif — Menghapus kunjungan yang sudah Completed (draf) | Coba hapus kunjungan dengan status Completed; Muncul pesan penolakan yang jelas | Kunjungan tetap berstatus Completed, tidak bisa dihapus; Muncul pesan kesalahan yang jelas |
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
| Positif — Mengatur kebijakan kerja sales untuk kantor pusat (draf) | Buka `/canvassing/work-policies`; pilih skema 'kepemilikan akun' dengan 'Warn' jika keluar dari wilayah; simpan | Kebijakan kerja terapkan dan tampil di halaman `Sales Work Policy` |
| Negatif — Memindahkan kepemilikan tanpa persetujuan (draf) | Buka `/canvassing/ownerships`; pilih lead Sentosa Farma; klik transfer ke Direktur baru; tidak memerlukan persetujuan; tidak disetujui oleh pemegang izin | Transfer ditolak dengan pesan 'Transfer kepemilikan memerlukan persetujuan' |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Lead harus dikonversi menjadi pelanggan sebelum menerima order lapangan atau penagihan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Lead yang sudah dikonversi menjadi pelanggan tidak bisa diambil dari kolam maupun dilepas ke kolam |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sistem menolak transfer bila pemilik baru sama dengan pemilik sekarang, atau bila sudah ada transfer yang menunggu keputusan. Approve ditolak bila pemilik sudah berubah sejak transfer diajukan, dan Anda perlu mengajukan ulang |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Di Leads, salesperson klik Claim Lead pada lead di kolam. Sistem menolak bila: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
