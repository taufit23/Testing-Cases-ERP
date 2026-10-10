---
title: Ranahku — SDM (Data Uji Seeder, Dua Periode Gaji)
description: Daftar periksa manual modul SDM di atas data yang dibuat seeder HrmTestCaseSeeder: 10 karyawan berprofil berbeda, absensi dua bulan, cuti, payroll dua periode, rekrutmen, dan skenario negatif. Tiap butir menyebut data yang harus dilihat dan hasil yang diharapkan.
---

# Ranahku — SDM (Data Uji Seeder, Dua Periode Gaji)

> Disusun 2026-10-10. Seeder: `erpApiServices/database/seeders/HrmTestCaseSeeder.php` (manual, tidak ikut `seed:all`).
> Jalankan: `php artisan db:seed --class=HrmTestCaseSeeder` di server dev atau DB uji, bukan produksi klien.
> Env: `HRM_TEST_BRANCH_ID`, `HRM_TEST_START` (format `YYYY-MM`, bawaan dua bulan sebelum bulan berjalan), `HRM_TEST_MONTHS`, `HRM_TEST_CUTOFF`.
>
> **Cara memakai berkas ini:** jalankan seeder, catat daftar "TEMUAN" di akhir output, lalu telusuri butir di bawah satu per satu lewat aplikasi.
> Di bawah, `BULAN-1` = bulan uji pertama, `BULAN-2` = bulan uji kedua. Karyawan uji punya email `<nama>@hrmtc.test`.
> Periode payroll `BULAN-1` dibiarkan **paid**, `BULAN-2` dibiarkan **processing** supaya approve dan bayar bisa dicoba dari aplikasi.
>
> Format kolom: **Positif** (harus berhasil) / **Negatif** (harus ditolak) / **Periksa** (bandingkan angka atau tampilan).

## Prasyarat

| # | Periksa | Hasil yang diharapkan |
| - | ------- | --------------------- |
| P1 | Cabang uji belum punya periode payroll non-draft pada bulan uji | Bila sudah ada, absensi bulan itu terkunci dan seeder mencatat temuan; pilih cabang atau bulan lain |
| P2 | Pengaturan SDM cabang | Geofence aktif radius 150 m, pusat -6.263357 / 106.614035; persetujuan cuti dan perubahan status aktif |
| P3 | Pengaturan BPJS tahun BULAN-1 | Lima program terisi (kesehatan, JHT, JKK, JKM, JP) dengan batas upah |

## A. Profil karyawan uji

| Email | Profil | Yang diuji |
| ----- | ------ | ---------- |
| rina@hrmtc.test | Manajer SDM, K/1, 15 juta, absensi sempurna | Tunjangan jabatan 10 persen, anak 1, manajer dari semua karyawan |
| budi@hrmtc.test | Staf keuangan, TK/0, 8 juta, sering terlambat | Potongan keterlambatan, potongan koperasi hanya aktif di BULAN-1, potongan pinjaman mulai BULAN-2 |
| sari@hrmtc.test | Staf keuangan, K/2, 9 juta, lembur banyak | Lembur, bonus kinerja manual, PPh21 dengan tanggungan 2 anak |
| dedi@hrmtc.test | Staf penjualan, K/0, 7 juta, beberapa alpa | Alpa tanpa keterangan, saldo cuti tahunan hanya 1 hari, komisi |
| maya@hrmtc.test | Admin, TK/0, PKWT berakhir bulan setelah BULAN-2 | Hari sakit, kontrak mendekati berakhir, pengajuan perpanjangan ditolak |
| joko@hrmtc.test | Masa percobaan, tanpa NPWP | Lupa check-out, perubahan status ke tetap disetujui, gaji naik 5 juta |
| wati@hrmtc.test | Staf penjualan, K/3, 12 juta | Cuti melahirkan 90 hari |
| anto@hrmtc.test | Harian lepas, tanpa NPWP dan tanpa bank | Kerja Sabtu, roster shift pagi dan malam |
| lina@hrmtc.test | Masuk di tengah BULAN-1 | Gaji prorata bulan pertama |
| hendra@hrmtc.test | Direktur keuangan, K/2, 45 juta, tanpa NPWP dan tanpa bank | PPh21 lapisan tinggi, tanpa NPWP lebih mahal, BPJS kena batas upah |

## B. Master data

| # | Jenis | Langkah | Hasil yang diharapkan |
| - | ----- | ------- | --------------------- |
| B1 | Positif | Buka Departemen dan Struktur Organisasi | 5 departemen, Operasional Gudang berada di bawah Operasional |
| B2 | Positif | Buka Posisi | 6 posisi dengan rentang gaji; Direktur Keuangan 30-60 juta |
| B3 | Negatif | Buat posisi dengan gaji minimum lebih besar dari maksimum | Ditolak |
| B4 | Positif | Buka Komponen Gaji | 7 komponen: tetap, persen dari gaji pokok, persen dari bruto, manual, potongan, beban perusahaan |
| B5 | Negatif | Buat komponen dengan kode ganda atau persentase di atas 100 | Ditolak kedua-duanya |
| B6 | Negatif | Buat tipe cuti dengan generate otomatis tanpa bulan generate | Ditolak |
| B7 | Negatif | Buat shift bukan global tanpa departemen | Ditolak |
| B8 | Periksa | Shift Malam 22:00-06:00 | Ditandai melewati tengah malam; jam kerja dihitung benar |

## C. Karyawan

| # | Jenis | Langkah | Hasil yang diharapkan |
| - | ----- | ------- | --------------------- |
| C1 | Positif | Buka Karyawan | 10 karyawan, nomor karyawan terbentuk otomatis, atasan terisi |
| C2 | Negatif | Buat karyawan dengan telepon `abc123` | Ditolak |
| C3 | Negatif | Buat karyawan dengan akun pengguna tetapi tanpa email | Ditolak |
| C4 | Negatif | Buat karyawan dengan gaji negatif atau atasan yang tidak ada | Ditolak |
| C5 | Periksa | Buka struktur gaji Rina | Gaji pokok, tunjangan transport, tunjangan jabatan, dan estimasi bulan ini tampil; angka sama dengan slip |
| C6 | Periksa | Buka struktur gaji Budi di BULAN-1 dan BULAN-2 | Potongan koperasi hanya di BULAN-1, potongan pinjaman hanya di BULAN-2 |
| C7 | Negatif | Ubah gaji pokok langsung lewat Edit Karyawan | Tidak bisa; wajib lewat Perubahan Status Kepegawaian |
| C8 | Negatif | Tambah komponen gaji dengan tanggal akhir sebelum tanggal mulai | Ditolak |

## D. Absensi

| # | Jenis | Langkah | Hasil yang diharapkan |
| - | ----- | ------- | --------------------- |
| D1 | Periksa | Rekap absensi BULAN-1 per karyawan | Budi banyak terlambat, Sari banyak lembur, Dedi punya alpa, Maya punya sakit, Joko punya hari tanpa check-out |
| D2 | Periksa | Hari libur nasional dan cuti bersama pada tanggal 17 dan 18 | Karyawan kantor tidak punya catatan; Anto tetap bisa tercatat Sabtu |
| D3 | Periksa | Karyawan baru Lina | Tidak ada absensi sebelum tanggal masuk |
| D4 | Negatif | Buat absensi ganda untuk karyawan dan tanggal yang sama | Ditolak |
| D5 | Negatif | Buat absensi dengan check-out sebelum check-in | Ditolak |
| D6 | Negatif | Buat absensi dengan kode status yang tidak dikenal | Ditolak |
| D7 | Negatif | Check-in dengan koordinat di luar radius 150 m | Ditolak dengan pesan di luar area |
| D8 | Positif | Check-in dengan koordinat -6.263357 / 106.614035 dari halaman absensi saya | Berhasil, jam dari server (uji manual; seeder tidak bisa) |
| D9 | Periksa | Log mesin absensi | Punch Rina dan Wati menjadi absensi; kode tidak dikenal berstatus tidak cocok; punch duplikat tidak membuat baris kedua |
| D10 | Negatif | Kirim punch dengan token mesin yang salah | 401 |
| D11 | Periksa | Pembuatan siklus hari kosong untuk satu periode | Hari kerja tanpa catatan terbentuk, hari libur tidak |

## E. Cuti

| # | Jenis | Langkah | Hasil yang diharapkan |
| - | ----- | ------- | --------------------- |
| E1 | Positif | Buka saldo cuti | Cuti tahunan 12 hari per karyawan; Dedi hanya 1 hari; Wati punya 90 hari cuti melahirkan |
| E2 | Periksa | Cuti Rina yang disetujui (3 hari kerja) | Saldo cuti tahunan Rina berkurang 3 |
| E3 | Periksa | Cuti setengah hari Sari yang disetujui | Saldo berkurang 0,5 |
| E4 | Periksa | Cuti Anto tanpa gaji | Tidak mengurangi saldo cuti tahunan; memotong gaji di slip |
| E5 | Negatif | Ajukan cuti yang bertumpuk dengan cuti Rina yang sudah disetujui | Ditolak |
| E6 | Negatif | Ajukan cuti dengan tanggal akhir sebelum tanggal mulai | Ditolak |
| E7 | Negatif | Ajukan cuti mundur lebih dari 60 hari | Ditolak |
| E8 | Negatif | Dedi mengajukan 5 hari cuti tahunan | Ditolak karena saldo kurang |
| E9 | Negatif | Budi (pria) mengajukan cuti melahirkan | Ditolak karena batasan gender |
| E10 | Negatif | Setengah hari tanpa periode pagi atau sore | Ditolak |
| E11 | Negatif | Setengah hari pada tipe cuti yang tidak mengizinkan | Ditolak |
| E12 | Periksa | Pengajuan Maya yang ditolak, Joko yang dibatalkan, Lina yang diminta revisi | Status akhir sesuai; saldo tidak berkurang |
| E13 | Periksa | Pengajuan Maya yang dibiarkan pending | Bisa disetujui atau ditolak dari aplikasi |

## F. Penyesuaian absensi

| # | Jenis | Langkah | Hasil yang diharapkan |
| - | ----- | ------- | --------------------- |
| F1 | Positif | Setujui penyesuaian Joko | Absensi tanggal itu berubah sesuai jam yang diminta |
| F2 | Periksa | Penyesuaian Budi yang ditolak dan Maya yang dibatalkan | Absensi tidak berubah |
| F3 | Positif | Penyesuaian Dedi yang masih menunggu | Bisa disetujui dari aplikasi |
| F4 | Negatif | Penyesuaian dengan jam terbalik atau alasan kosong | Ditolak |
| F5 | Periksa | Penyesuaian pada tanggal di periode BULAN-1 yang sudah paid | Perilaku sesuai aturan: absensi terkunci, koreksi hanya lewat penyesuaian; catat bila ternyata ditolak total |

## G. Payroll

| # | Jenis | Langkah | Hasil yang diharapkan |
| - | ----- | ------- | --------------------- |
| G1 | Periksa | Daftar periode payroll | BULAN-1 paid, BULAN-2 processing; tanggal mulai dan akhir sesuai siklus cabang |
| G2 | Negatif | Buat periode untuk bulan yang sudah punya periode | Ditolak |
| G3 | Negatif | Approve atau bayar periode yang masih draft | Ditolak |
| G4 | Negatif | Proses ulang periode yang sudah approved, atau bayar dua kali | Ditolak |
| G5 | Periksa | Item payroll Hendra | PPh21 memakai tarif tanpa NPWP (lebih tinggi); BPJS kesehatan dan JP kena batas upah |
| G6 | Periksa | Item payroll Lina BULAN-1 | Gaji prorata sesuai hari kerja sejak tanggal masuk |
| G7 | Periksa | Item payroll Dedi | Potongan alpa muncul; komisi tidak otomatis masuk gaji (cek perilaku sesuai desain) |
| G8 | Periksa | Item payroll Wati saat cuti melahirkan | Sesuai pengaturan cuti berbayar |
| G9 | Periksa | Total bruto, potongan, PPh21, BPJS di periode dibandingkan dengan jurnal | Jurnal akrual dan penyelesaian seimbang dan sama dengan total periode |
| G10 | Positif | Setujui lalu bayar periode BULAN-2 dari aplikasi | Status berurutan approved, paid; jurnal terbentuk satu kali |
| G11 | Negatif | Ubah item payroll dengan lembur negatif | Ditolak |
| G12 | Negatif | Buat absensi baru pada tanggal di periode paid | Ditolak karena terkunci |
| G13 | Periksa | Slip gaji per karyawan dan unduh PDF | Isi sama dengan item payroll; PDF terbuka; teks sesuai bahasa pengguna |
| G14 | Periksa | Halaman Slip Gaji Saya setelah akun ditautkan ke Rina | Hanya slip milik Rina |

## H. Komisi

| # | Jenis | Langkah | Hasil yang diharapkan |
| - | ----- | ------- | --------------------- |
| H1 | Positif | Buka aturan komisi | Dua aturan: persen dari pendapatan dan nominal tetap |
| H2 | Negatif | Buat aturan dengan tipe selain persen atau tetap | Ditolak |
| H3 | Periksa | Komisi Dedi | Satu dibayar, satu belum; tandai dibayar yang kedua dari aplikasi |

## I. Perubahan status dan mutasi

| # | Jenis | Langkah | Hasil yang diharapkan |
| - | ----- | ------- | --------------------- |
| I1 | Periksa | Perubahan status Joko ke tetap dengan gaji 5 juta | Setelah disetujui, jenis kontrak dan gaji berubah otomatis; riwayat tersimpan |
| I2 | Periksa | Perpanjangan kontrak Maya yang ditolak | Data karyawan tidak berubah |
| I3 | Negatif | Tanggal akhir kontrak yang sudah lewat | Ditolak |
| I4 | Positif | Pengajuan Lina yang masih menunggu | Bisa disetujui dari aplikasi |
| I5 | Periksa | Mutasi cabang | Hanya bila ada lebih dari satu cabang; mutasi ke cabang asal ditolak |

## J. Rekrutmen

| # | Jenis | Langkah | Hasil yang diharapkan |
| - | ----- | ------- | --------------------- |
| J1 | Positif | Buka lowongan Staf Akuntansi | Ada tautan publik yang berlaku 30 hari |
| J2 | Negatif | Buat tautan publik berlaku 999 hari | Ditolak (maksimal 180) |
| J3 | Periksa | Pelamar Ani | Melewati shortlist, wawancara selesai, penawaran terkirim lalu diterima, status akhir hired |
| J4 | Periksa | Pelamar Bayu | Shortlist lalu rejected |
| J5 | Periksa | Pelamar Citra | Tetap pending |
| J6 | Negatif | Lamar ke lowongan yang sudah ditutup | Ditolak |
| J7 | Negatif | Ubah status atau buat penawaran untuk lamaran yang tidak ada | Ditolak |

## K. Log aktivitas

| # | Jenis | Langkah | Hasil yang diharapkan |
| - | ----- | ------- | --------------------- |
| K1 | Positif | Log kunjungan Dedi | Dibuat, diubah, lalu di-submit |
| K2 | Negatif | Ubah log setelah di-submit | Ditolak |

## L. Hal yang tidak dicakup seeder (uji manual terpisah)

- Check-in dan check-out sungguhan dari halaman absensi saya (jam server, termasuk foto).
- Import Excel untuk karyawan, shift, departemen, jadwal kerja; unduh templat.
- Persetujuan berjenjang bila alur persetujuan diaktifkan di pengaturan.
- Notifikasi dan email.
- Peran dan izin: akses data rahasia karyawan saat `restrict_confidential_employee_data` aktif.

## Pencatatan temuan

Untuk tiap butir yang gagal, catat: nomor butir, data yang dipakai, hasil sebenarnya, hasil yang diharapkan, dan apakah sudah ada di daftar "TEMUAN" seeder.
Temuan seeder berprefix **DITOLAK/GAGAL** berarti panggilan yang mestinya sukses ditolak; **SEHARUSNYA DITOLAK** berarti validasi tidak menahan skenario negatif.
