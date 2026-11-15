---
title: (PT Sehat Sentosa Farma) — 24. Kerjasama (Partnership)
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul kerjasama untuk skenario PT Sehat Sentosa Farma. Tipe, katalog paket, perjanjian berversi, pemakaian dan tagihan mitra.
visibility: internal
---

# 24. Kerjasama (Partnership)

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Penawaran berversi dan perjanjian lewat persetujuan; rantai klien.
- Pemakaian direkap menjadi tagihan; penyelesaian terjurnal.
- Kewajiban dan penyesuaian kerja custom tercatat dan terlaporkan.

## 1. Pengaturan, Tipe Kerjasama, dan Katalog Paket — Modul Kerjasama

Bab manual: [`kerjasama/01-pengaturan-tipe-dan-katalog-paket.md`](../../erpApiServices/docs/manualBook/kerjasama/01-pengaturan-tipe-dan-katalog-paket.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengaturan cabang (draf) | Input data cabang (Kantor Pusat & Distribusi Jakarta) dengan detail benar; Simpan | Cabang berhasil ditambahkan ke modul Kerjasama |
| Negatif — Tipe kerjasama tidak sesuai (draf) | Memilih tipe kerjasama yang tidak ada dalam opsi; Coba kembali dengan pilihan valid | Sistem menolak input dan memberikan pesan error tentang pilihan tipe kerjasama yang salah |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Perjanjian Kerjasama dan Rantai Klien — Modul Kerjasama

Bab manual: [`kerjasama/02-perjanjian-dan-rantai-klien.md`](../../erpApiServices/docs/manualBook/kerjasama/02-perjanjian-dan-rantai-klien.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat perjanjian (draf) | Buat perjanjian dengan Klinik Pratama, termasuk syarat dan pihak terlibat; siklus status otomatis; rantai harga berbasis margin; cetak perjanjian | Perjanjian valid ditandatangani oleh kedua belah pihak, mencantumkan semua detail termasuk margin otomatis |
| Negatif — Input salah (draf) | Masukkan data produk yang tidak ada (SKU palsu) dalam rantai klien; pesan error pesan yang jelas muncul | Sistem menolak perubahan harga dengan pesan kesalahan jelas tentang SKU tidak valid |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 5. Biarkan Fill responsibilities and obligations from the type menyala bila ingin matriks tanggung jawab dan kewajiban awal terisi dari preset tipe |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Draft → Diajukan → Disetujui → Aktif ⇄ Ditangguhkan → Berakhir / Diakhiri, dengan Ditolak dan Dibatalkan sebagai ujung lain |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item yang sudah dipakai rekap atau perjanjian anak tidak bisa dihapus; akhiri saja item itu dengan tanggal berakhir |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu titik tiga di pojok kanan atas detail: Export PDF / Excel menghasilkan dokumen perjanjian (syarat, harga, para pihak, matriks tanggung jawab, kewajiban) dengan pengaturan ekspor dokumen cabang. Dokumen bertanda tangan diunggah di tab History (lampiran) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Penawaran Berversi — Modul Kerjasama

Bab manual: [`kerjasama/03-penawaran-berversi.md`](../../erpApiServices/docs/manualBook/kerjasama/03-penawaran-berversi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menyusun Penawaran Kerjasama (draf) | Membuat penawaran versi V1.0 untuk klinik mitra; menerima konfirmasi draft perjanjian dalam satu klik | Penawaran diterima sebagai draft perjanjian dengan versi V1.0 |
| Negatif — Input Data Salah (draf) | Menginput nama klinik mitra yang tidak ada di sistem; mendapat pesan kesalahan input data | Penawaran ditolak karena data klinik mitra tidak valid, mohon dicek kembali |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Pemakaian, Rekap Periodik, dan Tagihan — Modul Kerjasama

Bab manual: [`kerjasama/04-pemakaian-rekap-dan-tagihan.md`](../../erpApiServices/docs/manualBook/kerjasama/04-pemakaian-rekap-dan-tagihan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat pemakaian (draf) | Input SKU OBT-001, jumlah 50 botol, tanggal 2023-09-15; Verifikasi bersama; Simpan | Pemakaian tercatat dan diverifikasi dengan benar |
| Negatif — Rekap periodik (draf) | Input model nilai yang tidak ada; Coba membuat rekap | Sistem menolak dan memberikan pesan bahwa model nilai harus diperiksa kembali |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Rekap hanya bisa dibuat untuk perjanjian yang Active, yang punya tanggal mulai dan kadens berulang supaya periode berikutnya bisa ditentukan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Membatalkan rekap yang sudah ditagihkan lewat faktur memerlukan pembatalan faktur lebih dulu. Pembatalan juga ditolak selama jurnal rekap masih menunggu persetujuan jurnal |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Kewajiban, Penyesuaian Biaya, Kerja Custom, dan Laporan — Modul Kerjasama

Bab manual: [`kerjasama/05-kewajiban-penyesuaian-kerja-custom-dan-laporan.md`](../../erpApiServices/docs/manualBook/kerjasama/05-kewajiban-penyesuaian-kerja-custom-dan-laporan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Matriks tanggung jawab (draf) | Menentukan kewajiban Apoteker Penanggung Jawab, Kepala Gudang, Kasir, Staf Pembelian, Manajer Keuangan, Direktur | Tampilan matriks dengan kewajiban teridentifikasi dengan benar |
| Negatif — Input syarat tidak terpenuhi (draf) | Menetapkan kewajiban pada staf yang belum ditentukan | Pesan error: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tab Obligations mencatat hal non-uang yang harus terpenuhi, masing-masing dengan penanggung jawab (kita, lawan pihak, atau keduanya), tenggat, status, dan bukti: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Diagram Alur Kerjasama — Modul Kerjasama

Bab manual: [`kerjasama/06-diagram-alur-kerjasama.md`](../../erpApiServices/docs/manualBook/kerjasama/06-diagram-alur-kerjasama.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Sentosa Farma memasukkan penawaran berversi ke Apotek Bandung; status perjanjian diupdate; rekap dan tagihan dibuat secara otomatis | Proses kerjasama berjalan lancar, otomatis mengubah status dan mencetak dokumen sesuai langkah |
| Negatif — input salah (draf) | Sentosa Farma memasukkan penawaran berversi tanpa nomor perjanjian; sistem menolak input pesan penolakan yang jelas | Input ditolak, entitas diberitahu syarat yang belum terpenuhi dan harus diisi kembali |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | OBL["Kewajiban kedua pihak<br/bab 05"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Perjanjian harus punya tanggal mulai sebelum bisa di-Submit |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pengingat kewajiban dan tinjau harga juga dijalankan otomatis |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
