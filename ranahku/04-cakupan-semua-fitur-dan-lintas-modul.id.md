---
title: Ranahku — Cakupan Semua Fitur dan Pemeriksaan Lintas Modul
description: Lanjutan berkas 00 sampai 03. Menambah skenario untuk setiap halaman dan fitur yang belum tersentuh (Manufaktur, Pertambangan, pengaturan Kasir lanjutan, valuasi persediaan, pembelian lanjutan, SDM lanjutan, master data pendukung, keamanan akun) dan menutup dengan skenario lintas modul yang memeriksa angka antar fitur. Disusun dari pemetaan menu aplikasi per 2026-10-07 terhadap isi berkas 00 sampai 03.
---

# Ranahku — Cakupan Semua Fitur dan Pemeriksaan Lintas Modul

> Disusun 2026-10-07. Berkas 00 sampai 03 menguji master data, alur transaksi inti, dan modul lanjutan sampai Tahap X.
> Sejak itu aplikasi bertambah (Manufaktur, Pertambangan, valuasi persediaan, biaya logistik, akses kasir, dll.) dan pemetaan
> menu menunjukkan masih ada halaman yang belum pernah disebut di berkas mana pun. Berkas ini menutup celah itu **dan** menambah
> pemeriksaan antar-modul, karena banyak bug muncul di sambungan antar fitur, bukan di satu halaman saja.
>
> **Cara memakai.** Kerjakan per tahap, centang kolom **OK** bila hasil sesuai kolom *Yang diperiksa*. Bila tidak sesuai, catat sebagai temuan
> di `erpApiServices/docs/TemuanTestCase/<Modul>/Ranahku/NN-judul-singkat.id.md` (ikuti pola temuan yang sudah ada: apa yang dilakukan,
> hasil yang terlihat, hasil yang diharapkan, dan tangkapan layar). Langkah rinci tiap halaman ada di **Manual Book**
> (`erpApiServices/docs/manualBook/<modul>/`); berkas ini menyebut bab yang relevan di kolom *Rujukan*, supaya tidak ada dua sumber yang bisa berbeda.
>
> **Prasyarat:** Tahap 1–12 di berkas 01 selesai, dan sebaiknya Tahap A–F di berkas 02. Tanggal transaksi: 1–30 September 2026, kecuali disebut lain.
> Semua nama dan angka fiktif; sesuaikan asal proporsional.

## Ringkasan Tahap

| # | Tahap | Isi |
| --- | --- | --- |
| Y | Pengaturan dan master data pendukung yang belum tersentuh | Order Types, Charge Types, Product Modifiers, Product Recipes, Journal Types, Approval Thresholds dan Workflow Configs, Pola Transaksi, Dokumen Legal dan Permintaan Data Pribadi, KPI, Branch Setup/Translations/Logs, alamat dan rekening kontak |
| Z | Kasir (POS) lanjutan | Meja Kasir dan akses kasir, Denominasi dan Setoran Kasir, transaksi ditahan, Customer Display, cetak label, struk (QR), pengaturan lanjutan |
| AA | Persediaan: valuasi, lot, dan pergerakan | Standar akuntansi dan metode biaya, biaya standar, identifikasi spesifik (pilih lot), retail method, penutupan varians, Stock Take satu halaman, Stock Movements |
| AB | Pembelian lanjutan | Purchase Configs (award, anggaran), Purchase Quotation round-trip, rekomendasi pemenang, tagihan biaya logistik dan laporan landed cost |
| AC | Manufaktur | Work Center, BOM, Routing, Production Order sampai jurnal |
| AD | Pertambangan | Site sampai Royalti dan Rekonsiliasi Survei |
| AE | SDM lanjutan | Mesin dan log absensi, rekap, perubahan status karyawan, wawancara dan penawaran kerja, layanan mandiri karyawan, struktur organisasi, komponen gaji |
| AF | Penjualan, Rental, Akuntansi, dan Pengaturan Akun | Sales Configs, aset sewa banyak unit, cabang akuntansi terpusat, keamanan akun (2FA, PIN), langganan |
| AG | Pemeriksaan lintas modul | Skenario yang menyambung beberapa fitur dan membandingkan angka antar laporan |
| AH | Peta cakupan | Tabel menu → tahap, dan halaman yang sengaja diuji di suite lain |

---

## Data tambahan yang dipakai berkas ini

Ranahku tidak memproduksi atau menambang. Supaya modul itu tetap teruji, dua **kegiatan percontohan fiktif** ditambahkan untuk keperluan pengujian saja:

| Kegiatan | Gambaran | Dipakai di |
| --- | --- | --- |
| **Dapur Produksi Nasi Kotak** | Dapur Rumah Makan memproduksi paket nasi kotak untuk pesanan katering: 1 paket = 1 porsi nasi, 1 lauk, 1 sayur, 1 kemasan | Tahap AC |
| **Tambang Pasir Percontohan (Site "Kali Sumber")** | Satu site galian pasir dengan satu pit, dua stockpile, satu alat berat, dua tarif royalti | Tahap AD |

Produk bahan baku dan produk jadi untuk Dapur Produksi dibuat dari katalog yang sudah ada (beras, ayam, sayur, kemasan) ditambah satu produk jadi
"Paket Nasi Kotak" dengan satuan *porsi*. Produk "Pasir Ayak" (satuan *ton*) dibuat untuk Tambang Percontohan.

---

## TAHAP Y — Pengaturan dan Master Data Pendukung

Rujukan: manual `konfigurasi-umum` (bab 04, 09, 15, 23, 24, 25) dan `hrm/16`.

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| Y1 | Client Master → **Order Types** | Tambah tipe "Dine In", "Take Away", "Katering" | Muncul di pilihan pada kasir dan restoran; tipe yang sudah dipakai transaksi tidak bisa dihapus (muncul penjelasan) | ⬜ |
| Y2 | Client Master → **Charge Types** | Tambah jenis biaya "Biaya Pengiriman" dan "Biaya Pasang"; pakai di Sales Order | Muncul di bagian biaya tambahan SO; total SO ikut berubah | ⬜ |
| Y3 | Client Master → **Product Modifiers** | Buat modifier menu "Level Pedas" (pilih satu: Tidak, Sedang, Pedas) dan "Tambahan" (pilih banyak, ada harga) | Tampil saat memesan menu di kasir restoran; harga tambahan masuk ke total pesanan | ⬜ |
| Y4 | Client Master → **Product Recipes** | Buat resep "Ayam Goreng" (bahan: ayam, minyak, bumbu) pada menu | Saat pesanan restoran selesai, stok bahan berkurang sesuai resep (cek Stock History) | ⬜ |
| Y5 | Client Master → **General Journal Type** | Tambah tipe jurnal "Penyesuaian Akhir Bulan" | Muncul pada pilihan tipe di jurnal manual | ⬜ |
| Y6 | Client Master → **Chart of Account Type** | Buka daftar; unduh template impor, isi, impor ulang | Pratinjau menandai duplikat/kosong sebelum disimpan; data yang disimpan tampil | ⬜ |
| Y7 | Client Master → **Approval Workflow Configs** | Tinjau alur persetujuan per modul yang sudah diaktifkan di berkas 03 Tahap M | Alur yang tampil sama dengan yang berjalan di Approval Requests | ⬜ |
| Y8 | Client Master → **Approval Amount Thresholds** | Buat ambang: Purchase Order di atas Rp 5.000.000 butuh persetujuan Manajer Keuangan | PO Rp 4.000.000 jalan tanpa persetujuan tambahan; PO Rp 6.000.000 meminta persetujuan | ⬜ |
| Y9 | Client Master → **Transaction Patern Types** dan **Transaction Paterns** | Buat tipe "Biaya Rutin", lalu pola "Bayar Listrik" dengan nominal tetap; coba aksi massal | Pola bisa dipakai ulang; aksi massal (aktif/nonaktif/hapus) meminta konfirmasi | ⬜ |
| Y10 | Client Master → **Legal Document Types** | Tambah jenis "Kontrak Sewa Aplikasi" dengan template; impor dari Excel | Jenis muncul di dokumen legal pada Quotation/SO bila dipakai; impor menolak baris cacat | ⬜ |
| Y11 | Client Master → **Data Subject Requests** | Cari seorang pelanggan; ekspor datanya; anonimkan satu kontak uji | Ekspor berisi data milik orang itu saja; kontak teranonimkan tidak tampak lagi sebagai nama aslinya dan tetap ada di dokumen lama sebagai data anonim; riwayat permintaan tercatat | ⬜ |
| Y12 | Client Master → **Contact Addresses** dan **Contact Bank Accounts** | Tambah dua alamat dan satu rekening bank untuk pelanggan "Apotek Sehat Bersama" | Alamat utama dipakai otomatis di dokumen; rekening muncul pada pembayaran | ⬜ |
| Y13 | Client Master → **KPI Criteria** (di SDM: Activity Types dan Employee Activity Logs) | Buat kriteria "Jumlah Kunjungan", jenis aktivitas "Kunjungan Pelanggan", catat aktivitas untuk Andi Saputra | Aktivitas tampil di daftar; kriteria bisa diubah dan dihapus (aksi massal berfungsi) | ⬜ |
| Y14 | Client Master → **Branch Setup** | Ubah satu pengaturan cabang (mis. prefiks nomor dokumen) | Nomor dokumen berikutnya memakai prefiks baru; dokumen lama tidak berubah | ⬜ |
| Y15 | Client Master → **Branch Translations** dan **Branch Logs** | Ubah satu terjemahan khusus cabang; buka log cabang | Teks tampil sesuai di layar terkait; log mencatat perubahan Y14 dan Y15 | ⬜ |
| Y16 | Pengaturan tampilan PDF (**PDF Layout Settings**) | Ubah kop dan nomor halaman, unduh PDF satu PO | PDF memakai pengaturan baru; berlaku untuk dokumen lain yang berbagi pengaturan | ⬜ |

---

## TAHAP Z — Kasir (POS) Lanjutan

Rujukan: manual `pos/01`, `pos/06`, `konfigurasi-umum/16` dan `/19`.

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| Z1 | Client Master → **Cash Registers** | Buat Meja Kasir "Kasir Toko 1"; tetapkan kasir yang boleh memakainya (Fitri Handayani saja); kunci ke satu perangkat bila ada pilihannya | Hanya kasir yang ditetapkan yang bisa membuka sesi di meja itu; kasir lain melihat pesan penolakan yang jelas | ⬜ |
| Z2 | POS → **Cash Sessions** | Login sebagai Fitri, buka sesi; coba buka sesi kedua di meja yang sama | Satu sesi per kasir dan per meja; percobaan kedua ditolak | ⬜ |
| Z3 | POS → **POS Transactions** | Login sebagai pengguna yang tidak ditetapkan di meja mana pun, buka halaman transaksi POS | Halaman tidak bisa dipakai oleh akun yang tidak terkait kasir (ditolak atau kosong sesuai aturan akses kasir) | ⬜ |
| Z4 | Client Master → **Cash Denominations** | Buat pecahan 100.000, 50.000, 20.000, 10.000, 5.000, 2.000, 1.000 (uang kertas) dan 1.000, 500 (koin) | Muncul di layar hitung uang saat tutup sesi; pecahan yang sudah dipakai tidak bisa dihapus tetapi bisa dinonaktifkan | ⬜ |
| Z5 | POS → **POS Configs** (hitung kas) | Ubah cara hitung laci: hanya jumlah, per pecahan, atau gabungan | Layar tutup sesi mengikuti pilihan | ⬜ |
| Z6 | POS → transaksi | Buat 3 transaksi; **tahan** (hold) satu transaksi, layani pembeli lain, lalu panggil kembali yang ditahan | Transaksi tertahan muncul di daftar tahan; setelah dipanggil isinya utuh dan stok baru berkurang saat dibayar, bukan saat ditahan | ⬜ |
| Z7 | POS → **Customer Display** | Buka tampilan pelanggan di layar kedua; ubah tata letak (iklan, hanya sambutan) di POS Configs; lakukan transaksi | Layar pelanggan menampilkan item dan total secara langsung; tata letak sesuai pilihan; pratinjau di POS Configs sama dengan tampilan nyata | ⬜ |
| Z8 | POS → **POS Configs** → Struk | Atur logo, teks kepala/kaki, NPWP, lebar kertas 58/80 mm, tampilkan barcode dan QR; isi QR dengan teks sendiri berisi `{transaction_number}` | Simpan lalu muat ulang: semua tersimpan; struk (cetak dan PDF) menampilkan logo dan QR yang sesuai; QR memuat teks yang diatur, bukan hanya nomor transaksi | ⬜ |
| Z9 | POS → **POS Configs** → pengaturan lain | Nyalakan pemindai kamera, mode offline, jurnal otomatis; pilih Order Types | Pengaturan tersimpan dan terbaca ulang; pemindai kamera tampil di halaman transaksi | ⬜ |
| Z10 | Client Master → **Products** → Print Labels | Cetak label untuk 10 produk dengan tiga jenis kertas (A4 bebas, lembar stiker, gulungan) | Jenis kertas dan jumlah per halaman sesuai; barcode terbaca; URL tidak lagi memuat id mentah | ⬜ |
| Z11 | POS → **Cashier Deposits** (Client Master) | Setelah tutup sesi dengan selisih lebih/kurang, buka Cashier Deposits | Saldo per kasir tampil; selisih tercatat; kembalikan saldo secara tunai dan lihat riwayat pergerakan | ⬜ |
| Z12 | POS → tutup sesi | Tutup sesi Fitri dengan hitung per pecahan | Selisih dihitung benar terhadap total transaksi tunai; jurnal tutup sesi seimbang | ⬜ |

---

## TAHAP AA — Persediaan: Valuasi, Lot, dan Pergerakan

Rujukan: manual `inventory/01`, `inventory/04`, `inventory/05`, `konfigurasi-umum/26`. Pakai gudang toko dan produk dari berkas 01.

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AA1 | Inventory → **Config** | Pilih standar akuntansi "PSAK 14"; buka daftar metode biaya | LIFO **tidak** tersedia; FIFO, rata-rata, identifikasi spesifik, dan biaya standar tersedia. Ganti standar ke "US GAAP": LIFO muncul | ⬜ |
| AA2 | Inventory → **Config** | Kembali ke PSAK; pilih FIFO sebagai bawaan cabang | Tersimpan; bila ada produk memakai metode yang tidak diizinkan standar, simpan ditolak dengan penjelasan | ⬜ |
| AA3 | Client Master → **Products** → menu SKU → **Inventory Valuation** | Untuk SKU "Beras 5 kg" pilih biaya standar; kosongkan biaya standar lalu simpan | Wajib mengisi biaya standar; setelah diisi (mis. 62.000) tersimpan; pilihan "ikuti bawaan cabang" mengembalikan ke metode cabang | ⬜ |
| AA4 | Pembelian → Goods Receipt | Terima 20 sak Beras 5 kg dengan harga PO 65.000 (biaya standar 62.000) | Stok masuk bernilai 62.000 per sak; selisih 3.000 × 20 = 60.000 tercatat sebagai selisih harga pembelian di jurnal (bila akun varians dipetakan); jurnal seimbang | ⬜ |
| AA5 | Inventory → **Config** | Atur "Purchase price variance under standard cost" ke "boleh ditutup ke akun lain"; petakan akun penutup (mis. Harga Pokok Penjualan) | Pengaturan tersimpan; halaman **Close Purchase Variance** bisa dipakai | ⬜ |
| AA6 | Inventory → Valuation → **Close Purchase Variance** | Tutup varians untuk September 2026 | Jurnal tercipta memindahkan saldo varians ke akun penutup; menutup periode yang sama lagi ditolak | ⬜ |
| AA7 | Client Master → Products → **Inventory Valuation** | Setel SKU "Genset Mini Demo" (barang bernilai tinggi) ke identifikasi spesifik; terima dua kali dengan harga berbeda (lot 1: 4.000.000, lot 2: 4.500.000) | Dua lot terbentuk dengan biaya masing-masing | ⬜ |
| AA8 | Sales → **Sales Delivery** → Create | Kirim 1 unit dan klik **Choose lots**; pilih lot 2 | Jumlah pilihan harus sama dengan qty (tombol Terapkan nonaktif bila tidak); setelah delivery disetujui, harga pokok pengiriman = 4.500.000, bukan 4.000.000 | ⬜ |
| AA9 | Inventory → **Config** | Atur "When no lot is picked" ke "Require a pick"; buat delivery produk yang sama tanpa memilih lot | Delivery ditolak saat disetujui dengan pesan wajib pilih lot. Ubah ke "newest lots first": delivery tanpa pilih lot berhasil memakai lot terbaru | ⬜ |
| AA10 | Inventory → Valuation → **Retail Method** | Pilih daftar harga jual toko, periode September, hitung | Muncul rasio biaya-ke-harga-jual, estimasi biaya persediaan akhir, nilai buku, dan selisihnya; produk tanpa harga di daftar harga tercantum sebagai dikecualikan | ⬜ |
| AA11 | Inventory → **Config** → "Retail method result" | Ubah ke "boleh dijurnal"; petakan akun penyesuaian; klik **Post adjustment** | Satu jurnal selisih tercipta; klik lagi tanpa perubahan data → ditolak "tidak ada yang baru"; jumlah yang sudah dijurnal tampil | ⬜ |
| AA12 | Inventory → **Stock Takes** | Buat stock take gudang toko pada satu halaman; hitung 5 produk; pindai atau ketik barcode; selesaikan | Selisih dihitung; penyesuaian stok dan jurnal selisih tercipta; tidak perlu pindah halaman untuk menghitung | ⬜ |
| AA13 | Client Master → **Stock Movements** (Pergerakan Stok) | Catat satu pergerakan stok manual; lalu buka daftar dengan filter produk dan gudang | Pergerakan manual masuk daftar dan mengubah stok; filter bekerja; referensi dokumen asal tampil untuk pergerakan otomatis | ⬜ |
| AA14 | Inventory → **Stock History** | Buka riwayat produk "Beras 5 kg" | Urutan dan saldo berjalan sama dengan semua pergerakan di atas | ⬜ |

---

## TAHAP AB — Pembelian Lanjutan

Rujukan: manual `purchasing/01`, `/03`, `/10`, `/12`. Pemasok: CV Grosir Sembako Makmur dan UD Pasar Segar (berkas 01 Tahap 5).

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AB1 | Purchasing → **Purchase Configs** | Aktifkan peringatan kenaikan harga (mis. 20%), strategi pemenang "termurah", dan penegakan anggaran "blokir" | Tersimpan dan terbaca ulang | ⬜ |
| AB2 | Purchasing → **Purchase Requests** | Buat PR restock sembako dengan perkiraan anggaran Rp 10.000.000 | Perkiraan anggaran tersimpan dan tampil di detail PR | ⬜ |
| AB3 | Purchasing → **Purchase Quotations** | Dari PR, buat dua PQ (satu per pemasok), kirim permintaan; isi harga di PQ pertama saja | Status permintaan per pemasok bergerak (terkirim → sebagian terjawab → semua terjawab) dan tampil di PR dan di daftar PQ; batas waktu jawab tercatat | ⬜ |
| AB4 | PR → **Compare Quotations** | Isi harga PQ kedua; buka perbandingan | Panel rekomendasi menunjuk pemenang sesuai strategi; skor termurah per item benar; ringkasan "akan menjadi berapa PO" menyebut jumlah PO per pemasok | ⬜ |
| AB5 | Compare Quotations | Pilih pemenang berbeda per item (split), lalu **Convert semua ke PO** | Dibuat satu PO per pemasok dengan item sesuai pilihan; item tanpa pemenang tercantum belum diputuskan | ⬜ |
| AB6 | Purchasing → **Purchase Orders** | Buat PO dengan total melebihi anggaran PR | Dengan penegakan "blokir": PO ditolak dengan alasan anggaran; ubah ke "peringatan": PO jalan dengan peringatan | ⬜ |
| AB7 | PO | Buat PO dengan harga 30% di atas harga terakhir pemasok | Lencana peringatan kenaikan harga muncul pada item; riwayat harga produk menampilkan tren | ⬜ |
| AB8 | Contacts → pemasok | Buka kartu pemasok | Skor pemasok (ketepatan waktu, selisih harga, retur) tampil dan berubah setelah beberapa transaksi | ⬜ |
| AB9 | Purchasing → **Purchase Charge Configs** | Buat konfigurasi "Ongkos Angkut Barang" (tipe: dibagi ke nilai persediaan) dan "Biaya Impor" bila ada | Konfigurasi tersimpan dengan akun terpetakan | ⬜ |
| AB10 | Purchasing → **Purchase Charge Invoices** | Terima barang dari pemasok (Goods Receipt), lalu buat tagihan ongkos angkut dari ekspedisi yang merujuk Goods Receipt itu | Setelah disetujui: nilai persediaan barang tersebut bertambah sebesar ongkos (landed cost); jurnal seimbang; hutang ekspedisi tercatat terpisah dari hutang pemasok | ⬜ |
| AB11 | Charge Invoice | Tandai untuk ditagih ulang ke pelanggan (rebill) bila opsinya tampil; bayar sebagian; unduh PDF | Rebill membuat tagihan ke pelanggan; pembayaran sebagian mengurangi hutang; PDF memuat rincian | ⬜ |
| AB12 | Purchasing → **Purchase Charge Inbox** | Bila WhatsApp terhubung: kirim foto tagihan ekspedisi; bila tidak, pastikan halaman menampilkan keadaan kosong yang jelas | Tagihan masuk muncul sebagai kotak masuk untuk diproses; tanpa integrasi tidak ada error | ⬜ |
| AB13 | Reports → **Landed Cost** dan **Logistics Payables** | Buka kedua laporan untuk September | Landed cost per barang = harga beli + biaya tambahan; hutang logistik cocok dengan saldo akun hutang ekspedisi | ⬜ |
| AB14 | Purchasing → **Blanket Agreements** (ulang bila belum di Tahap P) | Buat kontrak payung 3 bulan untuk pemasok sembako; lepas (release) satu PO dari kontrak | Sisa kuota kontrak berkurang; PO memakai harga kontrak; melebihi kuota ditolak | ⬜ |

---

## TAHAP AC — Manufaktur (Dapur Produksi Nasi Kotak)

Rujukan: manual `manufacturing/01` sampai `/04`. Aktifkan modul Manufaktur untuk cabang bila belum (lihat Tahap AF langganan).

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AC1 | Manufacturing → **Config** | Tetapkan gudang bahan (Gudang Dapur) dan gudang barang jadi, nyalakan persetujuan Production Order, petakan akun (Persediaan, Barang Dalam Proses, Tenaga Kerja dan Overhead Dibebankan) | Tersimpan; pemetaan otomatis mengisi akun bila tersedia | ⬜ |
| AC2 | Manufacturing → **Work Centers** | Buat "Stasiun Pengemasan" dengan tarif tenaga kerja Rp 30.000/jam dan overhead Rp 15.000/jam | Tersimpan; tarif tampil di daftar | ⬜ |
| AC3 | Manufacturing → **Bills of Materials** | Buat BOM "Paket Nasi Kotak": hasil 1 porsi; komponen beras 0,15 kg, ayam 0,12 kg, sayur 0,1 kg, kemasan 1 pcs; jadikan default | Produk jadi tidak bisa menjadi komponennya sendiri; komponen ganda ditolak; **Calculate Cost** menampilkan estimasi biaya bahan, peringatan bila ada komponen tanpa dasar biaya | ⬜ |
| AC4 | Manufacturing → **Routings** | Buat routing dua operasi: "Masak" dan "Kemas" (Stasiun Pengemasan, 6 menit/porsi) | Routing hanya muncul untuk BOM yang cocok | ⬜ |
| AC5 | Manufacturing → **Production Orders** | Buat order 100 porsi; daftar bahan dan operasi tersusun otomatis; **Submit** | Kebutuhan bahan = resep × 100; status menjadi Submitted dan tidak bisa **Release** sebelum disetujui | ⬜ |
| AC6 | Approvals → **Approval Requests** | Setujui permintaan Production Order | Status order menjadi Approved; **Release** kemudian **Start** berfungsi | ⬜ |
| AC7 | Production Order → Materials | Keluarkan sebagian bahan, lalu coba keluarkan melebihi kebutuhan; retur sebagian | Melebihi kebutuhan ditolak kecuali opsi izin melebihi aktif; stok gudang bahan berkurang/kembali; jurnal Persediaan → Barang Dalam Proses seimbang | ⬜ |
| AC8 | Production Order → Cancel | Coba **Cancel** saat masih ada bahan yang belum diretur | Ditolak dengan pesan wajib retur dulu | ⬜ |
| AC9 | Production Order → Operations | Mulai dan selesaikan tiap operasi dengan menit aktual 60 | Biaya tenaga kerja dan overhead dihitung dari tarif Work Center × menit aktual | ⬜ |
| AC10 | Production Order → **Complete** | Selesaikan dengan hasil 95 porsi (sebagian) | Stok barang jadi bertambah 95; biaya per porsi = total biaya ÷ 95; jurnal Barang Dalam Proses → Persediaan Barang Jadi seimbang dan saldo Barang Dalam Proses kembali nol | ⬜ |
| AC11 | Production Order | Coba **Complete** atau **Cancel** lagi, dan hapus order yang sudah berjalan | Semuanya ditolak; hanya order Draft atau Cancelled yang bisa dihapus | ⬜ |
| AC12 | Dashboard → **Manufacturing** | Buka dashboard | Angka order per status, output, dan biaya cocok dengan data AC5–AC10 | ⬜ |

---

## TAHAP AD — Pertambangan (Tambang Pasir Percontohan)

Rujukan: manual `mining/01` sampai `/06`. Aktifkan modul Pertambangan untuk cabang uji.

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AD1 | Mining → **Config** | Nyalakan "Production Logs Must Be Verified Before Stock Is Added"; petakan akun (Persediaan, Biaya Produksi Tambang, Beban Royalti, Utang Royalti, Kas) | Tersimpan | ⬜ |
| AD2 | Mining → **Sites**, **Pits**, **Equipment**, **Quality Parameters**, **Stockpiles** | Buat Site "Kali Sumber" (komoditas pasir), Pit "Pit A", alat berat "Excavator 01", parameter kualitas "Kadar Air", Stockpile "SP-A" dan "SP-B" (masing-masing menunjuk satu gudang) | Pit tersaring menurut Site; stockpile yang sudah dipakai log atau hauling tidak bisa dihapus | ⬜ |
| AD3 | Mining → **Production Logs** | Catat log Ore 100 ton ke SP-A dengan biaya Rp 20.000/ton; lalu log Overburden | Log tersimpan Draft dan **stok belum** bertambah; Overburden tidak masuk stok; Ore wajib Stockpile dan Produk | ⬜ |
| AD4 | Production Logs → **Verify** | Verifikasi log Ore | Stok gudang SP-A bertambah 100; jurnal: Persediaan bertambah 2.000.000 dan Biaya Produksi Tambang terkredit | ⬜ |
| AD5 | Mining → **Haulings** | Buat hauling SP-A → SP-B (bruto 35, tara 5), Dispatch, Deliver | Netto 30 ton; stok SP-A turun 30, SP-B naik 30 | ⬜ |
| AD6 | Haulings | Buat hauling melebihi sisa stok SP-A, Dispatch lalu Deliver | Pengiriman ditolak; stok tidak berubah | ⬜ |
| AD7 | Haulings | Buat hauling SP-A → Pelabuhan (tipe Port) 50 ton, kirim sampai Delivered | Tidak ada pergerakan stok ganda (pergerakan stok hanya untuk transfer antar stockpile) | ⬜ |
| AD8 | Mining → **Royalty Rates** | Buat tarif "Royalti Pasir 5%" (persentase) dan "Iuran Tetap" Rp 100/ton | Tersimpan dengan periode berlaku | ⬜ |
| AD9 | Mining → **Royalties** | Generate royalti September untuk Site, dengan harga dasar Rp 1.000/ton; lalu coba tanpa harga dasar | Hanya hauling Delivered ke tujuan non-stockpile dihitung; dua tarif menghasilkan dua baris; tanpa harga dasar (tarif persentase) ditolak | ⬜ |
| AD10 | Royalties | **Approve**, **Mark as Paid**; coba generate periode yang sama lagi | Jurnal beban dan utang royalti, lalu pembayaran, seimbang; hauling yang sudah masuk dokumen tidak dihitung ganda | ⬜ |
| AD11 | Royalties | **Reverse** royalti yang sudah dibayar | Jurnal pembalik tercipta sekali; hauling bisa dihitung ulang | ⬜ |
| AD12 | Production Logs | Coba **Cancel** log Ore yang sebagian stoknya sudah keluar | Ditolak | ⬜ |
| AD13 | Mining → **Survey Reconciliations** | Buat rekonsiliasi survei membandingkan volume survei dengan log terverifikasi; **Finalize** | Selisih dihitung; pit milik site lain ditolak; setelah final tidak bisa diubah | ⬜ |
| AD14 | Dashboard → **Mining** | Buka dashboard | Produksi, hauling, dan royalti cocok dengan data AD3–AD11 | ⬜ |

---

## TAHAP AE — SDM Lanjutan

Rujukan: manual `hrm/03` sampai `/16`. Karyawan dari berkas 01 Tahap 9.

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AE1 | HRM → **Organization Structure** | Buka bagan; tetapkan atasan langsung untuk 3 karyawan | Bagan mengikuti atasan; tidak bisa membuat siklus (A atasan B, B atasan A) | ⬜ |
| AE2 | HRM → **Salary Components** | Tambah tunjangan "Tunjangan Transport" tetap Rp 300.000 dan potongan "Kasbon"; terapkan ke dua karyawan | Komponen muncul di slip; berlaku pada payroll periode berikutnya | ⬜ |
| AE3 | HRM → **Attendance Devices** | Daftarkan satu mesin absensi "Mesin Pintu Depan" | Mesin tersimpan; kunci/kode integrasi tampil sesuai petunjuk | ⬜ |
| AE4 | HRM → **Attendance Device Logs** | Bila ada mesin atau data contoh: masukkan log mentah; periksa pencocokan ke karyawan | Log yang cocok menjadi catatan absensi harian; log tak dikenali tampil sebagai tidak cocok | ⬜ |
| AE5 | HRM → **Attendance Recaps** | Buat rekap absensi September | Hadir, terlambat, cuti, dan alpa per karyawan cocok dengan catatan harian; baris yang terkunci payroll tidak bisa diubah | ⬜ |
| AE6 | HRM → **Employee Status Changes** | Ajukan perubahan status: satu karyawan kontrak menjadi tetap | Riwayat status tersimpan; data karyawan memakai status baru mulai tanggal berlaku | ⬜ |
| AE7 | HRM → **Job Vacancies** → **Job Interviews** | Dari lamaran yang ada (berkas 03 Tahap L), jadwalkan wawancara | Status lamaran berubah; wawancara tampil di daftar; jadwal bentrok memberi peringatan | ⬜ |
| AE8 | HRM → **Job Offers** | Buat penawaran kerja untuk pelamar yang lolos | Alur status penawaran (dibuat, dikirim, diterima/ditolak) berjalan; penawaran diterima bisa dilanjutkan menjadi karyawan | ⬜ |
| AE9 | HRM → **My Leave Requests**, **My Attendance Adjustments**, **My Payslips** | Login sebagai karyawan biasa (bukan HR): ajukan cuti, ajukan koreksi absensi, buka slip gaji | Karyawan hanya melihat data miliknya; pengajuan masuk ke antrean HR; slip gaji hanya setelah payroll diproses | ⬜ |
| AE10 | HRM → **Payslips** | Login sebagai HR: buka slip semua karyawan | Data gaji karyawan lain hanya terlihat oleh yang berhak (izin data rahasia); karyawan biasa tidak bisa membuka halaman ini | ⬜ |
| AE11 | HRM → **Employee Activity Logs** (lanjut Y13) | Catat tiga aktivitas untuk satu karyawan lalu lihat ringkasan KPI | Aktivitas dan KPI sesuai input | ⬜ |

---

## TAHAP AF — Penjualan, Rental, Akuntansi, dan Pengaturan Akun

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AF1 | Sales → **Sales Configs** | Ubah alur persetujuan SO dan invoice; buka konfigurasi jurnal penjualan | Pengaturan memengaruhi dokumen berikutnya (SO baru meminta persetujuan bila diaktifkan) | ⬜ |
| AF2 | Rental → **Rental Configs** | Nyalakan "Rent many identical units of one asset" | Tersimpan | ⬜ |
| AF3 | Rental → **Assets** | Buat aset "Kursi Plastik" dengan **Total units** 50 | Total unit tampil; tanpa pengaturan AF2 menyala, mengisi lebih dari 1 ditolak | ⬜ |
| AF4 | Rental → **Orders** | Buat dan aktifkan order 30 unit; buat order kedua 30 unit | Order kedua ditolak ("hanya 20 unit bebas"); order 20 unit lolos; aset berstatus *rented* hanya ketika unit habis | ⬜ |
| AF5 | Rental → Orders → Complete | Selesaikan order pertama | 30 unit kembali ke pool; order baru 30 unit kembali bisa dibuat | ⬜ |
| AF6 | Rental → Returns | Retur sebagian dengan kondisi "hilang" 2 unit | Total unit aset berkurang 2 setelah retur disetujui | ⬜ |
| AF7 | Client Master → **Branch Manage** | Buat cabang uji "Toko Cabang Uji" dengan cabang induk Ranahku; nyalakan *Keep this branch's accounting in the main branch* | Saklar hanya bisa dinyalakan bila ada cabang induk; kolom **Users** menampilkan `jumlah / batas` | ⬜ |
| AF8 | Cabang uji | Lakukan satu penjualan atau penerimaan barang yang membuat jurnal otomatis | Jurnal dan buku besar tercatat di buku Ranahku (induk) dengan keterangan cabang asal; dokumen tetap milik cabang uji; pemetaan akun memakai milik induk | ⬜ |
| AF9 | Cabang uji | Matikan saklar | Transaksi berikutnya membukukan ke buku cabang uji sendiri (atau menolak jelas bila konfigurasinya belum disiapkan); jurnal lama tidak berpindah | ⬜ |
| AF10 | Accounting → Fiscal Year | Tutup tahun buku uji (di cabang uji coba, bukan Ranahku), lalu **Reopen Year** | Periode dibuka kembali; periode berjalan tidak berubah (bawaan) atau pindah ke periode terakhir bila setup `reopen_fiscal_year_current_period` diubah | ⬜ |
| AF11 | Settings → **Security** | Ganti password; aktifkan verifikasi dua langkah dengan aplikasi autentikator; simpan kode pemulihan; keluar lalu masuk | Login meminta kode; satu kode tidak bisa dipakai dua kali; kode pemulihan bisa dipakai sekali; mematikan 2FA butuh password dan kode | ⬜ |
| AF12 | Settings → Security → **PIN Override** | Atur PIN manajer; coba pakai PIN yang sama di akun lain | PIN unik: duplikat ditolak; PIN dipakai untuk otorisasi override dan tercatat | ⬜ |
| AF13 | Settings → **Appearance** dan ikon tema di sidebar | Ganti mode terang/gelap dan warna lewat menu palet di sidebar | Pilihan tersimpan setelah muat ulang; kolom pencarian global tetap lega | ⬜ |
| AF14 | Settings → **Subscription** | Buka status langganan; minta ganti paket | Status, batas pengguna/cabang, dan modul aktif tampil; permintaan ganti paket terkirim dan statusnya terlihat | ⬜ |
| AF15 | Help dan Changelog | Buka Help, cari satu bab manual; buka Changelog | Pencarian memenuhi lebar daftar; Changelog menampilkan entri sesuai izin | ⬜ |

---

## TAHAP AG — Pemeriksaan Lintas Modul

Tahap ini menyambung beberapa fitur dan membandingkan angka. Kerjakan setelah tahap lain selesai. Setiap skenario punya **pemeriksaan angka** yang
harus cocok; selisih sekecil apa pun dicatat sebagai temuan.

| # | Skenario | Pemeriksaan angka |
| --- | --- | --- |
| AG1 | **Pembelian → Persediaan → Penjualan → HPP.** Beli 100 pcs @ 5.000 (PO → GR → PI), tambah ongkos angkut Rp 100.000 (AB10), jual 40 pcs lewat Sales Order → Delivery → Invoice | Nilai persediaan 100 pcs = 600.000 (500.000 + 100.000); HPP 40 pcs = 240.000; sisa persediaan 360.000; Laporan Landed Cost, Stock History, dan Neraca menunjukkan angka yang sama |
| AG2 | **Kasir → Tutup sesi → Setoran → Kas.** Lakukan 5 transaksi tunai dan 2 non-tunai, ada 1 refund, tutup sesi dengan selisih | Total penjualan sesi = total transaksi dikurangi refund; selisih kas tercatat di Cashier Deposits; saldo Kas di Neraca naik sebesar kas bersih; jurnal sesi seimbang |
| AG3 | **Restoran → Resep → Stok → HPP.** Pesanan 10 porsi menu beresep (Y4), bayar | Stok bahan berkurang sesuai resep × 10; HPP menu = biaya bahan; laba kotor restoran di laporan per unit usaha benar |
| AG4 | **Manufaktur → Persediaan → Penjualan.** Jual 20 porsi Paket Nasi Kotak (AC10) lewat Sales Order katering | HPP per porsi = biaya per porsi dari Production Order; stok barang jadi turun 20; saldo Barang Dalam Proses nol |
| AG5 | **Valuasi → Laporan.** Setelah AA4–AA11, buka Neraca, Buku Besar Persediaan, dan laporan nilai persediaan | Nilai persediaan di Neraca = jumlah nilai lapisan stok (lot) di laporan persediaan; jurnal penutupan varians dan penyesuaian retail tidak membuat Neraca tidak seimbang |
| AG6 | **Tambang → Royalti → Kas.** Setelah AD9–AD10, buka Buku Besar akun Beban Royalti, Utang Royalti, dan Kas | Beban = Utang saat disetujui; Utang nol dan Kas turun sebesar royalti setelah dibayar; reverse mengembalikan ke saldo awal |
| AG7 | **Sewa banyak unit → Faktur → Bayar.** Order AF4 → Rental Invoice → Payment Bill → Return | Total faktur = unit × tarif harian × hari; deposit dikembalikan dikurangi biaya kerusakan; pendapatan sewa di laporan laba rugi cocok |
| AG8 | **Persetujuan lintas dokumen.** Aktifkan persetujuan untuk PO, Production Order, dan Stock Adjustment; ajukan masing-masing | Setiap permintaan muncul di Approval Requests dengan pemberi persetujuan yang benar; dokumen tidak bisa maju sebelum disetujui; ditolak mengembalikan ke Draft |
| AG9 | **Akses antar peran.** Login sebagai Kasir, Staf Gudang, Staf Akunting, HR, lalu Direktur; buka menu yang sama | Menu dan tombol yang tidak berhak tampil nonaktif dengan penjelasan (bukan hilang tanpa sebab); data rahasia karyawan hanya untuk yang berhak |
| AG10 | **Terjemahan.** Ganti bahasa ke Inggris lalu Indonesia pada tiga halaman dari tiap tahap Y–AF | Tidak ada teks yang tetap berbahasa lain atau tampil sebagai kunci mentah (`content.xxx`); header Excel/PDF mengikuti bahasa pengguna |
| AG11 | **Ekspor.** Ekspor Excel dan PDF dari lima halaman daftar dan lima laporan | Jumlah baris dan total sama dengan layar; format angka dan tanggal sesuai pengaturan; tidak ada kolom kosong yang aneh |
| AG12 | **Muat ulang dan konsistensi.** Pada setiap halaman daftar yang disentuh di berkas ini, tekan Refresh setelah membuat/mengubah/menghapus data | Daftar, tampilan alternatif (pohon/grid), dan halaman detail memuat data terbaru tanpa muat ulang browser |
| AG13 | **Hapus dan batalkan.** Coba menghapus data master yang sudah dipakai transaksi di tiap tahap | Selalu ditolak dengan penjelasan spesifik, tidak error server; data tidak berubah |

---

## TAHAP AH — Peta Cakupan Menu

Setiap halaman klien di aplikasi dan tahap yang menguji. Bila halaman belum tercantum, tambahkan saat menemukannya.

| Menu | Halaman | Tahap |
| --- | --- | --- |
| Client Master | approval-amount-thresholds, approval-workflow-configs | Y7, Y8 |
| | branch-logs, branch-setup, branch-translations | Y14, Y15 |
| | cash-denominations, cash-registers, cashier-deposits | Z1, Z4, Z11 |
| | charge-types, order-types | Y1, Y2 |
| | chart-of-account-type, general-journal-type | Y5, Y6 |
| | contact-addresses, contact-bank-accounts | Y12 |
| | data-subject-requests, legal-document-types | Y10, Y11 |
| | kpi-criteria | Y13 |
| | product-modifiers, product-recipes | Y3, Y4 |
| | transaction-paterns, transaction-patern-types | Y9 |
| Dashboard | manufacturing, mining | AC12, AD14 |
| | ai-usage | Diuji di suite *penjualan-sewa-aplikasi* (butuh akses khusus) |
| | subscriptions | Suite *penjualan-sewa-aplikasi* (khusus pemilik platform) |
| HRM | attendance-devices, attendance-device-logs, attendance-recaps | AE3–AE5 |
| | employee-status-changes | AE6 |
| | job-interviews, job-offers | AE7, AE8 |
| | my-attendance-adjustments, my-leave-requests, my-payslips | AE9 |
| | organization-structure, salary-components, payslips | AE1, AE2, AE10 |
| Inventory | valuation (retail method, close purchase variance), config | AA1–AA11 |
| Manufacturing | work-centers, boms, routings, production-orders | AC2–AC11 |
| Mining | sites, pits, equipment, quality-parameters, stockpiles, production-logs, haulings, royalty-rates, royalties, survey-reconciliations | AD2–AD13 |
| POS | customer-display | Z7 |
| Purchasing | purchase-configs, purchase-quotations | AB1–AB4 |
| | purchase-charge-configs, purchase-charge-invoices, purchase-charge-inbox | AB9–AB12 |
| Reports | landed-cost, logistics-payables | AB13 |
| Sales | sales-configs | AF1 |
| Settings | security, subscription | AF11, AF12, AF14 |

**Sengaja di luar berkas ini:** halaman Core dan pemilik platform (providers, branches, users/roles/permissions global, licenses, subscription plans,
billing prices, partner statements, landing page dan SEO, dashboard langganan) diuji di suite
[`penjualan-sewa-aplikasi`](../penjualan-sewa-aplikasi/) karena butuh akun pemilik platform dan bukan bagian dari operasi Ranahku sebagai klien.
Halaman publik (lamaran kerja, penawaran, restoran, pengiriman pemasok) diuji sebagai bagian dari tahapnya masing-masing di berkas 02 dan 03.

---

## Daftar Periksa Cepat

- [ ] Y1–Y16 pengaturan dan master data pendukung
- [ ] Z1–Z12 kasir lanjutan
- [ ] AA1–AA14 valuasi, lot, dan pergerakan stok
- [ ] AB1–AB14 pembelian lanjutan
- [ ] AC1–AC12 manufaktur
- [ ] AD1–AD14 pertambangan
- [ ] AE1–AE11 SDM lanjutan
- [ ] AF1–AF15 penjualan, rental, akuntansi, akun
- [ ] AG1–AG13 pemeriksaan lintas modul
- [ ] Semua temuan dicatat di `TemuanTestCase/<Modul>/Ranahku/`
