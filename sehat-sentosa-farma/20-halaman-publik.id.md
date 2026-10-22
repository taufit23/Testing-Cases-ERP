---
title: (PT Sehat Sentosa Farma) — 20. Halaman Publik
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul halaman-publik untuk skenario PT Sehat Sentosa Farma. Halaman tanpa login untuk pihak luar.
visibility: internal
---

# 20. Halaman Publik

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** **Tanpa login.** Buka tautan publik dari browser jendela penyamaran, supaya tidak terbaca sebagai pengguna masuk.

**Cabang aktif:** tidak berlaku.

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- Token kedaluwarsa dan tidak dapat ditebak; data internal tidak bocor.
- Halaman karier, penawaran, tautan bayar, pemberitahuan pengiriman pemasok dan penangguhan klien menutup semuanya.

## 1. Halaman untuk Pihak Luar: Pelamar, Penawaran, Restoran, dan Pengiriman Pemasok

Bab manual: [`halaman-publik/01-halaman-untuk-pihak-luar.md`](../../erpApiServices/docs/manualBook/halaman-publik/01-halaman-untuk-pihak-luar.md)

**Input di:** `Halaman Publik → Job Applications` (`/public/job-applications`) · `Halaman Publik → Quotations` (`/public/quotations`) · `Halaman Publik → Restaurant` (`/public/restaurant`) · `Halaman Publik → Supplier Shipment` (`/public/supplier-shipment`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Job Applications (draf) | Pelamar mengisi form dengan detail lengkap; Direktur memvalidasi dan menerima aplikasi | Aplikasi diterima dan pelamar mendapat konfirmasi email |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Your Name, Email (keduanya wajib), Phone Number, dan Company Name |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Di Items You Want To Request, isi nama atau deskripsi produk dan Qty untuk tiap barang; klik Add Item untuk menambah baris. Tiap barang harus punya deskripsi dan jumlah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Decline Offer — menolak penawaran |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tiap tanggapan tercatat dan ditampilkan sebagai pesan konfirmasi. Penawaran yang sudah ditanggapi tidak bisa ditanggapi lagi (You have already responded to this quotation) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
