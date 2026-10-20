---
title: (PT Sehat Sentosa Farma) — 15. Keuangan: Biaya dan Pembayaran Online
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul finance untuk skenario PT Sehat Sentosa Farma. Pencatatan biaya, persetujuan dan pembayaran online.
visibility: internal
---

# 15. Keuangan: Biaya dan Pembayaran Online

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Biaya per kategori dengan persetujuan di atas batas; jurnal biaya saat disetujui.
- Pembayaran online (QRIS) dan transfer bank keluar (payout) lewat penyedia sandbox; status mengikuti peta status penyedia.
- Penyelesaian (settlement) dan akun penampung penyedia.

## 1. Kategori & Pencatatan Biaya — Modul Expense

Bab manual: [`finance/01-kategori-dan-pencatatan-biaya.md`](../../erpApiServices/docs/manualBook/finance/01-kategori-dan-pencatatan-biaya.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Expense Category (draf) | Buat kategori 'Biaya Gudang' di Sentosa Farma; Tambah item biaya 'Gaji Karyawan Gudang', status draft; Simpan | Berhasil membuat kategori dengan item biaya dan status draft |
| Negatif — Menandai Expense Sudah Dibayar (draf) | Coba tandai expense 'Biaya Gaji Januari' yang belum dibayar; Terima permintaan dengan pesan 'Harus dalam status Draft' | Permintaan ditolak dengan pesan 'Harus dalam status Draft untuk diubah ke Paid' |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Pilih Expense Category (wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi Expense Date (wajib) dan Due Date (opsional, kalau biaya ini punya tenggat pembayaran) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 7. Minimal harus ada 1 item dan setiap item wajib punya deskripsi sebelum bisa disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Expense hanya bisa diedit dan dihapus selama masih berstatus draft. Begitu status berubah (misalnya sudah ditandai Paid), tombol Delete di halaman detail otomatis nonaktif — ini untuk menjaga riwayat pengeluaran yang sudah difinalisasi tidak berubah-ubah |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Pembayaran Online, Rute Penyedia, dan Penyelesaian Dana

Bab manual: [`finance/02-pembayaran-online-dan-penyelesaian.md`](../../erpApiServices/docs/manualBook/finance/02-pembayaran-online-dan-penyelesaian.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Urutan Penyedia dan Cadangan (draf) | Konfigurasi QRIS dengan cadangan bank BCA dan Mandiri; memantau transaksi; mencatat dana dicairkan ke rekening bank | Proses pembayaran online lancar, catatan pencairan dana akurat |
| Negatif — Input Data Penyedia Salah (draf) | Menginput nama penyedia pembayaran yang tidak ada; pesan kesalahan muncul | Pengisian data penyedia pembayaran harus sesuai dengan daftar yang tersedia |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sebelum bisa mencatat penyelesaian, akun penampung pembayaran online harus sudah dipetakan di POS → POS Configs; bila belum, halaman menampilkan peringatan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
