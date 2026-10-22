---
title: (PT Sehat Sentosa Farma) — 17. Proyek dan Tugas
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul proyek-dan-tugas untuk skenario PT Sehat Sentosa Farma. Proyek, tugas, waktu, change request dan integrasi.
visibility: internal
---

# 17. Proyek dan Tugas

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** Konfigurasi dan proyek oleh **Dr. Rahmat**; tugas dan catatan waktu oleh anggota proyek.

**Cabang aktif:** Klinik Pratama & Laboratorium Bekasi (proyek akreditasi).

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- Tugas, papan, linimasa dan daftar; WIP limit; alur kerja per tipe tugas.
- Timesheet dan change request lewat persetujuan bila menyala; biaya tenaga kerja terjurnal bila saklarnya menyala.
- Tombol buat tugas dari dokumen (PO, SO, produksi, sewa) dan tautan ke dokumen.

## 1. Pengaturan Proyek, Tipe Tugas, Label, dan Peran — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/01-konfigurasi-dan-master.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/01-konfigurasi-dan-master.md)

**Input di:** `Proyek → Pengaturan Proyek`, `Tipe Tugas`, `Label`, `Peran Proyek`.

**Prasyarat:** data karyawan sudah ada di modul HRM.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Setup awal modul Proyek & Tugas (draf) | Atur proyek "Sentosa Farma", tipe tugas "Apoteker", label "Jakarta" pada proyek pusat; konfirmasi berhasil | Konfigurasi proyek dan tugas sesuai, tidak ada pesan error |
| Negatif — Input data proyek salah (draf) | Masukkan nama proyek dengan karakter khusus "@"; pesan penolakan yang jelas | Pesan kesalahan jelas diberikan mengenai input yang salah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tipe yang masih dipakai tugas tidak bisa dihapus |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Proyek, Tugas, dan Tampilan — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/02-proyek-dan-tugas.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/02-proyek-dan-tugas.md)

**Input di:** `Proyek → Proyek`, `Tugas`, `Tugas Saya`, `Papan`, `Kalender`, `Linimasa`, `Beban Kerja`, `Template`, `Workflow`, `Field Kustom`.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Proyek (draf) | Buat proyek pesan yang jelas, tugas pesan yang jelas & "Negosiasi Harga" | Proyek dan tugas terdaftar dengan status "Belum Dimulai" |
| Negatif — Input Tanggal Mulai (draf) | Tanggal mulai diinput sebelum proyek dibuat | Tampilan error: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dependensi (selesai-ke-mulai dan tiga jenis lain) mencegah atau memperingatkan sesuai pengaturan; siklus ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Catatan Waktu, Tarif, Penagihan, dan Alokasi — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/03-waktu-tarif-dan-penagihan.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/03-waktu-tarif-dan-penagihan.md)

**Input di:** `Proyek → Catatan Waktu`, `Kartu Tarif`, `Peran Proyek`, `Alokasi Sumber Daya`; kartu **Keuangan Proyek** di halaman proyek..

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Mencatat jam kerja karyawan di Klinik Pratama & Laboratorium Bekasi; persetujuan Direktur untuk retainer dari pelanggan Klinik Harapan Sehat | Waktu dan retainer tercatat dengan benar, persetujuan Direktur valid |
| Negatif — input salah (draf) | Input biaya tanpa persetujuan Direktur; mencatat waktu tanpa keterangan kegiatan | Input ditolak: Persetujuan Direktur diperlukan; Waktu harus disertai keterangan kegiatannya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila persetujuan waktu diwajibkan: entri berstatus Draf → Ajukan → manajer proyek Setujui atau Tolak (alasan wajib). Entri yang sudah disetujui dapat dibuka kembali selama belum ditagih. Tugas yang punya catatan waktu tidak bisa dihapus |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Integrasi Git (GitHub dan GitLab) — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/04-integrasi-git.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/04-integrasi-git.md)

**Input di:** `Proyek → Git`, `Rilis`, dan `Pengaturan Proyek → Integrasi Git`.

**Prasyarat:** admin repositori di GitHub/GitLab; `APP_URL` server benar.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Integrasi Git (draf) | Hubungkan repositori GitHub/GitLab; konfigurasi webhook; commit baru di repo muncul di tugas Sentosa Farma; pipeline otomatis berjalan; rilis dikaitkan dengan tugas manajemen keuangan | Semua integrasi dan otomasi berfungsi sesuai harapan |
| Negatif — Integrasi Git (draf) | Webhook tidak konfigurasi; commit di repo tidak muncul di tugas; pipeline gagal; rilis tidak terkait tugas keuangan; pesan error pesan yang jelas | Integrasinya ditolak dengan pesan jelas bahwa webhook belum dikonfigurasikan dan perbaiki konfigurasi tersebut |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Otomasi, Webhook, Portal Klien, Change Request, dan Tiket — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/05-otomasi-portal-dan-tiket.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/05-otomasi-portal-dan-tiket.md)

**Input di:** `Proyek → Otomasi`, `Webhook`, `SLA`; kartu **Change Request** dan **Portal Klien** di halaman proyek..

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Otomasi (draf) | Menjalankan aturan otomasi untuk pengiriman notifikasi ke klinik dan apotek mitra setiap pagi | Notifikasi diterima dengan data yang tepat pada waktu yang ditentukan |
| Negatif — Webhook keluar (draf) | Mengirim data pesanan dari pabrik ke klinik tanpa format webhook yang benar | Penerimaan gagal, pesan kesalahan tentang format yang salah dijalankan oleh sistem |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Perubahan status oleh aturan tetap melewati pemeriksaan status; bila ditolak, run tercatat Dilewati beserta alasannya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Laporan, Dasbor, LogBook, dan Asisten AI — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/06-laporan-logbook-dan-asisten-ai.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/06-laporan-logbook-dan-asisten-ai.md)

**Input di:** `Proyek → Laporan Proyek`, `Dasbor Proyek`.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Laporan (draf) | Membuat laporan penjualan klinik Bekasi untuk Januari 2023; mengekspor ke Excel | Laporan berisi data penjualan, total omzet, dan grafik perbandingan bulanan dengan format Excel terlampir |
| Negatif — Dasbor (draf) | Mengakses dasbor tanpa login; mencoba melihat laporan klinik Bekasi | Ditolak: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
