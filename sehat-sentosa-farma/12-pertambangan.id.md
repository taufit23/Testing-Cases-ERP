---
title: (PT Sehat Sentosa Farma) — 12. Pertambangan (Tambang Kapur)
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul mining untuk skenario PT Sehat Sentosa Farma. Pit, stockpile, log produksi dan penjualan bijih.
visibility: internal
---

# 12. Pertambangan (Tambang Kapur)

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** Konfigurasi oleh **Dr. Rahmat**; produksi dan hauling oleh **Joko Santoso** atau pengguna yang kamu beri peran tambang.

**Cabang aktif:** Pabrik Herbal Sukabumi (tambang kapur dikelola di cabang ini menurut profil `00`; sesuaikan bila kamu membuatnya terpisah).

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- Log produksi masuk ke stockpile; stockpile boleh dibatasi ke produk tertentu.
- Produksi melebihi estimasi cadangan pit diperingatkan atau ditolak menurut saklar.
- Jurnal tambang terposting di bawah tipe jurnal persediaan cabang.

## 1. Konfigurasi Tambang — Modul Mining

Bab manual: [`mining/01-konfigurasi-tambang.md`](../../erpApiServices/docs/manualBook/mining/01-konfigurasi-tambang.md)

**Input di:** `Mining → Config`, `Mining → Sites`, `Mining → Pits`, `Mining → Equipment`.

**Prasyarat:** Branch aktif sudah dipilih; modul Mining sudah aktif untuk branch ini.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Konfigurasi modul mining dilakukan dengan benar; site tambang Sehat Sentosa diatur; pit dan alat berat Kapur Medika dikonfigurasi; data produksi, hauling, dan royalti dapat dicatat. | Sukses setup modul mining untuk operasional tambang CV Kapur Medika. |
| Negatif — input salah (draf) | Input nama site tambang salah (contoh: Sehat Sentosa); harus diperbaiki menjadi Sehat Tambang. | Setup ditolak, pesan error pesan yang jelas. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Parameter Kualitas — Modul Mining

Bab manual: [`mining/02-parameter-kualitas.md`](../../erpApiServices/docs/manualBook/mining/02-parameter-kualitas.md)

**Input di:** `Mining → Quality Parameters` (`/mining/quality-parameters`).

**Prasyarat:** Tidak ada, tapi disarankan diisi sebelum mulai mencatat Production Log/Hauling supaya data kualitas ikut tercatat sejak awal.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | PT Sehat Sentosa Farma menginput parameter kualitas obat Paracetamol 500 mg strip (SKU OBT-001) dengan kadar tepat 500 mg per tablet, mencapai standar produksi. | Parameter kualitas tercatat dan disetujui. |
| Negatif — input salah (draf) | PT Sehat Sentosa Farma menginput parameter kualitas obat Paracetamol 500 mg strip (SKU OBT-001) dengan kadar 490 mg per tablet, di bawah standar produksi. | Input ditolak karena tidak memenuhi standar kualitas. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Produksi dan Hauling — Modul Mining

Bab manual: [`mining/03-produksi-dan-hauling.md`](../../erpApiServices/docs/manualBook/mining/03-produksi-dan-hauling.md)

**Input di:** `Mining → Production Logs` (`/mining/production-logs`), `Mining → Haulings` (`/mining/haulings`).

**Prasyarat:** Site, Pit, Equipment, dan Stockpile sudah dibuat (lihat chapter _01_ dan _04_).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Membuat Production Log untuk Jamu Kunyit Asam sachet (HRB-001) di Pabrik Herbal Sukabumi; Verifikasi dan Dispatch ke Apotek Sentosa Bandung | Production Log tercatat dengan benar, material dikirimkan sesuai jadwal |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Production Log berstatus Draft atau Verified masih bisa di-Cancel lewat tombol "Cancel Production Log". Log yang sudah Cancelled tidak bisa diubah lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hauling berstatus Draft atau In Transit masih bisa di-Cancel. Hauling yang sudah Delivered tidak bisa dibatalkan lagi — karena stok/perhitungan royalti mungkin sudah bergantung padanya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Stockpile — Modul Mining

Bab manual: [`mining/04-stockpile.md`](../../erpApiServices/docs/manualBook/mining/04-stockpile.md)

**Input di:** `Mining → Stockpiles` (`/mining/stockpiles`).

**Prasyarat:** Mining Site sudah dibuat (chapter _01_), Warehouse sudah dibuat di modul Inventory/Konfigurasi Umum.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendaftar Stockpile (draf) | Daftar stockpile CV Kapur Medika di Pabrik Herbal Sukabumi; hubungkan dengan gudang pusat | Tumpukan kapur karbonat terdaftar dan tersambung dengan inventaris gudang pusat |
| Negatif — Input Data Salah (draf) | Input nama tumpukan salah di Apotek Sentosa Bandung; coba hubungkan dengan gudang pusat | Pendaftaran ditolak pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Royalti — Modul Mining

Bab manual: [`mining/05-royalti.md`](../../erpApiServices/docs/manualBook/mining/05-royalti.md)

**Input di:** `Mining → Royalty Rates` (`/mining/royalty-rates`), `Mining → Royalties` (`/mining/royalties`).

**Prasyarat:** Royalty Rate sudah dibuat; sudah ada Hauling berstatus **Delivered** dengan tujuan **bukan stockpile** (Port/Customer/Other) dalam periode yang ingin dihitung.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Tarif royalti ditentukan dan periode hauling terpilih; dokumen royalti otomatis dibuat | Dokumen royalti sesuai dengan tarif dan periode hauling yang dipilih |
| Negatif — input salah (draf) | Periode hauling tidak ditemukan; tarif royalti kosong | Pengajuan ditolak karena periode hauling atau tarif royalti belum terisi dengan benar, dengan pesan kesalahan jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Royalty (transaksi) = dokumen yang di-generate otomatis oleh sistem, menghitung total royalti yang harus dibayar untuk hauling-hauling yang sudah terkirim dalam periode tertentu, berdasarkan tarif yang berlaku pada tanggal masing-masing hauling |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau tidak ada hauling yang memenuhi syarat pada periode tersebut, sistem juga menolak generate dengan pesan bahwa tidak ada hauling terkirim yang belum dihitung royaltinya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dokumen yang sudah di-generate tidak bisa diedit isinya — kalau ada hauling yang terlewat atau salah, generate ulang untuk periode yang benar (hauling yang sudah masuk dokumen aktif tidak akan ter-double-hitung di generate berikutnya) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mark as Paid — menandai royalti sudah dibayarkan ke pihak berwenang (hanya bisa dari status Approved) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Rekonsiliasi Survey — Modul Mining

Bab manual: [`mining/06-rekonsiliasi-survey.md`](../../erpApiServices/docs/manualBook/mining/06-rekonsiliasi-survey.md)

**Input di:** `Mining → Survey Reconciliations` (`/mining/survey-reconciliations`).

**Prasyarat:** Sudah ada Production Log (Verified) dan/atau Hauling (Delivered) di periode yang mau direkonsiliasi.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Rekonsiliasi Survey (draf) | Lakukan pembandingan hasil survey dengan catatan produksi hauling; perbaiki selisih volume | Selisih volume teridentifikasi dan diperbaiki |
| Negatif — Input data tidak valid (draf) | Masukkan data survey yang salah; sistem menolak input | Sistem menampilkan pesan kesalahan tentang data yang tidak valid |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dokumen berstatus Draft masih bisa di-Cancel. Dokumen yang sudah Finalized tidak bisa dibatalkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
