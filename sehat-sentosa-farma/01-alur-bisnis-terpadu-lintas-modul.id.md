---
title: (PT Sehat Sentosa Farma) — 01. Alur Bisnis Terpadu Lintas Modul (Oktober 2026)
category: sehat-sentosa-farma
description: 30 langkah berurutan yang melewati semua modul (platform owner sampai laporan) dengan angka acuan yang bisa dihitung ulang dan titik periksa di modul lain setelah tiap langkah.
visibility: internal
---

# 01. Alur Bisnis Terpadu Lintas Modul

> **Mulai dari berlangganan:** sebelum langkah 1, kerjakan [`00a`](./00a-perjalanan-berlangganan-klien.id.md) (landing page, formulir minat, onboarding, pembayaran, sampai login pertama klien). Langkah 1 di bawah adalah ringkasannya.
>
> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) selesai (provider, cabang, pengguna, master data acuan, saldo awal
> Bank Operasional dan Modal Pemilik masing-masing Rp 500.000.000). Kerjakan **berurutan**: langkah berikutnya memakai hasil langkah
> sebelumnya. Kolom **Periksa di modul lain** adalah inti suite ini: satu transaksi harus terlihat benar di tempat lain.
>
> **Asumsi hitung** (supaya angka bisa diperiksa tangan): PPN 11% dikenakan pada semua baris pembelian dan penjualan grosir; harga
> beli seperti tabel 3.2 file `00`; metode persediaan rata-rata; mode jurnal otomatis; persetujuan menyala hanya untuk Purchase Order
> di atas Rp 10.000.000 dan biaya di atas Rp 2.000.000. Bila konfigurasi cabang berbeda, catat selisihnya, jangan ubah angka acuan.

## A. Platform, akses dan konfigurasi (sebelum transaksi)

| # | Modul | Aksi | Hasil dan Periksa di modul lain |
| --- | --- | --- | --- |
| 1 | Platform Owner (rinci di `00a` S4 sampai S10) | Dari lead lewat Client Onboarding dan Provision untuk "PT Sehat Sentosa Farma" dengan paket yang memuat Pembelian, Persediaan, Penjualan, Kanvasing, POS, Restoran, Manufaktur, Pertambangan, Sewa, Akuntansi, Keuangan, Aset Tetap, SDM, Proyek | Provider dan cabang Pusat terbentuk; menu hanya menampilkan modul yang dibeli. **Periksa:** modul di luar paket (uji dengan paket pembanding) menghilang dari menu dan endpoint-nya 403 |
| 2 | Pengaturan Akun | Direktur masuk, ganti kata sandi awal, aktifkan 2FA, tambah 4 cabang lain dan 10 pengguna beserta peran (tabel peran file `00`) | Tiap pengguna hanya melihat cabang dan menu miliknya. **Periksa:** peran Kasir tidak bisa membuka Pembelian (403, tombol nonaktif bila ada di halaman bersama) |
| 3 | Konfigurasi Umum | Mata uang, pajak PPN 11%, gudang `WH-PST`/`WH-BDG`/`WH-SKB-RM`/`WH-SKB-FG`, metode pembayaran (Tunai, Transfer, QRIS), kategori produk, satuan, awalan nomor dokumen | Master tersedia di semua dropdown. **Periksa:** nomor dokumen memakai awalan dari pengaturan cabang, bukan teks tetap |
| 4 | Inti (Persetujuan) | Atur alur persetujuan PO > Rp 10.000.000 (Manajer Keuangan lalu Direktur) dan biaya > Rp 2.000.000 | Kedua modul menampilkan tombol pintas ke permintaan persetujuan. **Periksa:** menonaktifkan persetujuan membuat dokumen langsung berstatus disetujui saat diajukan |
| 5 | Akuntansi | Isi Chart of Accounts, tahun fiskal 2026 dengan 12 periode, unit bisnis per cabang, **saldo awal** 1 Okt (Bank Rp 500.000.000, Modal Rp 500.000.000) | Neraca Saldo seimbang pada Rp 500.000.000 per sisi. **Periksa:** laporan Neraca menampilkan Bank 500.000.000 dan Modal 500.000.000 |

## B. Pengadaan, persediaan dan distribusi (Pusat)

| # | Modul | Aksi | Hasil dan Periksa di modul lain |
| --- | --- | --- | --- |
| 6 | Pembelian | Permintaan Pembelian lalu Penawaran lalu **PO ke SUP-01**: OBT-001 × 2.000 @ 3.000 = 6.000.000; OBT-002 × 1.000 @ 9.000 = 9.000.000; PPN 1.650.000; **total 16.650.000** (di atas 10 juta: butuh persetujuan) | PO menunggu persetujuan; setelah disetujui Manajer Keuangan dan Direktur berstatus disetujui. **Periksa:** permintaan persetujuan tampil di Persetujuan dan tombol pintas di halaman PO aktif |
| 7 | Persediaan | **Goods Receipt** PO langkah 6 penuh ke `WH-PST` | Stok OBT-001 = 2.000, OBT-002 = 1.000; nilai persediaan 15.000.000. **Periksa:** jurnal GR (Dr Persediaan 15.000.000 / Cr barang diterima belum ditagih) dan Rekonsiliasi Persediaan nilai stok = saldo akun |
| 8 | Pembelian | **Purchase Invoice** dari GR langkah 7, jatuh tempo 14 hari | Utang Usaha 16.650.000 (termasuk PPN Masukan 1.650.000). **Periksa:** Laporan Umur Utang menampilkan SUP-01 belum jatuh tempo; PPN Masukan di Ringkasan Pajak |
| 9 | Pembelian | Pembelian alkes **SUP-02**: ALK-001 × 400 @ 25.000 = 10.000.000; PPN 1.100.000; total 11.100.000; GR, lalu invoice | Persediaan ALK-001 = 400. **Periksa:** total persediaan Pusat = 25.000.000; Utang Usaha total = 27.750.000 |
| 10 | Keuangan | Bayar invoice SUP-01 penuh 16.650.000 lewat **transfer bank** (pembayaran faktur) | Utang SUP-01 lunas. **Periksa:** Bank turun 16.650.000; umur utang SUP-01 hilang; status invoice lunas. Bayar **kurang** dari sisa harus menampilkan sisa, bayar **lebih** harus ditolak |
| 11 | Persediaan | **Transfer Stok** Pusat ke `WH-BDG`: OBT-001 × 500, OBT-002 × 200, ALK-001 × 100 | Stok Pusat: OBT-001 1.500, OBT-002 800, ALK-001 300; Bandung: 500, 200, 100. **Periksa:** nilai persediaan gabungan tidak berubah (hanya pindah gudang) |
| 12 | Penjualan | **Quotation lalu Sales Order ke CUS-01**: OBT-001 × 600 @ 4.500 = 2.700.000; ALK-001 × 100 @ 35.000 = 3.500.000; subtotal 6.200.000; PPN 682.000; **total 6.882.000** | Stok dipesan (reserved) 600 dan 100. **Periksa:** batas kredit CUS-01 (20 juta) cukup; pesanan di atas batas kredit harus ditolak atau ditahan sesuai konfigurasi |
| 13 | Penjualan | **Delivery** penuh lalu **Sales Invoice** | Stok Pusat: OBT-001 900, ALK-001 200. **Periksa:** HPP = 600 × 3.000 + 100 × 25.000 = **4.300.000**; Piutang 6.882.000; Pendapatan 6.200.000; Utang PPN 682.000; Laba kotor **1.900.000** |
| 14 | Keuangan | CUS-01 membayar 4.000.000 (sebagian) lewat **tautan pembayaran online** (QRIS sandbox) lalu sisanya tunai | Setelah webhook: pembayaran 4.000.000 tercatat; sisa piutang 2.882.000. **Periksa:** Umur Piutang CUS-01 = 2.882.000; faktur berstatus sebagian dibayar lalu lunas setelah sisa dibayar |

## C. Kanvasing, POS dan restoran

| # | Modul | Aksi | Hasil dan Periksa di modul lain |
| --- | --- | --- | --- |
| 15 | Kanvasing | Wilayah dan rute Bekasi; target bulanan Dewi; **titipan stok** 100 strip OBT-001 dari Pusat | Stok titipan tercatat atas nama Dewi. **Periksa:** stok gudang Pusat berkurang 100 dan muncul di Stok Titipan |
| 16 | Kanvasing | Kunjungan tak terjadwal ke calon pelanggan **Apotek Mitra Sehat** (check-in GPS), hasil "Tertarik", **konversi menjadi pelanggan** CUS-02, order lapangan 100 strip @ 4.500 = 450.000 | Calon berstatus Menang; kontak CUS-02 aktif; pesanan sumber kanvasing. **Periksa:** penagihan lapangan 450.000 tunai dan **setoran** tercatat; laporan realisasi target naik 450.000 |
| 17 | POS | **Buka sesi kas** kasir Rina di Apotek Bandung (modal Rp 200.000); jual OBT-001 × 50 @ 6.000 = 300.000 **tunai**; OBT-002 × 20 @ 15.000 = 300.000 lewat **QRIS** (sandbox, simulasikan bayar di dashboard penyedia) | Transaksi QRIS pending lalu lunas setelah webhook; layar pelanggan menampilkan QR. **Periksa:** stok `WH-BDG` OBT-001 450, OBT-002 180; obat keras tanpa resep ditolak bila fitur resep aktif |
| 18 | POS | Retur 5 strip OBT-001 (disetujui Apoteker), lalu **tutup sesi** dengan hitung pecahan | Selisih kas dihitung sesuai mode (ketat, toleransi, atau hanya catat). **Periksa:** jurnal tutup sesi (mode per sesi) dan stok OBT-001 Bandung 455 |
| 19 | Restoran | Kafe Sehat: 1 pesanan meja 4 (2 Teh Jahe @ 12.000 = 24.000), kirim ke dapur, **pisah tagihan** 2 orang, bayar QRIS | Tagihan terpisah dua; meja kembali kosong setelah bayar. **Periksa:** pendapatan kafe naik 24.000 (sebelum pajak sesuai konfigurasi) dan layar dapur menandai pesanan selesai |

## D. Produksi, tambang dan sewa

| # | Modul | Aksi | Hasil dan Periksa di modul lain |
| --- | --- | --- | --- |
| 20 | Pertambangan | CV Kapur Medika: pit "Bukit Kapur 1", **log produksi** 10 ton batu kapur ke stockpile, jual 5 ton ke Pabrik sebagai bahan baku | Stockpile 5 ton tersisa; produksi tidak boleh melebihi **batas cadangan pit** (uji dengan nilai berlebih: ditolak atau diperingatkan sesuai konfigurasi). **Periksa:** persediaan KAL-001 di `WH-SKB-RM` naik |
| 21 | Manufaktur | **BOM** Jamu Kunyit Asam (1 batch = 1.000 sachet: kunyit 20 kg × 10.000, asam 10 kg × 8.000, kemasan 1.000 × 100 = **380.000**); **Production Order 2 batch** | Persetujuan produksi bila menyala; bahan keluar, hasil 2.000 sachet masuk `WH-SKB-FG`. **Periksa:** biaya bahan 760.000; HPP per sachet **380**; bahan kurang menghalangi penyelesaian (kendali penyelesaian produksi) |
| 22 | Persediaan | Transfer 1.000 sachet HRB-001 ke Pusat; **stok opname** Bandung menemukan OBT-001 kurang 2 strip | Penyesuaian stok disetujui dan terjurnal. **Periksa:** persediaan Bandung turun 2 × 3.000 = 6.000; Rekonsiliasi Persediaan tetap cocok |
| 23 | Sewa | **Sewa Kursi Roda** 3 unit × 7 hari @ 15.000 = 315.000, deposit 3 × 100.000 = 300.000; kembali dengan kerusakan ringan **denda 50.000** dipotong deposit | Pesanan sewa aktif lalu selesai; deposit kembali 250.000. **Periksa:** jurnal deposit (Dr Bank 300.000 / Cr Utang deposit) lalu pelepasan: kas keluar 250.000, pendapatan denda 50.000, pendapatan sewa 315.000 |

## E. SDM, proyek, aset dan keuangan

| # | Modul | Aksi | Hasil dan Periksa di modul lain |
| --- | --- | --- | --- |
| 24 | SDM | Buat lowongan "Apoteker Pendamping" dan **tayangkan di halaman karier**; pelamar mengirim lamaran dengan CV dari halaman publik | Lamaran masuk berstatus awal dengan sumber halaman karier dan CV sebagai lampiran privat. **Periksa:** lamaran sama dari email sama ditolak; kolom jebakan tidak membuat lamaran |
| 25 | SDM | Karyawan baru: Apoteker (gaji pokok 8.000.000) dan Kasir (4.500.000); shift pagi; absensi satu bulan dengan toleransi terlambat 10 menit; **proses payroll Oktober** | Slip gaji per karyawan; periode gaji berstatus draf, diproses, disetujui, dibayar. **Periksa:** jurnal gaji (Beban Gaji / Utang Gaji) lalu pembayaran; slip hanya terlihat pemiliknya; PTKP kosong menolak proses |
| 26 | Proyek dan Tugas | Proyek "Akreditasi Klinik Bekasi": 5 tugas, timesheet, **change request** | Persetujuan timesheet dan change request lewat alur persetujuan bila menyala. **Periksa:** biaya tenaga kerja proyek terjurnal bila saklarnya menyala; tombol "buat tugas dari dokumen" tersedia di PO, SO, produksi dan sewa |
| 27 | Aset Tetap | Beli autoclave Rp 60.000.000 (5 tahun, garis lurus, nilai sisa 0); jalankan penyusutan Oktober | Penyusutan **1.000.000** per bulan. **Periksa:** jurnal akuisisi bila saklar menyala (Dr Aset / Cr Bank 60.000.000); jurnal penyusutan (Dr Beban Penyusutan / Cr Akumulasi); pelepasan tidak membuat akun aset negatif |
| 28 | Keuangan | Catat **biaya listrik** Rp 2.500.000 kategori Listrik (di atas 2 juta: butuh persetujuan), bayar lewat **bank transfer payout** (sandbox) | Biaya menunggu persetujuan lalu disetujui dan dibayar. **Periksa:** jurnal biaya (Dr Beban Listrik / Cr Utang Biaya) lalu pembayaran (Cr Bank) |

## F. Penutupan, laporan dan lintas fitur

| # | Modul | Aksi | Hasil dan Periksa di modul lain |
| --- | --- | --- | --- |
| 29 | Akuntansi dan Laporan | **Rekonsiliasi bank**; **rekonsiliasi persediaan**; Neraca Saldo, Laba Rugi, Neraca, Arus Kas, Ringkasan Pajak, Anggaran vs Aktual; tutup periode Oktober | Neraca Saldo seimbang; Laba Rugi = pendapatan − HPP − beban; Neraca seimbang. **Periksa:** Ringkasan Pajak: PPN Keluaran 682.000 (+ transaksi lain), PPN Masukan 2.750.000; jurnal draf tidak ikut terhitung; Anggaran vs Aktual tetap terbaca setelah tutup tahun uji |
| 30 | Dashboard, AI dan halaman publik | Dasbor keuangan, penjualan, pembelian, operasional, SDM; tanya Asisten AI "berapa stok Paracetamol di Pusat?" (jawaban **800**: 1.500 setelah transfer, dikurangi 600 terjual dan 100 titipan kanvasing) dan minta draf PO; buka tautan penawaran publik dan halaman karier tanpa login | Angka dasbor cocok dengan laporan. **Periksa:** AI memberi kartu aksi yang dikonfirmasi pengguna (tidak mengeksekusi sendiri); halaman publik tidak membocorkan data internal; penangguhan klien menutup halaman publik dan API |

## G. Skenario khas grup kesehatan (menguji kebutuhan bisnis, bukan menu)

Langkah 31 sampai 40 berasal dari kebutuhan bisnis kesehatan ([`96`](./96-riset-kebutuhan-bisnis-grup-kesehatan.id.md)). Bagian ini **sengaja menyentuh hal yang mungkin belum ada**:
bila fiturnya tidak ada, catat sebagai celah (nomor celah di kolom terakhir, daftar di [`95`](./95-daftar-celah-dan-usulan-perbaikan.id.md)) dan lanjut ke langkah berikutnya. Rincian dan
hasil harapan tiap langkah ada di [`21`](./21-kebutuhan-bisnis-kesehatan-dan-uji-celah.id.md).

| # | Modul | Aksi | Hasil yang diharapkan dari ERP yang matang | Celah bila belum ada |
| --- | --- | --- | --- | --- |
| 31 | Persediaan | Terima ulang OBT-001 dengan dua batch berbeda kedaluwarsa (21 A1), lalu jual 600 strip tanpa memilih batch | FEFO: batch dengan kedaluwarsa lebih dekat keluar dulu; stok per batch benar | G02 |
| 32 | Persediaan | Majukan tanggal melewati kedaluwarsa satu batch, lalu jual atau transfer batch itu | Lot otomatis kedaluwarsa dan diblokir; peringatan kedaluwarsa muncul sebelumnya | G01, G02 |
| 33 | Penjualan dan Persediaan | BPOM menarik satu batch: cari semua pelanggan penerimanya dan buat retur | Laporan penelusuran batch ke pelanggan; retur massal | G03 |
| 34 | POS | Jual obat keras (OBT-002) di Apotek Bandung dengan resep dokter; lalu coba tanpa resep | Dengan resep: tercatat dokter, pasien, aturan pakai; tanpa resep: ditolak atau perlu persetujuan Apoteker | G05, G06 |
| 35 | Persediaan | Satu bulan mutasi obat terkontrol uji | Laporan mutasi per produk siap disalin ke SIPNAP | G08 |
| 36 | Pembelian | Input dua kali faktur PBF dengan nomor pemasok yang sama | Peringatan faktur ganda | G31 |
| 37 | SDM | Karyawan apoteker dengan STR yang tinggal 30 hari | Peringatan perpanjangan; tidak bisa dijadwalkan setelah kedaluwarsa | G23 |
| 38 | Klinik (POS jasa sebagai jalan pintas) | Pasien baru mendaftar, konsultasi dokter, tindakan, resep, bayar | Idealnya kunjungan satu tagihan dengan tarif sesuai penjamin; di aplikasi sekarang hanya kasir biasa | G15, G18 |
| 39 | Klinik dan Keuangan | Jasa medis dokter bulan Oktober dari tindakan dan konsultasi | Perhitungan otomatis, hutang jasa, pembayaran dan PPh 21 | G19 |
| 40 | Manufaktur | Produksi 2 batch Jamu Kunyit Asam dengan catatan lot bahan dan penahanan sampai QC melepas | Batch record lengkap, barang jadi karantina sampai dilepas, penelusuran bahan baku ke batch | G26, G03 |

## Hubungan angka yang harus selalu benar

1. **Persediaan akhir di buku besar = nilai stok** di Rekonsiliasi Persediaan (selisih nol, selain koreksi yang terjurnal).
2. **Utang Usaha** = faktur pembelian belum lunas (langkah 8, 9, 10) = Laporan Umur Utang.
3. **Piutang Usaha** = faktur penjualan belum lunas = Laporan Umur Piutang (langkah 13 dan 14).
4. **PPN Keluaran − PPN Masukan** pada Ringkasan Pajak = saldo akun PPN di buku besar.
5. **Neraca Saldo** seimbang di setiap langkah; jurnal draf atau menunggu tinjauan tidak ikut terhitung.
6. **Kas fisik POS** = modal sesi + penjualan tunai − retur tunai − selisih yang dicatat.

## Netralisasi

Untuk mengulang dari awal pada database uji: jalankan ulang seeder cabang uji atau pakai salinan `erp_scratch`. Jangan menghapus dokumen
bertransaksi lewat antarmuka (dokumen yang sudah berjurnal dilindungi); pakai pembalikan jurnal, retur, atau pembatalan sesuai modul.
