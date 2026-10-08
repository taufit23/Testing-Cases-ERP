---
title: Ranahku — Proyek dan Tugas (Tampilan Tugas dan Ruang Kerja Proyek)
description: Langkah uji pengalih tampilan, ruang kerja proyek, papan kanban, linimasa, daftar berkelompok, kalender, dan entri sidebar Tugas Saya.
---

# Ranahku — Proyek dan Tugas (Tampilan dan Ruang Kerja)

> Disusun 2026-10-08. **Letak dalam urutan kerja:** setelah berkas `19`. Prasyarat: berkas `12`–`14` selesai; `permission:sync --all` sudah dijalankan (rute menu Papan) dan role pengguna uji mendapat izinnya; dua proyek dengan 15 tugas atau lebih (berbagai status, penanggung jawab, prioritas, tenggat termasuk yang lewat), beberapa tugas bertanggal mulai dan tenggat, beberapa dependensi (rantai A → B → C), satu sprint, dan satu milestone.

## TV1. Pengalih tampilan dan menu

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| TV1.1 | Buka sidebar sebagai pengguna dengan izin modul proyek | Ada entri Tugas Saya dan Papan; Tugas Saya muncul juga untuk pengguna yang tidak diberi izin khusus | ⬜ |
| TV1.2 | Buka halaman Tugas | Pengalih tampilan: Daftar, Tabel, Papan, Linimasa, Kalender, Beban Kerja; Tabel aktif | ⬜ |
| TV1.3 | Pindah antar tampilan lewat pengalih | Berpindah halaman tanpa galat; tampilan aktif ditandai | ⬜ |
| TV1.4 | Pengguna tanpa izin salah satu tampilan | Tombol tampilan itu tetap ada tetapi nonaktif dengan penjelasan | ⬜ |
| TV1.5 | Tekan tombol segarkan di tiap halaman tampilan | Data dimuat ulang; indikator pemuatan tampil lalu hilang | ⬜ |

## TV2. Ruang kerja proyek

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| TV2.1 | Buka detail proyek | Tab Ringkasan, Daftar, Papan, Linimasa, Kalender; Ringkasan menampilkan formulir seperti biasa | ⬜ |
| TV2.2 | Buka tab Papan | Hanya tugas proyek ini; filter proyek tidak ditampilkan | ⬜ |
| TV2.3 | Muat ulang halaman saat berada di tab Linimasa | Tab yang sama terbuka lagi (diingat di alamat `?tab=`) | ⬜ |
| TV2.4 | Kembali ke Ringkasan setelah mengisi sebagian formulir lalu berpindah tab | Isian formulir tidak hilang | ⬜ |
| TV2.5 | Buat proyek baru | Tab tidak tampil (hanya formulir) sampai proyek tersimpan | ⬜ |
| TV2.6 | Tambah tugas cepat dari tab Papan/Daftar | Tugas dibuat di proyek ini tanpa memilih proyek | ⬜ |

## TV3. Papan (kanban)

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| TV3.1 | Buka Papan | Satu kolom per status alur kerja; kartu menampilkan nomor, judul, ikon prioritas, label, progres, subtugas, poin, tenggat berwarna (lewat = merah, hari ini/segera = kuning), avatar penanggung jawab | ⬜ |
| TV3.2 | Seret kartu ke kolom lain yang diizinkan | Pindah; riwayat status mencatat | ⬜ |
| TV3.3 | Seret ke status yang ditolak gerbang (mis. Selesai dengan subtugas terbuka) | Kartu kembali; alasan ditampilkan | ⬜ |
| TV3.4 | Seret ke kolom Diblokir | Diminta alasan; tanpa alasan tidak bisa dikonfirmasi | ⬜ |
| TV3.5 | Seret kartu yang memicu peringatan dependensi | Muncul konfirmasi; setelah dikonfirmasi kartu pindah | ⬜ |
| TV3.6 | Pilih jalur: per penanggung jawab, per prioritas, per proyek | Kartu terkelompok per jalur; jalur bisa dilipat; jumlah per jalur benar; tanpa jalur kembali normal | ⬜ |
| TV3.7 | Atur batas WIP 2 pada satu status (Proyek → Alur Kerja → ubah status), lalu tambahkan 3 tugas ke kolom itu | Header kolom "3 / 2" merah dengan penjelasan; kolom berwarna peringatan; tetap bisa memindahkan (batas hanya penanda) | ⬜ |
| TV3.8 | Kosongkan batas WIP | Penanda hilang | ⬜ |
| TV3.9 | Lipat satu kolom, muat ulang halaman | Kolom tetap terlipat (diingat di peramban); klik untuk membuka lagi | ⬜ |
| TV3.10 | "Tambah tugas" di satu kolom (proyek dipilih), ketik judul, Enter | Tugas dibuat dan muncul di kolom itu; bila gerbang menolak, tugas tetap di kolom awal dengan pesan | ⬜ |
| TV3.11 | "Tambah tugas" tanpa proyek dipilih di Papan semua proyek | Tombol nonaktif dengan penjelasan memilih proyek | ⬜ |
| TV3.12 | Filter: proyek, penanggung jawab, prioritas, pencarian, hanya tugas saya, sembunyikan kolom selesai | Hasil sesuai; kombinasi bekerja | ⬜ |
| TV3.13 | Tampilan tersimpan Papan (simpan filter, pilih ulang, jadikan bawaan) | Filter terterapkan | ⬜ |
| TV3.14 | Papan dengan 200+ tugas | Tetap bisa digulir dan diseret tanpa lag berarti | ⬜ |

## TV4. Linimasa (Gantt)

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| TV4.1 | Buka Linimasa | Daftar tugas di kiri; batang di kanan; garis merah hari ini; bayangan akhir pekan pada zoom hari; milestone sebagai berlian | ⬜ |
| TV4.2 | Ganti zoom Hari / Minggu / Bulan | Skala header menyesuaikan, batang proporsional, rentang tanggal lebih panjang pada zoom besar | ⬜ |
| TV4.3 | Tombol sebelumnya / hari ini / berikutnya dan ubah tanggal mulai | Rentang bergeser; data dimuat ulang | ⬜ |
| TV4.4 | Tugas dengan dependensi A → B → C | Panah dari batang pendahulu ke penerus; badge jumlah dependensi di daftar kiri | ⬜ |
| TV4.5 | Nyalakan "Sorot jalur kritis" pada proyek dengan rantai dependensi | Rantai terpanjang diberi cincin merah dengan panah merah; matikan: penanda hilang | ⬜ |
| TV4.6 | Dependensi bertipe SS/FF/SF | Panah berpangkal/berujung di sisi yang sesuai | ⬜ |
| TV4.7 | Geser sebuah batang | Tanggal mulai dan tenggat bergeser sama banyak setelah dilepas; tersimpan | ⬜ |
| TV4.8 | Tarik tepi kanan batang | Hanya tenggat berubah; tidak boleh mendahului tanggal mulai | ⬜ |
| TV4.9 | Geser batang yang memicu aturan (tugas terkunci, penerus dengan penjadwalan ulang otomatis) | Aturan berlaku; galat ditampilkan bila ditolak; tampilan dimuat ulang | ⬜ |
| TV4.10 | Pengguna tanpa izin ubah tugas | Batang tidak bisa digeser (kursor biasa) | ⬜ |
| TV4.11 | Kelompokkan per proyek / penanggung jawab / status; lipat satu kelompok | Baris kelompok dengan jumlah; baris tugas sejajar antara daftar kiri dan batang kanan | ⬜ |
| TV4.12 | Gulir horizontal pada rentang panjang | Daftar kiri tetap; header skala ikut menggulir sejajar batang | ⬜ |

## TV5. Daftar berkelompok

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| TV5.1 | Tugas → pengalih "Daftar" | Bagian per status (urut alur kerja) dengan jumlah, bisa dilipat | ⬜ |
| TV5.2 | Kelompokkan per penanggung jawab, prioritas, proyek, tanpa kelompok | Bagian sesuai; tanpa penanggung jawab = "Belum ditugaskan" | ⬜ |
| TV5.3 | Ubah status langsung di baris | Berpindah bagian setelah muat ulang; gerbang menolak = pesan dan nilai kembali | ⬜ |
| TV5.4 | Ubah penanggung jawab, prioritas, dan tenggat di baris | Tersimpan; tenggat lewat berwarna merah | ⬜ |
| TV5.5 | Pemilih kolom: sembunyikan Progres, tampilkan Poin dan Proyek; muat ulang halaman | Pilihan kolom diingat | ⬜ |
| TV5.6 | Centang beberapa baris (termasuk centang header bagian) | Tombol Bulk Actions aktif dengan jumlah terpilih | ⬜ |
| TV5.7 | Bulk Actions → set prioritas Tinggi | Konfirmasi lalu semua terpilih berubah | ⬜ |
| TV5.8 | Bulk Actions → hapus terpilih | Konfirmasi; tugas terhapus (aturan penghapusan tetap berlaku) | ⬜ |
| TV5.9 | Tambah tugas cepat pada bagian status tertentu | Tugas dibuat lalu dipindah ke status bagian itu bila diizinkan | ⬜ |
| TV5.10 | Tambah tugas cepat pada bagian penanggung jawab/prioritas | Tugas membawa penanggung jawab/prioritas bagian itu | ⬜ |
| TV5.11 | Sembunyikan tugas selesai | Tugas berstatus selesai/dibatalkan hilang dari daftar | ⬜ |
| TV5.12 | Pengguna dengan izin terbatas | Menu Bulk Actions menampilkan item nonaktif bila tanpa izin | ⬜ |

## TV6. Kalender dan Tugas Saya

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| TV6.1 | Buka Kalender | Hari ini ditandai bulat; hari libur cabang berwarna merah; maksimal 3 tugas per hari | ⬜ |
| TV6.2 | Hari dengan lebih dari 3 tugas, tekan "+N lagi" | Sisa tugas terbuka | ⬜ |
| TV6.3 | Seret tugas ke hari lain | Tenggat berubah; galat ditampilkan bila ditolak (mis. tugas terkunci) | ⬜ |
| TV6.4 | Saring ke satu karyawan dengan cuti disetujui | Hari cuti diarsir dengan keterangan | ⬜ |
| TV6.5 | Tombol sebelumnya / hari ini / berikutnya | Bulan berpindah; data sesuai | ⬜ |
| TV6.6 | Buka Tugas Saya dari sidebar | Hanya tugas milik sendiri (sebagai karyawan atau pengguna); tugas selesai disembunyikan kecuali dipilih | ⬜ |
| TV6.7 | Pengguna tanpa izin modul proyek | Entri Tugas Saya tidak tampil | ⬜ |

## Riwayat dan Lampiran

- Pengujian otomatis padanan sisi BE: `ProjectsViewsTest` (batas WIP, rute Papan). Tampilan hanya dapat diuji manual di peramban; hasil visual (tata letak, panah dependensi, seret dan lepas) wajib dicek langsung.

## Troubleshooting

| Gejala | Penyebab umum | Tindakan |
| --- | --- | --- |
| Menu Papan tidak ada | Izin `projects/board/list` belum disinkronkan | `permission:sync --all`, beri izin ke role |
| Batas WIP tidak tampil | Migrasi `2026_10_10_230000` belum dijalankan | `migrate:all` |
| Panah dependensi tidak terlihat | Tugas pendahulu/penerus di luar rentang tanggal atau kelompok terlipat | Perlebar rentang atau buka kelompok |
| Jalur kritis tidak muncul | Proyek tidak punya rantai dependensi minimal dua tugas | Tambahkan dependensi |
