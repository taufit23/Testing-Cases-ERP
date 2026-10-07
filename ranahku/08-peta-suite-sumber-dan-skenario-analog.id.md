---
title: Ranahku — Peta Suite Sumber dan Skenario Analog
description: Menunjukkan di mana setiap suite pengujian lain (accounting, 16 suite industri, global-testing, suite per modul Nusatech/Coretax) diterapkan di Ranahku, dan menambahkan skenario analog untuk pola yang tidak punya padanan langsung (klaim BPJS ditolak, dana terikat NGO, selisih kurs, periode mingguan dan kuartalan, saldo awal tengah tahun).
---

# Ranahku — Peta Suite Sumber dan Skenario Analog

> Disusun 2026-10-07. Berkas 04–07 membawa semua pola dari suite lain ke Ranahku. Berkas ini adalah **daftar pemeriksa**: untuk tiap folder di
> `Testing-Cases-ERP/` tertulis pola apa yang diambil, di mana ia dijalankan di Ranahku, dan skenario analog bagi pola yang tidak punya
> padanan langsung. Bila ada folder baru di repo ini, tambahkan barisnya di sini.
>
> **Dua lapisan dari tiap suite sumber:** (1) *skenario bisnis* (diterapkan di berkas 04–07 dan skenario analog di bawah) dan (2) *uji penolakan dan kasus batas*
> (Negatif, guard, saldo awal, validasi API, jebakan desain), yang diterapkan di **berkas 09**. Kolom "Diterapkan di" di bawah menyebut kedua lapisan.

## 1. Peta Folder Sumber → Ranahku

| Folder sumber | Pola khas yang diambil | Diterapkan di |
| --- | --- | --- |
| `accounting/` (9 berkas) | Jurnal manual (sukses, negatif, approval, reverse, bulk), GL dan neraca saldo, tutup periode dan tahun, laporan keuangan, anggaran, aset tetap, rekonsiliasi bank, rekap PPN, edge case (guard periode berikutnya, tumpang tindih, celah, rantai reversal, post-dated, multi-currency, residu, pembagian 12 bulan) | 05 (AI–AP) |
| `accounting-construction` | Progres + retensi, subkontraktor, uang muka, jurnal per proyek, alat berat | 05 AI27–AI28, AI25; 07 AY5–AY8; 05 AN |
| `accounting-education` | Tagihan massal, beasiswa (kontra-pendapatan), amortisasi uang pangkal, setoran bendahara, selisih kas, PPh 21, guard tutup periode | 05 AI25, AI29, AI30, AI34; AK1–AK7; skenario analog BC3 |
| `accounting-ecommerce` | Rekap penjualan batch, biaya gateway, refund, rekonsiliasi gateway, per-channel | 05 AI23, AI31–AI32, AO10; 05 AJ5–AJ7 |
| `accounting-fnb-kafe` | Rekap harian, voucher korporat, selisih kas outlet, modal tambahan, penyusutan terlambat, tutup tahun | 05 AI26, AI29, AK11, AK16; 06 AT |
| `accounting-hospitality` | Deposit booking, pendapatan kamar + pajak daerah, USD, POS restoran dan spa | 05 AI35 (PB1), AI36 (USD); 06 AT39; 05 AI26 |
| `accounting-klinik-gigi`, `accounting-klinik-umum` | Transaksi mingguan, tutup periode **mingguan**, kapitasi, MCU korporat termin, payroll dokter, obat bebas PPN, kas kecil | Skenario analog BC4, BC5; 05 AI27; 06 AS |
| `accounting-rumah-sakit` | Klaim dengan pembayar berbeda (BPJS, asuransi, tunai), klaim ditolak sebagian, fee dokter persen, retur, kas kecil | Skenario analog BC1, BC2; 06 AV23 (komisi) |
| `accounting-manufaktur`, `accounting-manufaktur-2` | Bahan → WIP → barang jadi, overhead, susut bahan, pinjaman bank, **multi-currency dan selisih kurs**, anggaran **kuartalan**, rekonsiliasi dual currency | 04 AC; 05 AI34, AI36; skenario analog BC6, BC4 |
| `accounting-ngo` | Dana terikat per program, bank per donor, pakai bank donor untuk biaya umum (sistem tidak menolak), laporan aktivitas per program | Skenario analog BC7; 05 AO9 |
| `accounting-service-agency`, `accounting-nusatech` | Invoice retainer bulanan, pendapatan diterima dimuka, milestone proyek, PPh 23, penjualan retail di unit lain | 05 AI25, AI27, AI33; 06 AR8–AR10; 05 AJ5–AJ8 |
| `accounting-pos-retail` | Setup toko, warehouse pusat dan toko, cash session, transaksi harian, integrasi akuntansi | 04 Z; 06 AS; 05 AO11 |
| `accounting-retail-tahun-berjalan` | Dua tahun buku (2025 dan 2026), transaksi 12 bulan, tutup tahun, laporan lintas tahun | 05 AK19–AK20; skenario analog BC5 |
| `accounting-coretax` | Verifikasi gap saldo awal, jurnal manual, reverse | Skenario analog BC5; 05 AI18 |
| `global-testing/ACCOUNTING.md` | Tujuh kasus akuntansi bisnis (restoran, distribusi, jasa, aset, multi outlet, pajak, bank) | 05 (AI–AP) dan 07 AX |
| `global-testing/GLOBAL.md` | Siklus bisnis, 77 bagian uji integrasi dan prinsip | 07 |
| `global-testing/PO.md`, `SO.md` | 20 kasus pembelian, 20 kasus penjualan | 06 AQ, AR |
| `global-testing/POS.md`, `RERTO.md` | 60 kasus kasir, 80 kasus restoran | 06 AS, AT |
| `global-testing/Inventory.md` | 26 kasus persediaan | 06 AU |
| `global-testing/HRM.md` | 4 level pengujian SDM | 06 AV |
| `purchasing*`, `sales*` (termasuk Coretax dan Nusatech) | Alur PR→PQ→PO→GR→PI→PPB dan Quotation→SO→Delivery→Invoice→Payment; jasa tanpa delivery; retail dengan delivery | 02 B–E (sudah), 06 AQ, AR |
| `hrm-nusatech`, `inventory-nusatech` | Absensi, cuti, payroll, komisi; stok awal lewat penyesuaian, opname, lot dan serial | 02 F, 03 L; 06 AU, AV |
| *Semua* suite `accounting-*` (bagian 00 dan semua baris Negatif) | Validasi master data (kode unik, enum, isolasi cabang), saldo awal dan akun Ekuitas Saldo Awal, `balance_required`, mata uang dan kurs aktif, generate periode, penolakan jurnal | 09 BD, BI |
| `accounting-manufaktur`, `-manufaktur-2` (file 02, 06) | Utang valas, selisih kurs, jebakan pelunasan naif, kurs aktif vs tanggal, rekening bank USD, anggaran dan periode kuartalan | 09 BJ; 08 BC4, BC6 |
| `accounting-pos-retail` (Negatif) | Gudang toko saja, satu sesi per gudang, tendered kurang, hold, void/refund ganda, over-refund | 09 BG |
| `purchasing*`, `sales*` (Negatif) | PR kosong, kontak salah tipe, over-receipt, PI melebihi GR, bayar sebelum disetujui, SKU duplikat, batas kredit, diskon nonaktif, over-delivery, export ganda, konfigurasi penjualan belum diatur | 09 BE, BF |
| `hrm-nusatech`, `inventory-nusatech` (Negatif) | Absensi ganda, cuti melebihi saldo, payroll dibayar sebelum disetujui, komisi posisi non-sales, post tanpa submit, serial duplikat, unit cost nol, pemetaan akun hilang | 09 BH |
| `penjualan-sewa-aplikasi` | Sisi pemilik platform (langganan, mitra, lisensi) | Suite tersendiri (di luar Ranahku sebagai klien) |
| `_deferred-integrated` | Umur piutang dan utang | 07 AX17–AX19, AZ14; 06 AR21 |

---

## 2. Skenario Analog (pola tanpa padanan langsung)

Kolom *Pola asal* menunjuk suite sumbernya. Selesaikan Tahap AI–AP (berkas 05) lebih dulu.

| # | Skenario analog | Pola asal | Langkah di Ranahku | Yang diperiksa | OK |
| --- | --- | --- | --- | --- | --- |
| BC1 | **Faktur sewa disengketakan sebagian** (klaim ditolak sebagian) | Rumah sakit T12 | Faktur Distributor 7.500.000 + PPN; pelanggan menolak 1.500.000 karena fitur tidak terpakai; buat retur/credit note 1.500.000 + PPN; pelanggan bayar sisa | Piutang tepat sisa yang disepakati; pendapatan dan PPN keluaran berkurang sebesar yang ditolak; selisih tidak "menggantung" sebagai piutang abadi | ⬜ |
| BC2 | **Pembayar berbeda untuk satu layanan** (BPJS vs asuransi vs tunai) | Rumah sakit T3, T6, T13 | Satu paket kanvasing dibayar sebagian tunai di tempat, sebagian transfer oleh induk usaha pelanggan | Dua penerimaan terpisah ke satu faktur; alokasi benar; faktur lunas hanya bila total terpenuhi | ⬜ |
| BC3 | **Diskon sebagai kontra-pendapatan** (beasiswa/potongan SPP) | Pendidikan 1.2 | Beri pelanggan "Paket Dasar gratis 2 bulan" sebagai promosi: Dr `6-108` atau akun kontra pendapatan / Cr `4-101` | Pendapatan bruto tetap terlihat; potongan tampil di akun terpisah (bukan pendapatan dikurangi diam-diam); laporan menunjukkan keduanya | ⬜ |
| BC4 | **Periode mingguan dan kuartalan** | Klinik gigi (mingguan), manufaktur (kuartalan) | Di `FY-TEST` buat tahun buku dengan Generate Periods **mingguan**; ulangi dengan **kuartalan**; posting jurnal ke tiap periode | Periode terbentuk sesuai pilihan tanpa celah dan tanpa tumpang tindih; tutup periode berurutan dan penjaga berjalan sama dengan bulanan; laporan per rentang menjumlahkan periode benar | ⬜ |
| BC5 | **Saldo awal tengah tahun dan lintas tahun** | Coretax (gap saldo awal), retail tahun berjalan | (a) Verifikasi: Neraca Saldo awal 1 September seimbang dan total saldo awal aset = kewajiban + ekuitas (dengan `3-103` sebagai penyeimbang); (b) buat Fiscal Year 2027, tutup 2026 di FY-TEST yang tersalin, bandingkan saldo awal 2027 dengan saldo akhir 2026 | Tidak ada selisih saldo awal; saldo akhir tahun lama = saldo awal tahun baru untuk akun neraca; akun laba rugi mulai nol; laporan 2026 tidak berubah oleh transaksi 2027 | ⬜ |
| BC6 | **Selisih kurs realisasi** | Manufaktur 2, hotel USD | Beli langganan server USD 100 saat kurs 15.800 (utang 1.580.000); bayar saat kurs 16.000 (kas keluar 1.600.000) | Selisih 20.000 tercatat sebagai rugi selisih kurs di akun yang tepat (atau dicatat bahwa akun selisih kurs belum ada → 🆕); utang nol setelah lunas; rekonsiliasi bank valas selaras | ⬜ |
| BC7 | **Dana titipan tidak boleh dipakai operasional** | NGO 1.7 (negatif: sistem tidak menolak) | Terima deposit sewa jangka pendek 1.000.000 ke rekening penampung; pakai rekening yang sama membayar beban listrik | Dicatat apakah sistem menolak/memberi peringatan; bila tidak, 🆕 (tidak ada pemisahan dana terikat); saldo deposit tetap tampil sebagai kewajiban | ⬜ |
| BC8 | **Komisi persentase** (fee dokter persen) | Rumah sakit T2, T5 | Aturan komisi 10% dari nilai kontrak yang ditutup; tutup kontrak 3.500.000 | Komisi 350.000 muncul di payroll; beban komisi `6-102` bertambah; kontrak batal mengurangi komisi atau menjadi komisi minus sesuai aturan | ⬜ |
| BC9 | **Penagihan berulang bulanan** | Service agency (invoice retainer), Nusatech (managed service) | Pelanggan Paket Usaha ditagih tiap bulan lewat Pola Transaksi atau SO berulang | Faktur bulan berikutnya terbentuk dengan nomor, jatuh tempo, dan PPN benar tanpa menyalin manual | ⬜ |
| BC10 | **Opname kas kecil akhir bulan** | Klinik umum T19, RS T16 | Hitung kas kecil kantor; selisih lebih 10.000; setor sisa ke bank | Selisih tercatat; setor menutup kas ke nilai minimal yang ditetapkan | ⬜ |
| BC11 | **Koreksi dengan Reverse dan Recreate** | RS T16, kafe 1.x (demonstrasi reverse) | Salah akun pada beban listrik; Reverse lalu Recreate dengan akun benar | Tiga jurnal berurutan dapat ditelusuri; saldo akhir benar; tidak ada perubahan pada jurnal asli | ⬜ |
| BC12 | **Pelunasan piutang awal** | Klinik umum T5, Coretax | Pelunasan piutang dari saldo awal (piutang sebelum September) | Piutang saldo awal turun tanpa membuat piutang baru; tidak ada faktur "hantu" | ⬜ |

---

## 3. Cara Menandai Cakupan

1. Setiap kali satu folder sumber selesai dipetakan dan semua baris yang menunjuk ke Ranahku sudah diuji, beri tanda ✅ di kolom folder pada salinan lokal tabel 1.
2. Folder yang menghasilkan temuan baru ditandai dengan tautan ke berkas temuan di `TemuanTestCase/`.
3. Bila suite sumber diperbarui, periksa apakah pola baru perlu ditambahkan ke berkas 04–07.
