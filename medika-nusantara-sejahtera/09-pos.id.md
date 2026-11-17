---
title: (PT Medika Nusantara Sejahtera) — 09. Point of Sale (Apotek)
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul pos untuk skenario PT Medika Nusantara Sejahtera. Kasir, sesi kas, pembayaran QRIS dan penutupan sesi.
visibility: internal
---

# 09. Point of Sale (Apotek)

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji kasir (POS): sesi kasir, penjualan, pembayaran, retur, dan tutup kas.
>
> **Kalau semuanya benar, artinya:** Uang di laci kasir cocok dengan catatan, dan penjualan toko langsung masuk stok dan pembukuan.


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
| Positif — Membuka Cash Session di Apotek Nusantara Bandung (draf) | Buka POS → Cash Sessions; Pilih warehouse Store "Apotek Nusantara Bandung"; Pilih cash register "Register 1"; Masukkan opening balance Rp 500.000; Klik Open Session | Session Number terbentuk, status menjadi Open; Meja kasir "Register 1" tersedia untuk transaksi |
| Negatif — Membuka Cash Session di Warehouse Central (draf) | Buka POS → Cash Sessions; Pilih warehouse Central "Kantor Pusat & Distribusi Jakarta"; Coba klik Open Session | Sesi ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Transfer akan ditolak kalau qty yang diminta melebihi stok tersedia di warehouse asal |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Pilih Warehouse (harus bertipe Store dan punya stok yang bisa dijual) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Sesi dan penjualan milik pembukanya. Kasir biasa hanya melihat sesi dan transaksi dari sesi yang ia buka sendiri. Ia tidak bisa menjual, menahan pesanan, menutup, atau melihat laporan sesi milik kasir lain; sistem menolaknya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Transaksi Penjualan — Modul POS

Bab manual: [`pos/02-transaksi-penjualan.md`](../../erpApiServices/docs/manualBook/pos/02-transaksi-penjualan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Transaksi penjualan tunai (draf) | Buka POS Transactions; tambahkan Paracetamol 500 mg strip (SKU OBT-001) 2 pcs; pilih Payment Method "Tunai"; isi Amount Tendered Rp30.000; klik Complete | Total transaksi Rp24.000, change_amount Rp6.000, transaksi selesai dengan status paid |
| Negatif — Pembayaran kurang dari total transaksi (draf) | Buka POS Transactions; tambahkan Paracetamol 500 mg strip (SKU OBT-001) 2 pcs; pilih Payment Method "Tunai"; isi Amount Tendered Rp20.000; klik Complete | Sistem menolak dan pesan penolakan yang jelas |
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
| Positif — Menutup sesi dengan selisih kurang (draf) | POS → Cash Sessions; Report; Close Session; Isi Closing Balance; Close; Debit Selisih Kas (beban), Kredit Kas Hasil Penjualan POS di Jurnal | Sesinya ditutup dan jurnal koreksi terbentuk otomatis |
| Negatif — Menutup sesi dengan closing balance lebih dari expected (draf) | POS → Cash Sessions; Close Session; Isi Closing Balance lebih besar dari Expected Balance; Tidak dapat menutup sesi, muncul pesan kesalahan | Penutupan sesi ditolak dan meminta pengisian kembali Closing Balance yang benar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau ada kekurangan kas yang harus ditanggung kasir, sistem meminta konfirmasi dulu dan baru menutup sesi setelah kasir mengonfirmasi. Penanganan kekurangan mengikuti pengaturan cabang dan saldo deposit kasir |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sesi berstatus Closed tidak bisa dipakai lagi untuk transaksi POS baru — mencoba membuat transaksi dengan sesi yang sudah closed akan ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Verifikasi POS ke Accounting — Modul POS

Bab manual: [`pos/05-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/pos/05-verifikasi-ke-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Verifikasi transaksi POS ke Accounting (draf) | Buka Accounting → Journals; Cek jurnal penjualan dan HPP dari transaksi POS di Jakarta | Semua transaksi tercatat dengan benar, stok Persediaan berkurang sesuai penjualan, Trial Balance seimbang |
| Negatif — Persediaan tidak berkurang meski banyak penjualan POS (draf) | Buka Accounting → Journals; Cek Konfigurasi POS di Jakarta; Pastikan HPP dan Persediaan dipetakan dengan benar | Fungsi HPP dan Persediaan belum dipetakan, atau biaya barang yang terjual nol; Petakan keduanya di Konfigurasi POS dan pastikan stok punya biaya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Konfigurasi POS Lanjutan — Modul POS

Bab manual: [`pos/06-konfigurasi-pos-lanjutan.md`](../../erpApiServices/docs/manualBook/pos/06-konfigurasi-pos-lanjutan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi Struk (draf) | Pilih "Full-width cart" pada Customer Display; klik "Tampilkan gambar produk"; upload logo dengan posisi tengah; masukkan teks footer "Terima kasih telah berbelanja bersama kami!"; cetak struk. | Struk mencetak logo di tengah, menampilkan foto produk, dan footer teks sesuai yang dimasukkan. |
| Negatif — Waktu Posting Jurnal (draf) | Aktifkan "Once When the Cash Session Closes" tanpa melakukan transaksi; tutup cash session. | Muncul pesan error karena tidak ada transaksi untuk diposting dalam jurnal. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Saklar "Wajibkan Persetujuan Jurnal" — kalau aktif, jurnal otomatis yang terbentuk dari transaksi POS dan Refund tidak langsung masuk ke General Ledger, tapi harus melalui alur persetujuan (Approval) dulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Auto-map hanya bekerja untuk branch yang memakai struktur Chart of Accounts standar bawaan sistem. Kalau branch memakai Chart of Accounts custom (dibuat manual dari nol), tombol ini tidak akan mengisi apa-apa — mapping harus diisi manual satu per satu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Diskon, Promo, Member Tier, dan Cashback — Modul POS

Bab manual: [`pos/07-diskon-promo-member-dan-cashback.md`](../../erpApiServices/docs/manualBook/pos/07-diskon-promo-member-dan-cashback.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Aturan diskon flash sale (draf) | Pilih "Flash Sale" pada Discount Type; isi Valid From 10:00 25/10/2023, Valid Until 14:00 25/10/2023; pilih tingkatan member Gold; cek apakah diskon muncul di transaksi kasir pada waktu 12:00 25/10/2023 | Diskon muncul dalam pilihan di POS, berlaku untuk pelanggan Gold |
| Negatif — Flash sale luar jangka waktu (draf) | Pilih "Flash Sale" pada Discount Type; isi Valid From 10:00 26/10/2023, Valid Until 14:00 25/10/2023; cek apakah diskon muncul di transaksi kasir pada waktu 12:00 25/10/2023 | Diskon tidak muncul dalam pilihan di POS, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Opsional: Minimum Order Amount (transaksi harus mencapai nominal ini dulu supaya dapat cashback) dan Maximum Cashback Amount (batas cashback maksimal per transaksi, untuk diskon tipe persentase) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Diagram Alur POS — Modul POS

Bab manual: [`pos/08-diagram-alur-pos.md`](../../erpApiServices/docs/manualBook/pos/08-diagram-alur-pos.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Transaksi penjualan dengan QRIS (draf) | Buka kasir; pilih produk OBT-002; masukkan jumlah 1; cek stok; bayar menggunakan QRIS; konfirmasi pembayaran berhasil | Stok OBT-002 berkurang, transaksi disimpan, jurnal pembayaran QRIS terbentuk |
| Negatif — Refund transaksi yang belum selesai (draf) | Coba refund transaksi status Held; cek pesan error | Tidak bisa melakukan refund, pesan penolakan yang jelas |
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
| Positif — Menerima pembayaran QRIS (draf) | Di layar pembayaran terminal, pilih metode QRIS; Kode QR muncul dengan nominal 20.000; Layar pelanggan menampilkan kode QR dan sisa waktu 30 detik; Tunggu konfirmasi pembayaran dari penyedia; Transaksi status Completed | Transaksi terposting ke akun Kliring Pembayaran Online, stok berkurang sesuai penjualan, jurnal terbentuk otomatis |
| Negatif — Mencatat kas keluar melebihi uang di laci (draf) | Di layar sesi kasir yang terbuka, pilih Kas Keluar; Isi jumlah 50.000, akun lawan Kas Laci, alasan Penjualan; Coba simpan dengan saldo laci hanya 40.000 | Sistem menolak input dan memberikan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kas keluar tidak boleh lebih besar dari uang yang ada di laci |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Catatan kas masuk dan kas keluar tidak bisa diubah atau dihapus. Koreksi dengan Balikkan, hanya selama sesi masih terbuka |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | QRIS toko sendiri (EDC atau bank): kasir mengonfirmasi sendiri bahwa pembayaran sudah diterima, karena sistem tidak bisa mengeceknya ke penyedia |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Kalau salah, klik Balikkan pada catatan itu. Sistem membuat catatan lawan beserta jurnalnya. Ini hanya bisa selama sesi masih terbuka |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
