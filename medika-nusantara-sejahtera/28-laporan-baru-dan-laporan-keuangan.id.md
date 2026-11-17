---
title: (PT Medika Nusantara Sejahtera) — 28. Laporan Baru dan Tampilan Baru Laporan Keuangan
category: medika-nusantara-sejahtera
description: Kasus uji laporan keuangan bertingkat (Laba Rugi, Neraca, Arus Kas) dan delapan laporan baru, dengan alasan tiap langkah.
visibility: internal
---

# 28. Laporan Baru dan Tampilan Baru Laporan Keuangan

> **Kenapa bagian ini diuji (bahasa sederhana).** Laporan adalah tempat pemilik usaha percaya atau tidak pada angka. Sebagian laporan keuangan
> baru saja dipindah ke tampilan yang sama dengan laporan lain, dan ada laporan baru untuk modul yang dulu belum punya. Yang kita pastikan: angkanya
> **sama persis** dengan transaksi sumbernya, dan hasil ekspor sama dengan layar.
>
> **Kalau semuanya benar, artinya:** kamu bisa membuka laporan apa pun dan menelusuri satu angkanya kembali ke dokumen aslinya.

**Dikerjakan oleh:** akuntan atau admin klien. **Prasyarat:** data transaksi Oktober dari file `01` sudah ada. **Cabang aktif:** Pusat.

## A. Laporan keuangan dengan tampilan baru

| # | Langkah | Kenapa kamu melakukan ini | Hasil yang diharapkan |
| ---: | --- | --- | --- |
| 1 | Buka `Laporan → Laporan Laba Rugi`, pilih **periode akuntansi** Oktober | Cara paling umum memilih periode | Bagian Pendapatan dan Beban tampil berjudul, tiap bagian punya baris total, lalu Laba Bersih |
| 2 | Kosongkan pilihan periode, isi tanggal awal dan akhir sendiri | Pilihan lain untuk rentang bebas | Angka mengikuti rentang tanggal. Bila periode dan tanggal sama-sama diisi, **periode yang dipakai** |
| 3 | Cocokkan Laba Bersih dengan hitungan file `01` | Angka acuan tidak boleh melenceng | Sama persis. Bila beda, catat sebagai temuan, jangan diubah |
| 4 | Buat satu jurnal masih Draf, muat ulang laporan | Laporan hanya memuat jurnal yang sudah diposting | Muncul pemberitahuan kuning bahwa ada jurnal belum diposting dan tidak ikut dihitung |
| 5 | Klik Ekspor PDF, lalu Ekspor Excel | Banyak orang menyerahkan laporan dalam bentuk berkas | Isi berkas sama dengan layar, lengkap dengan judul bagian dan total |
| 6 | Buka `Neraca`, pilih tanggal akhir Oktober | Neraca harus selalu seimbang | Aset sama dengan Liabilitas ditambah Ekuitas; muncul pemberitahuan hijau "seimbang" |
| 7 | Periksa baris **Laba Tahun Berjalan** di Ekuitas | Sebelum tutup tahun, laba belum masuk laba ditahan | Baris itu ada dan nilainya sama dengan Laba Bersih kumulatif |
| 8 | Buka `Laporan Arus Kas`, rentang Oktober | Arus kas menjawab "uangnya ke mana" | Tiga bagian (Operasi, Investasi, Pendanaan) lalu bagian posisi kas dengan Kas Akhir |
| 9 | Bandingkan Kas Akhir dengan saldo akun kas di Buku Besar | Dua jalan menuju angka yang sama | Cocok, dan muncul pemberitahuan "terekonsiliasi". Bila belum ada akun kas yang ditandai, muncul peringatan |
| 10 | Aktifkan **Sertakan cabang anak** (bila Pusat adalah cabang utama) | Laporan gabungan grup | Muncul pemberitahuan bahwa laporan menggabungkan beberapa cabang; akun digabung hanya bila kode dan nama sama persis |
| 11 | Buka `Rekonsiliasi Inventaris` | Nilai stok harus sama dengan saldo akun persediaan | Selisih tampil per cabang; selisih di atas Rp 0,50 berwarna merah. Cabang tanpa akun persediaan terpetakan diberi peringatan |
| 12 | Buka `Ringkasan Pajak` | Ringkasan PPN untuk dilaporkan | Satu tabel PPN Masukan dan Keluaran dengan kolom Jenis; total masukan, keluaran, dan hutang pajak bersih di kartu ringkasan |

## B. Laporan baru (cukup periksa bahwa hasilnya masuk akal dan bisa diekspor)

| # | Laporan | Kenapa ini berguna | Cara memeriksa |
| ---: | --- | --- | --- |
| 13 | **Kemajuan Proyek** | Melihat proyek mana yang terlambat atau tersendat | Cocokkan jumlah tugas terbuka dan terlambat dengan daftar tugas di modul Proyek; orang tanpa akses proyek tidak melihat proyek itu |
| 14 | **Beban Tugas** | Menyeimbangkan pekerjaan antar orang | Tugas tanpa penanggung jawab muncul di baris "Belum ditugaskan"; tugas selesai tidak dihitung |
| 15 | **Kecepatan Persetujuan** | Mencari dokumen yang tertahan di persetujuan | Ajukan satu PO, biarkan, lalu lihat umur permintaan tertua bertambah; setujui satu dan rata-rata jam terisi |
| 16 | **Kinerja Kampanye Outreach** | Membandingkan kampanye email | Jumlah terkirim, bounce, dan balasan cocok dengan halaman kampanye |
| 17 | **Penyelesaian Kerjasama** | Mengikuti uang dari perjanjian kerjasama | Total, dibayar, belum dibayar, dan lewat jatuh tempo cocok dengan rekap di modul Kerjasama |
| 18 | **Pemakaian Cuti** | Melihat pola cuti | Hari terpakai cocok dengan pengajuan yang disetujui; karyawan biasa hanya melihat barisnya sendiri |
| 19 | **Sebaran Skor KPI** | Membandingkan departemen | Lihat file `27`; hanya karyawan yang boleh kamu lihat yang dihitung |
| 20 | **Rekap Mutasi Stok** | Merekonsiliasi stok sebulan | Saldo awal + masuk − keluar + penyesuaian + transfer = saldo akhir untuk tiap SKU dan gudang |
| 21 | Untuk **semua** laporan di atas | Memastikan ekspor andal | Ekspor PDF dan Excel berhasil dan isinya sama dengan layar |

> Catatan penguji: Kecepatan Persetujuan, Kinerja Kampanye Outreach, dan Penyelesaian Kerjasama baru diuji otomatis bentuk datanya, belum angkanya pada data nyata.
> Perhatikan ketiganya dengan ekstra teliti dan catat selisih sekecil apa pun.
