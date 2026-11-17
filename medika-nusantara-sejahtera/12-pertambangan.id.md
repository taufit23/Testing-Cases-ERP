---
title: (PT Medika Nusantara Sejahtera) — 12. Pertambangan (Tambang Kapur)
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul mining untuk skenario PT Medika Nusantara Sejahtera. Pit, stockpile, log produksi dan penjualan bijih.
visibility: internal
---

# 12. Pertambangan (Tambang Kapur)

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji pertambangan: produksi, pengangkutan, mutu, dan royalti.
>
> **Kalau semuanya benar, artinya:** Hasil tambang tercatat, royalti dihitung benar, dan selisih survei bisa ditelusuri.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Log produksi masuk ke stockpile; stockpile boleh dibatasi ke produk tertentu.
- Produksi melebihi estimasi cadangan pit diperingatkan atau ditolak menurut saklar.
- Jurnal tambang terposting di bawah tipe jurnal persediaan cabang.

## 1. Konfigurasi Tambang — Modul Mining

Bab manual: [`mining/01-konfigurasi-tambang.md`](../../erpApiServices/docs/manualBook/mining/01-konfigurasi-tambang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Buka Mining → Config; isi pengaturan; klik Save | Pengaturan tersimpan, konfirmasi dengan tim accounting diperlukan |
| Negatif — input salah (draf) | Tidak memilih branch aktif sebelum mengakses Mining → Config | Akses ditolak pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Parameter Kualitas — Modul Mining

Bab manual: [`mining/02-parameter-kualitas.md`](../../erpApiServices/docs/manualBook/mining/02-parameter-kualitas.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambahkan parameter kualitas baru (draf) | Buka `/mining/quality-parameters`; klik "+ Tambah Parameter Kualitas"; isi Code `MOISTURE`, Name "Kadar Air", Unit `%`, Commodity "Jamu", Sort Order 3, Active checked; Klik Save. | Parameter "Kadar Air" muncul di form Production Log dan Hauling dengan status aktif. |
| Negatif — Menambahkan parameter kualitas tanpa kode unik (draf) | Buka `/mining/quality-parameters`; klik "+ Tambah Parameter Kualitas"; isi Name "Kadar Nikel", Unit `%`, Commodity "Nikel", Sort Order 1, Active checked; Klik Save. | Muncul pesan kesalahan pesan yang jelas. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Produksi dan Hauling — Modul Mining

Bab manual: [`mining/03-produksi-dan-hauling.md`](../../erpApiServices/docs/manualBook/mining/03-produksi-dan-hauling.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat log produksi (draf) | Buka /mining/production-logs; pilih site "Sukabumi", pit "Pit A", stockpile "Stockpile 1", equipment "Excavator 1", material type "Bahan Galian", product "HRB-001", quantity 50, cost per unit 20000, quality 85; klik Save Production Log | Production Log status Draft tersimpan, field terkunci setelah bukan draft |
| Negatif — Input material type tidak Ore (draf) | Buka /mining/production-logs; pilih site "Sukabumi", pit "Pit A", equipment "Excavator 1", material type "Overburden", quantity 50, klik Save Production Log | Muncul pesan kesalahan: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Production Log berstatus Draft atau Verified masih bisa di-Cancel lewat tombol "Batalkan Log Produksi". Log yang sudah Cancelled tidak bisa diubah lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hauling berstatus Draft atau In Transit masih bisa di-Cancel. Hauling yang sudah Delivered tidak bisa dibatalkan lagi — karena stok/perhitungan royalti mungkin sudah bergantung padanya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Stockpile — Modul Mining

Bab manual: [`mining/04-stockpile.md`](../../erpApiServices/docs/manualBook/mining/04-stockpile.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat stockpile baru (draf) | Buka Mining → Stockpiles; tambah: Mining Site Sukabumi, Warehouse Medika Nusantara Sejahtera, Code ALK-001, Name Tumpukan Alkohol Swab, Stockpile Type Product; Save. | Stockpile ALK-001 muncul di list dengan status Active dan terhubung ke Warehouse Medika Nusantara Sejahtera. |
| Negatif — Membuat stockpile tanpa memilih mining site (draf) | Buka Mining → Stockpiles; tambah: skip Mining Site, Warehouse Medika Nusantara Sejahtera, Code ALK-002, Name Tumpukan Masker Medis, Stockpile Type Product; Save. | Sistem menolak input dan mengeluarkan pesan penolakan yang jelas. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Royalti — Modul Mining

Bab manual: [`mining/05-royalti.md`](../../erpApiServices/docs/manualBook/mining/05-royalti.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Generate royalti untuk Site Sukabumi (draf) | Buka Mining → Royalties; klik "+ Buat"; pilih Mining Site "Pabrik Herbal Sukabumi"; tanggal periode 1 Januari - 31 Desember 2023; klik Generate | Dokumen royalti otomatis terbentuk untuk hauling yang sudah terkirim pada periode tersebut, berdasarkan tarif yang berlaku |
| Negatif — Generate royalti tanpa Royalty Rate aktif (draf) | Buka Mining → Royalties; klik "+ Buat"; pilih Mining Site "Pabrik Herbal Sukabumi"; tanggal periode 1 Januari - 31 Desember 2023; klik Generate | Sistem menolak dan memberikan pesan bahwa tidak ada tarif royalti aktif yang cocok untuk site tersebut |
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
| Positif — Membuat survey reconciliation (draf) | Buka Mining → Survey Reconciliations; klik "+ Buat"; isikan: Site: Kebumen, Period Start: 1 Januari 2023, Period End: 31 Januari 2023, Survey Quantity: 5.000 m³; klik Save Reconciliation | Production Quantity dan Weighbridge Quantity dihitung otomatis; Variance Quantity dan Variance Percent ditampilkan; status Draft |
| Negatif — Input period end lebih awal dari start (draf) | Buka Mining → Survey Reconciliations; isikan Period End: 1 Januari 2023, Period Start: 1 Februari 2023 | Muncul pesan penolakan yang jelas; status Draft tetap |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dokumen berstatus Draft masih bisa di-Cancel. Dokumen yang sudah Finalized tidak bisa dibatalkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Diagram Alur Mining — Modul Mining

Bab manual: [`mining/07-diagram-alur-mining.md`](../../erpApiServices/docs/manualBook/mining/07-diagram-alur-mining.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Verify log bijih (draf) | Masuk ke Production Log; Pilih log OBT-001; Klik 'Verify'; Isi berat kotor 500 kg, tare 20 kg; Simpan | Stok stockpile OBT-001 bertambah 380 kg; Jurnal royalti dibuat untuk 380 kg dengan biaya per unit sesuai log |
| Negatif — Cancel royalti Approved (draf) | Pilih royalti Approved ALK-002; Klik 'Cancel'; Cek pesan error | Tampilan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hauling yang sudah Delivered tidak bisa dibatalkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Reverse ditolak selama jurnal royalti masih menunggu persetujuan jurnal. Selesaikan persetujuannya dulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
