---
title: Ranahku — Proyek dan Tugas (Integrasi SDM, F2)
description: Langkah uji tahap kedua modul Proyek dan Tugas yang terhubung ke SDM: pengaturan cuti dan beban kerja, peringatan atau penolakan penugasan saat karyawan cuti, halaman Beban Kerja, template tugas, tugas onboarding dan offboarding otomatis, dan karyawan tidak aktif.
---

# Ranahku — Proyek dan Tugas (Integrasi SDM, F2)

> Disusun 2026-10-09. **Letak dalam urutan kerja:** setelah berkas `12` (fondasi proyek dan tugas). Prasyarat: berkas `12` selesai; di modul SDM sudah ada minimal tiga karyawan,
> satu **jadwal kerja** (shift + hari kerja) untuk karyawan A, satu **hari libur** cabang, dan satu **cuti yang sudah disetujui** untuk karyawan B pada rentang tanggal tertentu
> (catat tanggalnya; di bawah disebut `TGL-CUTI`).

## BQ1. Pengaturan ketersediaan

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BQ1.1 | Buka **Pengaturan Proyek**; bagian "Ketersediaan karyawan dan beban kerja" | Ada pilihan penugasan saat cuti (Jangan periksa / Peringatan / Blokir), ambang beban (%), sumber hari kerja, jam kerja bawaan per hari | ⬜ |
| BQ1.2 | Biarkan "Peringatan", ambang 100, sumber "Jadwal kerja karyawan", 8 jam, simpan | Tersimpan tanpa dialog konfirmasi | ⬜ |
| BQ1.3 | Bagian "Onboarding dan offboarding": buka daftar template | Hanya template berjenis onboarding di kolom pertama, offboarding di kolom kedua (kosong dulu sebelum BQ4) | ⬜ |

## BQ2. Penugasan saat cuti, libur, dan beban

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BQ2.1 | Buat tugas, pilih karyawan B (yang cuti) dan tanggal yang menyentuh `TGL-CUTI` | Muncul kotak peringatan kuning "karyawan sedang cuti disetujui" dengan rentang tanggal dan jumlah hari kerja; tugas **tetap bisa disimpan** | ⬜ |
| BQ2.2 | Ubah tanggal ke minggu tanpa cuti | Peringatan hilang | ⬜ |
| BQ2.3 | Di Pengaturan ubah menjadi "Blokir", ulangi BQ2.1 | Simpan ditolak dengan pesan cuti; kotak peringatan berwarna merah | ⬜ |
| BQ2.4 | Pada tugas yang sudah ada (tanggal aman) ubah tanggalnya ke rentang cuti | Ditolak | ⬜ |
| BQ2.5 | Kembalikan ke "Peringatan". Beri karyawan A tugas 40 jam untuk satu minggu kerja, lalu tugas kedua 8 jam di minggu yang sama | Tugas kedua memunculkan peringatan beban melebihi batas; tetap bisa disimpan | ⬜ |
| BQ2.6 | Pilih "Jangan periksa" dan ulangi BQ2.1 | Tidak ada peringatan sama sekali | ⬜ |
| BQ2.7 | Pada rentang yang melewati hari libur cabang, perhatikan jumlah hari kerja di peringatan | Hari libur tidak dihitung sebagai hari kerja | ⬜ |

## BQ3. Halaman Beban Kerja

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BQ3.1 | Buka **Proyek → Beban Kerja** | Tabel karyawan × minggu; sel menampilkan jam rencana / kapasitas (persen); spinner saat memuat | ⬜ |
| BQ3.2 | Bandingkan kapasitas minggu yang ada cuti penuh satu hari dengan minggu biasa | Kapasitas berkurang sebesar jam kerja hari cuti; setengah hari cuti mengurangi separuh | ⬜ |
| BQ3.3 | Cari minggu dengan beban di atas ambang | Sel berwarna merah; 80–100% kuning | ⬜ |
| BQ3.4 | Selesaikan tugas yang membebani lalu muat ulang | Beban minggu itu turun (tugas selesai dan dibatalkan tidak dihitung) | ⬜ |
| BQ3.5 | Ganti ke **Per Departemen**, lalu pilih satu departemen di tampilan per karyawan | Ringkasan per departemen dijumlahkan benar; filter departemen mencakup sub-departemen | ⬜ |
| BQ3.6 | Tugas tanpa tenggat | Jam-nya muncul di kolom "Tanpa tenggat", tidak membebani minggu mana pun | ⬜ |
| BQ3.7 | Masuk sebagai pengguna yang tidak memiliki izin halaman beban kerja | Halaman/menu tidak tersedia; panggilan ditolak | ⬜ |

## BQ4. Template tugas

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BQ4.1 | **Proyek → Template Tugas → Buat**: jenis "Template proyek", tiga tugas; satu tugas induk dengan satu subtugas; penanggung jawab "karyawan paling sedikit beban di departemen X", satu "manajer proyek", satu "karyawan tertentu" | Konfirmasi simpan, lalu halaman detail; induk-anak tersimpan | ⬜ |
| BQ4.2 | Pilih induk subtugas dirinya sendiri atau posisi tanpa karyawan di aturan "posisi" | Aturan kosong (posisi/departemen/karyawan belum dipilih) ditolak saat simpan | ⬜ |
| BQ4.3 | **Terapkan Template** ke sebuah proyek dengan tanggal mulai hari Senin | Tugas dibuat bernomor `KEY-n`; tanggal mulai/selesai dihitung dalam **hari kerja** (melewati akhir pekan dan hari libur); subtugas di bawah induknya | ⬜ |
| BQ4.4 | Periksa penanggung jawab hasil terapan | Aturan departemen memilih karyawan aktif dengan tugas terbuka paling sedikit; aturan manajer memakai manajer proyek; aturan tertentu memakai karyawan itu | ⬜ |
| BQ4.5 | Terapkan template yang memuat baris tanpa kandidat | Tugas tetap dibuat tanpa penanggung jawab; muncul peringatan baris mana yang tidak punya kandidat | ⬜ |
| BQ4.6 | Terapkan template onboarding tanpa memilih karyawan | Ditolak ("pilih karyawan") | ⬜ |
| BQ4.7 | Template tidak aktif | Tidak muncul di pilihan pengaturan onboarding | ⬜ |

## BQ5. Onboarding dan offboarding otomatis

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BQ5.1 | Buat template onboarding "Karyawan Baru" (siapkan akun, orientasi) dan template offboarding "Karyawan Keluar" (tarik aset); pilih keduanya di Pengaturan | Pengaturan menerima; template berjenis salah ditolak | ⬜ |
| BQ5.2 | Tambah **karyawan baru** di SDM (tanggal masuk hari Senin) | Tugas onboarding terbentuk otomatis, berkaitan dengan karyawan itu, tanggal relatif dari tanggal masuk dalam hari kerja | ⬜ |
| BQ5.3 | Ubah karyawan itu lalu simpan lagi | Tidak ada tugas ganda | ⬜ |
| BQ5.4 | Setujui sebuah **Perubahan Status Karyawan** (mis. masa percobaan → tetap) untuk karyawan | Template onboarding dijalankan untuk peristiwa itu (satu kali per perubahan); menyetujui ulang tidak menggandakan | ⬜ |
| BQ5.5 | Setujui sebuah **Mutasi** karyawan | Template offboarding dijalankan (satu kali per mutasi) | ⬜ |
| BQ5.6 | Kosongkan template di Pengaturan, lalu tambah karyawan baru | Tidak ada tugas yang dibuat; pembuatan karyawan tidak terganggu | ⬜ |
| BQ5.7 | Nonaktifkan template lalu picu peristiwa karyawan | Tidak ada tugas; tidak ada galat di SDM | ⬜ |

## BQ6. Karyawan tidak aktif

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BQ6.1 | Pilih karyawan non-tetap dengan tanggal akhir kontrak yang sudah lewat (atau data yang sudah dianonimkan) sebagai penanggung jawab sebuah tugas lama; buka dropdown penanggung jawab di tugas baru | Karyawan itu tidak ada di pilihan; di tugas lamanya ia tetap tampil sebagai penanggung jawab saat ini | ⬜ |
| BQ6.2 | Buka **Beban Kerja**, kartu "Tugas yang perlu penanggung jawab baru" | Tugas terbuka milik karyawan tidak aktif terdaftar; karyawan itu tidak ada di tabel beban | ⬜ |
| BQ6.3 | Centang beberapa tugas, pilih karyawan pengganti, **Alihkan** | Penanggung jawab berganti, pengganti menerima notifikasi, tugas hilang dari kartu | ⬜ |
| BQ6.4 | Coba mengalihkan ke karyawan tidak aktif | Ditolak | ⬜ |
| BQ6.5 | Kosongkan pilihan pengganti lalu Alihkan | Penanggung jawab dikosongkan | ⬜ |
| BQ6.6 | Coba **hapus karyawan** yang masih menjadi manajer/anggota proyek atau penanggung jawab tugas | Ditolak dengan pesan "masih dipakai di proyek atau tugas" | ⬜ |

## Daftar Periksa Cepat

- [ ] BQ1 sampai BQ6 selesai tanpa temuan baru berprioritas High
- [ ] Peringatan cuti memakai data cuti SDM yang sama dengan halaman Cuti (tanggal dan setengah hari cocok)
- [ ] Pembuatan karyawan, persetujuan perubahan status, dan mutasi di SDM tidak pernah gagal karena modul proyek
