---
title: (PT Medika Nusantara Sejahtera) — 29. Fitur Terbaru Lintas Modul
category: medika-nusantara-sejahtera
description: Kasus uji fitur terbaru - restoran real-time, jurnal manual aset tetap, baca suara dan diagram di Help, perbaikan kanvasing - dengan alasan tiap langkah.
visibility: internal
---

# 29. Fitur Terbaru Lintas Modul

> **Kenapa bagian ini diuji (bahasa sederhana).** Beberapa fitur baru tersebar di banyak modul. Kita kumpulkan di satu file supaya tidak ada yang
> terlewat, dan tiap langkah menjelaskan hal yang sedang kamu pastikan.
>
> **Kalau semuanya benar, artinya:** fitur baru bekerja di lingkungan nyata (bukan hanya di komputer pengembang) dan tidak merusak yang lama.

## A. Restoran dan Kafe: layar dapur yang berubah seketika

**Dikerjakan oleh:** kasir dan juru masak, memakai **dua perangkat atau dua jendela browser**. **Cabang aktif:** Kafe. **Prasyarat:** Reverb dan worker antrean jalan di server.

| # | Langkah | Kenapa kamu melakukan ini | Hasil yang diharapkan |
| ---: | --- | --- | --- |
| 1 | Perangkat 1: buka layar dapur (KDS). Perangkat 2: kasir membuat pesanan lalu kirim ke dapur | Dulu layar dapur menunggu hingga 15 detik; sekarang harus seketika | Pesanan muncul di KDS sekitar 1 detik tanpa menekan refresh |
| 2 | Di KDS ubah status item menjadi siap | Dapur memberi kabar ke kasir | Terminal kasir dan denah meja ikut berubah (lencana "siap diantar", warna meja) |
| 3 | Di denah meja, buat booking dari perangkat lain | Booking juga memicu pembaruan | Denah di perangkat pertama berubah tanpa refresh |
| 4 | Matikan Reverb sebentar (atau putuskan internet perangkat 1), buat pesanan baru, hidupkan lagi | Layar tidak boleh macet bila koneksi real-time putus | Layar tetap memperbarui diri berkala (maksimal sekitar 15 sampai 30 detik) lalu kembali seketika setelah tersambung |
| 5 | Buka Network di browser, perhatikan pesan real-time yang masuk | Isyarat tidak boleh membawa data pelanggan | Isinya hanya penanda "ada perubahan", tanpa isi pesanan |

## B. Aset Tetap: jurnal ditahan sampai ditinjau

**Dikerjakan oleh:** akuntan. **Prasyarat:** di `Client Master → Pengaturan Cabang`, ubah `fixed_asset_journal_mode` menjadi `manual` untuk cabang uji, dan nyalakan saklar jurnal perolehan.

| # | Langkah | Kenapa kamu melakukan ini | Hasil yang diharapkan |
| ---: | --- | --- | --- |
| 6 | Daftarkan aset baru bernilai Rp 12.000.000 | Mode manual berarti aset tercatat tetapi pembukuan menunggu | Aset tersimpan; **tidak ada** jurnal perolehan di Buku Besar |
| 7 | Di detail aset, tombol **Export To Journal** menyala; klik dan konfirmasi | Akuntan meninjau dulu lalu memposting | Jurnal perolehan terbentuk. Klik lagi: ditolak, jurnal tidak ganda |
| 8 | Jalankan **Run Depreciation** untuk bulan berjalan | Penyusutan juga ditahan | Baris penyusutan tercatat dan nilai buku turun, tetapi belum ter-posting; muncul tombol **Post to GL** per baris |
| 9 | Klik **Post to GL** pada satu baris | Memposting satu per satu | Baris itu berstatus ter-posting dan jurnalnya ada |
| 10 | Lepas aset (Dispose) dengan hasil penjualan | Pelepasan juga ditahan | Status aset berubah, jurnal pelepasan belum ada; kartu Disposal menunjukkan tombol posting |
| 11 | Post jurnal pelepasan | Menyelesaikan siklus | Biaya perolehan dan akumulasi penyusutan keluar dari pembukuan, hasil jual masuk, untung atau rugi tercatat |
| 12 | Kembalikan `fixed_asset_journal_mode` ke `auto`, daftarkan aset baru | Memastikan mode lama tidak berubah | Jurnal terbit seketika seperti biasa |
| 13 | Isi mode dengan tulisan asal (mis. `kadang`) | Salah ketik tidak boleh menahan jurnal diam-diam | Dianggap `auto` |

## C. Halaman Bantuan (Help): diagram dan baca suara

| # | Langkah | Kenapa kamu melakukan ini | Hasil yang diharapkan |
| ---: | --- | --- | --- |
| 14 | Buka `Bantuan`, bab berjudul "Diagram Alur ..." (mis. Accounting atau Rental) | Diagram dulu tampil sebagai teks kode | Semua diagram di halaman tampil sebagai **gambar**, tidak ada kotak kosong; ada tombol **Enlarge Diagram** |
| 15 | Klik Enlarge Diagram, lalu ganti tema gelap atau terang | Diagram besar harus terbaca di dua tema | Diagram ikut berubah warna dan tetap terbaca |
| 16 | Buka bab dengan banyak diagram (mis. Rental atau Purchasing) dan perhatikan semuanya | Dulu diagram saling menimpa | Semua diagram terisi |
| 17 | Klik **Read Aloud** | Membacakan bab untuk yang lebih suka mendengar | Suara Indonesia terdengar; paragraf yang dibaca tersorot |
| 18 | Klik sebuah paragraf saat membaca | Mulai dari tengah | Pembacaan lompat ke paragraf itu |
| 19 | Geser kecepatan dan volume saat membaca | Kenyamanan | Berlaku mulai kalimat berikutnya |
| 20 | Coba di perangkat lain atau browser lain | Suara bergantung perangkat | Jika perangkat tak punya suara Indonesia, muncul peringatan, bukan gagal diam-diam |

## D. Kanvasing dan lain-lain

| # | Langkah | Kenapa kamu melakukan ini | Hasil yang diharapkan |
| ---: | --- | --- | --- |
| 21 | Buka detail kunjungan yang belum selesai, klik **Batalkan** | Tombol ini sempat selalu gagal | Kunjungan berstatus Dibatalkan; kunjungan yang sudah selesai: tombol nonaktif dengan alasan |
| 22 | Buka rute yang sudah punya kunjungan, lihat tombol **Hapus** | Rute berkunjungan tidak boleh dihapus | Tombol nonaktif dengan tooltip alasan; rute kosong bisa dihapus |
| 23 | Buka detail karyawan, tab Pelanggaran | Sanksi kini tampil di sini | Daftar sanksi (nomor, tingkat, status) tampil; yang rahasia atau draf hanya untuk HR |
| 24 | Buka Ringkasan Pajak dan Rekonsiliasi Persediaan di dasbor Akuntansi | Dasbor tidak boleh berubah karena laporannya dipindah | Angka dasbor sama dengan sebelum dan sesudah |
