---
title: (PT Sehat Sentosa Farma) — 09. Point of Sale (Apotek)
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul pos untuk skenario PT Sehat Sentosa Farma. Kasir, sesi kas, pembayaran QRIS dan penutupan sesi.
visibility: internal
---

# 09. Point of Sale (Apotek)

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Satu sesi per kasir; modal awal, hitung pecahan, selisih kas menurut mode.
- Transaksi tunai dan QRIS; QRIS membuat transaksi pending lalu lunas setelah webhook; layar pelanggan ikut menampilkan QR.
- Hold, void, retur dengan persetujuan; mode offline dan antrean sinkron.
- Jurnal POS per sesi atau langsung; promo, cashback, member.

## 1. Setup Toko & Cash Session — Modul POS

Bab manual: [`pos/01-setup-toko-dan-cash-session.md`](../../erpApiServices/docs/manualBook/pos/01-setup-toko-dan-cash-session.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Setup warehouse toko Sentosa Farma, isi stok awal produk Paracetamol 500 mg strip (SKU OBT-001), buka cash session di meja kasir kantor pusat | Transaksi POS dapat dimulai dengan lancar dan data transaksi tercatat dengan benar |
| Negatif — input salah (draf) | Mencoba membuka cash session tanpa setup warehouse atau isi stok awal, mencoba menggunakan meja kasir yang tidak diberikan izin | Sistem menolak akses pesan penolakan yang jelas dan pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Transfer akan ditolak kalau qty yang diminta melebihi stok tersedia di warehouse asal |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Pilih Warehouse (harus bertipe Store dan punya stok yang bisa dijual) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Sesi dan penjualan milik pembukanya. Kasir biasa hanya melihat sesi dan transaksi dari sesi yang ia buka sendiri. Ia tidak bisa menjual, menahan pesanan, menutup, atau melihat laporan sesi milik kasir lain; sistem menolaknya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Transaksi Penjualan — Modul POS

Bab manual: [`pos/02-transaksi-penjualan.md`](../../erpApiServices/docs/manualBook/pos/02-transaksi-penjualan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Transaksi Penjualan Tunai (draf) | Pelanggan membeli Paracetamol 500 mg strip (SKU OBT-001) di Apotek Sentosa Bandung; kasir memasukkan SKU dan jumlah, total dibayar pelanggan; transaksi selesai dengan kembalian jika ada. | Transaksi berhasil dilakukan, tercatat pada sistem POS. |
| Negatif — Split Payment Ditolak (draf) | Pelanggan mencoba split payment di Apotek Sentosa Bandung tetapi saldo di kartu hanya 50%; kasir menolak transaksi dan memberikan pesan penolakan yang jelas. | Transaksi ditolak dengan pesan jelas bahwa saldo tidak memadai. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tunai — isi Amount Tendered (uang yang diberikan pelanggan); changeamount (kembalian) terhitung otomatis. Amount Tendered harus ≥ total transaksi, tidak bisa kurang |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kartu Debit/Kredit — tidak ada kembalian, nominal harus pas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pesanan yang sudah Completed atau Voided tidak bisa di-Resume lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap transaksi POS terikat ke Cash Session yang aktif, yang terikat ke satu Warehouse. Stok yang berkurang selalu dari warehouse toko tersebut — tidak bisa "meminjam" stok dari warehouse toko lain, meskipun produk yang sama ada stoknya di toko sebelah |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Void & Refund — Modul POS

Bab manual: [`pos/03-void-dan-refund.md`](../../erpApiServices/docs/manualBook/pos/03-void-dan-refund.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — void transaksi Held | Buat transaksi OBT-001 × 2 lalu tahan (Held), buka detailnya dan Void dengan alasan | Transaksi berstatus Voided; stok tidak berubah karena belum pernah dikurangi |
| Positif — refund sebagian transaksi Completed | Transaksi OBT-001 × 10 selesai; Refund 3 strip dengan alasan barang rusak | Stok bertambah 3 di warehouse asal; jurnal kontra mengurangi Penjualan dan Kas Hasil Penjualan POS sebesar nilai 3 strip |
| Negatif — refund melebihi qty yang dibeli | Refund 11 strip pada transaksi yang hanya 10 strip | Ditolak; tidak ada perubahan stok dan jurnal |
| Negatif — void transaksi yang sudah punya refund | Void transaksi yang sebelumnya sudah di-refund sebagian | Ditolak secara khusus karena akan menghitung ganda qty yang sudah dikembalikan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Pilih item & qty yang dikembalikan (bisa sebagian, tidak harus seluruh transaksi) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tidak bisa refund melebihi sisa qty yang masih bisa di-refund untuk tiap item (qty beli dikurangi yang sudah pernah di-refund), dan tidak bisa refund transaksi yang sudah Voided. Refund hanya untuk transaksi berstatus Completed |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Transaksi yang sudah pernah di-refund tidak bisa di-Void, supaya jurnal penjualan tidak terbalik dua kali. Untuk koreksi lanjutan, lakukan refund tambahan. Pembayaran QRIS yang sudah diterima juga membuat Void ditolak, karena pembayarannya sudah sah |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Tutup Cash Session — Modul POS

Bab manual: [`pos/04-tutup-cash-session.md`](../../erpApiServices/docs/manualBook/pos/04-tutup-cash-session.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menutup Sesi Kasir (draf) | Apotek Sentosa Bandung menutup sesi kasir, menghitung selisih Rp 25.000, terposting ke jurnal penjualan | Selisih tercatat dan otomatis masuk jurnal penjualan |
| Negatif — Input Uang Laci Salah (draf) | Apotek Sentosa Bandung memasukkan uang laci Rp 1.000.000 namun seharusnya Rp 975.000, sistem menolak input dan memberikan pesan kesalahan | Input ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau ada kekurangan kas yang harus ditanggung kasir, sistem meminta konfirmasi dulu dan baru menutup sesi setelah kasir mengonfirmasi. Penanganan kekurangan mengikuti pengaturan cabang dan saldo deposit kasir |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sesi berstatus Closed tidak bisa dipakai lagi untuk transaksi POS baru — mencoba membuat transaksi dengan sesi yang sudah closed akan ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Verifikasi POS ke Accounting — Modul POS

Bab manual: [`pos/05-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/pos/05-verifikasi-ke-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Verifikasi POS ke Accounting (draf) | Transaksi OBT-001 di POS masuk jurnal dengan benar; metode pembayaran masuk akun kas 12101; HPP dan persediaan diperbarui; laporan keuangan akurat. | Transaksi tercatat dan disesuaikan dengan benar, laporan keuangan akurat. |
| Negatif — Input HPP Salah (draf) | Transaksi OBT-001 di POS input HPP 5000 per item; jurnal POS tidak sesuai; HPP tidak diperbarui; pesan kesalahan "HPP tidak valid". | Input HPP salah, transaksi ditolak dengan pesan jelas. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Konfigurasi POS Lanjutan — Modul POS

Bab manual: [`pos/06-konfigurasi-pos-lanjutan.md`](../../erpApiServices/docs/manualBook/pos/06-konfigurasi-pos-lanjutan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Konfigurasi struk untuk apotek Sentosa Bandung dengan logo dan informasi khusus | Struk terkonfigurasi dengan benar, mencakup logo dan informasi spesifik apotek |
| Negatif — input salah (draf) | Mencoba mengonfigurasi struk tanpa logo atau informasi yang diperlukan | Konfigurasi ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Saklar "Require Journal Approval" — kalau aktif, jurnal otomatis yang terbentuk dari transaksi POS dan Refund tidak langsung masuk ke General Ledger, tapi harus melalui alur persetujuan (Approval) dulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Auto-map hanya bekerja untuk branch yang memakai struktur Chart of Accounts standar bawaan sistem. Kalau branch memakai Chart of Accounts custom (dibuat manual dari nol), tombol ini tidak akan mengisi apa-apa — mapping harus diisi manual satu per satu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Diskon, Promo, Member Tier, dan Cashback — Modul POS

Bab manual: [`pos/07-diskon-promo-member-dan-cashback.md`](../../erpApiServices/docs/manualBook/pos/07-diskon-promo-member-dan-cashback.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Member Tiers (draf) | Buat aturan member: Platinum (10%), Gold (5%), Silver (2%) | Kasir dapat memilih tingkatan member saat transaksi dan diskon diterapkan sesuai aturan |
| Negatif — Promo "Beli 3 Gratis 1" (draf) | Input produk tidak termasuk dalam promo | Transaksi ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Opsional: Minimum Order Amount (transaksi harus mencapai nominal ini dulu supaya dapat cashback) dan Maximum Cashback Amount (batas cashback maksimal per transaksi, untuk diskon tipe persentase) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Diagram Alur POS — Modul POS

Bab manual: [`pos/08-diagram-alur-pos.md`](../../erpApiServices/docs/manualBook/pos/08-diagram-alur-pos.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Buka kasir, transaksi penjualan obat Paracetamol 500 mg strip (SKU OBT-001), bayar QRIS, tutup kasir; stok berkurang, transaksi tercatat | Proses selesai dengan benar, stok dan transaksi akurat |
| Negatif — input salah (draf) | Void transaksi tanpa buka kasir terlebih dahulu; pesan penolakan yang jelas muncul | Tidak dapat void tanpa memenuhi syarat, pesan jelas diberikan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | H --/"Ya, mode Block"/ I["Close ditolak<br/Resume atau batalkan dulu"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | H --/"Tidak"/ K["Hitung kas fisik<br/bandingkan dengan kas seharusnya"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kasir hanya bisa memakai Cash Session yang ia buka sendiri, kecuali ia manager |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | H --/"Kedaluwarsa, ditolak, atau dibatalkan"/ I(["Status Voided<br/stok tidak pernah berkurang"]) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Pembayaran QRIS, Kas Masuk dan Keluar Manual, serta Deposit Kasir — Modul POS

Bab manual: [`pos/09-qris-kas-masuk-keluar-dan-deposit-kasir.md`](../../erpApiServices/docs/manualBook/pos/09-qris-kas-masuk-keluar-dan-deposit-kasir.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menerima pembayaran QRIS (draf) | Kasir menerima pembayaran QRIS pelanggan, transaksi tercatat dengan benar di POS, pelanggan mendapatkan struk resmi | Transaksi sukses, struk diberikan kepada pelanggan |
| Negatif — Input nomor QRIS salah (draf) | Sistem menolak transaksi, memberikan pesan kesalahan input nomor QRIS tidak valid, kasir memasukkan nomor QRIS yang benar kembali | Transaksi ditolak, kasir diminta memasukkan nomor QRIS yang valid |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kas keluar tidak boleh lebih besar dari uang yang ada di laci |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Catatan kas masuk dan kas keluar tidak bisa diubah atau dihapus. Koreksi dengan Balikkan, hanya selama sesi masih terbuka |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | QRIS toko sendiri (EDC atau bank): kasir mengonfirmasi sendiri bahwa pembayaran sudah diterima, karena sistem tidak bisa mengeceknya ke penyedia |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Kalau salah, klik Balikkan pada catatan itu. Sistem membuat catatan lawan beserta jurnalnya. Ini hanya bisa selama sesi masih terbuka |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
