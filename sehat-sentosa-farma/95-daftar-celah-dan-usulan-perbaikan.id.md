---
title: (PT Sehat Sentosa Farma) — 95. Daftar Celah dan Usulan Perbaikan
category: sehat-sentosa-farma
description: Register celah yang ditemukan dari kebutuhan bisnis grup kesehatan (file 21) dan dari pembanding Odoo (file 97): dampak, usulan desain berbasis konfigurasi, prioritas dan ukuran kerja. Bahan memilih prioritas pengembangan.
visibility: internal
---

# 95. Daftar Celah dan Usulan Perbaikan

Dibuat dari [`21`](./21-kebutuhan-bisnis-kesehatan-dan-uji-celah.id.md) (kebutuhan bisnis) dan [`97`](./97-referensi-odoo-amati-tiru-modifikasi.id.md) (pembanding Odoo). Status awal semua baris:
**belum diverifikasi di layar**; perbarui setelah suite diuji. **Prioritas**: P1 = berdampak langsung ke kepatuhan atau uang dan lazim diminta klien kesehatan, P2 = penting tetapi ada
jalan pintas sementara, P3 = nilai tambah. **Ukuran**: S (hari), M (1 sampai 2 minggu), L (beberapa minggu), XL (proyek besar atau bergantung pihak ketiga). Prinsip desain: **config-first**
(bangun lewat konfigurasi cabang dengan bawaan sama dengan perilaku sekarang) dan memakai pola yang sudah ada (pola global + override, mesin lampiran, mesin persetujuan, status master).

## 1. Persediaan dan obat (P1 paling nyata untuk apotek dan PBF)

| ID | Celah | Dampak bisnis | Usulan | Prio | Ukuran |
| --- | --- | --- | --- | --- | --- |
| G01 | Tidak ada peringatan atau laporan obat mendekati kedaluwarsa | obat kedaluwarsa menumpuk, kerugian dan risiko kepatuhan | laporan dan dasbor "mendekati kedaluwarsa" per gudang dengan ambang 6/3/1 bulan (pengaturan cabang) + notifikasi | P1 | S |
| G02 | Lot tidak otomatis menjadi kedaluwarsa; FEFO hanya untuk metode identifikasi khusus; pengisian batch saat GR perlu dipastikan | penjualan dari lot kedaluwarsa, urutan keluar salah | proses terjadwal menandai lot kedaluwarsa; blok jual/transfer lot kedaluwarsa dan karantina; opsi "FEFO otomatis" per produk tanpa mengubah metode biaya; alasan penyesuaian "kedaluwarsa" + berita acara | P1 | M |
| G03 | Tidak ada penelusuran batch dua arah (batch → pelanggan, bahan → produk jadi) | tidak bisa recall dengan cepat | laporan penelusuran dari pergerakan lot yang sudah ada + tindakan "retur massal" | P1 | M |
| G04 | POS tidak memilih lot | batch dan kedaluwarsa hilang di retail | pilih lot otomatis (FEFO) di POS, riwayat transaksi menyimpan lot, opsi tampil di struk | P2 | M |
| G05 | Produk tanpa golongan obat | obat keras dan terkontrol tidak bisa diperlakukan khusus | atribut golongan (bebas, bebas terbatas, keras, narkotika, psikotropika, prekursor, OOT) per produk dengan aturan jual per golongan | P1 | M |
| G06 | Tidak ada resep, dokter dan pasien di penjualan | tidak bisa melayani obat keras sesuai aturan | entitas resep ringan di POS (dokter, pasien, aturan pakai, salinan, etiket), wajib resep untuk golongan tertentu dengan persetujuan Apoteker | P1 | L |
| G07 | Tidak ada racikan di kasir | apotek tidak bisa menjual puyer dan kapsul racik | transaksi racikan: bahan, biaya racik (tuslah/embalase), stok bahan berkurang proporsional | P2 | L |
| G08 | Tidak ada laporan narkotika dan psikotropika (SIPNAP) **[reg]** | kewajiban pelaporan bulanan | laporan mutasi per produk terkontrol dalam format yang mudah disalin ke SIPNAP (ekspor), tanpa integrasi langsung dulu | P1 | M |
| G09 | Tidak ada batas harga atas (HET) | risiko menjual di atas harga resmi | atribut HET per produk dengan peringatan atau penolakan | P2 | S |
| G10 | PPN campuran dan faktur pajak | salah hitung pajak, kewajiban pajak | pastikan pajak per baris di semua dokumen, ringkasan pajak memisahkan DPP kena dan tidak kena, ekspor data faktur pajak; verifikasi aturan terkini | P2 | M |
| G11 | Tidak ada data nomor izin edar (NIE/TR/AKL) dan masa berlaku | label dan kepatuhan | kolom registrasi produk + peringatan masa berlaku + tampil di label | P2 | S |

## 2. Distribusi (PBF)

| ID | Celah | Dampak bisnis | Usulan | Prio | Ukuran |
| --- | --- | --- | --- | --- | --- |
| G12 | Tidak ada kualifikasi pelanggan dan izin sarana | menjual obat keras ke pihak tak berizin | dokumen izin pelanggan bermasa berlaku (mesin lampiran) + aturan blok jual per golongan | P1 | M |
| G13 | Tidak ada surat pesanan khusus narkotika dan psikotropika **[reg]** | kewajiban dokumen | dokumen SP khusus bernomor, tertanda APJ, terlampir ke pesanan | P2 | M |
| G14 | Tidak ada log suhu rantai dingin | produk rantai dingin tidak teraudit | catatan suhu per gudang/pengiriman dengan peringatan penyimpangan dan karantina | P3 | L |

## 3. Klinik dan laboratorium

| ID | Celah | Dampak bisnis | Usulan | Prio | Ukuran |
| --- | --- | --- | --- | --- | --- |
| G15 | Tidak ada master pasien dan data klinis | inti operasional klinik tidak ada | modul Klinik baru (add-on seperti Restoran/Rental): pasien, nomor RM, kunjungan; persetujuan data pasien dan retensi | P1 | XL |
| G16 | Tidak ada pendaftaran, antrean dan jadwal dokter | klinik mengandalkan sistem lain | antrean per poli dan jadwal dokter | P2 | L |
| G17 | Tidak ada rekam medis elektronik dan SATUSEHAT **[reg]** | kewajiban regulasi klinik | **keputusan strategis**: bangun sendiri atau integrasi ke RME pihak ketiga (engine integrasi sudah ada) | P1 | XL |
| G18 | Tarif tindakan per penjamin dan penagihan gabungan | billing pasien tidak sesuai | paket tindakan, daftar harga per penjamin, tagihan kunjungan (konsultasi + tindakan + obat) | P1 | L |
| G19 | Jasa medis dokter | uang terbesar klinik; hitung manual | aturan jasa per tindakan/kunjungan (pola aturan komisi), hutang jasa, pembayaran, PPh 21 | P1 | M |
| G20 | Alur klaim penjamin | piutang asuransi sulit dilacak | status klaim, penolakan, penagihan ulang, umur piutang per penjamin | P2 | M |
| G21 | Kapitasi dan integrasi BPJS P-Care **[reg]** | efisiensi dan kepatuhan | pendapatan kapitasi otomatis dari jumlah peserta; integrasi P-Care menyusul | P2 | L |
| G22 | Laboratorium (order, spesimen, hasil, reagen) | layanan lab tanpa sistem | modul lab ringan: order, hasil, reagen per lot | P3 | L |

## 4. Produksi, aset dan SDM

| ID | Celah | Dampak bisnis | Usulan | Prio | Ukuran |
| --- | --- | --- | --- | --- | --- |
| G26 | Batch record dan pelepasan QC belum utuh; penelusuran bahan baku | CPOTB/CPOB | catatan batch (lot bahan, operator, penyimpangan), status karantina sampai QC melepas, laporan penelusuran | P1 | M |
| G27 | Versi formula (BOM) perlu diverifikasi | perubahan formula tanpa jejak | versi BOM dengan tanggal berlaku | P2 | S |
| G28 | Tidak ada jadwal kalibrasi dan pemeliharaan aset | alat tak terkalibrasi tetap dipakai atau disewa | jadwal dan riwayat kalibrasi/servis per aset, blok sewa bila lewat jatuh tempo, pengingat | P2 | M |
| G23 | Tidak ada izin kompetensi karyawan bermasa berlaku (STR/SIP) | tenaga tak berizin dijadwalkan | jenis dokumen karyawan dengan masa berlaku, peringatan 90/60/30 hari, tampil di jadwal | P1 | S |
| G24 | Tidak ada daftar izin usaha per cabang | izin kedaluwarsa tanpa disadari | daftar izin per cabang (SIA, izin klinik, CDOB) dengan masa berlaku dan peringatan | P2 | S |
| G25 | Tidak ada pencatatan limbah medis B3 | kepatuhan lingkungan | catatan limbah dan manifes | P3 | M |

## 5. Grup, keuangan dan pembanding Odoo

| ID | Celah | Dampak bisnis | Usulan | Prio | Ukuran |
| --- | --- | --- | --- | --- | --- |
| G29 | Tidak ada transaksi antar entitas dan eliminasi konsolidasi | grup dengan banyak PT | akun dan jurnal antar entitas, laporan gabungan dengan eliminasi (terkait rencana mode akuntansi terpusat) | P2 | L |
| G30 | Laporan laba per dokter/penjamin/lini | keputusan bisnis | dimensi tambahan pada laporan (pola unit bisnis) | P3 | M |
| G31 | Faktur pembelian tidak punya nomor faktur pemasok; tidak ada deteksi duplikat | risiko bayar ganda | kolom nomor faktur pemasok + peringatan duplikat (pemasok + nomor, lalu jumlah + tanggal) | **P1** | S |
| G32 | Tidak ada master syarat pembayaran dan diskon pembayaran dini | diskon tunai dan termin kompleks tak terjurnal | master termin (mis. 2/10 net 30) + jurnal diskon dini otomatis | P2 | M |
| G33 | Periode terkunci masih bisa dibuka; tidak ada izin sementara terbatas | kontrol audit lemah | kunci permanen opsional dan izin sementara berwaktu dengan alasan | P2 | M |
| G34 | Tidak ada akun penampung per metode pembayaran | dana QRIS H+1 tercatat langsung di bank | akun penampung opsional per metode pembayaran, dilepas saat settlement | P2 | M |
| G35 | Selisih kurs hanya di faktur biaya logistik; laba dan rugi kurs tidak dipisah di laporan | impor bahan baku valas | mata uang di faktur penjualan/pembelian + laporan laba/rugi kurs | P3 | L |

## 6. Urutan saran (untuk diputuskan owner)

1. **Cepat dan bernilai (S, P1):** G31 faktur pemasok ganda, G01 peringatan kedaluwarsa, G23 STR/SIP, G09 HET, G11 NIE.
2. **Inti apotek dan PBF (M, P1):** G02 kedaluwarsa dan FEFO, G03 penelusuran batch, G05 golongan obat, G08 laporan SIPNAP, G12 kualifikasi pelanggan, G26 batch record.
3. **Keputusan strategis sebelum menulis kode:** apakah **modul Klinik** (G15–G19, G21) dibangun sendiri atau lewat integrasi RME pihak ketiga (G17); ini menentukan apakah grup kesehatan menjadi pasar utama.
4. **Tidak dikerjakan dulu:** G14, G22, G25 (nilai tambah) dan G35 (menunggu klien dengan transaksi valas).

Konsultasikan dulu dengan Apoteker Penanggung Jawab, kepala klinik dan penanggung jawab mutu sebelum menetapkan desain G05–G08, G12, G15–G21 dan G26: banyak aturan yang saya tandai **[reg]**
belum diverifikasi ke teks peraturan.
