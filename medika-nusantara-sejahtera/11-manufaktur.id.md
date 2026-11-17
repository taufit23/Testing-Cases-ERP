---
title: (PT Medika Nusantara Sejahtera) — 11. Manufaktur (Pabrik Herbal)
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul manufacturing untuk skenario PT Medika Nusantara Sejahtera. BOM, rute produksi dan pesanan produksi.
visibility: internal
---

# 11. Manufaktur (Pabrik Herbal)

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji produksi: resep (BOM), perintah produksi, pemakaian bahan, dan hasil jadi.
>
> **Kalau semuanya benar, artinya:** Bahan baku berkurang, barang jadi bertambah, dan biaya produksi tercatat wajar.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Biaya bahan per BOM menjadi HPP barang jadi.
- Pesanan produksi: bahan keluar, hasil masuk; bahan kurang menghalangi penyelesaian bila saklar menyala; toleransi produksi melebihi rencana.
- Persetujuan pesanan produksi bila menyala.

## 1. Konfigurasi Manufaktur & Work Center — Modul Manufacturing

Bab manual: [`manufacturing/01-konfigurasi-manufaktur.md`](../../erpApiServices/docs/manualBook/manufacturing/01-konfigurasi-manufaktur.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi Manufaktur (draf) | Masuk Manufacturing → Config; Aktifkan Production Orders Require Approval Before Release; Simpan | Status Production Order memerlukan persetujuan sebelum dirilis |
| Negatif — Warehouse Default (draf) | Masuk Manufacturing → Config; Tidak mengisi Warehouse Default; Coba simpan | Muncul pesan penolakan yang jelas dan tidak bisa disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sebelum mulai membuat Bill of Materials (BOM) atau Production Order, dua hal ini wajib disiapkan dulu: Konfigurasi Manufaktur (aturan approval, warehouse default, pemetaan akun biaya) dan Work Center (lokasi/stasiun kerja tempat proses produksi berlangsung) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau toleransi reject diisi dan ada reject di atasnya, akun untuk fungsi Production Loss harus sudah dipetakan di bagian pemetaan akun. Kalau belum, Complete ditolak dengan pesan untuk memetakan akunnya dulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Bill of Materials (BOM) — Modul Manufacturing

Bab manual: [`manufacturing/02-bill-of-materials-bom.md`](../../erpApiServices/docs/manualBook/manufacturing/02-bill-of-materials-bom.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat BOM untuk jamu kunyit asam (draf) | Klik "+ Create Bill of Materials"; Isi Name: Jamu Kunyit Asam; Pilih SKU Produk Jadi HRB-001; Masukkan Output Quantity 500; Tambahkan Component: Bahan baku kunyit (SKU-001) x 200 gram, bahan baku asam jawa (SKU-002) x 100 gram; Aktifkan Default for this Product | BOM Jamu Kunyit Asam berhasil dibuat dengan default produk utama HRB-001 dan komponen yang sesuai |
| Negatif — Menambahkan produk jadi sebagai component (draf) | Tambahkan SKU Produk Jadi HRB-001 ke dalam tabel Components; Coba simpan BOM | Muncul pesan kesalahan pesan yang jelas dan input tidak disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bill of Materials (BOM) adalah "resep" produksi — daftar bahan baku (komponen) dan jumlahnya yang dibutuhkan untuk menghasilkan satu produk jadi. Setiap Production Order harus mengacu ke satu BOM |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi tabel Components (bahan baku) — wajib minimal 1 baris: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satu produk tidak bisa dipilih dua kali sebagai komponen dalam BOM yang sama, dan produk jadi yang sedang dibuat resepnya tidak bisa dipilih sebagai komponennya sendiri |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Routing Produksi — Modul Manufacturing

Bab manual: [`manufacturing/03-routing-produksi.md`](../../erpApiServices/docs/manualBook/manufacturing/03-routing-produksi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Klik "+ Buat Rute"; Isi Name: "Pemotongan Rakit Kemas", Bill of Materials: Paracetamol 500 mg strip (SKU OBT-001), Operations: 3 baris dengan Operation: Pemotongan, Work Center: Gudang Jakarta, Setup Minutes: 10, Run Minutes per Unit: 20; Klik Save Routing | Routing pesan yang jelas berhasil disimpan dengan total Run Minutes per Unit 60 |
| Negatif — input salah (draf) | Isi Name kosong saat membuat routing; Isi Bill of Materials tidak sesuai BOM yang ada | Tampilan error: pesan yang jelas dan pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap operasi di Routing akan disalin ke Production Order sebagai daftar Operations yang harus di-Start dan di-Finish satu per satu selama proses produksi berjalan (lihat chapter Production Order) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Production Order — Modul Manufacturing

Bab manual: [`manufacturing/04-production-order.md`](../../erpApiServices/docs/manualBook/manufacturing/04-production-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Klik "+ Buat Produksi"; pilih BOM Paracetamol 500 mg strip (SKU OBT-001), masukkan Planned Quantity 100, Material Warehouse Gudang Jakarta, dan Finished Goods Warehouse Gudang Jakarta; klik Save Production Order | Daftar Materials menunjukkan kebutuhan bahan baku 5000 mg Paracetamol; Operations kosong karena tidak menggunakan Routing; status menjadi Draft |
| Negatif — input salah (draf) | Membuat Production Order tanpa mengisi field Bill of Materials; coba klik Save Production Order | Sistem pesan penolakan yang jelas dan tidak menyimpan order; status tetap Draft |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau order ditolak (Rejected) saat approval, order kembali bisa diedit dan disubmit ulang |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau order memakai Routing, bagian Operations menampilkan daftar tahapan kerja sesuai urutan di Routing. Operasi hanya bisa dicatat saat order berstatus In Progress, dan harus dikerjakan sesuai urutan pending-nya: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Klik Complete Production untuk finalisasi. Syarat: Produced Quantity harus lebih dari 0 |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Order harus berstatus In Progress dan semua operasi Routing sudah selesai |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Diagram Alur Manufaktur — Modul Manufacturing

Bab manual: [`manufacturing/05-diagram-alur-manufaktur.md`](../../erpApiServices/docs/manualBook/manufacturing/05-diagram-alur-manufaktur.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Resep diterbitkan menjadi Production Order (draf) | 1. Masuk ke menu "Resep" <br>2. Pilih resep Paracetamol 500 mg strip (SKU OBT-001) <br>3. Klik tombol "Terbitkan PO" <br>4. Input jumlah produksi 1000 unit | Production Order OBT-001 diterbitkan dengan status Draft, bahan baku diubah ke stok tersedia dan jurnal pengeluaran bahan dibuat |
| Negatif — Coba menghapus Production Order yang sudah Released (draf) | 1. Masuk ke menu "Production Order" <br>2. Pilih PO OBT-001 status Released <br>3. Klik tombol "Hapus" <br>4. Input alasan penghapusan | Tampilan pesan penolakan yang jelas, Production Order tetap berstatus Released |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bahan hanya bisa dikeluarkan atau dikembalikan saat order berstatus Released atau In Progress |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Operasi hanya bisa dicatat saat order In Progress |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Cancel ditolak bila masih ada bahan yang dikeluarkan dan belum dikembalikan. Kembalikan bahan dulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
