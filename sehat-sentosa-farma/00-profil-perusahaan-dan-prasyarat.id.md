---
title: (PT Sehat Sentosa Farma) — 00. Profil Perusahaan, Master Data Acuan dan Prasyarat
category: sehat-sentosa-farma
description: Skenario perusahaan kesehatan terpadu (apotek, klinik dan laboratorium, distribusi obat, pabrik herbal, kafe, sewa alat medis, tambang kapur) yang dipakai semua file di suite ini. Memuat cabang, peran, data acuan, urutan kerja dan aturan membaca hasil.
visibility: internal
---

# 00. Profil Perusahaan, Master Data Acuan dan Prasyarat

Suite ini menguji **seluruh modul dan seluruh bab manual book** lewat satu perusahaan kesehatan yang saling terhubung. Berbeda dari suite
`accounting-klinik-*` dan `accounting-rumah-sakit` yang berdiri di modul Akuntansi saja, di sini satu transaksi mengalir lintas modul:
barang dibeli, disimpan, dipindah, diolah, dijual, dibayar, digaji, dan akhirnya muncul di laporan.

> **Cara suite ini disusun.** File `01` adalah **alur terpadu** yang ditulis tangan dengan angka acuan yang bisa dihitung ulang.
> File `02` sampai `20` adalah **kasus per modul**: satu bagian per bab manual book, dengan baris Positif dan Negatif yang
> **dirancang oleh Ollama lokal (qwen2.5:7b-instruct) dari isi bab manual book** dan sudah disaring. Baris dari Ollama berstatus
> **draf**: harus dibaca penguji dan disesuaikan dengan layar sebenarnya sebelum dianggap final. File `99` memetakan setiap bab ke
> file ujinya, jadi tidak ada fitur yang terlewat.

## 1. Profil

**PT Sehat Sentosa Farma** (merek "Sentosa Farma"), grup usaha kesehatan, berstatus PKP, mata uang Rupiah, tahun fiskal Januari sampai
Desember 2026. Periode uji utama: **Oktober 2026**.

| Cabang | Fungsi | Modul yang dominan |
| --- | --- | --- |
| **Kantor Pusat & Distribusi Jakarta** (cabang utama) | gudang obat dan alat kesehatan, penjualan grosir ke klinik dan apotek mitra, pembukuan pusat | Pembelian, Persediaan, Penjualan, Kanvasing, Akuntansi, Keuangan, Aset Tetap |
| **Apotek Sentosa Bandung** | apotek retail, resep, QRIS | POS, Persediaan, Pembayaran online |
| **Klinik Pratama & Laboratorium Bekasi** | layanan medis, kasir, tenaga kesehatan | SDM, POS (kasir jasa), Proyek (akreditasi) |
| **Pabrik Herbal Sukabumi** | produksi jamu dan suplemen, bahan baku kalsium karbonat | Manufaktur, Pertambangan |
| **Kafe Sehat (lobi klinik)** | kafe pasien dan keluarga | Restoran |
| **Layanan Sewa Alat Medis** (dikelola Pusat) | kursi roda, tabung oksigen, tempat tidur pasien | Sewa |

Cabang Pusat adalah **cabang utama** (laporan bisa digabung dengan cabang anak). Provider ini dibuat lewat **Onboard Client** oleh
platform owner (modul Platform Owner), bukan lewat seeder.

## 2. Peran dan pengguna uji

| Peran | Contoh pengguna | Ruang lingkup |
| --- | --- | --- |
| Direktur (admin klien) | Dr. Rahmat Hidayat | semua modul, persetujuan tingkat akhir |
| Manajer Keuangan | Sari Wulandari | Akuntansi, Keuangan, Aset Tetap, laporan, persetujuan biaya dan jurnal |
| Staf Pembelian | Bima Prakoso | Pembelian |
| Kepala Gudang | Hendra Saputra | Persediaan, penerimaan barang, transfer, stok opname |
| Apoteker Penanggung Jawab | Apt. Lestari Dewi | POS apotek, obat resep, persetujuan retur |
| Kasir Apotek | Rina Marlina | POS (hanya sesi kasirnya sendiri) |
| Sales Lapangan | Dewi Anggraini | Kanvasing |
| Kepala Produksi | Joko Santoso | Manufaktur |
| Staf HR | Maya Puspita | SDM, rekrutmen, payroll |
| Pemilik Platform | (akun owner) | Platform Owner: paket, klien, penangguhan |

Peran uji dipakai juga untuk kasus **izin**: setiap file modul punya baris "peran tanpa izin" yang harus berujung 403 dan tombol
berstatus nonaktif dengan penjelasan, bukan tombol hilang.

## 3. Data acuan

### 3.1 Mitra

| Kode | Nama | Jenis | Catatan |
| --- | --- | --- | --- |
| SUP-01 | PT Bintang Farmasi Utama | pemasok obat | termin 14 hari |
| SUP-02 | PT Alkes Prima Mandiri | pemasok alat kesehatan | termin 30 hari |
| SUP-03 | CV Kapur Medika | pemasok bahan baku (tambang kapur) | internal grup, dicatat sebagai pemasok |
| CUS-01 | Klinik Pratama Harapan Sehat | pelanggan grosir | batas kredit Rp 20.000.000, termin 14 hari |
| CUS-02 | Apotek Mitra Sehat | pelanggan grosir dan calon kanvasing | batas kredit Rp 10.000.000 |
| CUS-03 | Pasien Umum | pelanggan POS | tanpa kredit |

### 3.2 Produk dan harga acuan

| SKU | Produk | Satuan | Harga beli | Harga jual grosir | Harga jual apotek | Catatan |
| --- | --- | --- | ---: | ---: | ---: | --- |
| OBT-001 | Paracetamol 500 mg | strip | 3.000 | 4.500 | 6.000 | obat bebas |
| OBT-002 | Amoxicillin 500 mg | strip | 9.000 | 12.000 | 15.000 | obat keras, wajib resep di apotek |
| SUP-001 | Vitamin C 1000 mg | botol | 25.000 | 32.000 | 40.000 | suplemen |
| ALK-001 | Masker Medis (box 50) | box | 25.000 | 35.000 | 45.000 | alat kesehatan |
| ALK-002 | Alkohol Swab (box 100) | box | 18.000 | 25.000 | 30.000 | alat kesehatan |
| HRB-001 | Jamu Kunyit Asam | sachet | 380 (biaya produksi) | 700 | 1.000 | hasil produksi pabrik |
| HRB-002 | Suplemen Kalsium | botol | dari BOM | 30.000 | 38.000 | hasil produksi, memakai kalsium karbonat |
| KAL-001 | Kalsium Karbonat (bahan baku) | kg | dari tambang | - | - | bahan baku, tidak dijual eceran |
| RNT-001 | Sewa Kursi Roda | hari | - | 15.000 per hari | - | aset sewa, deposit Rp 100.000 per unit |
| MNU-001 | Teh Jahe Hangat | gelas | - | - | 12.000 | menu kafe |

### 3.3 Gudang

`WH-PST` (Pusat), `WH-BDG` (Apotek Bandung), `WH-SKB-RM` (bahan baku Sukabumi), `WH-SKB-FG` (barang jadi Sukabumi). Transfer antar
gudang wajib lewat **Transfer Stok**, bukan penyesuaian manual.

### 3.4 Akun kunci (acuan nama, kode mengikuti template akun cabang)

Kas Kecil, Bank Operasional, Piutang Usaha, Persediaan Barang Dagang, Persediaan Bahan Baku, Persediaan Barang Jadi, Aset Tetap, Akumulasi
Penyusutan, Utang Usaha, Utang PPN, PPN Masukan, Pendapatan Penjualan, Pendapatan Jasa, Harga Pokok Penjualan, Beban Gaji, Beban Listrik,
Beban Penyusutan, Modal Pemilik, Laba Ditahan, Laba/Rugi Pelepasan Aset, Laba/Rugi Selisih Kurs.

Saldo awal 1 Oktober 2026 (lewat fitur Saldo Awal): **Bank Operasional Rp 500.000.000** dan **Modal Pemilik Rp 500.000.000**. Tanpa
persediaan awal, supaya angka di file `01` bisa dihitung dari nol.

## 4. Urutan kerja yang disarankan

1. File `02` (Platform Owner, Mulai Menggunakan, Pengaturan Akun): provider, cabang, pengguna, peran.
2. File `03` (Konfigurasi Umum, Inti, Persetujuan): master data, template, alur persetujuan.
3. File `01` (alur terpadu) berjalan **mengikuti urutan langkahnya** dan memanggil file modul bila perlu rincian.
4. File modul `04` sampai `20` untuk kedalaman per bab, termasuk kasus Negatif dan izin.
5. File `98` (penutupan dan rekonsiliasi) terakhir, lalu `99` untuk memastikan tidak ada bab yang belum disentuh.

## 5. Aturan membaca hasil

- **Positif**: jalur normal harus berhasil dan efek di modul lain harus terlihat. **Negatif**: harus ditolak dengan pesan jelas, bukan
  gagal diam-diam atau error server. **Netralisasi**: cara mengembalikan data ke keadaan semula bila diperlukan file berikutnya.
- Angka di file `01` adalah **acuan hitung**: bila hasil di layar berbeda, catat sebagai temuan dan jangan menyesuaikan angka acuannya.
  Angka yang bergantung pada konfigurasi cabang (pajak POS, mode jurnal, persetujuan) ditulis sebagai **hubungan** (mis. "Persediaan
  turun sebesar HPP"), bukan angka mutlak.
- Setiap kali sebuah baris menyebut "tombol nonaktif", yang diuji adalah **tombol terlihat tetapi nonaktif disertai alasan di tooltip**
  (aturan tampilan proyek), bukan tombol yang hilang.
- Pengujian dilakukan di **database uji**, bukan produksi. Untuk pembayaran online pakai kunci sandbox dan panduan
  `erpApiServices/docs/panduan-uji-kredensial-pembayaran.id.md`.

## 6. Batas cakupan

- Integrasi eksternal nyata (SMTP, WhatsApp, bank sungguhan) tidak diuji di sini; yang diuji adalah perilaku aplikasi saat integrasi
  belum diatur dan saat memakai mode sandbox.
- QRIS sandbox memakai kode tiruan; pembayaran disimulasikan dari dashboard penyedia, bukan dengan memindai.
- Fitur yang dikunci paket langganan diuji dua kali: dengan fitur aktif dan dengan fitur tidak termasuk paket (menu hilang dan 403).
