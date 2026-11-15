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
| Positif — Konfigurasi Alur Sales (draf) | Atur tahapan approval ke Kepala Gudang dan Direktur; pilih Fulfillment Mode Delivery sebelum Invoice; batas DP 10%; map akun jurnal otomatis; transaksi dapat dilakukan | Alur persetujuan dan delivery berjalan sesuai konfigurasi, invoice otomatis dibuat setelah delivery |
| Negatif — Konfigurasi Alur Sales (draf) | Input Fulfillment Mode salah (Invoice sebelum Delivery); batas DP 150% melebihi syarat; tidak ada mapping akun jurnal; transaksi ditolak pesan penolakan yang jelas dan pesan yang jelas | Transaksi ditolak, muncul pesan kesalahan yang spesifik untuk setiap konfigurasi yang salah |
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
| Positif — Membuat Quotation (draf) | Input detail produk Sentosa Farma, pilih customer Klinik Pratama Harapan Sehat, konfirmasi harga dan kuantitas, klik Kirim | Quotation dikirim ke customer dengan status待定, menerima balasan setuju dari customer |
| Negatif — Menggunakan SKU salah (draf) | Memasukkan SKU OBT-003 yang tidak tersedia, mencoba mengirim | Sistem menolak input pesan penolakan yang jelas dan tidak mengirim Quotation |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Klik Save → Submit. Submit ditolak kalau ada item yang harganya masih kosong atau nol |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tombol "Download PDF" dan "Resend to Customer" hanya aktif selama status masih Awaiting Customer Response. Begitu penawaran sudah diterima, ditolak customer, atau dikonversi, kedua tombol ini nonaktif karena penawaran sudah final |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. "Record Customer Declined": customer menolak. Catatan wajib diisi. Status menjadi Customer Declined |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. "Record Customer Negotiating": customer ingin menawar. Catatan wajib diisi. Quotation kembali ke Draft supaya harga bisa diubah, lalu di-Submit lagi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Sales Order — Modul Sales

Bab manual: [`sales/03-sales-order.md`](../../erpApiServices/docs/manualBook/sales/03-sales-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Sales Order (draf) | Input customer: Apotek Mitra Sehat; item: Paracetamol 500 mg strip 10 buah; qty: 20; harga: Rp 3.000; diskon: 5% | Sales Order dibuat, status pending approval |
| Negatif — Cek Batas Kredit Customer (draf) | Input customer: Apotek Mitra Sehat; batas kredit: melebihi limit | Penolakan pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Sales Delivery — Modul Sales

Bab manual: [`sales/04-sales-delivery.md`](../../erpApiServices/docs/manualBook/sales/04-sales-delivery.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Pengiriman (draf) | Input Sales Order OBT-001 qty 50, pilih customer Apotek Mitra Sehat, catat pengiriman 20 unit, approve oleh Kepala Gudang | Pengiriman tercatat dengan benar, SO tersisa 30, approve berhasil |
| Negatif — Mengirim Melebihi Qty (draf) | Input Sales Order OBT-001 qty 50, pilih customer Apotek Mitra Sehat, catat pengiriman 60 unit | Tidak bisa mengirim melebihi qty SO, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sistem menolak kalau qty yang diinput melebihi sisa qty yang belum dikirim untuk item tersebut — sama seperti guard di Goods Receipt (modul Purchasing) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sales Delivery baru ditolak bila: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Sales Invoice — Modul Sales

Bab manual: [`sales/05-sales-invoice.md`](../../erpApiServices/docs/manualBook/sales/05-sales-invoice.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Tagihan (draf) | Input Sales Order OBT-001, pilih pelanggan Apotek Mitra Sehat, masukkan jumlah 50 strip, klik Approve & Posting | Tagihan berjalan dengan Piutang Dagang tercatat dan PPN Keluaran dihitung dengan benar |
| Negatif — Input Jumlah Nol (draf) | Input Sales Order OBT-001, pilih pelanggan Apotek Mitra Sehat, masukkan jumlah 0, klik Approve & Posting | Tidak dapat disimpan, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sudah Dibayar (Mark as Paid) — invoice langsung dianggap lunas saat disimpan; kalau Require Payment Proof aktif di Sales Configs, wajib upload bukti pembayaran di step ini juga |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Invoice dari SO hanya bisa dibuat bila SO sudah dikonfirmasi customer. Pada mode Delivery Before Invoice, SO harus sudah punya pengiriman |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Total semua invoice aktif untuk satu SO tidak boleh melebihi total SO |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Diskon tidak boleh lebih besar dari subtotal invoice |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Sales Payment Bill — Modul Sales

Bab manual: [`sales/06-sales-payment-bill.md`](../../erpApiServices/docs/manualBook/sales/06-sales-payment-bill.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Pelanggan: Apotek Mitra Sehat; Invoice OBT-001; Jumlah: Rp500.000; Metode: Transfer Bank; Status: Lunas | Berhasil mencatat penerimaan dan mem-posting jurnal, SO status "Lunas" |
| Negatif — input salah (draf) | Pelanggan: Apotek Mitra Sehat; Invoice OBT-001; Jumlah: Rp500.000; Metode: Tunai; Status: Belum Lunas | Ditolak: Metode pembayaran harus Transfer Bank untuk SO ini, silakan periksa kembali |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi Amount, Payment Method, dan bukti pembayaran (wajib kalau Require Payment Proof aktif di konfigurasi — lihat chapter 01) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Sales Return — Modul Sales

Bab manual: [`sales/07-sales-return.md`](../../erpApiServices/docs/manualBook/sales/07-sales-return.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal bab ini | Ikuti langkah di bab manual dengan data acuan file `00` (draf Ollama tidak dapat dipakai, isi manual) | Hasil sesuai uraian bab |
| Negatif — input tidak valid | Kosongkan field wajib atau isi di luar batas | Ditolak dengan pesan yang jelas, tidak ada data tersimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Sales → Sales Returns (/sales/sales-returns) · Prasyarat: ada Sales Delivery yang sudah tercatat (barang harus sudah "terkirim" dulu sebelum bisa "dikembalikan") |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sama seperti Purchase Return, retur tidak bisa melebihi qty yang terkirim (dikurangi retur sebelumnya untuk item yang sama) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Verifikasi Sales ke Accounting — Modul Sales

Bab manual: [`sales/08-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/sales/08-verifikasi-ke-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Verifikasi semua transaksi Quotation hingga Payment tercatat di General Ledger; Trial Balance seimbang; AR Aging akurat; Jurnal HPP dari Sales Delivery ada | Semua transaksi tercatat dengan benar, laporan keuangan akurat |
| Negatif — input salah (draf) | Salah satu transaksi tidak tercatat di General Ledger; Trial Balance tidak seimbang; AR Aging tidak akurat; Tidak ada jurnal HPP dari Sales Delivery | Transaksi tidak tercatat atau salah, laporan keuangan tidak akurat, perbaikan diperlukan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Konfigurasi Jurnal Penjualan

Bab manual: [`sales/09-konfigurasi-jurnal-penjualan.md`](../../erpApiServices/docs/manualBook/sales/09-konfigurasi-jurnal-penjualan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Konfigurasi mode penjualan otomatis; aktivasi persetujuan jurnal otomatis; hasil konfigurasi tersimpan dengan benar | Konfigurasi berhasil dan terapkan pada transaksi penjualan |
| Negatif — input salah (draf) | Mencoba mengaktifkan persetujuan tanpa memilih mode penjualan; muncul pesan kesalahan tentang syarat mutlak harus dipenuhi | Konfigurasi ditolak pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Diagram Alur Sales — Modul Sales

Bab manual: [`sales/10-diagram-alur-sales.md`](../../erpApiServices/docs/manualBook/sales/10-diagram-alur-sales.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Quotation diterbitkan (draf) | Apoteker membuat quotation untuk pelanggan Klinik Pratama, melampirkan daftar produk dan harga | Quotation masuk ke status 'Menunggu Persetujuan' & karyawan penjualan menghubungi pelanggan untuk konfirmasi pesanan |
| Negatif — Input data produk salah (draf) | Apoteker memasukkan SKU yang salah pada quotation | Sistem menolak dengan pesan 'SKU tidak ditemukan, silakan periksa kembali' & quotation tidak dapat disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | MenungguCustomer -- DitolakCustomer: Record Customer Declined |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | state "Ditolak Customer" as DitolakCustomer |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Quotation hanya bisa di-Submit kalau semua item sudah punya harga lebih dari nol |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
