---
title: (PT Medika Nusantara Sejahtera) — 24. Kerjasama (Partnership)
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul kerjasama untuk skenario PT Medika Nusantara Sejahtera. Tipe, katalog paket, perjanjian berversi, pemakaian dan tagihan mitra.
visibility: internal
---

# 24. Kerjasama (Partnership)

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji kerjasama dengan pihak lain: perjanjian, rekap penyelesaian, dan pembayaran.
>
> **Kalau semuanya benar, artinya:** Nilai kerjasama dihitung sesuai perjanjian dan tagihannya tidak salah hitung.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Penawaran berversi dan perjanjian lewat persetujuan; rantai klien.
- Pemakaian direkap menjadi tagihan; penyelesaian terjurnal.
- Kewajiban dan penyesuaian kerja custom tercatat dan terlaporkan.

## 1. Pengaturan, Tipe Kerjasama, dan Katalog Paket — Modul Kerjasama

Bab manual: [`kerjasama/01-pengaturan-tipe-dan-katalog-paket.md`](../../erpApiServices/docs/manualBook/kerjasama/01-pengaturan-tipe-dan-katalog-paket.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengaturan cabang (draf) | Buka Kerjasama → Config; Pilih Agreements Require Approval: Tidak; Set Default Cadence: Bulanan; Klik Save | Status pengaturan berubah menjadi tidak memerlukan persetujuan perjanjian, dan default cadens perjanjian baru adalah bulanan. |
| Negatif — Pengaturan cabang (draf) | Buka Kerjasama → Config; Pilih Agreements Require Approval: Ya; Tidak Memilih Default Cadence; Klik Save | Muncul pesan kesalahan pesan yang jelas. |
| Positif — Tipe kerjasama (draf) | Buka Kerjasama → Types; Klik Reseller perangkat lunak (sewa); Ubah Name: Reseller Alkes; Model nilai: Harga dasar + margin; Kadens: Bulanan; Syarat bawaan: Tidak ada; Klik Save | Tipe kerjasama "Reseller Alkes" ditambahkan dengan pengaturan yang disesuaikan. |
| Negatif — Tipe kerjasama (draf) | Buka Kerjasama → Types; Pilih Reseller perangkat lunak (sewa); Ubah Name: ""; Klik Save | Muncul pesan kesalahan pesan yang jelas. |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Perjanjian Kerjasama dan Rantai Klien — Modul Kerjasama

Bab manual: [`kerjasama/02-perjanjian-dan-rantai-klien.md`](../../erpApiServices/docs/manualBook/kerjasama/02-perjanjian-dan-rantai-klien.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat perjanjian baru (draf) | Buka Kerjasama → Agreements; klik New Agreement; isi judul "Perjanjian Medika Nusantara"; pilih tipe "Kita menyediakan", lawan pihak "Apotek Mitra Sehat"; item harga Paracetamol 500 mg strip (SKU OBT-001) dengan margin 20%; klik Save | Perjanjian ditambahkan; status menjadi Diajukan; jurnal rekap Piutang debit dan Pendapatan kredit terbentuk |
| Negatif — Membuat perjanjian tanpa tanggal mulai (draf) | Buka Kerjasama → Agreements; klik New Agreement; isi judul "Perjanjian Medika Nusantara"; pilih tipe "Kita menyediakan", lawan pihak "Apotek Mitra Sehat"; item harga Paracetamol 500 mg strip (SKU OBT-001) dengan margin 20%; klik Submit tanpa tanggal mulai | Perjanjian ditolak; pesan penolakan yang jelas muncul |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 5. Biarkan Fill responsibilities and obligations from the type menyala bila ingin matriks tanggung jawab dan kewajiban awal terisi dari preset tipe |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Draft → Diajukan → Disetujui → Aktif ⇄ Ditangguhkan → Berakhir / Diakhiri, dengan Ditolak dan Dibatalkan sebagai ujung lain |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item yang sudah dipakai rekap atau perjanjian anak tidak bisa dihapus; akhiri saja item itu dengan tanggal berakhir |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu titik tiga di pojok kanan atas detail: Export PDF / Excel menghasilkan dokumen perjanjian (syarat, harga, para pihak, matriks tanggung jawab, kewajiban) dengan pengaturan ekspor dokumen cabang. Dokumen bertanda tangan diunggah di tab History (lampiran) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Penawaran Berversi — Modul Kerjasama

Bab manual: [`kerjasama/03-penawaran-berversi.md`](../../erpApiServices/docs/manualBook/kerjasama/03-penawaran-berversi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat penawaran baru (draf) | Buka Kerjasama → Proposals; klik New Proposal; isikan lawan pihak, tipe kerjasama, arah, model nilai, tanggal, syarat, para pihak, dan item harga; masukkan Version Label "V1.0"; validasi sampai Sent | Status menjadi Sent, penawaran V1.0 tersedia untuk diteruskan ke langkah selanjutnya |
| Negatif — Menghapus penawaran yang sudah terkirim (draf) | Buka detail penawaran V1.5; klik tombol Delete; cek status penawaran | Tidak dapat menghapus, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Pemakaian, Rekap Periodik, dan Tagihan — Modul Kerjasama

Bab manual: [`kerjasama/04-pemakaian-rekap-dan-tagihan.md`](../../erpApiServices/docs/manualBook/kerjasama/04-pemakaian-rekap-dan-tagihan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat pemakaian (draf) | Masuk ke `Kerjasama → Settlements`, klik `Usage`; pilih periode, jenis (jumlah), nilai 100; klik `Add Usage` | Catatan pemakaian ditambahkan dengan status belum diverifikasi |
| Negatif — Input salah (draf) | Mencoba menambahkan catatan pemakaian tanpa memilih periode | Sistem memberikan pesan peringatan bahwa periode harus dipilih |
| Positif — Membuat rekap (draf) | Buka tab `Settlements`, klik `Generate Settlement`; pilih model nilai (Tarif tetap), periode 1 Januari - 31 Januari; klik `Generate` | Rekap otomatis dibuat sebagai draft dan status perjanjian berubah menjadi "Draft" |
| Negatif — Syarat tidak terpenuhi (draf) | Mencoba membuat rekap tanpa periode | Sistem memberikan pesan bahwa periode harus dipilih |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Rekap hanya bisa dibuat untuk perjanjian yang Active, yang punya tanggal mulai dan kadens berulang supaya periode berikutnya bisa ditentukan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Membatalkan rekap yang sudah ditagihkan lewat faktur memerlukan pembatalan faktur lebih dulu. Pembatalan juga ditolak selama jurnal rekap masih menunggu persetujuan jurnal |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Kewajiban, Penyesuaian Biaya, Kerja Custom, dan Laporan — Modul Kerjasama

Bab manual: [`kerjasama/05-kewajiban-penyesuaian-kerja-custom-dan-laporan.md`](../../erpApiServices/docs/manualBook/kerjasama/05-kewajiban-penyesuaian-kerja-custom-dan-laporan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat kewajiban pelatihan (draf) | Masuk ke tab Obligations; klik Add Obligation; pilih Pelatihan, Dokumentasi; masukkan penanggung jawab kita; tentukan tenggat waktu; upload manual book | Kewajiban pelatihan ditambahkan dengan status pending dan bukti manual book tersedia |
| Negatif — Menolak permintaan penyesuaian biaya (draf) | Masuk ke tab Adjustments; klik Add Adjustment Proposal; masukkan rincian hitung; pihak lawan menolak; cek status proposal | Pesan pesan yang jelas muncul dan status proposal berubah menjadi Rejected |
| Negatif — Membuat permintaan kerja custom tanpa estimasi (draf) | Masuk ke tab Work Requests; klik New Work Request; masukkan judul dan uraian; cek Work Request Mode Project; tidak memasukkan estimasi; coba mulai pekerjaan | Pesan pesan yang jelas muncul dan permintaan tidak dapat dimulai |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tab Obligations mencatat hal non-uang yang harus terpenuhi, masing-masing dengan penanggung jawab (kita, lawan pihak, atau keduanya), tenggat, status, dan bukti: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Diagram Alur Kerjasama — Modul Kerjasama

Bab manual: [`kerjasama/06-diagram-alur-kerjasama.md`](../../erpApiServices/docs/manualBook/kerjasama/06-diagram-alur-kerjasama.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Penawaran Berversi V1.0 diterima (draf) | Masuk ke menu Penawaran, pilih penawaran OBT-001, klik Convert menjadi Perjanjian Draft | Status perjanian berubah menjadi Draft dan header, syarat, para pihak, dan item harga disimpan |
| Negatif — Rekap tanpa periode dipilih (draf) | Masuk ke menu Rekap, klik Generate tanpa memilih periode | Sistem menandai dan memberi tahu untuk memilih periode berikutnya yang belum direkap, rekap tidak di-generate |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | OBL["Kewajiban kedua pihak<br/bab 05"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Perjanjian harus punya tanggal mulai sebelum bisa di-Submit |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pengingat kewajiban dan tinjau harga juga dijalankan otomatis |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
