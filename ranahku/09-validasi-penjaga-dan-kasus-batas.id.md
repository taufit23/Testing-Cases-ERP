---
title: Ranahku — Validasi, Penjaga (Guard), dan Kasus Batas
description: Menyerap seluruh pola negatif dan kasus batas dari suite industri, suite per modul (purchasing, sales, hrm, inventory — termasuk Coretax dan Nusatech) dan POS: master data dan saldo awal, penjaga alur pembelian, penjualan, kasir, persediaan, SDM, serta kasus batas akuntansi (akun kontra, saldo kewajiban terlampaui, presisi angka besar, arus kas tidak dobel). Setiap baris memberi harapan dan label bila sistem ternyata tidak menolak.
---

# Ranahku — Validasi, Penjaga (Guard), dan Kasus Batas

> Disusun 2026-10-07. Pembacaan lebih dalam atas suite lain menunjukkan bahwa selain skenario bisnis, mereka punya lapisan besar yang berbeda:
> **uji penolakan.** Hampir tiap skenario punya pasangan *Negatif* (input atau urutan salah harus ditolak dengan pesan jelas) dan *Netralisasi*.
> Banyak temuan berharga lahir dari sini, misalnya sistem yang **tidak menolak** sesuatu yang seharusnya ditolak. Berkas ini membawa lapisan itu ke Ranahku.
>
> **Pola tiap baris:** *Aksi salah* → *Harapan* (ditolak dengan pesan yang menyebut sebabnya, bukan error 500) → bila sistem **menerima**, beri label 🆕/🔧 dan catat sebagai
> temuan. Kolom *Pesan* cukup diisi pesan aktual yang terlihat, supaya kualitas pesan ikut dinilai.
>
> **Cara menjalankan di UI:** banyak kasus tidak bisa dipicu lewat UI karena dropdown hanya menampilkan data valid (mis. akun fiktif). Pada kasus itu **uji lewat API**
> dengan token tester (Insomnia/Postman); kolom *Cara* menandai `UI` atau `API`. Aplikasi memakai metode POST untuk hampir semua endpoint, termasuk daftar.
>
> **Label hasil:** 🆕 fitur penjaga belum ada · 🔧 penjaga ada tetapi kasus pinggiran lolos · ✅ regresi (sudah benar, dites supaya tidak mundur) · 🐞 error server (500) atau pesan teknis yang tidak ramah.

## Ringkasan Tahap

| # | Tahap | Isi |
| --- | --- | --- |
| BD | Master data dan saldo awal | Kode unik, enum, isolasi cabang, akun kontrol, saldo awal (jebakan terbesar), mata uang dan kurs, generate periode |
| BE | Penjaga alur pembelian | PR, PQ, PO, GR, PI, pembayaran |
| BF | Penjaga alur penjualan | Quotation, SO, Delivery, Invoice, diskon, batas kredit |
| BG | Penjaga kasir (POS) dan restoran | Gudang toko, sesi, pembayaran, hold, void, refund |
| BH | Penjaga persediaan dan SDM | Penyesuaian stok, serial, opname; absensi, cuti, payroll, komisi |
| BI | Kasus batas akuntansi | Akun kontra, saldo terlampaui, presisi, arus kas, dimensi, periode |
| BJ | Mata uang asing dan selisih kurs | Utang USD, pelunasan dengan kurs berbeda, jebakan pelunasan naif, untung kurs, kurs tanpa aktivasi, rekening bank USD |

---

## TAHAP BD — Master Data dan Saldo Awal

Rujukan: suite `accounting-*` file 00 (tiap suite punya bagian ini), manual `konfigurasi-umum`.

### BD-A. Validasi master data

| # | Aksi salah | Harapan | Cara | Pesan | OK |
| --- | --- | --- | --- | --- | --- |
| BD1 | Buat Chart of Account dengan kode duplikat (`1-110` dua kali) | Ditolak validasi unik per cabang | UI | | ⬜ |
| BD2 | Buat tipe akun dengan Code duplikat | Ditolak | UI | | ⬜ |
| BD3 | Buat mata uang `IDR` dua kali di cabang yang sama | Ditolak (unik per cabang) | UI | | ⬜ |
| BD4 | Buat Business Unit dengan `default_unit_type` di luar `cost/profit/both` | Ditolak 422 | API | | ⬜ |
| BD5 | Buat Business Unit dengan kode duplikat | Ditolak | UI | | ⬜ |
| BD6 | Buat produk dengan kategori teks bebas di luar daftar (bila ada enum) | Ditolak atau memilih dari daftar saja | API | | ⬜ |
| BD7 | Kirim id milik **cabang lain** (akun, kegiatan, gudang) pada payload | Ditolak "tidak ditemukan di cabang"; bukan membaca data cabang lain | API | | ⬜ |
| BD8 | Pakai `business_unit_id` cabang lain pada laporan | Hasil kosong, bukan error dan bukan data cabang lain | API | | ⬜ |
| BD9 | Generate periode untuk Fiscal Year yang sama dua kali | Ditolak atau tidak menggandakan periode (catat 🔧 bila periode dobel muncul) | UI | | ⬜ |
| BD10 | Setelah generate, hitung periode | 12 bulanan tanpa celah dan tanpa tumpang tindih; daftar tidak memuat dua baris untuk bulan yang sama | UI | | ⬜ |
| BD11 | Daftar mata uang dengan kurs `0` atau negatif | Ditolak (`min` positif) | UI | | ⬜ |
| BD12 | Jurnal mata uang asing tanpa kurs aktif | Ditolak dengan pesan kurs belum ada | UI | | ⬜ |
| BD13 | Buat akun bank dengan akun COA non-kas | Ditolak "bukan akun kas" | UI | | ⬜ |
| BD14 | Hapus master data yang sudah dipakai transaksi (kategori, satuan, pelanggan, akun, gudang) | Ditolak dengan penjelasan spesifik; bukan error 500 | UI | | ⬜ |
| BD15 | Produk dengan SKU duplikat di cabang yang sama | Ditolak | UI | | ⬜ |
| BD16 | Kontak bertipe `customer` dipilih sebagai pemasok | Ditolak di PR/PO/tier harga | API | | ⬜ |

### BD-B. Saldo awal (jebakan terbesar menurut suite sumber)

Saldo awal adalah fondasi seluruh laporan. Suite manufaktur dan klinik mencatat **bug berantai** di sini; ulangi di Ranahku dengan teliti. Halaman: **Finance → Bank Accounts** dan **Client Master → Chart of Accounts Balances**.

| # | Aksi | Harapan | Cara | OK |
| --- | --- | --- | --- | --- |
| BD17 | Buat saldo awal **sebelum** ada akun bertanda *Ekuitas Saldo Awal* (`3-103`) | Ditolak "tidak ada akun ekuitas saldo awal" | UI | ⬜ |
| BD18 | Setelah `3-103` ada, buat saldo awal Kas Kecil 3.000.000 | Terbentuk jurnal saldo awal (bukan hanya baris saldo); Neraca Saldo `1-101` = 3.000.000, `3-103` mengimbangi | UI | ⬜ |
| BD19 | Buat dua akun bertanda *Ekuitas Saldo Awal* | Dicatat apakah ditolak; bila tidak → 🔧 (sistem hanya memakai satu tanpa peringatan) | UI | ⬜ |
| BD20 | Buat saldo awal untuk akun yang `balance_required` tidak diaktifkan (mis. akun pendapatan) | Ditolak "COA ini tidak butuh saldo" | UI | ⬜ |
| BD21 | `opening_balance` berisi teks atau mata uang yang tidak ada | Ditolak 422 | API | ⬜ |
| BD22 | Saldo awal akun **kewajiban** (Utang Usaha) | Posting bersisi kredit (arah kebalikan aset) dan tampil kredit di Neraca Saldo | UI | ⬜ |
| BD23 | Saldo awal memakai field debit/kredit total (`debit_total`, `credit_total`) | Dicatat apakah dua field itu benar-benar memengaruhi jurnal saldo awal (suite lain menemukan **diabaikan**) → 🔧 bila diabaikan | API | ⬜ |
| BD24 | Saldo awal akun bank dengan mata uang asing | Dicatat apakah nilai dikonversi ke IDR dengan kurs aktif; tanpa kurs aktif ditolak jelas | UI/API | ⬜ |
| BD25 | Ubah saldo awal setelah dipakai transaksi | Jurnal saldo awal lama dibalik (reverse) lalu dibuat baru; tidak ada saldo ganda | UI | ⬜ |
| BD26 | Saldo di tabel saldo awal vs buku besar | Setelah semua langkah, Neraca Saldo per 31 Agustus memuat saldo awal; bila **tidak**, itu temuan (suite Coretax mencatat saldo tidak otomatis masuk GL) | UI | ⬜ |
| BD27 | Total saldo awal | Neraca Saldo awal seimbang; selisih bila ada ditangkap `3-103` dan diterangkan | UI | ⬜ |
| BD28 | Modal awal dan neraca pembuka dibandingkan berkas 00 | Setiap angka berkas 00 muncul di akun yang benar | UI | ⬜ |

---

## TAHAP BE — Penjaga Alur Pembelian

Rujukan: suite `purchasing`, `purchasing-coretax`, `purchasing-nusatech`.

| # | Aksi salah | Harapan | Cara | Pesan | OK |
| --- | --- | --- | --- | --- | --- |
| BE1 | Submit PR tanpa satu item pun | Ditolak (bukan dokumen kosong) | UI | | ⬜ |
| BE2 | Buat PR dengan cabang selain cabang aktif | Ditolak (isolasi cabang) | API | | ⬜ |
| BE3 | Tier harga PQ dengan kontak bukan pemasok | Ditolak (validasi tipe kontak) | API | | ⬜ |
| BE4 | Hapus item PQ yang sudah dipakai pada tier harga | Ditolak, atau catat 🔧 (harga jadi tak konsisten) | UI | | ⬜ |
| BE5 | PO dengan qty 0 atau negatif | Ditolak 422 | UI | | ⬜ |
| BE6 | PO dengan kontak bertipe pelanggan | Ditolak | API | | ⬜ |
| BE7 | PR ditolak, lalu langsung Submit lagi | Harus melalui revisi dahulu atau ditolak sesuai alur | UI | | ⬜ |
| BE8 | PO tanpa PQ ketika konfigurasi tidak mewajibkan PQ | Berhasil; bila ditolak, bendera konfigurasi tidak bekerja | UI | | ⬜ |
| BE9 | PO tanpa PQ ketika konfigurasi mewajibkan PQ | Ditolak dengan pesan jelas | UI | | ⬜ |
| BE10 | Buat PO dari PR yang belum disetujui (persetujuan PR aktif) | Ditolak, atau dicatat 🔧 bila PR hanya "rekomendasi" tanpa gerbang | UI | | ⬜ |
| BE11 | Goods Receipt melebihi sisa PO (PO 50, terima 60) | Ditolak 422 (regresi) | UI | | ⬜ |
| BE12 | GR kedua untuk PO yang sudah diterima penuh | Ditolak | UI | | ⬜ |
| BE13 | Export jurnal GR yang sudah pernah diekspor | Ditolak, tidak ada posting ganda | UI | | ⬜ |
| BE14 | Purchase Invoice dengan qty lebih besar dari GR | Ditolak, atau catat 🔧 (gap serupa over-receipt) | UI | | ⬜ |
| BE15 | Invoice tanpa GR ketika konfigurasi mengizinkan | Berhasil; jurnal memakai akun beban/persediaan sesuai pemetaan | UI | | ⬜ |
| BE16 | Invoice tanpa GR ketika konfigurasi mewajibkan GR | Ditolak | UI | | ⬜ |
| BE17 | Bayar (create/mark-paid) sebelum Purchase Invoice disetujui | Ditolak di **backend**, bukan hanya tombol nonaktif di UI (regresi) | API | | ⬜ |
| BE18 | Bayar melebihi sisa utang faktur | Ditolak atau dibatasi | UI | | ⬜ |
| BE19 | Export jurnal faktur yang sudah diekspor | Ditolak | UI | | ⬜ |
| BE20 | Pembayaran dengan metode tanpa akun terpetakan | Pesan jelas bahwa pemetaan belum ada, bukan error teknis | UI | | ⬜ |
| BE21 | PO dengan produk tak ada di cabang ini | Ditolak | API | | ⬜ |
| BE22 | Ubah pemasok pada PO yang sudah punya GR | Ditolak | UI | | ⬜ |
| BE23 | Hapus PO yang sudah punya GR | Ditolak dengan penjelasan | UI | | ⬜ |
| BE24 | Konfigurasi akun pembelian belum dipetakan lalu export jurnal | Pesan menyebut fungsi akun yang belum dipetakan | UI | | ⬜ |

---

## TAHAP BF — Penjaga Alur Penjualan

Rujukan: suite `sales`, `sales-coretax`, `sales-nusatech`. Suite Coretax menegaskan: **tanpa konfigurasi penjualan, semua posting jurnal gagal**; uji ini di Ranahku lewat Sales Configs.

| # | Aksi salah | Harapan | Cara | Pesan | OK |
| --- | --- | --- | --- | --- | --- |
| BF1 | Sales Order dengan SKU yang sama di dua baris | Ditolak atau digabung (regresi bug lama) | UI | | ⬜ |
| BF2 | Quotation: Customer Accept sebelum status Sent | Ditolak (urutan status) | UI | | ⬜ |
| BF3 | SO tanpa quotation ketika `require_quotation_for_so` aktif | Ditolak; saat tidak aktif diterima | UI | | ⬜ |
| BF4 | SO dengan qty 0 | Ditolak 422 | UI | | ⬜ |
| BF5 | Setujui SO melebihi batas kredit pelanggan (batas dikecilkan untuk uji) | Ditolak dengan pesan soal batas kredit | UI | | ⬜ |
| BF6 | Kode diskon yang sudah dinonaktifkan | Ditolak "kode tidak aktif" | UI | | ⬜ |
| BF7 | Kode diskon kedaluwarsa atau melebihi kuota pemakaian | Ditolak | UI | | ⬜ |
| BF8 | Delivery melebihi sisa SO | Ditolak (guard over-delivery) | UI | | ⬜ |
| BF9 | Invoice melebihi nilai SO | Ditolak atau dibatasi | UI | | ⬜ |
| BF10 | Export jurnal faktur yang sudah diekspor | Ditolak | UI | | ⬜ |
| BF11 | Terima pembayaran melebihi sisa piutang | Ditolak atau menjadi uang muka | UI | | ⬜ |
| BF12 | Sales Config belum disetel lalu terbitkan faktur dengan jurnal | Pesan jelas "konfigurasi penjualan belum diatur" | UI | | ⬜ |
| BF13 | Retur penjualan tanpa akun retur/kontra pendapatan | Pesan jelas atau memakai akun pendapatan dengan peringatan (catat) | UI | | ⬜ |
| BF14 | Delivery: apakah menyentuh buku besar? | Sesuai mode jurnal: manual (tidak), otomatis (HPP terbentuk); catat perilaku dan bandingkan dengan konfigurasi | UI | | ⬜ |
| BF15 | Ubah pelanggan pada SO yang sudah punya delivery | Ditolak | UI | | ⬜ |
| BF16 | Hapus SO yang sudah punya faktur | Ditolak | UI | | ⬜ |
| BF17 | Penjualan jasa (tanpa stok) memilih gudang | Tidak butuh gudang; stok tidak berubah | UI | | ⬜ |
| BF18 | Perpanjangan kontrak bulanan | Tidak ada pembuatan faktur otomatis kecuali fitur diaktifkan; kontrak bulan berikut dibuat manual (catat bila diharapkan otomatis → 🆕) | UI | | ⬜ |

---

## TAHAP BG — Penjaga Kasir (POS) dan Restoran

Rujukan: suite `accounting-pos-retail` dan manual `pos/`, `restaurant/`.

| # | Aksi salah | Harapan | Cara | Pesan | OK |
| --- | --- | --- | --- | --- | --- |
| BG1 | Buka sesi kasir di gudang bertipe pusat/central | Ditolak "hanya gudang toko" | UI | | ⬜ |
| BG2 | Buka sesi dengan gudang milik cabang lain | Ditolak | API | | ⬜ |
| BG3 | Buka sesi kedua di meja/gudang yang sama saat sesi pertama masih terbuka | Ditolak | UI | | ⬜ |
| BG4 | Satu kasir membuka dua sesi | Ditolak | UI | | ⬜ |
| BG5 | Tutup sesi yang sudah tertutup | Ditolak atau idempoten tanpa efek ganda | UI | | ⬜ |
| BG6 | Buat transaksi pada sesi yang sudah tertutup | Ditolak | API | | ⬜ |
| BG7 | Bayar tunai dengan uang diterima < total | Ditolak (tendered ≥ total untuk tunai penuh) | UI | | ⬜ |
| BG8 | Dua baris pembayaran yang totalnya ≠ total transaksi | Ditolak | UI | | ⬜ |
| BG9 | Pembayaran QRIS dibatalkan atau timeout | Transaksi tidak ditandai lunas; catat bila "pending" tanpa kedaluwarsa (🆕 expire) | UI | | ⬜ |
| BG10 | Tahan transaksi (hold) | Catat apakah stok berkurang saat hold (seharusnya tidak) | UI | | ⬜ |
| BG11 | Panggil kembali transaksi yang sudah selesai atau di-void | Ditolak | UI | | ⬜ |
| BG12 | Void transaksi yang sudah void | Ditolak atau idempoten | UI | | ⬜ |
| BG13 | Refund melebihi qty yang dibeli (beli 5, refund 10) | Ditolak (over-refund) | UI | | ⬜ |
| BG14 | Refund transaksi yang sudah void | Ditolak | UI | | ⬜ |
| BG15 | Jual barang yang stoknya 0 di gudang ini tetapi ada di gudang toko lain | Ditolak; stok per gudang, tidak "nyerempet" | UI | | ⬜ |
| BG16 | Transfer stok melebihi stok tersedia di pusat | Ditolak | UI | | ⬜ |
| BG17 | Buat transaksi sebelum fungsi jurnal kasir (kas, pendapatan, PPN) dipetakan | Transaksi tetap selesai tetapi jurnal tidak terbentuk dan ada peringatan (catat perilaku) | UI | | ⬜ |
| BG18 | Bayar dengan kartu debit dan QRIS | Dicatat apakah keduanya masuk akun kas kasir atau akun metode masing-masing; selaraskan dengan rekonsiliasi (AO10) | UI | | ⬜ |
| BG19 | HPP kasir | Catat apakah penjualan kasir membentuk HPP otomatis; bandingkan HPP di laba rugi dengan pengurangan persediaan | UI | | ⬜ |
| BG20 | Restoran: sesi meja tanpa area/meja/kitchen station | Pesan jelas bahwa master data restoran belum lengkap | UI | | ⬜ |
| BG21 | Pesan menu yang tidak diberi Sales Channel | Menu tidak muncul atau ditolak di modul Sales; di kasir meja jalan sesuai kanal | UI | | ⬜ |
| BG22 | Menu tanpa resep tetapi menu bahan lain | Penjualan tetap jalan; stok bahan tidak berkurang (catat) | UI | | ⬜ |
| BG23 | Reservasi tumpang tindih pada meja yang sama | Ditolak atau diperingatkan | UI | | ⬜ |
| BG24 | Tutup meja dengan pesanan belum dibayar | Ditolak atau minta konfirmasi | UI | | ⬜ |

---

## TAHAP BH — Penjaga Persediaan dan SDM

Rujukan: suite `inventory-nusatech`, `hrm-nusatech`, manual `inventory/` dan `hrm/`.

### BH-A. Persediaan

| # | Aksi salah | Harapan | Cara | Pesan | OK |
| --- | --- | --- | --- | --- | --- |
| BH1 | Buat gudang dengan cabang selain cabang aktif | Ditolak | API | | ⬜ |
| BH2 | Post Stock Adjustment tanpa Submit lebih dulu (bila status mensyaratkan) | Ditolak 422 | UI | | ⬜ |
| BH3 | Stock Adjustment dengan unit cost 0 pada item selisih | Stok tetap berubah; jurnal selisih tidak terbentuk untuk item tanpa nilai (catat) | UI | | ⬜ |
| BH4 | Hapus pemetaan akun `inventory_loss` lalu ulangi skenario susut | Stok dan status tetap berhasil, jurnal tidak terbentuk dan ada log peringatan (gagal lunak) | UI | | ⬜ |
| BH5 | Nomor seri duplikat | Ditolak (unik) | UI | | ⬜ |
| BH6 | Opname dengan hasil fisik lebih kecil dari sistem | Selisih negatif tercatat; stok disesuaikan hanya setelah selesai | UI | | ⬜ |
| BH7 | Selesaikan opname dua kali | Ditolak | UI | | ⬜ |
| BH8 | Transfer stok melebihi stok | Ditolak | UI | | ⬜ |
| BH9 | Terima transfer melebihi yang dikirim | Ditolak | UI | | ⬜ |
| BH10 | Pergerakan stok manual tanpa alasan | Ditolak atau alasan wajib | UI | | ⬜ |
| BH11 | Hapus gudang yang masih berisi stok | Ditolak | UI | | ⬜ |
| BH12 | Penyesuaian akhir stok negatif | Ditolak atau mengikuti pengaturan stok negatif | UI | | ⬜ |

### BH-B. SDM

| # | Aksi salah | Harapan | Cara | Pesan | OK |
| --- | --- | --- | --- | --- | --- |
| BH13 | Buat karyawan dengan departemen/jabatan yang tidak ada atau milik cabang lain | Ditolak | API | | ⬜ |
| BH14 | Absensi ganda untuk karyawan dan tanggal yang sama | Ditolak atau menimpa; catat bila tidak ada penjaga | UI | | ⬜ |
| BH15 | Cuti melebihi saldo cuti | Ditolak; bila lolos catat 🔧 (tidak ada validasi saldo) | UI | | ⬜ |
| BH16 | Cuti dengan tanggal selesai sebelum mulai | Ditolak | UI | | ⬜ |
| BH17 | Tandai payroll dibayar sebelum disetujui | Ditolak (urutan status) | UI | | ⬜ |
| BH18 | Generate payroll dua kali untuk periode yang sama | Ditolak atau tidak menggandakan | UI | | ⬜ |
| BH19 | Komisi untuk karyawan di posisi non-sales | Ditolak atau catat 🔧 (tidak ada validasi posisi) | UI | | ⬜ |
| BH20 | Karyawan tanpa NPWP atau data pajak lengkap masuk payroll | Pesan jelas atau memakai tarif tanpa NPWP (catat) | UI | | ⬜ |
| BH21 | Ubah absensi yang sudah terkunci payroll | Ditolak | UI | | ⬜ |
| BH22 | Karyawan biasa membuka halaman data gaji karyawan lain | Ditolak | UI | | ⬜ |
| BH23 | Jenis cuti baru: toggle berbayar/persetujuan/aktif saat Create | Tersimpan sesuai pilihan (temuan lama: tidak tersimpan; uji ulang) | UI | | ⬜ |

---

## TAHAP BI — Kasus Batas Akuntansi

Rujukan: suite pendidikan (saldo melebihi), kafe (voucher), rumah sakit (write-off), klinik gigi (komisi), manufaktur (presisi dan dual currency), hotel (pajak daerah), Coretax (akun pajak).

### BI-A. Penolakan yang **tidak** ada (uji bahwa Anda mengetahuinya)

Jurnal manual bebas selama debit = kredit. Beberapa suite sumber menegaskan **sistem tidak menolak** hal berikut; ini sengaja diuji supaya temuan dan keputusan produk terdokumentasi.

| # | Aksi | Harapan ideal | Catatan | OK |
| --- | --- | --- | --- | --- |
| BI1 | Pelunasan/pengakuan yang melebihi saldo kewajiban: amortisasi Pendapatan Diterima Dimuka `2-140` melebihi saldonya | Idealnya diperingatkan atau ditolak | Jika lolos → saldo `2-140` negatif; catat 🆕 | ⬜ |
| BI2 | Write-off piutang melebihi sisa piutang `1-120` | Idealnya diperingatkan | Jika lolos → piutang negatif; 🆕 | ⬜ |
| BI3 | Redemption voucher melebihi saldo voucher | Idealnya diperingatkan | 🆕 bila lolos | ⬜ |
| BI4 | Bayar komisi melebihi saldo akrual (akrual 1.285.000, bayar 2.000.000) | Idealnya diperingatkan | 🆕 bila lolos | ⬜ |
| BI5 | Pendapatan restoran tanpa memisahkan PB1 | Idealnya ada pengingat pajak | 🆕 bila lolos (sistem tidak mewajibkan PB1 di jurnal manual) | ⬜ |
| BI6 | Jurnal tanpa akun berflag pajak | Deteksi pajak otomatis tidak aktif; pastikan penguji tahu bahwa rekap pajak hanya membaca akun berflag | Cek Tahap AP | ⬜ |
| BI7 | Memakai rekening deposit/penampung untuk beban operasional | Idealnya dibatasi | Lihat BC7 (berkas 08) | ⬜ |
| BI8 | Dua akun berflag Laba Ditahan atau Ekuitas Saldo Awal | Idealnya ditolak | Lihat AK14–AK15 dan BD19 | ⬜ |

### BI-B. Tampilan dan perhitungan yang harus benar

| # | Skenario | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BI9 | **Akun kontra-aset** (Akumulasi Penyusutan `1-209`) | Tampil bersaldo kredit (negatif) di Neraca Saldo; di Neraca mengurangi aset tetap, tidak "bocor" ke bagian lain | ⬜ |
| BI10 | **Akun kontra-pendapatan** (diskon, retur) | Tidak salah kategori: tidak muncul sebagai pendapatan positif; mengurangi pendapatan di Laba Rugi | ⬜ |
| BI11 | **Arus kas tidak dobel** | Setor kas toko ke bank (antar dua akun kas) tidak dihitung dua kali; Operasi + Investasi + Pendanaan = perubahan kas riil | ⬜ |
| BI12 | **Jumlah dimensi = konsolidasi** | Neraca Saldo, Laba Rugi, Arus Kas: jumlah tiga kegiatan (+ baris tanpa kegiatan) = konsolidasi | ⬜ |
| BI13 | **Baris tanpa kegiatan tidak hilang** | Filter default memuat baris tanpa Business Unit | ⬜ |
| BI14 | **Aktual anggaran bertanda benar** | Beban aktual menambah realisasi (positif); pendapatan aktual positif untuk anggaran pendapatan | ⬜ |
| BI15 | **Presisi angka besar** | Jurnal Rp 40.000.000.000 dan Rp 14.750.000.000: tidak ada pembulatan atau floating-point drift di GL, Neraca, ekspor | ⬜ |
| BI16 | **Dua trial balance identik** | `Reports → Trial Balance` dan `General Ledger → Trial Balance`: hasil sama | ⬜ |
| BI17 | **Akun dengan banyak baris** | Detail ledger `1-110` yang berisi puluhan baris: halaman tidak lambat, saldo berjalan benar, ekspor lengkap | ⬜ |
| BI18 | **`as_of_date` sebelum transaksi** | Semua saldo nol kecuali saldo awal; tidak error | ⬜ |
| BI19 | **Tutup periode sebelum akhir periode** | Coba Close September pada 21 September: catat apakah ada penjaga tanggal | ⬜ |
| BI20 | **Lock sebelum Close, Lock dua kali, Close dua kali, Reopen periode terbuka** | Masing-masing ditolak dengan pesan khusus; reopen periode terkunci ditolak | ⬜ |
| BI21 | **Dua rekening bank untuk satu jurnal** | Setoran kasir ke bank dan bunga bank pada satu transaksi berbeda; rekonsiliasi masing-masing rekening berdiri sendiri | ⬜ |
| BI22 | **Jurnal 5 baris vs dua jurnal** | Transaksi bisnis yang dipecah dua jurnal tetap bisa ditelusuri lewat kode dan keterangan yang mengacu satu sama lain | ⬜ |
| BI23 | **Dimensi tidak merata** | Sebagian transaksi bertag kegiatan, sebagian tidak: laporan per kegiatan menjelaskan baris yang tidak bertag, bukan menyembunyikannya | ⬜ |
| BI24 | **Margin sangat tinggi bulan ini** | Bila laba kotor tampak tidak wajar karena data uji, catat sebagai catatan desain data, bukan bug | ⬜ |

---

## TAHAP BJ — Mata Uang Asing dan Selisih Kurs

Rujukan: suite `accounting-manufaktur` dan `-manufaktur-2` (file 02 dan 06) serta hotel (USD). **Mekanisme penting dari suite sumber:** kurs yang dipakai jurnal
dipilih dari baris kurs yang sedang **aktif** (`is_active`) untuk mata uang itu; **tanggal jurnal tidak memilih kurs**. Mengunggah kurs baru saja tidak cukup,
kurs itu harus **diaktifkan** (mengaktifkan satu kurs menonaktifkan kurs lain untuk mata uang yang sama).

Persiapan: mata uang `USD` ada; kurs A = 15.800 aktif; kurs B = 16.000 dibuat tetapi belum aktif. Buat akun **Rugi Selisih Kurs** (beban) dan **Laba Selisih Kurs**
(pendapatan lain) bila belum ada, dan catat bahwa Bagan Akun Ranahku awalnya **tidak memiliki** akun selisih kurs (🆕 bila dipandang perlu ada bawaan).
Buat akun bank **Bank Operasional USD** dengan mata uang USD dan saldo awal USD 500.

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| BJ1 | Utang valas | Jurnal: Dr `6-104` 1.580.000 / Cr Utang Usaha dalam **USD 100** (hanya `foreign_credit`, tanpa `credit`) | Jurnal lolos pemeriksaan seimbang (basis IDR dihitung dari kurs aktif 15.800); jumlah asing tersimpan | ⬜ |
| BJ2 | Posting dan GL | Post jurnal BJ1 | GL menyimpan basis IDR sebagai nilai utama (1.580.000) dan nominal asing sebagai pelengkap; saldo utang bertambah 1.580.000 | ⬜ |
| BJ3 | Aktifkan kurs baru | **Activate** kurs B (16.000) | Kurs A otomatis nonaktif; jurnal valas berikutnya apa pun tanggalnya memakai 16.000 | ⬜ |
| BJ4 | **Jebakan pelunasan naif** | Lunasi utang dengan satu baris `foreign_debit` USD 100 pada akun utang dan `foreign_credit` USD 100 pada bank USD | Jurnal lolos, **tetapi** utang terdebit 1.600.000 (kurs aktif), bukan 1.580.000 yang tercatat: saldo utang −20.000 (utang terdebit berlebih). Catat sebagai 🔧 jebakan desain; lalu **Reverse** jurnal ini | ⬜ |
| BJ5 | Pelunasan benar (3 baris) | Dr Utang Usaha **1.580.000 (IDR)** + Dr Rugi Selisih Kurs 20.000 / Cr Bank USD **foreign_credit USD 100** | Basis IDR: debit 1.600.000 = kredit 1.600.000 (100 × 16.000); utang tepat nol untuk faktur itu; rugi kurs 20.000 muncul di Laba Rugi | ⬜ |
| BJ6 | Untung kurs | Ulangi BJ1–BJ2 saat kurs aktif 15.800, aktifkan kurs 15.600, lunasi: Dr Utang 1.580.000 / Cr Laba Selisih Kurs 20.000 / Cr Bank USD (USD 100 = 1.560.000) | Utang nol; laba kurs 20.000 di pendapatan lain; saldo bank USD berkurang USD 100 | ⬜ |
| BJ7 | Mata uang tanpa kurs aktif | Buat mata uang `EUR` baru yang **tidak pernah** diberi kurs; buat jurnal dengan baris EUR | Ditolak dengan pesan kurs aktif tidak ditemukan; tanggal jurnal tidak relevan | ⬜ |
| BJ8 | Rekening bank USD | Buat akun bank USD dengan saldo awal USD 500 saat kurs belum ada | Ditolak jelas bila kurs tidak ada; dengan kurs aktif saldo awal terkonversi ke IDR (500 × kurs) dan jurnal saldo awal terbentuk | ⬜ |
| BJ9 | Saldo awal akun kewajiban valas | Saldo awal utang USD 2.000 | Posting kredit dengan konversi benar; dicatat apakah mata uang saldo awal memengaruhi hasil (suite sumber menemukan bug di jalur ini) | ⬜ |
| BJ10 | Neraca Saldo dan Neraca tetap IDR | Setelah BJ1–BJ6 | Semua laporan dalam IDR; tidak ada akun valas bersaldo asing tanpa konversi; total debit = kredit | ⬜ |
| BJ11 | Rekonsiliasi bank USD | Reconciliation untuk Bank Operasional USD periode berjalan | Saldo rekening koran USD dibandingkan dengan saldo buku **asing**, bukan IDR; selisih kurs bukan selisih rekonsiliasi (catat perilaku sebenarnya) | ⬜ |
| BJ12 | Reverse jurnal valas | Reverse BJ5 | Pembalik memakai nilai yang sama dengan jurnal asal (bukan kurs aktif terbaru); saldo kembali ke posisi semula | ⬜ |
| BJ13 | Revaluasi akhir bulan | Tentukan apakah ada fitur revaluasi saldo valas ke kurs akhir bulan | Bila tidak ada, catat 🆕 (jurnal revaluasi manual dibuat oleh akuntan) | ⬜ |

---

## Daftar Periksa Cepat

- [ ] BD1–BD28 master data dan saldo awal
- [ ] BE1–BE24 penjaga pembelian
- [ ] BF1–BF18 penjaga penjualan
- [ ] BG1–BG24 penjaga kasir dan restoran
- [ ] BH1–BH23 penjaga persediaan dan SDM
- [ ] BI1–BI24 kasus batas akuntansi
- [ ] BJ1–BJ13 mata uang asing dan selisih kurs
- [ ] Setiap penolakan yang **tidak** terjadi dicatat sebagai temuan dengan dampak bisnis dan prioritas
