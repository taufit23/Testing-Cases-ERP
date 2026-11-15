---
title: (PT Sehat Sentosa Farma) — 06. Persediaan
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul inventory untuk skenario PT Sehat Sentosa Farma. Stok, transfer, opname dan nilai persediaan.
visibility: internal
---

# 06. Persediaan

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
| Positif — jalur normal (draf) | Konfigurasi metode penilaian persediaan menjadi FIFO, approve transfer stok antar gudang, setting auto-replenishment dengan reorder point 50 unit dan reorder quantity 100 unit | Proses inventory berjalan sesuai konfigurasi yang ditentukan |
| Negatif — input salah (draf) | Mencoba mengatur metode penilaian persediaan menjadi LIFO tanpa hak akses tinggi, mencoba approve transfer stok tanpa approval manager, setting auto-replenishment tanpa menentukan reorder point dan quantity | Konfigurasi gagal pesan penolakan yang jelas, pesan yang jelas, pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Supaya auto-draft Stock Transfer tahu harus ambil dari warehouse mana, tiap warehouse Store wajib punya minimal satu baris di Warehouse Supply Sources (lihat section di bawah) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Pilih Supply Warehouse (warehouse sumber — tidak boleh sama dengan Store Warehouse) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Store Warehouse dan Supply Warehouse tidak bisa diedit setelah dibuat — kalau salah pasangan, hapus baris dan buat ulang lewat "+ Add". Priority dan status masih bisa diubah lewat Edit |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Stock Adjustment — Modul Inventory

Bab manual: [`inventory/02-stock-adjustment.md`](../../erpApiServices/docs/manualBook/inventory/02-stock-adjustment.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menyesuaikan Stok Awal (draf) | Input SKU OBT-001 dengan qty 500 dan alasan 'Stok awal' di kantor pusat | Stock OBT-001 berubah menjadi 500 dengan status approved |
| Negatif — Menginput Alasan Kosong (draf) | Mencoba menyesuaikan stok tanpa alasan di kantor pusat | Tidak dapat disimpan, muncul pesan 'Alasan wajib diisi' |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setiap Stock Adjustment wajib memilih alasan dari daftar yang sudah disiapkan (bukan teks bebas) — supaya riwayat penyesuaian tetap terkategori dan bisa dianalisis |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Stock Adjustment yang sudah Posted tidak bisa diedit langsung — kalau ada kesalahan, buat adjustment koreksi baru (bukan mengubah yang lama), demi menjaga jejak audit |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Stock Transfer — Modul Inventory

Bab manual: [`inventory/03-stock-transfer.md`](../../erpApiServices/docs/manualBook/inventory/03-stock-transfer.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Klinik Pratama meminta transfer 100 botol Vitamin C dari gudang Jakarta ke Bekasi; Direktur mengapprove; Gudang Jakarta mengirim 50 botol pertama, sisa 50 botol dikirim besok. | Transfer disetujui dan tercatat; 50 botol diterima di Bekasi hari ini, 50 botol lainnya besok. |
| Negatif — input salah (draf) | Klinik Pratama meminta transfer 100 botol Vitamin C tanpa stock yang mencukupi di Jakarta; Direktur menolak permintaan tersebut. | Permintaan ditolak pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Pilih From Warehouse dan To Warehouse — keduanya tidak boleh sama, dan pilihan yang sudah dipakai di satu sisi otomatis tersembunyi dari sisi lainnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Tambahkan baris item — pilih Product SKU (stok yang tersedia di warehouse asal ditampilkan di sampingnya; SKU dengan stok 0 di warehouse asal tidak bisa dipilih), isi Qty Requested |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Qty yang diminta di suatu item tidak bisa dikirim melebihi sisa (Qty Requested − Qty Sent) — sistem menolak kalau shipment baru diminta memindahkan lebih dari sisa yang belum terkirim |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Stock Take (Opname) — Modul Inventory

Bab manual: [`inventory/04-stock-take.md`](../../erpApiServices/docs/manualBook/inventory/04-stock-take.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Stock Take Apotek Sentosa Bandung (draf) | Membuat sesi stock take, scan barcode produk, mengoreksi manual jika gagal, menyelesaikan penyesuaian stok | Stok sistem sejalan dengan stok fisik |
| Negatif — Barcode Produk Tidak Terdaftar di Sistem (draf) | Scan barcode gagal, link ke produk langsung saat scan tidak berhasil, pesan penolakan yang jelas | Input ditolak dengan pesan jelas pesan yang jelas, perbaiki data sebelum melanjutkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setelah semua item terhitung, klik "Complete" — konfirmasi di modal peringatan. Stock Take hanya bisa di-Complete dari status Draft atau In Progress |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Stock Lots & Serials — Modul Inventory

Bab manual: [`inventory/05-stock-lots-dan-serials.md`](../../erpApiServices/docs/manualBook/inventory/05-stock-lots-dan-serials.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Skenario Normal (draf) | Sentosa Farma memasukkan stok paracetamol 500 mg strip (SKU OBT-001) dengan lot number L123456789 dan tanggal kedaluwarsa 31/12/2023; diakui sebagai Stock Lots | Stok OBT-001 diterima dengan lot number L123456789, dapat dilacak per-batch, memudahkan klaim garansi dan perhitungan harga pokok |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Serial Number harus unik — tidak bisa ada dua unit dengan nomor serial yang sama |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Consignment Settlements — Modul Inventory

Bab manual: [`inventory/06-consignment-settlements.md`](../../erpApiServices/docs/manualBook/inventory/06-consignment-settlements.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menyimpan transaksi konsinyasi OBT-001, menyelesaikan settlement dengan pemilik barang titipan, memverifikasi data dan pembayaran yang benar | Settlement berhasil dilakukan, stok OBT-001 ter-update, laporan pembayaran tersedia |
| Negatif — input salah (draf) | Mencoba menyelesaikan settlement tanpa transaksi konsinyasi terlebih dahulu, mendapatkan pesan kesalahan pesan yang jelas | Transaksi ditolak, diberitahu untuk memasukkan transaksi konsinyasi terlebih dahulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Valuasi Persediaan — Metode Eceran dan Penutupan Selisih Harga Beli

Bab manual: [`inventory/07-valuasi-metode-eceran-dan-selisih-harga-beli.md`](../../erpApiServices/docs/manualBook/inventory/07-valuasi-metode-eceran-dan-selisih-harga-beli.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Input data persediaan dengan metode eceran di gudang pusat; posting penyesuaian jika konfigurasi izinkan; tutup selisih harga beli periode lalu | Nilai persediaan akhir dikalkulasi dengan benar, penyesuaian otomatis dilakukan, dan selisih harga beli ditutup dengan lancar |
| Negatif — input salah (draf) | Input data persediaan tanpa metode eceran; posting tanpa konfigurasi izin; tutup selisih harga beli periode yang tidak ada | Penyesuaian ditolak karena syarat tidak terpenuhi, muncul pesan galat dan perbaikan diperlukan untuk mematuhi prosedur |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pilih daftar harga dan periode (tanggal mulai dan tanggal akhir); gudang bersifat opsional. Daftar harga dan periode wajib dipilih sebelum menghitung |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setelah ditutup, periode itu tidak bisa ditutup lagi. Layar meminta konfirmasi sebelum menutup |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Diagram Alur Inventory — Modul Inventory

Bab manual: [`inventory/08-diagram-alur-inventory.md`](../../erpApiServices/docs/manualBook/inventory/08-diagram-alur-inventory.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal bab ini | Ikuti langkah di bab manual dengan data acuan file `00` (draf Ollama tidak dapat dipakai, isi manual) | Hasil sesuai uraian bab |
| Negatif — input tidak valid | Kosongkan field wajib atau isi di luar batas | Ditolak dengan pesan yang jelas, tidak ada data tersimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | H -- I(["Stok disesuaikan, status Posted<br/tidak bisa diubah lagi"]) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Post hanya bisa dilakukan pada Stock Adjustment berstatus Approved |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Ship hanya bisa dari transfer berstatus Approved atau Partially Shipped (bab 03) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
