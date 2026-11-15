---
title: (PT Sehat Sentosa Farma) — 18. Dasbor
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul dashboard untuk skenario PT Sehat Sentosa Farma. Angka ringkasan per peran.
visibility: internal
---

# 18. Dasbor

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Angka dasbor sama dengan laporan sumbernya; dasbor hanya menampilkan data cabang aktif atau gabungan sesuai peran.

## 1. Dashboard Akuntansi, Penjualan, Pembelian, dan Inventori

Bab manual: [`dashboard/01-dashboard-keuangan-penjualan-dan-pembelian.md`](../../erpApiServices/docs/manualBook/dashboard/01-dashboard-keuangan-penjualan-dan-pembelian.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Filter Tanggal Dashboard (draf) | Memilih tanggal 1 Januari 2023 hingga 31 Desember 2023; memastikan data lengkap | Menampilkan angka utama, hal yang perlu ditindaklanjuti, grafik, dan ringkasan untuk periode tersebut |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dasbor Persediaan menunjukkan kesehatan stok di seluruh gudang: SKU yang menipis, opname dan transfer yang masih berjalan, nilai persediaan, dan pergerakan stok terbaru. Tujuannya memunculkan masalah yang butuh tindakan tanpa harus membuka tiap daftar |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Dashboard POS, Restoran, Canvassing, Manufaktur, dan Pertambangan

Bab manual: [`dashboard/02-dashboard-operasional.md`](../../erpApiServices/docs/manualBook/dashboard/02-dashboard-operasional.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Memasukkan transaksi penjualan obat Paracetamol 500 mg strip (SKU OBT-001) melalui POS di Apotek Sentosa Bandung | Dashboard POS menampilkan peningkatan omzet, notifikasi kecukupan stok, dan grafik penjualan harian |
| Negatif — input salah (draf) | Menambahkan produk Jamu Kunyit Asam sachet (HRB-001) tanpa data bahan baku di Pabrik Herbal Sukabumi | Sistem menolak input pesan penolakan yang jelas dan tidak memperbarui database produk |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Dashboard HRM, Karyawan, dan Pemakaian AI

Bab manual: [`dashboard/03-dashboard-sdm-notifikasi-dan-lainnya.md`](../../erpApiServices/docs/manualBook/dashboard/03-dashboard-sdm-notifikasi-dan-lainnya.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Karyawan masuk My Dashboard, lakukan check-in dan check-out dengan benar; data akurat | Check-in dan check-out tercatat dengan baik, status hadir terupdate secara real-time |
| Negatif — input salah (draf) | Karyawan melakukan check-in tanpa check-out; syarat tidak terpenuhi | Tidak dapat menutup hari kerja, sistem menolak dan memberikan pesan bahwa check-out diperlukan terlebih dahulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | di luar area: muncul You are outside the attendance area dan absensi ditolak, |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Bila perusahaan mewajibkan foto, klik Take Photo lalu ambil foto sebelum mengirim |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
