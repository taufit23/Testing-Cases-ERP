---
title: (PT Sehat Sentosa Farma) — 18. Dasbor
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul dashboard untuk skenario PT Sehat Sentosa Farma. Angka ringkasan per peran.
visibility: internal
---

# 18. Dasbor

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** Siapa saja yang punya izin dasbor. Angka dasbor baru bermakna **setelah** ada transaksi di modul terkait.

**Cabang aktif:** Cabang tempat transaksinya dibuat.

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- Angka dasbor sama dengan laporan sumbernya; dasbor hanya menampilkan data cabang aktif atau gabungan sesuai peran.

## 1. Dashboard Akuntansi, Penjualan, Pembelian, dan Inventori

Bab manual: [`dashboard/01-dashboard-keuangan-penjualan-dan-pembelian.md`](../../erpApiServices/docs/manualBook/dashboard/01-dashboard-keuangan-penjualan-dan-pembelian.md)

**Input di:** `Dashboard → Accounting Dashboard` (`/dashboard/accounting`) · `Dashboard → Sales Dashboard` (`/dashboard/sales`) · `Dashboard → Purchasing Dashboard` (`/dashboard/purchasing`) · `Dashboard → Inventory Dashboard` (`/dashboard/inventory`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Accounting Dashboard (draf) | Memilih periode Januari 2023; melihat angka utama laba/rugi; meninjau yang perlu ditindaklanjuti; memeriksa grafik dan ringkasan | Menampilkan laporan akuntansi dengan data yang valid dan lengkap |
| Negatif — Purchasing Dashboard (draf) | Memasukkan periode yang tidak tersedia; mencoba membuat dokumen tanpa mengisi data pemasok | Ditolak pesan penolakan yang jelas atau pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dasbor Persediaan menunjukkan kesehatan stok di seluruh gudang: SKU yang menipis, opname dan transfer yang masih berjalan, nilai persediaan, dan pergerakan stok terbaru. Tujuannya memunculkan masalah yang butuh tindakan tanpa harus membuka tiap daftar |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Dashboard POS, Restoran, Canvassing, Manufaktur, dan Pertambangan

Bab manual: [`dashboard/02-dashboard-operasional.md`](../../erpApiServices/docs/manualBook/dashboard/02-dashboard-operasional.md)

**Input di:** `Dashboard → Pos Dashboard` (`/dashboard/pos`) · `Dashboard → Restaurant Dashboard` (`/dashboard/restaurant`) · `Dashboard → Canvassing Dashboard` (`/dashboard/canvassing`) · `Dashboard → Manufacturing Dashboard` (`/dashboard/manufacturing`) · `Dashboard → Mining Dashboard` (`/dashboard/mining`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Input transaksi obat Paracetamol 500 mg strip (SKU OBT-001) ke POS Dashboard; cek laporan penjualan | Menampilkan laporan penjualan obat dengan detail SKU, jumlah terjual, total pendapatan |
| Negatif — input salah (draf) | Input harga jual obat di bawah harga beli ke POS Dashboard | Ditolak pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Dashboard HRM, Karyawan, dan Pemakaian AI

Bab manual: [`dashboard/03-dashboard-sdm-notifikasi-dan-lainnya.md`](../../erpApiServices/docs/manualBook/dashboard/03-dashboard-sdm-notifikasi-dan-lainnya.md)

**Input di:** `Dashboard → Hrm Dashboard` (`/dashboard/hrm`) · `Dashboard → My Dashboard` (`/dashboard/employee`) · `Dashboard → Ai Usage` (`/dashboard/ai-usage`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Klik Hrm Dashboard, masukkan NPWP PKP, tampilkan angka utama | Menampilkan angka utama HRM sesuai NPWP PKP |
| Negatif — input salah (draf) | Masukkan NPWP non-PKP, coba tampilkan angka utama | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | di luar area: muncul You are outside the attendance area dan absensi ditolak, |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Bila perusahaan mewajibkan foto, klik Take Photo lalu ambil foto sebelum mengirim |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
