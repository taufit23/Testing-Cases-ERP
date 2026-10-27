---
title: (PT Sehat Sentosa Farma) — 06. Persediaan
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul inventory untuk skenario PT Sehat Sentosa Farma. Stok, transfer, opname dan nilai persediaan.
visibility: internal
---

# 06. Persediaan

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** Konfigurasi oleh **Dr. Rahmat**. Transaksi stok oleh **Hendra Saputra** (Kepala Gudang); persetujuan penyesuaian oleh **Sari Wulandari**.

**Cabang aktif:** Pusat; transfer dan opname juga menyentuh Apotek Bandung.

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- Transfer stok bertahap (pengiriman ganda) dan penerimaan di gudang tujuan; nilai gabungan tidak berubah.
- Stok opname menghasilkan penyesuaian yang disetujui dan terjurnal.
- Metode costing rata-rata/FIFO terbuka untuk semua; LIFO, identifikasi khusus dan biaya standar hanya bila paket memuat fitur lanjutan.
- Rekonsiliasi Persediaan: nilai stok dari lapisan biaya = saldo akun persediaan di buku besar.
- Stok minimum per gudang dan riwayat pergerakan stok.

## 1. Konfigurasi Inventory — Modul Inventory

Bab manual: [`inventory/01-konfigurasi-inventory.md`](../../erpApiServices/docs/manualBook/inventory/01-konfigurasi-inventory.md)

**Input di:** `Inventory → Config` (`/inventory/config`) · `Inventory → Warehouse Supply Sources` (`/inventory/warehouse-supply-sources`) · `Inventory → Buffer Stock` (`/inventory/buffer-stock`) · `Inventory → Stock History` (`/inventory/stock-history`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Konfigurasi metode penilaian Paracetamol 500 mg strip (OBT-001) menjadi FIFo, approve transfer stok dari Jakarta ke Bandung, dan setting auto-replenishment dengan reorder point 200 botol | Stok OBT-001 di Jakarta berkurang, stok di Bandung bertambah, dan purchase request otomatis terbuat saat stok mencapai 200 botol |
| Negatif — input salah (draf) | Mencoba mengatur auto-replenishment tanpa menentukan reorder point atau reorder quantity | Sistem menolak konfigurasi pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Supaya auto-draft Stock Transfer tahu harus ambil dari warehouse mana, tiap warehouse Store wajib punya minimal satu baris di Warehouse Supply Sources (lihat section di bawah) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Pilih Supply Warehouse (warehouse sumber — tidak boleh sama dengan Store Warehouse) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Store Warehouse dan Supply Warehouse tidak bisa diedit setelah dibuat — kalau salah pasangan, hapus baris dan buat ulang lewat "+ Add". Priority dan status masih bisa diubah lewat Edit |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Stock Adjustment — Modul Inventory

Bab manual: [`inventory/02-stock-adjustment.md`](../../erpApiServices/docs/manualBook/inventory/02-stock-adjustment.md)

**Input di:** `Inventory → Stock Adjustments` (`/inventory/stock-adjustments`) dan `Inventory → Stock Adjustment Reasons` (`/inventory/stock-adjustment-reasons`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menyesuaikan Stok Awal (draf) | Input SKU OBT-001 dengan qty 500 unit; pilih alasan 'Stok awal'; submit & post | Stok OBT-001 berubah menjadi 500 unit, status transaksi tercatat dengan benar |
| Negatif — Input Salah | Input SKU OBT-001 dengan qty aktual negatif (mis. -5); alasan dipilih dari daftar yang tersedia (Correction, Damaged, Expired, Found, Initial Stock, Lost, Stock Opname Result); simpan | Tidak dapat disimpan, pesan penolakan yang jelas pada qty aktual dan tidak terposting |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap Stock Adjustment wajib memilih alasan dari daftar yang sudah disiapkan (bukan teks bebas) — supaya riwayat penyesuaian tetap terkategori dan bisa dianalisis |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Stock Adjustment yang sudah Posted tidak bisa diedit langsung — kalau ada kesalahan, buat adjustment koreksi baru (bukan mengubah yang lama), demi menjaga jejak audit |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Stock Transfer — Modul Inventory

Bab manual: [`inventory/03-stock-transfer.md`](../../erpApiServices/docs/manualBook/inventory/03-stock-transfer.md)

**Input di:** `Inventory → Stock Transfers` (`/inventory/stock-transfers`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Klinik Pratama mengajukan transfer 100 botol Vitamin C dari gudang Jakarta ke Bekasi; approval Direktur; pengiriman bertahap dalam 2 shipment; penerimaan di Bekasi berhasil. | Stok klinik Pratama berkurang, stok Klinik Pratama Bekasi bertambah sesuai permintaan. |
| Negatif — input salah (draf) | Apotek Sentosa Bandung mencoba transfer obat resep Amoxicillin ke Klinik Pratama tanpa resep; ditolak Direktur karena syarat tidak terpenuhi. | Permintaan transfer ditolak pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Pilih From Warehouse dan To Warehouse — keduanya tidak boleh sama, dan pilihan yang sudah dipakai di satu sisi otomatis tersembunyi dari sisi lainnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Tambahkan baris item — pilih Product SKU (stok yang tersedia di warehouse asal ditampilkan di sampingnya; SKU dengan stok 0 di warehouse asal tidak bisa dipilih), isi Qty Requested |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Qty yang diminta di suatu item tidak bisa dikirim melebihi sisa (Qty Requested − Qty Sent) — sistem menolak kalau shipment baru diminta memindahkan lebih dari sisa yang belum terkirim |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Stock Take (Opname) — Modul Inventory

Bab manual: [`inventory/04-stock-take.md`](../../erpApiServices/docs/manualBook/inventory/04-stock-take.md)

**Input di:** `Inventory → Stock Takes` (`/inventory/stock-takes`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Stock Take Apotek Sentosa Bandung (draf) | Membuat sesi opname, scan barcode produk, mengoreksi manual jika gagal, menyelesaikan opname; hasil akhir stok sistem setepat data fisik | Stok sistem sejalan dengan stok fisik, perbedaan tercatat dan dijelaskan |
| Negatif — Scan barcode gagal pada Jamu Kunyit Asam, Apotek Sentosa Bandung (draf) | Sesi opname dibatalkan, pesan error pesan yang jelas ditampilkan; user diminta memverifikasi kembali barcode atau menambahkan produk manual | Sistem menolak input dan memberikan petunjuk untuk memperbaiki masalah sebelum melanjutkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Stock Lots & Serials — Modul Inventory

Bab manual: [`inventory/05-stock-lots-dan-serials.md`](../../erpApiServices/docs/manualBook/inventory/05-stock-lots-dan-serials.md)

**Input di:** `Inventory → Stock Lots` (`/inventory/stock-lots`) dan `Inventory → Stock Serials` (`/inventory/stock-serials`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Skenario Normal (draf) | Langkah: Input SKU OBT-001 dengan jumlah 50 unit; Pilih opsi Stock Lots; Masukkan nomor lote "A123" dan tanggal kedaluwarsa | Hasil: Data lot tersimpan, harga pokok per-lote dapat dihitung, memudahkan klaim garansi |
| Negatif — Skenario Salah Input (draf) | Langkah: Input SKU OBT-001 dengan nomor lote duplikat "A123"; Tanggal kedaluwarsa masa depan | Hasil: Sistem menolak input, pesan penolakan yang jelas dan pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Serial Number harus unik — tidak bisa ada dua unit dengan nomor serial yang sama |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Consignment Settlements — Modul Inventory

Bab manual: [`inventory/06-consignment-settlements.md`](../../erpApiServices/docs/manualBook/inventory/06-consignment-settlements.md)

**Input di:** `Inventory → Consignment Settlements` (`/inventory/consignment-settlements`).

**Perhatikan:** **Terkait:** _01. Konfigurasi Inventory_ (Consignment Settlement Mode).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Klik "Settlement" -> Pilih konsinyasi OBT-001 -> Konfirmasi pembayaran 500.000 -> Terima notifikasi pembayaran berhasil | Proses settlement berhasil dan stok OBT-001 ter-update |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
