---
title: (PT Sehat Sentosa Farma) — 05. Pembelian
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul purchasing untuk skenario PT Sehat Sentosa Farma. Dari permintaan sampai pembayaran pemasok.
visibility: internal
---

# 05. Pembelian

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** Konfigurasi oleh **Dr. Rahmat**. Transaksi oleh **Bima Prakoso** (Staf Pembelian); penerimaan barang oleh **Hendra Saputra** (Kepala Gudang); persetujuan PO oleh **Sari Wulandari** dan **Dr. Rahmat**; pembayaran oleh **Sari Wulandari**.

**Cabang aktif:** Kantor Pusat & Distribusi Jakarta.

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- PR lalu PQ lalu PO lalu GR lalu PI lalu pembayaran; urutan GR dan faktur mengikuti konfigurasi.
- Penerimaan tidak boleh melebihi sisa PO; pembayaran tidak boleh melebihi faktur; faktur belum disetujui tidak bisa dibayar.
- PO dengan pengiriman bertahap dan pemberitahuan pengiriman pemasok (halaman publik).
- Faktur biaya logistik: alokasi landed cost, pembebanan ulang ke pelanggan, selisih kurs bila akunnya diatur.
- Pencocokan faktur dengan barang diterima (mati, peringatkan, tolak) dan produk yang tidak dapat dibeli tidak muncul di pemilih.

## 1. Konfigurasi Alur Purchasing — Modul Purchasing

Bab manual: [`purchasing/01-konfigurasi-alur-purchasing.md`](../../erpApiServices/docs/manualBook/purchasing/01-konfigurasi-alur-purchasing.md)

**Input di:** `Purchasing → Purchase Configs` (`/purchasing/purchase-configs`).

**Perhatikan:** **Kerjakan ini SEBELUM mulai transaksi PR/PQ/PO** — pengaturan di sini menentukan urutan dokumen apa yang boleh dibuat kapan.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi Alur Purchasing (draf) | Konfigurasi alur persetujuan, urutan GR vs Invoice, dan pemetaan akun jurnal otomatis untuk Sentosa Farma; uji dengan data pemasok dan pelanggan valid | Proses purchasing berjalan lancar, otomatisasi akuntansi terintegrasi dengan benar |
| Negatif — Konfigurasi Alur Purchasing (draf) | Input alur GR sebelum Invoice, tanpa konfigurasi persetujuan; uji dengan data pemasok dan pelanggan valid | Sistem menolak proses purchasing, pesan penolakan yang jelas dengan detail pesan kesalahan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Urutan GR vs PI — barang harus diterima dulu baru bisa ditagih, atau tagihan boleh datang duluan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Ini pengaturan paling penting untuk dipahami — menentukan urutan wajib antara menerima barang (GR) dan menagih (PI) setelah PO dibuat: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penting: begitu satu PO sudah punya minimal 1 Goods Receipt atau 1 Purchase Invoice, PO tersebut terkunci — item-nya tidak bisa diubah lagi. Pastikan PO sudah benar sebelum lanjut ke GR/PI |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Manual — staff harus klik "Export to Journal" sendiri di halaman detail dokumen |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Purchase Request — Modul Purchasing

Bab manual: [`purchasing/02-purchase-request.md`](../../erpApiServices/docs/manualBook/purchasing/02-purchase-request.md)

**Input di:** `Purchasing → Purchase Requests` (`/purchasing/purchase-requests`).

**Prasyarat:** _01. Konfigurasi Alur Purchasing_ sudah di-setup.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | membuat PR untuk Paracetamol 500 mg strip (SKU OBT-001) di gudang pusat; disetujui oleh kepala gudang; masuk ke antrian pembelian | Purchase Request diterbitkan dan masuk dalam proses pengadaan dengan status 'menunggu penerimaan' |
| Negatif — input salah (draf) | membuat PR tanpa menentukan SKU; ditolak oleh sistem pesan penolakan yang jelas | Input tidak valid, Purchase Request ditolak dan perlu dimasukkan kembali dengan SKU yang lengkap |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | PR yang sudah Submit tidak bisa diedit lagi — kalau ada revisi, PR harus dibatalkan (Cancel) dan dibuat ulang, atau ditolak (Reject, kalau lewat approval) lalu dibuatkan versi baru |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Purchase Quotation — Modul Purchasing

Bab manual: [`purchasing/03-purchase-quotation.md`](../../erpApiServices/docs/manualBook/purchasing/03-purchase-quotation.md)

**Input di:** `Purchasing → Purchase Quotations` (`/purchasing/purchase-quotations`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Purchase Quotation (draf) | Membuat PQ untuk Paracetamol 500 mg strip (SKU OBT-001) dari PT Bintang Farmasi Utama; mengisi harga tier; membandingkan dengan PT Alkes Prima Mandiri; submit, approve, dan convert menjadi PO. | Berhasil membuat PQ, bandingkan penawaran, dan konversi menjadi PO untuk Paracetamol 500 mg strip. |
| Negatif — Purchase Quotation (draf) | Membuat PQ untuk Paracetamol 500 mg strip (SKU OBT-001) tanpa mengisi harga tier; submit. | Ditolak karena harga penawaran belum diisi; muncul pesan kesalahan yang jelas. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Purchase Order — Modul Purchasing

Bab manual: [`purchasing/04-purchase-order.md`](../../erpApiServices/docs/manualBook/purchasing/04-purchase-order.md)

**Input di:** `Purchasing → Purchase Orders` (`/purchasing/purchase-orders`).

**Prasyarat:** Purchase Quotation sudah Approved (kecuali konfigurasi **Require PQ Before PO** dimatikan).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Purchase Order (draf) | PT Sehat Sentosa Farma membuat PO untuk Paracetamol 500 mg strip (SKU OBT-001) dari PT Bintang Farmasi Utama; Approve oleh Kepala Gudang; Terkunci setelah GR/PI masuk. | Purchase Order disetujui dan terkunci dengan benar, proses lanjut ke Goods Receipt. |
| Negatif — Input Tanggal Expired (draf) | PT Sehat Sentosa Farma mencoba membuat PO dengan tanggal expired di masa lalu; ditolak oleh sistem karena syarat tidak terpenuhi. | Sistem menolak input dan memberikan pesan kesalahan yang jelas tentang tanggal tidak valid. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tautan portal tidak bisa dibuat/regenerate lagi kalau seluruh item PO sudah selesai dikirim (fully shipped) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Goods Receipt — Modul Purchasing

Bab manual: [`purchasing/05-goods-receipt.md`](../../erpApiServices/docs/manualBook/purchasing/05-goods-receipt.md)

**Input di:** `Purchasing → Purchase Receipts` (`/purchasing/purchase-receipts`).

**Prasyarat:** PO sudah Approved, dan urutan sesuai **PO Flow Mode** (lihat _01. Konfigurasi Alur Purchasing_).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Penerimaan Barang (draf) | Input PO: OBT-001; Qty: 100; Tambah biaya: ongkir Rp50.000; Approve & posting | Persediaan OBT-001 bertambah, jurnal terposting dengan total biaya Rp550.000 |
| Negatif — Menerima Melebihi Qty PO (draf) | Input PO: OBT-001; Qty: 100; Tambah biaya: ongkir Rp50.000; input qty penerimaan 120; Approve & posting | Sistem menolak, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sistem menolak kalau qty yang diinput di GR melebihi sisa qty yang belum diterima untuk item tersebut — muncul pesan error jelas di form sebelum sempat disimpan. Ini mencegah pencatatan penerimaan barang lebih banyak dari yang sebenarnya dipesan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | GR yang sudah di-export tidak bisa di-export ulang — sistem menolak untuk mencegah jurnal tercatat dobel |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Purchase Invoice — Modul Purchasing

Bab manual: [`purchasing/06-purchase-invoice.md`](../../erpApiServices/docs/manualBook/purchasing/06-purchase-invoice.md)

**Input di:** `Purchasing → Purchase Invoices` (`/purchasing/purchase-invoices`).

**Prasyarat:** PO Approved, dan urutan sesuai **PO Flow Mode** (lihat _01. Konfigurasi Alur Purchasing_).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Tagihan Supplier (draf) | Input PO OBT-001, jumlah 100, harga Rp 500,000; klik Approve & Posting | Berhasil memposting invoice ke jurnal utang dagang dengan PPN Masukan |
| Negatif — Invoice Bertahap (draf) | Input PO OBT-001, tetapi pilih Partial Invoicing tanpa jumlah; coba Approve | Ditolak karena harus menentukan jumlah invoice terlebih dahulu untuk bertahap |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Purchase Payment Bill — Modul Purchasing

Bab manual: [`purchasing/07-purchase-payment-bill.md`](../../erpApiServices/docs/manualBook/purchasing/07-purchase-payment-bill.md)

**Input di:** `Purchasing → Purchase Payment Bills` (`/purchasing/purchase-payment-bills`).

**Prasyarat:** Purchase Invoice sudah **Approved**.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membayar Invoice (draf) | Input invoice OBT-001, pilih metode lunas, konfirmasi, approve manajer keuangan, posting jurnal otomatis | Invoice OBT-001 terbayar dan terposting pada jurnal bayar supplier |
| Negatif — Bayar Invoice Belum Approved (draf) | Coba bayar invoice OBT-001 tanpa approval, muncul notifikasi pesan yang jelas | Tidak dapat memproses pembayaran karena invoice belum diterbitkan oleh manajer keuangan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Purchase Return — Modul Purchasing

Bab manual: [`purchasing/08-purchase-return.md`](../../erpApiServices/docs/manualBook/purchasing/08-purchase-return.md)

**Input di:** `Purchasing → Purchase Returns` (`/purchasing/purchase-returns`).

**Prasyarat:** ada Goods Receipt yang sudah tercatat (barang harus sudah "diterima" dulu sebelum bisa "dikembalikan").

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Retur Pembelian (draf) | Input nomor PO: OBT-001, jumlah retur 50 unit, alasan: salah kemasan | Jurnal terbentuk, Utang Dagang supplier dikreditkan 750.000 Rupiah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Purchasing → Purchase Returns (/purchasing/purchase-returns) · Prasyarat: ada Goods Receipt yang sudah tercatat (barang harus sudah "diterima" dulu sebelum bisa "dikembalikan") |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Retur tidak bisa melebihi qty yang diterima (dikurangi retur sebelumnya untuk item yang sama) — sama seperti guard over-receipt di Goods Receipt (chapter 05), sistem menolak input yang melebihi batas ini |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Verifikasi Purchasing ke Accounting — Modul Purchasing

Bab manual: [`purchasing/09-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/purchasing/09-verifikasi-ke-accounting.md)

**Input di:** tidak ada halaman input; periksa di `Accounting → General Ledger` (`/accounting/general-ledger`), `Reports → Trial Balance` (`/reports/trial-balance`), dan `Reports → Accounts Payable Aging` (`/reports/ap-aging`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Verifikasi PR-PQ-PO-GR-PI-Payment (draf) | Cek GL akun AP, TB, dan AP Aging; semua transaksi tercatat dengan benar; laporan sehat | Seluruh alur purchasing terintegrasi dengan akuntansi, data akurat |
| Negatif — Salah satu transaksi tidak tercatat (draf) | PR-PQ-PO-GR-PI-Payment tidak lengkap di salah satu laporan; pesan error di AP Aging | Terdeteksi ketidaksesuaian dan perbaikan diperlukan segera |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Persediaan — harus bertambah sesuai total Goods Receipt yang sudah di-export |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Tagihan Biaya Logistik (Purchase Charge Invoice) — Modul Purchasing

Bab manual: [`purchasing/10-tagihan-biaya-logistik.md`](../../erpApiServices/docs/manualBook/purchasing/10-tagihan-biaya-logistik.md)

**Input di:** `Purchasing → Purchase Charge Invoices` (`/purchasing/purchase-charge-invoices`).

**Prasyarat:** konfigurasi di `Purchasing → Purchase Charge Configs` sudah diisi, dan ada Purchase Order/Goods Receipt sebagai target alokasi.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Biaya Logistik (draf) | Input data ongkos kirim ke konfigurasi, buat tagihan biaya logistik untuk OBT-001, approve & posting, rebill ke Apotek Mitra Sehat | Biaya logistik tercatat dan teralokasikan ke harga pokok, tagihan dikirim ke pelanggan dengan detail benar |
| Negatif — Input Data Salah (draf) | Memasukkan SKU yang salah dalam tagihan biaya logistik, mencoba approve & posting | Sistem menolak inputan dan memberi pesan kesalahan mengenai SKU tidak valid |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tombol "Reverse" membatalkan tagihan yang sudah posted — otomatis mengembalikan harga pokok barang ke nilai semula dan membalik jurnalnya. Tidak bisa reverse kalau masih ada pembayaran yang berstatus lunas; batalkan dulu pembayarannya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Blanket Agreement (Kontrak Payung) — Modul Purchasing

Bab manual: [`purchasing/11-blanket-agreement.md`](../../erpApiServices/docs/manualBook/purchasing/11-blanket-agreement.md)

**Input di:** `Purchasing → Blanket Agreements` (`/purchasing/blanket-agreements`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Blanket Agreement (draf) | PT Bintang Farmasi Utama; kontrak untuk Paracetamol 500 mg strip; periode 6 bulan; jumlah maksimal 1000 box | Kontrak berhasil dibuat dengan detail dan status "Draft" |
| Negatif — Input Pemasok Salah (draf) | CV Kapur Medika; produk Jamu Kunyit Asam sachet; kontrak untuk 5000 sachet | Ditolak: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Supplier, Valid From, dan Valid Until (tanggal akhir wajib diisi dan harus setelah tanggal mulai) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Isi Contract Price — harga yang terkunci selama masa kontrak, wajib lebih dari 0 |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satu produk tidak boleh muncul dua kali dalam kontrak yang sama |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Edit hanya bisa dilakukan saat status Draft. Setelah diaktifkan, item dan syarat kontrak tidak bisa diubah lagi — kalau ada perubahan harga/item, buat kontrak baru |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Konfigurasi Biaya Tambahan Pembelian

Bab manual: [`purchasing/12-konfigurasi-biaya-tambahan-pembelian.md`](../../erpApiServices/docs/manualBook/purchasing/12-konfigurasi-biaya-tambahan-pembelian.md)

**Input di:** `Purchasing → Logistics Charge Configuration` (`/purchasing/purchase-charge-configs`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menambah konfigurasi tagihan logistik untuk produk Paracetamol 500 mg strip (SKU OBT-001) dengan mengaktifkan biaya pengiriman dan mengalokasikannya ke barang, memilih perlakuan akuntansi sebagai beban, menentukan pihak yang menanggung sebagai penjual, dan menyimpan konfigurasi | Konfigurasi tagihan logistik berhasil ditambahkan dengan detail sesuai input |
| Negatif — input salah (draf) | Mengaktifkan biaya pengiriman tanpa mengalokasikannya ke barang pada produk Paracetamol 500 mg strip (SKU OBT-001) | Sistem menolak konfigurasi karena harus mengalokasikan biaya ke barang terlebih dahulu, menyertakan pesan kesalahan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
