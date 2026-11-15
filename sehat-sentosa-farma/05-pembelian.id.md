---
title: (PT Sehat Sentosa Farma) — 05. Pembelian
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul purchasing untuk skenario PT Sehat Sentosa Farma. Dari permintaan sampai pembayaran pemasok.
visibility: internal
---

# 05. Pembelian

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
| Positif — Konfigurasi Alur Purchasing (draf) | Atur alur persetujuan, urutan GR vs Invoice OBT-001, dan map akun jurnal otomatis; cek posting jurnal; pilih Bintang Farmasi Utama; konfirmasi PO; terima barang & invoice sesuai; bayar ke pemasok | Alur persetujuan berjalan lancar, GR vs Invoice OBT-001 sesuai, jurnal otomatis benar, pembayaran dilakukan dengan tepat |
| Negatif — Konfigurasi Alur Purchasing (draf) | Input alur GR sebelum setting persetujuan; coba posting jurnal tanpa setting GR vs Invoice; pilih pemasok baru tanpa kontrak; terima invoice tanpa PO; bayar ke pemasok tanpa PO | Sistem menolak input, memberikan pesan kesalahan tentang alur GR, syarat persetujuan belum lengkap, tidak bisa memproses invoice tanpa PO, pembayaran ditolak karena PO belum ada |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Urutan GR vs PI — barang harus diterima dulu baru bisa ditagih, atau tagihan boleh datang duluan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Ini pengaturan paling penting untuk dipahami — menentukan urutan wajib antara menerima barang (GR) dan menagih (PI) setelah PO dibuat: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penting: begitu satu PO sudah punya minimal 1 Goods Receipt atau 1 Purchase Invoice, PO tersebut terkunci — item-nya tidak bisa diubah lagi. Pastikan PO sudah benar sebelum lanjut ke GR/PI |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Manual — staff harus klik "Export to Journal" sendiri di halaman detail dokumen |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Purchase Request — Modul Purchasing

Bab manual: [`purchasing/02-purchase-request.md`](../../erpApiServices/docs/manualBook/purchasing/02-purchase-request.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Karyawan membuat PR OBT-001 di modul purchasing, memasukkan detail produk, jumlah, dan pemasok Bintang Farmasi Utama; karyawan menyetujui | Purchase Request OBT-001 disetujui dan masuk antrian pengadaan |
| Negatif — input salah (draf) | Karyawan membuat PR tanpa memilih pemasok; sistem menolak pesan penolakan yang jelas | Purchase Request ditolak, karyawan diminta memilih pemasok terlebih dahulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | PR yang sudah Submit tidak bisa diedit lagi — kalau ada revisi, PR harus dibatalkan (Cancel) dan dibuat ulang, atau ditolak (Reject, kalau lewat approval) lalu dibuatkan versi baru |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Purchase Quotation — Modul Purchasing

Bab manual: [`purchasing/03-purchase-quotation.md`](../../erpApiServices/docs/manualBook/purchasing/03-purchase-quotation.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Purchase Quotation (draf) | Membuat PQ untuk Paracetamol 500 mg strip (SKU OBT-001) dari PT Bintang Farmasi Utama; memasukkan harga tier; mengirim RFQ, memilih pemenang, submit dan approve | Berhasil membuat PO untuk Paracetamol 500 mg strip dengan supplier terpilih |
| Negatif — Purchase Quotation (draf) | Membuat PQ untuk Paracetamol 500 mg strip (SKU OBT-001) dari PT Bintang Farmasi Utama; memasukkan harga tier, mengirim RFQ tapi salah alamat penerima; tidak memilih pemenang sebelum submit | Ditolak karena alamat penerima tidak valid dan belum memilih pemenang |
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
| Positif — Membuat PO (draf) | Buat PO untuk Paracetamol 500 mg strip (SKU OBT-001) dari Bintang Farmasi Utama; isi detail sesuai penawaran; submit & approve; lanjut ke GR/PI | Purchase Order dibuat, disetujui, dan berlanjut ke Goods Receipt/Purchase Invoice dengan benar |
| Negatif — Input Supplier Salah (draf) | Masukkan nama supplier yang tidak ada (PT XYZ) pada PO Paracetamol 500 mg strip; submit & approve | PO ditolak karena supplier tidak valid; pesan penolakan yang jelas dengan detail entitas uji |
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
| Positif — Mencatat Penerimaan Barang (draf) | Input PO: OBT-001; Qty: 100; Tambah Landed Cost: Rp500; Approve & Post | Persediaan OBT-001 bertambah 100, jurnal terposting |
| Negatif — Menerima Melebihi Qty PO (draf) | Input PO: OBT-001; Qty: 200; Approve | Tidak bisa approve, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tiap baris punya isian Rejected Quantity untuk barang yang diterima tetapi ditolak. Nilainya tidak boleh melebihi qty diterima. Bagian yang ditolak tidak ikut masuk stok (lihat bab 16. Dampak Stok dari Pembelian) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sistem menolak kalau qty yang diinput di GR melebihi sisa qty yang belum diterima untuk item tersebut — muncul pesan error jelas di form sebelum sempat disimpan. Ini mencegah pencatatan penerimaan barang lebih banyak dari yang sebenarnya dipesan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | GR yang sudah di-export tidak bisa di-export ulang — sistem menolak untuk mencegah jurnal tercatat dobel |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Purchase Invoice — Modul Purchasing

Bab manual: [`purchasing/06-purchase-invoice.md`](../../erpApiServices/docs/manualBook/purchasing/06-purchase-invoice.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Tagihan Supplier (draf) | Input PO: OBT-001; PPN 10%; Jumlah: 500 unit; Harga: Rp2.000/unit; Total: Rp1.000.000; Approve & Post | Berhasil mencatat tagihan dan memposting ke jurnal utang dagang dengan benar |
| Negatif — Input PO Tidak Sesuai (draf) | PO: OBT-003; Jumlah: 600 unit (tidak sesuai); PPN 10% | Ditolak, pesan penolakan yang jelas dan tidak dapat diapprove & diposting |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Purchase Payment Bill — Modul Purchasing

Bab manual: [`purchasing/07-purchase-payment-bill.md`](../../erpApiServices/docs/manualBook/purchasing/07-purchase-payment-bill.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membayar Invoice (draf) | Input invoice OBT-001, pilih metode lunas, masukkan jumlah dan tanggal bayar; approve oleh manajer keuangan | Invoice OBT-001 terbayar secara langsung dan postingan jurnal muncul |
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
| Positif — Mencatat Retur (draf) | Input: Purchase Order OBT-001, Quantity 50, Price Rp2.000, Date 2023-09-15; Approve & Complete; Posting Jurnal | Berhasil mencatat retur pembelian dan memperbarui Utang Dagang supplier |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Purchasing → Purchase Returns (/purchasing/purchase-returns) · Prasyarat: ada Goods Receipt yang sudah tercatat (barang harus sudah "diterima" dulu sebelum bisa "dikembalikan") |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Retur tidak bisa melebihi qty yang diterima (dikurangi retur sebelumnya untuk item yang sama) — sama seperti guard over-receipt di Goods Receipt (chapter 05), sistem menolak input yang melebihi batas ini |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Complete ditolak kalau stok di gudang tempat barang diterima lebih sedikit dari qty yang diretur (misalnya sebagian sudah terjual atau dipindahkan). Tidak ada baris yang berubah. Selesaikan dulu penyebabnya lalu coba lagi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Verifikasi Purchasing ke Accounting — Modul Purchasing

Bab manual: [`purchasing/09-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/purchasing/09-verifikasi-ke-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Verifikasi PR-PQ-PO-GR-PI-Payment untuk Paracetamol 500 mg strip (SKU OBT-001) | Seluruh transaksi tercatat dengan benar di General Ledger, Trial Balance, dan AP Aging |
| Negatif — input salah (draf) | Input PO tanpa QRIS untuk Amoxicillin 500 mg (OBT-002) | Verifikasi ditolak: PO harus disertai QRIS untuk resep obat |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Persediaan — harus bertambah sesuai total Goods Receipt yang sudah di-export |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Tagihan Biaya Logistik (Purchase Charge Invoice) — Modul Purchasing

Bab manual: [`purchasing/10-tagihan-biaya-logistik.md`](../../erpApiServices/docs/manualBook/purchasing/10-tagihan-biaya-logistik.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Biaya Logistik (draf) | Input: Purchase Charge Configs dengan jenis biaya Ongkos Kirim; Buat Purchase Charge Invoice; Approve & Posting; Rebill ke Apotek Mitra Sehat; Bayar melalui transfer bank; Terima PDF dan notifikasi WhatsApp | Biaya logistik tercatat, dikalkulasikan ke HPP, dibebankan kepada customer dengan benar |
| Negatif — Input Jenis Biaya Salah (draf) | Input: Purchase Charge Configs dengan jenis biaya Bea Masuk; Tapi input sebagai Ongkos Kirim; Approve & Posting | Sistem menolak dan menginformasikan bahwa jenis biaya tidak sesuai dengan konfigurasi yang ada |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tombol "Reverse" membatalkan tagihan yang sudah posted — otomatis mengembalikan harga pokok barang ke nilai semula dan membalik jurnalnya. Tidak bisa reverse kalau masih ada pembayaran yang berstatus lunas; batalkan dulu pembayarannya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Blanket Agreement (Kontrak Payung) — Modul Purchasing

Bab manual: [`purchasing/11-blanket-agreement.md`](../../erpApiServices/docs/manualBook/purchasing/11-blanket-agreement.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Blanket Agreement (draf) | PT Sehat Sentosa Farma membuat kontrak dengan PT Bintang Farmasi Utama untuk obat Paracetamol 500 mg strip selama 6 bulan | Kontrak berhasil dibuat dengan detail dan nilai yang sesuai |
| Negatif — Input Data Salah (draf) | Input kode produk OBT-001 salah saat membuat PO dari kontrak | Sistem menolak input dan memberikan pesan kesalahan kode produk tidak valid |
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
| Positif — jalur normal (draf) | Aktifkan tagihan logistik untuk cabang Bandung, alokasikan ke harga pokok, atur akuntansi sebagai biaya operasional, tentukan klinik sebagai penanggung, aktifkan notifikasi sukses | Tagihan logistik diterapkan dengan benar dan notifikasi sukses muncul |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Jadwal Pembelian Berulang dari Kontrak Payung

Bab manual: [`purchasing/14-jadwal-pembelian-berulang.md`](../../erpApiServices/docs/manualBook/purchasing/14-jadwal-pembelian-berulang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Jadwal Pembelian Berulang (draf) | Buat jadwal baru dari kontrak Payung Bintang Farmasi; atur ulang 1 minggu; jalankan sekarang; input valid | Jadwal terdaftar dengan detail pesanan dan tindakan sesuai aturan |
| Negatif — Kontrak Tidak Aktif (draf) | Masukkan kontrak non-aktif sebagai payung; coba eksekusi jadwal | Tolakan: pesan yang jelas |
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
| Positif — jalur normal (draf) | Apoteker membuat Purchase Request, disetujui Kepala Gudang, PO dibuat dan disetujui Manajer Keuangan, Goods Receipt dan Invoice diterima, status PO menjadi Paid | Proses pengadaan berjalan lancar, status PO valid dan pembayaran dilakukan dengan benar |
| Negatif — input salah (draf) | Apoteker membuat Purchase Request tanpa nomor urut, ditolak Kepala Gudang karena syarat tidak terpenuhi, harus dimasukkan nomor urut yang valid | Purchase Request ditolak pesan penolakan yang jelas dan diberikan petunjuk untuk memperbaiki |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Begitu Purchase Order punya satu Goods Receipt atau satu Purchase Invoice, item PO terkunci dan tidak bisa diubah lagi (bab 04) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Cancel hanya bisa dari status Draft |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 15. Dampak Stok dari Pembelian — Modul Purchasing

Bab manual: [`purchasing/16-dampak-stok-dari-pembelian.md`](../../erpApiServices/docs/manualBook/purchasing/16-dampak-stok-dari-pembelian.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Stok Gudang Tambah (draf) | Goods Receipt OBT-001 Approved; Stok Paracetamol 500 mg strip ditambah | Stok gudang bertambah sesuai jumlah terima |
| Negatif — Retur Ditolak (draf) | Purchase Return OBT-001 Complete; Alkohol Swab tidak sesuai; Sistem menolak retur pesan penolakan yang jelas | Retur ditolak, stok gudang tidak berkurang dan sistem memberikan pesan kesalahan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Kalau baris Goods Receipt mencatat qty yang ditolak (rejected), bagian itu tidak ikut masuk stok. Yang dihitung hanya qty yang diterima |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
