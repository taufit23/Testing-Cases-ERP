---
title: (PT Medika Nusantara Sejahtera) — 06. Persediaan
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul inventory untuk skenario PT Medika Nusantara Sejahtera. Stok, transfer, opname dan nilai persediaan.
visibility: internal
---

# 06. Persediaan

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji stok: masuk, keluar, pindah gudang, hitung fisik, dan penilaian nilai persediaan.
>
> **Kalau semuanya benar, artinya:** Jumlah dan nilai stok di layar sama dengan kenyataan, dan setiap perubahan stok punya jejak.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Transfer stok bertahap (pengiriman ganda) dan penerimaan di gudang tujuan; nilai gabungan tidak berubah.
- Stok opname menghasilkan penyesuaian yang disetujui dan terjurnal.
- Metode costing rata-rata/FIFO terbuka untuk semua; LIFO, identifikasi khusus dan biaya standar hanya bila paket memuat fitur lanjutan.
- Rekonsiliasi Persediaan: nilai stok dari lapisan biaya = saldo akun persediaan di buku besar.
- Stok minimum per gudang dan riwayat pergerakan stok.

## 1. Konfigurasi Inventory — Modul Inventory

Bab manual: [`inventory/01-konfigurasi-inventory.md`](../../erpApiServices/docs/manualBook/inventory/01-konfigurasi-inventory.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pemilihan Metode Penilaian Persediaan (draf) | Masuk ke `/inventory/config`; pilih metode `Average` untuk warehouse pusat; simpan | Metode penilaian persediaan berubah menjadi Average pada warehouse pusat, refleksi biaya di jurnal akuntansi sesuai |
| Negatif — Pengaktifan Auto-Replenishment Tanpa Konfigurasi Sumber Pasokan (draf) | Masuk ke `/inventory/config`; aktifkan `Auto Draft Purchase Request on Reorder` tanpa konfigurasi sumber pasokan; coba buat draft PR dari buffer stock | Muncul pesan error tentang kebutuhan konfigurasi sumber pasokan sebelum bisa membuat draft otomatis PR |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Supaya auto-draft Stock Transfer tahu harus ambil dari warehouse mana, tiap warehouse Store wajib punya minimal satu baris di Warehouse Supply Sources (lihat section di bawah) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Pilih Supply Warehouse (warehouse sumber — tidak boleh sama dengan Store Warehouse) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Store Warehouse dan Supply Warehouse tidak bisa diedit setelah dibuat — kalau salah pasangan, hapus baris dan buat ulang lewat "+ Add". Priority dan status masih bisa diubah lewat Edit |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Stock Adjustment — Modul Inventory

Bab manual: [`inventory/02-stock-adjustment.md`](../../erpApiServices/docs/manualBook/inventory/02-stock-adjustment.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menyesuaikan stok awal produk Paracetamol 500 mg strip (draf) | Buka Stock Adjustments; klik "+ Create"; pilih Warehouse Jakarta; pilih Reason "Stok awal pengadaan mandiri sebelum PO pertama"; tambah item dengan Product SKU OBT-001, Qty 2000, Unit Cost 4000; klik Save | Stok Paracetamol 500 mg strip di Warehouse Jakarta berubah menjadi 2000 unit dengan nilai total 8.000.000; adjustment terposting dan tidak bisa diedit lagi |
| Negatif — Menggunakan Reason yang belum dibuat untuk stok awal (draf) | Buka Stock Adjustments; klik "+ Create"; pilih Warehouse Jakarta; coba pilih Reason "Stok awal baru" tanpa membuatnya dulu; klik Save | Tidak bisa memilih Reason "Stok awal baru", pesan penolakan yang jelas; tidak ada perubahan pada stok atau adjustment |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap Stock Adjustment wajib memilih alasan dari daftar yang sudah disiapkan (bukan teks bebas) — supaya riwayat penyesuaian tetap terkategori dan bisa dianalisis |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Stock Adjustment yang sudah Posted tidak bisa diedit langsung — kalau ada kesalahan, buat adjustment koreksi baru (bukan mengubah yang lama), demi menjaga jejak audit |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Stock Transfer — Modul Inventory

Bab manual: [`inventory/03-stock-transfer.md`](../../erpApiServices/docs/manualBook/inventory/03-stock-transfer.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Transfer stok antar gudang berhasil (draf) | Sebagai Kasir Medika Nusantara, buka menu `Inventory → Stock Transfers`; pilih warehouse Jakarta sebagai From Warehouse & Bandung sebagai To Warehouse; tambah item Paracetamol 500 mg strip (SKU OBT-001) dengan Qty Requested 20; klik Save; setelah Submit, jika Require Transfer Approval aktif, lakukan approval; buat shipment pertama dengan Shipped Date 10/10/2023 & Quantity to Ship 15; create shipment kedua dengan Quantity to Ship 5; di Bandung, terima shipment pertama & kedua masing-masing 15 & 5 unit | Stok OBT-001 Jakarta berkurang 20 unit; stok OBT-001 Bandung bertambah 20 unit; jurnal dibukukan untuk pengiriman & penerimaan; status transfer menjadi Received |
| Negatif — Transfer ditolak karena qty terlalu besar (draf) | Sebagai Kasir Medika Nusantara, buka menu `Inventory → Stock Transfers`; pilih warehouse Jakarta sebagai From Warehouse & Bandung sebagai To Warehouse; tambah item Paracetamol 500 mg strip (SKU OBT-001) dengan Qty Requested 200; klik Save; setelah Submit, jika Require Transfer Approval aktif, lakukan approval; buat shipment pertama dengan Shipped Date 10/10/2023 & Quantity to Ship 150 | Sistem menolak transfer karena `Quantity to Ship` melebihi sisa (`Qty Requested` − `Qty Sent`) & menampilkan pesan "Qty yang diminta tidak bisa dikirim |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Pilih From Warehouse dan To Warehouse — keduanya tidak boleh sama, dan pilihan yang sudah dipakai di satu sisi otomatis tersembunyi dari sisi lainnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Tambahkan baris item — pilih Product SKU (stok yang tersedia di warehouse asal ditampilkan di sampingnya; SKU dengan stok 0 di warehouse asal tidak bisa dipilih), isi Qty Requested |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Qty yang diminta di suatu item tidak bisa dikirim melebihi sisa (Qty Requested − Qty Sent) — sistem menolak kalau shipment baru diminta memindahkan lebih dari sisa yang belum terkirim |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Stock Take (Opname) — Modul Inventory

Bab manual: [`inventory/04-stock-take.md`](../../erpApiServices/docs/manualBook/inventory/04-stock-take.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Pilih gudang Jakarta; scan barcode Paracetamol 500 mg strip (SKU OBT-001); hitung fisik 20 unit; complete opname | Stok OBT-001 di warehouse Jakarta disesuaikan menjadi 20 unit, jurnal selisih persediaan dibuat otomatis |
| Negatif — input salah (draf) | Scan barcode produk yang belum terdaftar; klik "Link and Count" dengan salah pilih produk | Muncul pesan penolakan yang jelas, opname tetap berlanjut tanpa perubahan stok |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setelah semua item terhitung, klik "Complete" — konfirmasi di modal peringatan. Stock Take hanya bisa di-Complete dari status Draft atau In Progress |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Stock Lots & Serials — Modul Inventory

Bab manual: [`inventory/05-stock-lots-dan-serials.md`](../../erpApiServices/docs/manualBook/inventory/05-stock-lots-dan-serials.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat lot manual (draf) | Pilih "Create Lot"; Warehouse: Gudang Jakarta; Product SKU: Paracetamol 500 mg strip (OBT-001); Lot Number: LOT-2023-001; QTY Received: 100; Unit Cost: 15000; Ownership Status: Owned | Lot baru muncul dengan status "Owned" dan Effective Cost dihalaman Stock Lots |
| Negatif — Input serial number duplikat (draf) | Pilih "Create"; Serial Number: SRL-2023-001; Product SKU: Laptop; Status: Available; Purchase Cost: 7500000; Serial Number: SRL-2023-001 (ulangi) | Muncul pesan kesalahan pesan yang jelas dan tidak bisa simpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Serial Number harus unik — tidak bisa ada dua unit dengan nomor serial yang sama |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Consignment Settlements — Modul Inventory

Bab manual: [`inventory/06-consignment-settlements.md`](../../erpApiServices/docs/manualBook/inventory/06-consignment-settlements.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Settle konsinyasi Paracetamol 500 mg strip (draf) | Klik "Settle Consignment"; pilih lot OBT-001; isikan Settlement Quantity 200; klik Save | Lot OBT-001 di-settle sebanyak 200 unit; status lot berubah; jurnal penjualan konsinyasi terbentuk |
| Negatif — Coba settle lot yang bukan konsinyasi (draf) | Pilih lot Amoxicillin 500 mg OBT-002; coba klik Settle Consignment | Muncul pesan penolakan yang jelas dan proses ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Valuasi Persediaan — Metode Eceran dan Penutupan Selisih Harga Beli

Bab manual: [`inventory/07-valuasi-metode-eceran-dan-selisih-harga-beli.md`](../../erpApiServices/docs/manualBook/inventory/07-valuasi-metode-eceran-dan-selisih-harga-beli.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Metode eceran berhasil (draf) | Buka `Inventory → Valuation → Retail Method`; pilih "Daftar Harga 1", tanggal mulai 01-01-2023, tanggal akhir 31-12-2023; klik **Hitung**; jika diperbolehkan, klik **Posting penyesuaian** | Estimasi nilai persediaan akhir ditampilkan; jurnal penyesuaian dibuat dan disimpan |
| Negatif — Pilihan periode kosong (draf) | Buka `Inventory → Valuation → Retail Method`; klik **Hitung** tanpa memilih periode | Pesan pesan yang jelas muncul, proses tidak lanjut |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pilih daftar harga dan periode (tanggal mulai dan tanggal akhir); gudang bersifat opsional. Daftar harga dan periode wajib dipilih sebelum menghitung |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setelah ditutup, periode itu tidak bisa ditutup lagi. Layar meminta konfirmasi sebelum menutup |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Diagram Alur Inventory — Modul Inventory

Bab manual: [`inventory/08-diagram-alur-inventory.md`](../../erpApiServices/docs/manualBook/inventory/08-diagram-alur-inventory.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Stock Adjustment berhasil dilakukan (draf) | Buka modul Inventory; Pilih menu Stock Adjustment; Masukkan SKU OBT-001; Pilih alasan penyesuaian; Approve; Post | Stok OBT-001 berubah sesuai jumlah yang disesuaikan; Stock History menunjukkan perubahan stok; Pesan pesan yang jelas muncul |
| Negatif — Stock Transfer gagal dikirim karena qty melebihi stok tersedia (draf) | Buka modul Inventory; Pilih menu Stock Transfer; Masukkan detail transfer; Submit; Cek gudang asal; Cari qty yang diminta lebih besar dari stok tersedia | Sistem menampilkan peringatan pesan yang jelas; Tidak bisa Ship; Pesan pesan yang jelas muncul |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | H -- I(["Stok disesuaikan, status Posted<br/tidak bisa diubah lagi"]) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Post hanya bisa dilakukan pada Stock Adjustment berstatus Approved |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Ship hanya bisa dari transfer berstatus Approved atau Partially Shipped (bab 03) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
