---
title: (PT Medika Nusantara Sejahtera) — 17. Proyek dan Tugas
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul proyek-dan-tugas untuk skenario PT Medika Nusantara Sejahtera. Proyek, tugas, waktu, change request dan integrasi.
visibility: internal
---

# 17. Proyek dan Tugas

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji proyek dan tugas: papan kerja, jadwal, catatan waktu, dan penagihan proyek.
>
> **Kalau semuanya benar, artinya:** Pekerjaan terlacak dari tugas sampai tagihan, dan jam kerja yang dicatat bisa ditagihkan dengan benar.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Tugas, papan, linimasa dan daftar; WIP limit; alur kerja per tipe tugas.
- Timesheet dan change request lewat persetujuan bila menyala; biaya tenaga kerja terjurnal bila saklarnya menyala.
- Tombol buat tugas dari dokumen (PO, SO, produksi, sewa) dan tautan ke dokumen.

## 1. Pengaturan Proyek, Tipe Tugas, Label, dan Peran — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/01-konfigurasi-dan-master.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/01-konfigurasi-dan-master.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Setup proyek klinik Bekasi (draf) | Masuk ke `Proyek → Pengaturan Proyek`; atur akses penugasan, tugas baru selesai; masukkan pengingat 2 hari sebelum tenggat; simpan | Akses dan penugasan disetel, status tugas baru selesai sesuai aturan, pengingat dikirim 2 hari sebelum tenggat |
| Negatif — Menghapus tipe tugas Fitur (draf) | Masuk ke `Tipe Tugas`; coba hapus tipe tugas "Fitur" yang masih dipakai; coba simpan perubahan | Tidak bisa menghapus, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tipe yang masih dipakai tugas tidak bisa dihapus |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Proyek, Tugas, dan Tampilan — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/02-proyek-dan-tugas.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/02-proyek-dan-tugas.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat proyek baru (draf) | Pilih "Proyek → Proyek", isi nama proyek "Medika Nusantara-1", manajer "Budi", anggota "Andi, Budi, Caca", status "Rancangan"; klik "Simpan" | Proyek "Medika Nusantara-1pesan yang jelasRancangan" |
| Negatif — Mengubah status proyek tanpa persetujuan (draf) | Pilih proyek "ACME-1", klik tombol status, pilih "Selesai", bukan "Dikerjakan"; cek tombol "Simpan" | Tombol "Simpan" nonaktif pesan penolakan yang jelas |
| Positif — Menambah tugas ke proyek (draf) | Pilih "Proyek → Tugas", klik "Buat tugas", isi nama tugas "Pembelian Obat", penanggung jawab "Andi", tenggat "2023-10-15", label "Obat"; klik "Simpan" | Tugas "Pembelian Obatpesan yang jelasBelum mulai" |
| Negatif — Mengubah tugas tanpa checklist selesai (draf) | Pilih tugas "OBT-002", ubah status menjadi "Tinjau" tanpa menandai semua checklist; cek tombol "Simpan" | Tombol "Simpan" nonaktif pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dependensi (selesai-ke-mulai dan tiga jenis lain) mencegah atau memperingatkan sesuai pengaturan; siklus ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Catatan Waktu, Tarif, Penagihan, dan Alokasi — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/03-waktu-tarif-dan-penagihan.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/03-waktu-tarif-dan-penagihan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambahkan entri waktu (draf) | Masuk ke menu Catatan Waktu; klik tombol Timer; mulai timer untuk 2 jam; setujui entri dengan manajer proyek | Entri waktu ditambahkan, status menjadi Disetujui; muncul peringatan jika melebihi batas harian |
| Negatif — Menambahkan tarif tanpa persetujuan (draf) | Masuk ke menu Kartu Tarif; ubah tarif tanpa persetujuan; coba simpan | Tidak dapat disimpan, pesan penolakan yang jelas |
| Positif — Menagih milestone proyek (draf) | Masuk ke menu Keuangan Proyek; tag milestone sebagai siap ditagih; cek faktur draf | Faktur draf dibuat, status milestone menjadi Ditagih |
| Negatif — Menghapus faktur yang sudah diposting (draf) | Coba hapus faktur penjualan yang sudah diposting di proyek | Tidak dapat dihapus, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila persetujuan waktu diwajibkan: entri berstatus Draf → Ajukan → manajer proyek Setujui atau Tolak (alasan wajib). Entri yang sudah disetujui dapat dibuka kembali selama belum ditagih. Tugas yang punya catatan waktu tidak bisa dihapus |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Integrasi Git (GitHub dan GitLab) — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/04-integrasi-git.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/04-integrasi-git.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Aktifkan integrasi Git; tambah koneksi GitHub dengan URL webhook dan rahasia; daftar repositori `sentosa-farma/main-proyek` ke proyek; petakan username pengembang ke karyawan | Tugas dalam repositori terhubung otomatis ke tugas proyek, status tugas diperbarui sesuai peristiwa Git |
| Negatif — input salah (draf) | Mencoba menghubungkan repositori tanpa admin priviliege di GitHub; petakan username pengembang yang tidak ada di sistem | Tampilan pesan kesalahan tentang kebutuhan hak akses admin dan username yang valid di sistem |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Otomasi, Webhook, Portal Klien, Change Request, dan Tiket — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/05-otomasi-portal-dan-tiket.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/05-otomasi-portal-dan-tiket.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Aturan otomasi berjalan (draf) | Aktifkan aturan pada Pengaturan Proyek; buat tugas baru dengan pemicu "tugas dibuat"; tunggu 1 menit | Tugas otomatis berubah status sesuai aksi yang ditentukan, notifikasi dikirim ke pengguna yang dituju |
| Negatif — Aturan tidak berjalan (draf) | Matikan saklar otomasi pada Pengaturan Proyek; coba buat tugas baru dengan pemicu "tugas dibuat"; tunggu 1 menit | Aturan tidak berjalan, status tugas tetap sama, tidak ada notifikasi yang dikirim ke pengguna yang dituju |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Perubahan status oleh aturan tetap melewati pemeriksaan status; bila ditolak, run tercatat Dilewati beserta alasannya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Laporan, Dasbor, LogBook, dan Asisten AI — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/06-laporan-logbook-dan-asisten-ai.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/06-laporan-logbook-dan-asisten-ai.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Masuk ke Dasbor Proyek; pilih proyek Medika Nusantara; cek tugas terbuka | Menampilkan tugas terbuka dan terlambat, jumlah tugas, proyek berisiko, tiket melanggar SLA |
| Negatif — input salah (draf) | Coba ekspor laporan tanpa memilih rentang tanggal atau proyek | Pesan error: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Diagram Alur Proyek dan Tugas — Modul Proyek

Bab manual: [`proyek-dan-tugas/07-diagram-alur-proyek.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/07-diagram-alur-proyek.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mengubah status tugas dari Todo ke In Progress (draf) | Login sebagai Kepala Gudang; Pilih tugas OBT-001 Todo; Klik tombol "Mulai"; Masukkan tanggal mulai 2023-10-05 | Status tugas berubah menjadi In Progress, jurnal transaksi terbentuk, pesan konfirmasi muncul |
| Negatif — Menghapus status tugas tanpa alasan (draf) | Login sebagai Kepala Gudang; Pilih tugas OBT-001 Todo; Klik tombol "Hapus"; Tidak ada alasan penolakan | Muncul pesan peringatan meminta alasan penghapusan, tidak bisa menghapus tanpa alasan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | D --/"Tidak"/ X2["Ditolak: perpindahan tidak diizinkan"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | E --/"Tidak"/ X3["Ditolak dengan alasan<br/tombol dinonaktifkan dengan tooltip"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau Require Project Close Approval aktif, penyelesaian proyek harus melewati persetujuan penutupan dulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Tolak, alasan wajib |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
