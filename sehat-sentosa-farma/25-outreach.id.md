---
title: (PT Sehat Sentosa Farma) — 25. Sales Outreach
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul outreach untuk skenario PT Sehat Sentosa Farma. Kampanye, audiens, pengiriman, dan penggunaan.
visibility: internal
---

# 25. Sales Outreach

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Pratinjau audiens sebelum jadwal; kampanye terjadwal dikirim lewat gerbang pengiriman.
- Pemakaian outreach tercatat per cabang dan tampil di dashboard.

## 1. Kampanye Sales Outreach — Modul Outreach

Bab manual: [`outreach/01-kampanye-sales-outreach.md`](../../erpApiServices/docs/manualBook/outreach/01-kampanye-sales-outreach.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menyiapkan kampanye sales outreach (draf) | PT Sehat Sentosa Farma menyiapkan pengirim, templat email, daftar prospek dan penolakan, menyusun kampanye, menjadwalkan, dan memantau pesan | Kampanye terkirim dengan baik, statistik dan pemakaian diperiksa secara berkala |
| Negatif — Mengisi data prospek kosong (draf) | PT Sehat Sentosa Farma mencoba mengirim email tanpa mengisi daftar prospek | Tidak dapat menjadwalkan kampanye: masukkan daftar prospek terlebih dahulu, pesan error muncul |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Modul Outreach harus aktif untuk cabang. Bila tidak, kampanye tidak bisa dijadwalkan dan tidak ada email yang dikirim |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kampanye hanya bisa diubah atau dihapus selagi Draft |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Berhenti berlangganan, pental keras, keluhan, dan permintaan subjek data tidak bisa dicabut dari daftar penolakan. Itu pilihan penerima atau sinyal dari penyedia email. Pengguna hanya bisa mencabut alamat yang ditambahkan manual |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Buka Senders, klik "+ Create", lalu isi nama pengirim, alamat pengirim, alamat balasan, dan batas harian. Sender harus aktif supaya kampanye bisa dijadwalkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Diagram Alur Outreach — Modul Outreach

Bab manual: [`outreach/02-diagram-alur-outreach.md`](../../erpApiServices/docs/manualBook/outreach/02-diagram-alur-outreach.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Persiapan: Data valid, email valid, status 'Draft' | Proses berjalan, status berubah menjadi 'Pending' |
| Negatif — input salah (draf) | Email kosong, syarat tidak terpenuhi | Ditolak, pesan: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Draft -- Scheduled: Schedule Campaign, bila siap dan persetujuan tidak diwajibkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Draft -- PendingApproval: Schedule Campaign, bila persetujuan diwajibkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | PendingApproval -- Draft: Ditolak atau diminta revisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Persetujuan kampanye hanya berlaku bila diwajibkan di konfigurasi, dan alur persetujuannya sudah diatur pemilik platform (bab 01) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
