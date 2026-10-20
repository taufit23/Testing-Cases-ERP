---
title: (PT Sehat Sentosa Farma) — 96. Riset Kebutuhan Bisnis Grup Usaha Kesehatan
category: sehat-sentosa-farma
description: Apa yang dibutuhkan tiap lini usaha kesehatan (apotek, PBF, klinik, laboratorium, produksi herbal, alat kesehatan) dari sebuah ERP, dan di mana kebutuhan itu bersinggungan dengan modul yang sudah ada. Dasar untuk file 21 dan 95.
visibility: internal
---

# 96. Riset Kebutuhan Bisnis Grup Usaha Kesehatan

Tujuan file ini: berpindah dari "apa yang dimiliki aplikasi" ke **"apa yang dibutuhkan bisnisnya"**. Suite `02`–`20` mengikuti modul yang sudah ada; file
`21` menguji kebutuhan di bawah ini, sehingga **kekurangan modul terlihat** dan bisa menjadi acuan perbaikan (daftar di file `95`).

> **Catatan keandalan.** Ringkasan di bawah memadukan (a) hasil pencarian web yang **tipis** (banyak berupa skripsi, jurnal, dan blog vendor, bukan teks
> peraturan) dan (b) pengetahuan umum tentang praktik industri farmasi dan klinik di Indonesia. Nomor peraturan dan batas waktu yang disebut harus
> **diverifikasi ke sumber primer** (Kemenkes, BPOM, BPJS) sebelum menjadi dasar keputusan desain atau klaim ke pelanggan. Item yang saya tandai
> **[verifikasi]** adalah yang paling perlu dicek.

## 1. Peta bisnis grup kesehatan

| Lini usaha | Pelaku dan izin (gambaran) | Apa yang menjadi inti pekerjaan ERP |
| --- | --- | --- |
| **Apotek (retail)** | Apoteker Penanggung Jawab (APJ), Surat Izin Apotek; standar pelayanan kefarmasian (Permenkes 73/2016 [verifikasi]) | resep, obat keras dan terkontrol, stok per batch dan kedaluwarsa, harga, pelayanan swamedikasi, pelaporan |
| **PBF (distribusi obat)** | Pedagang Besar Farmasi bersertifikat **CDOB** (Cara Distribusi Obat yang Baik, BPOM 6/2020 [verifikasi]); APJ wajib; kategori produk: bebas, keras, rantai dingin, narkotika dan psikotropika | penelusuran batch, kualifikasi pelanggan, surat pesanan khusus, penarikan produk (recall), rantai dingin, retur |
| **Klinik pratama dan laboratorium** | izin klinik, tenaga medis ber-STR dan SIP; **rekam medis elektronik** wajib terhubung SATUSEHAT (surat edaran Kemenkes 2023, batas akhir 2023 [verifikasi]); layanan BPJS lewat P-Care | pendaftaran dan antrean, rekam medis, tindakan dan tarif, penagihan pasien dan penjamin, jasa medis dokter, klaim |
| **Produksi obat tradisional / jamu** | CPOTB bertingkat dari BPOM, nomor izin edar produk (TR) [verifikasi]; UMKM didorong memenuhi CPOTB | formula dan batch record, QC dan pelepasan, penelusuran bahan baku sampai produk jadi, penarikan |
| **Alat kesehatan dan sewa alat** | izin edar alat (AKL/AKD) [verifikasi], kalibrasi berkala | aset sewa, pemeliharaan, kalibrasi, isi ulang tabung oksigen, deposit |
| **Fasilitas penunjang** (kafe, parkir, kantin) | usaha biasa | restoran dan kasir |
| **Grup** | beberapa badan hukum berbeda (PBF, apotek, klinik), pembukuan konsolidasi | transaksi antar entitas, konsolidasi, kepatuhan pajak campuran |

## 2. Kebutuhan per lini usaha

### 2.1 Apotek

1. **Batch dan kedaluwarsa.** Setiap penerimaan membawa nomor batch dan tanggal kedaluwarsa; keluar mengikuti **FEFO** (yang paling dekat kedaluwarsa dulu); peringatan
   obat mendekati kedaluwarsa (mis. 6, 3, 1 bulan); obat kedaluwarsa tidak bisa dijual; pemusnahan tercatat dengan berita acara.
2. **Resep dan obat terkontrol.** Obat keras hanya dengan resep; narkotika, psikotropika, prekursor memerlukan pencatatan khusus, penyimpanan terpisah, dan
   **pelaporan berkala ke SIPNAP** (disebut paling lambat tanggal 10 tiap bulan oleh sebagian sumber [verifikasi]).
3. **Pelayanan resep.** Data dokter dan pasien, **racikan** (puyer, kapsul) dengan biaya jasa (tuslah, embalase), etiket dan label, salinan resep, penyerahan dan konseling.
4. **Harga.** Harga eceran tertinggi untuk produk tertentu, margin per golongan, harga berbeda untuk resep dan non-resep, pembulatan.
5. **Pajak.** Sebagian obat dan jasa medis diperlakukan bebas PPN, produk lain kena PPN: satu faktur bisa memuat **campuran** kena dan tidak kena pajak [verifikasi aturan terkini].
6. **Penjamin.** Penjualan ke pasien BPJS/asuransi/perusahaan dengan tagihan ke penjamin (piutang bukan ke pasien).

### 2.2 PBF dan distribusi

1. **Penelusuran batch dua arah:** dari batch ke semua pelanggan yang menerimanya, dan dari pengiriman ke batch asalnya; dasar **recall**.
2. **Kualifikasi pelanggan:** menjual obat keras atau narkotika hanya ke sarana yang berizin; dokumen izin pelanggan dengan masa berlaku.
3. **Surat pesanan khusus** untuk narkotika dan psikotropika, dengan nomor dan penandatangan APJ.
4. **Rantai dingin:** pencatatan suhu penyimpanan dan pengiriman, penanganan produk yang menyimpang.
5. **Retur dan penarikan:** retur ke pemasok, retur dari pelanggan ke gudang karantina, penarikan produk oleh BPOM atau produsen.
6. **Pengiriman dan bukti terima**, ekspedisi, dan ketentuan kualifikasi pemasok.

### 2.3 Klinik dan laboratorium

1. **Pasien dan kunjungan:** nomor rekam medis, pendaftaran, antrean, poli, dokter, jadwal praktik.
2. **Rekam medis elektronik** (anamnesis, diagnosis, tindakan, resep) yang bisa dipertukarkan ke SATUSEHAT; kerahasiaan dan akses berbasis peran.
3. **Tindakan dan tarif** per penjamin; paket layanan; penagihan pasien umum dan penjamin.
4. **Jasa medis dokter:** pembagian hasil per tindakan atau per kunjungan, tarif jasa, dan pembayaran periodik.
5. **Klaim:** BPJS (kapitasi dan non-kapitasi), asuransi swasta, perusahaan; umur piutang per penjamin; penolakan dan penagihan ulang.
6. **Laboratorium:** order pemeriksaan, spesimen, hasil, validasi; **reagen** ber-lot dan kedaluwarsa; kalibrasi dan pengendalian mutu alat.
7. **Kepatuhan:** masa berlaku **STR dan SIP** tenaga medis, pengelolaan **limbah medis** (B3) dengan manifes, dokumen akreditasi.

### 2.4 Produksi obat tradisional

1. **Formula (BOM) berversi** dengan bahan aktif dan pembantu, toleransi, dan hasil (yield).
2. **Catatan batch produksi** (siapa, kapan, bahan lot mana, hasil), pemeriksaan mutu, **pelepasan atau penahanan** batch.
3. **Penelusuran** bahan baku sampai produk jadi dan penarikan produk.
4. **Data registrasi produk** (nomor izin edar, masa berlaku) dan kewajiban label.
5. **Dokumen mutu** (SOP, hasil uji, kalibrasi) yang terhubung ke batch.

### 2.5 Alat kesehatan dan sewa

Aset sewa dengan **jadwal kalibrasi dan servis**, riwayat pemakaian, isi ulang tabung (oksigen) sebagai layanan berulang, deposit, denda kerusakan, dan izin edar alat yang dijual.

### 2.6 Grup dan keuangan

1. **Banyak badan hukum** dengan pembukuan terpisah dan **transaksi antar entitas** (penjualan dari PBF ke apotek) yang dieliminasi saat konsolidasi.
2. **Pajak campuran** per produk dan per jasa; faktur pajak elektronik; PPh 21 tenaga ahli dan honor dokter; pajak final tertentu.
3. **Laporan per lini usaha** (margin apotek, margin PBF, laba klinik per dokter, per penjamin).

## 3. Sumber yang ditemukan (tipis, hanya latar)

- Standar pelayanan kefarmasian dan pelaporan SIPNAP: karya ilmiah yang merujuk Permenkes 73/2016 dan Permenkes 3/2015, serta [regulasi.bkpk.kemkes.go.id](https://regulasi.bkpk.kemkes.go.id/detail/0de549c9-4958-4310-a0f3-be0d71fe22d5/unduh).
- Sertifikasi CDOB: [SK Standar Pelayanan Sertifikasi CDOB 2024 (BPOM)](https://sippn.menpan.go.id/images/article/temp/SK-STANDAR-PELAYANAN-SERTIFIKASI-CARA-DISTRIBUSI-OBAT-YANG-BAIK_2024-20241006190457.pdf) dan studi kepatuhan PBF di [journals.unpad.ac.id](https://journals.unpad.ac.id/farmaka/article/download/50940/pdf).
- Rekam medis elektronik dan SATUSEHAT: surat edaran Kemenkes 2023 ([keslan.kemkes.go.id](https://keslan.kemkes.go.id/unduhan/fileunduhan_1683252264_905012.pdf)) dan [JPNN tentang eClinic](https://www.jpnn.com/news/infokes-hadirkan-aplikasi-rekam-medis-elektronik-eclinic-leap).
- Produksi herbal: [HashMicro tentang inventori pabrik herbal](https://www.hashmicro.com/id/blog/software-inventory-pabrik-obat-herbal/), [HashMicro tentang QC CPOTB](https://www.hashmicro.com/id/blog/software-quality-control-pabrik-obat-herbal/), dan [Bisnis.com tentang target CPOTB UMKM jamu](https://ekonomi.bisnis.com/read/20181212/257/868941/bpom-targetkan-seluruh-umkm-jamu-penuhi-coptb-pada-2025).

Yang **tidak** berhasil diverifikasi lewat pencarian: aturan jasa medis dan penagihan penjamin, format surat pesanan narkotika, tata cara recall, dan teks CPOTB terbaru. Itu perlu
dibaca dari peraturan atau dikonsultasikan dengan APJ, kepala klinik, dan penanggung jawab mutu sebelum menetapkan desain fitur.
