---
title: (PT Medika Nusantara Sejahtera) — 25. Sales Outreach
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul outreach untuk skenario PT Medika Nusantara Sejahtera. Kampanye, audiens, pengiriman, dan penggunaan.
visibility: internal
---

# 25. Sales Outreach

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji outreach: kampanye email ke calon pelanggan, jadwal kirim, dan balasan.
>
> **Kalau semuanya benar, artinya:** Email terkirim sesuai jadwal dan batas harian, yang berhenti berlangganan tidak dikirimi lagi.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Pratinjau audiens sebelum jadwal; kampanye terjadwal dikirim lewat gerbang pengiriman.
- Pemakaian outreach tercatat per cabang dan tampil di dashboard.

## 1. Kampanye Sales Outreach — Modul Outreach

Bab manual: [`outreach/01-kampanye-sales-outreach.md`](../../erpApiServices/docs/manualBook/outreach/01-kampanye-sales-outreach.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menyiapkan konfigurasi pengirim (draf) | Buka Sales Outreach Settings; klik "+ Create" pada sender; isi nama "PT Medika Nusantara Sejahtera"; alamat pengirim "info@sehatsentosafarma.com"; alamat balasan "support@sehatsentosafarma.com"; batas harian 50 email | Sender PT Medika Nusantara Sejahtera ditambahkan dan status menjadi aktif |
| Negatif — Menyiapkan konfigurasi pengirim tanpa persetujuan (draf) | Buka Sales Outreach Settings; klik "+ Create" pada sender; isi nama "PT Medika Nusantara Sejahtera"; alamat pengirim "info@sehatsentosafarma.com"; alamat balasan "support@sehatsentosafarma.com"; batas harian 50 email tanpa centang persetujuan kampanye | Tampilan pesan kesalahan meminta konfirmasi persetujuan sebelum pengiriman email |
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
| Positif — Kampanye baru dimulai (draf) | Persiapan data; klik "Schedule" pada kampanye Draft | Status berubah menjadi Running, email pertama dikirim sesuai jadwal |
| Negatif — Email gagal pemeriksaan (draf) | Masukkan data yang tidak memenuhi syarat; klik "Send Now" | Tampilan pesan error menginformasikan alasan penolakan dan status tetap Draft |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Draft -- Scheduled: Schedule Campaign, bila siap dan persetujuan tidak diwajibkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Draft -- PendingApproval: Schedule Campaign, bila persetujuan diwajibkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | PendingApproval -- Draft: Ditolak atau diminta revisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Persetujuan kampanye hanya berlaku bila diwajibkan di konfigurasi, dan alur persetujuannya sudah diatur pemilik platform (bab 01) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
