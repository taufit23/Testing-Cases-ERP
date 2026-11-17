---
title: (PT Medika Nusantara Sejahtera) — 19. Laporan
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul reports untuk skenario PT Medika Nusantara Sejahtera. Laporan lintas modul dan ekspor.
visibility: internal
---

# 19. Laporan

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji laporan: tampilan, filter, ekspor PDF dan Excel, dan ketepatan angka.
>
> **Kalau semuanya benar, artinya:** Laporan bisa dibuka cepat, hasil ekspor sama dengan layar, dan angkanya cocok dengan transaksi sumbernya.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Laporan mendukung cabang anak bila cabang aktif adalah cabang utama.
- Ekspor PDF dan Excel memakai bahasa pengguna dan tata letak cabang.

## 1. Laporan Lintas Modul — Reports

Bab manual: [`reports/01-laporan-lintas-modul.md`](../../erpApiServices/docs/manualBook/reports/01-laporan-lintas-modul.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menampilkan laporan AP Aging (draf) | Pilih menu `Laporan → Umur Piutang Usaha`; Isi As Of Date 31 Desember 2023; Klik "Jalankan Laporan"; Cek tabel hasil | Tabel menampilkan utang ke supplier, umur utang, dan total utang |
| Negatif — Filter tanggal tidak valid (draf) | Pilih menu `Laporan → Umur Piutang Usaha`; Isi As Of Date 31 Desember 2024 (tanggal di masa depan); Klik "Jalankan Laporan" | Muncul pesan penolakan yang jelas; Tabel kosong |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Fitur ini berguna untuk pemilik yang mau melihat kondisi seluruh jaringan cabang dari satu tempat, tanpa harus login/pindah ke tiap cabang satu per satu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Katalog Laporan per Modul — Laporan

Bab manual: [`reports/02-katalog-laporan-per-modul.md`](../../erpApiServices/docs/manualBook/reports/02-katalog-laporan-per-modul.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menampilkan laporan neraca (draf) | Kunjungi `/reports/balance-sheet`; perusahaan memiliki izin laporan neraca; modul Accounting aktif | Laporan neraca ditampilkan dengan detail akun, saldo, dan penjelasan di manual Accounting bab 05. |
| Negatif — Menampilkan laporan tanpa izin (draf) | Kunjungi `/reports/income-statement`; perusahaan tidak memiliki izin laporan laba rugi; modul Accounting aktif | Tampilan menunjukkan pesan penolakan yang jelas |
| Positif — Menampilkan laporan arus kas (draf) | Kunjungi `/reports/cash-flow-statement`; perusahaan memiliki izin laporan arus kas; modul Accounting aktif | Laporan arus kas ditampilkan dengan detail sumber dan penggunaan kas, penjelasan di manual Accounting bab 05. |
| Negatif — Menampilkan laporan arus kas tanpa izin (draf) | Kunjungi `/reports/cash-flow-statement`; perusahaan tidak memiliki izin laporan arus kas; modul Accounting aktif | Tampilan menunjukkan pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
