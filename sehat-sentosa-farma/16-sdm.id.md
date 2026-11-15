---
title: (PT Sehat Sentosa Farma) — 16. SDM, Absensi, Payroll dan Rekrutmen
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul hrm untuk skenario PT Sehat Sentosa Farma. Karyawan, absensi, cuti, gaji, rekrutmen dan halaman karier.
visibility: internal
---

# 16. SDM, Absensi, Payroll dan Rekrutmen

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
| Positif — Konfigurasi Shift Kerja (draf) | Membuat shift 8-16 di klinik dan 9-17 di apotek | Shift berhasil dibuat dengan jadwal yang tepat |
| Negatif — Input Jam Kerja Salah (draf) | Membuat shift 24-32 di klinik | Ditolak: Jam kerja harus dalam rentang 0-23 |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kode tidak bisa diubah setelah tipe dibuat. Kalau salah ketik kode, buat tipe baru dan nonaktifkan yang lama |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Master data status yang bisa dipasang ke satu baris absensi karyawan, misalnya Hadir, Terlambat, Alpha, Sakit, Cuti, Libur. Wajib diatur sebelum menggunakan menu Attendances (chapter 05) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Struktur Organisasi — Modul HRM

Bab manual: [`hrm/02-struktur-organisasi.md`](../../erpApiServices/docs/manualBook/hrm/02-struktur-organisasi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Departemen (draf) | Tambah departemen "Kepatuhan" dengan posisi pesan yang jelas, gaji Rp 15.000.000, role "Manager" | Berhasil menambah departemen dan posisi, bagan struktur organisasi diperbarui |
| Negatif — Menghapus Departemen (draf) | Menghapus departemen "Kepatuhan" tanpa konfirmasi | Tidak dapat menghapus, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Departemen yang masih punya sub-departemen tidak bisa dihapus — tombol Delete akan menampilkan peringatan dan konfirmasi hapus tetap diblokir sampai seluruh sub-departemennya dipindahkan atau dihapus lebih dulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Data Karyawan — Modul HRM

Bab manual: [`hrm/03-data-karyawan.md`](../../erpApiServices/docs/manualBook/hrm/03-data-karyawan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Karyawan (draf) | Tambah satu karyawan (Form Lengkap) dengan detail lengkap; Akun login otomatis dibuat; Detail gaji dan struktur terlihat | Berhasil ditambahkan, akun login aktif, detail gaji sesuai input |
| Negatif — Input Data Salah (draf) | Menambah karyawan dengan data salah; Tidak valid; Ditolak pesan penolakan yang jelas | Input ditolak, perbaiki data dan coba lagi |
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
| Positif — Membuka Lowongan (draf) | Membuka lowongan pekerjaan apoteker di kantor pusat Jakarta | Lowongan berhasil dibuat dan diterbitkan |
| Negatif — Input Data Pribadi (draf) | Mengisi nama lamaran dengan angka 1234567890 | Lamaran ditolak: input nama tidak valid, masukkan nama lengkap yang benar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Judul Lowongan (wajib), Departemen, Posisi, Tanggal Berakhir (opsional), Kualifikasi, dan Deskripsi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Absensi — Modul HRM

Bab manual: [`hrm/05-absensi.md`](../../erpApiServices/docs/manualBook/hrm/05-absensi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Absensi Karyawan (draf) | Input absen karyawan menggunakan mesin absensi di klinik Bekasi | Absen tercatat dengan benar dan tersedia dalam rekap payroll |
| Negatif — Koreksi Absensi (draf) | Mengajukan koreksi tanpa approval HR | Tidak dapat mengajukan koreksi, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Simpan — sistem menampilkan Token perangkat satu kali saja (modal khusus, wajib disalin sebelum ditutup). Token ini yang dipasang di mesin/middleware sebagai kredensial pengiriman data |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Isi Alasan (wajib) dan Catatan tambahan (opsional) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Approved → tidak bisa dibatalkan; buat koreksi baru untuk membalikkannya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Cuti (Leave) — Modul HRM

Bab manual: [`hrm/06-cuti.md`](../../erpApiServices/docs/manualBook/hrm/06-cuti.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Jenis Cuti (draf) | HR menambah jenis cuti Tahun Baru dengan kuota 5 hari untuk karyawan | Sukses menambahkan jenis cuti baru |
| Negatif — Mengajukan Cuti Tanpa Saldo (draf) | Karyawan mengajukan cuti 10 hari padahal saldo hanya 3 hari | Ditolak: saldo tidak mencukupi, maksimal 3 hari |
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
| Positif — Menambahkan Tunjangan (draf) | Membuat komponen gaji 'transportasi' dengan jumlah 50 ribu; menyimpan | Tunjangan transportasi ditambahkan ke daftar komponen gaji |
| Negatif — Menghapus Gaji Pokok (draf) | Menghapus komponen 'gaji pokok'; tidak dapat dihapus karena syarat mutlak | Tidak bisa menghapus, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Referensi Pajak & BPJS — Modul HRM

Bab manual: [`hrm/08-referensi-pajak-dan-bpjs.md`](../../erpApiServices/docs/manualBook/hrm/08-referensi-pajak-dan-bpjs.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengatur PPh 21 (draf) | Input PTKP, TER, dan tarif PPh 21 untuk karyawan | Referensi pajak disetel dengan benar |
| Negatif — Input tarif PPh 21 salah (draf) | Menyertakan persentase yang tidak valid | Tidak berhasil: pesan penolakan yang jelas |
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
| Positif — Proses Payroll Bulanan (draf) | Membuka periode bulan ini, memproses gaji karyawan, menyetujui dan membayar, terbitnya slip gaji resmi | Proses payroll berjalan lancar, slip gaji diterbitkan dengan benar |
| Negatif — Periode sudah dibayar (draf) | Mencoba menandai periode yang telah dibayar sebagai dibayar kembali | Tidak dapat disetujui, sistem menolak karena periode tersebut sudah dibayarkan |
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
| Positif — Karyawan (draf) | Login My Payslips, pilih slip gaji Januari 2023, unduh sebagai PDF | Mendapatkan file PDF lengkap dengan detail slip gaji Januari 2023 |
| Negatif — Karyawan (draf) | Memilih bulan yang tidak tersedia, misal Februari 2023 | Ditolak: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Halaman ini adalah menu self-service — setiap karyawan yang login bisa melihat sendiri daftar slip gajinya tanpa perlu izin khusus dari HR, tapi hanya bisa melihat slip gajinya sendiri, tidak bisa melihat slip gaji karyawan lain |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Mapping Jurnal Payroll — Modul HRM

Bab manual: [`hrm/11-mapping-jurnal-payroll.md`](../../erpApiServices/docs/manualBook/hrm/11-mapping-jurnal-payroll.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Mapping akun gaji untuk Sentosa Farma, termasuk potongan pajak dan iuran BPJS; proses payroll otomatis tercatat ke jurnal yang tepat | Biaya gaji, potongan pajak, dan iuran BPJS tercatat secara otomatis ke jurnal yang sesuai dalam sistem akuntansi |
| Negatif — input salah (draf) | Input akun gaji tidak valid untuk Sentosa Farma; proses payroll ditolak | Pemetaan akun gagal, sistem menampilkan pesan kesalahan tentang akun gaji yang tidak valid dan perlu diperbaiki sebelum proses payroll dapat dilanjutkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tanpa pengaturan ini, tim finance harus mencatat jurnal biaya gaji secara manual setiap bulan. Dengan mapping yang benar, sistem bisa otomatis membuat jurnal akuntansi setiap kali: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Komisi Sales — Modul HRM

Bab manual: [`hrm/12-komisi-sales.md`](../../erpApiServices/docs/manualBook/hrm/12-komisi-sales.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Atur komisi sales (draf) | Masukkan aturan komisi untuk produk Paracetamol 500 mg strip (SKU OBT-001) dengan persentase 2% | Aturan komisi ditambahkan dan terlihat di sistem |
| Negatif — Input produk tidak ditemukan (draf) | Coba masukkan komisi untuk produk yang tidak ada, seperti SKU OBT-999 | Sistem menolak input dan memberikan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setelah komisi memang sudah dibayarkan ke karyawan sales (biasanya digabung dengan gaji atau dibayar terpisah), klik menu titik tiga pada baris komisi tersebut lalu pilih "Mark as Paid" — hanya bisa dilakukan untuk komisi berstatus pending |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Perubahan Status Karyawan

Bab manual: [`hrm/15-perubahan-status-karyawan.md`](../../erpApiServices/docs/manualBook/hrm/15-perubahan-status-karyawan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Perubahan status karyawan (draf) | Masa percobaan di konfirmasi, kontrak diperpanjang, tipe kepegawaian berubah, riwayat karier tercatat dengan benar | Proses perubahan status selesai, notifikasi dikirimkan kepada pihak yang berkepentingan |
| Negatif — Syarat tidak terpenuhi (draf) | Input data tidak lengkap, syarat perubahan status tidak dipenuhi, permintaan ditolak dengan alasan jelas | Permintaan perubahan status ditolak, notifikasi kesalahan dikirimkan kepada pengaju permohonan |
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
| Positif — Menambah Jenis Aktivitas (draf) | Tambah "Pembelian Obatpesan yang jelasSimpanpesan yang jelasTipe aktivitas berhasil ditambahkan." | Tampilan Activity Types berisi "Pembelian Obat". |
| Negatif — Menghapus Kriteria Tanpa Memilih (draf) | Klik "Hapuspesan yang jelasSilakan pilih kriteria terlebih dahulu." | Tidak menghapus kriteria apa pun. |
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
| Positif — Konfigurasi pelanggaran (draf) | Konfigurasi cabang Bandung; persetujuan Kepala Gudang; notifikasi ke General Affairs; sanksi potongan gaji 10% | Sukses konfigurasi dengan notifikasi dan persetujuan sesuai |
| Negatif — Input data salah (draf) | Menginput nama karyawan yang tidak ada di sistem; mengeset sanksi tanpa persetujuan | Gagal konfigurasi, muncul pesan galat pesan yang jelas dan pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Potongan gaji karena sanksi tidak bisa dinyalakan sebelum dasar tertulis dikonfirmasi: pengguna harus mencentang bahwa potongan memiliki dasar tertulis dalam perjanjian kerja atau peraturan perusahaan. Tanpa konfirmasi itu, penyimpanan ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Potongan dibatasi persen maksimum dari gaji kotor. Agent tidak boleh menyebut angka batas tertentu; angkanya diisi perusahaan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 16. Master Pelanggaran dan Sanksi Karyawan

Bab manual: [`hrm/18-master-pelanggaran-dan-sanksi.md`](../../erpApiServices/docs/manualBook/hrm/18-master-pelanggaran-dan-sanksi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menyiapkan pelanggaran "sakit palsu", tingkat keparahan ringan, sanksi penurunan gaji 10%, eskalasi HR, pelapor Kepala Gudang; cakupan otomatis | Input valid, sanksi teraplikasikan dan notifikasi HR & Kepala Gudang |
| Negatif — input salah (draf) | Menyiapkan pelanggaran tanpa tingkat keparahan; input tidak lengkap | Tolakan pesan penolakan yang jelas dan fokus pada field tersebut |
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
| Positif — Melaporkan Pelanggaran (draf) | Karyawan melaporkan pelanggaran, manajer keuangan memvalidasi, karyawan menandatangani banding, sidang ditutup oleh direktur | Proses pelaporan dan penyelesaian pelanggaran selesai dengan baik |
| Negatif — Data Karyawan Salah (draf) | Input data karyawan tidak valid, sistem menolak laporan dan memberikan pesan kesalahan | Laporan ditolak karena data karyawan salah, meminta input ulang data yang benar |
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
| Positif — Menjatuhkan Sanksi Karyawan (draf) | Karyawan pelanggaran disetujui, sanksi diterbitkan, surat sanksi diunduh, rekomendasi pemutusan hubungan kerja ditindaklanjuti | Sanksi tercatat, surat sanksi ada, tindak lanjut rekomendasi jelas |
| Negatif — Input Data Salah (draf) | Data karyawan tidak lengkap, sanksi tidak diterbitkan, surat sanksi tidak diunduh, tindak lanjut rekomendasi tidak dilakukan | Sanksi gagal tercatat, pesan galat data harus lengkap, perbaiki data sebelum melanjutkan |
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
| Positif — Mendaftar Absensi (draf) | Mendaftarkan mesin absensi Sentosa Farma, memetakan format data, memutar token, dan memantau absen yang cocok | Absen karyawan tercatat dengan benar di aplikasi HRM |
| Negatif — Input Wajah Salah (draf) | Menginput wajah karyawan yang tidak terdaftar, mencoba login | Sistem menolak akses pesan penolakan yang jelas dan meminta input ulang data valid |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Memutar token membuat token lama langsung berhenti berlaku. Mesin harus dikonfigurasi ulang dengan token baru |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jangan menebak jalur field untuk merek tertentu; jalurnya harus diambil dari contoh data nyata mesin |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 20. Halaman Karier Publik dan Absensi Saya

Bab manual: [`hrm/22-halaman-karier-dan-absensi-saya.md`](../../erpApiServices/docs/manualBook/hrm/22-halaman-karier-dan-absensi-saya.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Kunjungi Halaman Karier Publik; Persetujuan pelamar terdaftar; Cek Absensi Saya; Kehadiran pribadi tercatat | Lowongan dilihat dan persetujuan valid; Rekap kehadiran pribadi ditampilkan dengan benar |
| Negatif — input salah (draf) | Masuk sebagai tamu; Pilih lowongan tanpa melamar; Input data absen salah | Akses ditolak; Lowongan harus dilamar terlebih dahulu; Data absen tidak valid, perbaiki input sebelum mengajukan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Teks persetujuan per bahasa wajib dicentang pelamar sebelum mengirim; teks yang disetujui disimpan bersama lamaran. Bila kosong, kata-kata bawaan dipakai |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 21. Diagram Alur HRM — Modul HRM

Bab manual: [`hrm/23-diagram-alur-hrm.md`](../../erpApiServices/docs/manualBook/hrm/23-diagram-alur-hrm.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Karyawan baru di rekrutmen, proses cuti disetujui, payroll periode terbayar dengan benar, kinerja KPI memenuhi target | Alur HRM berjalan lancar, data payroll akurat, karyawan puas dengan pengalaman kerja |
| Negatif — input salah (draf) | Input data absensi salah, karyawan tidak memenuhi target KPI, cuti ditolak karena syarat tidak terpenuhi | Proses HRM terhambat, payroll tidak tepat waktu, kinerja karyawan turun, karyawan tidak puas dengan manajemen |
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
| Positif — jalur normal (draf) | Direksi menyiapkan rencana KPI untuk Manajer Keuangan, dihitung dan divalidasi oleh atasan, karyawan mengakui hasilnya | Skor akhir diterima, tidak ada keberatan dari karyawan |
| Negatif — input salah (draf) | Manajer Keuangan menolak hasil yang diberikan tanpa alasan, direksi meminta klarifikasi dan koreksi jika perlu | Rencana KPI harus diulangi sesuai prosedur hingga diterima karyawan |
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
| Positif — Input karyawan baru (draf) | Masukkan kompetensi, jenjang karier, sasaran, catatan pelatihan, umpan balik 360, dan rencana pengembangan untuk karyawan baru Sentosa Farma | KPI lengkap dengan data valid ditambahkan ke sistem tanpa perubahan gaji atau jabatan |
| Negatif — Input jenjang karier kosong (draf) | Menyisipkan data karyawan tanpa mengisi jenjang karier | Penambahan data gagal: jenjang karier wajib diisi sebelum disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Umpan balik 360 dinyalakan per cabang. Bila belum menyala, permintaan ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Di KPI Promotion Recommendations, HR klik Approved atau Rejected. Rekomendasi yang sudah diputuskan tidak bisa diputuskan lagi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
