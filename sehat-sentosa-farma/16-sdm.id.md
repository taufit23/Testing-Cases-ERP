---
title: (PT Sehat Sentosa Farma) — 16. SDM, Absensi, Payroll dan Rekrutmen
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul hrm untuk skenario PT Sehat Sentosa Farma. Karyawan, absensi, cuti, gaji, rekrutmen dan halaman karier.
visibility: internal
---

# 16. SDM, Absensi, Payroll dan Rekrutmen

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** **Maya Puspita** (Staf HR). Slip gaji dilihat karyawan sendiri di `My Payslips`.

**Cabang aktif:** Pusat untuk struktur dan payroll; Klinik Pratama & Laboratorium Bekasi untuk karyawan klinik.

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- Aturan absensi: toleransi, pulang cepat, lembur otomatis dengan persetujuan, konsekuensi gaji hanya bila dinyalakan.
- Payroll: PTKP wajib, slip hanya terlihat pemilik, periode berstatus draf lalu diproses, disetujui, dibayar.
- Rekrutmen: lowongan, lamaran, wawancara, penawaran; halaman karier publik, CV privat, persetujuan data pribadi.
- Cuti dan saldo cuti, kerahasiaan data karyawan, anonimisasi.

## 1. Konfigurasi HRM — Modul HRM

Bab manual: [`hrm/01-konfigurasi-hrm.md`](../../erpApiServices/docs/manualBook/hrm/01-konfigurasi-hrm.md)

**Input di:** `HRM → HRM Configs` (`/hrm/hrm-configs`) · `HRM → Employment Types` · `HRM → Shifts` · `HRM → Attendance Statuses`.

**Prasyarat:** akses admin HRM di branch yang aktif.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi Shift Kerja (draf) | Membuat shift 8 jam dengan nama "Shift Pagi" untuk karyawan di klinik | Shift "Shift Pagi" berhasil dibuat dan tersedia dalam sistem |
| Negatif — Input Shift Tidak Valid (draf) | Mencoba membuat shift dengan durasi negatif (-2) jam | Penolakan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kode tidak bisa diubah setelah tipe dibuat. Kalau salah ketik kode, buat tipe baru dan nonaktifkan yang lama |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Master data status yang bisa dipasang ke satu baris absensi karyawan, misalnya Hadir, Terlambat, Alpha, Sakit, Cuti, Libur. Wajib diatur sebelum menggunakan menu Attendances (chapter 05) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Struktur Organisasi — Modul HRM

Bab manual: [`hrm/02-struktur-organisasi.md`](../../erpApiServices/docs/manualBook/hrm/02-struktur-organisasi.md)

**Input di:** `HRM → Departments` (`/hrm/departments`) · `HRM → Positions` (`/hrm/positions`) · `HRM → Organization Structure` (`/hrm/organization-structure`).

**Prasyarat:** tidak ada, ini biasanya diisi paling awal sebelum menambah karyawan.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Struktur Organisasi (draf) | Menambah departemen "Kafe Sehat", menambah posisi kasir dan manajer kafe, mengimport struktur dari Excel | Struktur organisasi terupdate dengan departemen baru dan posisi yang ditambahkan |
| Negatif — Struktur Organisasi (draf) | Menghapus departemen utama pesan yang jelas tanpa konfirmasi ganda | Tindakan dibatalkan karena syarat penghapusan tidak terpenuhi, muncul pesan kesalahan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Departemen yang masih punya sub-departemen tidak bisa dihapus — tombol Delete akan menampilkan peringatan dan konfirmasi hapus tetap diblokir sampai seluruh sub-departemennya dipindahkan atau dihapus lebih dulu |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Data Karyawan — Modul HRM

Bab manual: [`hrm/03-data-karyawan.md`](../../erpApiServices/docs/manualBook/hrm/03-data-karyawan.md)

**Input di:** `HRM → Employees` (`/hrm/employees`) · `HRM → Employee Transfers` (`/hrm/employee-transfers`).

**Prasyarat:** Departemen dan Posisi sudah dibuat (chapter _02. Struktur Organisasi_) supaya bisa dipilih saat mengisi data karyawan.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah Karyawan (draf) | Tambah satu karyawan melalui form, isi detail lengkap; akun login otomatis dibuat; data tersimpan dengan benar | Proses tambah karyawan berhasil, akun login aktif dan dapat diakses oleh karyawan |
| Negatif — Import Data Excel (draf) | Mengimport file Excel tanpa kolom ID Karyawan; proses import gagal, muncul pesan kesalahan | Input salah, proses import ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Informasi Pribadi: Nama Depan (wajib), Nama Belakang, Jenis Kelamin, Tanggal Lahir, Tempat Lahir, NIK, NPWP, Email, No. HP, Alamat |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau pengaturan "Auto-create Login Account for New Employees" di HRM Configs (chapter 01) aktif, checkbox "Create a login account for this employee" pada form tambah karyawan akan tercentang secara default — hanya bisa dicentang kalau kolom Email sudah diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Klik Edit di halaman detail atau di menu titik tiga pada daftar karyawan. Catatan: karyawan dengan status selain Active (misalnya sudah resign/nonaktif) tidak bisa diedit lagi lewat menu ini — tombol Edit akan nonaktif dengan keterangan alasan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Isi Tanggal Efektif, Alasan (wajib), dan Catatan (opsional) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Rekrutmen — Modul HRM

Bab manual: [`hrm/04-rekrutmen.md`](../../erpApiServices/docs/manualBook/hrm/04-rekrutmen.md)

**Input di:** `HRM → Job Vacancies` (`/hrm/job-vacancies`) · `HRM → Applications` (`/hrm/applications`) · `HRM → Job Interviews` (`/hrm/job-interviews`) · `HRM → Job Offers` (`/hrm/job-offers`).

**Prasyarat:** Departemen dan Posisi sudah dibuat (chapter _02_).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuka Lowongan (draf) | Membuka lowongan dokter umum di klinik Bekasi; menerima lamaran dari 15 kandidat; menetapkan wawancara dengan 5 calon terbaik; membuat penawaran kerja kepada 2 kandidat yang disetujui | Proses rekrutmen berjalan lancar, mendapatkan 2 kandidat yang sesuai untuk posisi dokter umum |
| Negatif — Menerima Lamaran (draf) | Menerima lamaran tanpa lampiran; menolak pesan penolakan yang jelas | Lamaran tidak diproses, kandidat diberi informasi yang jelas tentang langkah selanjutnya untuk melengkapi aplikasi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Judul Lowongan (wajib), Departemen, Posisi, Tanggal Berakhir (opsional), Kualifikasi, dan Deskripsi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Absensi — Modul HRM

Bab manual: [`hrm/05-absensi.md`](../../erpApiServices/docs/manualBook/hrm/05-absensi.md)

**Input di:** `HRM → Attendances` (`/hrm/attendances`) · `HRM → Attendance Devices` · `HRM → Attendance Device Logs` · `HRM → Attendance Adjustments` · `HRM → My Attendance Adjustments` · `HRM → Attendance Recaps`.

**Prasyarat:** Attendance Statuses dan (kalau perlu jadwal kerja) Shifts/Work Schedules sudah diatur (chapter _01_).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Absensi Karyawan (draf) | Input absen karyawan menggunakan mesin absensi, check-in pukul 08:05 | Absen tercatat dengan benar pada sistem HRM |
| Negatif — Koreksi Absensi (draf) | Meminta koreksi absen tanpa approval manajer | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Simpan — sistem menampilkan Token perangkat satu kali saja (modal khusus, wajib disalin sebelum ditutup). Token ini yang dipasang di mesin/middleware sebagai kredensial pengiriman data |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Isi Alasan (wajib) dan Catatan tambahan (opsional) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Cuti (Leave) — Modul HRM

Bab manual: [`hrm/06-cuti.md`](../../erpApiServices/docs/manualBook/hrm/06-cuti.md)

**Input di:** sisi HR: `HRM → Leave Types` (`/hrm/leave-types`), `HRM → Leave Balances` (`/hrm/leave-balances`), `HRM → Leave Requests` (`/hrm/leave-requests`). Sisi karyawan (self-service): `HRM → My Leave Requests` (`/hrm/my-leave-requests`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Setup Jenis Cuti (draf) | Menambah cuti sakit, generate saldo otomatis untuk karyawan | Jenis cuti ditambahkan dan saldo otomatis tergenerikasi |
| Negatif — Mengajukan Cuti (draf) | Memasukkan tanggal cuti di luar kuota | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sebelum ada pengajuan cuti, HR wajib mendefinisikan dulu jenis-jenis cuti yang berlaku di perusahaan (misalnya Cuti Tahunan, Cuti Sakit, Cuti Melahirkan, dsb) lewat menu Leave Types |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 0 = tidak boleh mundur sama sekali (tanggal mulai harus hari ini atau ke depan) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jenis cuti yang sudah punya pengajuan cuti (Leave Requests) atau saldo (Leave Balances) tidak bisa dihapus — nonaktifkan saja lewat saklar Active kalau sudah tidak dipakai |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Baris saldo yang sudah pernah terpakai (Used Days lebih dari 0) tidak bisa dihapus — untuk menjaga riwayat pemakaian cuti tetap konsisten dengan pengajuan yang sudah disetujui |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Komponen Gaji — Modul HRM

Bab manual: [`hrm/07-komponen-gaji.md`](../../erpApiServices/docs/manualBook/hrm/07-komponen-gaji.md)

**Input di:** `HRM → Payroll → Salary Components` (`/hrm/salary-components`).

**Prasyarat:** tidak ada, tapi sebaiknya disiapkan sebelum mulai proses payroll pertama kali.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambahkan Tunjangan (draf) | Membuat komponen gaji "Transportasi" dengan jumlah Rp50.000; menyimpan | Komponen "Transportasi" ditambahkan ke daftar gaji dengan nilai sesuai |
| Negatif — Input Nilai Nol (draf) | Membuat komponen gaji "Unggun" dengan jumlah 0; menyimpan | Gagal, pesan penolakan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Referensi Pajak & BPJS — Modul HRM

Bab manual: [`hrm/08-referensi-pajak-dan-bpjs.md`](../../erpApiServices/docs/manualBook/hrm/08-referensi-pajak-dan-bpjs.md)

**Input di:** `HRM → Payroll → Payroll Tax Reference` (`/hrm/payroll-tax-reference`) dan `HRM → Payroll → BPJS Settings` (`/hrm/bpjs-settings`).

**Prasyarat:** tidak ada, tapi harus dicek/diisi sebelum proses payroll pertama supaya potongan pajak & BPJS karyawan terhitung benar.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengatur Referensi Pajak (draf) | Masukkan PTKP Rp50jt, TER 21%, PPh 21 5% untuk Jabatan Direktur | Referensi pajak teraplikasi dengan benar pada payroll Direktur |
| Negatif — Input PTKP Negatif (draf) | Menginputkan PTKP negatif -10jt | Sistem menolak inputan dan memberi pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: HRM → Payroll → Payroll Tax Reference (/hrm/payroll-tax-reference) dan HRM → Payroll → BPJS Settings (/hrm/bpjs-settings) · Prasyarat: tidak ada, tapi harus dicek/diisi sebelum proses payroll pertama supaya potongan pajak & BPJS karyawan terhitung benar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | BPJS Settings — tempat mengatur tarif iuran BPJS (yang bisa diedit), plus tampilan referensi saja (tidak bisa diedit dari sini) untuk tabel TER dan PTKP yang sama datanya dengan halaman Payroll Tax Reference |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau login sebagai user cabang biasa: hanya bisa mengisi kolom "Override untuk Cabang Ini" — nilai nasional tetap tampil sebagai referensi tapi tidak bisa diubah dari sini |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Sistem akan menampilkan pratinjau tiap baris — status valid (baris baru), updateexisting (akan menimpa data lama), duplicateinfile (ada baris kembar dalam file), atau invalid (ada kesalahan, tidak bisa dicentang) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Proses Payroll — Modul HRM

Bab manual: [`hrm/09-proses-payroll.md`](../../erpApiServices/docs/manualBook/hrm/09-proses-payroll.md)

**Input di:** `HRM → Payroll → Payroll Periods` (`/hrm/payroll-periods`) dan `HRM → Payroll → Payslips` (`/hrm/payslips`).

**Prasyarat:** Komponen Gaji dan Referensi Pajak/BPJS sudah diatur (lihat chapter sebelumnya); karyawan sudah punya data gaji di profil masing-masing.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | membuat periode gaji bulan ini untuk karyawan di klinik dan apotek; memproses perhitungan gaji; menyetujui; menandai sudah dibayar; menerbitkan slip gaji | proses payroll berjalan lancar, slip gaji terbit sesuai harapan |
| Negatif — input salah (draf) | mencoba membuat periode gaji di masa lalu tanpa alasan valid; input data karyawan tidak lengkap | permintaan ditolak pesan penolakan yang jelas dan pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Card "Period Summary" menampilkan total keseluruhan periode: Total Gross (total gaji kotor semua karyawan), Total Deductions (total potongan), Total Net (total gaji bersih yang harus dibayarkan), beserta tanggal Process dan tanggal Paid (kalau sudah ada) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sama seperti Payroll Period: dari daftar Payslips, tiap baris punya aksi Approve (hanya bisa dari status draft) dan Mark as Paid (hanya bisa dari status approved) lewat menu titik tiga. Payslip berstatus draft juga bisa dihapus kalau ternyata salah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Delete — hanya bisa selama status masih draft |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Slip Gaji Karyawan (My Payslips) — Modul HRM

Bab manual: [`hrm/10-slip-gaji-karyawan.md`](../../erpApiServices/docs/manualBook/hrm/10-slip-gaji-karyawan.md)

**Input di:** `HRM → My Payslips` (`/hrm/my-payslips`).

**Prasyarat:** slip gaji sudah diterbitkan HR dan berstatus **Approved** atau **Paid** (lihat chapter _09. Proses Payroll_).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Karyawan (draf) | Login My Payslips, pilih slip gaji Januari 2023, unduh sebagai PDF | Mendapatkan file PDF dari slip gaji Januari 2023 |
| Negatif — Karyawan (draf) | Memilih bulan yang tidak tersedia, misal Maret 2023 | Ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Halaman ini adalah menu self-service — setiap karyawan yang login bisa melihat sendiri daftar slip gajinya tanpa perlu izin khusus dari HR, tapi hanya bisa melihat slip gajinya sendiri, tidak bisa melihat slip gaji karyawan lain |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Mapping Jurnal Payroll — Modul HRM

Bab manual: [`hrm/11-mapping-jurnal-payroll.md`](../../erpApiServices/docs/manualBook/hrm/11-mapping-jurnal-payroll.md)

**Input di:** `HRM → Payroll → Payroll Journal Configuration` (`/hrm/payroll-journal-configuration`).

**Prasyarat:** Chart of Accounts (akun-akun akuntansi) sudah disiapkan di modul Accounting.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Mapping akun gaji dan potongan pajak untuk Sentosa Farma; input data payroll valid | Biaya gaji, potongan pajak, dan iuran BPJS otomatis tercatat ke jurnal yang tepat |
| Negatif — input salah (draf) | Input data payroll tidak valid; mapping akun salah | Sistem menolak proses dengan pesan kesalahan tentang akun yang harus di-map ulang |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tanpa pengaturan ini, tim finance harus mencatat jurnal biaya gaji secara manual setiap bulan. Dengan mapping yang benar, sistem bisa otomatis membuat jurnal akuntansi setiap kali: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Komisi Sales — Modul HRM

Bab manual: [`hrm/12-komisi-sales.md`](../../erpApiServices/docs/manualBook/hrm/12-komisi-sales.md)

**Input di:** `HRM → Commission Rules` (`/hrm/commission-rules`) dan `HRM → Commissions` (`/hrm/commissions`).

**Prasyarat:** Sales Invoice sudah berjalan normal, dan karyawan sales sudah terhubung sebagai salesperson di Sales Order/Invoice terkait.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Atur komisi sales (draf) | Masukkan aturan komisi untuk tim sales; terapkan pada transaksi penjualan; bayar komisi sesuai aturan | Komisi otomatis terbentuk dan dibayarkan sesuai aturan yang ditetapkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Setelah komisi memang sudah dibayarkan ke karyawan sales (biasanya digabung dengan gaji atau dibayar terpisah), klik menu titik tiga pada baris komisi tersebut lalu pilih "Mark as Paid" — hanya bisa dilakukan untuk komisi berstatus pending |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Perubahan Status Karyawan

Bab manual: [`hrm/15-perubahan-status-karyawan.md`](../../erpApiServices/docs/manualBook/hrm/15-perubahan-status-karyawan.md)

**Input di:** `HRM → Employee Status Changes` (`/hrm/employee-status-changes`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Menjalankan proses pengajuan perubahan status karyawan dari aktif ke nonaktif; memasukkan nama karyawan, tanggal mulai dan berakhir; menyetujui permohonan | Status karyawan diubah dengan benar, tercatat dalam daftar perubahan status karyawan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Pilih New Employment Type (wajib) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 4. Isi New Contract End Date. Wajib untuk tipe kepegawaian yang berkontrak; kalau kosong muncul pesan Contract end date is required for this employment type |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 6. Isi Reason (wajib) dan Notes |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 14. Log Aktivitas, Tipe Aktivitas, dan Kriteria KPI

Bab manual: [`hrm/16-log-aktivitas-tipe-aktivitas-dan-kpi.md`](../../erpApiServices/docs/manualBook/hrm/16-log-aktivitas-tipe-aktivitas-dan-kpi.md)

**Input di:** `HRM → Employee Activity Logs` (`/hrm/activity-logs`) · `Client Master → Activity Types` (`/client-master/activity-types`) · `Client Master → Kpi Criteria` (`/client-master/kpi-criteria`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Log Aktivitas (draf) | Menambah log aktivitas untuk kasir Bandung dengan tipe penjualan obat dan mencatat kriteria KPI penjualan tercapai 10% | Berhasil menambah log dengan detail yang lengkap |
| Negatif — Log Aktivitas (draf) | Menghapus semua log tanpa konfirmasi ulang | Tidak dapat menghapus log, muncul pesan kesalahan pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi Title (wajib), Occurred At (kapan terjadi), dan Description |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submit For Review mengirim log untuk ditinjau; hanya log berstatus draft yang bisa dikirim (tooltip menjelaskan bila tidak bisa) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Name (wajib; kalau kosong muncul Name is required), Code, dan Category |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi Name (wajib), Category, dan Description |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
