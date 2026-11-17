---
title: (PT Medika Nusantara Sejahtera) — 05. Pembelian
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul purchasing untuk skenario PT Medika Nusantara Sejahtera. Dari permintaan sampai pembayaran pemasok.
visibility: internal
---

# 05. Pembelian

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji proses membeli: dari meminta barang, menawar, memesan, menerima, menagih, sampai membayar pemasok.
>
> **Kalau semuanya benar, artinya:** Barang yang dibeli masuk stok, utang tercatat, dan pembayaran melunasi utang itu. Tidak ada barang diterima atau uang dibayar melebihi yang dipesan.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- PR lalu PQ lalu PO lalu GR lalu PI lalu pembayaran; urutan GR dan faktur mengikuti konfigurasi.
- Penerimaan tidak boleh melebihi sisa PO; pembayaran tidak boleh melebihi faktur; faktur belum disetujui tidak bisa dibayar.
- PO dengan pengiriman bertahap dan pemberitahuan pengiriman pemasok (halaman publik).
- Faktur biaya logistik: alokasi landed cost, pembebanan ulang ke pelanggan, selisih kurs bila akunnya diatur.
- Pencocokan faktur dengan barang diterima (mati, peringatkan, tolak) dan produk yang tidak dapat dibeli tidak muncul di pemilih.

## 1. Konfigurasi Alur Purchasing — Modul Purchasing

Bab manual: [`purchasing/01-konfigurasi-alur-purchasing.md`](../../erpApiServices/docs/manualBook/purchasing/01-konfigurasi-alur-purchasing.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi alur purchasing (draf) | Masuk ke `Pembelian → Purchase Configs`, aktifkan "Require PO Approval", pilih "Goods Receipt First" untuk PO Flow Mode, simpan konfigurasi. | Alur purchasing berubah menjadi memerlukan persetujuan PO dan GR harus diterima terlebih dahulu sebelum PI bisa dibuat. |
| Negatif — Konfigurasi alur purchasing (draf) | Masuk ke `Pembelian → Purchase Configs`, cek "Require PO Approval" tanpa mengaktifkannya, coba membuat PO baru. | Muncul pesan kesalahan bahwa persetujuan PO diperlukan sebelum membuat PO baru. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Urutan GR vs PI — barang harus diterima dulu baru bisa ditagih, atau tagihan boleh datang duluan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Ini pengaturan paling penting untuk dipahami — menentukan urutan wajib antara menerima barang (GR) dan menagih (PI) setelah PO dibuat: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penting: begitu satu PO sudah punya minimal 1 Goods Receipt atau 1 Purchase Invoice, PO tersebut terkunci — item-nya tidak bisa diubah lagi. Pastikan PO sudah benar sebelum lanjut ke GR/PI |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Manual — staff harus klik "Ekspor ke Jurnal" sendiri di halaman detail dokumen |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Purchase Request — Modul Purchasing

Bab manual: [`purchasing/02-purchase-request.md`](../../erpApiServices/docs/manualBook/purchasing/02-purchase-request.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat PR untuk Paracetamol 500 mg strip (draf) | Buka Purchase Requests; klik "+ Buat"; isi Date: 2023-10-01, Expected Date Needed: 2023-10-05, Department: Gudang; tambah item Paracetamol 500 mg strip (SKU OBT-001), Unit: box, Qty: 100; klik Save | PR dibuat dengan status Draft, nomor otomatis, item Paracetamol 500 mg strip terdaftar |
| Negatif — Submit PR tanpa menambahkan item (draf) | Buka detail PR, klik "Ajukan"; PR tidak boleh diajukan tanpa item | PR ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | PR yang sudah Submit tidak bisa diedit lagi — kalau ada revisi, PR harus dibatalkan (Cancel) dan dibuat ulang, atau ditolak (Reject, kalau lewat approval) lalu dibuatkan versi baru |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Purchase Quotation — Modul Purchasing

Bab manual: [`purchasing/03-purchase-quotation.md`](../../erpApiServices/docs/manualBook/purchasing/03-purchase-quotation.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat PQ untuk supplier baru (draf) | Buka Purchase Quotations; klik "+ Buat"; pilih PT Alkes Prima Mandiri sebagai Contact; masukkan tanggal 10 Januari 2023 dan Expected Date Needed 15 Januari 2023; tambahkan item Paracetamol 500 mg strip dengan Qty Requested 1000; klik Save | Purchase Quotation berhasil dibuat untuk PT Alkes Prima Mandiri, status menjadi Draft |
| Negatif — Mengirim RFQ tanpa menentukan pemenang (draf) | Dari detail PQ Draft, klik Mark RFQ Sent; unduh dan kirim RFQ ke supplier; tidak memilih pemenang di halaman Compare Quotations; coba Submit PQ | Muncul pesan error pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Setelah supplier membalas, isi harga satu per satu atau klik Import Prices dan unggah Excel RFQ yang sudah diisi supplier. Baris yang tidak cocok dengan item di PQ ditolak, dan impor hanya bisa selama PQ masih Draft |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Kalau supplier tidak menyediakan sebuah item, tandai Not Available at this supplier. Harga harus lebih dari nol. Selain itu, tiap item harus punya harga supplier atau ditandai tidak tersedia sebelum PQ bisa di-Submit |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau satu produk ditawarkan oleh lebih dari satu PQ, Anda wajib memilih supplier pemenang di halaman Compare Quotations sebelum PQ bisa di-Submit. Hanya satu penawaran boleh dipilih per produk |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penawaran tanpa harga atau yang ditandai tidak tersedia tidak bisa dipilih. Pilihan terkunci setelah produknya dipesan lewat PO |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Purchase Order — Modul Purchasing

Bab manual: [`purchasing/04-purchase-order.md`](../../erpApiServices/docs/manualBook/purchasing/04-purchase-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat PO dari PQ (draf) | Login sebagai Apoteker Penanggung Jawab; klik "Convert to PO" PQ OBT-001; pilih supplier PT Bintang Farmasi Utama; set item, qty 500; klik "Simpan"; status PO menjadi "Draf". | Form PO ter-prefill dengan detail PQ, subtotal, tax dan total otomatis; tombol "Ajukan" muncul. |
| Negatif — Mengubah item PO setelah GR (draf) | Login sebagai Kepala Gudang; buka PO OBT-001 yang sudah ada GR; coba ubah qty item; pesan muncul "Item PO terkunci". | Item PO tidak bisa diubah, hanya bisa dilakukan penyesuaian melalui Purchase Return. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Anggaran: bila Budget Enforcement aktif (bab 01), total PO dari satu Purchase Request tidak boleh melebihi perkiraan anggaran di PR itu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item Purchase Request yang sudah dipesan lewat PO lain tidak bisa dipesan lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Expected Delivery Date tidak boleh sebelum tanggal PO |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Baris yang terhubung ke item Sales Order harus berasal dari Sales Order yang sama |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Goods Receipt — Modul Purchasing

Bab manual: [`purchasing/05-goods-receipt.md`](../../erpApiServices/docs/manualBook/purchasing/05-goods-receipt.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat penerimaan barang (draf) | Buka "Purchasing → Purchase Receipts"; "+ Buat", pilih PO dari Medika Nusantara; isi qty diterima 100 unit Paracetamol 500 mg strip OBT-001; klik Save. | Status GR berubah menjadi Approved, stok Persediaan bertambah 100 unit Paracetamol 500 mg strip OBT-001, jurnal terbentuk dari Debit akun Persediaan ke Kredit Utang Dagang. |
| Negatif — Menerima melebihi qty PO (draf) | Buka GR, isi qty diterima 120 unit Paracetamol 500 mg strip OBT-001 (melebihi sisa 100 unit); coba klik Save. | Sistem menampilkan pesan error pesan yang jelas, GR tidak bisa disimpan. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tiap baris punya isian Rejected Quantity untuk barang yang diterima tetapi ditolak. Nilainya tidak boleh melebihi qty diterima. Bagian yang ditolak tidak ikut masuk stok (lihat bab 16. Dampak Stok dari Pembelian) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sistem menolak kalau qty yang diinput di GR melebihi sisa qty yang belum diterima untuk item tersebut — muncul pesan error jelas di form sebelum sempat disimpan. Ini mencegah pencatatan penerimaan barang lebih banyak dari yang sebenarnya dipesan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | GR yang sudah di-export tidak bisa di-export ulang — sistem menolak untuk mencegah jurnal tercatat dobel |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Purchase Invoice — Modul Purchasing

Bab manual: [`purchasing/06-purchase-invoice.md`](../../erpApiServices/docs/manualBook/purchasing/06-purchase-invoice.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Tagihan Supplier (draf) | Buka Purchase Invoices; klik "+ Buat"; pilih PO OBT-001 sumbernya; isi item Paracetamol 500 mg strip 200 box; masukkan PPN Masukan 11%; klik Save | Subtotal PO ditampilkan; tagihan disimpan dengan status draft |
| Negatif — Tombol Create Disabled (draf) | Buka PO OBT-001; cek tombol Create Purchase Invoice; PO belum Approved; Flow Mode = Goods Receipt First tanpa GR yang sudah dibuat | Tombol Create Purchase Invoice terkunci; pesan penolakan yang jelas muncul |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Purchase Payment Bill — Modul Purchasing

Bab manual: [`purchasing/07-purchase-payment-bill.md`](../../erpApiServices/docs/manualBook/purchasing/07-purchase-payment-bill.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membayar invoice (draf) | Buka Purchase Payment Bills; pilih PI OBT-001 (sisa: Rp 500.000); pilih mode Single; masukkan Amount Rp 500.000; pilih Payment Method Transfer Bank; klik Save | Invoice OBT-001 tercatat lunas, jurnal debit Utang Dagang dan kredit Kas/Bank dibuat |
| Negatif — Membayar invoice tanpa approval (draf) | Buka Purchase Payment Bills; pilih PI OBT-002 (sisa: Rp 750.000); pilih mode Single; masukkan Amount Rp 750.000; pilih Payment Method Transfer Bank; coba klik Save | Sistem menolak pembuatan Payment Bill pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bukti pembayaran: kalau Require Payment Proof aktif di Purchase Configs, Payment Bill tidak bisa disimpan tanpa mengunggah file bukti pembayaran. Pesan galatnya "proof file required" |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Payment Bill yang sudah Paid tidak bisa diedit, dihapus, atau dipecah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Hanya Payment Bill yang sudah Approved yang bisa disiapkan. Mark as Paid ditolak pada mode ini |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Orang lain yang berwenang melakukan Release untuk mengirim instruksi. Penyusun tidak bisa merilis transfernya sendiri, rilis memerlukan kode verifikasi (TOTP), dan pengiriman ulang aman karena idempoten |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Purchase Return — Modul Purchasing

Bab manual: [`purchasing/08-purchase-return.md`](../../erpApiServices/docs/manualBook/purchasing/08-purchase-return.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat retur obat Paracetamol 500 mg strip (draf) | Buka Purchase Returns; pilih GR OBT-001; isi qty 20; Save | Retur disimpan dengan status Draft, qty diterima 20, stok Persediaan berkurang |
| Negatif — Mencoba retur obat Paracetamol 500 mg strip melebihi qty diterima (draf) | Buka Purchase Returns; pilih GR OBT-001; isi qty 30; Save | Sistem menolak input, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Purchasing → Purchase Returns (/purchasing/purchase-returns) · Prasyarat: ada Goods Receipt yang sudah tercatat (barang harus sudah "diterima" dulu sebelum bisa "dikembalikan") |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Retur tidak bisa melebihi qty yang diterima (dikurangi retur sebelumnya untuk item yang sama) — sama seperti guard over-receipt di Goods Receipt (chapter 05), sistem menolak input yang melebihi batas ini |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Complete ditolak kalau stok di gudang tempat barang diterima lebih sedikit dari qty yang diretur (misalnya sebagian sudah terjual atau dipindahkan). Tidak ada baris yang berubah. Selesaikan dulu penyebabnya lalu coba lagi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Verifikasi Purchasing ke Accounting — Modul Purchasing

Bab manual: [`purchasing/09-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/purchasing/09-verifikasi-ke-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Verifikasi purchasing ke accounting berjalan dengan baik (draf) | Buka General Ledger; cek Detail Ledger akun Persediaan, Utang Dagang, PPN Masukan, Kas/Bank; cek Trial Balance; lihat AP Aging; semua dokumen sudah Approved dan Export to Journal; Total Debit = Total Kredit seimbang; saldo Utang Dagang supplier kembali ke 0 | Akun-akun tercatat dengan benar; Trial Balance seimbang; AP Aging tidak menunjukkan invoice yang sudah lunas; saldo Utang Dagang supplier menjadi 0 |
| Negatif — GR belum di-export ke jurnal (draf) | Buka Goods Receipt untuk PR-001; status Export to Journal belum dilakukan | Persediaan tidak bertambah; Trial Balance tidak seimbang; AP Aging masih menunjukkan invoice yang sudah lunas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Persediaan — harus bertambah sesuai total Goods Receipt yang sudah di-export |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Tagihan Biaya Logistik (Purchase Charge Invoice) — Modul Purchasing

Bab manual: [`purchasing/10-tagihan-biaya-logistik.md`](../../erpApiServices/docs/manualBook/purchasing/10-tagihan-biaya-logistik.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat tagihan biaya logistik (draf) | Buka `/purchasing/purchase-charge-invoices`, pilih PO, konfigurasi, jenis biaya, alokasi; Approve & Posting. | Biaya logistik ditambahkan ke harga pokok barang dan jurnal posting terbentuk. |
| Negatif — Membuat tagihan tanpa konfigurasi (draf) | Mencoba membuat tagihan tanpa mengaktifkan `Enable Logistics Charge Invoice` di `/purchasing/purchase-charge-configs`. | Tidak bisa membuat tagihan biaya logistik, pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tombol "Balik" membatalkan tagihan yang sudah posted — otomatis mengembalikan harga pokok barang ke nilai semula dan membalik jurnalnya. Tidak bisa reverse kalau masih ada pembayaran yang berstatus lunas; batalkan dulu pembayarannya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Blanket Agreement (Kontrak Payung) — Modul Purchasing

Bab manual: [`purchasing/11-blanket-agreement.md`](../../erpApiServices/docs/manualBook/purchasing/11-blanket-agreement.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat kontrak dengan supplier (draf) | Buka Purchasing → Blanket Agreements; klik "+ Perjanjian Induk Baru"; isikan PT Alkes Prima Mandiri sebagai Supplier, tanggal mulai 1 Januari 2023, dan selesai 31 Desember 2023; pilih Total Value dengan total komitmen Rp 50.000.000; tambahkan Paracetamol 500 mg strip (SKU OBT-001) dengan harga kontrak Rp 2.000 per unit dan batas maksimal 10.000 unit; klik Save | Kontrak berstatus Draft, bisa langsung mengulas detail |
| Negatif — Menarik PO tanpa kontrak aktif (draf) | Buka halaman Purchase Order; coba tarik PO dari kontrak yang statusnya Expired; isikan Kafe Sehat sebagai penerima | Sistem menolak dan memberi pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Supplier, Valid From, dan Valid Until (tanggal akhir wajib diisi dan harus setelah tanggal mulai) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Isi Contract Price — harga yang terkunci selama masa kontrak, wajib lebih dari 0 |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satu produk tidak boleh muncul dua kali dalam kontrak yang sama |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Edit hanya bisa dilakukan saat status Draft. Setelah diaktifkan, item dan syarat kontrak tidak bisa diubah lagi — kalau ada perubahan harga/item, buat kontrak baru |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Konfigurasi Biaya Tambahan Pembelian

Bab manual: [`purchasing/12-konfigurasi-biaya-tambahan-pembelian.md`](../../erpApiServices/docs/manualBook/purchasing/12-konfigurasi-biaya-tambahan-pembelian.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi biaya logistik (draf) | Masuk ke `/purchasing/purchase-charge-configs`; aktifkan fitur tagihan biaya logistik; pilih metode masukan biaya `Inline on purchase invoice` untuk cabang Apotek Nusantara Bandung; simpan. | Fitur tagihan biaya logistik aktif di cabang Apotek Nusantara Bandung dan terlihat pada form Purchase Invoice. |
| Negatif — Penolakan alokasi sebelum diterima (draf) | Masuk ke `/purchasing/purchase-charge-configs`; aktifkan `Izinkan Alokasi Sebelum Barang Diterima` untuk cabang Pabrik Herbal Sukabumi; coba alokasikan biaya tanpa penerimaan barang. | Muncul pesan penolakan yang jelas dan alokasi tidak dapat disimpan. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Jadwal Pembelian Berulang dari Kontrak Payung

Bab manual: [`purchasing/14-jadwal-pembelian-berulang.md`](../../erpApiServices/docs/manualBook/purchasing/14-jadwal-pembelian-berulang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Jadwal berulang untuk Paracetamol 500 mg strip (draf) | Buka Purchasing → Recurring Schedules; Pilih Blanket Agreement OBT-001, Aturan pengulangan harian, Tanggal mulai 1 Januari 2023, Baris barang Paracetamol 500 mg strip; Simpan; Jalankan sekarang | PO untuk Paracetamol 500 mg strip terbit, stok diperbarui, riwayat eksekusi ditambahkan |
| Negatif — Hapus jadwal yang sudah membuat pesanan (draf) | Coba hapus jadwal OBT-001; Dapat pesan "Jadwal yang sudah membuat pesanan tidak bisa dihapus" | Tidak ada perubahan, jadwal tetap berada dalam daftar dan masih aktif |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jadwal yang sudah selesai tidak bisa diubah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jadwal yang sudah membuat pesanan tidak bisa dihapus. Gunakan Jeda sebagai gantinya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pesanan tetap tunduk pada aturan lain di Purchasing (persetujuan PO bila diwajibkan) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penjadwal server harus berjalan agar jadwal berjalan otomatis; bila tidak, pesanan tidak terbit sendiri |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 14. Diagram Alur Purchasing — Modul Purchasing

Bab manual: [`purchasing/15-diagram-alur-purchasing.md`](../../erpApiServices/docs/manualBook/purchasing/15-diagram-alur-purchasing.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Purchase Order (draf) | Masuk ke menu Purchase Request; pilih produk Paracetamol 500 mg strip (SKU OBT-001); isi jumlah 100 box; klik tombol "Create PO"; masuk ke menu Purchase Order; lihat PO baru dengan status Draft | Purchase Order dengan nomor dan tanggal muncul di menu Purchase Order, status menjadi Draft |
| Negatif — Membuat Purchase Order tanpa Goods Receipt First aktif (draf) | Masuk ke menu Purchase Request; pilih produk Paracetamol 500 mg strip (SKU OBT-001); isi jumlah 100 box; klik tombol "Create PO"; masuk ke menu Purchase Order; lihat pesan error "PO Flow Mode tidak memungkinkan pembuatan PO tanpa GR" | Tampilan error muncul dan PO tidak dibuat, status tetap Draft di menu Purchase Request |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Begitu Purchase Order punya satu Goods Receipt atau satu Purchase Invoice, item PO terkunci dan tidak bisa diubah lagi (bab 04) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Cancel hanya bisa dari status Draft |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 15. Dampak Stok dari Pembelian — Modul Purchasing

Bab manual: [`purchasing/16-dampak-stok-dari-pembelian.md`](../../erpApiServices/docs/manualBook/purchasing/16-dampak-stok-dari-pembelian.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Stok Masuk Saat Approved (draf) | Save Goods Receipt OBT-001; Approve dengan gudang Medika Nusantara; Submit Purchase Order OBT-001 dengan harga 5000 | Stok OBT-001 masuk ke gudang Medika Nusantara dengan jumlah dan harga sesuai PO |
| Negatif — Retur Ditolak Karena Kurang Stok (draf) | Buat Purchase Return OBT-001; Approve; Coba Complete dengan qty melebihi stok di gudang | Sistem menolak retur pesan penolakan yang jelas dan stok tetap tidak berubah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Kalau baris Goods Receipt mencatat qty yang ditolak (rejected), bagian itu tidak ikut masuk stok. Yang dihitung hanya qty yang diterima |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
