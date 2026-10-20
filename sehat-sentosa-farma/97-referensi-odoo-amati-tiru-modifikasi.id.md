---
title: (PT Sehat Sentosa Farma) — 97. Referensi Odoo: Amati, Tiru, Modifikasi (Pilot Modul Akuntansi)
category: sehat-sentosa-farma
description: Perilaku ERP yang dianggap benar menurut tes Odoo 20.0 (modul account), dibandingkan dengan aplikasi ini, menjadi kasus uji tambahan dan daftar peluang agar modul kita lebih unggul. Pilot metode ATM (Amati, Tiru, Modifikasi).
visibility: internal
---

# 97. Referensi Odoo: Amati, Tiru, Modifikasi

Metode **ATM**: **Amati** perilaku yang diuji di tes Odoo (`addons/<modul>/tests`, cabang 20.0), **Tiru** perilaku yang memang benar menjadi kasus uji di
suite ini, lalu **Modifikasi** di tempat desain kita berbeda atau bisa lebih baik. Yang dipakai hanya **gagasan skenario**; kode dan teks tes Odoo
tidak disalin. Rangkuman perilaku diambil dari tes lewat peringkas otomatis, jadi **tiap baris di bawah perlu dicek ulang ke berkas aslinya**
sebelum dijadikan keputusan desain. Kolom status "Aplikasi kita" sudah diperiksa ke kode kita (bukan tebakan).

> **Batas:** repositori publik Odoo hanya memuat edisi Community. Modul Enterprise (payroll, aset, rekonsiliasi lanjutan) tidak ada di sana, jadi
> pembanding untuk SDM-gaji dan aset tetap tidak bisa diambil dari sumber ini.

## 1. Pilot: `addons/account/tests` (dibaca: reconcile, payment method line, lock exception, tax report)

| # | Amati (perilaku Odoo) | Aplikasi kita | Tiru: kasus uji | Modifikasi / peluang unggul |
| --- | --- | --- | --- | --- |
| 1 | **Selisih kurs** dijurnal saat pelunasan valas dengan kurs berbeda; **dua akun terpisah**, laba kurs dan rugi kurs; dijurnal pada akhir bulan; **batal rekonsiliasi membalik** jurnal selisih | Sudah, terbatas: hanya **faktur biaya logistik** valas, **satu akun** laba/rugi (debit = rugi, kredit = laba), dijurnal di **tanggal pembayaran**; pembatalan pembayaran membalik selisih. Faktur penjualan/pembelian barang **belum punya mata uang** | `05` dan `15`: bayar faktur valas pada kurs lebih rendah (laba), lebih tinggi (rugi), sama (tanpa baris selisih); batalkan pembayaran; tanpa akun terpilih pembayaran memakai kurs faktur | Pisahkan laporan laba kurs dan rugi kurs walau satu akun (kolom di laporan); perluas ke faktur penjualan/pembelian valas bila ada klien dengan transaksi valas |
| 2 | **Lunas sebagian valas**: selisih kurs hanya untuk bagian yang dilunasi, sisa tetap terbuka dalam mata uang asing | Sama prinsipnya: selisih dihitung per pembayaran dari jumlah yang dibayar | `05`: bayar 60% lalu 40% pada dua kurs berbeda; jumlah dua selisih = selisih seluruhnya terhadap kurs faktur | Tampilkan sisa utang dalam mata uang asing di umur utang |
| 3 | **Metode pembayaran per jurnal** dengan akun sendiri; urutan pemilihan: pilihan mitra, lalu pilihan di faktur, lalu baris pertama jurnal | Sudah, lebih sederhana: setiap metode pembayaran punya akun buku besar opsional; kosong memakai akun kas/bank modul | `03` dan `15`: Tunai, Transfer, QRIS masing-masing akun berbeda; pembayaran masuk ke akun metode; metode tanpa akun masuk akun modul | Odoo memakai akun **"uang di jalan" (outstanding)** sampai dicocokkan dengan mutasi bank; kita langsung ke bank. Peluang: opsi akun penampung per metode (mis. QRIS menunggu settlement) |
| 4 | **Tanggal kunci** (pajak, tahun fiskal, penjualan, pembelian): dokumen terposting di periode kunci tidak bisa dikembalikan ke draf | Ada: periode bisa **ditutup** lalu **dikunci**; posting ke periode tertutup ditolak (tes `JournalIntegrityTest`) | `14`: posting jurnal, kembalikan ke draf, edit di periode tertutup/terkunci; harus ditolak | Odoo juga punya **kunci keras** yang tidak bisa dibatalkan; kita: periode terkunci masih bisa **dibuka kembali**. Putuskan: apakah perlu kunci permanen (mis. setelah tahun fiskal diaudit) |
| 5 | **Pengecualian kunci per pengguna**: waktu terbatas, per jenis kunci, bisa dicabut, tidak berlaku di perusahaan lain | Padanannya: **override PIN rekan** (token berumur pendek, dicatat penggunaannya, hanya untuk izin yang dimiliki penolong). Belum untuk membuka periode terkunci | `98`: token override kedaluwarsa ditolak, dicabut ditolak; `14`: koreksi di periode terkunci hanya lewat penyesuaian atau buka kembali | Peluang: izin "posting di periode terkunci" sementara bagi satu pengguna dengan alasan wajib dan masa berlaku |
| 6 | **Laporan pajak** menghitung dari dokumen **terposting**; retur menetralkan | Sudah (diperbaiki 2026-10-20): Ringkasan Pajak hanya jurnal yang masuk buku besar; PPN dihitung bersih per sisi akun | `14`: jurnal draf/menunggu review tidak ikut; retur penjualan mengurangi PPN keluaran | Tambah pemeriksaan: total laporan pajak = saldo akun PPN di GL (sudah jadi hubungan angka no. 4 di `01`) |
| 7 | **Deteksi tagihan pemasok ganda** (nomor referensi pemasok + mitra + jumlah) | **Belum**: faktur pembelian tidak punya kolom nomor faktur pemasok (hanya faktur biaya logistik yang punya) | `05`: input faktur pemasok sama dua kali; sistem harus memperingatkan atau menolak | **Celah nyata untuk ditutup**: kolom nomor faktur pemasok + peringatan duplikat; peluang unggul bila disertai pencocokan jumlah dan tanggal |
| 8 | **Syarat pembayaran** (termin) dan **diskon pembayaran dini** | Sebagian: pelanggan/pemasok punya hari termin; **tidak ada** master syarat pembayaran bertingkat atau diskon dini | `07` dan `05`: faktur ikut termin kontak, jatuh tempo benar | Peluang unggul: master syarat pembayaran (mis. 2/10 net 30) dengan jurnal diskon dini otomatis |
| 9 | **Urutan nomor dokumen** tidak boleh bolong/ganda, awalan per jurnal | Ada: nomor unik per cabang, awalan dari setup cabang | `03`: dua pengguna membuat dokumen bersamaan tidak menghasilkan nomor sama | Uji beban sederhana nomor ganda lintas cabang |
| 10 | **Jejak audit** perubahan dokumen terposting; **hash tak terubah** pada entri | Ada: pencatatan aktivitas (ActivityLogger) dan pembalikan; **tidak ada** rantai hash | `98`: ubah dokumen terposting meninggalkan jejak siapa, kapan, sebelum dan sesudah | Hash berantai hanya perlu bila regulasi mewajibkan; tidak untuk sekarang |
| 11 | **Pendaftaran pembayaran massal** dengan pilihan metode otomatis per mitra | Sebagian: pembayaran per faktur dan pembayaran massal pemasok; pemilihan metode manual | `15`: bayar tiga faktur pemasok berbeda sekaligus | Pilih metode pembayaran bawaan per pemasok |
| 12 | **Rekonsiliasi**: transaksi ganda dalam satu mata uang mencapai nol, sisa 0,01 karena pembulatan ditangani | Pembulatan dua desimal di jurnal; ada uji pembulatan di `98` | `98`: baris dengan diskon persen dan PPN menghasilkan jurnal seimbang | Tampilkan peringatan bila pembulatan menghasilkan selisih satu sen |

## 2. Hasil pengecekan ulang pekerjaan 2026-10-20 terhadap pembanding Odoo

| Pekerjaan | Pembanding Odoo | Kesimpulan |
| --- | --- | --- |
| Selisih kurs faktur biaya logistik (satu akun, tanggal pembayaran) | dua akun, akhir bulan, pembalikan saat batal rekonsiliasi | **Selaras** pada prinsip dan pembalikan; **berbeda** pada akun dan tanggal (keputusan sengaja: tanggal pembayaran lebih mudah diaudit). Catat sebagai peluang laporan laba/rugi kurs terpisah |
| Akun buku besar per metode pembayaran | metode pembayaran per jurnal + akun outstanding | **Selaras sebagian**: kita belum punya akun penampung; QRIS yang menunggu settlement langsung ke bank |
| Ringkasan Pajak hanya jurnal terposting | laporan pajak dari entri terposting | **Selaras** |
| Rekonsiliasi persediaan nilai stok vs GL | Odoo memeriksa konsistensi valuasi stok dengan akuntansi (modul stock_account) | **Perlu dibandingkan** di tahap `stock_account` |
| Jurnal akuisisi aset tetap opsional | Odoo membuat aset dari baris tagihan pemasok (modul Enterprise) | **Tidak bisa dibandingkan** (Enterprise); desain kita (akun lawan dipilih) cukup |
| Penangguhan klien dan penutupan halaman publik | multi-company/portal Odoo | Tidak sebanding: fitur platform SaaS khas aplikasi ini |

## 3. Temuan yang menjadi pekerjaan baru (untuk diputuskan owner)

1. **Nomor faktur pemasok + deteksi duplikat di faktur pembelian** (baris 7). Risiko pembayaran ganda; paling cepat memberi nilai.
2. **Master syarat pembayaran dan diskon pembayaran dini** (baris 8).
3. **Kunci periode permanen** atau izin sementara membuka periode terkunci (baris 4 dan 5).
4. **Akun penampung (clearing) per metode pembayaran** (baris 3).
5. **Pelaporan laba dan rugi kurs terpisah** dan perluasan valas ke faktur penjualan/pembelian barang (baris 1).

## 4. Rencana pengambilan modul Odoo berikutnya (urutan usulan)

| Modul Odoo | Berkas tes yang dibaca | Dipakai untuk file |
| --- | --- | --- |
| `sale` | `test_sale_order`, `test_sale_to_invoice`, `test_sale_product_attribute_value_config` | `07` Penjualan |
| `purchase` | `test_purchase_order`, `test_purchase_invoice`, `test_purchase_order_report` | `05` Pembelian |
| `stock` dan `stock_account` | `test_stockvaluation`, `test_anglo_saxon_valuation_reconciliation`, `test_move`, `test_quant` | `06` Persediaan, rekonsiliasi persediaan |
| `mrp` | `test_order`, `test_bom`, `test_multicompany` | `11` Manufaktur |
| `point_of_sale` | `test_point_of_sale_flow`, `test_point_of_sale_session` | `09` POS |
| `hr_holidays` | `test_leave_requests`, `test_accrual_allocations` | `16` SDM (cuti saja; payroll Enterprise) |

Tiap modul dikerjakan dengan langkah yang sama: baca tes, rangkum aturan bisnis, periksa status di kode kita, tulis baris Tiru dan peluang Modifikasi.
