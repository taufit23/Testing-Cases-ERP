---
title: Ranahku — Proyek dan Tugas (Laporan, Dasbor, LogBook, Asisten AI, F7)
description: Langkah uji tahap ketujuh modul Proyek dan Tugas: laporan dan ekspor, dasbor, jembatan LogBook, dan asisten AI yang hanya memberi saran.
---

# Ranahku — Proyek dan Tugas (Laporan, LogBook, AI, F7)

> Disusun 2026-10-10. **Letak dalam urutan kerja:** setelah berkas `17`. Prasyarat: berkas `12`–`17` selesai; beberapa tugas selesai (sebagian tepat waktu, sebagian terlambat), entri waktu disetujui, dan satu penyedia AI terkonfigurasi di Integrasi bila menguji bagian AI.

## BL1. Laporan dan dasbor

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BL1.1 | **Proyek → Laporan Proyek**, laporan Ketepatan Waktu dengan rentang tanggal | Per karyawan: selesai, tepat waktu, terlambat, persen tepat waktu, rata-rata hari terlambat; cocok dengan hitungan manual | ⬜ |
| BL1.2 | Laporan Throughput | Tugas selesai per minggu | ⬜ |
| BL1.3 | Laporan Usia Tugas Terbuka | Per proyek: kelompok umur dan jumlah terlambat | ⬜ |
| BL1.4 | Laporan Anggaran vs Aktual | Jam, burn, progres; kolom biaya/tagihan/margin hanya terlihat bagi pemegang izin melihat tarif | ⬜ |
| BL1.5 | Laporan SLA Tiket | Tiket, direspons, melanggar, persen pelanggaran | ⬜ |
| BL1.6 | Saring per proyek; pakai pengguna yang bukan anggota proyek lain | Hanya proyek yang boleh dilihat pengguna yang masuk laporan | ⬜ |
| BL1.7 | Ekspor PDF dan Excel | Berkas terunduh; judul dan header kolom sesuai bahasa; kop sesuai pengaturan dokumen cabang | ⬜ |
| BL1.8 | **Dasbor Proyek** | Tugas terbuka dan terlambat milik sendiri, proyek berisiko (burn jam melebihi progres 20 poin), tiket melanggar SLA | ⬜ |

## BL2. Jembatan LogBook

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BL2.1 | Saklar mati: catat dan setujui waktu | Tidak ada entri LogBook | ⬜ |
| BL2.2 | Aktifkan "entri waktu disetujui ditulis ke LogBook"; catat waktu | Satu kegiatan bertipe "Tugas" untuk karyawan itu (judul memuat nomor tugas, jam di deskripsi) | ⬜ |
| BL2.3 | Setujui ulang / buka kembali dan setujui | Tidak ada kegiatan ganda | ⬜ |
| BL2.4 | Aktifkan PR ke LogBook; merge PR dari karyawan terpetakan | Satu kegiatan bertipe "Kode" | ⬜ |
| BL2.5 | Buka LogBook karyawan | Kegiatan muncul tanpa skor otomatis; review/skor tetap manual | ⬜ |

## BL3. Asisten AI

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BL3.1 | Saklar AI proyek mati, tekan "Usulkan tugas" | Ditolak dengan pesan saklar mati | ⬜ |
| BL3.2 | Aktifkan saklar tetapi pengungkapan AI cabang belum dikonfirmasi | Ditolak dengan pesan pengungkapan | ⬜ |
| BL3.3 | Semua siap; di detail proyek tulis deskripsi pekerjaan, "Usulkan tugas" | Daftar usulan tugas/subtugas dengan estimasi jam; BELUM ada tugas yang dibuat | ⬜ |
| BL3.4 | Centang sebagian, "Buat tugas yang dicentang" | Hanya yang dicentang dibuat (subtugas di bawah induknya) lewat pemeriksaan biasa | ⬜ |
| BL3.5 | Di detail tugas, "Ringkas komentar" | Ringkasan komentar tim/klien; komentar sistem tidak ikut | ⬜ |
| BL3.6 | "Susun draf status mingguan" | Draf narasi; angka di draf sama dengan fakta yang ditampilkan di bawahnya; tanpa data uang | ⬜ |
| BL3.7 | Pengguna tanpa akses ke proyek/tugas tertutup mencoba fitur AI untuknya | Ditolak (403) | ⬜ |
