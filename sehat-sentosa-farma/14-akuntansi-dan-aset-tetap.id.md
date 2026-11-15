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
| Positif — Setup Chart of Account Type (draf) | Pilih "Use Template", pilih template ASSET, LIABILITY, EQUITY, REVENUE, EXPENSE; klik Apply/Use | Tampilan COA Type lengkap dengan 5 tipe akun yang dipilih, status sukses |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Langkah 5 (COA) butuh Chart of Account Type (Langkah 1) sudah ada, karena setiap akun wajib pilih tipe-nya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sama seperti Langkah 1 — tersedia Use Template, Add (manual satu-satu), Bulk Add, dan Import from Excel untuk COA. Setiap akun wajib terhubung ke Chart of Account Type (Langkah 1) yang sudah dibuat sebelumnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mengisi Opening Balance di sini otomatis memposting jurnal saldo awal ke General Ledger (lihat syarat di Langkah 5 — akun equity harus sudah ditandai). Tujuannya sama dengan Langkah 8, hanya beda titik masuk (dari Bank Account, bukan dari COA) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Jurnal Manual — Modul Akuntansi

Bab manual: [`accounting/02-jurnal-manual.md`](../../erpApiServices/docs/manualBook/accounting/02-jurnal-manual.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat jurnal baru (draf) | Buka Journals; klik "+ Create Journal"; masukkan Code: 202301, Date: 1 Januari 2023, Description: Pembelian obat; tambahkan baris dengan Account: Inventory (Debit), Tax %: 10%, Business Unit: Kantor Pusat & Distribusi Jakarta; klik Save | Header jurnal berubah status menjadi Balanced; jurnal baru muncul di daftar dengan status Draft |
| Negatif — Menghapus jurnal yang sudah posted (draf) | Buka Journals; pilih jurnal yang sudah Posted; coba klik tombol Delete | Muncul pesan penolakan yang jelas; status jurnal tetap Posted |
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
| Positif — Menampilkan detail ledger akun Paracetamol 500 mg strip (SKU OBT-001) dari Januari hingga Desember 2026 (draf) | Buka General Ledger; Pilih Account: SKU OBT-001; Date From: 01/01/2026; Date To: 31/12/2026; Klik Search | Kartu Opening Balance, Period Movement, dan Closing Balance akun Paracetamol 500 mg strip ditampilkan. Tabel menunjukkan riwayat transaksi dengan saldo berjalan per tanggal. |
| Negatif — Trial Balance tidak seimbang untuk periode Januari 2026 karena ada jurnal yang tercatat hanya sebelah (draf) | Buka Trial Balance; Pilih Period: Januari 2026; Klik Search; Periksa baris Total | Pesan error muncul menunjukkan Debit ≠ Kredit. Baris Total menunjukkan jumlah Debit dan Kredit yang tidak seimbang, mengindikasikan ada jurnal yang tercatat hanya sebelah. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi filter: Account (wajib pilih satu akun), Date From, Date To |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tabel menampilkan kolom Beginning/Period Movement/Ending Balance per akun, dengan baris Total di paling bawah. Baris Total inilah yang paling penting: total Debit harus sama dengan total Kredit untuk seluruh akun |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Tutup Periode & Tahun Fiskal — Modul Akuntansi

Bab manual: [`accounting/04-tutup-periode-dan-tahun-fiskal.md`](../../erpApiServices/docs/manualBook/accounting/04-tutup-periode-dan-tahun-fiskal.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menutup Periode Bulanan (draf) | Masuk ke `/client-master/accounting-period`, cari periode Januari 2023, klik menu ⋮ → Close Period → konfirmasi; Kolom Closed berubah jadi badge merah. | Tidak ada jurnal baru yang bisa diposting untuk periode Januari 2023, tetapi masih bisa dibuka lagi jika diperlukan koreksi. |
| Negatif — Menutup Periode Bulanan dengan Jurnal Draft Masih Ada (draf) | Masuk ke `/client-master/accounting-period`, cari periode Januari 2023 yang memiliki jurnal draft, klik menu ⋮ → Close Period; Sistem menolak dengan pesan "Ada jurnal belum posted, post atau hapus dulu." | Tidak ada perubahan pada status periode, tetap bisa memasukkan jurnal baru. |
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
| Positif — Neraca (Balance Sheet) berhasil diproses (draf) | Masuk ke `Reports → Balance Sheet`, isikan `As Of Date` 31 Desember 2023, klik **Run Report** | Laporan menampilkan Aset, Liabilitas, dan Ekuitas dengan total seimbang |
| Negatif — Neraca (Balance Sheet) tidak seimbang (draf) | Masuk ke `Reports → Balance Sheet`, isikan `As Of Date` 31 Desember 2023, klik **Run Report**, laporan menampilkan `is_balanced: false` | Laporan menunjukkan kesalahan kategori akun di Chart of Accounts, periksa ulang kategorisasi akun |
| Positif — Laba Rugi (Income Statement) ditampilkan (draf) | Masuk ke `Reports → Income Statement`, isikan `Start Date` 1 Januari 2023, `End Date` 31 Desember 2023, klik **Run Report** | Laporan menampilkan Pendapatan, Beban, dan Laba Bersih |
| Negatif — Laba Rugi (Income Statement) tidak ada transaksi (draf) | Masuk ke `Reports → Income Statement`, isikan `Start Date` 1 Januari 2023, `End Date` 31 Desember 2023, klik **Run Report** | Laporan menampilkan semua nilai 0, bukan pesan error |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Baru curigai konfigurasi Chart of Account Type — field Category, Normal Balance, dan Cash Flow Section per akun harus benar sejak awal setup |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Anggaran (Budget) — Modul Akuntansi

Bab manual: [`accounting/06-anggaran-budget.md`](../../erpApiServices/docs/manualBook/accounting/06-anggaran-budget.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | PT Sehat Sentosa Farma membuat anggaran untuk tahun 2027; memilih akun Beban Sewa, Unit Bisnis Kantor Pusat, periode Januari 2027 dengan jumlah Rp1.500.000; klik "Save Budget" | Anggaran disimpan dan status menjadi Draft |
| Negatif — input salah (draf) | PT Sehat Sentosa Farma mencoba membuat anggaran untuk periode yang sudah closed; memilih akun Beban Sewa, Unit Bisnis Kantor Pusat, periode Januari 2026 dengan jumlah Rp1.500.000; klik "Save Budget" | Sistem menolak dan memberikan pesan bahwa periode tidak aktif |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Isi Fiscal Year (wajib) dan Name (nama anggaran, misalnya "Anggaran Operasional 2027") |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Aset Tetap & Penyusutan — Modul Akuntansi

Bab manual: [`accounting/07-aset-tetap-dan-penyusutan.md`](../../erpApiServices/docs/manualBook/accounting/07-aset-tetap-dan-penyusutan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Pilih menu Aset; masukkan data aset baru (SKU OBT-001, Harga Perolehan 5.000.000, Masa Manfaat 60 bulan, Nilai Residu 500.000) | Aset baru ditambahkan dengan status pesan yang jelas dan jurnal penambahan aset muncul |
| Negatif — input salah (draf) | Menggunakan metode yang tidak sesuai (Saldo Menurun untuk aset yang sebaiknya menggunakan Garis Lurus) | Sistem menolak input pesan penolakan yang jelas |
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
| Positif — Setup Bank Account (draf) | Isi "Sehat Sentosa Farma" untuk Account Name; "BNI" untuk Bank Name; "1234567890" untuk Account Number; Rupiah untuk Currency; 10.000.000 untuk Opening Balance; dan hubungkan ke akun kas yang sesuai | Bank account Sehat Sentosa Farma dibuat dengan status Save berhasil |
| Negatif — Setup Bank Account (draf) | Tidak memilih Chart of Account sebelum klik Save | Muncul pesan penolakan yang jelas saat mencoba menyimpan bank account baru |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Rekonsiliasi bank adalah proses mencocokkan dua catatan yang seharusnya sama tapi seringkali beda karena beda waktu pencatatan: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Laporan Pajak PPN — Modul Akuntansi

Bab manual: [`accounting/09-laporan-pajak-ppn.md`](../../erpApiServices/docs/manualBook/accounting/09-laporan-pajak-ppn.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Buka Reports → Tax Summary; Isi Start Date 01-01-2023, End Date 31-12-2023; Klik Run Report | Menampilkan Total PPN Masukan, Total PPN Keluaran, dan Net Payable dengan nilai sesuai transaksi di perusahaan uji |
| Negatif — input salah (draf) | Buka Reports → Tax Summary; Isi Start Date 01-01-2023, End Date 30-06-2023; Klik Run Report | Menampilkan "No data" dan semua kartu total menunjukkan Rp 0 karena tidak ada transaksi berpajak dalam rentang tanggal yang dipilih |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Chart of Accounts — Tree View, Saldo Akun & Jenis Jurnal

Bab manual: [`accounting/10-chart-of-accounts.md`](../../erpApiServices/docs/manualBook/accounting/10-chart-of-accounts.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Buka halaman Chart of Accounts; klik ikon Tree View; filter pencarian "Kas & Bank"; cek indentasi sub-akun. | Tampilan berubah menjadi pohon akun dengan "Kas & Bankpesan yang jelasKas & Bank" berhasil. |
| Negatif — input salah (draf) | Buka halaman Chart of Accounts; coba klik ikon Tree View tanpa membuat akun terlebih dahulu; cek tampilan. | Sistem pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Syarat: asisten AI harus aktif dan pengungkapan AI cabang sudah dikonfirmasi. Pengguna yang boleh menambah akun otomatis boleh memakai bantuan ini. Aturan simpan tetap dicek server, misalnya laba ditahan hanya boleh satu per cabang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Diagram Alur Accounting — Modul Accounting

Bab manual: [`accounting/11-diagram-alur-accounting.md`](../../erpApiServices/docs/manualBook/accounting/11-diagram-alur-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Siklus Jurnal Manual (draf) | Input jurnal draft untuk Paracetamol 500 mg strip (SKU OBT-001) dengan tanggal dalam periode terbuka; Approve jika persyaratan ada; Post jurnal. | Jurnal draft berubah menjadi posted, saldo akun ter-update sesuai transaksi. |
| Negatif — Siklus Jurnal Manual (draf) | Input jurnal draft untuk Paracetamol 500 mg strip (SKU OBT-001) dengan tanggal di luar periode terbuka; Approve. | Sistem menolak input, pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jurnal yang belum seimbang tetap tersimpan sebagai Draft, tetapi tidak bisa di-Post |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tanggal jurnal harus berada di Accounting Period yang masih terbuka |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | B --/"Ya"/ C["Ditolak: jurnal sudah di-reverse"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | D --/"Ya, dan pembalikan penutup tidak diizinkan cabang"/ E["Ditolak"] |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
