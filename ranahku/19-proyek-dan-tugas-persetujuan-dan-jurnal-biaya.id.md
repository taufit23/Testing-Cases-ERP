---
title: Ranahku — Proyek dan Tugas (Persetujuan Lewat Alur Persetujuan dan Jurnal Biaya Tenaga Kerja)
description: Langkah uji persetujuan penutupan proyek, timesheet mingguan, dan change request lewat alur persetujuan, serta jurnal biaya tenaga kerja per catatan waktu yang disetujui.
---

# Ranahku — Proyek dan Tugas (Persetujuan dan Jurnal Biaya)

> Disusun 2026-10-08. **Letak dalam urutan kerja:** setelah berkas `18`. Prasyarat: berkas `12`–`18` selesai; seeder `ProjectCloseApprovalTemplateSeeder`, `ProjectTimesheetApprovalTemplateSeeder`, `ProjectChangeRequestApprovalTemplateSeeder` sudah dijalankan (`seed:all`); dua pengguna: pengaju dan penyetuju (pengguna kedua memegang izin persetujuan, bukan orang yang sama dengan pengaju); satu proyek aktif dengan beberapa tugas dan catatan waktu; kalender akuntansi aktif untuk bulan berjalan.

## PA1. Persetujuan penutupan proyek

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| PA1.1 | Pengaturan Proyek: biarkan "Penutupan proyek perlu persetujuan" mati. Pindahkan proyek aktif ke Selesai | Langsung Selesai, tanggal selesai aktual terisi (perilaku lama) | ⬜ |
| PA1.2 | Buka kembali proyek ke Aktif, nyalakan saklar persetujuan penutupan, simpan | Tersimpan | ⬜ |
| PA1.3 | Pindahkan proyek ke Selesai | Pesan "permintaan penutupan dikirim untuk disetujui"; status proyek TETAP Aktif; tanggal selesai aktual kosong; muncul tombol pintasan ke permintaan persetujuan di detail proyek | ⬜ |
| PA1.4 | Ulangi memindahkan ke Selesai saat permintaan masih menunggu | Ditolak: proyek sudah menunggu persetujuan penutupan; tombol Selesai nonaktif dengan penjelasan di opsi transisi | ⬜ |
| PA1.5 | Aturan lama tetap berlaku: proyek masih punya tugas terbuka dan pengaturan "blok" | Pengajuan ditolak sebelum permintaan dibuat | ⬜ |
| PA1.6 | Masuk sebagai penyetuju, buka antrean persetujuan, setujui semua tingkat | Proyek berubah ke Selesai, tanggal selesai aktual terisi, riwayat status mencatat perpindahan oleh sistem, notifikasi perubahan status terkirim | ⬜ |
| PA1.7 | Ulangi dengan proyek lain, tolak permintaannya | Proyek tetap Aktif; boleh diajukan lagi; tombol pintasan hilang setelah selesai diputuskan | ⬜ |
| PA1.8 | Hapus proyek yang punya permintaan menunggu (proyek tanpa tugas dan tanpa dokumen tertaut) | Terhapus; permintaan persetujuannya hilang dari antrean (tidak yatim) | ⬜ |
| PA1.9 | Hapus proyek yang masih punya pesanan penjualan, faktur pembelian, pengeluaran, atau biaya proyek tertaut | Ditolak dengan pesan harus dilepas tautannya dulu | ⬜ |
| PA1.10 | Cabang tanpa template persetujuan (hapus template, coba ajukan) | Ditolak dengan pesan alur persetujuan penutupan belum diatur; status tidak berubah | ⬜ |

## PA2. Persetujuan timesheet mingguan lewat alur persetujuan

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| PA2.1 | Nyalakan "Time entries need approval" dan biarkan "Timesheet per minggu lewat alur persetujuan" mati. Catat waktu, ajukan, setujui lewat tombol setujui | Perilaku lama: entri langsung disetujui oleh pengelola proyek | ⬜ |
| PA2.2 | Nyalakan saklar alur persetujuan. Catat 3 entri pada minggu lalu dan 1 entri pada dua minggu lalu, ajukan keempatnya | 2 pengajuan terbentuk (satu per minggu per karyawan); keempat entri berstatus Diajukan | ⬜ |
| PA2.3 | Pengelola proyek memakai tombol setujui langsung pada entri yang diajukan | Dilewati: tidak ada entri yang disetujui lewat jalur langsung | ⬜ |
| PA2.4 | Coba hapus salah satu entri yang menunggu | Ditolak: entri menunggu persetujuan timesheet | ⬜ |
| PA2.5 | Penyetuju menyetujui pengajuan minggu lalu (semua tingkat) | 3 entri jadi Disetujui, tarif tagih/biaya tercatat, jam terpakai tugas benar; entri minggu lainnya tetap Diajukan | ⬜ |
| PA2.6 | Penyetuju menolak pengajuan yang lain | Entri jadi Ditolak dengan alasan bawaan; jam terpakai tugas dihitung ulang (entri ditolak tidak dihitung) | ⬜ |
| PA2.7 | Perbaiki entri yang ditolak, ajukan lagi | Pengajuan baru dibuat (bukan yang lama); alur berjalan lagi | ⬜ |
| PA2.8 | Penyetuju meminta revisi pada satu pengajuan | Entri kembali ke Draf, bisa diedit | ⬜ |
| PA2.9 | Matikan "Time entries need approval" lalu catat waktu | Entri langsung Disetujui; alur persetujuan tidak dipakai | ⬜ |

## PA3. Persetujuan internal change request lewat alur persetujuan

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| PA3.1 | Saklar "Keputusan internal change request lewat alur persetujuan" mati; buat, ajukan, setujui lewat tombol Setujui | Perilaku lama berjalan | ⬜ |
| PA3.2 | Nyalakan saklar. Buat change request (jam +10, uang +100) dan ajukan | Status Diajukan; panel menampilkan tombol "Lihat permintaan persetujuan" menggantikan Setujui/Tolak | ⬜ |
| PA3.3 | Coba setujui/tolak lewat API langsung | Ditolak: diputuskan lewat alur persetujuan | ⬜ |
| PA3.4 | Penyetuju menyetujui semua tingkat | Status Disetujui; anggaran jam dan uang proyek bertambah sekali saja (bila "tambah ke anggaran" aktif); proyek harga tetap: nilai kontrak ikut bertambah | ⬜ |
| PA3.5 | Penyetuju menolak change request lain | Status Ditolak, catatan keputusan terisi | ⬜ |
| PA3.6 | Penyetuju meminta revisi | Kembali ke Draf, bisa diedit dan diajukan lagi | ⬜ |
| PA3.7 | Mode "keduanya" (internal + klien lewat portal): setujui internal lewat alur, setujui klien lewat portal | Disetujui hanya setelah KEDUA pihak setuju, urutan bebas | ⬜ |
| PA3.8 | Batalkan change request yang menunggu | Status Dibatalkan; permintaan persetujuan hilang dari antrean | ⬜ |

## PA4. Jurnal biaya tenaga kerja (K17)

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| PA4.1 | Saklar "Posting jurnal biaya tenaga kerja" mati; setujui entri waktu | Tidak ada jurnal | ⬜ |
| PA4.2 | Nyalakan saklar tanpa memetakan akun; setujui entri waktu | Tidak ada jurnal, tidak ada galat (dilewati bertahap) | ⬜ |
| PA4.3 | Kartu pemetaan akun, tekan "Auto map" | Dua fungsi terisi dari bagan akun standar (akun 5546 dan 5547 dibuat bila belum ada); pemetaan sendiri tidak ditimpa | ⬜ |
| PA4.4 | Setujui entri 2,5 jam dengan tarif biaya 40 | Satu jurnal seimbang: debit Biaya Tenaga Kerja Proyek 100 dan kredit Alokasi Biaya Tenaga Kerja Proyek 100; sumber jurnal = entri waktu; buku besar terisi | ⬜ |
| PA4.5 | Buka kembali entri itu | Jurnal dibalik (jurnal asli bertanda dibalik, ada jurnal pembalik); tidak ada jurnal berlaku untuk entri itu | ⬜ |
| PA4.6 | Ubah jam menjadi 3, ajukan dan setujui lagi | Jurnal baru bernilai 120; jurnal lama tetap dibalik | ⬜ |
| PA4.7 | Hapus entri yang sudah dijurnal (setelah dibuka kembali bila persetujuan diwajibkan) | Jurnalnya dibalik; entri terhapus | ⬜ |
| PA4.8 | Matikan persetujuan timesheet; catat waktu | Entri langsung Disetujui dan langsung dijurnal | ⬜ |
| PA4.9 | Tutup periode akuntansi bulan ini lalu setujui entri | Persetujuan TETAP berhasil; entri tercatat gagal dijurnal (tidak ada jurnal) | ⬜ |
| PA4.10 | Buka lagi periode, jalankan `php artisan projects:post-labor-journals --dry-run`, lalu tanpa `--dry-run` | Dry run menampilkan jumlah entri tanpa jurnal; pada run sungguhan jurnal terbentuk; dijalankan ulang tidak menggandakan | ⬜ |
| PA4.11 | Entri yang disetujui sebelum saklar dinyalakan | Tidak dijurnal otomatis; ikut terposting bila memakai opsi `--from=tanggal` | ⬜ |
| PA4.12 | Suspensi penyedia lalu jalankan perintah pemulihan | Cabang penyedia yang disuspensi dilewati | ⬜ |
| PA4.13 | Pengguna tanpa izin pemetaan akun membuka pengaturan Proyek | Kartu pemetaan menampilkan tombol nonaktif; tidak bisa menyimpan | ⬜ |

## Riwayat dan Lampiran

- Dokumen ini mencakup persetujuan lewat alur persetujuan dan jurnal biaya tenaga kerja. Tampilan tugas dibahas di berkas `20`; Git otomatis, portal, dan lintas modul di berkas `21`.
- Pengujian otomatis padanan: `ProjectsCloseApprovalTest`, `ProjectsWorkflowApprovalsTest`, `ProjectsLaborJournalTest`.

## Troubleshooting

| Gejala | Penyebab umum | Tindakan |
| --- | --- | --- |
| Pengajuan penutupan ditolak "alur persetujuan belum diatur" | Template persetujuan belum di-seed | Jalankan `seed:all`, ulangi |
| Penyetuju tidak melihat permintaan | Peran penyetuju tidak ada di langkah persetujuan cabang | Atur peran di pengaturan alur persetujuan cabang (modul Project Close / Timesheet / Change Request) |
| Jurnal tidak terbentuk padahal saklar nyala | Akun belum dipetakan atau tipe jurnal Persediaan belum ada di cabang | Lengkapi pemetaan; entri gagal diulang oleh perintah terjadwal harian |
| Tombol pemetaan nonaktif | Izin rute baru belum disinkronkan | Jalankan `permission:sync --all` dan beri izin ke role |
