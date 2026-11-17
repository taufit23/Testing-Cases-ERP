---
title: (PT Medika Nusantara Sejahtera) — 18. Dasbor
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul dashboard untuk skenario PT Medika Nusantara Sejahtera. Angka ringkasan per peran.
visibility: internal
---

# 18. Dasbor

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji dasbor: ringkasan angka penting per modul.
>
> **Kalau semuanya benar, artinya:** Angka di dasbor sama dengan angka di laporan dan transaksinya, dan tiap orang hanya melihat bagiannya.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Angka dasbor sama dengan laporan sumbernya; dasbor hanya menampilkan data cabang aktif atau gabungan sesuai peran.

## 1. Dashboard Akuntansi, Penjualan, Pembelian, dan Inventori

Bab manual: [`dashboard/01-dashboard-keuangan-penjualan-dan-pembelian.md`](../../erpApiServices/docs/manualBook/dashboard/01-dashboard-keuangan-penjualan-dan-pembelian.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Filter Tanggal Dashboard (draf) | Pilih periode "Bulan Lalu" pada dashboard akuntansi; klik tombol "Bulan Lalu" | Header menampilkan periode akuntansi "Bulan Lalu", laba rugi, saldo kas dan bank, piutang, utang, dan jurnal yang masih menunggu diposting atau disetujui untuk periode tersebut |
| Negatif — Filter Tanggal Dashboard (draf) | Masukkan tanggal masa depan pada filter; klik tombol "Terapikan" | Sistem memotong ke hari ini, tidak menampilkan data untuk tanggal masa depan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dasbor Persediaan menunjukkan kesehatan stok di seluruh gudang: SKU yang menipis, opname dan transfer yang masih berjalan, nilai persediaan, dan pergerakan stok terbaru. Tujuannya memunculkan masalah yang butuh tindakan tanpa harus membuka tiap daftar |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Dashboard POS, Restoran, Canvassing, Manufaktur, dan Pertambangan

Bab manual: [`dashboard/02-dashboard-operasional.md`](../../erpApiServices/docs/manualBook/dashboard/02-dashboard-operasional.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Dashboard POS (draf) | Buka `/dashboard/pos`, lihat `Penjualan Hari Ini` 500.000, `Sesi Tunai Terbuka` 2, `Produk Terlaris 7 Hari Terakhir` Paracetamol 500 mg strip 300 unit | Menampilkan ringkasan kinerja POS hari ini dengan data yang sesuai |
| Negatif — Dashboard Canvassing (draf) | Buka `/dashboard/canvassing`, masukkan geofence tidak valid, `Kepatuhan Geofencing` 60% | Muncul pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Dashboard HRM, Karyawan, dan Pemakaian AI

Bab manual: [`dashboard/03-dashboard-sdm-notifikasi-dan-lainnya.md`](../../erpApiServices/docs/manualBook/dashboard/03-dashboard-sdm-notifikasi-dan-lainnya.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Hrm Dashboard (draf) | Buka `/dashboard/hrm`, lihat angka utama, klik `Buka Rekap Absensi` | Muncul halaman rekap absensi dengan tombol untuk menghitung rekap absensi |
| Negatif — Hrm Dashboard (draf) | Tidak login sebagai HR, coba buka `/dashboard/hrm` | Muncul pesan penolakan yang jelas |
| Positif — My Dashboard (draf) | Login sebagai karyawan, buka `/dashboard/employee`, klik `Masuk` saat bekerja, `Lakukan Pengecekan` selesai | Status hari ini berubah menjadi "Sudah Cek-In" dan "Sudah Keluar", slip gaji terbaru muncul |
| Negatif — My Dashboard (draf) | Login sebagai karyawan, coba klik `Masuk` tanpa absen | Muncul pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | di luar area: muncul You are outside the attendance area dan absensi ditolak, |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Bila perusahaan mewajibkan foto, klik Take Photo lalu ambil foto sebelum mengirim |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
