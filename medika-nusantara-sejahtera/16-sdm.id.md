---
title: (PT Medika Nusantara Sejahtera) — 16. SDM, Absensi, Payroll dan Rekrutmen
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul hrm untuk skenario PT Medika Nusantara Sejahtera. Karyawan, absensi, cuti, gaji, rekrutmen dan halaman karier.
visibility: internal
---

# 16. SDM, Absensi, Payroll dan Rekrutmen

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji SDM: karyawan, absensi, cuti, gaji, pajak karyawan, dan pelanggaran.
>
> **Kalau semuanya benar, artinya:** Gaji dan potongan dihitung benar, data pribadi karyawan terlindungi, dan aturan disiplin berjalan adil.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Aturan absensi: toleransi, pulang cepat, lembur otomatis dengan persetujuan, konsekuensi gaji hanya bila dinyalakan.
- Payroll: PTKP wajib, slip hanya terlihat pemilik, periode berstatus draf lalu diproses, disetujui, dibayar.
- Rekrutmen: lowongan, lamaran, wawancara, penawaran; halaman karier publik, CV privat, persetujuan data pribadi.
- Cuti dan saldo cuti, kerahasiaan data karyawan, anonimisasi.

## 1. Konfigurasi HRM — Modul HRM

Bab manual: [`hrm/01-konfigurasi-hrm.md`](../../erpApiServices/docs/manualBook/hrm/01-konfigurasi-hrm.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengaturan umum HRM (draf) | Buka `HRM → HRM Configs`; Aktifkan `Require Leave Approval`; Klik Save | Status pengaturan berubah menjadi disetujui dan mengaktifkan proses approval cuti. |
| Negatif — Pengaturan geofence (draf) | Masuk area cakupan absensi yang tidak diizinkan; Cek-in tanpa lokasi pusat | Tampilan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kode tidak bisa diubah setelah tipe dibuat. Kalau salah ketik kode, buat tipe baru dan nonaktifkan yang lama |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Master data status yang bisa dipasang ke satu baris absensi karyawan, misalnya Hadir, Terlambat, Alpha, Sakit, Cuti, Libur. Wajib diatur sebelum menggunakan menu Attendances (chapter 05) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Struktur Organisasi — Modul HRM

Bab manual: [`hrm/02-struktur-organisasi.md`](../../erpApiServices/docs/manualBook/hrm/02-struktur-organisasi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Departemen (draf) | Klik "+ Add Department"; Isi Kode `HR-001`, Nama "Human Resources", Kosongkan Departemen Induk; Isi Deskripsi "Departemen HR untuk manajemen karyawan"; Save. | Tampilan konfirmasi penyimpanan dan muncul data baru di daftar departemen. |
| Negatif — Menghapus Departemen dengan Sub-Departemen (draf) | Klik tombol Delete pada Departemen "Operasional" yang memiliki sub-departemen; Perhatikan peringatan dan tidak dapat menghapus sampai sub-departemennya dipindahkan atau dihapus. | Tampilan peringatan pesan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Departemen yang masih punya sub-departemen tidak bisa dihapus — tombol Delete akan menampilkan peringatan dan konfirmasi hapus tetap diblokir sampai seluruh sub-departemennya dipindahkan atau dihapus lebih dulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Data Karyawan — Modul HRM

Bab manual: [`hrm/03-data-karyawan.md`](../../erpApiServices/docs/manualBook/hrm/03-data-karyawan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah satu karyawan baru (draf) | Klik "+ Add Employee"; Isi form dengan data lengkap (Nama Depan: Novi, Nama Belakang: Wijaya, Posisi: Apoteker, Departemen: Apotek Sentosa Bandung) dan klik Save; Konfirmasi di modal yang muncul. | Akun login otomatis dibuat; Detail karyawan terlihat di halaman daftar. |
| Negatif — Menambah karyawan tanpa email (draf) | Klik "+ Add Employee"; Isi form tanpa mengisi kolom Email, klik Save; Cek form untuk pesan kesalahan. | Form pesan penolakan yang jelas dan tidak membuat akun login. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Informasi Pribadi: Nama Depan (wajib), Nama Belakang, Jenis Kelamin, Tanggal Lahir, Tempat Lahir, NIK, NPWP, Email, No. HP, Alamat |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau pengaturan "Auto-create Login Account for New Employees" di HRM Configs (chapter 01) aktif, checkbox "Create a login account for this employee" pada form tambah karyawan akan tercentang secara default — hanya bisa dicentang kalau kolom Email sudah diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Klik Edit di halaman detail atau di menu titik tiga pada daftar karyawan. Catatan: karyawan dengan status selain Active (misalnya sudah resign/nonaktif) tidak bisa diedit lagi lewat menu ini — tombol Edit akan nonaktif dengan keterangan alasan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Isi Tanggal Efektif, Alasan (wajib), dan Catatan (opsional) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Rekrutmen — Modul HRM

Bab manual: [`hrm/04-rekrutmen.md`](../../erpApiServices/docs/manualBook/hrm/04-rekrutmen.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuka lowongan (draf) | HR klik "+ Create", masukkan "Apoteker" ke Judul Lowongan, Pilih Departemen "Apotek Sentosa Bandung", Tanggal Berakhir 30 Des 2023, Kualifikasi "S1 Farmasi", Deskripsi "Apoteker untuk Apotek Sentosa Bandung", centang Active | Lowongan berstatus Active dan otomatis diarahkan ke halaman detail lowongan |
| Negatif — Menjadwalkan wawancara tanpa input data (draf) | HR klik "Schedule Interview" tanpa mengisi Tanggal & Jam, Lokasi/Tautan | Muncul pesan error pesan yang jelas dan tidak bisa menyimpan jadwal wawancara |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Judul Lowongan (wajib), Departemen, Posisi, Tanggal Berakhir (opsional), Kualifikasi, dan Deskripsi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Absensi — Modul HRM

Bab manual: [`hrm/05-absensi.md`](../../erpApiServices/docs/manualBook/hrm/05-absensi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambahkan absensi karyawan (draf) | Klik "Check In" pada navbar; pilih karyawan; konfirmasi lokasi GPS; ambil foto kehadiran; simpan | Absensi ditambahkan dengan status "Hadir", jam masuk, dan foto terlampir |
| Negatif — Mengajukan koreksi absensi yang sudah terkunci (draf) | Pilih baris absensi karyawan; klik "Koreksi" (Attendance Adjustments); masukkan alasan; ajukan untuk approval | Muncul pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Simpan — sistem menampilkan Token perangkat satu kali saja (modal khusus, wajib disalin sebelum ditutup). Token ini yang dipasang di mesin/middleware sebagai kredensial pengiriman data |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Isi Alasan (wajib) dan Catatan tambahan (opsional) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Approved → tidak bisa dibatalkan; buat koreksi baru untuk membalikkannya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Cuti (Leave) — Modul HRM

Bab manual: [`hrm/06-cuti.md`](../../erpApiServices/docs/manualBook/hrm/06-cuti.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Jenis Cuti Tahunan (draf) | Buka HRM → Leave Types; klik "+ Add Leave Type"; masukkan Code `ANNUAL`, Leave Type Name "Cuti Tahunan", Quota Days 10, Is Paid checked, Requires Approval unchecked, Allow Half Day unchecked, Active checked; klik Save. | Jenis cuti "Cuti Tahunan" ditambahkan dengan saldo awal 10 hari untuk semua karyawan. |
| Negatif — Mengajukan Cuti Tanpa Jenis Cuti (draf) | Buka HRM → Leave Requests; pilih Employee, Choose Leave Type "Tidak Ditemukan", masukkan Start Date dan End Date; klik Submit. | Pengajuan cuti ditolak pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sebelum ada pengajuan cuti, HR wajib mendefinisikan dulu jenis-jenis cuti yang berlaku di perusahaan (misalnya Cuti Tahunan, Cuti Sakit, Cuti Melahirkan, dsb) lewat menu Leave Types |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 0 = tidak boleh mundur sama sekali (tanggal mulai harus hari ini atau ke depan) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Allow Half Day — kalau aktif, pengajuan jenis cuti ini boleh setengah hari (pagi atau sore). Tanggal mulai dan selesai harus sama. Kalau tidak aktif, pengajuan setengah hari ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Allow Leave By Hours — kalau aktif, pengajuan boleh per jam dengan jam mulai dan jam selesai. Tanggal mulai dan selesai harus sama, dan durasinya tidak boleh melebihi satu hari kerja. Kalau tidak aktif, pengajuan per jam ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Komponen Gaji — Modul HRM

Bab manual: [`hrm/07-komponen-gaji.md`](../../erpApiServices/docs/manualBook/hrm/07-komponen-gaji.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Buat komponen gaji "Tunjangan Makan" dengan tipe Earning, formula Fixed 50000, aktifkan Taxable dan BPJS Base, nonaktifkan Active; Klik Save | Komponen "Tunjangan Makan" ditambahkan ke daftar dengan status Aktif, nominal default 50000, kena pajak dan masuk dasar hitung BPJS |
| Negatif — input salah (draf) | Coba hapus komponen gaji yang pernah digunakan di slip gaji; Klik Delete | Muncul pesan penolakan yang jelas dan komponen tidak terhapus |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Referensi Pajak & BPJS — Modul HRM

Bab manual: [`hrm/08-referensi-pajak-dan-bpjs.md`](../../erpApiServices/docs/manualBook/hrm/08-referensi-pajak-dan-bpjs.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengatur PPh 21 untuk karyawan (draf) | Buka `/hrm/payroll-tax-reference`; pilih karyawan; ubah nilai PTKP, TER, PPh 21; simpan | Nilai pajak diperbarui otomatis saat proses payroll |
| Negatif — Menetapkan PTKP di bawah minimum (draf) | Buka `/hrm/payroll-tax-reference`; pilih karyawan; masukkan PTKP < Rp24 juta; coba simpan | Muncul pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: HRM → Payroll → Payroll Tax Reference (/hrm/payroll-tax-reference) dan HRM → Payroll → BPJS Settings (/hrm/bpjs-settings) · Prasyarat: tidak ada, tapi harus dicek/diisi sebelum proses payroll pertama supaya potongan pajak & BPJS karyawan terhitung benar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | BPJS Settings — tempat mengatur tarif iuran BPJS (yang bisa diedit), plus tampilan referensi saja (tidak bisa diedit dari sini) untuk tabel TER dan PTKP yang sama datanya dengan halaman Payroll Tax Reference |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau login sebagai user cabang biasa: hanya bisa mengisi kolom "Override untuk Cabang Ini" — nilai nasional tetap tampil sebagai referensi tapi tidak bisa diubah dari sini |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Sistem akan menampilkan pratinjau tiap baris — status valid (baris baru), updateexisting (akan menimpa data lama), duplicateinfile (ada baris kembar dalam file), atau invalid (ada kesalahan, tidak bisa dicentang) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Proses Payroll — Modul HRM

Bab manual: [`hrm/09-proses-payroll.md`](../../erpApiServices/docs/manualBook/hrm/09-proses-payroll.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat periode payroll bulan ini (draf) | Klik "Generate This Month's Period" pada halaman Payroll Periods; status menjadi processing | Status Payroll Period berubah menjadi processing, tabel Payroll Items kosong |
| Negatif — Menyetujui periode tanpa proses (draf) | Coba klik Approve pada periode dengan status draft; muncul pesan "Perhitungan gaji belum dilakukan" | Tidak ada perubahan pada status Payroll Period dan tidak ada jurnal yang dibuat |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Process ditolak bila ada karyawan aktif tanpa status PTKP (sistem menampilkan daftar namanya), dan memberi peringatan untuk karyawan yang tidak ikut dihitung karena statusnya bukan status aktif bawaan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Card "Period Summary" menampilkan total keseluruhan periode: Total Gross (total gaji kotor semua karyawan), Total Deductions (total potongan), Total Net (total gaji bersih yang harus dibayarkan), beserta tanggal Process dan tanggal Paid (kalau sudah ada) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sama seperti Payroll Period: dari daftar Payslips, tiap baris punya aksi Approve (hanya bisa dari status draft) dan Mark as Paid (hanya bisa dari status approved) lewat menu titik tiga. Payslip berstatus draft juga bisa dihapus kalau ternyata salah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Delete — hanya bisa selama status masih draft |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Slip Gaji Karyawan (My Payslips) — Modul HRM

Bab manual: [`hrm/10-slip-gaji-karyawan.md`](../../erpApiServices/docs/manualBook/hrm/10-slip-gaji-karyawan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Karyawan Medika Nusantara (draf) | Login ke My Payslips; klik nomor slip gaji OBT-001 periode Januari 2023 | Detail slip gaji muncul dengan ringkasan, earnings, deductions dan tombol "Download PDF" aktif |
| Negatif — Karyawan Medika Nusantara (draf) | Coba download PDF tanpa generate slip gaji HR dulu | Tombol "Download PDF" tidak aktif dan muncul pesan untuk menghubungi HR tentang status payroll |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Halaman ini adalah menu self-service — setiap karyawan yang login bisa melihat sendiri daftar slip gajinya tanpa perlu izin khusus dari HR, tapi hanya bisa melihat slip gajinya sendiri, tidak bisa melihat slip gaji karyawan lain |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Mapping Jurnal Payroll — Modul HRM

Bab manual: [`hrm/11-mapping-jurnal-payroll.md`](../../erpApiServices/docs/manualBook/hrm/11-mapping-jurnal-payroll.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Pilih "Auto" pada Journal Mode; klik "Save Configuration"; masukkan akun untuk Salary Expense, Salary Payable, Pph21 Payable, Bpjs Payable, Other Deductions Payable, Cash Bank; klik "Save Configuration". | Konfigurasi berhasil disimpan dan jurnal payroll otomatis akan dibuat sesuai dengan mapping yang diberikan. |
| Negatif — input salah (draf) | Tidak mengaktifkan Chart of Accounts sebelum melakukan konfigurasi; coba simpan. | Sistem menolak konfigurasi karena Chart of Accounts belum terdefinisi, pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tanpa pengaturan ini, tim finance harus mencatat jurnal biaya gaji secara manual setiap bulan. Dengan mapping yang benar, sistem bisa otomatis membuat jurnal akuntansi setiap kali: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Komisi Sales — Modul HRM

Bab manual: [`hrm/12-komisi-sales.md`](../../erpApiServices/docs/manualBook/hrm/12-komisi-sales.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Aturan komisi sales berhasil dibuat (draf) | HRM → Commission Rules; "+ Add"; Name: "Komisi Retail 2%"; Rule Type: Percentage; Basis: Revenue; Rate: 2%; Active: checked; Create | Aturan komisi pesan yang jelas muncul di daftar dengan status active, ready untuk menghitung komisi otomatis |
| Negatif — Komisi tidak terbentuk karena invoice tanpa salesperson (draf) | HRM → Sales Invoice; Approve invoice tanpa salesperson; Cek Commission Rules dan Commissions | Pesan error pesan yang jelas muncul, dan tidak ada entri komisi baru di halaman Commission |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setelah komisi memang sudah dibayarkan ke karyawan sales (biasanya digabung dengan gaji atau dibayar terpisah), klik menu titik tiga pada baris komisi tersebut lalu pilih "Mark as Paid" — hanya bisa dilakukan untuk komisi berstatus pending |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Perubahan Status Karyawan

Bab manual: [`hrm/15-perubahan-status-karyawan.md`](../../erpApiServices/docs/manualBook/hrm/15-perubahan-status-karyawan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengajukan perubahan status karyawan (draf) | Klik New Status Change; Pilih Apoteker Penanggung Jawab; Pilih Kontrak tetap; Isi 31 Des 2023; Centang Adjust Salary; Isi Reason dan Notes; Klik Submit | Perubahan status diteruskan untuk persetujuan, Current Employment Type berubah menjadi Kontrak tetap, New Contract End Date ditetapkan, Salary Adjustment dilakukan jika dipilih. |
| Negatif — Mengajukan perubahan status tanpa menentukan tipe kontrak baru (draf) | Klik New Status Change; Pilih Apoteker Penanggung Jawab; Tidak memilih New Employment Type; Coba Submit | Muncul pesan penolakan yang jelas dan permintaan tidak dapat disubmit. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Pilih New Employment Type (wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Isi New Contract End Date. Wajib untuk tipe kepegawaian yang berkontrak; kalau kosong muncul pesan Contract end date is required for this employment type |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 6. Isi Reason (wajib) dan Notes |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Satu karyawan hanya boleh punya satu perubahan status yang masih berjalan pada satu waktu. Pengajuan baru ditolak sampai yang berjalan selesai atau dibatalkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 14. Log Aktivitas, Tipe Aktivitas, dan Kriteria KPI

Bab manual: [`hrm/16-log-aktivitas-tipe-aktivitas-dan-kpi.md`](../../erpApiServices/docs/manualBook/hrm/16-log-aktivitas-tipe-aktivitas-dan-kpi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Jenis Aktivitas (draf) | Klik Create; Isi Name: Pelatihan Internal; Code: INTL; Category: Pendidikan; Active In Catalog: checked; Klik Create | Tampilan berhasil menambah jenis aktivitas Pelatihan Internal dengan status active |
| Negatif — Menghapus Kriteria KPI (draf) | Centang baris KPI Criteria, klik Bulk Actions, pilih Delete; Konfirmasi hapus | Muncul pesan penolakan yang jelas karena tidak ada baris tercentang; Tidak menghapus kriteria apapun |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi Title (wajib), Occurred At (kapan terjadi), dan Description |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submit For Review mengirim log untuk ditinjau; hanya log berstatus draft yang bisa dikirim (tooltip menjelaskan bila tidak bisa) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Name (wajib; kalau kosong muncul Name is required), Code, dan Category |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Name (wajib), Category, dan Description |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 15. Konfigurasi Pelanggaran dan Sanksi Karyawan

Bab manual: [`hrm/17-konfigurasi-pelanggaran.md`](../../erpApiServices/docs/manualBook/hrm/17-konfigurasi-pelanggaran.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi mode eskalasi berdasarkan jumlah pelanggaran (draf) | Buka HRM → Violation Configs; pilih Mode eskalasi Jumlah; atur batas 3 pelanggaran; klik Simpan | Pengaturan tersimpan, sanksi ditentukan otomatis jika mencapai 3 pelanggaran |
| Negatif — Menyalakan potongan gaji tanpa konfirmasi dasar tertulis (draf) | Buka HRM → Violation Configs; nyalakan Potong gaji karena sanksi; klik Simpan tanpa centang Konfirmasi dasar tertulis | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Potongan gaji karena sanksi tidak bisa dinyalakan sebelum dasar tertulis dikonfirmasi: pengguna harus mencentang bahwa potongan memiliki dasar tertulis dalam perjanjian kerja atau peraturan perusahaan. Tanpa konfirmasi itu, penyimpanan ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Potongan dibatasi persen maksimum dari gaji kotor. Agent tidak boleh menyebut angka batas tertentu; angkanya diisi perusahaan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 16. Master Pelanggaran dan Sanksi Karyawan

Bab manual: [`hrm/18-master-pelanggaran-dan-sanksi.md`](../../erpApiServices/docs/manualBook/hrm/18-master-pelanggaran-dan-sanksi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah jenis pelanggaran (draf) | Buka `HRM → Violation Types`; tambah "Pelanggaran Keuangan" dengan kode VTF, nama "Kekecewaan Kas", kategori "Integritas", poin 50, dapat dibanding, wajib sidang, rahasia tidak | Jenis pelanggaran "Kekecewaan Kas" muncul di form pelaporan |
| Negatif — Tidak memilih cakupan pelapor (draf) | Buka `HRM → Violation Reporting Scopes`; pilih jabatan "Apoteker", tetapi tidak memilih cakupan dan peringkat keparahan maksimum | Muncul pesan galat pesan yang jelas saat menyimpan form |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tingkat sanksi punya mode denda: tanpa, nominal tetap, persen gaji pokok, upah per hari; juga hari skorsing, tanda pemutusan hubungan kerja, dan wajib surat |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Buka HRM → Violation Severities; tambah atau pilih dari katalog: kode, nama, peringkat, poin bawaan, wajib sidang, rahasia, warna |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Buka Sanction Levels; isi kode, nama, peringkat, masa berlaku (bulan), mode denda dan jumlahnya, hari skorsing, wajib surat, dan tanda pemutusan hubungan kerja |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Buka Violation Types; isi kode, nama, kategori, poin, dapat dibanding, wajib sidang, rahasia, keparahan, sanksi bawaan, masa kedaluwarsa (bulan), dan sumber deteksi otomatis bila ada |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 17. Melaporkan Pelanggaran, Banding, dan Sidang

Bab manual: [`hrm/19-melaporkan-pelanggaran-banding-dan-sidang.md`](../../erpApiServices/docs/manualBook/hrm/19-melaporkan-pelanggaran-banding-dan-sidang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Melaporkan pelanggaran (draf) | Buka HRM → Employee Violations; pilih Karyawan: Apoteker Penanggung Jawab; Jenis Pelanggaran: Tidak Hadir Tanpa Alasan; Tanggal: 2023-10-05; Uraian: Tidak hadir tanpa izin; Ajukan ke karyawan | Draf pelanggaran masuk daftar, status Draft |
| Negatif — Melaporkan pelanggaran (draf) | Pilih Karyawan: Apoteker Penanggung Jawab; Jenis Pelanggaran: tidak ada; Tanggal: 2023-10-05; Uraian: Tidak hadir tanpa izin; Ajukan ke karyawan | Pesan galat: Jenis pelanggaran wajib diisi, status tetap draf |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jenis pelanggaran dapat dibanding: karyawan diberi jendela banding beberapa hari; jenis tidak dapat dibanding: pelanggaran langsung ke persetujuan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Banding hanya mungkin selama pelanggaran sedang ditinjau. Banding diterima: pelanggaran gugur. Banding ditolak: pelanggaran tetap berlaku |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Selesaikan persetujuan bila diwajibkan (Lihat Persetujuan) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Pada pelanggaran yang dibanding pilih Banding diterima atau Banding ditolak dengan catatan wajib |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 18. Menjatuhkan Sanksi Karyawan

Bab manual: [`hrm/20-sanksi-karyawan.md`](../../erpApiServices/docs/manualBook/hrm/20-sanksi-karyawan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menjatuhkan sanksi (draf) | Buka HRM → Employee Sanctions; Pilih karyawan Medika Nusantara, tingkat sanksi, tanggal terbit, pelanggaran OBT-001; Simpan, Terbitkan; Unduh surat sanksi | Sanksi tampil di daftar, surat sanksi bisa diunduh |
| Negatif — Menjatuhkan sanksi tanpa persetujuan (draf) | Buka HRM → Employee Sanctions; Pilih karyawan Medika Nusantara, tingkat sanksi, tanggal terbit, pelanggaran OBT-001; Simpan, coba Terbitkan tanpa persetujuan; Terbitkan setelah disetujui | Muncul pesan penolakan yang jelas bila tidak disetujui |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila persetujuan sanksi diwajibkan di konfigurasi, sanksi diajukan dulu dan menunggu persetujuan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Surat sanksi hanya bisa diunduh setelah sanksi diterbitkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Klik Ajukan bila persetujuan diwajibkan dan tunggu disetujui; selainnya langsung Terbitkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 6. Bila sanksi harus ditarik, klik Cabut. Untuk rekomendasi pemutusan hubungan kerja, klik Buat Perubahan Status Karyawan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 19. Mesin Absensi (Fingerprint dan Wajah)

Bab manual: [`hrm/21-mesin-absensi.md`](../../erpApiServices/docs/manualBook/hrm/21-mesin-absensi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendaftarkan mesin absensi Medika Nusantara (draf) | Buka HRM → Attendance Devices; tambah perangkat; isikan nama "Medika Nusantara"; vendor "Fingerprint & Wajah"; nomor seri "SF001"; zona waktu "Asia/Jakarta"; jalur ID karyawan "employee_id"; jalur waktu "timestamp"; format waktu "YYYY-MM-DD HH:MM:SS"; peta arah "{direction: 'in'}", tempel payload valid; uji pemetaan; simpan | Mesin Medika Nusantara muncul dengan nama dan terakhir terlihat; absen cocok masuk di catatan, absen belum cocok 0 |
| Negatif — Token tidak disalin saat putar token (draf) | Buka HRM → Attendance Devices; sentuh "Putar Token"; klik konfirmasi; alamat push dan token baru ditampilkan; tidak salin token; kirim kiriman mesin | Muncul pesan galat pesan yang jelas dan token lama masih berlaku; absen belum cocok bertambah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Memutar token membuat token lama langsung berhenti berlaku. Mesin harus dikonfigurasi ulang dengan token baru |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jangan menebak jalur field untuk merek tertentu; jalurnya harus diambil dari contoh data nyata mesin |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 20. Halaman Karier Publik dan Absensi Saya

Bab manual: [`hrm/22-halaman-karier-dan-absensi-saya.md`](../../erpApiServices/docs/manualBook/hrm/22-halaman-karier-dan-absensi-saya.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menampilkan halaman karier publik (draf) | Buka HRM → Career Pages; nyalakan status online; masukkan alamat halaman; isi profil perusahaan; pilih tampil departemen; isikan teks persetujuan bahasa Indonesia dan Inggris; simpan | Halaman karier tampil publik berisi lowongan dan profil |
| Negatif — Status offline tetapi diakses (draf) | Buka HRM → Career Pages; tidak nyalakan status online; coba akses halaman karier | Pesan galat: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Teks persetujuan per bahasa wajib dicentang pelamar sebelum mengirim; teks yang disetujui disimpan bersama lamaran. Bila kosong, kata-kata bawaan dipakai |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 21. Diagram Alur HRM — Modul HRM

Bab manual: [`hrm/23-diagram-alur-hrm.md`](../../erpApiServices/docs/manualBook/hrm/23-diagram-alur-hrm.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Alur HRM dari awal sampai akhir (draf) | 1. Masuk ke menu Rekrutmen; 2. Pilih status lamaran Hired; 3. Klik Approve pada proses payroll; 4. Cek slip gaji karyawan yang terapprove | Status lamaran berubah menjadi Hired, proses payroll diteruskan dan slip gaji dibuat |
| Negatif — Alur HRM dari awal sampai akhir (draf) | 1. Masuk ke menu Rekrutmen; 2. Pilih status lamaran Rejected; 3. Coba Approve pada proses payroll tanpa melakukan persetujuan rekrutmen terlebih dahulu | Sistem menolak dan memberikan pesan bahwa harus melakukan persetujuan rekrutmen terlebih dahulu sebelum dapat mengapprove payroll |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Process ditolak kalau ada karyawan aktif yang belum punya status PTKP. Sistem menampilkan daftar namanya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau persetujuan payroll aktif tetapi belum ada alur persetujuannya, Approve ditolak. Atur alurnya dulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau pembayaran memakai transfer bank, Mark As Paid ditolak dan gaji dibayar lewat batch transfer: Prepare dan Release (diagram 5) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 22. KPI Karyawan: Rencana, Hasil, dan Tinjauan — Modul HRM

Bab manual: [`hrm/24-kpi-karyawan-rencana-hasil-dan-tinjauan.md`](../../erpApiServices/docs/manualBook/hrm/24-kpi-karyawan-rencana-hasil-dan-tinjauan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Meninjau hasil karyawan (draf) | Buka "KPI Results", pilih Karyawan A periode Januari, klik Review; beri nilai 80 pada kriteria tinjauan, isi catatan "Perlu peningkatan komunikasi"; klik Finalize. | Status hasil menjadi Reviewed dan Final, dengan catatan tinjauan diarsipkan. |
| Negatif — Meninjau hasil tanpa penugasan (draf) | Buka "KPI Results", pilih Karyawan A periode Januari, klik Review; beri nilai 80 pada kriteria tinjauan, isi catatan "Perlu peningkatan komunikasi". | Sistem menolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | KPI harus dinyalakan di KPI Settings cabang. Bila belum menyala, perhitungan ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bawaan cabang adalah mode bayangan: hasil dihitung tanpa skor resmi dan tidak punya alur tinjauan. Hasil bayangan tidak bisa ditinjau, difinalkan, atau diakui. Matikan mode bayangan setelah data dianggap layak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Rencana KPI per jabatan punya tiga kelompok: kinerja, kompetensi, dan perilaku. Bobot ketiga kelompok harus berjumlah 100, dan bobot baris di tiap kelompok juga berjumlah 100 |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bobot indikator kinerja tidak boleh melebihi batas bobot yang diatur cabang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 23. KPI: Kompetensi, Jenjang Karier, Promosi, Sasaran, 360, dan Pengembangan — Modul HRM

Bab manual: [`hrm/25-kpi-kompetensi-karier-promosi-dan-pengembangan.md`](../../erpApiServices/docs/manualBook/hrm/25-kpi-kompetensi-karier-promosi-dan-pengembangan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menilai kompetensi karyawan (draf) | Buka KPI Competencies; Buat master kompetensi Laravel, SQL, desain API; Di KPI Competency Matrix, atasan menilai tingkat kompetensi karyawan dengan hasil 3 untuk Laravel dan 4 untuk SQL | Tampilan matriks kompetensi berubah, menunjukkan penilaian baru |
| Negatif — Menilai kompetensi tanpa login HR (draf) | Buka KPI Competencies; Buat master kompetensi Laravel, SQL, desain API; Tanpa login sebagai HR, coba di KPI Competency Matrix menilai tingkat kompetensi karyawan dengan hasil 3 untuk Laravel dan 4 untuk SQL | Muncul pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Umpan balik 360 dinyalakan per cabang. Bila belum menyala, permintaan ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Di KPI Promotion Recommendations, HR klik Approved atau Rejected. Rekomendasi yang sudah diputuskan tidak bisa diputuskan lagi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
