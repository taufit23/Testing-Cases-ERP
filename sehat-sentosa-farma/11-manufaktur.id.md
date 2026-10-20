---
title: (PT Sehat Sentosa Farma) — 11. Manufaktur (Pabrik Herbal)
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul manufacturing untuk skenario PT Sehat Sentosa Farma. BOM, rute produksi dan pesanan produksi.
visibility: internal
---

# 11. Manufaktur (Pabrik Herbal)

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Biaya bahan per BOM menjadi HPP barang jadi.
- Pesanan produksi: bahan keluar, hasil masuk; bahan kurang menghalangi penyelesaian bila saklar menyala; toleransi produksi melebihi rencana.
- Persetujuan pesanan produksi bila menyala.

## 1. Konfigurasi Manufaktur & Work Center — Modul Manufacturing

Bab manual: [`manufacturing/01-konfigurasi-manufaktur.md`](../../erpApiServices/docs/manualBook/manufacturing/01-konfigurasi-manufaktur.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi Manufaktur (draf) | Setup awal modul Manufacturing dengan aturan approval dan warehouse default untuk pabrik herbal Sukabumi; pemetaan jurnal biaya produksi untuk SKU OBT-001; Work Center dikonfigurasi dengan benar. | Modul manufacturing berjalan lancar, data konfigurasi tersimpan dengan baik. |
| Negatif — Warehouse Default (draf) | Input warehouse default salah (warehouse tidak ada); pesan kesalahan pesan yang jelas. | Konfigurasi ditolak dengan pesan jelas pesan yang jelas, perbaiki input warehouse. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sebelum mulai membuat Bill of Materials (BOM) atau Production Order, dua hal ini wajib disiapkan dulu: Konfigurasi Manufaktur (aturan approval, warehouse default, pemetaan akun biaya) dan Work Center (lokasi/stasiun kerja tempat proses produksi berlangsung) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Bill of Materials (BOM) — Modul Manufacturing

Bab manual: [`manufacturing/02-bill-of-materials-bom.md`](../../erpApiServices/docs/manualBook/manufacturing/02-bill-of-materials-bom.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat BOM (draf) | Input komposisi bahan baku untuk Jamu Kunyit Asam (HRB-001), termasuk kalsium karbonat dari CV Kapur Medika; cek dan simpan data | BOM HRB-001 terdaftar dengan komponen bahan baku yang benar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bill of Materials (BOM) adalah "resep" produksi — daftar bahan baku (komponen) dan jumlahnya yang dibutuhkan untuk menghasilkan satu produk jadi. Setiap Production Order harus mengacu ke satu BOM |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi tabel Components (bahan baku) — wajib minimal 1 baris: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satu produk tidak bisa dipilih dua kali sebagai komponen dalam BOM yang sama, dan produk jadi yang sedang dibuat resepnya tidak bisa dipilih sebagai komponennya sendiri |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Routing Produksi — Modul Manufacturing

Bab manual: [`manufacturing/03-routing-produksi.md`](../../erpApiServices/docs/manualBook/manufacturing/03-routing-produksi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Routing (draf) | Input: Paracetamol 500 mg strip (SKU OBT-001), work center Pemotongan & Pengemasan, waktu kerja 30 menit | Routing disusun dengan benar dan tersimpan dalam sistem |
| Negatif — Waktu Kerja Tidak Sesuai (draf) | Input: Paracetamol 500 mg strip (SKU OBT-001), work center Pemotongan & Pengemasan, waktu kerja 60 menit | Sistem menolak input pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap operasi di Routing akan disalin ke Production Order sebagai daftar Operations yang harus di-Start dan di-Finish satu per satu selama proses produksi berjalan (lihat chapter Production Order) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Production Order — Modul Manufacturing

Bab manual: [`manufacturing/04-production-order.md`](../../erpApiServices/docs/manualBook/manufacturing/04-production-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Production Order (draf) | Buat PO untuk Jamu Kunyit Asam (HRB-001), approve & release, catat operasi, terima produk ke stok | Proses berjalan lancar, status PO menjadi Complete, stok HRB-001 bertambah |
| Negatif — Input Jumlah Negatif (draf) | Masukkan jumlah negatif untuk keluar bahan baku | Tidak dapat submit, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau order ditolak (Rejected) saat approval, order kembali bisa diedit dan disubmit ulang |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau order memakai Routing, bagian Operations menampilkan daftar tahapan kerja sesuai urutan di Routing. Operasi hanya bisa dicatat saat order berstatus In Progress, dan harus dikerjakan sesuai urutan pending-nya: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Klik Complete Production untuk finalisasi. Syarat: Produced Quantity harus lebih dari 0 |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Production Order hanya bisa dihapus selama masih berstatus Draft atau Cancelled |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
