---
title: (Klinik Gigi) — 01. Jurnal Manual & Transaksi Harian Klinik
category: accounting-klinik-gigi
description: 20 transaksi jurnal manual bernilai kecil-kecil (tindakan pasien, komisi dokter, kas kecil, BPJS, BHP) tersebar 4 minggu pertama FY2026 — didesain sebagai alat uji akurasi akumulasi angka. Total debit=kredit dihitung manual per transaksi DAN akumulasi akhir, harus cocok persis dengan Trial Balance file 02.
visibility: internal
---

# 01. Jurnal Manual & Transaksi Harian Klinik

> Prasyarat: file [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) sudah selesai — Modal Pemilik (3101) harus sudah **181.350.000** sebelum mulai file ini.
>
> **Cara pakai file ini**: setiap transaksi (T1-T20) adalah 1 pemanggilan `POST accounting/journals/create` (bisa multi-baris dalam 1 jurnal) diikuti `POST accounting/journals/post` (asumsi `require_journal_approval` OFF — approval workflow generik sudah dites di suite retail file 01, tidak diulang di sini). Isi `date` sesuai kolom Tanggal, `business_unit_id` sesuai kolom Cabang (kosongkan kalau tidak berlaku ke 1 cabang spesifik). Setiap baris jurnal WAJIB `debit + credit` per transaksi balance — dicek ulang manual di tabel masing-masing.
>
> **Kenapa banyak transaksi kecil**: ini SENGAJA — total akumulasi 20 transaksi di file ini dihitung manual sampai ke rupiah terakhir di §Rekonsiliasi Akhir. Kalau hasil **General Ledger — `trial-balance`** di file 02 BERBEDA dari angka di §Rekonsiliasi Akhir walau cuma selisih Rp1, itu indikasi kuat ada bug pembulatan/rounding atau baris jurnal yang salah posting — laporkan sebagai temuan prioritas tinggi.

## Minggu 1 (2026-01-01 s/d 2026-01-07)

### T1 — Tindakan Gigi Umum tunai, harian gabungan (Kelapa Gading, 2026-01-02)

| Baris | Akun                           |   Debit |  Kredit |
| ----- | ------------------------------ | ------: | ------: |
| 1     | 1101 Kas Kecil Klinik          | 750.000 |         |
| 2     | 4101 Pendapatan Jasa Gigi Umum |         | 750.000 |
| 3     | 5101 Beban Komisi Dokter (40%) | 300.000 |         |
| 4     | 2103 Utang Komisi Dokter       |         | 300.000 |
| 5     | 5102 Beban BHP Gigi            |  45.000 |         |
| 6     | 1104 Persediaan BHP Gigi       |         |  45.000 |

Total Debit = 1.095.000, Total Kredit = 1.095.000 ✓ balanced. `business_unit_id`: KG.

| Skenario | Detail                                                | Hasil                                             |
| -------- | ----------------------------------------------------- | ------------------------------------------------- |
| Positif  | Create + post jurnal 6 baris di atas                  | 201 create, 200 post, status `JRN_POSTED`         |
| Negatif  | Coba post ulang jurnal yang SAMA (sudah `JRN_POSTED`) | Ditolak — sudah posted, tidak boleh post dua kali |

### T2 — Tindakan BPJS (klaim), (BSD, 2026-01-03)

Cabut gigi + perawatan akar gigi, klaim BPJS Rp1.200.000 (piutang, belum cair).

| Baris | Akun                                      |     Debit |    Kredit |
| ----- | ----------------------------------------- | --------: | --------: |
| 1     | 1103 Piutang Pasien BPJS/Asuransi         | 1.200.000 |           |
| 2     | 4101 Pendapatan Jasa Gigi Umum            |           | 1.200.000 |
| 3     | 5101 Beban Komisi Dokter (30% klaim BPJS) |   360.000 |           |
| 4     | 2103 Utang Komisi Dokter                  |           |   360.000 |
| 5     | 5102 Beban BHP Gigi                       |    80.000 |           |
| 6     | 1104 Persediaan BHP Gigi                  |           |    80.000 |

Total Debit = 1.640.000, Total Kredit = 1.640.000 ✓. `business_unit_id`: BSD.

**Catatan komisi berbeda per jalur pembayaran (kasus khas klinik gigi)**: komisi tindakan BPJS (30%) LEBIH RENDAH dari tunai (40%) karena tarif reimbursement BPJS lebih rendah dari tarif normal — ini keputusan bisnis klinik, bukan aturan sistem; sistem sendiri tidak tahu "ini BPJS jadi komisi harus X%", angka `debit`/`credit` tetap manual dihitung staf lalu diinput. Dicatat di sini supaya jelas kenapa persentase komisi bervariasi antar transaksi di file ini (bukan salah ketik).

### T3 — Ortodonti DP pasien baru (Bekasi, 2026-01-05)

DP behel tunai Rp2.500.000, komisi dokter ortodonti 25%.

| Baris | Akun                           |     Debit |    Kredit |
| ----- | ------------------------------ | --------: | --------: |
| 1     | 1101 Kas Kecil Klinik          | 2.500.000 |           |
| 2     | 4102 Pendapatan Jasa Ortodonti |           | 2.500.000 |
| 3     | 5101 Beban Komisi Dokter (25%) |   625.000 |           |
| 4     | 2103 Utang Komisi Dokter       |           |   625.000 |

Total Debit = 3.125.000, Total Kredit = 3.125.000 ✓. `business_unit_id`: BKS.

### T4 — Penjualan produk ritel kena PPN (Kelapa Gading, 2026-01-06)

Pasta gigi & mouthwash, harga jual **termasuk PPN 11%**: harga dasar 300.000 + PPN 33.000 = total tunai 333.000.

| Baris | Akun                                   |   Debit |  Kredit |
| ----- | -------------------------------------- | ------: | ------: |
| 1     | 1101 Kas Kecil Klinik                  | 333.000 |         |
| 2     | 4104 Pendapatan Penjualan Produk Ritel |         | 300.000 |
| 3     | 2102 PPN Keluaran                      |         |  33.000 |

Total Debit = 333.000, Total Kredit = 333.000 ✓. `business_unit_id`: KG. TIDAK ada baris komisi dokter (produk ritel dijual resepsionis, bukan tindakan dokter).

| Skenario | Detail                                                                             | Hasil                                                                                                                                                               |
| -------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | Create + post — **satu-satunya transaksi di file ini yang menyentuh PPN Keluaran** | Verifikasi ulang di file `06-rekonsiliasi-bank-dan-ppn.id.md` bahwa PPN Keluaran akumulasi HANYA dari transaksi ini (33.000), tidak tercampur pendapatan jasa medis |

### T5 — Setor kas kecil ke bank (Kelapa Gading, 2026-01-07)

| Baris | Akun                      |     Debit |    Kredit |
| ----- | ------------------------- | --------: | --------: |
| 1     | 1102 Bank BCA Operasional | 2.000.000 |           |
| 2     | 1101 Kas Kecil Klinik     |           | 2.000.000 |

Total Debit = 2.000.000, Total Kredit = 2.000.000 ✓.

## Minggu 2 (2026-01-08 s/d 2026-01-14)

### T6 — Pembelian BHP gigi kredit dari supplier (Kelapa Gading, pembelian pusat, 2026-01-09)

Harga barang 5.000.000 + PPN Masukan 11% (550.000) = utang dagang 5.550.000.

| Baris | Akun                                    |     Debit |    Kredit |
| ----- | --------------------------------------- | --------: | --------: |
| 1     | 1104 Persediaan BHP Gigi                | 5.000.000 |           |
| 2     | 1105 PPN Masukan                        |   550.000 |           |
| 3     | 2101 Utang Dagang — Supplier Bahan Gigi |           | 5.550.000 |

Total Debit = 5.550.000, Total Kredit = 5.550.000 ✓.

### T7 — Pembayaran komisi dokter Minggu 1 (2026-01-10)

Total akrual komisi Minggu 1 = T1 300.000 + T2 360.000 + T3 625.000 = **1.285.000**, dibayar penuh dari Bank BCA.

| Baris | Akun                      |     Debit |    Kredit |
| ----- | ------------------------- | --------: | --------: |
| 1     | 2103 Utang Komisi Dokter  | 1.285.000 |           |
| 2     | 1102 Bank BCA Operasional |           | 1.285.000 |

Total Debit = 1.285.000, Total Kredit = 1.285.000 ✓.

| Skenario | Detail                                                                                                                     | Hasil                                                                                                                                                                                                                                                                                                                                                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Negatif  | Coba bayar komisi lebih besar dari saldo akrual (mis. 2.000.000 padahal akrual cuma 1.285.000) sebagai jurnal manual biasa | Sistem TIDAK menolak (jurnal manual bebas isi angka apapun selama balance debit=kredit — tidak ada validasi silang ke saldo 2103 saat ini) — catat sebagai keterbatasan desain: kontrol saldo minus akun liability HARUS dijaga manual oleh staf, bukan oleh sistem. Belum diverifikasi ke kode apakah ada guard tersembunyi, laporkan kalau ternyata ditolak (temuan positif tak terduga) |

### T8 — Tindakan Estetika Gigi (Whitening), (BSD, 2026-01-11)

| Baris | Akun                               |     Debit |    Kredit |
| ----- | ---------------------------------- | --------: | --------: |
| 1     | 1101 Kas Kecil Klinik              | 1.800.000 |           |
| 2     | 4103 Pendapatan Jasa Estetika Gigi |           | 1.800.000 |
| 3     | 5101 Beban Komisi Dokter (35%)     |   630.000 |           |
| 4     | 2103 Utang Komisi Dokter           |           |   630.000 |
| 5     | 5102 Beban BHP Gigi                |    60.000 |           |
| 6     | 1104 Persediaan BHP Gigi           |           |    60.000 |

Total Debit = 2.490.000, Total Kredit = 2.490.000 ✓. `business_unit_id`: BSD.

### T9 — Pelunasan piutang BPJS PARSIAL (2026-01-12)

Klaim T2 (1.200.000) cair sebagian dari BPJS ke Bank BCA — **hanya 1.000.000 cair**, sisa 200.000 tetap piutang (masih proses verifikasi berkas, khas pola pencairan BPJS).

| Baris | Akun                              |     Debit |    Kredit |
| ----- | --------------------------------- | --------: | --------: |
| 1     | 1102 Bank BCA Operasional         | 1.000.000 |           |
| 2     | 1103 Piutang Pasien BPJS/Asuransi |           | 1.000.000 |

Total Debit = 1.000.000, Total Kredit = 1.000.000 ✓.

| Skenario                                                              | Detail                                                                                                               | Hasil                                                                                                                          |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Positif — pelunasan parsial (kasus khas jasa, beda dari 2 suite lain) | Setelah T9, saldo 1103 tidak nol — masih ada 200.000 piutang tersisa dari klaim T2, PLUS 680.000 dari T14 (Minggu 3) | Verifikasi saldo akhir 1103 di §Rekonsiliasi Akhir & file 02 mencerminkan sisa piutang yang BENAR (bukan dianggap lunas semua) |

### T10 — Opname kas kasir harian, selisih kurang (Bekasi, 2026-01-13)

Kas fisik kasir Bekasi kurang Rp15.000 dari catatan pembukuan (kembalian salah/uang hilang kecil).

| Baris | Akun                                |  Debit | Kredit |
| ----- | ----------------------------------- | -----: | -----: |
| 1     | 5206 Beban Selisih Kas Kasir Harian | 15.000 |        |
| 2     | 1101 Kas Kecil Klinik               |        | 15.000 |

Total Debit = 15.000, Total Kredit = 15.000 ✓. `business_unit_id`: BKS.

## Minggu 3 (2026-01-15 s/d 2026-01-21)

### T11 — Gaji karyawan non-dokter (resepsionis & perawat, gabungan 3 cabang), (2026-01-16)

Gaji bruto 9.000.000, potongan PPh 21 sebesar 450.000, dibayar bersih dari Bank BCA.

| Baris | Akun                                |     Debit |    Kredit |
| ----- | ----------------------------------- | --------: | --------: |
| 1     | 5202 Beban Gaji Karyawan Non-Dokter | 9.000.000 |           |
| 2     | 2104 Utang PPh 21 Karyawan          |           |   450.000 |
| 3     | 1102 Bank BCA Operasional           |           | 8.550.000 |

Total Debit = 9.000.000, Total Kredit = 9.000.000 (450.000 + 8.550.000) ✓.

### T12 — Sewa klinik BSD bulanan (2026-01-17)

| Baris | Akun                      |     Debit |    Kredit |
| ----- | ------------------------- | --------: | --------: |
| 1     | 5201 Beban Sewa Klinik    | 6.000.000 |           |
| 2     | 1102 Bank BCA Operasional |           | 6.000.000 |

Total Debit = 6.000.000, Total Kredit = 6.000.000 ✓. `business_unit_id`: BSD.

### T13 — Tindakan Gigi Umum tunai, harian gabungan (Kelapa Gading, 2026-01-19)

| Baris | Akun                           |   Debit |  Kredit |
| ----- | ------------------------------ | ------: | ------: |
| 1     | 1101 Kas Kecil Klinik          | 920.000 |         |
| 2     | 4101 Pendapatan Jasa Gigi Umum |         | 920.000 |
| 3     | 5101 Beban Komisi Dokter (40%) | 368.000 |         |
| 4     | 2103 Utang Komisi Dokter       |         | 368.000 |
| 5     | 5102 Beban BHP Gigi            |  55.000 |         |
| 6     | 1104 Persediaan BHP Gigi       |         |  55.000 |

Total Debit = 1.343.000, Total Kredit = 1.343.000 ✓.

### T14 — Tindakan BPJS (klaim), (BSD, 2026-01-20)

| Baris | Akun                              |   Debit |  Kredit |
| ----- | --------------------------------- | ------: | ------: |
| 1     | 1103 Piutang Pasien BPJS/Asuransi | 680.000 |         |
| 2     | 4101 Pendapatan Jasa Gigi Umum    |         | 680.000 |
| 3     | 5101 Beban Komisi Dokter (30%)    | 204.000 |         |
| 4     | 2103 Utang Komisi Dokter          |         | 204.000 |
| 5     | 5102 Beban BHP Gigi               |  40.000 |         |
| 6     | 1104 Persediaan BHP Gigi          |         |  40.000 |

Total Debit = 924.000, Total Kredit = 924.000 ✓.

### T15 — Listrik & air gabungan 3 cabang (2026-01-21)

| Baris | Akun                      |     Debit |    Kredit |
| ----- | ------------------------- | --------: | --------: |
| 1     | 5203 Beban Listrik & Air  | 2.750.000 |           |
| 2     | 1102 Bank BCA Operasional |           | 2.750.000 |

Total Debit = 2.750.000, Total Kredit = 2.750.000 ✓.

## Minggu 4 (2026-01-22 s/d 2026-01-28)

### T16 — Pembayaran komisi dokter Minggu 2 & 3 (2026-01-22)

Akrual belum dibayar: T8 630.000 + T13 368.000 + T14 204.000 = **1.202.000**.

| Baris | Akun                      |     Debit |    Kredit |
| ----- | ------------------------- | --------: | --------: |
| 1     | 2103 Utang Komisi Dokter  | 1.202.000 |           |
| 2     | 1102 Bank BCA Operasional |           | 1.202.000 |

Total Debit = 1.202.000, Total Kredit = 1.202.000 ✓.

**Verifikasi akun 2103 kembali ke saldo awal**: total akrual komisi selama 4 minggu (T1+T2+T3+T8+T13+T14 = 300.000+360.000+625.000+630.000+368.000+204.000 = 2.487.000) PERSIS SAMA dengan total pembayaran komisi (T7 1.285.000 + T16 1.202.000 = 2.487.000) — akun 2103 Utang Komisi Dokter kembali ke saldo **6.750.000** (sama seperti saldo awal file 00, karena semua akrual periode ini sudah lunas dibayar). Ini poin verifikasi presisi utama file ini — kalau saldo 2103 di Trial Balance file 02 BUKAN 6.750.000, ada transaksi yang salah input.

### T17 — Pembayaran sebagian Utang Dagang Supplier (2026-01-23)

Dari total utang T6 (5.550.000), dibayar sebagian 3.000.000.

| Baris | Akun                                    |     Debit |    Kredit |
| ----- | --------------------------------------- | --------: | --------: |
| 1     | 2101 Utang Dagang — Supplier Bahan Gigi | 3.000.000 |           |
| 2     | 1102 Bank BCA Operasional               |           | 3.000.000 |

Total Debit = 3.000.000, Total Kredit = 3.000.000 ✓.

### T18 — Sterilisasi & limbah medis bulanan — DEMONSTRASI KOREKSI/REVERSE (2026-01-24)

**Skenario disengaja**: staf salah kode akun saat input (pakai 5207 Beban Sterilisasi, padahal seharusnya masuk 5102 Beban BHP Gigi karena memakai stok bahan sterilisasi dari persediaan BHP yang sama). Dipakai untuk menguji jalur `reverse` jurnal.

**T18a (salah, jangan dihapus manual — akan direverse via endpoint)**:

| Baris | Akun                                  |   Debit |  Kredit |
| ----- | ------------------------------------- | ------: | ------: |
| 1     | 5207 Beban Sterilisasi & Limbah Medis | 450.000 |         |
| 2     | 1101 Kas Kecil Klinik                 |         | 450.000 |

Total Debit = 450.000, Total Kredit = 450.000 ✓ — create + post seperti biasa dulu.

| Skenario                           | Detail                                                                                             | Hasil                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — reverse                  | `POST accounting/journals/reverse {id:<T18a>}` (atau endpoint reverse yang sesuai kontrak project) | Jurnal baru `REV-JRN-...` terposting: Dr 1101 450.000 / Cr 5207 450.000 (kebalikan T18a persis). Cek saldo 5207 & 1101 balik SEPERTI SEBELUM T18a diposting (net 0 dari T18a+reversalnya) — ini regression check untuk fix `Journal::reverse()` additive yang sudah diperbaiki 2026-08-01 (lihat memori `project_journal_reverse_nets_wrong_bug`), BUKAN net -2x |
| Positif — verifikasi `is_reversed` | `GET accounting/journals/show {id:<T18a>}`                                                         | `is_reversed:true`                                                                                                                                                                                                                                                                                                                                               |

**T18b (repost dengan akun yang benar, jurnal BARU terpisah, tanggal sama 2026-01-24)**:

| Baris | Akun                  |   Debit |  Kredit |
| ----- | --------------------- | ------: | ------: |
| 1     | 5102 Beban BHP Gigi   | 450.000 |         |
| 2     | 1101 Kas Kecil Klinik |         | 450.000 |

Total Debit = 450.000, Total Kredit = 450.000 ✓ — create + post seperti transaksi baru biasa.

**Efek bersih T18a+reverse+T18b**: 1101 Kas Kecil berkurang total 450.000 (satu kali, bukan dua kali — 450.000 keluar di T18a, masuk lagi 450.000 dari reverse, keluar lagi 450.000 di T18b = bersih -450.000). 5207 kembali 0. 5102 bertambah 450.000 (klasifikasi yang benar).

### T19 — (nomor disatukan dengan T18 reverse di atas, lihat blok T18)

### T20 — Setor sisa kas kecil ke bank (Kelapa Gading, 2026-01-28)

| Baris | Akun                      |     Debit |    Kredit |
| ----- | ------------------------- | --------: | --------: |
| 1     | 1102 Bank BCA Operasional | 1.500.000 |           |
| 2     | 1101 Kas Kecil Klinik     |           | 1.500.000 |

Total Debit = 1.500.000, Total Kredit = 1.500.000 ✓.

## Rekonsiliasi Akhir — Saldo Per Akun Setelah 20 Transaksi (per 2026-01-28)

Dihitung manual: **Saldo Akhir = Saldo Awal (file 00) ± akumulasi net seluruh transaksi T1-T20** (net = total debit dikurangi total kredit untuk akun debit-normal, sebaliknya untuk akun kredit-normal).

| Akun                                    |  Saldo Awal |   Net Perubahan | **Saldo Akhir** |
| --------------------------------------- | ----------: | --------------: | --------------: |
| 1101 Kas Kecil Klinik                   |   3.000.000 |      +2.338.000 |   **5.338.000** |
| 1102 Bank BCA Operasional               | 150.000.000 |     −18.287.000 | **131.713.000** |
| 1103 Piutang Pasien BPJS/Asuransi       |  28.500.000 |        +880.000 |  **29.380.000** |
| 1104 Persediaan BHP Gigi                |  22.750.000 |      +4.720.000 |  **27.470.000** |
| 1105 PPN Masukan                        |           0 |        +550.000 |     **550.000** |
| 2101 Utang Dagang — Supplier Bahan Gigi |  14.300.000 |      +2.550.000 |  **16.850.000** |
| 2102 PPN Keluaran                       |           0 |         +33.000 |      **33.000** |
| 2103 Utang Komisi Dokter                |   6.750.000 | 0 (lunas penuh) |   **6.750.000** |
| 2104 Utang PPh 21 Karyawan              |   1.850.000 |        +450.000 |   **2.300.000** |
| 3101 Modal Pemilik                      | 181.350.000 |               0 | **181.350.000** |
| 4101 Pendapatan Jasa Gigi Umum          |           0 |      +3.550.000 |   **3.550.000** |
| 4102 Pendapatan Jasa Ortodonti          |           0 |      +2.500.000 |   **2.500.000** |
| 4103 Pendapatan Jasa Estetika Gigi      |           0 |      +1.800.000 |   **1.800.000** |
| 4104 Pendapatan Penjualan Produk Ritel  |           0 |        +300.000 |     **300.000** |
| 5101 Beban Komisi Dokter                |           0 |      +2.487.000 |   **2.487.000** |
| 5102 Beban BHP Gigi                     |           0 |        +730.000 |     **730.000** |
| 5201 Beban Sewa Klinik                  |           0 |      +6.000.000 |   **6.000.000** |
| 5202 Beban Gaji Karyawan Non-Dokter     |           0 |      +9.000.000 |   **9.000.000** |
| 5203 Beban Listrik & Air                |           0 |      +2.750.000 |   **2.750.000** |
| 5206 Beban Selisih Kas Kasir Harian     |           0 |         +15.000 |      **15.000** |
| 5207 Beban Sterilisasi & Limbah Medis   |           0 |  0 (di-reverse) |           **0** |

**Verifikasi total (harus balance)**:

```
Total Aset  = 5.338.000 + 131.713.000 + 29.380.000 + 27.470.000 + 550.000       = 194.451.000
Total Beban = 2.487.000 + 730.000 + 6.000.000 + 9.000.000 + 2.750.000 + 15.000 + 0 = 20.982.000
TOTAL SISI DEBIT (Aset + Beban)                                                  = 215.433.000

Total Liabilitas = 16.850.000 + 33.000 + 6.750.000 + 2.300.000                  = 25.933.000
Total Ekuitas    = 181.350.000                                                    = 181.350.000
Total Pendapatan = 3.550.000 + 2.500.000 + 1.800.000 + 300.000                  = 8.150.000
TOTAL SISI KREDIT (Liabilitas + Ekuitas + Pendapatan)                            = 215.433.000
```

**215.433.000 = 215.433.000 → BALANCE.** Angka ini adalah acuan mutlak untuk `accounting/general-ledger/trial-balance` di file [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) — kalau hasil aktual beda walau Rp1, catat sebagai temuan dan telusuri transaksi mana yang menyimpang sebelum lanjut ke file berikutnya.

## Referensi Silang

- `App\Services\JournalPostingService` — posting engine dipakai `accounting/journals/create`+`post`
- `App\Models\Accounting\Journal::reverse()` — dipakai T18, sudah fix additive (lihat memori `project_journal_reverse_nets_wrong_bug`, 2026-08-01)
- File [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) — verifikasi akumulasi di atas lewat endpoint GL sungguhan
