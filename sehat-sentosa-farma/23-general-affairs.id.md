---
title: (PT Sehat Sentosa Farma) — 23. General Affairs
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul general-affairs untuk skenario PT Sehat Sentosa Farma. Barang dan unit, permintaan, pengadaan, perawatan, ganti rugi dan bebas tanggungan.
visibility: internal
---

# 23. General Affairs

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Permintaan barang lewat persetujuan; stok keluar dan kapitalisasi mengikuti jatah dan kategori.
- Penyelesaian ganti rugi dari pelanggaran karyawan tertaut ke HRM; bebas tanggungan memeriksa semua kewajiban.
- Pengadaan GA menautkan PR dan PO; unit GA dapat tertaut aset tetap.

## 1. Konfigurasi General Affairs

Bab manual: [`general-affairs/01-konfigurasi-general-affairs.md`](../../erpApiServices/docs/manualBook/general-affairs/01-konfigurasi-general-affairs.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi GA untuk Klinik Pratama (draf) | Buka `General Affairs → Configs`; pilih mode pengadaan `Purchase Request`; pilih gudang; nyalakan jurnal akuntansi dengan akun persediaan 12345, biaya 67890, dan lawan 11223; klik **Simpan Konfigurasi** | Pesan sukses muncul; halaman memuat ulang konfigurasi GA Klinik Pratama |
| Negatif — Mode pengadaan tanpa Purchasing diaktifkan (draf) | Buka `General Affairs → Configs`; pilih mode pengadaan `Blanket Agreement`; coba klik **Simpan Konfigurasi** | Muncul pesan penolakan yang jelas; konfigurasi GA tidak disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mode pengadaan Purchase Request dan Blanket Agreement terkunci (tidak bisa dipilih) bila cabang belum memakai modul Purchasing. Mode Manual selalu bisa dipilih |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penjadwal berjalan di server. Bila tidak ada tanda aktif dalam dua hari, halaman menampilkan peringatan; pengguna biasa tidak dapat memperbaikinya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Barang dan Unit General Affairs

Bab manual: [`general-affairs/02-barang-dan-unit.md`](../../erpApiServices/docs/manualBook/general-affairs/02-barang-dan-unit.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendaftarkan unit obat (draf) | Buka `/ga/units`; pilih Paracetamol 500 mg strip (SKU OBT-001), isi jumlah 10, tag otomatis; klik Simpan | Unit Paracetamol 500 mg strip muncul di daftar Units dengan status Available dan pemegang kosong |
| Negatif — Mendaftarkan unit tanpa stok (draf) | Buka `/ga/units`; pilih Paracetamol 500 mg strip (SKU OBT-001), isi jumlah 20, tag kosong; klik Simpan | Muncul pesan penolakan yang jelas dan tidak ada unit yang terdaftar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jenis barang ada empat dan tidak bisa dikarang: habis pakai, serah-terima, inventaris pegawai (custody), fasilitas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Nama, kode SKU, dan satuan wajib diisi pada Item |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Unit yang masih dipegang pegawai tidak boleh dianggap bebas; pemegang saat ini ditampilkan di daftar dan detail unit |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Atur perilaku: dipakai bersama, wajib dikembalikan, dilacak masa berlakunya |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Jatah, Aturan Kapitalisasi, dan Kategori Kesalahan General Affairs

Bab manual: [`general-affairs/03-jatah-kapitalisasi-dan-kategori-kesalahan.md`](../../erpApiServices/docs/manualBook/general-affairs/03-jatah-kapitalisasi-dan-kategori-kesalahan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menetapkan jatah stok untuk pegawai (draf) | Buka /ga/quotas; tambah; pilih Paracetamol 500 mg strip (SKU OBT-001); berlaku untuk Pegawai; masukkan kuantitas 200; periode Bulanan; simpan | Jatah stok Paracetamol 500 mg strip (SKU OBT-001) ditetapkan untuk pegawai dengan batas 200 per bulan |
| Negatif — Menggunakan nama kategori kesalahan yang sudah ada di cabang (draf) | Buka /ga/fault-categories; tambah; masukkan nama "Kehilangan"; persentase beban pegawai 50%; tandai wajib dokumen; simpan | Muncul pesan galat pesan yang jelas dan input tidak disimpan, tetapkan nama lain untuk kategori kesalahan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jatah dicek saat permintaan diajukan dan saat pengeluaran diposting. Hasilnya bergantung pada mode Penegakan jatah di Configs: Mati tidak mengecek, Peringatan memberi tahu dan tetap melanjutkan, Blokir menolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Nama kategori kesalahan harus unik per cabang; nama kembar ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi nama, persentase beban pegawai, dan tandai wajib dokumen bila bukti harus dilampirkan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Kebijakan Penyelesaian Ganti Rugi General Affairs

Bab manual: [`general-affairs/04-kebijakan-ganti-rugi.md`](../../erpApiServices/docs/manualBook/general-affairs/04-kebijakan-ganti-rugi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menambah kebijakan ganti rugi (draf) | Buka General Affairs → Settlement Policies; Tambah; Nama: Kebijakan A; Jenis penyelesaian: Kehilangan; Cara penyelesaian: Bayar nominal; Metode harga: Nominal tetap; Nominal tetap: 100000; Simpan | Kebijakan "Kebijakan A" muncul di daftar dan bisa dipilih saat membuat kasus penyelesaian. |
| Negatif — Menambah kebijakan tanpa nama (draf) | Buka General Affairs → Settlement Policies; Tambah; Nama: kosong; Jenis penyelesaian: Kehilangan; Cara penyelesaian: Bayar nominal; Metode harga: Nominal tetap; Nominal tetap: 100000; Simpan | Muncul pesan penolakan yang jelas dan tidak ada kebijakan baru yang muncul di daftar. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Metode nominal tetap wajib mengisi jumlah. Metode persentase menurut umur wajib memiliki minimal satu rentang umur (bulan dari–sampai). Metode berbasis persentase wajib mengisi persentase |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jangan menyatakan potong gaji selalu sah; pasti ada catatan hukum yang harus dibaca pengguna di layar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 5. Atur pembayaran: izinkan potong gaji (dan batas persen), izinkan cicilan (dan jumlah maksimum), wajib pengakuan pegawai, dan masa tenggang (hari) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Penerimaan Barang General Affairs

Bab manual: [`general-affairs/05-penerimaan-barang.md`](../../erpApiServices/docs/manualBook/general-affairs/05-penerimaan-barang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Penerimaan barang dengan saldo awal (draf) | Buka `/ga/receipts`; tambah draf; pilih `Saldo Awal` untuk Paracetamol 500 mg strip, isi kuantitas 100 dan biaya per unit 15000; simpan sebagai draf; konfirmasi terima barang; ganti status menjadi 'Terima' | Stok Paracetamol 500 mg strip di gudang GA bertambah 100, jurnal terbentuk sesuai pemetaan akun |
| Negatif — Penerimaan tanpa saldo awal untuk barang baru (draf) | Buka `/ga/receipts`; tambah draf; pilih Paracetamol 500 mg strip, isi kuantitas 100 dan biaya per unit 15000; simpan sebagai draf; coba konfirmasi terima barang | Pesan galat: pesan yang jelas |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Permintaan Barang dan Pengeluaran ke Pegawai

Bab manual: [`general-affairs/06-permintaan-dan-pengeluaran-barang.md`](../../erpApiServices/docs/manualBook/general-affairs/06-permintaan-dan-pengeluaran-barang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pegawai meminta barang (draf) | Pegawai Jakarta meminta 50 strip Paracetamol 500 mg (SKU OBT-001) untuk klinik Bekasi; diajukan, disetujui, dan dikeluarkan ke Klinik Pratama | Stok gudang GA berkurang, pegawai Klinik Pratama tercatat sebagai pemegang barang bernomor tag, jumlah 50 strip Paracetamol 500 mg muncul di permintaan |
| Negatif — Jatah melebihi batas (draf) | Pegawai Jakarta meminta 100 strip Paracetamol 500 mg (SKU OBT-001) untuk klinik Bekasi; diajukan, tetapi disetop karena jatah terlampaui di mode penegakan | Muncul pesan penolakan yang jelas; permintaan tidak bisa dikeluarkan ke gudang GA |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | My Requests hanya tersedia bila saklar Pegawai boleh meminta sendiri menyala; bila mati, halaman menyatakan pegawai tidak bisa meminta barang di cabang ini |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hanya permintaan draf yang boleh diedit atau diajukan. Permintaan yang sudah berlanjut tidak bisa dibatalkan lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jangan mengeluarkan barang tanpa pegawai penerima; penerima wajib diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Isi tanggal dibutuhkan dan tujuan, tambah barang beserta jumlah (harus lebih dari nol), dan catatan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Pengembalian Barang General Affairs

Bab manual: [`general-affairs/07-pengembalian-barang.md`](../../erpApiServices/docs/manualBook/general-affairs/07-pengembalian-barang.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengembalian barang dengan kondisi baik (draf) | General Affairs → Returns; Pilih pengeluaran OBT-001; Isi jumlah 50, Tanggal pengembalian 2023-10-01, Kondisi baik; Simpan, Terima Pengembalian, Konfirmasi | Riwayat pemegang unit mencatat tanggal kembali 2023-10-01 dan kondisi baik; Stok gudang OBT-001 bertambah 50 |
| Negatif — Jumlah lebih besar dari yang masih dipegang pegawai (draf) | General Affairs → Returns; Pilih pengeluaran OBT-001; Isi jumlah 60, Tanggal pengembalian 2023-10-01, Kondisi baik; Simpan | Pesan galat: Jumlah lebih besar dari yang masih dipegang pegawai; Status tetap draf dan stok gudang tidak berubah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jumlah yang dikembalikan tidak boleh melebihi yang masih dipegang pegawai. Bila tidak ada sisa, layar menyatakan tidak ada yang bisa dikembalikan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kondisi tiap barang wajib dipilih: baik, rusak, atau hilang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Pemesanan Unit Bersama General Affairs

Bab manual: [`general-affairs/08-pemesanan-unit-bersama.md`](../../erpApiServices/docs/manualBook/general-affairs/08-pemesanan-unit-bersama.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pemesanan unit proyektor untuk klinik (draf) | Buka General Affairs → Bookings; pilih proyektor; awal 10:00, akhir 12:00; tujuan Klinik Pratama; pegawai Kepala Gudang; Simpan; Check-out saat mengambil; Check-in saat kembali; pegawai Kepala Gudang | Pemesanan tampil di daftar dengan status "Check-in"; check-out dan check-in tercatat pada waktunya |
| Negatif — Waktu akhir sebelum awal (draf) | Buka General Affairs → Bookings; pilih proyektor; awal 10:00, akhir 9:00; tujuan Klinik Pratama; pegawai Kepala Gudang; Simpan | Muncul pesan penolakan yang jelas; pemesanan tidak tersimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Waktu selesai harus setelah waktu mulai. Bila tidak, pemesanan ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Unit dengan rencana perawatan yang memblokir pemakaian saat terlambat tidak boleh dipakai selama perawatannya terlambat |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Perawatan Unit dan Masa Berlaku General Affairs

Bab manual: [`general-affairs/09-perawatan-dan-masa-berlaku.md`](../../erpApiServices/docs/manualBook/general-affairs/09-perawatan-dan-masa-berlaku.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat rencana perawatan (draf) | Buka `General Affairs → Maintenance Plans`; tambah nama "Perawatan Alat Kesehatan", pilih unit "Kantor Pusat & Distribusi Jakarta", jenis "inspeksi", interval 30 hari, jatuh tempo berikutnya 15 Des 2023, penanggung jawab "Kepala Gudang", blokir pemakaian bila terlambat; simpan | Rencana perawatan muncul dengan status jatuh tempo 15 Des 2023 |
| Negatif — Input interval kurang dari satu hari (draf) | Buka `General Affairs → Maintenance Plans`; tambah nama "Perawatan Alat Kesehatan", pilih unit, jenis, interval 0 hari; coba simpan | Muncul pesan penolakan yang jelas dan tidak bisa disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Rencana perawatan terikat pada satu unit. Nama wajib diisi, interval minimal satu hari, dan jatuh tempo berikutnya wajib diisi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Opsi blokir pemakaian bila terlambat membuat unit yang lewat jatuh tempo tidak bisa dipesan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Pengadaan Barang Kantor dan Program Kegiatan General Affairs

Bab manual: [`general-affairs/10-pengadaan-dan-program-kegiatan.md`](../../erpApiServices/docs/manualBook/general-affairs/10-pengadaan-dan-program-kegiatan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat permintaan pengadaan baru (draf) | Buka `General Affairs → Procurement Requests`; klik **Buat Permintaan Baru**; masukkan barang Paracetamol 500 mg strip, jumlah 100, tanggal dibutuhkan 2023-10-01; klik **Ajukan**; permintaan berubah menjadi Purchase Request | Purchase Request untuk Paracetamol 500 mg strip 100 di Purchasing |
| Negatif — Membuat permintaan pengadaan tanpa persetujuan (draf) | Buka `General Affairs → Procurement Requests`; klik **Buat Permintaan Baru**; masukkan barang Paracetamol 500 mg strip, jumlah 100; coba klik **Ajukan**; muncul pesan "Hanya permintaan pengadaan yang disetujui yang bisa menjadi Purchase Request" | Tidak bisa mengajukan permintaan tanpa persetujuan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Permintaan pengadaan berstatus draf; hanya draf yang boleh diedit atau diajukan. Setelah diproses, permintaan tidak bisa dibatalkan lagi |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Mode pengadaan yang membutuhkan Purchasing ditolak bila cabang tidak memakainya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Buka detail, klik Ajukan (bila persetujuan diwajibkan, tunggu disetujui; lewat tombol Buka Persetujuan) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Item permintaan yang dirilis dari perjanjian harus bagian dari perjanjian yang dipilih |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 11. Penyelesaian Ganti Rugi Barang General Affairs

Bab manual: [`general-affairs/11-penyelesaian-ganti-rugi.md`](../../erpApiServices/docs/manualBook/general-affairs/11-penyelesaian-ganti-rugi.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Kasus ganti rugi obat oleh pegawai (draf) | Buka `General Affairs → Settlements`; pilih pegawai, unit Alkohol Swab (ALK-002), kebijakan, kategori kesalahan, nilai taksiran; ajukan persetujuan; pegawai mengakui; atur pembayaran tunai 3 kali dengan uang muka 100.000, jatuh tempo pertama 1 Januari 2024; catat pembayaran; tutup kasus | Jadwal pembayaran terbentuk dan jumlah dibayar bertambah tiap pembayaran. Kasus berstatus tertutup saat lunas. |
| Negatif — Tidak ada persetujuan untuk draf kasus (draf) | Buka `General Affairs → Settlements`; pilih pegawai, unit Alkohol Swab (ALK-002), kebijakan, kategori kesalahan, nilai taksiran; coba atur pembayaran tanpa ajukan persetujuan | Muncul pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Urutan wajib: draf → ajukan persetujuan (bila diwajibkan) → pegawai mengakui → atur pembayaran → catat pembayaran → ditutup |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Bila kebijakan mewajibkan pengakuan, pegawai harus mengakui lebih dulu sebelum pembayaran diatur. Tombol Mengakui tidak bisa diulang |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jumlah cicilan tidak boleh melebihi maksimum kebijakan. Jadwal pembayaran hanya bisa diatur sekali |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Cicilan potong gaji dibayar oleh proses payroll; tidak boleh dicatat manual. Pembayaran tunai dicatat manual, tidak boleh melebihi sisa terutang |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 12. Bebas Tanggungan dan Laporan General Affairs

Bab manual: [`general-affairs/12-bebas-tanggungan-dan-laporan.md`](../../erpApiServices/docs/manualBook/general-affairs/12-bebas-tanggungan-dan-laporan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Pengecekan bebas tanggungan pegawai (draf) | Buka `/ga/clearances`; pilih Kepala Gudang; cek status | Menampilkan "bebas" atau daftar penghalang beserta rinciannya |
| Negatif — Pengecekan tanpa menjalankan pengecekan di layar (draf) | Buka `/ga/clearances` tanpa memilih pegawai; klik "Cek"; pilih Kepala Gudang | Menampilkan pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hasil pengecekan terlihat segera. Bila mode Blokir, pegawai yang punya penghalang tidak dapat diproses keluar sampai penghalang selesai |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 13. Diagram Alur General Affairs — Modul General Affairs

Bab manual: [`general-affairs/13-diagram-alur-general-affairs.md`](../../erpApiServices/docs/manualBook/general-affairs/13-diagram-alur-general-affairs.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat permintaan baru (draf) | Masuk My Requests; klik Permintaan Baru; pilih barang Paracetamol 500 mg strip (SKU OBT-001); isi jumlah 20 box; konfirmasi | Dokumen permintaan baru terbentuk, status Draft |
| Negatif — Membatalkan permintaan tanpa login (draf) | Klik Batalkan pada dokumen permintaan; tidak bisa dilakukan | Pesan pesan yang jelas muncul |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | D --/"Stok kurang"/ E["Ditolak"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Jadwal pemesanan satu unit tidak boleh bertabrakan dengan pemesanan lain yang masih berlaku |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Unit yang sedang dirawat, hilang, dihentikan, atau terlambat pemeriksaan yang bersifat memblokir tidak bisa dipesan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
