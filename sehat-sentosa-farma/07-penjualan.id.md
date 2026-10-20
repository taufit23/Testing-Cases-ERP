---
title: (PT Sehat Sentosa Farma) — 07. Penjualan
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul sales untuk skenario PT Sehat Sentosa Farma. Dari penawaran sampai retur penjualan.
visibility: internal
---

# 07. Penjualan

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Quotation, SO, delivery, faktur, pembayaran dan retur; HPP terjurnal saat pengiriman.
- Batas kredit pelanggan dan batas diskon (cap) ditegakkan.
- Tautan pembayaran online per faktur memakai saldo terutang; pembayaran sebagian dan lunas dicatat sekali walau webhook berulang.
- Retur: pembalikan PPN sesuai saklar konfigurasi penjualan.
- Penawaran publik dapat dibuka tanpa login lewat token dan kedaluwarsa.

## 1. Konfigurasi Alur Sales — Modul Sales

Bab manual: [`sales/01-konfigurasi-alur-sales.md`](../../erpApiServices/docs/manualBook/sales/01-konfigurasi-alur-sales.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi Alur Sales (draf) | Atur persetujuan 2 tahap, Delivery sebelum Invoice, DP minimal 15%, peta akun jurnal otomatis | Alur sales terkonfigurasi dengan benar dan dapat digunakan untuk transaksi |
| Negatif — Persyaratan Tidak Terpenuhi (draf) | Mencoba membuat SO tanpa persetujuan, Delivery setelah Invoice, DP kurang dari 10% | Transaksi ditolak pesan penolakan yang jelas, pesan yang jelas, "DP minimal 10%" |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Require Quotation for SO — kalau aktif, Sales Order wajib berasal dari Quotation yang sudah accepted customer (tidak bisa buat SO manual langsung) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Restrict Agreed Due Date to Quotation Range — kalau aktif, tanggal jatuh tempo yang disepakati di SO tidak boleh melebihi rentang validitas Quotation asalnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kapan pakai "Minimum Payment Percentage": cocok untuk bisnis yang mewajibkan uang muka (DP) sebelum barang dikirim — misalnya wajib bayar 50% dulu baru barang jalan, sisanya ditagih belakangan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Require Payment Proof — mewajibkan bukti pembayaran (upload) saat mencatat penerimaan pembayaran dari customer |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Quotation — Modul Sales

Bab manual: [`sales/02-quotation.md`](../../erpApiServices/docs/manualBook/sales/02-quotation.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Quotation (draf) | Input data produk & harga, pilih customer, klik 'Kirim', cek status di admin panel | Quotation dikirim ke Apotek Mitra Sehat dengan detail produk dan harga yang benar |
| Negatif — Menggunakan SKU salah (draf) | Memasukkan OBT-099 (SKU palsu), coba kirim | Sistem menolak & memberi pesan penolakan yang jelas, Quotation gagal dikirim |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Kalau ditolak, gunakan opsi Reject yang setara |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Record Customer Accepted hanya bisa dilakukan setelah status "sent" — tidak bisa langsung dari draft, harus melalui alur kirim dulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Sales Order — Modul Sales

Bab manual: [`sales/03-sales-order.md`](../../erpApiServices/docs/manualBook/sales/03-sales-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Sales Order (draf) | Input data produk, jumlah, harga, customer, alamat pengiriman; Approve oleh manager | Sales Order terbentuk dengan detail yang benar dan status 'Pending' |
| Negatif — Cek Batas Kredit Customer (draf) | Input customer dengan batas kredit melebihi limit; Submit | Ditolak: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Sales Delivery — Modul Sales

Bab manual: [`sales/04-sales-delivery.md`](../../erpApiServices/docs/manualBook/sales/04-sales-delivery.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Pengiriman Barang (draf) | Input Sales Order OBT-001 qty 50, pilih customer Apotek Mitra Sehat, masukkan qty 20, klik approve | Berhasil mencatat pengiriman dan update stok di gudang |
| Negatif — Mengirim Melebihi Qty SO (draf) | Coba input Sales Order OBT-001 qty 50, pilih customer Apotek Mitra Sehat, masukkan qty 60, klik approve | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sistem menolak kalau qty yang diinput melebihi sisa qty yang belum dikirim untuk item tersebut — sama seperti guard di Goods Receipt (modul Purchasing) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Sales Invoice — Modul Sales

Bab manual: [`sales/05-sales-invoice.md`](../../erpApiServices/docs/manualBook/sales/05-sales-invoice.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Tagihan (draf) | Buat Sales Invoice berdasarkan SO/Delivery; masukkan data customer & produk; approve & posting | Berhasil membuat tagihan dengan total yang benar; Piutang Dagang terposting pada jurnal akuntansi |
| Negatif — Input Data Salah (draf) | Masukkan nama customer salah; coba approve | Gagal, muncul pesan kesalahan pesan yang jelas dan tidak bisa posting ke jurnal |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sudah Dibayar (Mark as Paid) — invoice langsung dianggap lunas saat disimpan; kalau Require Payment Proof aktif di Sales Configs, wajib upload bukti pembayaran di step ini juga |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Invoice yang sudah di-export tidak bisa di-export ulang — mencegah jurnal tercatat dobel |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Sales Payment Bill — Modul Sales

Bab manual: [`sales/06-sales-payment-bill.md`](../../erpApiServices/docs/manualBook/sales/06-sales-payment-bill.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Pelanggan: Apotek Mitra Sehat; Invoice OBT-001; Jumlah: Rp500.000; Metode: Transfer Bank; Catatan: Lunas | Penerimaan tercatat, invoice diteruskan ke status lunas & jurnal posting dengan benar |
| Negatif — input salah (draf) | Pelanggan: Klinik Pratama; Invoice HRB-001; Jumlah: Rp750.000; Metode: Tunai; Catatan: Tidak valid | Input ditolak, pesan: pesan yang jelas & invoice tetap dalam status pending |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi Amount, Payment Method, dan bukti pembayaran (wajib kalau Require Payment Proof aktif di konfigurasi — lihat chapter 01) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Sales Return — Modul Sales

Bab manual: [`sales/07-sales-return.md`](../../erpApiServices/docs/manualBook/sales/07-sales-return.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Retur Penjualan (draf) | Customer mengembalikan obat Paracetamol 500 mg strip (SKU OBT-001) dari Sales Delivery No.12345; input retur valid; sistem otomatis mencatat retur dan memperbarui piutang dagang; jurnal penyesuaian dibuat | Retur tercatat, piutang dagang diperbaiki, jurnal penyesuaian benar |
| Negatif — Input Data Salah (draf) | Customer mengembalikan obat Amoxicillin 500 mg (SKU OBT-002) tetapi input SKU salah; sistem menolak retur dan memberi pesan kesalahan karena SKU tidak cocok dengan Sales Delivery No.12345; retur ditolak | Retur ditolak, pesan kesalahan jelas tentang kesalahan input SKU |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Sales → Sales Returns (/sales/sales-returns) · Prasyarat: ada Sales Delivery yang sudah tercatat (barang harus sudah "terkirim" dulu sebelum bisa "dikembalikan") |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sama seperti Purchase Return, retur tidak bisa melebihi qty yang terkirim (dikurangi retur sebelumnya untuk item yang sama) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Verifikasi Sales ke Accounting — Modul Sales

Bab manual: [`sales/08-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/sales/08-verifikasi-ke-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Verifikasi Quotation OBT-001 ke Invoice dengan benar di General Ledger; Trial Balance seimbang; AR Aging tidak terlambat lunas | Seluruh transaksi tercatat dan akurat dalam sistem akuntansi |
| Negatif — input salah (draf) | Input SO untuk OBT-002 tanpa Quotation; AR Aging menunjukkan banyak piutang lama | Verifikasi ditolak karena SO tanpa dasar Quotation; pesan error muncul mengingatkan syarat mutlak terpenuhi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Konfigurasi Jurnal Penjualan

Bab manual: [`sales/09-konfigurasi-jurnal-penjualan.md`](../../erpApiServices/docs/manualBook/sales/09-konfigurasi-jurnal-penjualan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menyusun jurnal penjualan dengan data produk Paracetamol 500 mg strip (SKU OBT-001) dan Amoxicillin 500 mg (OBT-002), menentukan kategori obat, mengonfigurasi metode pembayaran tunai | Jurnal penjualan berhasil disusun dengan data produk dan metode pembayaran yang benar |
| Negatif — input salah (draf) | Mengonfigurasi jurnal penjualan tanpa memasukkan SKU produk atau metode pembayaran | Konfigurasi ditolak pesan penolakan yang jelas dan pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
