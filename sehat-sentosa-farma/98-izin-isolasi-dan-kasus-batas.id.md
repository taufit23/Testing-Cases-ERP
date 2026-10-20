---
title: (PT Sehat Sentosa Farma) — 98. Izin, Isolasi Data, Paket Langganan dan Kasus Batas
category: sehat-sentosa-farma
description: Kasus lintas modul yang tidak milik satu modul saja: izin per peran, isolasi antar klien dan cabang, fitur terkunci paket, penangguhan, angka batas, dan pola tampilan wajib.
visibility: internal
---

# 98. Izin, Isolasi Data, Paket Langganan dan Kasus Batas

> Prasyarat: alur `01` selesai sampai langkah 14 (ada dokumen di Pembelian, Persediaan, Penjualan, Keuangan). Kasus di sini ditulis tangan
> dan **tidak berasal dari Ollama**, karena menyangkut keamanan dan keputusan desain yang sudah ditetapkan.

## 1. Izin per peran

| Skenario | Detail | Hasil |
| --- | --- | --- |
| Positif — peran memegang izin | Staf Pembelian membuat PO, Kepala Gudang menerima barang, Manajer Keuangan menyetujui | Setiap aksi berhasil hanya untuk peran yang memegang izin aksi itu |
| Negatif — Kasir memanggil endpoint Pembelian | Panggil daftar PO dengan token Kasir | 403 "Access denied"; tidak ada data bocor |
| Negatif — role baru belum aktif | Tambahkan role Admin ke satu pengguna tanpa mengaktifkannya lalu buka halaman bermenu | Pengguna tidak memiliki izin sampai role diaktifkan lewat ganti role (Admin wajib PIN owner); tidak ada halaman setengah terbuka |
| Positif — tombol nonaktif bersyarat | Buka PO yang sudah punya GR sebagai Staf Pembelian | Tombol Edit terlihat **nonaktif dengan tooltip alasan**, bukan hilang; aksi tidak bisa dipicu lewat klik |
| Positif — override PIN rekan | Kasir meminta Apoteker memasukkan PIN untuk aksi yang butuh izin lebih tinggi | Aksi berjalan sekali dalam masa token; pencatatan penggunaan override tersimpan; PIN rekan yang rolenya tidak punya izin ditolak |
| Negatif — token override kedaluwarsa | Pakai token override setelah masa berlaku habis | Ditolak seperti tanpa izin |
| Netralisasi | Cabut role uji dan hapus token override | Pengguna kembali ke izin awal |

## 2. Isolasi antar klien dan antar cabang

| Skenario | Detail | Hasil |
| --- | --- | --- |
| Positif — klien kedua tidak melihat data klien pertama | Onboard klien pembanding, buat satu PO di sana, lalu buka daftar PO di PT Sehat Sentosa Farma | Daftar hanya memuat dokumen sendiri di semua modul |
| Negatif — baca dokumen klien lain lewat slug atau id | Panggil show dengan slug dokumen klien pembanding | Ditolak atau tidak ditemukan; tidak membocorkan keberadaan dokumen |
| Positif — cabang utama menggabung laporan | Di cabang Pusat aktifkan "sertakan cabang anak" pada laporan stok, laba rugi, Neraca | Angka gabungan = jumlah angka tiap cabang; cabang non-utama tidak punya opsi itu |
| Negatif — pengguna cabang Bandung membuka dokumen Pusat | Pakai tautan langsung dokumen Pusat | Ditolak, pesan jelas bahwa dokumen bukan milik cabang aktif |
| Positif — halaman publik per provider | Buka halaman karier provider A dan coba akses lowongan provider B lewat alamat A | Lowongan B tidak pernah muncul di halaman A |

## 3. Paket langganan dan fitur terkunci

| Skenario | Detail | Hasil |
| --- | --- | --- |
| Positif — paket memuat modul | Paket dengan Manufaktur dan Pertambangan | Menu dan endpoint kedua modul aktif |
| Negatif — modul tidak termasuk paket | Paket pembanding tanpa Pertambangan | Menu hilang, endpoint 403, dan halaman publik terkait menyatakan tidak tersedia |
| Negatif — fitur opsional tidak termasuk | Paket tanpa biaya logistik/landed cost, gateway cadangan, tata letak PDF, loyalitas, restoran lanjutan | Izin fitur dicabut: menu hilang dan endpoint 403; modul inti tetap jalan |
| Positif — batas angka paket | Isi karyawan melebihi batas paket | Penambahan ditolak dengan pesan batas paket, data lama tidak terhapus |
| Positif — penangguhan klien | Platform owner menangguhkan PT Sehat Sentosa Farma | Login dan semua API menjawab penangguhan, halaman publik (karier, penawaran, tautan bayar) tertutup; setelah dipulihkan semuanya kembali dan data utuh |

## 4. Kasus batas angka

| Skenario | Detail | Hasil |
| --- | --- | --- |
| Negatif — nominal di luar batas penyedia | QRIS di bawah minimum atau di atas maksimum penyedia | Ditolak sebelum memanggil penyedia, dengan pesan batas nominal |
| Negatif — penerimaan melebihi PO | GR OBT-001 3.000 padahal PO 2.000 | Ditolak dengan pesan sisa yang boleh diterima |
| Negatif — pembayaran melebihi faktur | Bayar Rp 20.000.000 pada faktur sisa 16.650.000 | Ditolak; pembayaran berjumlah tepat sisa diterima |
| Negatif — stok tidak cukup | Jual OBT-002 × 300 padahal stok Pusat 800 dan sudah terpesan 500 | Ditolak atau ditahan sesuai konfigurasi stok negatif |
| Negatif — jurnal tidak seimbang | Jurnal manual debit 1.000.000, kredit 900.000 | Tidak bisa diposting dan tidak masuk buku besar |
| Negatif — posting ke periode tertutup | Jurnal bertanggal periode September setelah ditutup | Ditolak; hanya lewat buka kembali periode atau penyesuaian bertanggal periode terbuka |
| Positif — pembulatan | Diskon persen pada banyak baris dengan PPN | Total dokumen = jumlah baris setelah pembulatan; jurnal seimbang |
| Negatif — webhook ganda | Kirim webhook "lunas" yang sama dua kali | Pembayaran dicatat sekali; webhook kedua tidak mengubah saldo |
| Negatif — webhook tanpa token | POST ke URL webhook tanpa header token atau token salah | Ditolak; tidak ada perubahan status |

## 5. Pola tampilan yang harus ada di semua halaman transaksi

| Skenario | Hasil |
| --- | --- |
| Halaman transaksi memakai kerangka dashboard dengan navbar; aksi simpan hanya di navbar | Tidak ada tombol aksi di bawah halaman |
| Simpan melewati validasi lalu **modal konfirmasi** lalu kirim | Modal punya deskripsi dan tombol rata kanan; tidak ada kirim langsung |
| Halaman daftar memakai tabel standar, kosong tetap menampilkan tabel dengan pesan kosong | Tidak ada daftar kartu manual |
| Halaman memuat dependensi: tampil spinner penuh sampai semua data siap | Tidak ada kilatan form kosong |
| Tombol refresh tersedia di navbar tiap halaman daftar dan detail | Data dimuat ulang tanpa memuat ulang halaman |
| Pilihan panjang (gudang, SKU, kontak, akun) dapat dicari | Tidak ada dropdown polos tanpa pencarian |
| Nominal memakai input mata uang; kuantitas memakai format kuantitas global | Tidak ada input angka polos untuk uang |
| Buat dokumen sukses lalu pindah ke halaman detail dokumen | Tidak kembali ke daftar |

## 6. Bahasa dan teks

| Skenario | Hasil |
| --- | --- |
| Ganti bahasa pengguna ke Inggris | Semua label, status (termasuk status dari master), header Excel dan PDF mengikuti bahasa; tidak ada kunci mentah tampil |
| Header template impor berbahasa Inggris diunggah ke pengguna berbahasa Indonesia | Impor tetap terbaca |
| Halaman publik dengan `?lang=` | Teks halaman (karier) memakai bahasa itu walau pengunjung belum login |
