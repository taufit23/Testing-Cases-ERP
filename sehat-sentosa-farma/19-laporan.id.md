---
title: (PT Sehat Sentosa Farma) — 19. Laporan
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul reports untuk skenario PT Sehat Sentosa Farma. Laporan lintas modul dan ekspor.
visibility: internal
---

# 19. Laporan

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Laporan mendukung cabang anak bila cabang aktif adalah cabang utama.
- Ekspor PDF dan Excel memakai bahasa pengguna dan tata letak cabang.

## 1. Laporan Lintas Modul — Reports

Bab manual: [`reports/01-laporan-lintas-modul.md`](../../erpApiServices/docs/manualBook/reports/01-laporan-lintas-modul.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Filter Utang Piutang Jatuh Tempo (draf) | Input tanggal awal dan akhir, pilih cabang, klik filter; laporan berisi data utang piutang jatuh tempo sesuai kriteria | Laporan mengandung data utang piutang jatuh tempo dari periode dan cabang yang ditentukan |
| Negatif — Filter Umur Utang Piutang Tidak Valid (draf) | Input tanggal tidak valid, klik filter; pesan penolakan yang jelas | Laporan ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Fitur ini berguna untuk pemilik yang mau melihat kondisi seluruh jaringan cabang dari satu tempat, tanpa harus login/pindah ke tiap cabang satu per satu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Katalog Laporan per Modul — Laporan

Bab manual: [`reports/02-katalog-laporan-per-modul.md`](../../erpApiServices/docs/manualBook/reports/02-katalog-laporan-per-modul.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Katalog Laporan (draf) | Langkah: Pilih modul Accounting, pilih laporan Ringkasan Keuangan, klik 'Lihat' | Harapkan tampilan laporan Ringkasan Keuangan dengan data keuangan terbaru |
| Negatif — Katalog Laporan (draf) | Input: Memilih modul yang tidak ada, misal Modul X, dan pilih laporan apapun | Harus ditolak pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
