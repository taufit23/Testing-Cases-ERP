---
title: Ranahku — Siklus Bisnis Penuh dan Uji Prinsip
description: Membawa global-testing/GLOBAL.md (77 bagian) ke Ranahku: siklus beli-bayar, jual-terima, persediaan, karyawan-gaji, restoran, aset; kasus keuangan (pinjaman karyawan, beban dibayar dimuka, akrual, kredit pelanggan/pemasok, pembayaran sebagian dan ganda, jatuh tempo); simulasi hari perusahaan; rantai penuh pelanggan/pemasok/karyawan; serta uji prinsip ("satu rupiah", "satu transaksi", "tidak ada uang muncul dari ketiadaan") dan uji peran (pemilik, keuangan, auditor).
---

# Ranahku — Siklus Bisnis Penuh dan Uji Prinsip

> Disusun 2026-10-07 dari `global-testing/GLOBAL.md`. Tujuan: menguji apakah semua modul bekerja sebagai **satu sistem perusahaan**, bukan kumpulan aplikasi yang berdiri
> sendiri. Pertanyaan utama setiap tahap:
>
> > **Apakah satu aktivitas bisnis dapat berjalan dari awal sampai akhir tanpa menghasilkan informasi yang saling bertentangan antar modul?**
>
> Berkas ini dikerjakan **terakhir**, setelah 01–06 (master data, transaksi, modul lanjutan, akuntansi mendalam, kasus per modul), karena memakai dokumen dan
> angka yang sudah ada. Setiap tahap punya kolom **Bukti** (angka yang dibandingkan) dan **OK**.
>
> **Aturan emas penguji:** bila satu angka tidak bisa dijelaskan asalnya, catat sebagai gap — jangan menyimpulkan "mungkin benar".

## Ringkasan Tahap

| # | Tahap | Isi |
| --- | --- | --- |
| AW | Enam siklus bisnis utama | Pembelian ke pembayaran, penjualan ke penerimaan kas, persediaan, karyawan ke gaji, restoran, aset tetap |
| AX | Kasus keuangan lintas modul | Selisih pembelian, diskon, retur, uang muka pemasok, pinjaman karyawan, beban dibayar dimuka, akrual, kredit, pembayaran sebagian dan ganda, jatuh tempo, kas |
| AY | Penyesuaian, periode, mundur tanggal, banyak titik, unit biaya, proyek | Jurnal penyesuaian, tutup periode, backdate, multi outlet, cost center, proyek pendampingan, profitabilitas |
| AZ | Simulasi satu hari perusahaan dan rantai penuh | Satu hari dari buka toko sampai tutup buku; rantai pelanggan, pemasok, karyawan, restoran, persediaan; rekonsiliasi |
| BA | Uji prinsip | Mengapa, mundur, satu transaksi, satu rupiah, satu barang, satu pelanggan, satu pemasok, satu karyawan, tidak ada data/uang/stok hilang atau muncul |
| BB | Uji peran dan titik periksa akhir | Pemilik, keuangan, auditor, titik periksa akhir ERP |

---

## TAHAP AW — Enam Siklus Bisnis Utama

### AW-1. Pembelian ke pembayaran (Procure to Pay)

Satu kasus besar: **Ranahku membeli 200 karung Beras Premium dari CV Grosir Sembako Makmur @ 62.000, termin 21 hari.**

| Langkah | Aksi | Bukti yang dibandingkan | OK |
| --- | --- | --- | --- |
| 1 PO | Buat PR → PO, disetujui sesuai ambang | Nilai PO 12.400.000 + PPN 1.364.000 = 13.764.000; PO belum mengubah stok maupun jurnal | ⬜ |
| 2 Barang datang | Goods Receipt 200 karung | Stok `Gudang Toko Retail` +200; nilai persediaan +12.400.000; kewajiban sementara (GR/IR) tercatat bila alur GR duluan | ⬜ |
| 3 Faktur pemasok | Purchase Invoice 13.764.000 | Utang Usaha `2-101` +13.764.000; PPN Masukan `1-160` +1.364.000; GR/IR nol | ⬜ |
| 4 Pembayaran | Payment Bill pada hari ke-21 | Utang nol; Bank −13.764.000; pemasok tidak lagi ada di umur utang | ⬜ |
| Penutup | Telusuri mundur dari pembayaran ke PR | Setiap mata rantai ditemukan tanpa bertanya orang | ⬜ |

### AW-2. Penjualan ke penerimaan kas (Order to Cash)

**Ranahku menjual 100 karung Beras ke Toko Bangunan Sumber Rejeki @ 72.000, tempo 14 hari.**

| Langkah | Aksi | Bukti | OK |
| --- | --- | --- | --- |
| 1 SO | SO 100 karung | Nilai 7.200.000 + PPN 792.000 = 7.992.000; stok dicadangkan, belum berkurang | ⬜ |
| 2 Delivery | Kirim 100 | Stok −100; HPP = 100 × 62.000 = 6.200.000 (`5-201` +, `1-130` −) | ⬜ |
| 3 Faktur | Sales Invoice | Piutang +7.992.000; Pendapatan Toko `4-201` +7.200.000; PPN Keluaran +792.000 | ⬜ |
| 4 Terima kas | Payment Bill | Bank +7.992.000; piutang nol | ⬜ |
| Penutup | Laba kotor transaksi | 7.200.000 − 6.200.000 = **1.000.000**, sama di laporan laba rugi per kegiatan RETAIL | ⬜ |

### AW-3. Siklus persediaan

| Aksi | Bukti | OK |
| --- | --- | --- |
| Terima barang → transfer ke gudang lain → jual → retur → opname → penyesuaian | Kartu stok (Stock History) menunjukkan setiap perubahan dengan dokumen asalnya; jumlah akhir = hitungan fisik setelah penyesuaian | ⬜ |
| Nilai persediaan | Nilai di laporan persediaan = saldo `1-130` + `1-131` di Neraca | ⬜ |

### AW-4. Karyawan ke gaji (Employee to Payroll)

| Aksi | Bukti | OK |
| --- | --- | --- |
| Karyawan baru → jadwal → absen selama bulan → cuti → lembur → payroll → slip → pembayaran gaji | Slip gaji = gaji pokok + tunjangan + lembur + komisi − potongan; total semua slip = jurnal gaji (`6-101`, `2-122`, `2-131`, Bank) | ⬜ |
| Karyawan melihat slipnya sendiri | Hanya data miliknya; HR melihat semua dengan izin data rahasia | ⬜ |

### AW-5. Siklus rumah makan

| Aksi | Bukti | OK |
| --- | --- | --- |
| Reservasi → meja → pesan → dapur → saji → bayar → tutup meja → stok bahan | Penjualan `4-301`, PB1 `2-121`, HPP bahan `5-301` dan stok `1-131` semua berubah konsisten; tidak ada meja tersangkut | ⬜ |

### AW-6. Siklus aset tetap

| Aksi | Bukti | OK |
| --- | --- | --- |
| Beli → daftarkan → susutkan bulanan → rusak/jual → lepas | Nilai buku = perolehan − akumulasi; jurnal pelepasan menutup akun aset dan akumulasi; laba/rugi pelepasan tampil di laba rugi | ⬜ |

---

## TAHAP AX — Kasus Keuangan Lintas Modul

| # | Kasus | Contoh Ranahku | Bukti / yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AX1 | Pembelian dengan selisih | PO 100 dus Teh Kotak datang 95 dus; faktur untuk 100 | Selisih 5 dus terlihat; faktur tidak bisa dibayar penuh tanpa pemeriksaan; tindak lanjut tercatat | ⬜ |
| AX2 | Pembelian dengan diskon | Diskon pemasok 5% pada faktur | Persediaan masuk pada nilai neto; PPN masukan dari DPP neto; utang = neto + PPN | ⬜ |
| AX3 | Retur pembelian | Retur 5 dus rusak | Stok turun, utang turun, PPN masukan turun; jurnal pembalik rapi | ⬜ |
| AX4 | Uang muka pemasok | Bayar DP 2.000.000 ke CV Grosir sebelum barang datang | DP tampil sebagai uang muka (aset), bukan beban; terpotong saat faktur; sisa DP bisa ditagih kembali | ⬜ |
| AX5 | Penjualan tunai | Pembeli membeli di kasir | Tidak ada piutang; kas bertambah; PPN keluaran | ⬜ |
| AX6 | Penjualan POS dan restoran | Satu hari penjualan kasir dan restoran | Kas laci, QRIS, pajak (PPN dan PB1), HPP semua cocok dengan tutup sesi | ⬜ |
| AX7 | Pemborosan dapur | Catat sisa makanan 1 kg ayam | Stok bahan turun; beban kerugian; tidak masuk HPP penjualan | ⬜ |
| AX8 | Pinjaman karyawan | Kasbon 1.000.000 dipotong 4 kali | Piutang karyawan 1.000.000 turun 250.000 per slip; saldo akhir nol; tidak ada potongan setelah lunas | ⬜ |
| AX9 | Penggantian biaya karyawan | Reimburse biaya parkir kanvasing 80.000 | Beban `6-105` bertambah; kas keluar; bukti terlampir | ⬜ |
| AX10 | Beban operasional | Bayar internet bulanan 600.000 | Beban `6-104`; tanggal dan periode benar | ⬜ |
| AX11 | Beban dibayar dimuka | Asuransi toko setahun 2.400.000 | Awalnya aset; dibebankan 200.000 per bulan; saldo aset menurun | ⬜ |
| AX12 | Akrual | Listrik September ditagih Oktober: jurnal akrual 700.000 | Beban September mencakup 700.000; saat tagihan datang utang akrual dilunasi, bukan beban ganda | ⬜ |
| AX13 | Kredit pelanggan | Batas kredit Distributor 20.000.000 | SO yang melewati batas diperingatkan/ditahan; saldo piutang + SO terbuka dihitung | ⬜ |
| AX14 | Kredit pemasok | Batas pembelian kredit dari CV Grosir | Informasi hutang berjalan terlihat sebelum PO baru | ⬜ |
| AX15 | Pembayaran sebagian | Pelanggan bayar 60% faktur | Sisa 40% tetap piutang; faktur berstatus sebagian | ⬜ |
| AX16 | Satu pembayaran beberapa faktur | Distributor membayar tiga faktur sekaligus | Alokasi per faktur jelas; total kas = jumlah alokasi; sisa lebih bayar sebagai titipan | ⬜ |
| AX17 | Pembayaran terlambat | Faktur jatuh tempo lewat | Umur piutang menampilkan kelompok telat; tidak ada denda otomatis kecuali diatur | ⬜ |
| AX18 | Pelanggan menunggak | Tunggakan 2 bulan | Dapat dilihat dalam satu layar; riwayat penagihan | ⬜ |
| AX19 | Pemasok jatuh tempo | Utang akan jatuh tempo minggu depan | Daftar utang jatuh tempo; prioritas pembayaran jelas | ⬜ |
| AX20 | Manajemen kas | Kas kecil, kas toko, kas rumah makan, bank | Saldo tiap rekening kas jelas; total kas = laporan arus kas | ⬜ |
| AX21 | Selisih kas | Kas fisik berbeda dengan sistem | Selisih tercatat dengan penjelasan (lihat AI29, AS23) | ⬜ |
| AX22 | Pajak | Rekap PPN, PB1, PPh 21, PPh 23 | Selaras dengan Tahap AP; sisa utang pajak benar | ⬜ |

---

## TAHAP AY — Penyesuaian, Periode, Mundur Tanggal, Banyak Titik, Unit Biaya, Proyek

| # | Kasus | Contoh Ranahku | Bukti / yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AY1 | Jurnal penyesuaian | Koreksi salah akun biaya via Reverse + jurnal baru | Jejak: asli → pembalik → baru; tidak ada penghapusan diam-diam | ⬜ |
| AY2 | Tutup periode | Tutup Agustus (lihat AK2) | Transaksi baru ke Agustus ditolak; laporan Agustus stabil | ⬜ |
| AY3 | Mundur tanggal | Catat transaksi bertanggal 28 Agustus di bulan September | Dibolehkan hanya bila periode terbuka; laporan Agustus berubah hanya bila periode belum ditutup | ⬜ |
| AY4 | Banyak titik jual | Kasir toko, kasir rumah makan, meja sewa | Tiap titik punya kas dan laporan sendiri; konsolidasi benar | ⬜ |
| AY5 | Pusat biaya | Cost Center "Kantor", "Toko", "Dapur" ditempel di beban | Laporan beban per pusat biaya; total sama dengan akun beban | ⬜ |
| AY6 | Proyek pendampingan | Satu klien baru: pendampingan 5 hari dengan biaya perjalanan | Biaya (transport, upah) dan pendapatan (`4-102`) bisa dikaitkan ke satu proyek/kegiatan | ⬜ |
| AY7 | Pembelian ke proyek | Beli tablet untuk pendampingan | Biaya dibebankan ke proyek atau kegiatan SEWA | ⬜ |
| AY8 | Penjualan ke proyek | Faktur pendampingan ke klien | Pendapatan dikaitkan ke proyek yang sama | ⬜ |
| AY9 | Profitabilitas | Laba per kegiatan (SEWA/RETAIL/RESTO), per pelanggan, per produk | Angka laba kegiatan = pendapatan − HPP − beban langsung dan alokasi; konsisten antar laporan | ⬜ |

---

## TAHAP AZ — Simulasi Satu Hari dan Rantai Penuh

### AZ-1. Simulasi hari perusahaan (Senin, 21 September 2026)

Urutan, semuanya dalam satu hari:

1. 07.30 Karyawan absen; satu terlambat.
2. 08.00 Buka sesi kasir toko dan rumah makan; gudang menerima kiriman beras dari CV Grosir.
3. 09.00 Kanvasing: Petugas menutup satu kontrak sewa Paket Usaha dengan bayar tunai bulan pertama.
4. 10.00 Penjualan toko: 12 transaksi, satu retur kecil.
5. 11.30 Rumah makan: reservasi meja dan 18 pesanan, dua pembayaran QRIS, satu void.
6. 13.00 Penagihan kantor: pelanggan bayar sebagian faktur sewa.
7. 14.00 Pembelian bahan segar tunai dari UD Pasar Segar.
8. 16.00 Transfer 20 Kopi Sachet dari toko ke dapur.
9. 18.00 Tutup rumah makan; catat pemborosan.
10. 20.00 Tutup sesi kasir toko; setor kas ke bank.
11. 21.00 Periksa laporan harian.

| # | Pemeriksaan akhir hari | Bukti | OK |
| --- | --- | --- | --- |
| AZ1 | Total penjualan hari itu | Σ sesi toko + rumah makan + sewa = pendapatan hari itu di Laba Rugi | ⬜ |
| AZ2 | Kas | Σ kas laci + bank bergerak = arus kas hari itu | ⬜ |
| AZ3 | Stok | Stok akhir = stok awal + masuk − keluar; nilai sama dengan Neraca | ⬜ |
| AZ4 | Piutang dan utang | Mutasi piutang dan utang sesuai dokumen hari itu | ⬜ |
| AZ5 | Pajak | PPN, PB1 hari itu sesuai transaksi | ⬜ |
| AZ6 | Absensi | Karyawan terlambat terlihat di rekap | ⬜ |
| AZ7 | Neraca saldo | Seimbang pada akhir hari | ⬜ |

### AZ-2. Rantai penuh

| # | Rantai | Cara uji | Bukti | OK |
| --- | --- | --- | --- | --- |
| AZ8 | Bisnis penuh | Dari penawaran sampai laporan keuangan untuk satu pelanggan sewa | Quotation → SO → faktur → bayar → jurnal → Laba Rugi → Neraca | ⬜ |
| AZ9 | Pelanggan penuh | Ambil Apotek Sehat Bersama | Total pembelian, piutang, faktur belum dibayar, retur, diskon, riwayat pembayaran, batas kredit, profitabilitas — semua dari satu kartu | ⬜ |
| AZ10 | Pemasok penuh | Ambil CV Grosir Sembako Makmur | Total pembelian, utang, faktur belum dibayar, retur, harga terakhir, ketepatan pengiriman | ⬜ |
| AZ11 | Karyawan penuh | Ambil satu kasir | Data, jadwal, absen, cuti, lembur, slip gaji, pinjaman, penilaian, riwayat jabatan | ⬜ |
| AZ12 | Restoran penuh | Dari reservasi sampai laporan menu | Reservasi → pesanan → dapur → bayar → stok bahan → laporan margin menu | ⬜ |
| AZ13 | Persediaan penuh | Satu barang dari pembelian sampai penjualan, retur, opname | Kartu stok lengkap dan nilainya benar | ⬜ |
| AZ14 | Rekonsiliasi akuntansi | Bandingkan: stok vs `1-130`, piutang vs `1-120`, utang vs `2-101`, kas vs `1-10x`, pajak vs akun pajak | Selisih nol atau dapat dijelaskan | ⬜ |

---

## TAHAP BA — Uji Prinsip

Kerjakan setelah AZ. Tiap uji memaksa sistem **menjelaskan dirinya**.

| # | Uji | Cara | Lulus bila | OK |
| --- | --- | --- | --- | --- |
| BA1 | **"Mengapa"** | Ambil angka pendapatan September; tanya kenapa | Bisa dipecah ke pelanggan, faktur, produk, kegiatan, pembayaran, biaya, stok keluar, laba | ⬜ |
| BA2 | **"Mundur"** (Reverse) | Dari Laba Rugi, klik beban `6-101` Rp 20.000.000, telusuri ke jurnal, payroll, karyawan | Setiap angka bisa ditelusuri sampai dokumen sumber; arah sebaliknya pun sama | ⬜ |
| BA3 | **"Satu transaksi"** | Pilih satu faktur secara acak | Customer → SO → delivery → stok → faktur → bayar → jurnal bisa dijelaskan seluruhnya | ⬜ |
| BA4 | **"Satu rupiah"** | Ambil Rp 1 dari penerimaan kas | Dapat ditelusuri: pembayaran → faktur → penjualan → produk → stok → pembelian → pemasok → biaya | ⬜ |
| BA5 | **"Satu barang"** | Ambil Kopi Sachet | Dibeli dari siapa, berapa harga, diterima berapa, masuk gudang mana, dipindah berapa, dijual berapa, terbuang berapa, sisa berapa, nilai berapa | ⬜ |
| BA6 | **"Satu pelanggan"** | Distributor Minuman | Total beli, outstanding, faktur belum lunas, retur, diskon, pembayaran, batas kredit, profit | ⬜ |
| BA7 | **"Satu pemasok"** | PT Distribusi Minuman | Total beli, utang, jatuh tempo, retur, harga | ⬜ |
| BA8 | **"Satu karyawan"** | Satu pramuniaga | Jadwal, absen, lembur, cuti, gaji, pinjaman, jabatan, atasan | ⬜ |
| BA9 | **Tidak ada data hilang** | Hapus/ubah dokumen yang sudah dipakai | Ditolak, atau meninggalkan jejak; tidak ada angka laporan berubah tanpa catatan | ⬜ |
| BA10 | **Tidak ada uang muncul dari ketiadaan** | Bandingkan total kas Neraca dengan jumlah semua penerimaan yang punya dokumen | Tidak ada penambahan kas tanpa dokumen | ⬜ |
| BA11 | **Tidak ada uang hilang** | Bandingkan pengeluaran kas dengan dokumen pembayaran | Setiap pengeluaran punya dokumen dan alasan | ⬜ |
| BA12 | **Tidak ada stok muncul** | Bandingkan penambahan stok dengan GR, retur, produksi, transfer, penyesuaian | Setiap penambahan punya dokumen | ⬜ |
| BA13 | **Tidak ada stok hilang** | Bandingkan pengurangan stok dengan delivery, POS, pemakaian, transfer, penyesuaian | Setiap pengurangan punya dokumen | ⬜ |
| BA14 | **"Akuntansi adalah hakim"** | Untuk lima transaksi acak dari modul berbeda, periksa jurnalnya | Jurnal seimbang, akun logis, periode benar, kegiatan benar | ⬜ |

---

## TAHAP BB — Uji Peran dan Titik Periksa Akhir

### BB-1. Tiga sudut pandang

| # | Peran | Pertanyaan | Lulus bila | OK |
| --- | --- | --- | --- | --- |
| BB1 | **Pemilik** (Arman Halim) | Berapa laba bulan ini? Kegiatan mana yang rugi? Berapa kas? Berapa piutang yang telat? Berapa nilai stok? | Semua terjawab dari dashboard dan satu atau dua laporan, tanpa Excel | ⬜ |
| BB2 | **Keuangan** (Sofyan Nugroho) | Apakah neraca seimbang, periode siap ditutup, pajak siap lapor, rekonsiliasi bank selesai, tidak ada jurnal draft menggantung? | Daftar kesiapan tutup bulan bisa dibuat langsung dari aplikasi | ⬜ |
| BB3 | **Auditor** | Pilih sampel 10 transaksi: dokumen asli, persetujuan, siapa yang membuat, siapa yang menyetujui, jurnal | Setiap sampel punya jejak lengkap (aktivitas dan siapa melakukan) tanpa celah | ⬜ |

### BB-2. Titik periksa akhir ERP

Tandai tiap butir bila **seluruhnya** benar. Satu butir gagal berarti ada temuan *High* atau *Critical*.

- [ ] Satu aktivitas bisnis dapat berjalan dari awal sampai akhir tanpa informasi yang bertentangan antar modul.
- [ ] Setiap angka di laporan keuangan dapat ditelusuri sampai dokumen sumbernya.
- [ ] Stok, piutang, utang, kas, dan pajak di modul sama dengan akun terkait di Neraca.
- [ ] Hak akses: peran tidak berhak tidak melihat atau mengubah data yang bukan miliknya; tombol nonaktif menjelaskan alasannya.
- [ ] Setiap perubahan penting punya jejak (siapa, kapan, apa yang berubah).
- [ ] Periode tertutup tidak berubah diam-diam.
- [ ] Bahasa, ekspor, dan pencetakan konsisten dengan layar.
- [ ] Semua temuan sudah dicatat dengan format enam bagian dan prioritas.

**Prinsip penutup (dari panduan asli):** ERP yang baik tidak hanya mencatat transaksi, tetapi dapat **menjelaskan bisnisnya sendiri**. Bila penguji harus menebak, itu temuan.
