---
title: (PT Sehat Sentosa Farma) — 12. Pertambangan (Tambang Kapur)
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul mining untuk skenario PT Sehat Sentosa Farma. Pit, stockpile, log produksi dan penjualan bijih.
visibility: internal
---

# 12. Pertambangan (Tambang Kapur)

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Log produksi masuk ke stockpile; stockpile boleh dibatasi ke produk tertentu.
- Produksi melebihi estimasi cadangan pit diperingatkan atau ditolak menurut saklar.
- Jurnal tambang terposting di bawah tipe jurnal persediaan cabang.

## 1. Konfigurasi Tambang — Modul Mining

Bab manual: [`mining/01-konfigurasi-tambang.md`](../../erpApiServices/docs/manualBook/mining/01-konfigurasi-tambang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Konfigurasi tambang dilakukan dengan benar; site, pit, dan alat berat terdefinisi; data disimpan dengan sukses | Proses produksi, hauling, dan royalti dapat dilacak dengan baik |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Parameter Kualitas — Modul Mining

Bab manual: [`mining/02-parameter-kualitas.md`](../../erpApiServices/docs/manualBook/mining/02-parameter-kualitas.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menyiapkan parameter kualitas Paracetamol 500 mg strip (OBT-001) dengan kadar aktif bahan obat ≥98% | Kadar aktif bahan obat Paracetamol 500 mg strip mencapai standar ≥98%, produksi diteruskan |
| Negatif — input salah (draf) | Menentukan parameter kualitas Amoxicillin 500 mg (OBT-002) tanpa menentukan kadar aktif bahan obat | Pengajuan tidak valid, perlu menentukan parameter kualitas yang lengkap sebelum proses produksi dilanjutkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Produksi dan Hauling — Modul Mining

Bab manual: [`mining/03-produksi-dan-hauling.md`](../../erpApiServices/docs/manualBook/mining/03-produksi-dan-hauling.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Membuat Production Log untuk Jamu Kunyit Asam sachet (HRB-001) di Pabrik Herbal Sukabumi; Dispatch Hauling ke Apotek Sentosa Bandung; Verifikasi dan Deliver. | Proses produksi dan pengangkutan berjalan lancar, stok diperbarui dengan benar. |
| Negatif — input salah (draf) | Membuat Production Log tanpa mencantumkan SKU (HRB-001); Dispatch Hauling tanpa alamat tujuan. | Tidak dapat membuat Production Log dan Dispatch; muncul pesan kesalahan yang jelas tentang data yang harus diisi. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Production Log berstatus Draft atau Verified masih bisa di-Cancel lewat tombol "Cancel Production Log". Log yang sudah Cancelled tidak bisa diubah lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hauling berstatus Draft atau In Transit masih bisa di-Cancel. Hauling yang sudah Delivered tidak bisa dibatalkan lagi — karena stok/perhitungan royalti mungkin sudah bergantung padanya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Stockpile — Modul Mining

Bab manual: [`mining/04-stockpile.md`](../../erpApiServices/docs/manualBook/mining/04-stockpile.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendaftar Stockpile (draf) | Daftar stockpile CV Kapur Medika (SKU OBT-001) di Sukabumi; hubungkan dengan gudang pusat | Tampilan stockpile terdaftar dan koneksi dengan gudang valid |
| Negatif — Input Data Salah (draf) | Input SKU tidak sesuai (OBT-999); CV Kapur Medika tidak ada | Pesan kesalahan pesan yang jelas atau pesan yang jelas, penolakan input |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Royalti — Modul Mining

Bab manual: [`mining/05-royalti.md`](../../erpApiServices/docs/manualBook/mining/05-royalti.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Tarif royalti diatur, hauling terkirim periode Januari, generate dilakukan | Dokumen royalti untuk periode Januari otomatis terbuat dengan tarif yang ditentukan |
| Negatif — input salah (draf) | Tarif royalti tidak diperiksa, hauling luar periode, generate dilakukan tanpa persetujuan | Generate ditolak pesan penolakan yang jelas dan pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Royalty (transaksi) = dokumen yang di-generate otomatis oleh sistem, menghitung total royalti yang harus dibayar untuk hauling-hauling yang sudah terkirim dalam periode tertentu, berdasarkan tarif yang berlaku pada tanggal masing-masing hauling |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau tidak ada hauling yang memenuhi syarat pada periode tersebut, sistem juga menolak generate dengan pesan bahwa tidak ada hauling terkirim yang belum dihitung royaltinya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dokumen yang sudah di-generate tidak bisa diedit isinya — kalau ada hauling yang terlewat atau salah, generate ulang untuk periode yang benar (hauling yang sudah masuk dokumen aktif tidak akan ter-double-hitung di generate berikutnya) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mark as Paid — menandai royalti sudah dibayarkan ke pihak berwenang (hanya bisa dari status Approved) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Rekonsiliasi Survey — Modul Mining

Bab manual: [`mining/06-rekonsiliasi-survey.md`](../../erpApiServices/docs/manualBook/mining/06-rekonsiliasi-survey.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Rekonsiliasi Survey (draf) | Lakukan validasi volume survey dengan catatan produksi dan hauling; perbaiki selisih; finalisasi | Selisih terdeteksi dan diperbaiki, hasil akhir sesuai harapan |
| Negatif — Input Data Salah (draf) | Masukkan data survey tidak sesuai; sistem menolak; pesan kesalahan muncul | Input ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dokumen berstatus Draft masih bisa di-Cancel. Dokumen yang sudah Finalized tidak bisa dibatalkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Diagram Alur Mining — Modul Mining

Bab manual: [`mining/07-diagram-alur-mining.md`](../../erpApiServices/docs/manualBook/mining/07-diagram-alur-mining.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Alur tambang normal: produksi → hauling → stockpile → royalti → rekonsiliasi survey | Proses berjalan lancar, semua dokumen terverifikasi |
| Negatif — input salah (draf) | Input data haul log salah; tidak valid | Dokumen ditolak, pesan error pesan yang jelas muncul |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hauling yang sudah Delivered tidak bisa dibatalkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Reverse ditolak selama jurnal royalti masih menunggu persetujuan jurnal. Selesaikan persetujuannya dulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
