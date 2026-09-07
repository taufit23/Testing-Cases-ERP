---
title: (Rumah Sakit) — 02. General Ledger & Trial Balance
category: accounting-rumah-sakit
description: Verifikasi Detail Ledger, Summary by Account (dengan filter dimensi departemen), dan Trial Balance terhadap angka yang sudah dihitung manual di file 01 — skala nilai miliaran rupiah, harus cocok persis sampai ke rupiah terakhir.
visibility: internal
---

# 02. General Ledger & Trial Balance

> Prasyarat: file [`01-jurnal-manual-transaksi-klinis-dan-klaim-bpjs.id.md`](./01-jurnal-manual-transaksi-klinis-dan-klaim-bpjs.id.md) sudah selesai — 17 transaksi (T1-T17, termasuk 1 reversal di T16b) sudah terposting.

## 1. Trial Balance (**General Ledger — `trial-balance`**)

| Skenario                          | Detail                                                                   | Hasil                                                                                                      |
| --------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Positif — trial balance lengkap   | `POST accounting/general-ledger/trial-balance {as_of_date:"2026-01-28"}` | `total_debit = total_credit = 66.333.170.000` (lihat §Rekonsiliasi Akhir file 01)                          |
| **Positif — cocokkan tiap baris** | Bandingkan tiap akun di response dengan tabel di bawah                   | Semua HARUS persis sama — kalau ada 1 akun beda, itu bug posting atau transaksi file 01 yang belum lengkap |

**Tabel acuan (WAJIB cocok persis dengan hasil endpoint):**

| Kode      | Akun                                                     |                      Saldo (Debit/Kredit) |
| --------- | -------------------------------------------------------- | ----------------------------------------: |
| 1101      | Kas Kecil Operasional RS                                 |                             Dr 29.935.000 |
| 1102      | Bank BCA Operasional                                     |                            Dr 750.700.000 |
| 1103      | Bank Mandiri Khusus BPJS                                 |                          Dr 3.300.000.000 |
| 1104      | Piutang Pasien Umum                                      |                            Dr 180.000.000 |
| 1105      | Piutang Klaim BPJS Kesehatan                             |                            Dr 240.000.000 |
| 1106      | Piutang Klaim Asuransi Swasta                            |                                      Dr 0 |
| 1107      | Persediaan Obat, Alkes & BMHP                            |                          Dr 1.360.350.000 |
| 1108      | PPN Masukan                                              |                             Dr 91.200.000 |
| 1201      | Gedung Rumah Sakit                                       |                         Dr 40.000.000.000 |
| 1202      | Akumulasi Penyusutan Gedung                              |      Cr 8.000.000.000 (negatif di Neraca) |
| 1203      | Mesin CT-Scan                                            |                         Dr 12.000.000.000 |
| 1204      | Akumulasi Penyusutan Mesin CT-Scan                       |                          Cr 4.000.000.000 |
| 1205      | Mesin MRI                                                |                         Dr 18.000.000.000 |
| 1206      | Akumulasi Penyusutan Mesin MRI                           |                          Cr 3.000.000.000 |
| 1207      | Peralatan Radiologi (X-Ray & USG)                        |                          Dr 5.000.000.000 |
| 1208      | Akumulasi Penyusutan Peralatan Radiologi                 |                          Cr 2.000.000.000 |
| 2101      | Utang Dagang — Supplier Farmasi & Alkes                  |                          Cr 1.246.200.000 |
| 2102      | PPN Keluaran                                             |                             Cr 15.220.000 |
| 2103      | Utang Fee Dokter Spesialis                               |                            Cr 166.250.000 |
| 2104      | Utang Gaji Karyawan Tetap                                |                            Cr 420.000.000 |
| 2105      | Utang PPh 21 Karyawan                                    |                            Cr 187.500.000 |
| 2106      | Uang Muka Pasien Rawat Inap                              |                            Cr 210.000.000 |
| 2201      | Utang Bank Jangka Panjang — Ekspansi Gedung              |                         Cr 14.750.000.000 |
| 3101      | Modal Pemilik                                            |                         Cr 49.100.000.000 |
| 3102      | Laba Ditahan                                             |                  Cr 0 (belum tutup tahun) |
| 4101      | Pendapatan RI Kelas 3                                    |                             Cr 18.000.000 |
| 4102      | Pendapatan RI Kelas 2                                    |    Cr 0 (tidak ada transaksi periode ini) |
| 4103      | Pendapatan RI Kelas 1                                    |    Cr 0 (tidak ada transaksi periode ini) |
| 4104      | Pendapatan RI VIP                                        |                             Cr 85.000.000 |
| 4105      | Pendapatan RI ICU                                        |                             Cr 62.000.000 |
| 4106      | Pendapatan RJ Poli Umum                                  |                              Cr 3.600.000 |
| 4107      | Pendapatan RJ Poli Spesialis                             |                             Cr 12.400.000 |
| 4108      | Pendapatan Laboratorium                                  |                              Cr 9.800.000 |
| 4109      | Pendapatan Radiologi                                     |                             Cr 38.000.000 |
| 4110      | Pendapatan Farmasi Obat Resep                            |                              Cr 7.200.000 |
| 4111      | Pendapatan Farmasi Obat Bebas/OTC                        |                              Cr 2.000.000 |
| 5101      | Beban Fee Dokter Spesialis                               |                             Dr 16.250.000 |
| 5102      | Beban Gaji Karyawan Tetap                                |                          Dr 1.850.000.000 |
| 5103      | Beban HPP Obat & Alkes                                   |                              Dr 5.800.000 |
| 5104      | Beban Bahan Medis Habis Pakai                            |                              Dr 3.850.000 |
| 5105      | Beban Listrik, Air & Pemeliharaan Gedung                 | Dr 0 (belum ada, file ini tidak mencakup) |
| 5106-5110 | Beban Penyusutan (Gedung/CT-Scan/MRI/Radiologi/Ambulans) |                 Dr 0 (belum ada, file 06) |
| 5111      | Beban Piutang Tak Tertagih (Klaim BPJS Ditolak)          |                            Dr 200.000.000 |
| 5112      | Beban Administrasi Bank                                  |         Dr 0 (net 0 setelah reverse T16b) |
| 5113      | Beban Bunga Pinjaman Bank                                |                            Dr 125.000.000 |
| 5114      | Beban Selisih Kas Kasir                                  |                                 Dr 85.000 |
| 5115      | Beban Sterilisasi & Limbah Medis                         |                            Dr 180.000.000 |

|    Total Debit |   Total Kredit |
| -------------: | -------------: |
| 66.333.170.000 | 66.333.170.000 |

| Skenario                                     | Detail                                                                                                                                      | Hasil                                                                                                                                                                                                                                                                                                                                                                                               | Label temuan               |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **Positif — dua implementasi trial balance** | Ada JUGA `reports/trial-balance` (kalau tersedia) selain `accounting/general-ledger/trial-balance` — jalankan keduanya                      | Harus hasilnya identik. Kalau beda, temuan konsistensi                                                                                                                                                                                                                                                                                                                                              | Belum diverifikasi ke kode |
| **Positif — presisi angka besar (miliaran)** | Cek TIDAK ADA pembulatan/floating-point drift pada akun bernilai miliaran (mis. 1201 Gedung 40.000.000.000, 2201 Utang Bank 14.750.000.000) | Nilai HARUS presisi sampai rupiah terakhir — kolom currency di database seharusnya `decimal(20,4)` (lihat konvensi migrasi project), bukan tipe float yang rawan drift pada angka besar. Kalau ditemukan selisih kecil (mis. 14.749.999.999,99...), catat sebagai temuan presisi PRIORITAS TINGGI — inilah alasan suite ini sengaja pakai nilai miliaran, beda dari suite lain yang nilainya jutaan | Belum diverifikasi ke kode |
| Negatif                                      | `as_of_date` sebelum ada transaksi apapun (mis. `2025-12-31`)                                                                               | Semua saldo 0 KECUALI saldo awal (bertanggal hari jurnal opening balance diposting) — regression check, sudah dites detail di suite lain                                                                                                                                                                                                                                                            |

## 2. Detail Ledger per Akun (**General Ledger**)

### 2.1 Piutang Klaim BPJS Kesehatan (1105) — siklus klaim dengan dispute, akun paling kompleks di suite ini

| Skenario                                                                     | Detail                                                                                                      | Hasil                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                                      | `POST accounting/general-ledger {chart_of_account_id:<1105>, date_from:"2026-01-01", date_to:"2026-01-28"}` | 4 baris mutasi (di luar saldo awal): +62.000.000 (T3), +28.000.000 (T7), −2.100.000.000 (T12a, pencairan disetujui), −200.000.000 (T12b, write-off ditolak) — saldo awal 2.450.000.000 → saldo akhir **240.000.000**                                                 |
| **Positif — 2 baris pengurang dengan sifat berbeda tetap tercatat terpisah** | Cek deskripsi/referensi 2 baris pengurang (T12a & T12b)                                                     | HARUS bisa dibedakan (referensi jurnal berbeda: pencairan vs write-off) — staf audit harus bisa menelusuri MANA yang benar-benar cair ke bank dan MANA yang dihapusbukukan tanpa kas masuk, keduanya sama-sama mengurangi 1105 tapi beda "lawan akun" (1103 vs 5111) |

### 2.2 Piutang Klaim Asuransi Swasta (1106) — kontras BPJS, lunas bersih

| Skenario                                                    | Detail                                                                                                      | Hasil                                                                                                                           |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                     | `POST accounting/general-ledger {chart_of_account_id:<1106>, date_from:"2026-01-01", date_to:"2026-01-28"}` | 2 baris: +4.000.000 (T6), −624.000.000 (T13) — saldo awal 620.000.000 → saldo akhir **0**                                       |
| **Positif — bukti "saldo nol" BUKAN "tidak ada aktivitas"** | Pastikan tercatat 2 baris mutasi meski saldo akhir 0                                                        | Sama seperti prinsip verifikasi di suite lain — saldo nol karena SEMUA piutang tertagih penuh, bukan karena tidak ada transaksi |

### 2.3 Utang Fee Dokter Spesialis (2103) — akrual fee-for-service berjalan

| Skenario | Detail                                                                                                      | Hasil                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST accounting/general-ledger {chart_of_account_id:<2103>, date_from:"2026-01-01", date_to:"2026-01-28"}` | 4 baris: +8.500.000 (T2), +4.650.000 (T3), +3.100.000 (T5), −1.200.000.000 (T11) — saldo awal 1.350.000.000 → saldo akhir **166.250.000** (BUKAN kembali ke saldo awal seperti pola di suite klinik gigi — di suite ini akrual baru SEBAGIAN dibayar, sisa 166.250.000 masih terutang, mencerminkan siklus pembayaran fee dokter spesialis RS besar yang biasanya periodik bulanan penuh, bukan mingguan) |

## 3. Summary by Account dengan Filter Dimensi Departemen (Business Unit)

| Skenario                                   | Detail                                                                                       | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------ | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — filter RI                        | `POST accounting/general-ledger/summary` filter `business_unit_id:<RI>`, akun 4101+4104+4105 | T1 18.000.000 + T2 85.000.000 + T3 62.000.000 = **165.000.000**                                                                                                                                                                                                                                                                                                                                                                   |
| Positif — filter RJ                        | Sama, `business_unit_id:<RJ>`, akun 4106+4107                                                | T4 3.600.000 + T5 12.400.000 = **16.000.000**                                                                                                                                                                                                                                                                                                                                                                                     |
| Positif — filter FAR                       | Sama, `business_unit_id:<FAR>`, akun 4110+4111                                               | T8 7.200.000 + T9 2.000.000 = **9.200.000**                                                                                                                                                                                                                                                                                                                                                                                       |
| Positif — filter PJG                       | Sama, `business_unit_id:<PJG>`, akun 4108+4109                                               | T6 9.800.000 + T7 38.000.000 = **47.800.000**                                                                                                                                                                                                                                                                                                                                                                                     |
| **Positif — total keseluruhan tetap utuh** | Total tanpa filter `business_unit_id`, semua akun 41xx                                       | 165.000.000 + 16.000.000 + 9.200.000 + 47.800.000 = **238.000.000** — cocok Total Pendapatan file 01, transaksi T12/T13 (piutang, tanpa BU) sengaja tidak menyumbang pendapatan baru sehingga total per-departemen otomatis pas dengan total keseluruhan di suite ini (beda dari suite klinik gigi yang punya 1 baris beban tidak ter-tag yang bikin rekonsiliasi beban tidak penuh — cek §4 file 04 untuk kasus serupa di beban) |
| Negatif                                    | `business_unit_id` yang tidak ada di branch aktif                                            | 422 `not_found_in_branch`                                                                                                                                                                                                                                                                                                                                                                                                         |

## 4. Verifikasi Silang Persamaan Akuntansi Dasar

| Skenario    | Detail                                                           | Hasil                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | Aset = Liabilitas + Ekuitas + (Pendapatan − Beban) berjalan      | `63.952.185.000 = 16.995.170.000 + 49.100.000.000 + (238.000.000 − 2.380.985.000)` → `63.952.185.000 = 16.995.170.000 + 49.100.000.000 + (−2.142.985.000)` → `63.952.185.000 = 63.952.185.000` ✓ — RS **rugi berjalan** 2.142.985.000 di sampel transaksi Januari ini, murni timing (beban tetap bulanan besar dibebankan penuh, pendapatan yang didokumentasikan cuma sampel hari, bukan indikasi bug) |
| Netralisasi | — (tidak ada state yang perlu dibalikkan, hanya query read-only) |

## Referensi Silang

- File [`01-jurnal-manual-transaksi-klinis-dan-klaim-bpjs.id.md`](./01-jurnal-manual-transaksi-klinis-dan-klaim-bpjs.id.md) — sumber seluruh angka acuan di file ini
- File [`04-laporan-keuangan-per-departemen.id.md`](./04-laporan-keuangan-per-departemen.id.md) — Neraca & Laba Rugi memakai angka Trial Balance yang sama persis
