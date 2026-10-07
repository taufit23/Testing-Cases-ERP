---
title: Ranahku — Proyek dan Tugas (Fondasi F1)
description: Langkah uji modul Proyek dan Tugas tahap pertama: pengaturan, master tipe tugas dan label, proyek, anggota, milestone, tugas, subtugas, checklist, perpindahan status berkondisi, komentar dan penyebutan, tugas saya, pengingat, serta hak lihat. Dikerjakan setelah bagian SDM karena penanggung jawab adalah karyawan.
---

# Ranahku — Proyek dan Tugas (Fondasi F1)

> Disusun 2026-10-09. **Letak dalam urutan kerja:** setelah blok SDM (berkas `02` Tahap F dan blok BL di berkas `10`), karena penanggung jawab dan anggota proyek adalah karyawan.
> Berkas ini berdiri sendiri (kode butir **BP**) dan belum disisipkan ke `00a`; kerjakan setelah semua sesi SDM selesai dan sebelum berkas `11`.
> Prasyarat: modul **Proyek dan Tugas** aktif untuk perusahaan, minimal dua karyawan, satu karyawan terhubung ke akun pengujimu, dan satu kontak klien.

## BP1. Pengaturan dan master (kerjakan pertama)

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BP1.1 | Buka **Proyek → Pengaturan Proyek** (`/projects/config`) | Halaman penuh tanpa tabel, nilai bawaan terisi; tombol Simpan dan Refresh di bilah atas | ⬜ |
| BP1.2 | Ubah batas kedalaman subtugas menjadi 2, kunci tugas mandiri menjadi `JOB`, simpan | Berhasil tanpa dialog konfirmasi; muat ulang halaman dan nilai tetap | ⬜ |
| BP1.3 | Isi kunci tugas mandiri dengan `a-b` | Ditolak (huruf besar dan angka, 2–10 karakter) | ⬜ |
| BP1.4 | Buka **Tipe Tugas**, tambah "Fitur" dan "Bug" (estimasi bawaan 8 dan 2 jam) | Muncul di daftar; kode ganda ditolak | ⬜ |
| BP1.5 | Buka **Label Tugas**, tambah "Mendesak" dan "Frontend"; coba nama yang sama | Nama ganda ditolak | ⬜ |
| BP1.6 | Kembalikan kunci tugas mandiri ke `TASK` dan kedalaman ke 3 | Tersimpan | ⬜ |

## BP2. Proyek, anggota, dan milestone

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BP2.1 | **Proyek → Proyek → Buat Proyek**: nama "Implementasi ERP Klien A", biarkan kunci kosong, pilih klien, manajer, dua anggota (satu `member`, satu `reviewer`), anggaran jam dan uang | Konfirmasi simpan muncul; setelah simpan pindah ke halaman detail; nomor `PRJ/tahun/0001`, kunci usulan dari nama (mis. `IEKA`), status Rancangan | ⬜ |
| BP2.2 | Buat proyek kedua dengan kunci yang sama | Ditolak "kunci sudah dipakai" | ⬜ |
| BP2.3 | Buat proyek dengan kunci `TASK` (kunci tugas mandiri) | Ditolak | ⬜ |
| BP2.4 | Di detail, tambah milestone "Desain" dengan tenggat; centang selesai; hapus milestone lain | Milestone tercatat, centang menyimpan waktu selesai | ⬜ |
| BP2.5 | Coba aktifkan proyek **tanpa manajer atau tanpa anggota** (proyek baru kosong) | Tombol "Active" nonaktif dengan tooltip alasan (butuh manajer dan satu anggota) | ⬜ |
| BP2.6 | Aktifkan proyek BP2.1 | Status Active; anggota menerima notifikasi perubahan status | ⬜ |
| BP2.7 | Ubah kunci proyek setelah ada tugas (lihat BP3) | Ditolak selama pengaturan "kunci boleh diganti" mati | ⬜ |

## BP3. Tugas, subtugas, dan checklist

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BP3.1 | **Tombol Buat Tugas** di detail proyek (proyek terisi otomatis); judul "Siapkan data master", tipe "Fitur", penanggung jawab karyawan A, tenggat besok | Nomor `KEY-1`, status Backlog, estimasi terisi dari tipe tugas; penanggung jawab menerima notifikasi | ⬜ |
| BP3.2 | Buat tugas kedua | Nomor `KEY-2` (tanpa lompatan) | ⬜ |
| BP3.3 | Buat tugas **tanpa proyek** (kosongkan Project) | Nomor memakai kunci cabang, mis. `TASK-1` | ⬜ |
| BP3.4 | Di tugas `KEY-1` pilih **Tambah Subtugas** dua kali; buat subtugas di bawah subtugas (tingkat 3) | Tingkat sesuai batas kedalaman diterima; tingkat berikutnya ditolak ("batas kedalaman") | ⬜ |
| BP3.5 | Pilih induk dari proyek lain atau jadikan tugas induk dirinya sendiri / turunannya | Ditolak ("harus proyek yang sama" / "tidak boleh di bawah dirinya") | ⬜ |
| BP3.6 | Tambah checklist: satu butir **wajib**, satu biasa | Tampil dengan lencana "Wajib" | ⬜ |
| BP3.7 | Tambah kolaborator, reviewer, dan pengamat; simpan | Tersimpan; muat ulang tetap ada | ⬜ |
| BP3.8 | Ubah persentase progres tugas yang **punya subtugas** | Kolom nonaktif ("dihitung dari subtugas") | ⬜ |
| BP3.9 | Pindahkan tugas ke proyek lain lewat ubah | Tidak ada pilihan; jika dipaksa lewat API ditolak | ⬜ |

## BP4. Perpindahan status berkondisi (satu pintu)

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BP4.1 | Di tugas induk yang masih punya subtugas terbuka, lihat tombol status "Done" | Nonaktif; tooltip: semua subtugas harus selesai dahulu | ⬜ |
| BP4.2 | Pada subtugas dengan checklist wajib belum dicentang, coba "Done" | Nonaktif; tooltip: checklist harus lengkap | ⬜ |
| BP4.3 | Centang butir wajib, pindahkan subtugas ke Done, lalu induknya | Berhasil; progres subtugas 100, progres induk dan proyek naik; tanggal selesai terisi | ⬜ |
| BP4.4 | Pilih status "Blocked" | Muncul dialog meminta **alasan**; tanpa alasan tombol Konfirmasi nonaktif; dengan alasan tugas berstatus Blocked dan alasan tampil di detail | ⬜ |
| BP4.5 | Buka kembali tugas Done ke In Progress | Tanggal selesai kosong, progres kembali bukan 100 otomatis | ⬜ |
| BP4.6 | Di **Pengaturan**, aktifkan "Reviewer harus menyetujui", lalu coba In Progress → Done | Done nonaktif ("harus direview"); setelah In Review, hanya reviewer/manajer yang bisa Done | ⬜ |
| BP4.7 | Di **Pengaturan**, set mode perpindahan "Strict" | Perpindahan tanpa transisi terdaftar ditolak ("tidak diizinkan workflow"); kembalikan ke "Open" setelah uji | ⬜ |
| BP4.8 | Ganti nama status "Done" di Master Status (mis. "Beres") | Progres dan aturan tetap bekerja (dibaca dari kategori, bukan nama) | ⬜ |
| BP4.9 | Batalkan satu tugas (Cancelled) | Tugas keluar dari penyebut progres proyek | ⬜ |
| BP4.10 | Pilih dua tugas di daftar dan pindahkan massal ke status yang sama (jika menu massal tersedia) | Tugas yang lolos pindah; yang ditolak dilaporkan beserta alasannya | ⬜ |

## BP5. Penutupan proyek

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BP5.1 | Dengan masih ada tugas terbuka, pindahkan proyek ke Completed (mode default "peringatan") | Dialog peringatan jumlah tugas terbuka; "Lanjutkan" menyelesaikan proyek dan mengisi tanggal selesai | ⬜ |
| BP5.2 | Ubah pengaturan "Menutup proyek dengan tugas terbuka" menjadi Blokir; ulangi pada proyek lain | Tombol nonaktif dengan alasan | ⬜ |
| BP5.3 | Matikan "Proyek selesai boleh dibuka kembali"; coba Completed → Active | Ditolak | ⬜ |
| BP5.4 | Hapus proyek yang masih punya tugas | Ditolak ("proyek yang punya tugas tidak bisa dihapus") | ⬜ |
| BP5.5 | Hapus tugas induk yang punya subtugas | Ditolak; hapus subtugas dahulu lalu induk berhasil | ⬜ |

## BP6. Komentar, penyebutan, dan lampiran

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BP6.1 | Di tugas, tulis komentar dengan memilih satu rekan di "Sebut rekan" | Komentar tampil dengan nama penulis; rekan yang disebut dan penanggung jawab menerima notifikasi (penulis tidak menerima notifikasi sendiri) | ⬜ |
| BP6.2 | Hapus komentar milik sendiri; coba hapus komentar orang lain tanpa izin "kelola semua" | Milik sendiri terhapus; milik orang lain tidak ada tombolnya / ditolak | ⬜ |
| BP6.3 | Unggah lampiran pada tugas dan pada proyek | Muncul di panel lampiran masing-masing; orang yang tidak boleh melihat tugas tidak melihat lampirannya | ⬜ |

## BP7. Tugas saya, hak lihat, dan pengingat

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BP7.1 | Buka `/projects/my-tasks` sebagai karyawan penanggung jawab | Hanya tugas milikmu yang terbuka, diurut tenggat; tenggat lewat berwarna merah; tugas selesai tersembunyi | ⬜ |
| BP7.2 | Hidupkan "Tampilkan tugas selesai" | Tugas selesai ikut tampil | ⬜ |
| BP7.3 | Masuk sebagai pengguna **bukan anggota** proyek (tanpa izin kelola semua), buka daftar proyek dan alamat detail proyek BP2.1 | Proyek tidak ada di daftar; alamat detail menolak (tidak ada akses) | ⬜ |
| BP7.4 | Ubah visibilitas proyek menjadi "Seluruh cabang" lalu ulangi BP7.3 | Proyek terlihat | ⬜ |
| BP7.5 | Beri pengguna izin "kelola semua proyek" | Seluruh proyek dan tugas cabang terlihat | ⬜ |
| BP7.6 | Setelah tengah malam (atau jalankan perintah terjadwal pengingat tugas oleh tim teknis), cek notifikasi penanggung jawab | Tugas jatuh tempo besok mendapat pengingat; tugas terlambat mendapat pengingat harian; tugas selesai tidak | ⬜ |
| BP7.7 | Masuk sebagai pengguna perusahaan **lain** (tenant berbeda) dan buka alamat detail proyek/tugas perusahaan pertama | Ditolak; tidak ada data bocor | ⬜ |

## Daftar Periksa Cepat

- [ ] BP1 sampai BP7 selesai tanpa temuan baru berprioritas High
- [ ] Setiap tombol yang nonaktif punya tooltip alasan; tidak ada tombol yang hilang diam-diam
- [ ] Halaman memuat dengan spinner (bukan kerangka kosong) dan tombol Refresh berfungsi di semua halaman modul
