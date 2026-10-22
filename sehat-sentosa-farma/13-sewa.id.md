---
title: (PT Sehat Sentosa Farma) — 13. Sewa Alat Medis
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul rental untuk skenario PT Sehat Sentosa Farma. Aset sewa, pesanan sewa, deposit dan pengembalian.
visibility: internal
---

# 13. Sewa Alat Medis

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** Konfigurasi oleh **Dr. Rahmat**; transaksi sewa oleh **Dr. Rahmat** atau pengguna berperan penjualan; pembayaran oleh **Sari Wulandari**.

**Cabang aktif:** Kantor Pusat & Distribusi Jakarta (layanan sewa dikelola Pusat).

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- Pesanan sewa dari draf ke aktif lalu selesai; aset tidak bisa disewa ganda pada periode yang sama.
- Deposit dicatat sebagai kewajiban lalu dikembalikan dikurangi denda kerusakan.
- Faktur dan pembayaran sewa memakai akun sewa dan metode pembayaran.

## 1. Konfigurasi Alur Rental — Modul Rental

Bab manual: [`rental/01-konfigurasi-alur-rental.md`](../../erpApiServices/docs/manualBook/rental/01-konfigurasi-alur-rental.md)

**Input di:** `Rental → Rental Configs` (`/rental/rental-configs`).

**Perhatikan:** **Kerjakan ini SEBELUM mulai transaksi Quotation/Order.** Rantai dokumennya: **Quotation → Order → Usage Entries → Invoice → Payment Bill → Return**, dipola sama seperti modul Sales.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi Alur Rental (draf) | Atur tahapan persetujuan untuk alat medis, posting jurnal otomatis ke akun aset tetap | Proses rental alat medis berjalan lancar dengan jurnal otomatis terposting ke akun yang tepat |
| Negatif — Input Data Salah (draf) | Masukkan SKU Alkohol Swab (ALK-002) tanpa persetujuan tahapan, coba posting jurnal | Transaksi ditolak, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Rental Assets — Modul Rental

Bab manual: [`rental/02-rental-assets.md`](../../erpApiServices/docs/manualBook/rental/02-rental-assets.md)

**Input di:** `Rental → Assets` (`/rental/assets`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendaftarkan Aset (draf) | Input data aset: Kursi roda, jumlah 10, harga 2.500.000, tarif harian 50.000, stok tersedia 8 | Aset berhasil didaftar dengan status tersedia dan tarif harian sesuai |
| Negatif — Tarif Harian Salah (draf) | Input data aset: Kursi roda, jumlah 10, harga 2.500.000, tarif harian 100.000 (lebih dari harga) | Tidak dapat disimpan, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Rental Quotation — Modul Rental

Bab manual: [`rental/03-rental-quotation.md`](../../erpApiServices/docs/manualBook/rental/03-rental-quotation.md)

**Input di:** `Rental → Quotations` (`/rental/quotations`).

**Perhatikan:** **Opsional** — Rental Order tetap bisa dibuat langsung tanpa Quotation, kecuali dikonfigurasi wajib.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Quotation (draf) | Input data produk Alat Medis, pilih periode sewa 1 bulan, masukkan detail khusus, klik Kirim | Quotation terkirim ke Kafe Sehat dengan detail dan total harga yang benar |
| Negatif — Input Produk Salah (draf) | Memasukkan SKU OBT-002 (Amoxicillin) di bagian produk Alat Medis, mengirim | Sistem menolak input dan memberikan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Rental → Quotations (/rental/quotations) · Opsional — Rental Order tetap bisa dibuat langsung tanpa Quotation, kecuali dikonfigurasi wajib |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Rental Order — Modul Rental

Bab manual: [`rental/04-rental-order.md`](../../erpApiServices/docs/manualBook/rental/04-rental-order.md)

**Input di:** `Rental → Orders` (`/rental/orders`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Rental Order (draf) | Input data: Kafe Sehat, kursi roda, 1 minggu, 2 unit, harga Rp50.000/unit | Order disimpan dengan status draft, total Rp100.000 |
| Negatif — Deposit Kurang (draf) | Input deposit: 30% dari total order (Rp30.000) | Ditolak: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Klik "Preview Price" untuk melihat estimasi total sebelum benar-benar submit — berguna untuk memberi gambaran biaya ke calon penyewa tanpa harus commit dulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Usage Entries — Modul Rental

Bab manual: [`rental/05-usage-entries.md`](../../erpApiServices/docs/manualBook/rental/05-usage-entries.md)

**Input di:** `Rental → Usage Entries` (`/rental/usage-entries`).

**Perhatikan:** **Opsional** — hanya relevan kalau penagihan sewa berbasis pemakaian (bukan flat per periode).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — catat pemakaian dan tagih | Aset sewa berbasis pemakaian: catat 3 usage entry harian lalu buat Rental Invoice dari entry itu | Entry yang ikut invoice berstatus sudah ditagih; total invoice = jumlah pemakaian dikali tarif |
| Negatif — entry yang sudah ditagih ikut ditagih lagi | Buat invoice baru untuk item yang sama | Entry berstatus sudah ditagih tidak ikut lagi; tidak ada penagihan ganda |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satu entry per kombinasi item order + tanggal — tidak bisa ada dua entry dengan tanggal yang sama untuk item sewa yang sama (mencegah pemakaian tanggal yang sama tercatat dobel) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Rental Invoice — Modul Rental

Bab manual: [`rental/06-rental-invoice.md`](../../erpApiServices/docs/manualBook/rental/06-rental-invoice.md)

**Input di:** `Rental → Invoices` (`/rental/invoices`).

**Prasyarat:** Rental Order sudah **Active**.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat tagihan rental (draf) | Input Rental Order OBT-001, approve & posting ke jurnal | Tagihan rental berhasil dibuat dan diterbitkan ke klien |
| Negatif — Input data usage entries salah (draf) | Input jumlah usage entries negatif untuk Alkohol Swab ALK-002 | Penagihan ditolak pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Rental Payment Bill — Modul Rental

Bab manual: [`rental/07-rental-payment-bill.md`](../../erpApiServices/docs/manualBook/rental/07-rental-payment-bill.md)

**Input di:** `Rental → Payment Bills` (`/rental/payment-bills`).

**Prasyarat:** Rental Invoice sudah **Approved**.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Penerimaan pembayaran dari Kafe Sehat; Invoice ALK-001; Tanggal bayar 25 Mei 2023; Jumlah Rp 750.000; Status diterima; Jurnal posting dengan nomor voucher V001234 | Penerimaan tercatat, invoice diteruskan, status otomatis berubah menjadi 'Terbayar', jurnal posting berhasil |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Rental Return — Modul Rental

Bab manual: [`rental/08-rental-return.md`](../../erpApiServices/docs/manualBook/rental/08-rental-return.md)

**Input di:** `Rental → Returns` (`/rental/returns`).

**Prasyarat:** Rental Order berstatus **Active**.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Pengembalian kursi roda ke kafe; approve oleh kepala gudang; kondisi baik; deposit $100; tidak dipotong | Catatan pengembalian tercatat, sisa deposit $100 dikembalikan ke penyewa |
| Negatif — input salah (draf) | Pengembalian tabung oksigen tanpa approve; kondisi rusak; deposit $50; kerusakan dikenai biaya $25 | Ditolak: approve diperlukan sebelum pengembalian, kerusakan mengurangi sisa deposit menjadi $25 |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi qty yang dikembalikan (tidak boleh melebihi qty yang disewakan di order tersebut) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Field Damage Charge Amount hanya bisa diisi kalau Condition bukan "Good" — otomatis nonaktif untuk pengembalian kondisi baik |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Verifikasi Rental ke Accounting — Modul Rental

Bab manual: [`rental/09-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/rental/09-verifikasi-ke-accounting.md)

**Input di:** tidak ada halaman input; periksa di `Accounting → General Ledger` (`/accounting/general-ledger`) dan `Reports → Trial Balance` (`/reports/trial-balance`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Verifikasi Quotation OBT-001 di GL dengan kode akun 62101; cek Trial Balance; diagnosis: cocok | Seluruh transaksi tercatat dan seimbang |
| Negatif — input salah (draf) | Input Order OBT-001 tanpa Quotation; cek GL 62101, TB tidak seimbang; diagnosis: order tanpa basis | Tolak input pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
