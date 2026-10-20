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
| Positif — jalur normal (draf) | Setup Chart of Account Type dengan benar untuk entitas utama dan cabang; import template; buat manual untuk detail akun; lengkapi taxes sesuai peraturan | Semua setup berhasil, chart of account type dan tax tersedia di modul Akuntansi |
| Negatif — input salah (draf) | Input nama tax tidak sesuai format; coba import file Excel tanpa kolom wajib | Import gagal, muncul pesan kesalahan yang jelas tentang input atau format yang salah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Langkah 5 (COA) butuh Chart of Account Type (Langkah 1) sudah ada, karena setiap akun wajib pilih tipe-nya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sama seperti Langkah 1 — tersedia Use Template, Add (manual satu-satu), Bulk Add, dan Import from Excel untuk COA. Setiap akun wajib terhubung ke Chart of Account Type (Langkah 1) yang sudah dibuat sebelumnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mengisi Opening Balance di sini otomatis memposting jurnal saldo awal ke General Ledger (lihat syarat di Langkah 5 — akun equity harus sudah ditandai). Tujuannya sama dengan Langkah 8, hanya beda titik masuk (dari Bank Account, bukan dari COA) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Jurnal Manual — Modul Akuntansi

Bab manual: [`accounting/02-jurnal-manual.md`](../../erpApiServices/docs/manualBook/accounting/02-jurnal-manual.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Jurnal Penjualan Paracetamol (draf) | Membuat jurnal penjualan Paracetamol 500 mg strip ke Apotek Mitra Sehat; Approve & Post; Terlihat dalam laporan laba rugi | Berhasil mencatat transaksi penjualan dan menghasilkan laporan akuntansi yang benar |
| Negatif — Input tanpa Approval Workflow (draf) | Membuat jurnal tanpa aktivasi approval workflow; Tidak dapat approve & post; Ditolak pesan penolakan yang jelas | Penginputan ditolak karena syarat penggunaan fitur belum terpenuhi |
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
| Positif — Detail Ledger (draf) | Memasukkan nomor akun dan periode, menampilkan transaksi terperinci untuk akun tersebut | Menyajikan transaksi yang telah diposting dengan detail yang lengkap |
| Negatif — Summary by Account (draf) | Menggunakan kriteria tidak valid, misalnya jenis transaksi palsu | Menolak input pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi filter: Account (wajib pilih satu akun), Date From, Date To |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tabel menampilkan kolom Beginning/Period Movement/Ending Balance per akun, dengan baris Total di paling bawah. Baris Total inilah yang paling penting: total Debit harus sama dengan total Kredit untuk seluruh akun |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Tutup Periode & Tahun Fiskal — Modul Akuntansi

Bab manual: [`accounting/04-tutup-periode-dan-tahun-fiskal.md`](../../erpApiServices/docs/manualBook/accounting/04-tutup-periode-dan-tahun-fiskal.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Tutup Periode Bulanan (draf) | Langkah: Pilih periode Januari 2023, klik "Close" | Periode Januari 2023 terkunci dan laporan bulanan tersedia |
| Negatif — Input Tahun Fiskal Salah (draf) | Langkah: Masukkan tahun fiskal 2021, klik "Close" | Ditolak: Tahun fiskal harus 2022 atau setelahnya |
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
| Positif — Neraca Sehat Sentosa Farma (draf) | Buat neraca dengan aset Rp15M, kewajiban Rp8M, ekuitas Rp7M; cek keseimbangan | Aset = Kewajiban + Ekuitas (Rp15M = Rp8M + Rp7M) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Baru curigai konfigurasi Chart of Account Type — field Category, Normal Balance, dan Cash Flow Section per akun harus benar sejak awal setup |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Anggaran (Budget) — Modul Akuntansi

Bab manual: [`accounting/06-anggaran-budget.md`](../../erpApiServices/docs/manualBook/accounting/06-anggaran-budget.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Anggaran (draf) | Input data akun "Paracetamol" di klinik Bekasi untuk periode 2023, realisasikan per unit bisnis | Anggaran tersimpan dengan detail per unit dan periode, dapat dibandingkan dengan realisasi |
| Negatif — Input Realisasi Sebelum Anggaran (draf) | Mencoba memasukkan realisasi "Paracetamol" tanpa ada anggaran terlebih dahulu | Sistem menolak input, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Isi Fiscal Year (wajib) dan Name (nama anggaran, misalnya "Anggaran Operasional 2027") |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Aset Tetap & Penyusutan — Modul Akuntansi

Bab manual: [`accounting/07-aset-tetap-dan-penyusutan.md`](../../erpApiServices/docs/manualBook/accounting/07-aset-tetap-dan-penyusutan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendaftarkan Aset (draf) | PT Sehat Sentosa Farma memasukkan aset tetap baru dengan nilai awal Rp10 juta, masa manfaat 5 tahun, metode garis lurus; data valid | Aset tetap terdaftar dengan benar di sistem dan penyusutan otomatis dimulai |
| Negatif — Metode Penyusutan Salah (draf) | PT Sehat Sentosa Farma memilih metode penyusutan yang tidak sesuai (contoh: saldo menurun untuk aset garis lurus); data tidak valid | Sistem menolak input pesan penolakan yang jelas |
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
| Positif — Rekonsiliasi Bank (draf) | Setup akun bank Sentosa Farma, lakukan rekonsiliasi dengan rekening koran bank, selesaikan selisih dan catat jurnal koreksi | Saldo buku dan rekening koran bank cocok, selisih terjawab dengan jurnal koreksi yang benar |
| Negatif — Input Data Salah (draf) | Setup akun bank dengan data salah, coba lakukan rekonsiliasi | Sistem menolak setup akun karena data tidak valid, tampilkan pesan kesalahan yang jelas tentang kesalahan input |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Rekonsiliasi bank adalah proses mencocokkan dua catatan yang seharusnya sama tapi seringkali beda karena beda waktu pencatatan: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Laporan Pajak PPN — Modul Akuntansi

Bab manual: [`accounting/09-laporan-pajak-ppn.md`](../../erpApiServices/docs/manualBook/accounting/09-laporan-pajak-ppn.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membaca rekap PPN (draf) | Lihat rekap PPN Masukan/Keluaran Sentosa Farma; hitung Net Payable | Net Payable sesuai dengan perhitungan |
| Negatif — Retur tidak diinput (draf) | Input transaksi retur tanpa mengurangi total PPN Keluaran | Sistem menolak input dan memberi pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Chart of Accounts — Tree View, Saldo Akun & Jenis Jurnal

Bab manual: [`accounting/10-chart-of-accounts.md`](../../erpApiServices/docs/manualBook/accounting/10-chart-of-accounts.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Struktur Akun (draf) | Buat akun baru "Kas", pilih induk "Aset Lancar" & simpan | Struktur tampil dengan "Aset Lancarpesan yang jelasKas" di bawahnya |
| Negatif — Input Salah (draf) | Masukkan nama akun kosong & coba simpan | Terima inputan gagal, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
