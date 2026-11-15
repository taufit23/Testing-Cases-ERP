---
title: (PT Sehat Sentosa Farma) — 17. Proyek dan Tugas
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul proyek-dan-tugas untuk skenario PT Sehat Sentosa Farma. Proyek, tugas, waktu, change request dan integrasi.
visibility: internal
---

# 17. Proyek dan Tugas

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Tugas, papan, linimasa dan daftar; WIP limit; alur kerja per tipe tugas.
- Timesheet dan change request lewat persetujuan bila menyala; biaya tenaga kerja terjurnal bila saklarnya menyala.
- Tombol buat tugas dari dokumen (PO, SO, produksi, sewa) dan tautan ke dokumen.

## 1. Pengaturan Proyek, Tipe Tugas, Label, dan Peran — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/01-konfigurasi-dan-master.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/01-konfigurasi-dan-master.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengaturan Proyek (draf) | Setup proyek Sentosa Farma; aturan tugas dan proyek; tipe tugas; label; peran proyek; preset IT konsultan | Semua pengaturan berhasil, sistem memuat data dengan benar |
| Negatif — Input Tipe Tugas Salah (draf) | Menetapkan tipe tugas untuk produk Paracetamol 500 mg strip (SKU OBT-001) sebagai pesan yang jelas ketika seharusnya "resep" | Sistem menolak input dan memberikan pesan bahwa tipe tugas harus sesuai dengan jenis produk, yaitu "resep" untuk obat resep |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tipe yang masih dipakai tugas tidak bisa dihapus |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Proyek, Tugas, dan Tampilan — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/02-proyek-dan-tugas.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/02-proyek-dan-tugas.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Proyek (draf) | Buat proyek pesan yang jelas, tugas: pesan yang jelas, status: "Sedang Berjalan" | Sukses membuat proyek dengan tugas dan status sesuai harapan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dependensi (selesai-ke-mulai dan tiga jenis lain) mencegah atau memperingatkan sesuai pengaturan; siklus ditolak |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Catatan Waktu, Tarif, Penagihan, dan Alokasi — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/03-waktu-tarif-dan-penagihan.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/03-waktu-tarif-dan-penagihan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat Waktu (draf) | Input jam kerja karyawan; Approve oleh manajer | Data waktu disimpan dengan benar; Timer otomatis berhenti setelah persetujuan |
| Negatif — Tarif Tidak Ditemukan (draf) | Input nama layanan tanpa tarif; Coba submit | Form tidak valid: Tarif untuk layanan ini belum ditentukan; Tolong hubungi admin |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila persetujuan waktu diwajibkan: entri berstatus Draf → Ajukan → manajer proyek Setujui atau Tolak (alasan wajib). Entri yang sudah disetujui dapat dibuka kembali selama belum ditagih. Tugas yang punya catatan waktu tidak bisa dihapus |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Integrasi Git (GitHub dan GitLab) — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/04-integrasi-git.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/04-integrasi-git.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Integrasi Git (draf) | Hubungkan repositori GitHub/GitLab; konfigurasi webhook; commit teraut dengan tugas Sentosa Farma; pipeline otomatis; rilis otomatis | Integrasi berhasil; webhook berfungsi; tugas dan pipeline sesuai; rilis otomatis |
| Negatif — Tidak ada webhook (draf) | Commit dilakukan tanpa konfigurasi webhook; tidak teraut dengan tugas; pipeline tidak berjalan; rilis gagal | Integrasinya ditolak; perlu konfigurasi webhook untuk integrasi yang benar; pesan error jelas tentang kebutuhan webhook |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Otomasi, Webhook, Portal Klien, Change Request, dan Tiket — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/05-otomasi-portal-dan-tiket.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/05-otomasi-portal-dan-tiket.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Otomasi (draf) | Menjalankan aturan otomasi untuk pengiriman stok minimum; data uji: SKU OBT-001, threshold 50 unit | Sistem mengirim notifikasi ke gudang untuk restock dengan stok 48 unit tersisa |
| Negatif — Webhook keluar (draf) | Mengirim data pesanan yang salah; data uji: ID pesanan OBT-999, status "selesai" | Sistem menolak dan memberikan pesan bahwa ID pesanan tidak ditemukan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Perubahan status oleh aturan tetap melewati pemeriksaan status; bila ditolak, run tercatat Dilewati beserta alasannya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Laporan, Dasbor, LogBook, dan Asisten AI — Modul Proyek & Tugas

Bab manual: [`proyek-dan-tugas/06-laporan-logbook-dan-asisten-ai.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/06-laporan-logbook-dan-asisten-ai.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Direksi meminta laporan laba rugi bulanan; sistem menghasilkan laporan dengan detail keuangan dan visualisasi grafik | Laporan disajikan dengan benar dan lengkap sesuai permintaan |
| Negatif — input salah (draf) | Direksi meminta laporan yang tidak ada dalam sistem seperti laporan penjualan khusus obat resep; sistem menolak permintaan tersebut pesan penolakan yang jelas | Permintaan ditolak dengan alasan yang jelas karena laporan tidak ada dalam sistem |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Diagram Alur Proyek dan Tugas — Modul Proyek

Bab manual: [`proyek-dan-tugas/07-diagram-alur-proyek.md`](../../erpApiServices/docs/manualBook/proyek-dan-tugas/07-diagram-alur-proyek.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Alur Proyek (draf) | Menentukan tujuan proyek di klinik, merencanakan tugas dan timeline, melaksanakan tugas, mengevaluasi hasil, menutup proyek | Alur proyek terlihat jelas dengan langkah-langkah yang sesuai dan hasil evaluasi mencerminkan peningkatan kinerja klinik |
| Negatif — Status Tugas (draf) | Mengubah status tugas tanpa persetujuan manajer, menginput data waktu tidak valid | Perubahan ditolak karena syarat belum terpenuhi, pesan error muncul meminta persetujuan manajer atau memasukkan data waktu yang benar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | D --/"Tidak"/ X2["Ditolak: perpindahan tidak diizinkan"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | E --/"Tidak"/ X3["Ditolak dengan alasan<br/tombol dinonaktifkan dengan tooltip"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau Require Project Close Approval aktif, penyelesaian proyek harus melewati persetujuan penutupan dulu |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Tolak, alasan wajib |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
