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
| Positif — Membuat kategori biaya dan mencatat expense (draf) | Masuk ke `Finance → Expense Categories`, buat kategori "Listrik & Air"; masuk ke `Finance → Expenses`, buat expense untuk listrik dengan kategori "Listrik & Air" dan jumlah 100.000 Rupiah; pilih metode pembayaran "Transfer Bank". | Kategori "Listrik & Air" terdaftar, expense berstatus Draft; jurnal otomatis dibuat di General Ledger. |
| Negatif — Mencoba menghapus expense yang sudah disetujui (draf) | Cari expense dengan status Approved, klik tiga titik, pilih Delete; cek apakah bisa menghapus. | Tidak dapat menghapus expense yang sudah disetujui, pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Pilih Expense Category (wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi Expense Date (wajib) dan Due Date (opsional, kalau biaya ini punya tenggat pembayaran) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 7. Minimal harus ada 1 item dan setiap item wajib punya deskripsi sebelum bisa disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Expense yang ditolak kembali bisa diperbaiki lalu di-Submit lagi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Pembayaran Online, Rute Penyedia, dan Penyelesaian Dana

Bab manual: [`finance/02-pembayaran-online-dan-penyelesaian.md`](../../erpApiServices/docs/manualBook/finance/02-pembayaran-online-dan-penyelesaian.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah urutan penyedia pembayaran online (draf) | Pilih Midtrans, klik Add; susun urutan Midtrans di atas DOKU, lalu Save. | Penyedia Midtrans muncul di daftar dengan urutan teratas dan status 'Saved'. |
| Negatif — Menggunakan kredensial lengkap tapi tidak valid (draf) | Isi kredensial Midtrans yang salah; coba Add. | Tampilan error 'Kredensial tidak valid' dan tombol Add nonaktif. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sebelum bisa mencatat penyelesaian, akun penampung pembayaran online harus sudah dipetakan di POS → POS Configs; bila belum, halaman menampilkan peringatan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Diagram Alur Finance — Modul Finance

Bab manual: [`finance/03-diagram-alur-finance.md`](../../erpApiServices/docs/manualBook/finance/03-diagram-alur-finance.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pencatatan expense (draf) | Buka menu Expense; Input OBT-001, 250.000, Draft; Approve oleh manajer; Bayar dengan QRIS | Status expense berubah menjadi Paid; Jurnal pembayaran tercatat; Pesan konfirmasi pembayaran muncul |
| Negatif — Pembayaran expense (draf) | Coba bayar OBT-001 yang masih Draft; Tidak bisa, muncul pesan "Expense belum Approved" | Sistem menolak dan memberikan pesan kesalahan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | J --/"Transfer bank"/ L["Mark as Paid ditolak<br/gunakan Prepare dan Release"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Expense hanya bisa diedit dan dihapus selama masih Draft |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | H --/"Kedaluwarsa atau ditolak"/ J["Transaksi Voided<br/stok tidak pernah berkurang"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penyedia yang kredensialnya belum lengkap tidak bisa dipakai. Lengkapi di halaman Integrations |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
