---
title: Ranahku — Akuntansi Mendalam (Jurnal, Buku Besar, Tutup Periode, Laporan, Anggaran, Aset, Bank, Pajak)
description: Pengujian akuntansi sedalam suite accounting/ dan 16 suite industri (konstruksi, pendidikan, e-commerce, kafe, hotel, klinik, rumah sakit, manufaktur, NGO, jasa, retail tahun berjalan) tetapi memakai akun, kegiatan usaha, dan transaksi Ranahku. Mencakup jalur sukses, jalur negatif, penjaga (guard) periode, rantai reversal, dan angka yang harus cocok antar laporan.
---

# Ranahku — Akuntansi Mendalam

> Disusun 2026-10-07. Berkas 03 Tahap I hanya menyentuh akuntansi sekali. Suite `accounting/` (9 berkas) dan suite industri
> (konstruksi, pendidikan, e-commerce, F&B, hotel, klinik gigi/umum, rumah sakit, manufaktur 1 dan 2, NGO, jasa, retail tahun berjalan, Nusatech, Coretax)
> menguji akuntansi jauh lebih dalam. Berkas ini membawa **semua pola uji itu** ke Ranahku: tiap pola industri dipetakan ke kegiatan
> Ranahku (sewa aplikasi, toko, rumah makan) supaya tim penguji tidak perlu berpindah skenario bisnis.
>
> **Prasyarat:** Tahap 1–12 berkas 01 selesai (akun `1-101` … `6-190`, kegiatan `SEWA`/`RETAIL`/`RESTO`, pajak `PPN-OUT`, `PPN-IN`, `PPH23`, `PPH21`, `PB1`,
> saldo awal 1 September 2026). Bank: **Bank Operasional** (`1-110`). Bila tahap A–F berkas 02 sudah dijalankan, angka saldo akhir berbeda;
> karena itu setiap pemeriksaan di sini memakai **selisih terhadap saldo sebelum tahap dimulai**, bukan saldo mutlak. Catat saldo awal tiap akun yang disebut sebelum mulai.
>
> **Cara baca label hasil** (dipakai bila hasil tidak sesuai harapan): 🆕 fitur belum ada · 🔧 perbaikan kecil (fitur ada, kasus pinggiran belum ditangani) · ✅ regresi (sudah benar, dites supaya tidak mundur).
>
> **Aturan netralisasi:** setiap skenario yang membuat data uji ditutup dengan *Netralisasi* (Reverse jurnal terposting, Delete bila masih draft). Jurnal yang sudah
> terposting tidak bisa dihapus, hanya di-Reverse. Gunakan kode jurnal berawalan `JT-` supaya mudah dicari dan dibersihkan.

## Ringkasan Tahap

| # | Tahap | Isi |
| --- | --- | --- |
| AI | Jurnal Manual | 18 transaksi khas Ranahku (pendapatan diterima dimuka, voucher, termin, PPh 23, QRIS, pinjaman, prive, opname kas, kurs asing), negatif, approval, post, reverse, bulk |
| AJ | Buku Besar dan Neraca Saldo | Detail ledger, summary per akun, pemisahan per kegiatan usaha, biaya bersama, konsolidasi = jumlah unit |
| AK | Tutup Periode dan Tahun Buku | Penjaga tutup periode, kunci, buka kembali, tumpang tindih, celah, bulk, tutup tahun, pembukaan tahun berikutnya |
| AL | Laporan Keuangan | Neraca, Laba Rugi, Arus Kas konsolidasi dan per kegiatan, uji kewajaran |
| AM | Anggaran | Buat, negatif, realisasi vs anggaran, status, pembagian 12 bulan |
| AN | Aset Tetap dan Penyusutan | Garis lurus, saldo menurun, nilai residu, penyusutan terlambat, pelepasan |
| AO | Rekonsiliasi Bank | Cocok sempurna, empat jenis selisih, penjaga, multi rekening, penyelesaian QRIS |
| AP | Pajak | Rekap PPN masukan/keluaran, retur, PB1, PPh 21 dan PPh 23, pembayaran pajak |

---

## Transaksi Baku untuk Tahap AI (dipakai ulang di tahap berikutnya)

Semua tanggal September 2026. Kolom *Kegiatan* diisi pada baris pendapatan/beban yang relevan (kolom Business Unit pada baris jurnal).

| # | Peristiwa | Jurnal (Debit / Kredit) | Nominal | Pola asal |
| --- | --- | --- | ---: | --- |
| JT-01 | Modal tambahan pemilik | Dr `1-110` Bank Operasional / Cr `3-101` Modal Pemilik | 100.000.000 | accounting §1.1, kafe 1.13 |
| JT-02 | Bayar sewa ruko 12 bulan di muka | Dr `1-140` Sewa Ruko Dibayar Dimuka / Cr `1-110` | 36.000.000 | accounting §1.4 |
| JT-03 | Amortisasi sewa ruko bulan ini | Dr `6-103` Beban Sewa Ruko / Cr `1-140` | 3.000.000 | pendidikan 1.4 (amortisasi) |
| JT-04 | Sewa aplikasi tahunan Apotek diterima di muka (Paket Pro tahunan + PPN 11%) | Dr `1-110` 8.325.000 / Cr `2-140` Pendapatan Sewa Diterima Dimuka 7.500.000 (**SEWA**) / Cr `2-120` PPN Keluaran 825.000 | 8.325.000 | pendidikan uang pangkal, Nusatech 1.3 |
| JT-05 | Pengakuan sewa bulan pertama (1/12 dari 7.500.000) | Dr `2-140` 625.000 / Cr `4-101` Pendapatan Sewa Aplikasi 625.000 (**SEWA**) | 625.000 | Nusatech 1.3 |
| JT-06 | Penjualan tunai toko harian | Dr `1-102` Kas Toko 5.550.000 / Cr `4-201` 5.000.000 (**RETAIL**) / Cr `2-120` 550.000 | 5.550.000 | accounting §1.3 |
| JT-07 | Penjualan rumah makan harian dengan PB1 | Dr `1-103` Kas Rumah Makan 2.200.000 / Cr `4-301` 2.000.000 (**RESTO**) / Cr `2-121` Utang PB1 200.000 | 2.200.000 | hotel 1.3 (pajak daerah) |
| JT-08 | Beli persediaan toko kredit dengan PPN masukan | Dr `1-130` 10.000.000 / Dr `1-160` 1.100.000 / Cr `2-101` Utang Usaha 11.100.000 | 11.100.000 | accounting §1.9a |
| JT-09 | Bayar sebagian utang usaha | Dr `2-101` 5.000.000 / Cr `1-110` 5.000.000 | 5.000.000 | accounting §1.9b |
| JT-10 | Beban listrik, air, internet dibagi ke tiga kegiatan | Dr `6-104` 1.000.000 (**SEWA**) + 1.000.000 (**RETAIL**) + 1.000.000 (**RESTO**) / Cr `1-110` 3.000.000 | 3.000.000 | pendidikan 1.9, kafe 1.10 (biaya bersama) |
| JT-11 | Gaji dengan potongan PPh 21 | Dr `6-101` 20.000.000 / Cr `2-122` 500.000 / Cr `1-110` 19.500.000 | 20.000.000 | accounting §1.9j, pendidikan 1.5 |
| JT-12 | Setor PPh 21 ke kas negara | Dr `2-122` 500.000 / Cr `1-110` 500.000 | 500.000 | pendidikan 1.6 |
| JT-13 | Setor kas toko ke bank | Dr `1-110` 5.550.000 / Cr `1-102` 5.550.000 | 5.550.000 | accounting §1.9g, kafe 1.8 |
| JT-14 | Pinjaman bank | Dr `1-110` 50.000.000 / Cr `2-110` Utang Bank 50.000.000 | 50.000.000 | manufaktur 1.8 |
| JT-15 | Cicilan pertama: pokok 4.000.000 + bunga 500.000 | Dr `2-110` 4.000.000 / Dr `6-110` 500.000 / Cr `1-110` 4.500.000 | 4.500.000 | manufaktur 1.9, rumah sakit T15 |
| JT-16 | Biaya QRIS 0,7% atas penjualan nontunai 2.000.000 | Dr `6-109` Beban Administrasi Bank 14.000 / Cr `1-110` 14.000 | 14.000 | e-commerce 2 (biaya gateway) |
| JT-17a | Faktur sewa Distributor (badan usaha) | Dr `1-120` Piutang Sewa 8.325.000 / Cr `4-101` 7.500.000 (**SEWA**) / Cr `2-120` 825.000 | 8.325.000 | Nusatech 1.1 |
| JT-17b | Pelunasan faktur itu dengan pemotongan PPh 23 oleh pelanggan 2% × 7.500.000 | Dr `1-110` 8.175.000 / Dr `1-170` Uang Muka PPh 23 150.000 / Cr `1-120` 8.325.000 | 8.325.000 | Nusatech 6 (PPh 23) |
| JT-18 | Prive pemilik | Dr `3-101` 2.000.000 / Cr `1-110` 2.000.000 | 2.000.000 | accounting §1.9i |

**Perubahan saldo Bank Operasional yang harus terbaca setelah semua transaksi terposting:**
+100.000.000 − 36.000.000 + 8.325.000 − 5.000.000 − 3.000.000 − 19.500.000 − 500.000 + 5.550.000 + 50.000.000 − 4.500.000 − 14.000 + 8.175.000 − 2.000.000 = **+101.536.000**.

**Pendapatan September dari transaksi baku:** 625.000 + 5.000.000 + 2.000.000 + 7.500.000 = **15.125.000** (SEWA 8.125.000, RETAIL 5.000.000, RESTO 2.000.000).
**Beban September dari transaksi baku:** 3.000.000 + 3.000.000 + 20.000.000 + 500.000 + 14.000 = **26.514.000** (di luar selisih kas JT-19 di bawah).

---

## TAHAP AI — Jurnal Manual

Rujukan: manual `accounting` (bab jurnal) dan suite `accounting/01`. Halaman: **Accounting → Journals** (`/accounting/journals`).

### AI-A. Jalur sukses dan validasi dasar

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AI1 | Jurnal seimbang sederhana | Buat **JT-01** (Create Journal, Date 2026-09-02, dua baris) | Tersimpan; status Pending Review atau Draft sesuai pengaturan; kode otomatis disarankan | ⬜ |
| AI2 | Jurnal tidak seimbang | Ubah kredit JT-01 menjadi 90.000.000 | Tidak bisa disimpan sebagai jurnal seimbang; lencana *Unbalanced*; total debit ≠ kredit ditunjukkan | ⬜ |
| AI3 | Kurang dari dua baris | Hapus baris hingga tersisa satu | Tombol hapus baris nonaktif di baris terakhir; Save ditolak | ⬜ |
| AI4 | Akun atau kegiatan tidak ada | (Hanya via API) kirim `account_id` fiktif | Ditolak server dengan pesan validasi, bukan error 500 (catat sebagai 🔧 bila 500) | ⬜ |
| AI5 | Tiga baris dengan akun pajak | Buat **JT-04** (Cr `2-120` ber-flag pajak) | Kolom pajak dan tarif 11% terisi otomatis; di detail jurnal, centang **Show Taxes** lalu **Show Tax Detail** menampilkan rincian DPP dan PPN | ⬜ |
| AI6 | Pemisahan kegiatan | Buat **JT-06**, **JT-07**, **JT-10** dengan Business Unit pada baris | Setiap baris membawa kegiatannya; baris tanpa pilihan memakai kegiatan bawaan akun | ⬜ |
| AI7 | Jurnal beberapa kegiatan dalam satu transaksi | JT-10 (tiga baris beban berbeda kegiatan) | Satu jurnal, tiga kegiatan; total beban 3.000.000 | ⬜ |
| AI8 | Buat seluruh transaksi baku | Buat JT-02 sampai JT-18 | Semua tersimpan dengan nomor berurutan; tidak ada penolakan periode September | ⬜ |
| AI9 | Alokasi biaya bersama | Bandingkan JT-10 dengan aturan: beban dibagi rata ke tiga kegiatan | Laba rugi per kegiatan (AL) menanggung 1.000.000 listrik masing-masing | ⬜ |

### AI-B. Status, approval, post, reverse

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AI10 | Mode tanpa approval jurnal | Pada cabang tanpa `Requires Journal Approval`, buka detail jurnal berstatus Pending Review → **Post** | Modal konfirmasi; setelah Post terisi tanggal posting; tombol Post nonaktif; GL terbentuk | ⬜ |
| AI11 | Mode dengan approval jurnal | Nyalakan persetujuan jurnal di konfigurasi jurnal modul terkait (atau di akun uji), buat jurnal seimbang | Tombol **View Approval Request** muncul; **Post** dan **Edit** nonaktif selama menunggu | ⬜ |
| AI12 | Approval berjenjang | Login sebagai Manajer lalu Direktur, setujui bergantian | Hanya peran yang tercantum di langkah saat ini yang bisa bertindak; setelah semua langkah selesai jurnal terposting otomatis | ⬜ |
| AI13 | Bypass approval via API | Saat approval masih berjalan, panggil Post dan Update lewat API | Ditolak dengan pesan jelas; jurnal tidak berubah | ⬜ |
| AI14 | Tolak approval | **Reject** pada langkah pertama | Jurnal kembali ke status yang bisa diperbaiki atau dibatalkan; bukan terposting | ⬜ |
| AI15 | Post ganda | Panggil Post pada jurnal terposting (UI: tombol nonaktif; API: panggil) | Ditolak; tidak ada GL ganda | ⬜ |
| AI16 | Post ke periode tertutup | Setelah Tahap AK menutup satu periode: post jurnal bertanggal periode closed | Ditolak dengan pesan periode tertutup/terkunci | ⬜ |
| AI17 | Post-bulk | Centang beberapa jurnal draft, **Bulk Actions → Post Bulk Journals** | Hanya jurnal eligible diproses; ringkasan berhasil/gagal tampil; jurnal tak eligible dilewati tanpa membatalkan sisanya | ⬜ |
| AI18 | Reverse dasar | Reverse **JT-18** dengan Reversal Date 2026-09-30 dan alasan | Jurnal `REV-…` baru terposting dengan debit/kredit terbalik; jurnal asal berlabel *Reversed*; saldo Modal Pemilik dan Bank kembali | ⬜ |
| AI19 | Reverse draft | Coba Reverse jurnal yang belum terposting | Tombol nonaktif; API menolak | ⬜ |
| AI20 | Reverse ganda | Reverse jurnal yang sudah *Reversed* | Ditolak ("sudah di-reverse") | ⬜ |
| AI21 | Reverse dari reverse | Reverse jurnal `REV-…` hasil AI18 | Berhasil membentuk jurnal ketiga yang mengembalikan efek jurnal asal; saldo akhir = semula | ⬜ |
| AI22 | Recreate Journal | Pada jurnal berlabel Reversed klik **Recreate Journal** | Form Create Journal terisi dari jurnal asal; ubah nominal lalu simpan menghasilkan jurnal koreksi | ⬜ |
| AI23 | Create Bulk dan Edit Bulk | Buat tiga jurnal sekaligus (satu sengaja tidak seimbang); lalu Edit Bulk dua jurnal draft | Blok tak seimbang ditandai dan ditolak tanpa menyimpan blok lain; edit massal menyimpan perubahan yang valid | ⬜ |
| AI24 | Hapus draft | Delete jurnal yang belum terposting | Terhapus; jurnal terposting tidak bisa dihapus (hanya Reverse) | ⬜ |

### AI-C. Kasus lapangan khas (dari suite industri)

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AI25 | Pendapatan diterima dimuka tahunan | JT-04 lalu JT-05; ulangi JT-05 untuk Oktober (jurnal bertanggal Oktober bila periode ada) | `2-140` turun 625.000 per bulan sampai habis dalam 12 bulan; pendapatan hanya diakui bertahap | ⬜ |
| AI26 | Paket voucher prabayar (korporat) | Sewa aplikasi paket 5 pelanggan dibayar sekali: Dr Bank 3.330.000 / Cr `2-140` 3.000.000 / Cr `2-120` 330.000, lalu tiap pemakaian Dr `2-140` / Cr `4-101` | Saldo `2-140` mencerminkan sisa voucher belum terpakai | ⬜ |
| AI27 | Termin pendampingan implementasi | Kontrak pendampingan 3 tahap (30/40/30) senilai 1.500.000: tiap tahap faktur Dr `1-120` / Cr `4-102` + PPN; pelunasan terpisah | Pendapatan diakui sesuai tahap; piutang turun sesuai pelunasan; sisa tagihan benar | ⬜ |
| AI28 | Retensi pelanggan (analog retensi konstruksi) | Pelanggan menahan 5% dari faktur sampai serah terima: Dr Bank 95%, Dr `1-120` (retensi) 5% | Piutang retensi tetap tampil terpisah sampai dilunasi pada tanggal serah terima | ⬜ |
| AI29 | Selisih kas kasir | Opname kas toko menunjukkan kurang 50.000: Dr `6-190` atau akun beban yang dipilih / Cr `1-102` 50.000 (**JT-19**) | Saldo Kas Toko = catatan sistem − 50.000; 🔧 catat bahwa **tidak ada akun khusus selisih kas** di Bagan Akun Ranahku | ⬜ |
| AI30 | Selisih kas lebih | Opname menunjukkan lebih 20.000: Dr `1-102` / Cr `4-901` | Pendapatan Lain-lain bertambah | ⬜ |
| AI31 | Refund pelanggan atas sewa | Pelanggan membatalkan paket dalam masa uji: Dr `2-140` atau `4-101` + `2-120` / Cr Bank | Pendapatan dan PPN keluaran berkurang proporsional; jurnal balik rapi | ⬜ |
| AI32 | Biaya payment gateway | JT-16 | Beban administrasi bank 14.000; saldo bank mencerminkan penerimaan bersih | ⬜ |
| AI33 | Pelunasan dengan potongan PPh 23 | JT-17a lalu JT-17b | `1-170` bertambah 150.000; piutang `1-120` = 0 untuk faktur itu; PPh 23 muncul di laporan pajak | ⬜ |
| AI34 | Pinjaman dan cicilan | JT-14 dan JT-15 | `2-110` = 46.000.000 setelah cicilan pertama; beban bunga 500.000 masuk laba rugi, pokok tidak | ⬜ |
| AI35 | Pajak daerah restoran | JT-07, lalu setor PB1: Dr `2-121` 200.000 / Cr Bank | Utang PB1 nol setelah setor; PB1 tidak ikut rekap PPN | ⬜ |
| AI36 | Beban dengan mata uang asing (langganan cloud USD) | Buat jurnal USD 100 dengan kurs aktif 15.800: Dr `6-104` / Cr `2-101`; sebelumnya pastikan mata uang USD dan kurs aktif | Baris menyimpan jumlah asing dan jumlah IDR (1.580.000); GL dan Neraca Saldo tetap dalam IDR; tanpa kurs aktif jurnal ditolak | ⬜ |
| AI37 | Jurnal bertanggal masa depan | Buat satu jurnal bertanggal 2027-06-15 bila periode 2027 sudah ada | Dicatat apakah sistem mengizinkan, memberi peringatan, atau menolak (🆕 bila tidak ada kontrol sama sekali) | ⬜ |
| AI38 | Jurnal ke tanggal tanpa periode | Pilih tanggal di luar periode manapun | Ditolak di form dengan pesan "tidak ada periode"; pesan berbeda dari kasus periode tertutup | ⬜ |
| AI39 | Netralisasi | Reverse semua jurnal `JT-` yang tidak dipakai tahap berikutnya | Neraca Saldo kembali seimbang | ⬜ |

---

## TAHAP AJ — Buku Besar dan Neraca Saldo

Rujukan: suite `accounting/02`, `accounting-pos-retail`, suite per-kegiatan (kafe, pendidikan, e-commerce).

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AJ1 | Detail ledger Bank Operasional | **Accounting → General Ledger → Detail Ledger**, akun `1-110`, September | Saldo awal, setiap mutasi AK, saldo berjalan; saldo akhir − saldo awal = **+101.536.000** | ⬜ |
| AJ2 | Summary by Account | Rentang 1–30 September | Total debit, kredit, dan saldo tiap akun cocok dengan mutasi AK di tabel baku | ⬜ |
| AJ3 | Neraca Saldo (Trial Balance) | **Reports → Trial Balance** per 30 September | Total debit = total kredit; tidak ada akun bersaldo tidak wajar tanpa sebab (mis. piutang bersaldo kredit) | ⬜ |
| AJ4 | Dua endpoint neraca saldo | Bandingkan Trial Balance di Reports dan di General Ledger | Keduanya sengaja ada; angkanya sama pada rentang dan filter yang sama | ⬜ |
| AJ5 | Filter kegiatan SEWA | Summary by Account dengan filter Business Unit `SEWA` | Hanya baris bertag SEWA: pendapatan 8.125.000 dan listrik 1.000.000 | ⬜ |
| AJ6 | Filter kegiatan RETAIL | Filter `RETAIL` | Pendapatan 5.000.000 dan listrik 1.000.000 | ⬜ |
| AJ7 | Filter kegiatan RESTO | Filter `RESTO` | Pendapatan 2.000.000 dan listrik 1.000.000 | ⬜ |
| AJ8 | Konsolidasi = jumlah kegiatan | Jumlahkan hasil AJ5+AJ6+AJ7 untuk akun pendapatan dan akun `6-104`; bandingkan tanpa filter | Total tanpa filter = jumlah tiga kegiatan + baris tanpa kegiatan; selisih (baris tanpa kegiatan) dapat dijelaskan | ⬜ |
| AJ9 | Persediaan tanpa dimensi | Lihat `1-130` dengan filter kegiatan | Persediaan terpusat per akun; catat bila akun bertag RETAIL tampil tidak konsisten antar filter | ⬜ |
| AJ10 | Biaya bersama tanpa kegiatan | Buat jurnal beban tanpa Business Unit | Muncul sebagai "tanpa kegiatan" di rincian per kegiatan; konsolidasi tetap menghitungnya | ⬜ |
| AJ11 | Transfer antar kegiatan | Jurnal pindah dana Kas Rumah Makan ke Kas Toko: Dr `1-102` (RETAIL) / Cr `1-103` (RESTO) 1.000.000 | Saldo kas masing-masing kegiatan berubah; konsolidasi kas tidak berubah | ⬜ |
| AJ12 | Reverse tercermin di GL | Reverse JT-18 (dari AI18) | Detail ledger menampilkan baris asli dan baris pembalik; saldo akhir kembali | ⬜ |
| AJ13 | Ekspor | Ekspor Detail Ledger dan Trial Balance ke Excel dan PDF | Jumlah baris dan total sama dengan layar | ⬜ |

---

## TAHAP AK — Tutup Periode dan Tahun Buku

Rujukan: suite `accounting/03` dan `/09`, serta suite industri (kafe 3.1–3.11, pendidikan 3.1–3.9, retail tahun berjalan 04). **Kerjakan di Fiscal Year uji `FY-TEST` bila perlu menguji periode tumpang tindih, celah, dan guard tahun terakhir; jangan merusak FY2026 Ranahku yang dipakai berkas lain.**

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AK1 | Tutup periode dengan jurnal draft | Buat satu jurnal draft bertanggal September; **Close Period** September | Ditolak; pesan menyebut jurnal belum terposting | ⬜ |
| AK2 | Tutup periode sukses | Posting/hapus semua draft; **Close Period** Agustus (periode sebelum September) | Badge **Closed**; jurnal baru bertanggal Agustus ditolak | ⬜ |
| AK3 | Guard periode berikutnya wajib ada dan terbuka | Di `FY-TEST` dengan satu periode saja, coba Close; lalu tutup Maret sebelum Februari | Ditolak bila periode berikutnya tidak ada atau sudah tertutup; menutup periode terakhir tahun buku tanpa tahun berikutnya diizinkan | ⬜ |
| AK4 | Tutup periode yang menaungi hari ini | Close periode bulan berjalan (di FY-TEST) | Sah secara data; indikator periode aktif di sidebar menampilkan peringatan "periode berjalan tertutup"; posting jurnal hari ini ditolak | ⬜ |
| AK5 | Kunci periode | **Lock Period** pada periode tertutup | Hanya periode Closed yang bisa dikunci (opsi nonaktif dengan alasan pada periode terbuka); posting ke periode terkunci ditolak | ⬜ |
| AK6 | Reverse jurnal pada periode tertutup | Reverse jurnal terposting bertanggal periode yang sudah Closed | Dicatat perilaku sebenarnya: bila berhasil menghapus/mengubah GL periode tertutup → 🔧 pelanggaran prinsip "periode tertutup tidak berubah"; hasil yang benar adalah jurnal pembalik bertanggal periode terbuka | ⬜ |
| AK7 | Buka kembali periode | **Reopen Period** pada periode Closed (bukan Locked) | Berhasil; periode Locked harus dibuka kunci dahulu atau ditolak dengan alasan | ⬜ |
| AK8 | Periode tumpang tindih | Di `FY-TEST` buat dua periode dengan rentang bertumpuk (1–31 Jan dan 15 Jan–14 Feb) | Dicatat apakah form menolak; bila diterima → 🔧/🆕 (tidak ada batasan basis data); periode aktif yang tampil harus deterministik | ⬜ |
| AK9 | Celah periode | Di tahun uji yang hanya punya Januari, buat jurnal bertanggal Maret | Ditolak dengan pesan khusus "tidak ada periode untuk tanggal ini" (bukan "periode tertutup") | ⬜ |
| AK10 | Aksi massal campuran | Centang tiga periode (satu terbuka, satu tertutup, satu terkunci) → **Bulk Actions → Close Period** | Hanya yang eligible diproses; yang lain dilewati dengan ringkasan; dua periode berurutan terbuka dalam satu batch diuji urutan eksekusinya | ⬜ |
| AK11 | Penyusutan terlambat setelah periode tertutup | Tutup Agustus; coba jalankan penyusutan Agustus | Ditolak karena periode tertutup, atau dijurnal ke periode terbuka berikutnya dengan penjelasan | ⬜ |
| AK12 | Dashboard periode | Setelah AK2 buka dashboard Akuntansi | Label periode memakai periode aktif yang berisi transaksi, bukan 0/0/0; angka laba bersih cocok dengan Laba Rugi periode yang sama | ⬜ |
| AK13 | Tutup tahun: periode belum semua tertutup | **Close Fiscal Year** FY-TEST saat masih ada periode terbuka | Ditolak | ⬜ |
| AK14 | Tutup tahun: tidak ada akun Laba Ditahan | Matikan flag Laba Ditahan pada `3-102` lalu coba | Ditolak; pesan menyebut harus tepat satu akun | ⬜ |
| AK15 | Tutup tahun: lebih dari satu akun Laba Ditahan | Aktifkan flag pada `3-101` juga | Ditolak; kembalikan flag setelahnya | ⬜ |
| AK16 | Tutup tahun sukses (FY-TEST dengan data) | Isi FY-TEST dengan pendapatan dan beban; tutup semua periode; **Close Fiscal Year** | Jurnal penutup `CLOSE-…` mengosongkan semua akun pendapatan dan beban; selisihnya masuk `3-102`; laba bersih di jurnal = laba bersih Laba Rugi | ⬜ |
| AK17 | Tutup tahun dua kali | Coba lagi | Opsi nonaktif ("sudah ditutup") | ⬜ |
| AK18 | Buka kembali tahun buku | Aktifkan setup izin pembalikan jurnal penutup lalu **Reopen Year** | Jurnal penutup dibalik, periode dibuka, saldo akun P&L kembali; tanpa izin setup ditolak; tahun yang lebih baru sudah tertutup → ditolak | ⬜ |
| AK19 | Pembukaan tahun berikutnya | Setelah AK16 buat Fiscal Year berikutnya dan generate periode | Saldo neraca (aset, kewajiban, modal) terbawa; akun P&L mulai nol; saldo awal tahun baru = saldo akhir tahun lama | ⬜ |
| AK20 | Dua tahun buku berjalan (pola retail tahun berjalan) | Isi satu jurnal di FY-TEST lama dan satu di tahun baru | Laporan per tanggal memilih periode yang tepat; Neraca per akhir tahun lama tidak berubah oleh transaksi tahun baru | ⬜ |

---

## TAHAP AL — Laporan Keuangan

Rujukan: suite `accounting/04`, suite industri bab 04 (konsolidasi dan per kegiatan). Rentang: 1–30 September 2026.

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AL1 | Laba Rugi konsolidasi | **Reports → Income Statement**, September | Pendapatan transaksi baku **15.125.000** (+ transaksi operasional berkas 02 bila sudah dijalankan); beban transaksi baku 26.514.000 (+ JT-19 bila diposting); laba bersih = pendapatan − HPP − beban | ⬜ |
| AL2 | Laba Rugi per kegiatan | Jalankan dengan filter `SEWA`, `RETAIL`, `RESTO` | Pendapatan SEWA 8.125.000, RETAIL 5.000.000, RESTO 2.000.000; listrik 1.000.000 per kegiatan; jumlah tiga kegiatan = konsolidasi untuk baris bertag | ⬜ |
| AL3 | Neraca | **Reports → Balance Sheet**, as of 30 September | Total aset = total kewajiban + modal; laba berjalan di ekuitas = laba bersih Laba Rugi periode yang sama | ⬜ |
| AL4 | Neraca setelah tutup tahun uji | Pada FY-TEST setelah AK16 | Laba berjalan nol dan tertampung di Laba Ditahan; total tidak berubah | ⬜ |
| AL5 | Arus Kas | **Reports → Cash Flow Statement** September (metode langsung) | Arus operasi, investasi, pendanaan terklasifikasi (pinjaman JT-14 dan modal JT-01 = pendanaan); saldo kas akhir = Kas Kecil + Kas Toko + Kas Rumah Makan + Bank dari Neraca | ⬜ |
| AL6 | Neraca Saldo historis | Trial Balance per 1 September dan 30 September | Saldo awal September = saldo awal berkas 01; selisih per akun = mutasi September | ⬜ |
| AL7 | Uji kewajaran | Hitung: rasio kas toko terhadap transaksi tunai, HPP toko ÷ pendapatan toko, beban gaji ÷ pendapatan | Angka masuk akal untuk skenario (tidak ada HPP negatif atau pendapatan nol saat ada penjualan) | ⬜ |
| AL8 | Konsistensi antar laporan | Bandingkan laba bersih dashboard, Income Statement, dan perubahan ekuitas di Balance Sheet | Ketiganya identik | ⬜ |
| AL9 | Ekspor | Ekspor tiga laporan ke Excel/PDF | Angka dan format sama dengan layar; judul dan periode benar | ⬜ |

---

## TAHAP AM — Anggaran

Rujukan: suite `accounting/05` dan `/09 §9.10`, anggaran suite industri. Halaman: **Accounting → Budgets**.

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AM1 | Buat anggaran | Fiscal Year 2026 (atau tahun uji), Name "Anggaran Operasional 2026", tiga baris: `6-104` per kegiatan untuk September @ 1.200.000 | Tersimpan Draft; header dan tiga baris | ⬜ |
| AM2 | Fiscal year kosong | Kosongkan Fiscal Year lalu Save | Ditolak dengan pesan validasi | ⬜ |
| AM3 | Baris kembar | Dua baris dengan akun + kegiatan + periode sama | Ditolak | ⬜ |
| AM4 | Jumlah negatif | Budgeted Amount negatif | Ditolak | ⬜ |
| AM5 | Periode tahun tertutup | Buka pilihan periode pada tahun yang sudah tertutup | Dicatat apakah periode tertutup muncul sebagai pilihan (🔧 bila anggaran bisa dibuat ke periode yang sudah ditutup) | ⬜ |
| AM6 | Realisasi untuk uji | Pastikan JT-10 sudah terposting (realisasi 1.000.000 per kegiatan) dan buat satu beban lebih besar untuk RETAIL (mis. listrik tambahan 400.000) | Realisasi RETAIL = 1.400.000 | ⬜ |
| AM7 | Budget vs Actual | Detail anggaran → kartu **Budget vs Actual** → **Run Report** | Varians per baris benar: SEWA 200.000 sisa, RETAIL −200.000 (melebihi), RESTO 200.000 sisa; persentase benar | ⬜ |
| AM8 | Pemisahan per kegiatan | Bandingkan baris per kegiatan | Realisasi tiap kegiatan terpisah | ⬜ |
| AM9 | Status | Draft → **Activate** → **Close** | Setiap transisi sah; baris tak bisa diubah setelah aktif; anggaran aktif yang semua barisnya satu periode tertutup otomatis ikut tertutup saat periode terakhir ditutup | ⬜ |
| AM10 | Pembagian tahunan tidak habis dibagi 12 | Rencana tahunan Rp 100.000.000 ke 12 bulan | Dicatat bahwa tidak ada fitur "bagi rata 12 bulan" (🆕); pengisian manual 12 baris, sisa pembulatan masuk bulan terakhir secara manual | ⬜ |
| AM11 | Hapus anggaran | Delete anggaran Draft; coba Delete anggaran Aktif | Draft terhapus; yang aktif ditolak | ⬜ |

---

## TAHAP AN — Aset Tetap dan Penyusutan

Rujukan: suite `accounting/06` dan `/09 §9.9`, konstruksi (alat berat), kafe (garis lurus dan saldo menurun), manufaktur (mesin). Data uji: tiga aset Ranahku.

| # | Aset | Perolehan | Metode | Umur | Residu |
| --- | --- | --- | --- | --- | ---: |
| 1 | Laptop Admin (`1-201`) | 12.000.000 pada 2026-09-01 | Garis lurus | 48 bulan | 0 |
| 2 | Etalase Toko (`1-203`) | 6.000.000 | Garis lurus | 60 bulan | 0 |
| 3 | Motor Operasional Kanvasing (`1-202`) | 24.000.000 | Saldo menurun | 48 bulan | 4.000.000 |

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AN1 | Registrasi tiga aset | **Fixed Assets → Assets → Create Asset** | Tersimpan; tanpa akun akumulasi penyusutan terpetakan muncul peringatan bahwa akun penyusutan belum diatur | ⬜ |
| AN2 | Masa manfaat tidak valid | Isi 0 atau negatif | Ditolak | ⬜ |
| AN3 | Hubungkan akun lewat Edit | Edit aset: akun aset, akumulasi penyusutan `1-209`, beban `6-106` | Tersimpan; peringatan hilang | ⬜ |
| AN4 | Penyusutan garis lurus | **Run Depreciation** Laptop September | Beban = 12.000.000 ÷ 48 = **250.000**; Etalase 6.000.000 ÷ 60 = **100.000**; jurnal Dr `6-106` / Cr `1-209` seimbang dan masuk GL | ⬜ |
| AN5 | Penyusutan saldo menurun | Motor: jalankan September lalu Oktober | Beban bulan kedua lebih kecil dari bulan pertama; dihitung dari nilai buku berjalan | ⬜ |
| AN6 | Penyusutan ganda | Jalankan lagi untuk bulan yang sama | Ditolak | ⬜ |
| AN7 | Nilai buku tidak di bawah residu | Jalankan penyusutan Motor berturut-turut sampai masa manfaat habis (periode uji) | Nilai buku akhir ≥ 4.000.000; bulan terakhir dibatasi sehingga tidak melewati residu (🔧 bila lewat) | ⬜ |
| AN8 | Verifikasi neraca | Neraca setelah AN4–AN5 | Akumulasi Penyusutan bersaldo kredit sebesar total beban; Aset Tetap bersih = perolehan − akumulasi | ⬜ |
| AN9 | Laba rugi | Income Statement September | Beban Penyusutan = jumlah AN4 (350.000 untuk dua aset garis lurus) ditambah beban bulan pertama Motor | ⬜ |
| AN10 | Penyusutan terlambat | Tutup periode lalu coba jalankan untuk periode itu (lihat AK11) | Ditolak atau dijurnal ke periode terbuka | ⬜ |
| AN11 | Pelepasan aset (jual) | **Dispose Asset** Etalase: metode Sale, hasil jual 5.000.000 | Jurnal: Dr Bank 5.000.000, Dr Akumulasi, Cr Aset; selisih ke laba/rugi pelepasan; nilai buku nol; status Disposed | ⬜ |
| AN12 | Pelepasan karena rusak | Dispose Motor sebelum umur habis dengan hasil 0 | Rugi pelepasan = nilai buku saat itu | ⬜ |
| AN13 | Hapus aset berriwayat | Delete aset yang sudah punya penyusutan | Ditolak; hanya aset tanpa riwayat yang bisa dihapus | ⬜ |
| AN14 | Aset yang sudah dilepas | Coba edit/penyusutan setelah Disposed | Ditolak | ⬜ |

---

## TAHAP AO — Rekonsiliasi Bank

Rujukan: suite `accounting/07`, kafe 06 (selisih setoran kasir), pendidikan 06 (guard complete), e-commerce 06 (payment gateway), NGO 06 (multi rekening). Halaman: **Finance → Bank Accounts**, **Bank Reconciliations**.

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AO1 | Rekening bank | Buat **Bank Operasional** (Bank Name, nomor rekening, akun `1-110`) dan satu rekening **Penampungan QRIS** | Akun COA wajib bertanda akun kas; memilih akun non-kas ditolak | ⬜ |
| AO2 | Cocok sempurna | Reconciliation September: Closing Balance dari rekening koran fiktif = saldo buku `1-110` | Selisih nol; **Complete** menyelesaikan; status berubah | ⬜ |
| AO3 | Biaya admin bank belum dicatat | Rekening koran lebih kecil 14.000 dari buku | Selisih 14.000 terdeteksi; buat jurnal penyesuaian (Dr `6-109` / Cr `1-110`), perbarui Closing Balance, Complete | ⬜ |
| AO4 | Setoran dalam perjalanan | Setor kas toko 5.550.000 di akhir bulan, belum di rekening koran | Selisih = setoran dalam perjalanan; dicatat sebagai uncleared, bukan kesalahan | ⬜ |
| AO5 | Transfer keluar belum cair | Bayar pemasok 5.000.000 yang belum muncul di bank | Selisih = outstanding transfer | ⬜ |
| AO6 | Kesalahan input nominal | Jurnal bank dicatat 8.175.000 padahal di bank 8.157.000 | Selisih 18.000 terdeteksi; perbaiki lewat Reverse + jurnal baru | ⬜ |
| AO7 | Complete saat masih selisih | Klik Complete dengan selisih belum dijelaskan | Ditolak atau memberi peringatan tegas (catat perilaku) | ⬜ |
| AO8 | Guard setelah selesai | Update atau Delete reconciliation berstatus Completed | Ditolak; hanya Draft yang bisa diubah atau dihapus | ⬜ |
| AO9 | Multi rekening | Dua reconciliation berbeda untuk dua rekening pada periode sama | Saling independen; saldo tiap rekening cocok dengan akun COA masing-masing | ⬜ |
| AO10 | Penyelesaian payment gateway | Jurnal penjualan nontunai 2.000.000 ke akun penampung; penyelesaian ke bank T+1 dikurangi biaya 14.000 | Reconciliation penampung selisih nol setelah pelunasan; akun penampung nol | ⬜ |
| AO11 | Setoran kasir dengan selisih | Kas toko dihitung 5.500.000, disetor 5.500.000 padahal sistem 5.550.000 | Selisih 50.000 tercatat (lihat AI29); setoran bank cocok dengan jumlah yang disetor | ⬜ |

---

## TAHAP AP — Pajak

Rujukan: suite `accounting/08`, rumah sakit dan klinik (pajak mixed), hotel (pajak daerah), Nusatech 6 (PPN dan PPh 23).

| # | Skenario | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| AP1 | Rekap PPN minimal | **Reports → Tax Summary**, September, hanya JT-06 dan JT-08 yang ada | PPN Keluaran 550.000 dan PPN Masukan 1.100.000; kurang/lebih bayar benar tandanya | ⬜ |
| AP2 | Rekap PPN lengkap | Dengan seluruh transaksi baku | **PPN Keluaran 2.200.000** (825.000 + 550.000 + 825.000), **PPN Masukan 1.100.000**; selisih 1.100.000 harus disetor | ⬜ |
| AP3 | Klasifikasi otomatis | Lihat tabel masukan dan keluaran | Akun, nama pajak, dan tarif terklasifikasi benar; PB1 **tidak** masuk rekap PPN | ⬜ |
| AP4 | Retur mengurangi | Retur pembelian dengan PPN dan retur penjualan dengan PPN | PPN Masukan dan Keluaran **berkurang** proporsional (regresi bug lama retur menambah) | ⬜ |
| AP5 | Periode tanpa transaksi | Rentang tanpa transaksi berpajak | Hasil kosong dengan pesan jelas, tanpa error | ⬜ |
| AP6 | Setor PPN | Jurnal Dr `2-120` 2.200.000 / Cr `1-160` 1.100.000 / Cr Bank 1.100.000 | Kedua akun PPN nol setelah setor; rekap periode berikutnya mulai dari nol | ⬜ |
| AP7 | Setor PB1 dan PPh 21 | AI35 dan JT-12 | Utang tiap pajak nol setelah setor | ⬜ |
| AP8 | Uang muka PPh 23 | Lihat `1-170` setelah JT-17b | 150.000 sebagai kredit pajak; saldo muncul di Neraca sebagai aset lancar | ⬜ |
| AP9 | Pajak pada dokumen operasional | Bandingkan rekap PPN dengan jumlah PPN pada faktur penjualan dan pembelian di berkas 02 | Selisih nol (jurnal otomatis dan jurnal manual berkontribusi sama pada rekap) | ⬜ |

---

## Daftar Periksa Cepat

- [ ] AI1–AI39 jurnal manual
- [ ] AJ1–AJ13 buku besar dan neraca saldo
- [ ] AK1–AK20 periode dan tahun buku
- [ ] AL1–AL9 laporan keuangan
- [ ] AM1–AM11 anggaran
- [ ] AN1–AN14 aset tetap
- [ ] AO1–AO11 rekonsiliasi bank
- [ ] AP1–AP9 pajak
- [ ] Semua jurnal `JT-` yang tidak dipakai berkas lain sudah dinetralkan
