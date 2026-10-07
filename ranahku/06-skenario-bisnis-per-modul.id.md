---
title: Ranahku — Skenario Bisnis per Modul (Pembelian, Penjualan, Kasir, Restoran, Persediaan, SDM)
description: Membawa seluruh daftar kasus dari global-testing (PO 20 kasus, SO 20 kasus, POS 60 kasus, Inventory 26 kasus, Restaurant 80 kasus, HRM 4 level) ke data Ranahku. Tiap kasus punya contoh konkret, hal yang diperiksa, dan label kategori. Dipakai penguji untuk memeriksa "apakah bisnis nyata bisa direpresentasikan", bukan hanya "apakah tombol bekerja".
---

# Ranahku — Skenario Bisnis per Modul

> Disusun 2026-10-07 dari `global-testing/PO.md`, `SO.md`, `POS.md`, `Inventory.md`, `RERTO.md`, dan `HRM.md`. Panduan asli bersifat umum
> (restoran, distributor, jasa); di sini setiap kasus diberi **data Ranahku** supaya bisa langsung dijalankan di cabang yang sama dengan berkas 01–05.
>
> **Cara berpikir (dipertahankan dari panduan asli):** jangan mulai dari "apakah tombol ini berhasil", mulai dari **"apakah perusahaan bisa menjawab pertanyaan
> bisnis ini dari data di aplikasi?"** Bila jawabannya tidak, itu *gap* dan dicatat.
>
> **Format catatan tiap temuan** (pakai di `TemuanTestCase/<Modul>/Ranahku/`):
> 1. *Business Case*: apa yang terjadi. 2. *Expected Business Result*: apa yang seharusnya bisa diketahui atau dilakukan perusahaan.
> 3. *Actual Result*. 4. *Gap*: apa yang belum bisa direpresentasikan. 5. *Business Impact*. 6. *Priority*: Critical / High / Medium / Low.
>
> **Prasyarat tambahan** (celah yang sudah ditemukan penguji sebelumnya; siapkan dulu): Sales Channel pada semua menu restoran; produk bahan segar
> (Sayur Campur, Ayam Potong, Telur Ayam; satuan Kg/Butir); Area, Meja, dan Kitchen Station restoran; Jenis Cuti "Cuti Tahunan" (aktifkan toggle lewat Edit).
>
> **Label:** 🆕 fitur belum ada · 🔧 kasus pinggiran belum ditangani · ✅ regresi.

## Ringkasan Tahap

| # | Tahap | Sumber | Jumlah kasus |
| --- | --- | --- | ---: |
| AQ | Pembelian | PO.md (20 kasus + uji siklus) | 22 |
| AR | Penjualan | SO.md (20 kasus + uji status) | 22 |
| AS | Kasir toko (POS) | POS.md (kasus retail, pembayaran, promo, kendali) | 40 |
| AT | Rumah makan | RERTO.md dan POS.md 22–36 | 45 |
| AU | Persediaan | Inventory.md (26 kasus) | 26 |
| AV | SDM | HRM.md (4 level pengujian) | 24 |

---

## TAHAP AQ — Pembelian

Pemasok: CV Grosir Sembako Makmur (21 hari), UD Pasar Segar (tunai), PT Distribusi Minuman Kemasan (14 hari), PT Sumber Elektronik Andalan (30 hari), Koperasi Percetakan Kreatif (tunai).

| # | Kasus | Contoh Ranahku | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AQ1 | Pembelian rutin | PR → PQ → PO restock 100 karung Beras (BRG-001) @ 62.000 dari CV Grosir Sembako | Alur lengkap, nomor dokumen berurutan, total + PPN benar, status tiap tahap | ⬜ |
| AQ2 | Pemasok baru | Tambah "UD Sayur Mayur Baru" lalu beli satu kali | Pemasok baru bisa dipilih; termin kosong tidak membuat error; tampil di kartu pemasok setelah transaksi | ⬜ |
| AQ3 | Pembelian darurat | Gas LPG habis hari ini: buat PO dan terima barang di hari yang sama tanpa PQ | Alur ringkas bisa berjalan bila konfigurasi tidak mewajibkan PQ; jejak "darurat" terbaca (catatan atau lampiran) | ⬜ |
| AQ4 | Harga pemasok berubah | Harga beras naik dari 62.000 ke 66.000 | Lencana kenaikan harga muncul; riwayat harga menampilkan tren; PO lama tidak berubah harganya | ⬜ |
| AQ5 | Permintaan pembelian dan persetujuan | PR dari staf gudang, disetujui Supervisor Toko | PR yang belum disetujui tidak bisa dikonversi; penolak dan alasan tercatat | ⬜ |
| AQ6 | Bandingkan pemasok | Dua PQ untuk Teh Kotak (BRG-006): CV Grosir vs PT Distribusi Minuman | Perbandingan per item dan rekomendasi; pilih pemenang per item (split) | ⬜ |
| AQ7 | Persetujuan bertingkat | Ambang: PO di atas 5.000.000 ke Manajer Keuangan, di atas 20.000.000 ke Direktur | PO 4 juta jalan; 6 juta butuh satu persetujuan; 25 juta butuh dua | ⬜ |
| AQ8 | Perubahan setelah persetujuan | Ubah qty PO yang sudah disetujui | Ditolak atau mengulang persetujuan; riwayat perubahan tercatat | ⬜ |
| AQ9 | Pengiriman bertahap | PO 100 dus Teh Kotak datang 60 lalu 40 | Dua Goods Receipt; PO berstatus sebagian lalu selesai; stok bertambah bertahap | ⬜ |
| AQ10 | Barang kurang | Dari 100 hanya 90 datang dan pemasok tidak akan mengirim sisanya | Sisa 10 bisa ditutup/dibatalkan; PO tidak menggantung selamanya | ⬜ |
| AQ11 | Barang rusak | 5 dus datang rusak | Retur ke pemasok atau penerimaan ditolak sebagian; stok hanya menghitung yang baik; utang menyesuaikan | ⬜ |
| AQ12 | Pembelian jasa | Jasa servis AC kantor 1.500.000 (non-persediaan) | Invoice tanpa Goods Receipt; beban masuk akun yang tepat; tidak menambah stok | ⬜ |
| AQ13 | Kontrak dan pembelian berulang | Kontrak payung 3 bulan gas LPG dengan pelepasan mingguan (Blanket Agreement) | Sisa kuota berkurang tiap release; harga kontrak dipakai; melebihi kuota ditolak | ⬜ |
| AQ14 | Faktur sebagian | Pemasok menagih 60% dulu | Dua Purchase Invoice terhadap satu PO; total tidak melebihi PO | ⬜ |
| AQ15 | Faktur melebihi PO | PO 50.000.000, faktur 55.000.000 | Ditolak atau diberi peringatan selisih; penyebab (harga, jumlah, biaya tambahan) bisa ditelusuri | ⬜ |
| AQ16 | Barang datang, faktur belum | GR hari ini, faktur seminggu lagi | Kewajiban sementara (GR/IR) tampil; laporan tidak kehilangan utang | ⬜ |
| AQ17 | PO dibatalkan | Batalkan PO yang belum diterima, lalu yang sudah diterima sebagian | Yang belum diterima bisa dibatalkan; yang sudah sebagian hanya sisa yang bisa ditutup | ⬜ |
| AQ18 | Pemasok gagal memenuhi | Pemasok menyatakan tidak sanggup kirim PO penuh | Sisa dibatalkan dan dialihkan ke pemasok lain lewat PO baru tanpa mengacaukan stok | ⬜ |
| AQ19 | Pembelian berdasarkan anggaran | PR dengan perkiraan anggaran 10.000.000; PO 12.000.000 | Penegakan anggaran memblokir atau memperingatkan sesuai pengaturan | ⬜ |
| AQ20 | Pembelian aset | Beli laptop 12.000.000 dari PT Sumber Elektronik | Masuk Aset Tetap (bukan persediaan); jurnal ke akun aset; bisa didaftarkan di modul Aset | ⬜ |
| AQ21 | Biaya tambahan | Ongkos angkut 100.000 untuk pembelian beras | Landed cost menaikkan nilai persediaan; tampil di laporan landed cost | ⬜ |
| AQ22 | Pertanyaan manajemen | "Berapa total beli dari CV Grosir bulan ini, berapa utangnya, berapa yang terlambat?" | Semua angka bisa dijawab dari kartu pemasok dan laporan; rincian PO menunjukkan siapa yang membuat dan menyetujui | ⬜ |

**Uji siklus pembelian:** satu PO diikuti dari PR sampai pembayaran, lalu dari pembayaran **mundur** ke PR (prinsip *reverse*). Setiap mata rantai (PR, PQ, PO, GR, PI, PPB, jurnal) harus bisa ditemukan dari yang lain.
**Uji "siapa yang perlu tahu":** setelah PO dibuat, apakah gudang, keuangan, dan pembuat PR bisa melihat statusnya tanpa bertanya?

---

## TAHAP AR — Penjualan

Pelanggan: Toko Bangunan Sumber Rejeki, Bengkel Motor Laju Jaya, Apotek Sehat Bersama, Distributor Minuman Segar Nusantara, CV Katering Nikmat Rasa.

| # | Kasus | Contoh Ranahku | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AR1 | Pesanan langsung | SO 10 karung Beras ke Toko Bangunan Sumber Rejeki | Alur SO → Delivery → Invoice → Payment; stok keluar saat delivery | ⬜ |
| AR2 | Pesanan katering | SO 150 porsi Paket Nasi Ayam Komplit untuk CV Katering | Menu bisa dijual lewat modul Sales (butuh Sales Channel); tanggal acara tercatat | ⬜ |
| AR3 | Perubahan pesanan | Pelanggan mengubah qty sebelum dan sesudah delivery | Sebelum delivery boleh; sesudah delivery dibatasi; riwayat perubahan tercatat | ⬜ |
| AR4 | Pembatalan | Batalkan SO sebelum dan sesudah sebagian dikirim | Hanya sisa yang bisa dibatalkan; reservasi stok dilepas | ⬜ |
| AR5 | Pelanggan minta tempo | Distributor Minuman minta 30 hari | Termin mengisi jatuh tempo faktur; piutang tampil di umur piutang | ⬜ |
| AR6 | Barang tidak cukup | Pesan 400 Gula tetapi stok 150 | Peringatan stok kurang atau backorder; kirim sebagian | ⬜ |
| AR7 | Pengiriman sebagian | Kirim 100 dari 150, lalu 50 | Dua delivery; SO berstatus sebagian lalu selesai; tidak bisa melebihi pesanan | ⬜ |
| AR8 | Jasa dan kontrak | Kontrak sewa aplikasi tahunan Apotek (Paket Pro) | Faktur tanpa delivery; pendapatan sesuai kebijakan (diterima dimuka) | ⬜ |
| AR9 | Pembayaran bertahap | Pendampingan awal 3 termin | Faktur per termin; sisa tagihan benar | ⬜ |
| AR10 | Perubahan lingkup | Pelanggan menambah modul Kasir di tengah kontrak | Penambahan lewat SO/faktur tambahan; kontrak awal tidak rusak | ⬜ |
| AR11 | Pelanggan baru | Daftar pelanggan baru lewat form dan lewat kanvasing cepat | Data minimal cukup untuk transaksi pertama; tidak ada duplikat nama | ⬜ |
| AR12 | Harga khusus pelanggan | Daftar harga Member/Reseller untuk Distributor | Harga pelanggan menggantikan harga umum; terlihat di SO | ⬜ |
| AR13 | Diskon | Diskon per item dan diskon total | Total dan PPN dihitung dari nilai setelah diskon; diskon tampil di dokumen | ⬜ |
| AR14 | Harga berubah setelah pesanan | Harga beras naik setelah SO dibuat | SO lama tetap harga lama; SO baru memakai harga baru | ⬜ |
| AR15 | Pembatalan sebagian oleh pelanggan | Pelanggan membatalkan 20 dari 100 | Qty berkurang; sisa konsisten di delivery | ⬜ |
| AR16 | Retur barang | Pelanggan mengembalikan 5 karung (cacat) | Retur menambah stok atau masuk karantina sesuai kondisi; piutang dan PPN berkurang | ⬜ |
| AR17 | Barang ditolak | Pelanggan menolak seluruh pengiriman | Delivery dibatalkan/retur penuh; faktur tidak terbentuk atau dikoreksi | ⬜ |
| AR18 | Pengiriman terlambat | Janji 5 September, kirim 9 September | Tanggal janji dan realisasi terbaca; ada indikator keterlambatan | ⬜ |
| AR19 | Dari penawaran | Quotation → Sales Order | Data penawaran terbawa; status penawaran menjadi diterima/dikonversi | ⬜ |
| AR20 | Uang muka | Distributor membayar DP 30% | DP tercatat sebagai titipan/uang muka, bukan pendapatan; terpotong saat pelunasan | ⬜ |
| AR21 | Pembayaran sebagian dan tidak membayar | Bayar 60% lalu menunggak | Faktur sebagian terbayar; umur piutang bertambah; ada tindak lanjut penagihan | ⬜ |
| AR22 | Pertanyaan manajemen | "Siapa pelanggan terbesar, berapa piutangnya, siapa yang menunggak, berapa labanya per pelanggan?" | Dapat dijawab dari kartu pelanggan dan laporan; hubungan SO ↔ stok ↔ akuntansi jelas | ⬜ |

**Uji status:** status SO tidak selalu linear (sebagian dikirim, sebagian ditagih, dibatalkan sebagian). Pastikan status menggambarkan kenyataan, bukan sekadar urutan tombol.
**Uji komitmen:** SO yang disetujui harus mengikat stok (reservasi) dan terlihat di gudang.

---

## TAHAP AS — Kasir Toko (POS)

Kasir: Fitri Handayani; produk BRG-001..010. Rujukan manual `pos/`.

| # | Kasus | Contoh Ranahku | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AS1 | Retail sederhana | 2 Gula + 1 Minyak, tunai | Total, kembalian, stok berkurang, struk | ⬜ |
| AS2 | Pembeli tidak terdaftar | "Pembeli Umum" | Transaksi tidak butuh data pembeli | ⬜ |
| AS3 | Pembeli terdaftar/member | Pilih member | Poin atau tingkat member terlihat; riwayat belanja tersimpan | ⬜ |
| AS4 | Banyak metode bayar | Total 95.000: tunai 50.000 + QRIS 45.000 | Jumlah metode = total; masing-masing masuk akun yang benar | ⬜ |
| AS5 | Bayar lebih | Total 95.000, uang 100.000 | Kembalian 5.000 benar | ⬜ |
| AS6 | Bayar kurang | Uang 90.000 | Transaksi tidak dapat diselesaikan atau jadi piutang bila diizinkan | ⬜ |
| AS7 | Diskon per item dan seluruh transaksi | 10% pada Teh Kotak; 5.000 pada total | Dasar PPN benar; diskon tampil di struk | ⬜ |
| AS8 | Promo dan promo waktu | Promo akhir pekan | Berlaku hanya pada jam/hari yang benar; di luar jam tidak berlaku | ⬜ |
| AS9 | Diskon member dan tingkat member | Member Gold 5% | Diskon sesuai tingkat; naik tingkat sesuai aturan | ⬜ |
| AS10 | Poin/loyalti dan cashback | Belanja menghasilkan poin/cashback | Poin atau saldo bertambah; dipakai di transaksi berikut; kedaluwarsa sesuai aturan | ⬜ |
| AS11 | Retur produk | Kembalikan 1 Pouch minyak dengan struk | Stok kembali (atau karantina), kas berkurang, jurnal pembalik | ⬜ |
| AS12 | Refund sebagian dan penuh | Refund 1 dari 3 item; refund seluruh transaksi | Total refund benar; metode refund sesuai pilihan | ⬜ |
| AS13 | Refund lewat metode berbeda | Bayar tunai, refund ke saldo cashback | Perbedaan metode tercatat dan jurnalnya benar | ⬜ |
| AS14 | Salah harga / salah produk | Salah scan Gula jadi Beras | Koreksi lewat void atau retur; tidak ada stok hantu | ⬜ |
| AS15 | Void sebelum dan sesudah bayar | Void keranjang; void setelah bayar | Void setelah bayar butuh otorisasi PIN manajer dan tercatat siapa yang mengotorisasi | ⬜ |
| AS16 | Pelanggan mengubah pesanan | Tambah/kurangi item sebelum bayar | Total ikut berubah | ⬜ |
| AS17 | Tahan transaksi | Tahan dan panggil kembali | Isi utuh; stok baru berkurang saat dibayar | ⬜ |
| AS18 | Perubahan harga | Harga diubah saat transaksi tertahan | Dicatat harga lama atau baru yang dipakai; konsisten | ⬜ |
| AS19 | Promo bertumpuk dan diskon manual | Promo + diskon manual kasir | Aturan prioritas jelas; diskon manual melebihi batas butuh otorisasi | ⬜ |
| AS20 | Shift kasir | Buka sesi pagi, ganti kasir siang | Sesi berbeda per kasir; tidak bisa dua sesi di meja sama | ⬜ |
| AS21 | Kas keluar dan kas masuk | Kas keluar beli es batu 20.000; kas masuk tambahan modal kembalian 100.000 | Tercatat dengan alasan; ikut perhitungan tutup sesi | ⬜ |
| AS22 | Tutup shift | Hitung per pecahan | Selisih = hitung fisik − (kas awal + tunai − refund + masuk − keluar) | ⬜ |
| AS23 | Kas lebih dan kurang | Lebih 20.000; kurang 50.000 | Selisih tercatat per kasir; terlihat di Setoran Kasir | ⬜ |
| AS24 | Pembayaran gagal | QRIS kedaluwarsa | Transaksi tidak ditandai lunas; bisa diulang dengan metode lain | ⬜ |
| AS25 | Pembayaran ganda | Bayar dua kali karena jaringan lambat | Tidak ada dua pembayaran untuk satu transaksi, atau duplikat bisa dilihat dan dibalik | ⬜ |
| AS26 | Beda outlet | Pembeli membeli di toko, retur di rumah makan | Retur lintas titik jual diperlakukan sesuai aturan; stok kembali ke gudang yang benar | ⬜ |
| AS27 | POS offline | Matikan jaringan, jual 3 barang | Transaksi tersimpan lokal dan sinkron saat daring; tidak ada nomor ganda | ⬜ |
| AS28 | POS tidak bisa dipakai | Perangkat rusak di tengah transaksi | Pemulihan: transaksi tertahan bisa dilanjutkan di perangkat lain | ⬜ |
| AS29 | Stok tidak cukup | Jual 10 Gula padahal stok 8 | Peringatan/penolakan sesuai pengaturan stok negatif | ⬜ |
| AS30 | Retur tanpa struk | Pembeli tanpa struk | Pencarian transaksi lewat nama, tanggal, atau nomor; kebijakan retur dipatuhi | ⬜ |
| AS31 | Struk ulang | Cetak ulang struk | Struk sama dengan aslinya (QR, nomor); ditandai salinan | ⬜ |
| AS32 | Riwayat transaksi | Cari transaksi kemarin | Filter tanggal, kasir, metode bayar | ⬜ |
| AS33 | Kinerja kasir | Laporan penjualan per kasir | Total sesuai transaksi; selisih kas per kasir terbaca | ⬜ |
| AS34 | Transaksi mencurigakan | Banyak void atau diskon manual oleh satu kasir | Dapat dilihat lewat laporan atau log; siapa dan kapan jelas | ⬜ |
| AS35 | Tutup harian | Seluruh sesi hari itu ditutup | Total penjualan harian = jumlah semua sesi; jurnal sesi seimbang | ⬜ |
| AS36 | Transaksi ≠ pembayaran | Transaksi tertahan belum bayar | Tidak masuk penjualan sebelum lunas | ⬜ |
| AS37 | Transaksi ≠ kas | Penjualan QRIS tidak menambah kas laci | Kas laci hanya dari tunai; QRIS ke penampung/bank | ⬜ |
| AS38 | Penjualan ≠ laba | Penjualan 1.000.000 dengan HPP 800.000 | Laba kotor dihitung dari HPP nyata (bukan dari harga jual) | ⬜ |
| AS39 | Keluhan pelanggan | Barang kadaluarsa dikembalikan | Retur masuk alasan khusus; stok tidak kembali ke jual | ⬜ |
| AS40 | Pertanyaan manajemen | "Berapa omzet, margin, jam tersibuk, produk terlaris, kasir mana yang selisihnya sering?" | Terjawab dari laporan dan dashboard | ⬜ |

---

## TAHAP AT — Rumah Makan

Master: Area Dalam (Meja 1–6), Area Luar (Meja 7–10), Dapur Panas, Dapur Dingin/Minuman; menu MNU-001..008. Rujukan manual `restaurant/`.

| # | Kasus | Contoh Ranahku | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AT1 | Restoran baru buka | Siapkan area, meja, kitchen station, menu, resep | Tanpa master data sesi meja tidak bisa dibuka (catat pesan); setelah lengkap berjalan | ⬜ |
| AT2 | Tamu datang tanpa reservasi | Walk-in 4 orang ke Meja 3 | Meja menjadi terisi; sesi dibuat | ⬜ |
| AT3 | Reservasi | Booking Meja 5 untuk 6 orang jam 19.00 | Meja ditahan pada jamnya; tidak bentrok dengan reservasi lain | ⬜ |
| AT4 | Tamu terlambat | Datang 40 menit lewat | Aturan toleransi; meja dilepas bila melewati | ⬜ |
| AT5 | Tamu tidak datang | No-show | Booking menjadi no-show; deposit (bila ada) diperlakukan sesuai aturan | ⬜ |
| AT6 | Status meja | Kosong → terisi → perlu dibersihkan → kosong; meja di luar layanan | Status berubah sesuai aksi; meja nonaktif tidak bisa dipilih | ⬜ |
| AT7 | Pindah meja | Pindah Meja 3 ke Meja 8 | Pesanan ikut pindah; meja lama kosong | ⬜ |
| AT8 | Gabung dan pisah meja | Gabung Meja 1 dan 2; pisah kembali | Satu tagihan; setelah pisah pesanan terbagi benar | ⬜ |
| AT9 | Jumlah tamu berubah | 4 orang jadi 6 | Perubahan tercatat; tidak mengacaukan pesanan | ⬜ |
| AT10 | Pesanan pertama dan tambahan | Pesan 2 Nasi Goreng; tambah 1 Es Jeruk | Item tambahan masuk dapur terpisah; total ikut | ⬜ |
| AT11 | Batal item | Batalkan Mie Goreng sebelum dan sesudah diproses dapur | Sebelum diproses langsung batal; sesudah butuh otorisasi dan tercatat sebagai pemborosan | ⬜ |
| AT12 | Modifier | Es Teh "kurang manis"; tambahan "+ telur" berharga | Modifier tanpa harga tidak mengubah total; yang berharga menambah total | ⬜ |
| AT13 | Menu habis | Tandai Soto Ayam habis | Tidak bisa dipesan; mudah dikembalikan | ⬜ |
| AT14 | Bahan habis | Ayam habis saat stok bahan nol | Menu bergantung bahan itu ditandai atau ditolak sesuai pengaturan | ⬜ |
| AT15 | Pesanan ke dapur | Pesan campuran makanan dan minuman | Rute ke Dapur Panas dan Dapur Dingin sesuai kategori | ⬜ |
| AT16 | Status dapur | Diterima → dimasak → siap → disajikan | Setiap perubahan terlihat di Kitchen Display dan pelayan | ⬜ |
| AT17 | Siap sebagian | Minuman siap, makanan belum | Status per item; pesanan tidak dianggap selesai | ⬜ |
| AT18 | Dapur terlambat dan prioritas | Pesanan lama terlewat | Urutan tampilan menurut waktu atau prioritas | ⬜ |
| AT19 | Pesanan salah | Dapur membuat Mie padahal pesan Nasi | Item dibatalkan dan dibuat ulang; bahan terbuang tercatat | ⬜ |
| AT20 | Sisa makanan dan bahan rusak | Catat pemborosan 2 porsi nasi dan sayur busuk | Pencatatan waste mengurangi stok dan masuk akun kerugian; terlihat di laporan | ⬜ |
| AT21 | Resep dan perubahan resep | Ubah resep Nasi Goreng (tambah 20 g ayam) | Pesanan baru memakai resep baru; riwayat pesanan lama tidak berubah | ⬜ |
| AT22 | Ukuran porsi dan combo | Porsi besar; paket combo (nasi + es teh) | Bahan terpotong sesuai porsi; harga paket benar | ⬜ |
| AT23 | Bungkus dan antar | Take away dan delivery | Tipe order berbeda; tanpa meja; biaya antar (bila ada) | ⬜ |
| AT24 | Status antar dan mitra | Status pengantaran; mitra antar fiktif | Status dapat diubah; pesanan tidak tertinggal | ⬜ |
| AT25 | Permintaan dan keluhan tamu | "Kurang pedas", "makanan dingin" | Catatan tersimpan; keluhan bisa ditelusuri ke pesanan | ⬜ |
| AT26 | Gratis dan diskon manajer | Item gratis; diskon manajer 10% | Butuh otorisasi; tercatat siapa; nilai gratis masuk beban promosi atau biaya | ⬜ |
| AT27 | Service charge dan pajak | Service 5% dan PB1 10% | Urutan penghitungan benar; PB1 ke utang pajak restoran | ⬜ |
| AT28 | Pisah tagihan dan pisah item | Split bill 2 orang; split per item | Total gabungan = total asli; pajak tidak hilang karena pembulatan | ⬜ |
| AT29 | Gabung tagihan | Dua meja bayar bersama | Satu pembayaran; kedua meja tertutup | ⬜ |
| AT30 | Tamu pergi tanpa bayar | Meja ditinggalkan | Pesanan tidak hilang; ada jalan mencatat kerugian | ⬜ |
| AT31 | Pembayaran dan multi pembayaran | Tunai + QRIS | Total sama; jurnal ke akun berbeda | ⬜ |
| AT32 | Refund dan void | Refund setelah bayar; void setelah dapur memproses | Void setelah dapur memproses butuh otorisasi; bahan sudah terpakai tetap tercatat | ⬜ |
| AT33 | Tutup meja dan bersihkan | Setelah bayar | Meja otomatis perlu dibersihkan lalu kosong | ⬜ |
| AT34 | Shift pelayan, dapur, kasir | Tiga shift sehari | Aktivitas terikat shift; laporan per shift | ⬜ |
| AT35 | Tutup harian | Ringkasan hari | Penjualan, pajak, pemborosan, selisih kas | ⬜ |
| AT36 | Jam sibuk dan kinerja menu | Laporan jam tersibuk, menu terlaris, meja tersering | Angka cocok dengan transaksi | ⬜ |
| AT37 | Profitabilitas menu | Margin per menu | Margin = harga − biaya bahan dari resep; menu bermargin rendah teridentifikasi | ⬜ |
| AT38 | Pelanggan langganan dan member | Pelanggan kembali | Riwayat dan preferensi terlihat | ⬜ |
| AT39 | Deposit reservasi dan no-show | Deposit 100.000 untuk reservasi 6 orang | Deposit tercatat sebagai titipan; dipakai saat bayar; hangus atau kembali sesuai aturan | ⬜ |
| AT40 | Stok teoritis vs aktual | Pemakaian bahan menurut resep vs hasil opname dapur | Selisih terlihat sebagai pemborosan; varians resep dapat dijelaskan | ⬜ |
| AT41 | Permintaan bahan dapur dan pengiriman pemasok | Dapur meminta ke gudang; UD Pasar Segar mengirim pagi | Stok dapur naik; transfer atau penerimaan tercatat | ⬜ |
| AT42 | Keamanan pangan dan menu dinonaktifkan sementara | Matikan Es Jeruk karena bahan basi | Menu hilang dari pilihan; tidak mengganggu pesanan lama | ⬜ |
| AT43 | Puncak pelanggan dan dapur kelebihan beban | Banyak pesanan sekaligus | Tidak ada pesanan hilang; urutan tetap terbaca | ⬜ |
| AT44 | Self-order QR | Tamu memesan lewat QR meja | Pesanan masuk ke meja yang benar; kasir melihatnya | ⬜ |
| AT45 | Pertanyaan manajemen | "Menu apa paling untung? Jam berapa paling sibuk? Berapa pemborosan bulan ini?" | Terjawab dari laporan tanpa hitung manual | ⬜ |

---

## TAHAP AU — Persediaan

Gudang: Gudang Toko Retail, Dapur Rumah Makan. Rujukan manual `inventory/`.

| # | Kasus | Contoh Ranahku | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AU1 | Barang masuk | GR beras 100 karung | Stok, nilai, dan hutang bertambah | ⬜ |
| AU2 | Barang digunakan | Dapur memakai bahan untuk menu | Stok bahan turun sesuai resep atau pemakaian manual | ⬜ |
| AU3 | Stok rusak | 5 dus Teh pecah | Penyesuaian dengan alasan "rusak"; jurnal beban kerugian persediaan | ⬜ |
| AU4 | Stok fisik berbeda | Hitung Gula 480 vs sistem 500 | Stock take mendeteksi selisih −20; penyesuaian dan jurnal selisih | ⬜ |
| AU5 | Stok minimum dan reorder | Atur batas minimum Beras 50 | Buffer stock menandai bila di bawah; PR otomatis bila diaktifkan | ⬜ |
| AU6 | Masuk bertahap | Lihat AQ9 | Stok bertambah per penerimaan | ⬜ |
| AU7 | Keluar lewat penjualan | Lihat AR1 | Stok turun saat delivery, bukan saat SO | ⬜ |
| AU8 | Backorder | Pesanan melebihi stok | Sisa tercatat; terpenuhi saat barang masuk | ⬜ |
| AU9 | Banyak gudang dan transfer | Transfer 100 Kopi Sachet dari Gudang Toko ke Dapur | Stok kedua gudang benar; status dikirim/diterima; barang dalam perjalanan terlihat | ⬜ |
| AU10 | Satuan berbeda | Beli per Dus (24 botol) jual per botol | Konversi satuan benar; stok dasar konsisten | ⬜ |
| AU11 | Satuan berat | Beras kiloan vs karung | Konversi 1 karung = 5 kg tampil benar | ⬜ |
| AU12 | Batch | Produk dengan nomor batch | Stok per batch; penjualan memilih batch sesuai aturan | ⬜ |
| AU13 | Tanggal kedaluwarsa | Teh Kotak kedaluwarsa 30 hari lagi | Peringatan; FEFO bila diatur; barang kedaluwarsa tidak bisa dijual | ⬜ |
| AU14 | Nomor seri | Laptop dengan nomor seri | Satu seri satu unit; tidak bisa dikeluarkan dua kali | ⬜ |
| AU15 | Retur pelanggan dan pemasok | Retur dari pelanggan masuk stok; retur ke pemasok keluar | Nilai stok dan hutang/piutang menyesuaikan | ⬜ |
| AU16 | Penyesuaian stok | Penyesuaian dengan alasan dan persetujuan | Alasan wajib; tersetujui baru berlaku (bila approval aktif) | ⬜ |
| AU17 | Stok tercadang | SO disetujui, belum dikirim | Stok tersedia = fisik − dicadangkan | ⬜ |
| AU18 | Beli dan jual bersamaan | PO datang sambil SO menunggu | Stok masuk langsung bisa memenuhi SO | ⬜ |
| AU19 | Produksi | Lihat Tahap AC | Bahan keluar, barang jadi masuk, biaya terhitung | ⬜ |
| AU20 | Paket/bundle | Paket "Sembako Hemat" (beras + minyak + gula) | Penjualan paket mengurangi komponen; harga paket benar | ⬜ |
| AU21 | Konsinyasi | Barang titipan pemasok di toko | Stok titipan terpisah dari milik sendiri; settlement saat terjual | ⬜ |
| AU22 | Barang milik pelanggan | Aset pelanggan disimpan di gudang | Tidak masuk nilai persediaan perusahaan | ⬜ |
| AU23 | Dalam perjalanan | Transfer dikirim belum diterima | Nilai di akun transit; tidak hilang dari neraca | ⬜ |
| AU24 | Kehilangan stok | Kehilangan 10 Gas LPG | Beban kerugian; dapat dilihat siapa yang mencatat | ⬜ |
| AU25 | Barang gratis | Bonus pemasok 5 dus | Stok bertambah dengan nilai nol atau sesuai kebijakan; HPP rata-rata terpengaruh sesuai metode | ⬜ |
| AU26 | Stok negatif | Jual lebih dari stok bila diizinkan | Perilaku sesuai pengaturan; laporan menandai stok negatif | ⬜ |

**Uji kuantitas, lokasi, kepemilikan, nilai:** untuk satu barang (BRG-003 Gula), telusuri berapa dibeli, di mana sekarang, milik siapa, berapa nilai total; angkanya cocok antara Stock History, kartu stok, laporan persediaan, dan Neraca `1-130`.

---

## TAHAP AV — SDM

Karyawan dari berkas 01 Tahap 9. Rujukan manual `hrm/`.

| # | Kasus | Contoh Ranahku | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AV1 | Karyawan baru | Terima Ibu Wati Suryani sebagai pramuniaga tanggal 15 | Data, jabatan, jadwal, dan akun pengguna terbentuk; gaji bulan pertama prorata | ⬜ |
| AV2 | Pindah posisi | Pramuniaga menjadi Supervisor Toko | Riwayat jabatan; gaji baru berlaku dari tanggal efektif; payroll bulan berjalan benar | ⬜ |
| AV3 | Tidak masuk | Tanpa keterangan 2 hari | Absen tercatat; potongan sesuai aturan; terlihat di rekap | ⬜ |
| AV4 | Lembur | Kasir lembur 3 jam | Lembur butuh persetujuan; yang tidak disetujui tidak masuk payroll | ⬜ |
| AV5 | Banyak pola kerja | Kantor 5 hari, toko shift, kanvasing lapangan | Tiap pola punya jadwal sendiri; keterlambatan dihitung dari jadwal masing-masing | ⬜ |
| AV6 | Transfer departemen | Staf gudang ke penjualan | Atasan dan departemen berubah; data lama tetap | ⬜ |
| AV7 | Dipindah sementara | Pramuniaga membantu rumah makan 1 minggu | Penugasan sementara terbaca; absen tetap benar | ⬜ |
| AV8 | Keterlambatan | Terlambat 25 menit | Terhitung dari jadwal; toleransi sesuai aturan | ⬜ |
| AV9 | Remote | Staf pendampingan bekerja dari rumah | Absen lewat cara yang sesuai (bukan mesin kantor) | ⬜ |
| AV10 | Cuti | Cuti tahunan 3 hari | Kuota berkurang; absen diberi status cuti; butuh persetujuan atasan | ⬜ |
| AV11 | Atasan cuti | Karyawan mengajukan cuti saat atasan juga cuti | Pengajuan tidak menggantung; ada pengganti persetujuan atau eskalasi | ⬜ |
| AV12 | Resign | Karyawan keluar tanggal 20 | Status berubah; gaji prorata; akses pengguna dinonaktifkan; riwayat tetap | ⬜ |
| AV13 | Pindah di tengah bulan | Pindah departemen tanggal 15 | Payroll membagi dua periode jabatan bila perlu | ⬜ |
| AV14 | Dua jenis jadwal | Kasir shift dan juga dinas luar | Aturan jadwal mana yang berlaku jelas | ⬜ |
| AV15 | Salah catat kehadiran | Koreksi absensi oleh karyawan | Pengajuan koreksi → disetujui HR → absen berubah; jejak audit | ⬜ |
| AV16 | Bekerja di hari libur | Masuk Minggu | Dihitung lembur atau pengganti sesuai kebijakan | ⬜ |
| AV17 | Lembur tidak disetujui | Lembur tanpa persetujuan | Tidak masuk payroll | ⬜ |
| AV18 | Pinjaman karyawan | Kasbon 500.000 dipotong dua bulan | Piutang karyawan; potongan di slip; saldo menurun | ⬜ |
| AV19 | Penggantian biaya | Reimburse bensin 150.000 | Pengajuan, persetujuan, pembayaran, jurnal beban | ⬜ |
| AV20 | Karyawan lintas outlet | Karyawan membantu outlet lain | Biaya tenaga kerja terbebankan ke kegiatan yang benar (bila ada pembebanan) | ⬜ |
| AV21 | Atasan berbeda per unit | Struktur atasan Toko vs Rumah Makan | Persetujuan mengikuti atasan langsung | ⬜ |
| AV22 | Payroll bulanan | Generate September | Pokok + tunjangan + komisi − BPJS − PPh 21 benar per karyawan; total sama dengan jurnal gaji | ⬜ |
| AV23 | Komisi sales | Aturan komisi untuk petugas kanvasing | Komisi dihitung dari kontrak yang ditutup; masuk payroll | ⬜ |
| AV24 | "Apakah saya sebagai HR bisa menjawab?" | Tanyakan: berapa karyawan aktif, siapa terlambat bulan ini, siapa cuti minggu depan, biaya SDM per departemen, siapa mendekati batas kontrak | Semua terjawab dari laporan tanpa Excel tambahan | ⬜ |

**Urutan pengujian yang disarankan (dari panduan asli):** siklus hidup karyawan (masuk, ubah, keluar) → perubahan → kasus pengecualian → pertanyaan HR. Prioritas temuan: *Critical* (gaji salah atau data rahasia bocor), *High* (alur terblokir), *Medium*, *Low*.

---

## Daftar Periksa Cepat

- [ ] AQ1–AQ22 pembelian
- [ ] AR1–AR22 penjualan
- [ ] AS1–AS40 kasir toko
- [ ] AT1–AT45 rumah makan
- [ ] AU1–AU26 persediaan
- [ ] AV1–AV24 SDM
- [ ] Setiap temuan memakai format enam bagian dan diberi prioritas
