---
title: Ranahku — Proyek dan Tugas (Webhook Git Otomatis, Unggah Portal, dan Lintas Modul)
description: Langkah uji pendaftaran webhook Git otomatis lewat Integrasi, unggah berkas dari portal klien, serta hubungan modul Proyek dengan modul lain dan keamanan.
---

# Ranahku — Proyek dan Tugas (Git Otomatis, Portal, Lintas Modul)

> Disusun 2026-10-08. **Letak dalam urutan kerja:** setelah berkas `20`. Prasyarat: berkas `12`–`19` selesai; bagian LG hanya bila punya akun GitHub (App) atau GitLab (token) uji dan `APP_URL` berupa alamat https publik; `seed:all` sudah dijalankan (baris Integrasi `github_app` dan `gitlab`).

## LG1. Kredensial di Integrasi

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| LG1.1 | Core → Integration Configs: baris `github_app` dan `gitlab` ada | Dua baris dengan bidang kredensial (App ID + kunci privat; token akses) | ⬜ |
| LG1.2 | Halaman Git, tanpa kredensial | Tombol "Load repositories" dan saklar daftar otomatis nonaktif dengan penjelasan | ⬜ |
| LG1.3 | Isi kredensial `github_app` (kunci privat PEM yang benar) | Disimpan terenkripsi; tampilan daftar menutup nilainya | ⬜ |

## LG2. Pendaftaran webhook otomatis

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| LG2.1 | Buat koneksi GitHub; "Load repositories" | Daftar repositori yang dijangkau aplikasi (yang sudah terdaftar tidak ikut) | ⬜ |
| LG2.2 | Tambah repositori dari daftar dengan saklar "Register the webhook automatically" aktif | Repositori dibuat; kolom Webhook "Terdaftar otomatis"; di GitHub muncul webhook berisi URL koneksi, tipe JSON, event push/create/pull_request/pull_request_review/workflow_run/release | ⬜ |
| LG2.3 | Lakukan commit berisi nomor tugas ke repositori itu | Event tiba, ledger terisi, commit tertaut ke tugas (alur berkas `16`) | ⬜ |
| LG2.4 | Matikan izin Webhooks pada App lalu daftarkan repositori lain | Repositori tetap dibuat; kolom Webhook "Pendaftaran gagal" dengan pesan dari GitHub saat disorot | ⬜ |
| LG2.5 | Menu baris → "Daftarkan webhook otomatis" pada repositori yang gagal (setelah izin diperbaiki) | Berhasil; galat hilang | ⬜ |
| LG2.6 | Daftarkan ulang repositori yang sudah terdaftar | Tidak ada webhook ganda di GitHub (yang lama dicabut lebih dulu) | ⬜ |
| LG2.7 | Menu baris → "Hapus webhook otomatis" | Webhook hilang di GitHub; kolom kembali "Manual" | ⬜ |
| LG2.8 | Hapus repositori yang punya webhook otomatis | Webhook di GitHub ikut dicabut | ⬜ |
| LG2.9 | Ulangi LG2.1–LG2.2 untuk GitLab (token akses) | Daftar proyek dan hook (push, tag, merge request, pipeline, release) terbentuk; id hook tersimpan | ⬜ |
| LG2.10 | `APP_URL` bukan alamat publik / bukan https | Penyedia menolak; pesan galat tampil di kolom Webhook | ⬜ |
| LG2.11 | Pengguna tanpa izin daftar otomatis | Item menu nonaktif | ⬜ |
| LG2.12 | Jalur manual (tempel URL dan rahasia ke GitHub) pada koneksi lain | Tetap berfungsi seperti berkas `16` | ⬜ |

## LG3. Unggah berkas dari portal klien

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| LG3.1 | Buat tautan portal dengan izin Unggah dan bagikan satu tugas ke klien | Tautan dibuat | ⬜ |
| LG3.2 | Buka portal sebagai klien; ikon penjepit pada tugas yang dibagikan; unggah satu berkas | Berkas diterima; di detail tugas muncul sebagai lampiran (setelah diproses antrean); manajer proyek mendapat notifikasi | ⬜ |
| LG3.3 | Unggah berkas bertipe/ukuran yang ditolak | Ditolak dengan pesan | ⬜ |
| LG3.4 | Tautan tanpa izin Unggah | Ikon tidak tampil; panggilan langsung ditolak | ⬜ |
| LG3.5 | Unggah ke tugas yang tidak dibagikan ke klien (ubah id) | Ditolak | ⬜ |
| LG3.6 | Unggah belasan kali dalam semenit | Dibatasi (10 per menit) | ⬜ |
| LG3.7 | Pastikan antrean worker berjalan (supervisor) | Lampiran terproses; bila worker mati, lampiran menunggu lalu terproses saat worker hidup | ⬜ |

## LM1. Hubungan dengan modul lain

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| LM1.1 | HRM: hapus karyawan yang menjadi manajer/anggota/penanggung jawab proyek atau tugas | Ditolak dengan pesan karyawan masih dipakai proyek/tugas | ⬜ |
| LM1.2 | HRM: tandai karyawan tidak aktif | Tugas yang masih ditugaskan padanya muncul di Beban Kerja sebagai penanggung jawab tidak aktif | ⬜ |
| LM1.3 | HRM: cuti disetujui dan hari libur | Kapasitas minggu itu turun; peringatan saat menugaskan di tanggal cuti sesuai pengaturan | ⬜ |
| LM1.4 | Kontak / unit bisnis / pusat biaya / departemen yang dipakai proyek: coba hapus | Gagal (dijaga basis data); pesan galat dari server tampil | ⬜ |
| LM1.5 | Penjualan: buat faktur dari tagihan proyek (berkas `15`), lalu hapus faktur draf | Entri waktu terlepas dan bisa ditagih lagi | ⬜ |
| LM1.6 | Penjualan: proyek yang punya faktur atau pesanan penjualan tertaut, coba hapus proyek | Ditolak | ⬜ |
| LM1.7 | Pembelian: tautkan faktur pembelian ke proyek; setujui | Biaya proyek bertambah sebesar subtotal tanpa pajak (berkas `18` BL4) | ⬜ |
| LM1.8 | Pengeluaran: tautkan pengeluaran ke proyek | Biaya langsung terhitung | ⬜ |
| LM1.9 | Akuntansi: jurnal biaya tenaga kerja (berkas `19` PA4) masuk Buku Besar dan neraca saldo tetap seimbang | Seimbang | ⬜ |
| LM1.10 | Alur persetujuan: permintaan penutupan/timesheet/change request muncul di antrean persetujuan beserta modulnya | Muncul; setelah diputuskan hilang dari antrean | ⬜ |
| LM1.11 | Lampiran: unggah lampiran di proyek dan tugas | Lampiran tersimpan lewat mesin lampiran terpusat | ⬜ |
| LM1.12 | Notifikasi: tugas ditugaskan, tenggat dekat, SLA melanggar, pengingat timesheet | Masuk ke kotak notifikasi penerima yang benar; tidak ganda | ⬜ |
| LM1.13 | LogBook: waktu disetujui dan PR merge tercatat (berkas `18` BL2) | Kegiatan muncul, tanpa skor otomatis | ⬜ |
| LM1.14 | Asisten AI aplikasi: tanya "tugas saya" dan "status proyek X" | Jawaban memakai data milik pengguna saja; proyek yang tidak boleh dilihat ditolak | ⬜ |
| LM1.15 | Dokumen penjualan/pembelian/sewa/produksi: tombol "Buat tugas dari dokumen" | Tugas terbuat dengan tautan dokumen; kartu Dokumen terkait membuka dokumen | ⬜ |

## LM2. Gerbang modul, izin, dan keamanan

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| LM2.1 | Penyedia tanpa modul Proyek | Menu dan seluruh rute proyek tertutup | ⬜ |
| LM2.2 | Penyedia disuspensi | Seluruh API dan masuk ditolak; perintah terjadwal modul (pengingat, SLA, webhook keluar, jurnal biaya) melewati cabangnya | ⬜ |
| LM2.3 | Dua penyedia berbeda: pengguna penyedia A mencoba id proyek/tugas/entri milik B | Tidak ditemukan / ditolak untuk semua endpoint | ⬜ |
| LM2.4 | Rahasia dan tarif | Tarif biaya/tagih hanya terlihat bagi pemegang izin lihat tarif; webhook, token portal, dan kunci Integrasi tidak pernah muncul penuh setelah dibuat | ⬜ |
| LM2.5 | Portal klien: token tidak valid/kedaluwarsa/dicabut | Selalu respons seragam tanpa membocorkan keberadaan proyek | ⬜ |
| LM2.6 | Webhook masuk dengan tanda tangan salah | Ditolak dan tercatat di ledger; tidak ada tautan terbentuk | ⬜ |

## Riwayat dan Lampiran

- Pengujian otomatis padanan: `ProjectsScmAutoRegisterTest` (panggilan penyedia dipalsukan), `ProjectsPortalTest`, `ProjectsBranchIsolationTest`, `ProjectsDocumentLinksTest`. Pendaftaran ke GitHub/GitLab sungguhan, unggah portal (lampiran), dan push notification hanya bisa diuji manual di server.

## Troubleshooting

| Gejala | Penyebab umum | Tindakan |
| --- | --- | --- |
| "Load repositories" nonaktif | Kredensial integrasi kosong atau tidak lengkap | Isi `github_app` / `gitlab` di Integration Configs |
| Pendaftaran gagal 404/403 di GitHub | App belum terpasang di repositori atau izin Webhooks kurang | Pasang App di repositori; beri izin Repository webhooks: write |
| Pendaftaran gagal 422 | URL webhook tidak dapat dijangkau (bukan https publik) | Perbaiki `APP_URL` |
| Lampiran dari portal tidak muncul | Worker antrean mati | Periksa supervisor `laravel-worker` dan jalankan ulang |
