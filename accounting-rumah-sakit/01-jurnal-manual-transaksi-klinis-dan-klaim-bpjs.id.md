---
title: (Rumah Sakit) — 01. Jurnal Manual, Transaksi Klinis & Klaim BPJS
category: accounting-rumah-sakit
description: 17 transaksi jurnal manual (T1-T17) bernilai besar tersebar Januari 2026 — rawat inap multi-kelas, rawat jalan, farmasi, lab/radiologi, fee dokter spesialis vs gaji tetap, dan kasus flagship klaim BPJS ditolak sebagian (dispute) yang harus dihapusbukukan. Total debit=kredit dihitung manual, harus cocok persis dengan Trial Balance file 02.
visibility: internal
---

# 01. Jurnal Manual, Transaksi Klinis & Klaim BPJS

> Prasyarat: file [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) sudah selesai — Modal Pemilik (3101) harus sudah **49.100.000.000** sebelum mulai file ini.
>
> **Cara pakai file ini**: setiap transaksi (T1-T17) adalah 1 pemanggilan `POST accounting/journals/create` diikuti `POST accounting/journals/post` (asumsi `require_journal_approval` OFF — approval workflow generik sudah dites di suite retail, tidak diulang di sini). Isi `date` sesuai kolom Tanggal, `business_unit_id` sesuai kolom Departemen (kosongkan kalau transaksi lintas-departemen/pusat). Setiap transaksi WAJIB `debit = credit` — dicek ulang manual di tabel masing-masing.
>
> **Kenapa 4102 (RI Kelas 2) dan 4103 (RI Kelas 1) TIDAK punya transaksi di file ini**: disengaja — bukan semua kelas kamar terisi di hari-hari yang didokumentasikan (realistis, okupansi RS bervariasi per hari). Akun tetap ada di COA dan boleh dipakai kapan saja, hanya kebetulan tidak terpakai di rentang tanggal yang didokumentasikan — regression check di file 02 harus menunjukkan saldo 0 untuk 2 akun ini, BUKAN error/hilang dari daftar akun.

## T1 — Rawat Inap Kelas 3, tunai/kartu debit (2026-01-05)

Pasien umum, beberapa hari rawat + tindakan, dibayar penuh via kartu debit (masuk rekening bank).

| Baris | Akun                       |      Debit |     Kredit |
| ----- | -------------------------- | ---------: | ---------: |
| 1     | 1102 Bank BCA Operasional  | 18.000.000 |            |
| 2     | 4101 Pendapatan RI Kelas 3 |            | 18.000.000 |

Total Debit = 18.000.000, Total Kredit = 18.000.000 ✓. `business_unit_id`: RI. Tidak ada baris fee dokter — kelas 3 ditangani dokter umum bergaji tetap (5102), bukan dokter spesialis fee-for-service.

| Skenario | Detail                                                | Hasil                                     |
| -------- | ----------------------------------------------------- | ----------------------------------------- |
| Positif  | Create + post jurnal di atas                          | 201 create, 200 post, status `JRN_POSTED` |
| Negatif  | Coba post ulang jurnal yang SAMA (sudah `JRN_POSTED`) | Ditolak — sudah posted                    |

## T2 — Rawat Inap VIP + fee dokter spesialis 10% (2026-01-06)

Tagihan VIP dibayar tunai/kartu penuh. Dokter spesialis penanggung jawab dapat fee 10% dari total tagihan (kesepakatan RS-dokter, bukan aturan sistem).

| Baris | Akun                                  |      Debit |     Kredit |
| ----- | ------------------------------------- | ---------: | ---------: |
| 1     | 1102 Bank BCA Operasional             | 85.000.000 |            |
| 2     | 4104 Pendapatan RI VIP                |            | 85.000.000 |
| 3     | 5101 Beban Fee Dokter Spesialis (10%) |  8.500.000 |            |
| 4     | 2103 Utang Fee Dokter Spesialis       |            |  8.500.000 |

Total Debit = 93.500.000, Total Kredit = 93.500.000 ✓. `business_unit_id`: RI.

**Catatan model kompensasi (kasus khas RS besar, kontras dengan gaji tetap T1/T14)**: fee dokter spesialis dihitung persentase MANUAL per kesepakatan kontrak (bervariasi per dokter/tindakan) — sistem tidak tahu "dokter A dapat 10%", nominal `debit`/`credit` tetap diinput manual oleh staf keuangan setelah verifikasi tagihan. Dicatat di sini supaya jelas kenapa persentase bervariasi antar transaksi (T2 10%, T3 15%, T5 25% — bukan salah ketik, tapi tarif kontrak berbeda per spesialisasi/kompleksitas tindakan).

## T3 — Rawat Inap ICU, klaim BPJS (piutang) + BMHP + fee dokter 15% (2026-01-07)

Tagihan paket ICU (INA-CBG) seluruhnya diklaim ke BPJS — piutang, belum cair. Dokter intensivist dapat fee 15%. BMHP (infus, oksigen, dsb) terpakai langsung dari persediaan.

| Baris | Akun                                  |      Debit |     Kredit |
| ----- | ------------------------------------- | ---------: | ---------: |
| 1     | 1105 Piutang Klaim BPJS Kesehatan     | 62.000.000 |            |
| 2     | 4105 Pendapatan RI ICU                |            | 62.000.000 |
| 3     | 5101 Beban Fee Dokter Spesialis (15%) |  4.650.000 |            |
| 4     | 2103 Utang Fee Dokter Spesialis       |            |  4.650.000 |
| 5     | 5104 Beban Bahan Medis Habis Pakai    |  3.200.000 |            |
| 6     | 1107 Persediaan Obat, Alkes & BMHP    |            |  3.200.000 |

Total Debit = 69.850.000, Total Kredit = 69.850.000 ✓. `business_unit_id`: RI.

## T4 — Rawat Jalan Poli Umum, tunai harian (2026-01-08)

Beberapa pasien poli umum, rekap harian, tunai kas kecil.

| Baris | Akun                          |     Debit |    Kredit |
| ----- | ----------------------------- | --------: | --------: |
| 1     | 1101 Kas Kecil Operasional RS | 3.600.000 |           |
| 2     | 4106 Pendapatan RJ Poli Umum  |           | 3.600.000 |

Total Debit = 3.600.000, Total Kredit = 3.600.000 ✓. `business_unit_id`: RJ. Tidak ada fee dokter (poli umum, dokter bergaji tetap).

## T5 — Rawat Jalan Poli Spesialis + fee dokter 25% (2026-01-09)

Rekap harian poli spesialis (jantung, kulit, dll), dibayar via bank karena nilai besar.

| Baris | Akun                                  |      Debit |     Kredit |
| ----- | ------------------------------------- | ---------: | ---------: |
| 1     | 1102 Bank BCA Operasional             | 12.400.000 |            |
| 2     | 4107 Pendapatan RJ Poli Spesialis     |            | 12.400.000 |
| 3     | 5101 Beban Fee Dokter Spesialis (25%) |  3.100.000 |            |
| 4     | 2103 Utang Fee Dokter Spesialis       |            |  3.100.000 |

Total Debit = 15.500.000, Total Kredit = 15.500.000 ✓. `business_unit_id`: RJ.

## T6 — Laboratorium, tunai + asuransi swasta piutang (split pembayaran) (2026-01-12)

Total pemeriksaan lab hari itu Rp9.800.000: Rp5.800.000 tunai/kartu (bank), Rp4.000.000 piutang asuransi swasta (klaim diajukan, belum cair). BMHP lab terpakai Rp650.000.

| Baris | Akun                               |     Debit |    Kredit |
| ----- | ---------------------------------- | --------: | --------: |
| 1     | 1102 Bank BCA Operasional          | 5.800.000 |           |
| 2     | 1106 Piutang Klaim Asuransi Swasta | 4.000.000 |           |
| 3     | 4108 Pendapatan Laboratorium       |           | 9.800.000 |
| 4     | 5104 Beban Bahan Medis Habis Pakai |   650.000 |           |
| 5     | 1107 Persediaan Obat, Alkes & BMHP |           |   650.000 |

Total Debit = 10.450.000, Total Kredit = 10.450.000 ✓. `business_unit_id`: PJG.

## T7 — Radiologi (CT-Scan & MRI), campuran tunai + BPJS (2026-01-13)

Total tagihan radiologi Rp38.000.000: tunai/kartu Rp10.000.000, BPJS piutang Rp28.000.000.

| Baris | Akun                              |      Debit |     Kredit |
| ----- | --------------------------------- | ---------: | ---------: |
| 1     | 1102 Bank BCA Operasional         | 10.000.000 |            |
| 2     | 1105 Piutang Klaim BPJS Kesehatan | 28.000.000 |            |
| 3     | 4109 Pendapatan Radiologi         |            | 38.000.000 |

Total Debit = 38.000.000, Total Kredit = 38.000.000 ✓. `business_unit_id`: PJG.

## T8 — Penjualan Obat Resep (bebas PPN, bagian pengobatan rawat jalan), tunai (2026-01-14)

| Baris | Akun                                 |     Debit |    Kredit |
| ----- | ------------------------------------ | --------: | --------: |
| 1     | 1101 Kas Kecil Operasional RS        | 7.200.000 |           |
| 2     | 4110 Pendapatan Farmasi — Obat Resep |           | 7.200.000 |
| 3     | 5103 Beban HPP Obat & Alkes          | 4.500.000 |           |
| 4     | 1107 Persediaan Obat, Alkes & BMHP   |           | 4.500.000 |

Total Debit = 11.700.000, Total Kredit = 11.700.000 ✓. `business_unit_id`: FAR.

## T9 — Penjualan Obat Bebas/OTC Apotek Luar, KENA PPN 11% (2026-01-15)

Harga jual termasuk PPN: dasar 2.000.000 + PPN 220.000 = total tunai 2.220.000. **Satu-satunya transaksi pendapatan di file ini yang menyentuh PPN Keluaran.**

| Baris | Akun                                     |     Debit |    Kredit |
| ----- | ---------------------------------------- | --------: | --------: |
| 1     | 1101 Kas Kecil Operasional RS            | 2.220.000 |           |
| 2     | 4111 Pendapatan Farmasi — Obat Bebas/OTC |           | 2.000.000 |
| 3     | 2102 PPN Keluaran                        |           |   220.000 |
| 4     | 5103 Beban HPP Obat & Alkes              | 1.300.000 |           |
| 5     | 1107 Persediaan Obat, Alkes & BMHP       |           | 1.300.000 |

Total Debit = 3.520.000, Total Kredit = 3.520.000 ✓. `business_unit_id`: FAR.

| Skenario | Detail                                                                                                                                                                                   | Hasil                                              |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Positif  | Verifikasi ulang di file `07-rekonsiliasi-bank-multi-rekening-dan-ppn.id.md` bahwa PPN Keluaran akumulasi HANYA dari T9 (220.000), tidak tercampur 10 akun pendapatan jasa medis lainnya | Konsisten dengan desain PPN selektif file 00 §3/§7 |

## T10 — Pembelian Obat & Alkes kredit dari supplier (2026-01-16)

Harga barang 420.000.000 + PPN Masukan 11% (46.200.000) = utang dagang 466.200.000.

| Baris | Akun                                         |       Debit |      Kredit |
| ----- | -------------------------------------------- | ----------: | ----------: |
| 1     | 1107 Persediaan Obat, Alkes & BMHP           | 420.000.000 |             |
| 2     | 1108 PPN Masukan                             |  46.200.000 |             |
| 3     | 2101 Utang Dagang — Supplier Farmasi & Alkes |             | 466.200.000 |

Total Debit = 466.200.000, Total Kredit = 466.200.000 ✓. Tidak ada `business_unit_id` (pembelian pusat).

## T11 — Pembayaran sebagian Utang Fee Dokter Spesialis (2026-01-19)

Akrual berjalan (T2+T3+T5 = 8.500.000+4.650.000+3.100.000 = 16.250.000) ditambah saldo awal 1.350.000.000 = total akrual 1.366.250.000. Dibayar sebagian besar dari bank.

| Baris | Akun                            |         Debit |        Kredit |
| ----- | ------------------------------- | ------------: | ------------: |
| 1     | 2103 Utang Fee Dokter Spesialis | 1.200.000.000 |               |
| 2     | 1102 Bank BCA Operasional       |               | 1.200.000.000 |

Total Debit = 1.200.000.000, Total Kredit = 1.200.000.000 ✓. Sisa akrual belum dibayar setelah ini = 166.250.000 (dibawa ke saldo akhir).

## T12 — KLAIM BPJS DITOLAK SEBAGIAN (dispute) — skenario flagship suite ini (2026-01-20)

BPJS memverifikasi & mencairkan klaim yang jatuh tempo diproses sebesar **2.300.000.000** (bagian dari saldo piutang BPJS yang ada) — **HANYA 2.100.000.000 yang disetujui & cair** ke rekening khusus BPJS, sisanya **200.000.000 DITOLAK** (verifikator BPJS menilai readmisi dalam 7 hari untuk kasus sama tidak memenuhi kriteria klaim ulang sesuai ketentuan INA-CBG). Setelah upaya banding internal RS gagal, sisa yang ditolak dihapusbukukan sebagai piutang tak tertagih.

**T12a — Pencairan yang disetujui:**

| Baris | Akun                                     |         Debit |        Kredit |
| ----- | ---------------------------------------- | ------------: | ------------: |
| 1     | 1103 Bank Mandiri — Rekening Khusus BPJS | 2.100.000.000 |               |
| 2     | 1105 Piutang Klaim BPJS Kesehatan        |               | 2.100.000.000 |

Total Debit = 2.100.000.000, Total Kredit = 2.100.000.000 ✓.

**T12b — Write-off klaim yang ditolak (jurnal TERPISAH, tanggal sama):**

| Baris | Akun                                                 |       Debit |      Kredit |
| ----- | ---------------------------------------------------- | ----------: | ----------: |
| 1     | 5111 Beban Piutang Tak Tertagih (Klaim BPJS Ditolak) | 200.000.000 |             |
| 2     | 1105 Piutang Klaim BPJS Kesehatan                    |             | 200.000.000 |

Total Debit = 200.000.000, Total Kredit = 200.000.000 ✓.

Total klaim diproses (T12a+T12b) = 2.300.000.000. Tidak ada `business_unit_id` (klaim gabungan lintas kelas kamar/tindakan, tidak bisa ditrack ke 1 departemen).

| Skenario                                                    | Detail                                                                                                                                                         | Hasil                                                                                                                                                                                                                                                                                                                     | Label temuan               |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **Positif — 2 jurnal terpisah untuk 1 siklus klaim**        | Create + post T12a lalu T12b sebagai jurnal manual TERPISAH (bukan 1 jurnal 4-baris)                                                                           | Keduanya `JRN_POSTED` independen — mencerminkan proses bisnis nyata (pencairan dan keputusan penolakan biasanya diterima di waktu terpisah/dari sumber informasi terpisah, meski didokumentasikan tanggal sama di sini untuk simplifikasi)                                                                                | —                          |
| **Negatif — tidak ada validasi silang saldo piutang**       | Coba post T12b dengan nominal write-off LEBIH BESAR dari sisa saldo 1105 yang tersedia (mis. 5.000.000.000 padahal sisa piutang jauh lebih kecil setelah T12a) | Sistem TIDAK menolak (jurnal manual bebas isi angka apapun selama baris balance debit=kredit — tidak ada validasi silang ke saldo akun 1105 saat ini) — catat sebagai keterbatasan desain: kontrol saldo piutang tidak boleh minus HARUS dijaga manual oleh staf. Belum diverifikasi ke kode apakah ada guard tersembunyi | Belum diverifikasi ke kode |
| **Positif — verifikasi saldo piutang BPJS setelah dispute** | Setelah T12a+T12b, saldo 1105 berkurang tepat 2.300.000.000 dari sebelumnya (opening 2.450.000.000 + T3 62.000.000 + T7 28.000.000 − 2.300.000.000)            | Sisa piutang BPJS = **240.000.000** — masih ada saldo piutang berjalan yang BELUM diklaim/diverifikasi (bukan otomatis nol), cek presisi di file 02                                                                                                                                                                       |

## T13 — Pencairan Klaim Asuransi Swasta PENUH, kontras dengan BPJS (2026-01-21)

Piutang asuransi swasta (opening 620.000.000 + T6 4.000.000 = 624.000.000) dicairkan **penuh, tanpa sengketa** — asuransi swasta memproses & menyetujui klaim tanpa potongan, kontras tegas dengan proses BPJS di T12 yang berujung dispute.

| Baris | Akun                               |       Debit |      Kredit |
| ----- | ---------------------------------- | ----------: | ----------: |
| 1     | 1102 Bank BCA Operasional          | 624.000.000 |             |
| 2     | 1106 Piutang Klaim Asuransi Swasta |             | 624.000.000 |

Total Debit = 624.000.000, Total Kredit = 624.000.000 ✓.

| Skenario                                        | Detail                     | Hasil                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Positif — saldo 1106 nol persis setelah T13** | Cek saldo 1106 setelah T13 | **0** — kontras dengan 1105 (BPJS) yang masih sisa saldo 240.000.000 setelah T12 — bukti visual bahwa 2 jalur piutang pihak ketiga di suite ini punya karakter penyelesaian yang beda (asuransi swasta lebih cepat & bersih, BPJS lebih lambat & berpotensi dispute), verifikasi lengkap di file 02 |

## T14 — Gaji Karyawan Tetap (dokter umum, perawat, staf non-medis) + PPh 21 (2026-01-25)

Gaji bruto Januari Rp1.850.000.000. Potongan PPh 21 Rp92.500.000 (5%), dibayar bersih dari bank. **Beda model kompensasi dari T2/T3/T5** (fee dokter spesialis) — gaji tetap dibayar LANGSUNG tanpa lewat akrual 2103.

| Baris | Akun                           |         Debit |        Kredit |
| ----- | ------------------------------ | ------------: | ------------: |
| 1     | 5102 Beban Gaji Karyawan Tetap | 1.850.000.000 |               |
| 2     | 2105 Utang PPh 21 Karyawan     |               |    92.500.000 |
| 3     | 1102 Bank BCA Operasional      |               | 1.757.500.000 |

Total Debit = 1.850.000.000, Total Kredit = 92.500.000 + 1.757.500.000 = 1.850.000.000 ✓.

## T15 — Cicilan Pinjaman Bank Ekspansi Gedung — pokok + bunga (2026-01-26)

Cicilan bulanan: pokok Rp250.000.000 + bunga Rp125.000.000 = total kas keluar Rp375.000.000.

| Baris | Akun                                             |       Debit |      Kredit |
| ----- | ------------------------------------------------ | ----------: | ----------: |
| 1     | 2201 Utang Bank Jangka Panjang — Ekspansi Gedung | 250.000.000 |             |
| 2     | 5113 Beban Bunga Pinjaman Bank                   | 125.000.000 |             |
| 3     | 1102 Bank BCA Operasional                        |             | 375.000.000 |

Total Debit = 375.000.000, Total Kredit = 375.000.000 ✓.

| Skenario                            | Detail                                                                     | Hasil                                                                                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif — verifikasi saldo pinjaman | Saldo 2201 setelah T15 = 15.000.000.000 − 250.000.000 = **14.750.000.000** | Cek di file 02 — cicilan pokok mengurangi liability jangka panjang, bunga jadi beban periode berjalan, dua efek berbeda dari 1 transaksi cicilan |

## T16 — Opname Kas Kecil & DEMONSTRASI KOREKSI/REVERSE (2026-01-27)

**T16a — Selisih kas kecil (kurang):**

Opname kas kecil menemukan selisih kurang Rp85.000 dari catatan pembukuan.

| Baris | Akun                          |  Debit | Kredit |
| ----- | ----------------------------- | -----: | -----: |
| 1     | 5114 Beban Selisih Kas Kasir  | 85.000 |        |
| 2     | 1101 Kas Kecil Operasional RS |        | 85.000 |

Total Debit = 85.000, Total Kredit = 85.000 ✓.

**T16b — Beban Sterilisasi & Limbah Medis bulanan, SALAH KODE AKUN (akan direverse):**

Staf salah input — memakai akun `5112 Beban Administrasi Bank` padahal seharusnya `5115 Beban Sterilisasi & Limbah Medis` (kesalahan klasifikasi umum saat input manual, kode akun berdekatan di sistem).

| Baris | Akun                                 |       Debit |      Kredit |
| ----- | ------------------------------------ | ----------: | ----------: |
| 1     | 5112 Beban Administrasi Bank (SALAH) | 180.000.000 |             |
| 2     | 1102 Bank BCA Operasional            |             | 180.000.000 |

Total Debit = 180.000.000, Total Kredit = 180.000.000 ✓ — create + post seperti biasa dulu.

| Skenario                           | Detail                                         | Hasil                                                                                                                                                                         |
| ---------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — reverse                  | `POST accounting/journals/reverse {id:<T16b>}` | Jurnal baru `REV-JRN-...` terposting: Dr 1102 180.000.000 / Cr 5112 180.000.000 (kebalikan T16b persis, additive — bukan net -2x, sesuai fix `Journal::reverse()` 2026-08-01) |
| Positif — verifikasi `is_reversed` | `GET accounting/journals/show {id:<T16b>}`     | `is_reversed:true`                                                                                                                                                            |

**T16c — Repost dengan akun yang benar (jurnal BARU terpisah, tanggal sama 2026-01-27):**

| Baris | Akun                                  |       Debit |      Kredit |
| ----- | ------------------------------------- | ----------: | ----------: |
| 1     | 5115 Beban Sterilisasi & Limbah Medis | 180.000.000 |             |
| 2     | 1102 Bank BCA Operasional             |             | 180.000.000 |

Total Debit = 180.000.000, Total Kredit = 180.000.000 ✓.

**Efek bersih T16b+reverse+T16c**: 1102 Bank BCA berkurang bersih 180.000.000 (satu kali, bukan dua kali). 5112 kembali 0. 5115 bertambah 180.000.000 (klasifikasi yang benar).

## T17 — Setor sisa kas kecil ke bank (2026-01-28)

| Baris | Akun                          |     Debit |    Kredit |
| ----- | ----------------------------- | --------: | --------: |
| 1     | 1102 Bank BCA Operasional     | 8.000.000 |           |
| 2     | 1101 Kas Kecil Operasional RS |           | 8.000.000 |

Total Debit = 8.000.000, Total Kredit = 8.000.000 ✓.

## Rekonsiliasi Akhir — Saldo Per Akun Setelah 17 Transaksi (per 2026-01-28)

Dihitung manual: **Saldo Akhir = Saldo Awal (file 00) ± akumulasi net seluruh transaksi T1-T17.**

| Akun                                                 |           Saldo Awal |                 Net Perubahan |          **Saldo Akhir** |
| ---------------------------------------------------- | -------------------: | ----------------------------: | -----------------------: |
| 1101 Kas Kecil Operasional RS                        |           25.000.000 |                    +4.935.000 |           **29.935.000** |
| 1102 Bank BCA Operasional                            |        3.500.000.000 |                −2.749.300.000 |          **750.700.000** |
| 1103 Bank Mandiri Khusus BPJS                        |        1.200.000.000 |                +2.100.000.000 |        **3.300.000.000** |
| 1104 Piutang Pasien Umum                             |          180.000.000 |                             0 |          **180.000.000** |
| 1105 Piutang Klaim BPJS Kesehatan                    |        2.450.000.000 |                −2.210.000.000 |          **240.000.000** |
| 1106 Piutang Klaim Asuransi Swasta                   |          620.000.000 |                  −620.000.000 |                    **0** |
| 1107 Persediaan Obat, Alkes & BMHP                   |          950.000.000 |                  +410.350.000 |        **1.360.350.000** |
| 1108 PPN Masukan                                     |           45.000.000 |                   +46.200.000 |           **91.200.000** |
| 1201-1208 (Aset Tetap)                               | 58.000.000.000 (net) |        0 (belum ada, file 06) | **58.000.000.000 (net)** |
| 2101 Utang Dagang Supplier                           |          780.000.000 |                  +466.200.000 |        **1.246.200.000** |
| 2102 PPN Keluaran                                    |           15.000.000 |                      +220.000 |           **15.220.000** |
| 2103 Utang Fee Dokter Spesialis                      |        1.350.000.000 |                −1.183.750.000 |          **166.250.000** |
| 2104 Utang Gaji Karyawan Tetap                       |          420.000.000 | 0 (tidak dibayar periode ini) |          **420.000.000** |
| 2105 Utang PPh 21 Karyawan                           |           95.000.000 |                   +92.500.000 |          **187.500.000** |
| 2106 Uang Muka Pasien Rawat Inap                     |          210.000.000 |                             0 |          **210.000.000** |
| 2201 Utang Bank Jangka Panjang                       |       15.000.000.000 |                  −250.000.000 |       **14.750.000.000** |
| 3101 Modal Pemilik                                   |       49.100.000.000 |                             0 |       **49.100.000.000** |
| 4101 Pendapatan RI Kelas 3                           |                    0 |                   +18.000.000 |           **18.000.000** |
| 4102 Pendapatan RI Kelas 2                           |                    0 |                             0 |                    **0** |
| 4103 Pendapatan RI Kelas 1                           |                    0 |                             0 |                    **0** |
| 4104 Pendapatan RI VIP                               |                    0 |                   +85.000.000 |           **85.000.000** |
| 4105 Pendapatan RI ICU                               |                    0 |                   +62.000.000 |           **62.000.000** |
| 4106 Pendapatan RJ Poli Umum                         |                    0 |                    +3.600.000 |            **3.600.000** |
| 4107 Pendapatan RJ Poli Spesialis                    |                    0 |                   +12.400.000 |           **12.400.000** |
| 4108 Pendapatan Laboratorium                         |                    0 |                    +9.800.000 |            **9.800.000** |
| 4109 Pendapatan Radiologi                            |                    0 |                   +38.000.000 |           **38.000.000** |
| 4110 Pendapatan Farmasi Obat Resep                   |                    0 |                    +7.200.000 |            **7.200.000** |
| 4111 Pendapatan Farmasi Obat Bebas/OTC               |                    0 |                    +2.000.000 |            **2.000.000** |
| 5101 Beban Fee Dokter Spesialis                      |                    0 |                   +16.250.000 |           **16.250.000** |
| 5102 Beban Gaji Karyawan Tetap                       |                    0 |                +1.850.000.000 |        **1.850.000.000** |
| 5103 Beban HPP Obat & Alkes                          |                    0 |                    +5.800.000 |            **5.800.000** |
| 5104 Beban Bahan Medis Habis Pakai                   |                    0 |                    +3.850.000 |            **3.850.000** |
| 5111 Beban Piutang Tak Tertagih (Klaim BPJS Ditolak) |                    0 |                  +200.000.000 |          **200.000.000** |
| 5112 Beban Administrasi Bank                         |                    0 |                0 (di-reverse) |                    **0** |
| 5113 Beban Bunga Pinjaman Bank                       |                    0 |                  +125.000.000 |          **125.000.000** |
| 5114 Beban Selisih Kas Kasir                         |                    0 |                       +85.000 |               **85.000** |
| 5115 Beban Sterilisasi & Limbah Medis                |                    0 |                  +180.000.000 |          **180.000.000** |

**Verifikasi total (harus balance) — dihitung 2 arah:**

```
Total Aset (Lancar + Tetap net)
  = (29.935.000 + 750.700.000 + 3.300.000.000 + 180.000.000 + 240.000.000 + 0
     + 1.360.350.000 + 91.200.000) + 58.000.000.000
  = 5.952.185.000 + 58.000.000.000 = 63.952.185.000

Total Beban (5101-5115, exclude 5112=0)
  = 16.250.000 + 1.850.000.000 + 5.800.000 + 3.850.000 + 200.000.000
    + 125.000.000 + 85.000 + 180.000.000
  = 2.380.985.000

TOTAL SISI DEBIT (Aset + Beban) = 63.952.185.000 + 2.380.985.000 = 66.333.170.000

Total Liabilitas (2101-2106 + 2201)
  = 1.246.200.000 + 15.220.000 + 166.250.000 + 420.000.000 + 187.500.000
    + 210.000.000 + 14.750.000.000
  = 16.995.170.000

Total Ekuitas (3101) = 49.100.000.000

Total Pendapatan (4101-4111)
  = 18.000.000 + 85.000.000 + 62.000.000 + 3.600.000 + 12.400.000 + 9.800.000
    + 38.000.000 + 7.200.000 + 2.000.000
  = 238.000.000

TOTAL SISI KREDIT (Liabilitas + Ekuitas + Pendapatan)
  = 16.995.170.000 + 49.100.000.000 + 238.000.000 = 66.333.170.000
```

**66.333.170.000 = 66.333.170.000 → BALANCE.** Angka ini adalah acuan mutlak untuk `accounting/general-ledger/trial-balance` di file [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) — kalau hasil aktual beda walau Rp1, catat sebagai temuan dan telusuri transaksi mana yang menyimpang sebelum lanjut ke file berikutnya.

**Laba (Rugi) berjalan per 2026-01-28** = Total Pendapatan 238.000.000 − Total Beban 2.380.985.000 = **RUGI 2.142.985.000** — RS sedang rugi berjalan besar di bulan Januari ini, WAJAR dan bukan indikasi bug: beban tetap besar (gaji karyawan 1.850.000.000, write-off klaim BPJS 200.000.000, sterilisasi 180.000.000) dibebankan penuh dalam 1 bulan sementara pendapatan yang didokumentasikan di file ini hanya sampel sebagian hari-hari operasional (bukan rekap 1 bulan penuh — realistis untuk dokumentasi test case, bukan representasi kinerja RS sesungguhnya).

## Referensi Silang

- `App\Services\JournalPostingService` — posting engine dipakai `accounting/journals/create`+`post`
- `App\Models\Accounting\Journal::reverse()` — dipakai T16b, sudah fix additive (lihat memori `project_journal_reverse_nets_wrong_bug`, 2026-08-01)
- File [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) — verifikasi akumulasi di atas lewat endpoint GL sungguhan
