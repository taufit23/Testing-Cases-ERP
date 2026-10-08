---
title: Ranahku — Proyek dan Tugas (Otomasi, Webhook, Portal Klien, Change Request, Tiket, F6)
description: Langkah uji tahap keenam modul Proyek dan Tugas: aturan otomasi, webhook keluar, portal klien, change request, tiket dan SLA.
---

# Ranahku — Proyek dan Tugas (Otomasi, Portal, Tiket, F6)

> Disusun 2026-10-08. **Letak dalam urutan kerja:** setelah berkas `16`. Prasyarat: berkas `12`–`16` selesai; satu proyek berklien; satu endpoint penerima webhook uji (mis. webhook.site, https publik).

## BA1. Aturan otomasi

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BA1.1 | **Proyek → Otomasi** saat saklar mati | Banner "otomasi dimatikan"; aturan tidak berjalan | ⬜ |
| BA1.2 | Aktifkan di Pengaturan Proyek; buat aturan: tugas dibuat -> prioritas urgent + tambah label + komentar | Tugas baru otomatis berprioritas urgent, berlabel, berkomentar sistem; Riwayat mencatat Berhasil | ⬜ |
| BA1.3 | Aturan "pindah ke Done saat komentar ditambah" pada tugas yang punya subtugas terbuka | Riwayat mencatat Dilewati dengan alasan; status tidak berubah | ⬜ |
| BA1.4 | Dua aturan saling memicu dengan batas kedalaman 1 | Aturan kedua tercatat "diblokir batas kedalaman" | ⬜ |
| BA1.5 | Aturan yang mengubah bidang yang sama dengan pemicunya | Berjalan sekali, tidak berulang tanpa henti | ⬜ |
| BA1.6 | Batas 2 run per menit, buat 4 tugas | 2 berhasil, 2 "diblokir batas laju" | ⬜ |
| BA1.7 | Bentuk tidak sah (aksi kosong, nilai prioritas salah) | Ditolak dengan pesan saat disimpan | ⬜ |
| BA1.8 | Matikan lalu hapus aturan | Berhenti berjalan; riwayat ikut terhapus | ⬜ |

## BA2. Webhook keluar

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BA2.1 | **Proyek → Webhook**: tambah dengan URL https dan peristiwa Tugas dibuat | Rahasia tampil sekali | ⬜ |
| BA2.2 | URL `http://`, `localhost`, IP privat, atau berkredensial | Ditolak | ⬜ |
| BA2.3 | Kirim peristiwa uji | Penerima menerima header X-ERP-Event, X-ERP-Delivery, X-ERP-Signature; tanda tangan cocok HMAC-SHA256 badan | ⬜ |
| BA2.4 | Buat tugas | Dalam ±1 menit penerima menerima `task.created` tanpa tarif/biaya | ⬜ |
| BA2.5 | Penerima dibuat gagal (500) | Pengiriman dicoba ulang bertingkat; setelah 5 kali menyerah; webhook nonaktif sesuai batas gagal beruntun | ⬜ |
| BA2.6 | Putar rahasia, kirim ulang pengiriman | Tanda tangan memakai rahasia baru | ⬜ |

## BA3. Change request

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BA3.1 | Detail proyek → Change Request: buat (+20 jam, +500) lalu ajukan | Status Menunggu keputusan; tidak bisa diubah lagi | ⬜ |
| BA3.2 | Setujui internal | Anggaran jam/uang proyek bertambah, kontrak harga tetap ikut; disetujui dua kali ditolak | ⬜ |
| BA3.3 | Mode "keduanya": setujui internal lalu klien lewat portal | Baru disetujui setelah kedua pihak; anggaran bertambah sekali | ⬜ |
| BA3.4 | Tolak tanpa alasan, lalu dengan alasan | Alasan wajib; status Ditolak | ⬜ |
| BA3.5 | Matikan "menambah anggaran" | CR disetujui tanpa mengubah anggaran | ⬜ |

## BA4. Portal klien

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BA4.1 | Aktifkan portal; tandai satu tugas "terlihat klien"; buat tautan portal | Tautan tampil sekali; daftar tidak menampilkan token | ⬜ |
| BA4.2 | Buka tautan tanpa login | Terlihat progres, milestone, tugas yang dibagikan; tidak ada tarif/biaya/anggaran/gaji | ⬜ |
| BA4.3 | Komentar sebagai klien pada tugas terbagi | Muncul di tugas sebagai komentar klien | ⬜ |
| BA4.4 | Setujui milestone yang belum selesai, lalu yang selesai | Hanya yang selesai bisa; tercatat nama penyetuju | ⬜ |
| BA4.5 | Tautan tanpa izin komentar mencoba komentar | Ditolak | ⬜ |
| BA4.6 | Cabut tautan / lewati kedaluwarsa / matikan saklar portal / tutup proyek | Tautan menampilkan "tidak valid" | ⬜ |
| BA4.7 | Tandai tugas terlihat klien oleh bukan manajer proyek | Ditolak | ⬜ |

## BA5. Tiket dan SLA

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BA5.1 | Portal "Laporkan masalah" sebelum ada tipe tiket | Ditolak | ⬜ |
| BA5.2 | Buat tipe tugas "tiket dukungan" dan kebijakan SLA bawaan (urgent 1 jam respons / 4 jam selesai) | Tersimpan; hanya satu kebijakan bawaan | ⬜ |
| BA5.3 | Kirim tiket urgent dari portal | Tugas tiket terbuat, terlihat klien, dengan tenggat respons dan penyelesaian | ⬜ |
| BA5.4 | Kebijakan jam kerja: tiket dibuat Jumat sore | Tenggat melompati akhir pekan dan libur | ⬜ |
| BA5.5 | Komentar klien, lalu komentar staf | Respons pertama tercatat hanya pada komentar staf | ⬜ |
| BA5.6 | Lewati tenggat tanpa respons (tunggu penyapu 15 menit) | Tiket ditandai melanggar SLA sekali; manajer proyek diberi notifikasi | ⬜ |
