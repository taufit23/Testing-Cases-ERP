---
title: (PT Sehat Sentosa Farma) — 23. General Affairs
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul general-affairs untuk skenario PT Sehat Sentosa Farma. Barang dan unit, permintaan, pengadaan, perawatan, ganti rugi dan bebas tanggungan.
visibility: internal
---

# 23. General Affairs

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Permintaan barang lewat persetujuan; stok keluar dan kapitalisasi mengikuti jatah dan kategori.
- Penyelesaian ganti rugi dari pelanggaran karyawan tertaut ke HRM; bebas tanggungan memeriksa semua kewajiban.
- Pengadaan GA menautkan PR dan PO; unit GA dapat tertaut aset tetap.

## 1. Konfigurasi General Affairs

Bab manual: [`general-affairs/01-konfigurasi-general-affairs.md`](../../erpApiServices/docs/manualBook/general-affairs/01-konfigurasi-general-affairs.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi General Affairs (draf) | Konfigurasi mode pengadaan, gudang, penegakan jatah, bebas tanggungan, jurnal, persetujuan, dan fitur terjadwal untuk cabang Klinik Pratama & Laboratorium Bekasi; hasil yang diharapkan adalah pengaturan berjalan dengan lancar | Pengaturan General Affairs berhasil dikonfigurasi sesuai aturan baku perusahaan |
| Negatif — Konfigurasi General Affairs (draf) | Menginput data jurnal tanpa persetujuan terlebih dahulu; hasil yang diharapkan adalah penolakan konfigurasi pesan penolakan yang jelas | Konfigurasi ditolak dengan pesan kesalahan yang jelas dan konfigurasi tidak berubah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mode pengadaan Purchase Request dan Blanket Agreement terkunci (tidak bisa dipilih) bila cabang belum memakai modul Purchasing. Mode Manual selalu bisa dipilih |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penjadwal berjalan di server. Bila tidak ada tanda aktif dalam dua hari, halaman menampilkan peringatan; pengguna biasa tidak dapat memperbaikinya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Barang dan Unit General Affairs

Bab manual: [`general-affairs/02-barang-dan-unit.md`](../../erpApiServices/docs/manualBook/general-affairs/02-barang-dan-unit.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendaftar Jamu (draf) | Input: Jenis Item Jamu, Kondisi Baik, Perawatan Rutin, Pensiun Tidak, Riwayat Pemegang HRB-001 | Berhasil mendaftar jamu dengan detail kondisi dan riwayat pemegang |
| Negatif — Mendaftar Unit Tanpa Nomor Tag (draf) | Input: Jenis Item Amoxicillin, Tidak Memasukkan Nomor Tag | Ditolak karena wajib memasukkan nomor tag untuk unit fisik |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jenis barang ada empat dan tidak bisa dikarang: habis pakai, serah-terima, inventaris pegawai (custody), fasilitas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Nama, kode SKU, dan satuan wajib diisi pada Item |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Unit yang masih dipegang pegawai tidak boleh dianggap bebas; pemegang saat ini ditampilkan di daftar dan detail unit |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Atur perilaku: dipakai bersama, wajib dikembalikan, dilacak masa berlakunya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Jatah, Aturan Kapitalisasi, dan Kategori Kesalahan General Affairs

Bab manual: [`general-affairs/03-jatah-kapitalisasi-dan-kategori-kesalahan.md`](../../erpApiServices/docs/manualBook/general-affairs/03-jatah-kapitalisasi-dan-kategori-kesalahan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Jatah (draf) | Menentukan jatah pengambilan barang untuk staf pembelian sebesar 500 unit per hari | Staf pembelian diberikan akses dengan batas 500 unit per hari |
| Negatif — Aturan kapitalisasi (draf) | Memasukkan obat Paracetamol ke dalam aset tetap tanpa syarat menjadi aset tetap | Sistem menolak input dan memberikan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jatah dicek saat permintaan diajukan dan saat pengeluaran diposting. Hasilnya bergantung pada mode Penegakan jatah di Configs: Mati tidak mengecek, Peringatan memberi tahu dan tetap melanjutkan, Blokir menolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Nama kategori kesalahan harus unik per cabang; nama kembar ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi nama, persentase beban pegawai, dan tandai wajib dokumen bila bukti harus dilampirkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Kebijakan Penyelesaian Ganti Rugi General Affairs

Bab manual: [`general-affairs/04-kebijakan-ganti-rugi.md`](../../erpApiServices/docs/manualBook/general-affairs/04-kebijakan-ganti-rugi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Karyawan kehilangan obat Paracetamol 500 mg strip (SKU OBT-001) dan melaporkan ke gudang; ganti rugi dengan harga beli dikurangi potongan gaji | Ganti rugi diberikan sesuai kebijakan, potongan gaji dilakukan, catatan transaksi terperinci |
| Negatif — input salah (draf) | Karyawan membeli obat Paracetamol 500 mg strip (SKU OBT-001) pribadi; laporan hilang disusupi | Laporan ditolak, karyawan diberikan penjelasan tentang kebijakan yang berlaku dan tidak dapat mengganti rugi barang yang dibeli pribadi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Metode nominal tetap wajib mengisi jumlah. Metode persentase menurut umur wajib memiliki minimal satu rentang umur (bulan dari–sampai). Metode berbasis persentase wajib mengisi persentase |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jangan menyatakan potong gaji selalu sah; pasti ada catatan hukum yang harus dibaca pengguna di layar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 5. Atur pembayaran: izinkan potong gaji (dan batas persen), izinkan cicilan (dan jumlah maksimum), wajib pengakuan pegawai, dan masa tenggang (hari) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Penerimaan Barang General Affairs

Bab manual: [`general-affairs/05-penerimaan-barang.md`](../../erpApiServices/docs/manualBook/general-affairs/05-penerimaan-barang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Penerimaan Barang General Affairs (draf) | Mencatat penerimaan barang kantor, mengisi form draf, menandatangani dan memasukkan ke sistem | Proses penerimaan berhasil, saldo awal tercatat dengan benar |
| Negatif — Input data salah (draf) | Form draf tidak lengkap, tanpa nomor transaksi atau tanggal | Tolakan: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Permintaan Barang dan Pengeluaran ke Pegawai

Bab manual: [`general-affairs/06-permintaan-dan-pengeluaran-barang.md`](../../erpApiServices/docs/manualBook/general-affairs/06-permintaan-dan-pengeluaran-barang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pegawai meminta obat Paracetamol 500 mg strip (draf) | Pegawai meminta, bagian umum cek stok, keluarkan ke pegawai sesuai jatah | Obat dikeluarkan dan diserahkan kepada pegawai dengan catatan |
| Negatif — Pegawai meminta obat yang tidak ada stok (draf) | Bagian umum menolak permintaan karena stok habis, berikan solusi alternatif | Permintaan ditolak dengan penjelasan stok habis dan saran penggantinya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | My Requests hanya tersedia bila saklar Pegawai boleh meminta sendiri menyala; bila mati, halaman menyatakan pegawai tidak bisa meminta barang di cabang ini |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hanya permintaan draf yang boleh diedit atau diajukan. Permintaan yang sudah berlanjut tidak bisa dibatalkan lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jangan mengeluarkan barang tanpa pegawai penerima; penerima wajib diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi tanggal dibutuhkan dan tujuan, tambah barang beserta jumlah (harus lebih dari nol), dan catatan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Pengembalian Barang General Affairs

Bab manual: [`general-affairs/07-pengembalian-barang.md`](../../erpApiServices/docs/manualBook/general-affairs/07-pengembalian-barang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengembalian barang (draf) | Pegawai mengembalikan obat Paracetamol (SKU OBT-001) dalam kondisi baik; dicatat dan disetujui oleh manajer keuangan | Transaksi pengembalian tercatat dengan benar, status stok diperbarui secara otomatis |
| Negatif — Kondisi barang rusak (draf) | Pegawai mencatat obat Paracetamol (SKU OBT-001) dalam kondisi rusak; manajer keuangan menolak tanpa alasan | Tidak dapat disimpan, muncul pesan galat pesan yang jelas dan harus diisi ulang dengan alasan yang valid |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jumlah yang dikembalikan tidak boleh melebihi yang masih dipegang pegawai. Bila tidak ada sisa, layar menyatakan tidak ada yang bisa dikembalikan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kondisi tiap barang wajib dipilih: baik, rusak, atau hilang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Pemesanan Unit Bersama General Affairs

Bab manual: [`general-affairs/08-pemesanan-unit-bersama.md`](../../erpApiServices/docs/manualBook/general-affairs/08-pemesanan-unit-bersama.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pemesanan unit bersama (draf) | Menjadwalkan proyektor untuk klinik, mencatat check-in dan check-out | Proyektor disiapkan sesuai jadwal, catatan check-in dan check-out tercatat dengan benar |
| Negatif — Input tanggal tidak valid (draf) | Memasukkan tanggal di masa lalu untuk pemesanan | Tidak dapat memproses pemesanan, silakan masukkan tanggal di masa depan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Waktu selesai harus setelah waktu mulai. Bila tidak, pemesanan ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Unit dengan rencana perawatan yang memblokir pemakaian saat terlambat tidak boleh dipakai selama perawatannya terlambat |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Perawatan Unit dan Masa Berlaku General Affairs

Bab manual: [`general-affairs/09-perawatan-dan-masa-berlaku.md`](../../erpApiServices/docs/manualBook/general-affairs/09-perawatan-dan-masa-berlaku.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | PT Sehat Sentosa Farma membuat rencana perawatan untuk gudang dan alat kesehatan; mencatat hasil perawatan secara rapi; memantau masa berlaku barang dengan baik | Rencana perawatan teratur, catatan akurat, penanganan barang sesuai jadwal |
| Negatif — input salah (draf) | Input data perawatan tidak lengkap; masa berlaku salah diinput | Tidak dapat membuat rencana perawatan yang valid; sistem menolak input dan memberikan pesan kesalahan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Rencana perawatan terikat pada satu unit. Nama wajib diisi, interval minimal satu hari, dan jatuh tempo berikutnya wajib diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Opsi blokir pemakaian bila terlambat membuat unit yang lewat jatuh tempo tidak bisa dipesan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Pengadaan Barang Kantor dan Program Kegiatan General Affairs

Bab manual: [`general-affairs/10-pengadaan-dan-program-kegiatan.md`](../../erpApiServices/docs/manualBook/general-affairs/10-pengadaan-dan-program-kegiatan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengadaan Barang Kantor (draf) | Membuat permintaan pengadaan kertas toilet, diteruskan ke Purchasing; stok menipis | Permintaan berhasil dikirim ke Purchasing, stok diperbarui |
| Negatif — Program Kegiatan Tidak Dibudgetkan (draf) | Input program tanpa alokasi anggaran; mencoba menyimpan | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Permintaan pengadaan berstatus draf; hanya draf yang boleh diedit atau diajukan. Setelah diproses, permintaan tidak bisa dibatalkan lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mode pengadaan yang membutuhkan Purchasing ditolak bila cabang tidak memakainya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Buka detail, klik Ajukan (bila persetujuan diwajibkan, tunggu disetujui; lewat tombol Buka Persetujuan) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item permintaan yang dirilis dari perjanjian harus bagian dari perjanjian yang dipilih |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Penyelesaian Ganti Rugi Barang General Affairs

Bab manual: [`general-affairs/11-penyelesaian-ganti-rugi.md`](../../erpApiServices/docs/manualBook/general-affairs/11-penyelesaian-ganti-rugi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Ganti rugi obat (draf) | Pegawai mengajukan ganti rugi Paracetamol 500 mg strip (OBT-001), nilai taksiran Rp200.000, disetujui manajer keuangan, pembayaran dilakukan dalam jangka waktu 7 hari | Ganti rugi diberikan sesuai nilai taksiran dan proses ditutup dengan status "Selesai" |
| Negatif — Ganti rugi alat medis (draf) | Pegawai mengajukan ganti rugi kursi roda (ALK-001) tanpa nilai taksiran, disetujui manajer keuangan | Pengajuan ditolak karena syarat nilai taksiran tidak terpenuhi pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Urutan wajib: draf → ajukan persetujuan (bila diwajibkan) → pegawai mengakui → atur pembayaran → catat pembayaran → ditutup |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila kebijakan mewajibkan pengakuan, pegawai harus mengakui lebih dulu sebelum pembayaran diatur. Tombol Mengakui tidak bisa diulang |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jumlah cicilan tidak boleh melebihi maksimum kebijakan. Jadwal pembayaran hanya bisa diatur sekali |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Cicilan potong gaji dibayar oleh proses payroll; tidak boleh dicatat manual. Pembayaran tunai dicatat manual, tidak boleh melebihi sisa terutang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Bebas Tanggungan dan Laporan General Affairs

Bab manual: [`general-affairs/12-bebas-tanggungan-dan-laporan.md`](../../erpApiServices/docs/manualBook/general-affairs/12-bebas-tanggungan-dan-laporan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Bebas Tanggungan (draf) | Pegawai mengambil Paracetamol 500 mg strip (SKU OBT-001) tanpa tanggungan, tercatat di sistem | Status barang berubah menjadi "keluar" dengan nama pegawai yang mengambilnya |
| Negatif — Input Salah (draf) | Pegawai mengambil obat tanpa nomor tanggungan, namun menulis kode SKU yang tidak sesuai | Sistem menolak permintaan dan memberikan pesan kesalahan tentang kebutuhan nomor tanggungan yang valid |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hasil pengecekan terlihat segera. Bila mode Blokir, pegawai yang punya penghalang tidak dapat diproses keluar sampai penghalang selesai |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Diagram Alur General Affairs — Modul General Affairs

Bab manual: [`general-affairs/13-diagram-alur-general-affairs.md`](../../erpApiServices/docs/manualBook/general-affairs/13-diagram-alur-general-affairs.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Alur Barang GA (draf) | Penerimaan obat Paracetamol 500 mg strip dari pemasok, input data ke sistem | Sistem menerima data dan menambah stok dengan benar |
| Negatif — Permintaan obat tak tersedia (draf) | Permintaan Vitamin C 1000 mg botol saat stok habis, tanpa pengadaan baru | Sistem menolak permintaan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | D --/"Stok kurang"/ E["Ditolak"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jadwal pemesanan satu unit tidak boleh bertabrakan dengan pemesanan lain yang masih berlaku |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Unit yang sedang dirawat, hilang, dihentikan, atau terlambat pemeriksaan yang bersifat memblokir tidak bisa dipesan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
