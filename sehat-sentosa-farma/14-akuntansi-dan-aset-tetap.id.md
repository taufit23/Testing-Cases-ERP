---
title: (PT Sehat Sentosa Farma) — 14. Akuntansi, Aset Tetap dan Pajak
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul accounting untuk skenario PT Sehat Sentosa Farma. Jurnal, buku besar, penutupan, laporan, anggaran, aset tetap, bank dan PPN.
visibility: internal
---

# 14. Akuntansi, Aset Tetap dan Pajak

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Jurnal tidak seimbang tidak bisa diposting; jurnal reverse bersifat aditif; periode tertutup menolak posting.
- Tutup tahun membuat jurnal penutup; Laba Rugi dan Anggaran vs Aktual tidak menghitung jurnal penutup, Neraca tetap menghitungnya.
- Ringkasan Pajak hanya menghitung jurnal yang sudah masuk buku besar.
- Aset tetap: jurnal akuisisi opsional, penyusutan bulanan, pelepasan tidak membuat akun aset negatif.
- Rekonsiliasi bank dan rekonsiliasi persediaan; saldo awal ke buku besar.

## 1. Setup Master Data & Saldo Awal — Modul Akuntansi

Bab manual: [`accounting/01-setup-master-data-dan-saldo-awal.md`](../../erpApiServices/docs/manualBook/accounting/01-setup-master-data-dan-saldo-awal.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Setup Chart of Account Type untuk Sentosa Farma; import template; verifikasi saldo awal di Journal & Reports | Semua account type terdefinisi dengan benar dan saldo awal akuntansi valid |
| Negatif — input salah (draf) | Input salah dalam Chart of Account Type; coba import template yang tidak sesuai | Import ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Langkah 5 (COA) butuh Chart of Account Type (Langkah 1) sudah ada, karena setiap akun wajib pilih tipe-nya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sama seperti Langkah 1 — tersedia Use Template, Add (manual satu-satu), Bulk Add, dan Import from Excel untuk COA. Setiap akun wajib terhubung ke Chart of Account Type (Langkah 1) yang sudah dibuat sebelumnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mengisi Opening Balance di sini otomatis memposting jurnal saldo awal ke General Ledger (lihat syarat di Langkah 5 — akun equity harus sudah ditandai). Tujuannya sama dengan Langkah 8, hanya beda titik masuk (dari Bank Account, bukan dari COA) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Jurnal Manual — Modul Akuntansi

Bab manual: [`accounting/02-jurnal-manual.md`](../../erpApiServices/docs/manualBook/accounting/02-jurnal-manual.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Jurnal Penjualan Obat (draf) | Input jurnal penjualan obat Paracetamol 500 mg strip ke Apotek Sentosa Bandung; Approve & Post; Terlihat transaksi di laporan penjualan | Transaksi tercatat dengan benar, laporan penjualan update |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jurnal yang sudah Posted tidak bisa dihapus atau diedit langsung — karena sudah resmi mengubah saldo dan mungkin sudah "dilaporkan" ke pihak lain (bank, kantor pajak, dst). Satu-satunya cara mengoreksi jurnal yang sudah posted adalah Reverse: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kedua jurnal (asli + kebalikannya) tetap tersimpan selamanya — ini prinsip audit trail: riwayat tidak boleh hilang atau berubah diam-diam, koreksi harus lewat entri baru, bukan mengubah yang lama |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jurnal yang masih Draft tidak bisa di-Reverse (tombolnya nonaktif) — untuk jurnal draft yang salah, langsung Delete saja, tidak perlu reverse |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Create Bulk Journal — buat beberapa jurnal sekaligus dalam satu form: tiap blok punya Code/Date/Description dan baris jurnalnya sendiri, masing-masing blok wajib Balanced sebelum bisa Save |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. General Ledger & Neraca Saldo — Modul Akuntansi

Bab manual: [`accounting/03-general-ledger-dan-neraca-saldo.md`](../../erpApiServices/docs/manualBook/accounting/03-general-ledger-dan-neraca-saldo.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Detail Ledger (draf) | Cek detail ledger Paracetamol 500 mg strip (SKU OBT-001) di kantor pusat | Jurnal tercatat dengan benar dan sesuai saldo akhir bulan |
| Negatif — Summary by Account (draf) | Menggunakan filter salah untuk account non-exist | Tampilan error atau pesan bahwa account tidak ditemukan, tidak menampilkan data apa pun |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi filter: Account (wajib pilih satu akun), Date From, Date To |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tabel menampilkan kolom Beginning/Period Movement/Ending Balance per akun, dengan baris Total di paling bawah. Baris Total inilah yang paling penting: total Debit harus sama dengan total Kredit untuk seluruh akun |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Tutup Periode & Tahun Fiskal — Modul Akuntansi

Bab manual: [`accounting/04-tutup-periode-dan-tahun-fiskal.md`](../../erpApiServices/docs/manualBook/accounting/04-tutup-periode-dan-tahun-fiskal.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Tutup Periode Bulanan (draf) | Langkah: Pilih periode Januari 2023, klik "Close", konfirmasi | Periode Januari 2023 terkunci dan laporan keuangan bulan tersebut tersedia |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Pastikan semua jurnal bertanggal bulan tersebut sudah Posted (bukan Draft) — kalau masih ada draft, Close akan ditolak dengan pesan jelas ("ada jurnal belum posted, post atau hapus dulu") |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Periode yang belum Closed tidak bisa langsung di-Lock (opsi ini otomatis nonaktif). Setelah Locked, sama seperti Closed — tidak ada jurnal baru yang bisa masuk ke tanggal tersebut |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Semua Accounting Period dalam tahun itu (biasanya 12 bulan) harus sudah Closed. Kalau bulan tertentu tidak ada transaksinya sama sekali, tetap bisa di-Close (tidak ada jurnal draft yang memblokir) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Ada tepat SATU akun di Chart of Accounts yang ditandai "Is Retained Earnings Account". Kalau nol akun yang ditandai, atau lebih dari satu, sistem menolak — sistem sengaja tidak mau menebak akun mana yang benar |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Laporan Keuangan — Modul Akuntansi

Bab manual: [`accounting/05-laporan-keuangan.md`](../../erpApiServices/docs/manualBook/accounting/05-laporan-keuangan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Neraca Sehat Sentosa Farma (draf) | Memasukkan data aset dan kewajiban tahunan; memeriksa saldo modal; mengevaluasi rasio likuiditas | Neraca seimbang dengan total aset = total kewajiban + modal, rasio likuiditas sesuai standar industri farmasi |
| Negatif — Laba Rugi Sentosa Farma (draf) | Menginput data penjualan dan biaya yang tidak valid; mengabaikan syarat penilaian laba rugi | Input ditolak: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Baru curigai konfigurasi Chart of Account Type — field Category, Normal Balance, dan Cash Flow Section per akun harus benar sejak awal setup |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Anggaran (Budget) — Modul Akuntansi

Bab manual: [`accounting/06-anggaran-budget.md`](../../erpApiServices/docs/manualBook/accounting/06-anggaran-budget.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | PT Sehat Sentosa Farma membuat anggaran untuk klinik Bekasi & apotek Bandung; membandingkan dengan realisasi; status budget diperbarui secara otomatis | Anggaran akun terbentuk, dibandingkan dengan realisasi, dan status budget diperbarui sesuai periode |
| Negatif — input salah (draf) | PT Sehat Sentosa Farma mencoba membuat anggaran untuk periode yang telah berlalu; syarat masa depan gagal | Input tidak valid: anggaran hanya bisa dibuat untuk periode aktif/masa depan, silakan pilih periode masa depan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Isi Fiscal Year (wajib) dan Name (nama anggaran, misalnya "Anggaran Operasional 2027") |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Aset Tetap & Penyusutan — Modul Akuntansi

Bab manual: [`accounting/07-aset-tetap-dan-penyusutan.md`](../../erpApiServices/docs/manualBook/accounting/07-aset-tetap-dan-penyusutan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendaftarkan Aset (draf) | PT Sehat Sentosa Farma memasukkan aset tetap kantor pusat, termasuk nilai historis dan estimasi umur manfaat | Aset tetap terdaftar dengan benar di sistem akuntansi |
| Negatif — Metode Penyusutan Salah (draf) | Menggunakan metode garis lurus untuk aset yang lebih cocok menggunakan saldo menurun | Sistem memberikan pesan kesalahan tentang pemilihan metode yang tidak tepat |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Wajib dijalankan tiap bulan, per aset — sistem tidak otomatis menyusutkan semua aset sekaligus setiap bulan berjalan (tidak ada cron/scheduler bawaan untuk ini). Kalau ada beberapa aset, ulangi langkah ini untuk masing-masing aset setiap bulannya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sistem mencegah penyusutan ganda untuk periode yang sama — kalau Run Depreciation diklik lagi dengan Period Date bulan yang sudah pernah diproses, akan ditolak. Ini penting supaya Beban Penyusutan tidak tercatat dobel di laporan keuangan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Neraca (Balance Sheet) — cari akun Akumulasi Penyusutan di Trial Balance/COA, saldonya harus negatif (mengurangi total Aset Tetap) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Laba Rugi (Income Statement) — akun Beban Penyusutan harus muncul di section Expense, sebesar total penyusutan periode itu dari semua aset yang sudah diproses |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Rekonsiliasi Bank — Modul Akuntansi

Bab manual: [`accounting/08-rekonsiliasi-bank.md`](../../erpApiServices/docs/manualBook/accounting/08-rekonsiliasi-bank.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Rekonsiliasi Bank (draf) | Setup bank account Sentosa Farma; Buat rekonsiliasi; Selesaikan selisih dengan jurnal koreksi; Selisih teridentifikasi dan diperbaiki | Saldo buku dan rekening koran sejalan, akuntansi benar |
| Negatif — Rekonsiliasi Bank (draf) | Setup bank account tanpa data valid; Buat rekonsiliasi tanpa saldo awal | Proses tidak dapat dilanjutkan, muncul pesan kesalahan tentang data yang harus diisi terlebih dahulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Rekonsiliasi bank adalah proses mencocokkan dua catatan yang seharusnya sama tapi seringkali beda karena beda waktu pencatatan: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Laporan Pajak PPN — Modul Akuntansi

Bab manual: [`accounting/09-laporan-pajak-ppn.md`](../../erpApiServices/docs/manualBook/accounting/09-laporan-pajak-ppn.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Cek PPN Masukan (draf) | Input rekap PPN masukan, hitung net payable, periksa batasan cakupan | Net payable sesuai harapan, laporan valid |
| Negatif — Input data salah (draf) | Input jumlah PPN masukan tidak akurat, terlalu besar | Laporan ditolak, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Chart of Accounts — Tree View, Saldo Akun & Jenis Jurnal

Bab manual: [`accounting/10-chart-of-accounts.md`](../../erpApiServices/docs/manualBook/accounting/10-chart-of-accounts.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Struktur Akun (draf) | Buat akun baru untuk Paracetamol 500 mg strip (SKU OBT-001) dan lihat strukturnya sebagai pohon; otomatis disusun ke akun induk Obat & Alat Kesehatan | Menampilkan struktur akun Paracetamol 500 mg strip di bawah akun induk Obat & Alat Kesehatan |
| Negatif — Saldo Akun (draf) | Input saldo awal untuk Jamu Kunyit Asam sachet (HRB-001) tanpa memilih jenis jurnal; coba simpan | Muncul pesan kesalahan bahwa harus memilih jenis jurnal sebelum menyimpan saldo akun |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Syarat: asisten AI harus aktif dan pengungkapan AI cabang sudah dikonfirmasi. Pengguna yang boleh menambah akun otomatis boleh memakai bantuan ini. Aturan simpan tetap dicek server, misalnya laba ditahan hanya boleh satu per cabang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Diagram Alur Accounting — Modul Accounting

Bab manual: [`accounting/11-diagram-alur-accounting.md`](../../erpApiServices/docs/manualBook/accounting/11-diagram-alur-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Sentosa Farma membuat jurnal penjualan obat Paracetamol 500 mg strip ke Apotek Mitra Sehat | Jurnal terdaftar dan diposting dengan benar di modul accounting |
| Negatif — input salah (draf) | Input harga jual obat yang salah pada draft jurnal | Sistem menolak inputan, memberikan pesan kesalahan harga harus sesuai data master produk |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jurnal yang belum seimbang tetap tersimpan sebagai Draft, tetapi tidak bisa di-Post |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tanggal jurnal harus berada di Accounting Period yang masih terbuka |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | B --/"Ya"/ C["Ditolak: jurnal sudah di-reverse"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | D --/"Ya, dan pembalikan penutup tidak diizinkan cabang"/ E["Ditolak"] |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
