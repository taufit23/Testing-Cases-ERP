---
title: Ranahku — Proyek dan Tugas (Integrasi Git, F5)
description: Langkah uji tahap kelima modul Proyek dan Tugas: koneksi GitHub/GitLab lewat webhook, repositori, identitas, tautan commit/cabang/PR/pipeline ke tugas, aturan status, smart commit, dan rilis.
---

# Ranahku — Proyek dan Tugas (Integrasi Git, F5)

> Disusun 2026-10-10. **Letak dalam urutan kerja:** setelah berkas `15`. Prasyarat: berkas `12`–`15` selesai; akun GitHub atau GitLab dengan satu repositori uji; `APP_URL` server benar (dipakai membentuk URL webhook); satu proyek dengan beberapa tugas dan satu karyawan yang tertaut ke akun pengguna.

## BG1. Koneksi dan webhook

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BG1.1 | **Proyek → Pengaturan Proyek → Integrasi Git**: aktifkan, simpan | Tersimpan; aturan status bawaan terbentuk (tab Aturan di halaman Git) | ⬜ |
| BG1.2 | **Proyek → Git → Tambah koneksi** (GitHub) | Jendela menampilkan URL webhook dan rahasia (rahasia hanya sekali); daftar koneksi tidak menampilkan rahasia | ⬜ |
| BG1.3 | Di repositori GitHub: Settings → Webhooks → tempel URL dan rahasia, content type `application/json`, centang Push, Branch or tag creation, Pull requests, Pull request reviews, Workflow runs, Releases | GitHub menampilkan pengiriman "ping" tanpa galat | ⬜ |
| BG1.4 | Tab **Repositori**: tambah `pemilik/repo`, petakan ke proyek | Muncul di daftar; mendaftarkan yang sama lagi ditolak; nama dengan spasi ditolak | ⬜ |
| BG1.5 | Tab **Identitas**: petakan username Git ke karyawan | Tersimpan; username sama dua kali ditolak | ⬜ |
| BG1.6 | **Putar rahasia**, lalu kirim ulang pengiriman lama dari GitHub | Pengiriman dengan rahasia lama ditolak (401); isi rahasia baru di GitHub lalu berhasil | ⬜ |
| BG1.7 | Nonaktifkan koneksi, push | Webhook ditolak (404/diabaikan); aktifkan lagi menormalkan | ⬜ |

## BG2. Tautan ke tugas

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BG2.1 | Di detail tugas, kartu **Pengembangan** menampilkan nama cabang yang disarankan; tekan Salin | Nama berformat `kunci-n-judul`; tersalin | ⬜ |
| BG2.2 | Push commit dengan pesan memuat nomor tugas (`ACME-12`, juga huruf kecil) | Commit tertaut; satu komentar sistem berisi hash, judul, tautan | ⬜ |
| BG2.3 | Kirim ulang pengiriman yang sama dari GitHub (Redeliver) | Tidak ada tautan atau komentar ganda | ⬜ |
| BG2.4 | Pesan memuat kunci yang tidak ada atau milik cabang lain | Diabaikan | ⬜ |
| BG2.5 | Push ke repositori yang tidak terdaftar | Diabaikan | ⬜ |
| BG2.6 | Buka tab Pengembangan tugas orang lain yang tidak boleh kamu lihat | Ditolak | ⬜ |

## BG3. Aturan status

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BG3.1 | Buat cabang `acme-12-login` (username Git terpetakan) | Tugas pindah ke In Progress; penanggung jawab terisi bila kosong | ⬜ |
| BG3.2 | Buka PR berjudul memuat `ACME-12` | Tugas pindah ke Review; tautan PR berstatus open | ⬜ |
| BG3.3 | Merge PR | Tugas pindah ke Done (atau Review bila diatur); tautan merged | ⬜ |
| BG3.4 | Kirim ulang peristiwa "PR opened" setelah merge | Status tugas dan tautan tidak mundur | ⬜ |
| BG3.5 | Merge PR untuk tugas yang punya subtugas terbuka | Status tidak berubah; komentar sistem menjelaskan alasan penolakan | ⬜ |
| BG3.6 | Gunakan username Git yang belum dipetakan | Tautan tetap dibuat; status tidak berubah; komentar menyebut identitas belum dipetakan | ⬜ |
| BG3.7 | Pipeline gagal pada cabang bertanda tugas | Tautan pipeline berstatus failed; komentar peringatan; penanggung jawab diberi notifikasi | ⬜ |
| BG3.8 | Matikan satu aturan, ulangi peristiwanya | Aksi aturan itu tidak berjalan | ⬜ |

## BG4. Smart commit

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BG4.1 | Commit `ACME-12 #time 1h 30m menulis parser` | Entri waktu 1,5 jam atas nama karyawan terpetakan, sumber Git; jam terpakai tugas bertambah | ⬜ |
| BG4.2 | Redeliver commit yang sama | Tidak ada entri waktu ganda | ⬜ |
| BG4.3 | Commit `ACME-12 #in-review` dan `#done` | Status mengikuti, lewat pemeriksaan yang sama dengan perubahan manual | ⬜ |
| BG4.4 | Commit `ACME-12 #comment perlu desain` | Komentar muncul di tugas | ⬜ |
| BG4.5 | Matikan saklar smart commit, ulangi dengan commit baru | `#time` dan `#done` diabaikan, commit tetap tertaut | ⬜ |
| BG4.6 | `#time` yang melewati batas jam harian | Entri tidak dibuat; komentar menjelaskan | ⬜ |

## BG5. Rilis dan retensi

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BG5.1 | Terbitkan Release `v1.0.0` di GitHub | Rilis muncul di **Proyek → Rilis**; tugas yang PR-nya sudah merged tertaut | ⬜ |
| BG5.2 | Tambah, ubah, dan hapus rilis manual | Versi ganda ditolak; menghapus rilis melepas tugas, bukan menghapusnya | ⬜ |
| BG5.3 | (Owner) jalankan `projects:purge-scm-data` pada data lama | Ringkasan payload dan buku besar yang lewat retensi dibuang; tautan tetap ada | ⬜ |
