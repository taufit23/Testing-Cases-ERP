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
| Positif — jalur normal (draf) | Setup warehouse toko Sentosa Farma, isi stok awal produk Paracetamol 500 mg strip (SKU OBT-001), buka cash session di meja kasir utama | Transaksi POS bisa dimulai dengan lancar dan data transaksi tercatat dengan benar. |
| Negatif — input salah (draf) | Tidak melakukan stock transfer dari gudang pusat, langsung isi stok awal di toko Sentosa Bandung | Sistem menolak pengisian stok awal karena harus melalui proses stock transfer dari warehouse pusat terlebih dahulu. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Transfer akan ditolak kalau qty yang diminta melebihi stok tersedia di warehouse asal |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Pilih Warehouse (harus bertipe Store dan punya stok yang bisa dijual) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Sesi dan penjualan milik pembukanya. Kasir biasa hanya melihat sesi dan transaksi dari sesi yang ia buka sendiri. Ia tidak bisa menjual, menahan pesanan, menutup, atau melihat laporan sesi milik kasir lain; sistem menolaknya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Transaksi Penjualan — Modul POS

Bab manual: [`pos/02-transaksi-penjualan.md`](../../erpApiServices/docs/manualBook/pos/02-transaksi-penjualan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Transaksi Penjualan Tunai (draf) | Pelanggan membeli Paracetamol 500 mg strip (SKU OBT-001) di Apotek Sentosa Bandung; kasir menginput produk dan jumlah; total dibayar pelanggan dengan uang tunai; transaksi selesai. | Kasir menerima pembayaran, transaksi dicatat dalam sistem, stok produk dikurangi. |
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
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tidak bisa refund melebihi qty yang dibeli di transaksi asli, dan tidak bisa refund transaksi yang sudah Voided (transaksi batal tidak masuk akal direfund) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Tutup Cash Session — Modul POS

Bab manual: [`pos/04-tutup-cash-session.md`](../../erpApiServices/docs/manualBook/pos/04-tutup-cash-session.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menutup Sesi Kasir (draf) | Klik "Tutup Sesi", masukkan PIN, cek saldo fisik & sistem, selisih terposting otomatis ke jurnal | Selisih diteruskan ke jurnal, sesi ditutup dengan sukses |
| Negatif — Input PIN Salah (draf) | Masukkan PIN yang salah 3 kali, menerima pesan penolakan yang jelas, tidak dapat menutup sesi | Pesan kesalahan jelas dan penutupan sesi ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sesi berstatus Closed tidak bisa dipakai lagi untuk transaksi POS baru — mencoba membuat transaksi dengan sesi yang sudah closed akan ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Verifikasi POS ke Accounting — Modul POS

Bab manual: [`pos/05-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/pos/05-verifikasi-ke-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Verifikasi POS ke Accounting (draf) | Input transaksi POS dengan benar; cek akun kas dan penyesuaian persediaan; laporan keuangan akurat | Transaksi tercatat di akun kas dan persediaan, laporan keuangan akurat |
| Negatif — Verifikasi POS ke Accounting (draf) | Input transaksi POS salah; metode pembayaran tidak dipisahkan; cek akun kas dan penyesuaian persediaan; laporan keuangan tidak akurat | Transaksi tidak tercatat di akun yang tepat, laporan keuangan tidak akurat, harus diperbaiki dengan jelas pesannya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Konfigurasi POS Lanjutan — Modul POS

Bab manual: [`pos/06-konfigurasi-pos-lanjutan.md`](../../erpApiServices/docs/manualBook/pos/06-konfigurasi-pos-lanjutan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi POS (draf) | Menyetel struk dengan logo dan informasi klinik; menghubungkan jurnal ke Chart of Accounts; mengaktifkan mode offline; menggunakan kamera untuk scan barcode; menampilkan layar Customer Display; mencetak struk penjualan | Struk sesuai, jurnal otomatis masuk ke Chart of Accounts, mode offline berfungsi, data terbaca dengan baik, layar Customer Display tampil dengan benar |
| Negatif — Konfigurasi POS (draf) | Mengaktifkan mode offline tanpa koneksi internet; mencetak struk tanpa informasi klinik; menggunakan barcode yang tidak valid; menghapus jurnal mapping tanpa konfirmasi | Mode offline gagal, struk tidak sesuai, data barcode tidak terbaca, jurnal tidak otomatis masuk ke Chart of Accounts, sistem menolak konfigurasi dengan pesan error jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Saklar "Require Journal Approval" — kalau aktif, jurnal otomatis yang terbentuk dari transaksi POS dan Refund tidak langsung masuk ke General Ledger, tapi harus melalui alur persetujuan (Approval) dulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Auto-map hanya bekerja untuk branch yang memakai struktur Chart of Accounts standar bawaan sistem. Kalau branch memakai Chart of Accounts custom (dibuat manual dari nol), tombol ini tidak akan mengisi apa-apa — mapping harus diisi manual satu per satu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Diskon, Promo, Member Tier, dan Cashback — Modul POS

Bab manual: [`pos/07-diskon-promo-member-dan-cashback.md`](../../erpApiServices/docs/manualBook/pos/07-diskon-promo-member-dan-cashback.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Member Tiers (draf) | Input ID member, pilih tingkat keanggotaan Gold, cek diskon khusus Gold | Diskon 5% diterapkan pada transaksi, notifikasi keanggotaan aktif |
| Negatif — Promo "Beli N Gratis M" (draf) | Input produk tidak ada dalam promo, cek stok dan promo | Transaksi ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Opsional: Minimum Order Amount (transaksi harus mencapai nominal ini dulu supaya dapat cashback) dan Maximum Cashback Amount (batas cashback maksimal per transaksi, untuk diskon tipe persentase) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
