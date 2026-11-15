---
title: (PT Sehat Sentosa Farma) — 20. Halaman Publik
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul halaman-publik untuk skenario PT Sehat Sentosa Farma. Halaman tanpa login untuk pihak luar.
visibility: internal
---

# 20. Halaman Publik

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Token kedaluwarsa dan tidak dapat ditebak; data internal tidak bocor.
- Halaman karier, penawaran, tautan bayar, pemberitahuan pengiriman pemasok dan penangguhan klien menutup semuanya.

## 1. Halaman untuk Pihak Luar: Pelamar, Penawaran, Restoran, dan Pengiriman Pemasok

Bab manual: [`halaman-publik/01-halaman-untuk-pihak-luar.md`](../../erpApiServices/docs/manualBook/halaman-publik/01-halaman-untuk-pihak-luar.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Job Applications (draf) | Pelamar mengisi form dengan data lengkap; Direksi menyetujui aplikasi | Pelamar diterima dan diinformasikan proses selanjutnya |
| Negatif — Quotations (draf) | Penawaran tanpa detail produk; Ditolak karena kurang informasi | Tidak valid, perlu mencantumkan SKU, jumlah, dan harga produk secara spesifik |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Your Name, Email (keduanya wajib), Phone Number, dan Company Name |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Di Items You Want To Request, isi nama atau deskripsi produk dan Qty untuk tiap barang; klik Add Item untuk menambah baris. Tiap barang harus punya deskripsi dan jumlah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Decline Offer — menolak penawaran |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tiap tanggapan tercatat dan ditampilkan sebagai pesan konfirmasi. Penawaran yang sudah ditanggapi tidak bisa ditanggapi lagi (You have already responded to this quotation) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Halaman Publik: Bayar Tagihan, Portal Proyek, Karier, dan Berhenti Berlangganan — Halaman Publik

Bab manual: [`halaman-publik/02-bayar-tagihan-portal-proyek-karier-dan-berhenti-berlangganan.md`](../../erpApiServices/docs/manualBook/halaman-publik/02-bayar-tagihan-portal-proyek-karier-dan-berhenti-berlangganan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membayar Faktur Penjualan (draf) | Kunjungi tautan, masukkan nomor faktur dan jumlah bayar, klik bayar; terima konfirmasi pembayaran berhasil | Berhasil membayar tagihan dengan notifikasi email |
| Negatif — Membayar Tagihan Langganan (draf) | Tidak login, coba bayar tagihan; pesan penolakan yang jelas | Harus login terlebih dahulu sebelum dapat membayar tagihan langganan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Token yang salah, dicabut, atau kedaluwarsa dijawab sama persis dengan token yang tidak ada, sehingga token tidak bisa ditebak dengan mencoba-coba |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Portal tidak menampilkan tarif, biaya, margin, gaji, atau data karyawan selain nama tampilan. Portal tidak dapat dibuka bila token dicabut atau kedaluwarsa, portal dimatikan, cabang disuspensi, atau proyek sudah tertutup. Semua kegagalan itu dijawab sama |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Penerima membuka tautan. Halaman hanya menampilkan konfirmasi, karena pemindai tautan di kotak surat sering membuka semua tautan dan tidak boleh memberhentikan langganan secara tidak sengaja |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Alamat yang berhenti berlangganan tidak bisa dicabut dari daftar penolakan oleh pengguna (bab 01. Kampanye Sales Outreach di Outreach) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
