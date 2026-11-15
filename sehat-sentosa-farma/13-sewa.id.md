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
| Positif — Konfigurasi alur persetujuan rental (draf) | Masuk ke `/rental/rental-configs`, Aktifkan "Require Rental Quotation Approval", "Require Rental Order Approval" dan "Require Rental Invoice Approval"; pilih "Auto" untuk Mode Posting Jurnal; konfigurasi Aset Berjumlah Banyak. | Alur persetujuan rental ditentukan, jurnal otomatis disetup, mode posting jurnal diaktifkan, aset berjumlah banyak dikonfigurasi dengan benar. |
| Negatif — Pengaturan alur persetujuan tidak lengkap (draf) | Masuk ke `/rental/rental-configs`, Aktifkan "Require Rental Quotation Approval" saja; coba submit dokumen rental. | Submit gagal, pesan penolakan yang jelas. |
| Positif — Pemetaan akun jurnal otomatis (draf) | Masuk ke `/rental/rental-configs`, pilih "Rental AR", "Rental Revenue" dll; klik tombol "Auto Map". | Akun jurnal otomatis rental dipetakan, jurnal pengembalian deposit menggunakan pemetaan ini. |
| Negatif — Pemetaan akun tidak lengkap (draf) | Masuk ke `/rental/rental-configs`, hanya pilih "Rental AR"; coba submit dokumen rental. | Submit gagal, pesan penolakan yang jelas. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Rental Assets — Modul Rental

Bab manual: [`rental/02-rental-assets.md`](../../erpApiServices/docs/manualBook/rental/02-rental-assets.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendaftarkan kursi roda (draf) | Klik "+ Add Asset"; Isi Asset Code: ALK-001, Asset Name: Kursi Roda Medis, Description: Kursi roda medis untuk pasien; Daily Rate: 25000; Klik Create | Aset Kursi Roda Medis muncul di daftar aset dengan status Available |
| Negatif — Mendaftarkan aset tanpa stok (draf) | Isi Asset Code: ALK-001, Asset Name: Kursi Roda Medis, Daily Rate: 25000; Coba klik Create tanpa menambahkan stok di gudang | Muncul pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Rental Quotation — Modul Rental

Bab manual: [`rental/03-rental-quotation.md`](../../erpApiServices/docs/manualBook/rental/03-rental-quotation.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Quotation baru (draf) | Buka Quotations; "+ Create"; Contact: Apotek Mitra Sehat; Start Date: 1 Januari 2023; End Date: 31 Desember 2023; Tambah item: kursi roda qty 5, tarif Rp 100.000/hari; Klik Save → Submit | Quotation baru berstatus Submitted dengan detail sesuai input |
| Negatif — Mencoba hapus Quotation yang sudah dikonversi (draf) | Buka Quotation yang sudah dikonversi ke Rental Order; Coba klik Delete | Pesan error muncul: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Rental → Quotations (/rental/quotations) · Opsional — Rental Order tetap bisa dibuat langsung tanpa Quotation, kecuali dikonfigurasi wajib |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Rental Order — Modul Rental

Bab manual: [`rental/04-rental-order.md`](../../erpApiServices/docs/manualBook/rental/04-rental-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Rental Order (draf) | Klik "Convert to Order" dari detail Quotation OBT-001; isi Contact Sehat Sentosa Farma, Start Date 1 Januari 2023, End Date 31 Januari 2023; tambah item Alkohol Swab ALK-002 qty 50; klik "Preview Price"; Save | Order OBT-001 dibuat dengan total harga sesuai preview; status Draft |
| Negatif — Deposit Tidak Tersedia (draf) | Cek detail Order OBT-001 setelah Save; deposit tidak muncul di form Create | Harus mengisi field Deposit Amount lewat halaman Edit Order; pesan penolakan yang jelas jika ditinggalkan kosong |
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
| Positif — Membuat tagihan rental (draf) | Buka Invoices; "+ Create"; pilih Rental Order OBT-001; Save | Tagihan ditampilkan dengan total sesuai order; status Draft |
| Negatif — Tidak ada usage entry (draf) | Semua Usage Entry untuk order ini sudah pernah ditagih; cek Usage Entries | Tidak ada opsi Usage Entry yang bisa dipilih, tagihan tidak dapat dibuat |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Rental Payment Bill — Modul Rental

Bab manual: [`rental/07-rental-payment-bill.md`](../../erpApiServices/docs/manualBook/rental/07-rental-payment-bill.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat bayaran rental (draf) | Buka Payment Bills; klik "+ Create"; pilih Rental Invoice OBT-001; isikan Amount 50000, Payment Method Transfer; klik Save | Payment Bill terbentuk; status Rental Invoice OBT-001 menjadi Partial |
| Negatif — Menciptakan Payment tanpa approval invoice (draf) | Buka Payment Bills; klik "+ Create"; pilih Rental Invoice OBT-002; isikan Amount 75000, Payment Method Cash; klik Save | Tidak bisa membuat Payment Bill; pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Rental Return — Modul Rental

Bab manual: [`rental/08-rental-return.md`](../../erpApiServices/docs/manualBook/rental/08-rental-return.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengembalian kondisi baik (draf) | Buka Returns; pilih Rental Order OBT-001; tentukan Condition "Good"; qty 50; klik Save | Aset OBT-001 kembali ke status Available; tidak ada potongan deposit; jurnal terbentuk mengurangi Rental AR/Revenue |
| Negatif — Kondisi item masih Good (draf) | Buka Returns; pilih item OBT-001; tentukan Condition "Damaged"; Damage Charge Amount 5000; qty 50; klik Save | Damage Charge Amount tidak bisa diisi; pesan penolakan yang jelas muncul; Condition tetap Good; jurnal tidak terbentuk |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi qty yang dikembalikan (tidak boleh melebihi qty yang disewakan di order tersebut) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Field Damage Charge Amount hanya bisa diisi kalau Condition bukan "Good" — otomatis nonaktif untuk pengembalian kondisi baik |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Verifikasi Rental ke Accounting — Modul Rental

Bab manual: [`rental/09-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/rental/09-verifikasi-ke-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Verifikasi Rental ke Accounting berhasil (draf) | Buka General Ledger; Detail Ledger Rental AR bertambah; Rental Revenue bertambah; Rental Deposit Liability berkurang; Kas/Bank bertambah; Trial Balance seimbang | Semua akun tercatat dengan benar, transaksi rental dorekkan dengan akuntansi |
| Negatif — Invoice belum di-Export to Journal (draf) | Buka detail invoice OBT-001; Export to Journal tidak dilakukan; Rental Revenue tidak bertambah; Trial Balance tidak seimbang | Periksa dan export invoice ke jurnal, perbaiki keseimbangan trial balance |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Diagram Alur Rental — Modul Rental

Bab manual: [`rental/10-diagram-alur-rental.md`](../../erpApiServices/docs/manualBook/rental/10-diagram-alur-rental.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Alur sewa dari awal sampai akhir (draf) | Masuk ke modul Rental; Buat Quotation OBT-001; Konversi Quotation menjadi Order; Bayar Invoice; Kembalikan Aset ALK-001; Approve Pengembalian | Quotation diterima, Order Active, Invoice dibuat, Pembayaran dilakukan, Aset dikembalikan status Available, Jurnal pembayaran terbentuk |
| Negatif — Input salah dalam Rental Quotation (draf) | Masuk ke modul Rental; Buat Quotation OBT-001 dengan data salah; Coba Konversi Quotation menjadi Order | Muncul pesan penolakan yang jelas atau pesan yang jelas, Quotation tidak berubah status |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | MenungguCustomer -- DitolakCustomer: Customer Decline |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | state "Ditolak Customer" as DitolakCustomer |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | B --/"Tidak"/ C["Activate ditolak<br/dengan pesan kekurangan aset"] |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
