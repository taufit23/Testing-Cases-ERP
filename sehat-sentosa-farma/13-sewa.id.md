---
title: (PT Sehat Sentosa Farma) — 13. Sewa Alat Medis
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul rental untuk skenario PT Sehat Sentosa Farma. Aset sewa, pesanan sewa, deposit dan pengembalian.
visibility: internal
---

# 13. Sewa Alat Medis

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Pesanan sewa dari draf ke aktif lalu selesai; aset tidak bisa disewa ganda pada periode yang sama.
- Deposit dicatat sebagai kewajiban lalu dikembalikan dikurangi denda kerusakan.
- Faktur dan pembayaran sewa memakai akun sewa dan metode pembayaran.

## 1. Konfigurasi Alur Rental — Modul Rental

Bab manual: [`rental/01-konfigurasi-alur-rental.md`](../../erpApiServices/docs/manualBook/rental/01-konfigurasi-alur-rental.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Konfigurasi tahap persetujuan, pemetaan akun jurnal otomatis, mode posting jurnal, aset banyak, persetujuan otomatis rental; alat medis kursi roda dipinjamkan | Alur persetujuan berjalan lancar, jurnal otomatis terbentuk, transaksi rental kursi roda masuk akun dengan benar |
| Negatif — input salah (draf) | Persetujuan tahap 2 kosong, alat medis tabung oksigen dipinjamkan; tanpa persetujuan | Transaksi ditolak, pesan: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Rental Assets — Modul Rental

Bab manual: [`rental/02-rental-assets.md`](../../erpApiServices/docs/manualBook/rental/02-rental-assets.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendaftarkan Aset (draf) | Input data aset (Nama: kursi roda, Tahun Beli: 2021, Harga Beli: 500000, Tarif Harian: 20000) | Aset berhasil didaftarkan dengan status tersedia |
| Negatif — Input Tarif Harian Nol (draf) | Input tarif harian 0 | Pengisian gagal: tarif harus lebih dari nol |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Rental Quotation — Modul Rental

Bab manual: [`rental/03-rental-quotation.md`](../../erpApiServices/docs/manualBook/rental/03-rental-quotation.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Quotation (draf) | Input SKU HRB-001, masa sewa 2 minggu, alamat klinik, total harga, dikirim ke Kepala Gudang | Quotation diterbitkan dan masuk inbox Kepala Gudang |
| Negatif — Masa Sewa Tidak Valid (draf) | Input masa sewa negatif, mengirim ke Kepala Gudang | Penawaran ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Rental → Quotations (/rental/quotations) · Opsional — Rental Order tetap bisa dibuat langsung tanpa Quotation, kecuali dikonfigurasi wajib |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Rental Order — Modul Rental

Bab manual: [`rental/04-rental-order.md`](../../erpApiServices/docs/manualBook/rental/04-rental-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Membuat order sewa kursi roda untuk klinik, memasukkan detail produk, jumlah, periode, dan deposit | Order berhasil dibuat dengan status draft, dapat diperiksa dalam daftar order |
| Negatif — input salah (draf) | Menginput harga deposit kurang dari minimal diatur, mencoba submit | Ditolak pesan penolakan yang jelas, tidak bisa disubmit |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Klik "Preview Price" untuk melihat estimasi total sebelum benar-benar submit — berguna untuk memberi gambaran biaya ke calon penyewa tanpa harus commit dulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Usage Entries — Modul Rental

Bab manual: [`rental/05-usage-entries.md`](../../erpApiServices/docs/manualBook/rental/05-usage-entries.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — catat pemakaian dan tagih | Aset sewa berbasis pemakaian: catat 3 usage entry harian lalu buat Rental Invoice dari entry itu | Entry yang ikut invoice berstatus sudah ditagih; total invoice = jumlah pemakaian dikali tarif |
| Negatif — entry yang sudah ditagih ikut ditagih lagi | Buat invoice baru untuk item yang sama | Entry berstatus sudah ditagih tidak ikut lagi; tidak ada penagihan ganda |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satu entry per kombinasi item order + tanggal — tidak bisa ada dua entry dengan tanggal yang sama untuk item sewa yang sama (mencegah pemakaian tanggal yang sama tercatat dobel) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Rental Invoice — Modul Rental

Bab manual: [`rental/06-rental-invoice.md`](../../erpApiServices/docs/manualBook/rental/06-rental-invoice.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Tagihan (draf) | Input Rental Order OBT-001, pilih periode rental, klik Approve & Posting; tagihan muncul dengan total yang benar | Tagihan berisi detail rental order dan jurnal piutang terposting dengan benar |
| Negatif — Input Data Salah (draf) | Input SKU salah pada Rental Invoice, ceklist Approve & Posting; sistem menolak input pesan penolakan yang jelas | Sistem menolak input dan memberikan pesan kesalahan yang jelas tentang masalah SKU |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Rental Payment Bill — Modul Rental

Bab manual: [`rental/07-rental-payment-bill.md`](../../erpApiServices/docs/manualBook/rental/07-rental-payment-bill.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Penerimaan pembayaran dari Kafe Sehat; Invoice RENT-001; Jumlah Rp500.000; Tanggal 2023-09-15 | Status invoice RENT-001 diterima dan ter-update menjadi "Diterima"; Jurnal penagihan dibuat otomatis |
| Negatif — input salah (draf) | Penerimaan pembayaran dari Kafe Sehat; Invoice RENT-002; Tanggal 2023-09-15; Jumlah Rp750.000 (lebih dari nominal invoice) | Input ditolak: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Rental Return — Modul Rental

Bab manual: [`rental/08-rental-return.md`](../../erpApiServices/docs/manualBook/rental/08-rental-return.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Pengembalian kursi roda ke kafe; approve kondisi baik; tidak ada kerusakan; deposit penuh dikembalikan | Proses pengembalian berhasil; sisa deposit dikreditkan ke penyewa; status asset dan deposit diperbarui dengan benar |
| Negatif — input salah (draf) | Pengembalian kursi roda ke kafe; approve kondisi buruk; kerusakan terdeteksi; deposit tidak cukup untuk mengganti kerusakan | Proses ditolak; pesan error tentang kerusakan dan kekurangan deposit; asset dan deposit tetap sama sebelumnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi qty yang dikembalikan (tidak boleh melebihi qty yang disewakan di order tersebut) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Field Damage Charge Amount hanya bisa diisi kalau Condition bukan "Good" — otomatis nonaktif untuk pengembalian kondisi baik |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Verifikasi Rental ke Accounting — Modul Rental

Bab manual: [`rental/09-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/rental/09-verifikasi-ke-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Verifikasi Rental ke Accounting (draf) | Cek General Ledger akun 71201 Sewa Alat Medis; cek Trial Balance seluruh transaksi rental | Semua transaksi rental tercatat dengan benar di pembukuan, saldo akun seimbang |
| Negatif — Verifikasi Rental ke Accounting (draf) | Input data quotation tanpa nomor invoice; Order tanpa tanggal; Invoice tanpa detail order; Payment tanpa invoice; Return tanpa payment | Transaksi ditolak karena tidak lengkap, pesan: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Diagram Alur Rental — Modul Rental

Bab manual: [`rental/10-diagram-alur-rental.md`](../../erpApiServices/docs/manualBook/rental/10-diagram-alur-rental.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Alur Sewa (draf) | Input data lengkap, proses rental mulai dari quotation hingga order, penagihan dan pembayaran selesai, aset dikembalikan sesuai aturan | Proses sewa berjalan lancar, status Rental Order dan aset diperbarui dengan benar |
| Negatif — Alur Sewa (draf) | Input data tidak lengkap atau syarat tidak terpenuhi, seperti tanggal pengembalian melebihi batas | Pengajuan ditolak dengan pesan jelas tentang kesalahan input atau syarat yang belum terpenuhi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | MenungguCustomer -- DitolakCustomer: Customer Decline |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | state "Ditolak Customer" as DitolakCustomer |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | B --/"Tidak"/ C["Activate ditolak<br/dengan pesan kekurangan aset"] |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
