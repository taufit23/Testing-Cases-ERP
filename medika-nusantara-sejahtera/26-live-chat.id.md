---
title: (PT Medika Nusantara Sejahtera) — 26. Live Chat
category: medika-nusantara-sejahtera
description: Kasus uji Live Chat antar karyawan dan saluran dukungan ke pemilik aplikasi, ditulis dengan bahasa sederhana dan alasan tiap langkah.
visibility: internal
---

# 26. Live Chat

> **Kenapa bagian ini diuji (bahasa sederhana).** Karyawan bisa saling berkirim pesan di dalam aplikasi tanpa pindah ke WhatsApp, dan bisa
> menyisipkan data ERP (mis. nomor PO atau faktur) sebagai kartu yang bisa diklik. Fitur ini berbayar dan dikunci per paket, jadi kita periksa juga
> bahwa orang yang tidak berhak tidak bisa mengintip.
>
> **Kalau semuanya benar, artinya:** percakapan lancar, kartu data hanya menampilkan yang boleh dilihat pembacanya, dan pesan tidak hilang diam-diam.

**Dikerjakan oleh:** dua karyawan berbeda (buka dua jendela browser: satu biasa, satu mode penyamaran). **Prasyarat:** paket Enterprise (fitur `live_chat`),
modul Chat aktif, dan saklar chat cabang menyala di `Chat → Konfigurasi` (`/chat/configs`).

| # | Langkah | Kenapa kamu melakukan ini | Hasil yang diharapkan |
| ---: | --- | --- | --- |
| 1 | Nyalakan chat di halaman Konfigurasi Chat, simpan | Chat sengaja mati bawaan; ini memastikan saklarnya benar-benar mengontrol fitur | Menu Chat muncul di sidebar untuk karyawan cabang itu |
| 2 | Login sebagai Karyawan A, buka `Chat`, mulai percakapan langsung dengan Karyawan B, kirim "Halo" | Ini jalur paling dasar; kalau gagal, sisanya tidak berarti | Pesan muncul di jendela Karyawan B dalam beberapa detik, tanpa perlu muat ulang |
| 3 | Karyawan B membalas, lalu A melihat lencana angka belum dibaca hilang setelah membukanya | Memastikan penanda "belum dibaca" jujur | Lencana turun ke 0 setelah dibaca |
| 4 | Buat grup tiga orang, kirim pesan, keluarkan satu orang | Grup dipakai tim; yang keluar tidak boleh lagi menerima pesan baru | Yang keluar tetap bisa melihat riwayat lama, tetapi tidak menerima pesan baru |
| 5 | Kirim satu berkas gambar kecil (di bawah 2 MB) | Uji lampiran yang paling ringan dulu | Berkas terkirim dan bisa dibuka lawan bicara |
| 6 | Kirim berkas **lebih dari 2 MB** (mis. 5 MB) | Server saat ini membatasi unggahan PHP ke 2 MB; kita ingin tahu apakah pesan penolakannya jelas | Jika batas belum dinaikkan: ditolak. Catat sebagai temuan, jangan dianggap salah pengguna |
| 7 | Kirim pesan suara singkat | Memastikan perekaman suara di browser berfungsi | Pesan suara bisa diputar lawan bicara |
| 8 | Sisipkan kartu data ERP (mis. satu Purchase Order) ke pesan | Inilah pembeda chat ini dari chat biasa | Kartu tampil dengan nomor dan judul, bisa diklik, dan hanya terbuka bila pembaca punya izin atas PO itu |
| 9 | Login sebagai karyawan **tanpa izin** melihat PO itu, buka pesan berkartu tadi | Kartu tidak boleh membocorkan data | Kartu tampil terkunci atau tanpa isi, bukan menampilkan data PO |
| 10 | Edit pesan sendiri dalam batas waktu, lalu coba edit setelah batas lewat | Aturan edit dan tarik pesan diatur klien | Dalam batas: berhasil. Lewat batas: ditolak dengan pesan jelas. Nilai 0 menit berarti tidak boleh edit |
| 11 | Pada Konfigurasi Chat, pilih kebijakan "karyawan boleh menghapus permanen", lalu hapus satu pesan sendiri | Menyimpan atau menghapus riwayat adalah keputusan bisnis klien | Pesan hilang untuk semua peserta. Perhatikan peringatan di layar bahwa akses darurat tidak bisa membacanya lagi |
| 12 | Kembalikan kebijakan ke "simpan untuk penyelidikan", hapus pesan lagi | Bandingkan dua kebijakan | Pesan hanya hilang dari tampilanmu sendiri; peserta lain masih melihatnya |
| 13 | Lihat status aktif kolega di pemilih orang (hijau = aktif, atau waktu terakhir dilihat) | Berguna sebelum menghubungi seseorang | Status tampil untuk semua kolega satu perusahaan, tidak pernah lintas perusahaan |
| 14 | Login sebagai karyawan yang diberi izin **menghubungi pemilik aplikasi**, buka tab Dukungan, buat utas "Bug prioritas" | Jalur resmi melapor masalah ke pemilik aplikasi | Utas terbuat; konteks halaman dan versi aplikasi terlampir otomatis |
| 15 | Login sebagai staf pemilik aplikasi, buka Kotak Masuk Dukungan, ambil utas lalu balas | Sisi pemilik aplikasi harus rapi | Balasan muncul di sisi karyawan; ringkasan di kepala kotak masuk bertambah |
| 16 | Login sebagai **admin klien** biasa, coba cari utas dukungan tadi | Utas dukungan hanya untuk pemohon dan pemilik aplikasi | Admin klien **tidak** melihatnya |
| 17 | Login sebagai karyawan tanpa izin menghubungi pemilik aplikasi, buka halaman Chat | Orang tanpa hak tidak boleh punya jalur ini | Tab atau tombol Dukungan nonaktif dengan tooltip alasan |
| 18 | Matikan saklar chat cabang, lalu coba buka `Chat` | Memastikan mematikan saklar benar-benar menutup fitur | Chat tidak bisa dipakai dan tidak ada koneksi real-time yang tersisa |

**Netralisasi:** nyalakan kembali saklar chat bila file lain membutuhkannya; hapus percakapan uji bukan kewajiban (pesan disimpan selamanya menurut kebijakan bawaan).
