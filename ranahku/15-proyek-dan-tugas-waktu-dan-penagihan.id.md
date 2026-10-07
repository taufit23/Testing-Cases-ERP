---
title: Ranahku — Proyek dan Tugas (Waktu, Biaya, Penagihan, F4)
description: Langkah uji tahap keempat modul Proyek dan Tugas: catatan waktu dan timer, persetujuan, peran dan kartu tarif, penagihan ke faktur draf, biaya, profitabilitas, dan alokasi sumber daya.
---

# Ranahku — Proyek dan Tugas (Waktu, Biaya, Penagihan, F4)

> Disusun 2026-10-10. **Letak dalam urutan kerja:** setelah berkas `14`. Prasyarat: berkas `12`–`14` selesai; ada proyek berklien dengan beberapa tugas dan minimal dua karyawan yang tertaut ke akun pengguna; izin "melihat tarif" hanya diberikan ke satu peran uji.

## BW1. Peran dan kartu tarif

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BW1.1 | **Proyek → Peran Proyek**: tambah "Developer" dan "Konsultan" | Muncul di daftar; hapus peran yang belum dipakai berhasil | ⬜ |
| BW1.2 | **Proyek → Kartu Tarif**: buat kartu cabang bawaan dengan baris peran Developer (tagih 100, biaya 60) | Tersimpan; membuat kartu bawaan kedua menjadikan yang pertama tidak bawaan | ⬜ |
| BW1.3 | Buat baris tanpa peran dan tanpa karyawan; buat kartu yang dimiliki klien sekaligus proyek | Ditolak dengan pesan | ⬜ |
| BW1.4 | Buat kartu klien (tarif Developer 120) lalu kartu proyek (karyawan A tarif 150) | Entri baru memakai tarif paling spesifik: proyek, klien, bawaan, tarif anggota, cadangan pengaturan | ⬜ |
| BW1.5 | Isi masa berlaku yang sudah lewat pada kartu proyek | Kartu itu diabaikan | ⬜ |
| BW1.6 | Login sebagai pengguna **tanpa** izin melihat tarif; buka detail proyek, anggota, dan catatan waktu | Tarif tagih/biaya, margin, dan tarif cadangan tidak tampil di mana pun | ⬜ |

## BW2. Catatan waktu dan timer

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BW2.1 | Di detail tugas isi 1,5 jam pada kartu **Catatan Waktu** | Entri muncul; "jam terpakai" tugas bertambah; entri dapat ditagih bila proyek berpenagihan | ⬜ |
| BW2.2 | Isi jam di proyek "tidak berpenagihan" | Entri tidak dapat ditagih secara bawaan | ⬜ |
| BW2.3 | Isi 25 jam, tanggal besok, atau total harian melewati batas | Ditolak dengan pesan (maks 24 jam, tanggal depan, batas harian) | ⬜ |
| BW2.4 | Atur pembulatan 15 menit, isi 1,1 jam | Tersimpan 1,25 jam | ⬜ |
| BW2.5 | Atur kunci mundur 7 hari, isi tanggal 10 hari lalu sebagai pengguna biasa | Ditolak (tanggal terkunci); pemegang "kelola semua proyek" boleh | ⬜ |
| BW2.6 | Tekan **Mulai timer** di tugas lain saat timer berjalan | Ditolak (sudah ada timer); navbar menampilkan waktu berjalan | ⬜ |
| BW2.7 | Tekan **Stop** | Entri tercatat sebesar waktu berjalan (dibulatkan); timer hilang | ⬜ |
| BW2.8 | Atur absensi menjadi "peringatan", catat jam melebihi jam hadir | Muncul peringatan, entri tetap tersimpan | ⬜ |
| BW2.9 | Hapus tugas yang punya entri waktu | Ditolak | ⬜ |

## BW3. Persetujuan

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BW3.1 | Aktifkan "entri waktu perlu persetujuan"; catat waktu | Status Draf; jam tetap dihitung di tugas | ⬜ |
| BW3.2 | Pilih entri, **Bulk Actions → Ajukan** | Status Diajukan | ⬜ |
| BW3.3 | Sebagai manajer proyek, **Tolak** tanpa alasan | Tombol konfirmasi nonaktif; dengan alasan berhasil, jam tidak lagi dihitung | ⬜ |
| BW3.4 | Ubah entri yang ditolak lalu ajukan ulang dan **Setujui** | Status Disetujui; tarif tagih/biaya terkunci pada entri | ⬜ |
| BW3.5 | Ubah tarif anggota setelah entri disetujui | Entri lama tidak berubah | ⬜ |
| BW3.6 | Ubah entri Disetujui langsung | Ditolak; **Buka kembali** mengembalikannya ke Draf | ⬜ |
| BW3.7 | Matikan "boleh menyetujui entri sendiri", setujui entri milik sendiri sebagai manajer biasa | Dilewati (tidak disetujui) | ⬜ |

## BW4. Penagihan

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BW4.1 | Proyek jenis **Waktu dan bahan**: catat beberapa entri disetujui, buka kartu **Keuangan Proyek**, **Pratinjau faktur** | Baris sesuai pengelompokan (per peran); entri tanpa tarif ditandai dilewati | ⬜ |
| BW4.2 | **Buat faktur draf**, buka faktur dari daftar | Faktur penjualan berstatus draft, bertanda proyek; entri berstatus Ditagih | ⬜ |
| BW4.3 | Buat faktur lagi | Ditolak (tidak ada yang bisa ditagih) | ⬜ |
| BW4.4 | Hapus entri yang sudah ditagih | Ditolak | ⬜ |
| BW4.5 | Hapus faktur draf | Entri kembali Belum ditagih dan bisa ditagih lagi | ⬜ |
| BW4.6 | Proyek **Milestone**: milestone dengan persen 30, tombol "Siap ditagih", buat faktur | Faktur 30% dari kontrak; milestone Ditagih dan tidak bisa dihapus | ⬜ |
| BW4.7 | Proyek **Harga tetap** kontrak 2.000: tagih 500, lalu tagih lagi tanpa jumlah | Faktur kedua 1.500; faktur ketiga ditolak | ⬜ |
| BW4.8 | Ubah jenis tagih proyek yang sudah berfaktur | Ditolak | ⬜ |
| BW4.9 | Proyek tanpa klien atau tidak berpenagihan | Pratinjau ditolak dengan pesan | ⬜ |

## BW5. Biaya dan profitabilitas

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BW5.1 | Tambah biaya lain "Lisensi 100" | Muncul di daftar biaya; masuk total biaya | ⬜ |
| BW5.2 | Lihat ringkasan: jam vs anggaran jam, biaya tenaga kerja, total biaya, margin | Angka cocok dengan perhitungan manual (jam x tarif biaya) | ⬜ |
| BW5.3 | Sebelum ada faktur | Margin ditandai perkiraan dari jam yang dapat ditagih; setelah faktur, berdasarkan faktur | ⬜ |
| BW5.4 | Hapus proyek yang punya faktur | Ditolak | ⬜ |

## BW6. Alokasi sumber daya

| # | Langkah | Hasil yang diharapkan | OK |
| --- | --- | --- | --- |
| BW6.1 | **Proyek → Alokasi Sumber Daya**, klik sel karyawan, isi proyek dan 8 jam | Sel menampilkan rencana/kapasitas; baris "tercatat" menunjukkan jam nyata | ⬜ |
| BW6.2 | Isi rencana melebihi kapasitas minggu itu | Tersimpan dengan peringatan; sel merah | ⬜ |
| BW6.3 | Karyawan dengan cuti disetujui di minggu itu | Kapasitas berkurang sesuai cuti dan hari libur | ⬜ |
| BW6.4 | Isi 0 jam | Alokasi terhapus | ⬜ |
| BW6.5 | Pengguna bukan manajer proyek mengubah alokasi | Ditolak | ⬜ |
