---
title: Ranahku — Proyek dan Tugas (Konfigurasi dan Tampilan, F3)
description: Langkah uji tahap ketiga modul Proyek dan Tugas: editor workflow, field kustom, tampilan tersimpan, papan kanban, kalender, linimasa, dependensi, sprint, tugas berulang, dan preset IT konsultan.
---

# Ranahku — Proyek dan Tugas (Konfigurasi dan Tampilan, F3)

> Disusun 2026-10-09. **Letak dalam urutan kerja:** setelah berkas `13`. Prasyarat: berkas `12` dan `13` selesai; ada minimal dua proyek (satu berstatus "kanban", satu "scrum") dengan beberapa tugas.

## BR1. Editor workflow

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BR1.1 | Buka **Proyek → Workflow** | Workflow bawaan terpilih; daftar status dengan kategori, lencana "Status awal", jumlah tugas per status, panah urut | ⬜ |
| BR1.2 | Tambah status "QA" kategori Review | Muncul di daftar; tugas bisa dipindah ke "QA" dari halaman tugas; papan kanban memuat kolom QA | ⬜ |
| BR1.3 | Ubah kategori satu-satunya status "Done" menjadi kategori lain | Ditolak (harus ada status selesai) | ⬜ |
| BR1.4 | Jadikan "To Do" status awal | Tepat satu status awal; tugas baru kini mulai di "To Do" | ⬜ |
| BR1.5 | Geser urutan status dengan panah | Urutan berubah dan tersimpan; kolom papan mengikuti | ⬜ |
| BR1.6 | Lepas status yang dipakai tugas tanpa memilih tujuan | Pilihan "Pindahkan tugas ke" wajib; setelah dipilih, tugas pindah dan status terlepas | ⬜ |
| BR1.7 | Tambah transisi "Backlog → To Do" yang mensyaratkan field "description" | Memindahkan tugas tanpa deskripsi ditolak (tooltip alasan); dengan deskripsi berhasil | ⬜ |
| BR1.8 | Transisi dengan izin yang tidak ada / syarat tak dikenal | Ditolak dengan pesan | ⬜ |
| BR1.9 | Di Pengaturan ubah mode status ke "Strict" | Hanya transisi terdaftar yang boleh; kembalikan ke "Open" setelah uji | ⬜ |
| BR1.10 | Buat workflow khusus untuk satu tipe tugas | Menyalin workflow bawaan; tugas bertipe itu memakai workflow itu; satu workflow per tipe | ⬜ |

## BR2. Field kustom

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BR2.1 | **Proyek → Field Kustom → tugas**: buat "Lingkungan" (pilihan tunggal, wajib; opsi `dev=Development`, `prod=Production`) | Muncul di daftar | ⬜ |
| BR2.2 | Buat tugas baru tanpa mengisi Lingkungan | Ditolak (wajib) | ⬜ |
| BR2.3 | Isi Lingkungan lalu simpan; buka ulang | Nilai tersimpan; field tampil di bagian "Informasi tambahan" form tugas | ⬜ |
| BR2.4 | Buat field "Tautan desain" (tautan) dan isi dengan teks bukan URL | Ditolak (nilai tidak valid) | ⬜ |
| BR2.5 | Buat field yang hanya berlaku untuk tipe tugas "Bug" | Hanya tampil di tugas bertipe Bug | ⬜ |
| BR2.6 | Buat field dengan kunci yang sama / berhuruf besar / pilihan tanpa opsi | Ditolak | ⬜ |
| BR2.7 | Ubah tipe field yang sudah punya nilai | Ditolak | ⬜ |
| BR2.8 | Di workflow, syaratkan "custom:kunci" pada transisi ke Done; coba selesaikan tugas tanpa nilai | Ditolak sampai field diisi | ⬜ |
| BR2.9 | Hapus field dan jawab Ya untuk membuang nilainya | Field dan nilainya hilang dari tugas; jawab Tidak: field disembunyikan tetapi nilai tetap di basis data | ⬜ |
| BR2.10 | Buat field proyek (mis. "Nomor kontrak") | Tampil di form proyek | ⬜ |

## BR3. Papan kanban dan tampilan tersimpan

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BR3.1 | Buka **Proyek → Papan** | Kolom sesuai status workflow; kartu menampilkan nomor, judul, label, penanggung jawab, tenggat; prioritas tinggi berpita warna | ⬜ |
| BR3.2 | Seret kartu ke kolom lain | Status berubah; muncul di kolom baru setelah muat ulang | ⬜ |
| BR3.3 | Seret kartu induk dengan subtugas terbuka ke "Done" | Kartu kembali ke kolom asal dengan pesan alasan | ⬜ |
| BR3.4 | Seret ke "Blocked" | Dialog alasan; tanpa alasan tidak bisa dikonfirmasi | ⬜ |
| BR3.5 | Seret kartu yang memiliki dependensi belum selesai (mode "Peringatan") | Dialog konfirmasi; setelah dikonfirmasi kartu berpindah | ⬜ |
| BR3.6 | Saring per proyek, prioritas, "Tugas saya", dan pencarian | Kartu mengikuti filter | ⬜ |
| BR3.7 | Simpan tampilan pribadi "Tugas mendesak saya" dengan opsi bawaan | Muncul di pilihan; membuka papan lagi langsung memakai tampilan itu | ⬜ |
| BR3.8 | Simpan tampilan bersama (butuh izin berbagi) lalu masuk sebagai pengguna lain | Tampilan bersama terlihat; tampilan pribadi orang lain tidak | ⬜ |
| BR3.9 | Pengguna tanpa izin berbagi memilih "bagikan" | Opsi nonaktif dengan tooltip izin | ⬜ |
| BR3.10 | Hapus tampilan milik sendiri | Hilang dari daftar | ⬜ |

## BR4. Dependensi

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BR4.1 | Di tugas B tambah dependensi "Selesai → Mulai" pada tugas A | Muncul di "Tugas ini bergantung pada" dan di tugas A pada "Tugas ini menahan" | ⬜ |
| BR4.2 | Tambah dependensi A bergantung pada B (siklus) dan siklus tidak langsung (A→B→C→A) | Ditolak | ⬜ |
| BR4.3 | Dependensi ke dirinya sendiri / dobel | Ditolak | ⬜ |
| BR4.4 | Pengaturan "Peringatan": mulai B sebelum A selesai | Konfirmasi muncul; setelah dikonfirmasi berhasil | ⬜ |
| BR4.5 | Pengaturan "Blokir": mulai B sebelum A selesai | Tombol status nonaktif dengan tooltip tugas yang harus selesai dulu | ⬜ |
| BR4.6 | Tipe FF: selesaikan B sebelum A selesai; tipe SS: mulai B sebelum A mulai | FF menolak "Done" tetapi mengizinkan "mulai"; SS menolak "mulai" sampai A mulai | ⬜ |
| BR4.7 | Pengaturan "Jangan periksa" | Tidak ada pemeriksaan dependensi | ⬜ |

## BR5. Sprint

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BR5.1 | Proyek berstatus kanban | Kartu Sprint tidak tampil | ⬜ |
| BR5.2 | Pada proyek scrum buat Sprint 1 dan Sprint 2, mulai Sprint 1 | Sprint 1 aktif; memulai Sprint 2 ditolak selama Sprint 1 aktif | ⬜ |
| BR5.3 | Di form tugas proyek scrum pilih Sprint 1 dan isi story points | Tersimpan; tugas proyek lain tidak boleh memakai sprint ini | ⬜ |
| BR5.4 | Selesaikan satu tugas, lalu tutup Sprint 1 (rollover "kembali ke backlog") | Tugas selesai tetap di sprint; tugas terbuka dikeluarkan dari sprint | ⬜ |
| BR5.5 | Ubah rollover ke "sprint berikutnya", ulangi dengan Sprint 2 dan Sprint 3 | Tugas terbuka pindah ke sprint terencana berikutnya | ⬜ |
| BR5.6 | Tambah tugas ke sprint yang sudah ditutup / hapus sprint aktif | Ditolak | ⬜ |

## BR6. Tugas berulang

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BR6.1 | Di sebuah tugas (mis. "Laporan mingguan") atur ulang: mingguan, tiap Senin, mulai Senin depan, berakhir akhir bulan | Tersimpan; panel menunjukkan aturan aktif | ⬜ |
| BR6.2 | Setelah jadwal jalan (atau tim teknis menjalankan perintah pembuat tugas berulang) | Satu salinan tugas dibuat dengan penanggung jawab, label, dan field kustom yang sama; tenggat mengikuti selisih tugas contoh; nomor baru | ⬜ |
| BR6.3 | Jalankan lagi pada hari yang sama | Tidak ada salinan ganda | ⬜ |
| BR6.4 | Tunggu melewati tanggal berakhir | Pengulangan berstatus selesai; tidak ada salinan baru | ⬜ |
| BR6.5 | Buka salinan | Panel menyatakan ini salinan; tidak bisa diatur berulang | ⬜ |
| BR6.6 | Hentikan pengulangan | Aturan hilang; salinan lama tetap ada | ⬜ |

## BR7. Kalender dan linimasa

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BR7.1 | Buka **Proyek → Kalender** | Tugas muncul pada tanggal tenggatnya; hari libur cabang bertanda merah; navigasi bulan berfungsi | ⬜ |
| BR7.2 | Saring ke seorang karyawan yang punya cuti | Hari cuti disorot dengan keterangan | ⬜ |
| BR7.3 | Buka **Linimasa** | Batang tugas dari mulai ke tenggat, milestone bertanda bendera, lencana dependensi | ⬜ |
| BR7.4 | Pengguna tanpa akses ke proyek membuka keduanya | Tugas proyek itu tidak muncul | ⬜ |

## BR8. Preset IT konsultan

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BR8.1 | Di **Pengaturan Proyek** tekan "Terapkan preset IT konsultan" | Tipe tugas (Fitur, Bug, Tugas, Change Request, Dukungan), label, 3 field kustom, status QA, dan 3 template terbentuk | ⬜ |
| BR8.2 | Tekan lagi | Pesan "preset sudah diterapkan"; tidak ada data ganda | ⬜ |
| BR8.3 | Ubah nama salah satu tipe tugas, tekan lagi | Perubahan tidak ditimpa | ⬜ |

## Daftar Periksa Cepat

- [ ] BR1 sampai BR8 selesai tanpa temuan baru berprioritas High
- [ ] Setiap penolakan menampilkan alasan; tidak ada tombol yang hilang diam-diam
- [ ] Seret kartu di papan tidak pernah melewati aturan yang sama di halaman tugas
