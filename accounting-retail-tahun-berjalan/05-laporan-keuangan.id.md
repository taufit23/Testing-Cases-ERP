---
title: — 05. Laporan Keuangan (FY2025 Penuh vs FY2026 Year-to-Date)
category: Accounting 2
description: Neraca, Laba Rugi, dan Arus Kas PT Retail Nusantara Jaya — FY2025 penuh (setelah Close Fiscal Year) dibandingkan FY2026 year-to-date Agustus (berjalan) — seluruh angka sudah direkonsiliasi manual dua arah (per transaksi & per akun) sebagai acuan pembanding.
visibility: internal
---

# 05. Laporan Keuangan (FY2025 Penuh vs FY2026 Year-to-Date)

> Prasyarat: [`04-tutup-periode-dan-tahun-fiskal.id.md`](./04-tutup-periode-dan-tahun-fiskal.id.md) selesai (FY2025 sudah Closed, Laba Ditahan terisi 27.050.000). Halaman: `accounting/reports/balance-sheet`, `accounting/reports/income-statement`, `accounting/reports/cash-flow-statement`.

## 1. Neraca (Balance Sheet) — 31 Desember 2025 (Setelah Close FY2025)

| Aset                     |                 | Liabilitas & Ekuitas           |                 |
| ------------------------ | --------------: | ------------------------------ | --------------: |
| Kas Kecil                |       9.800.000 | Utang Dagang                   |      61.050.000 |
| Bank BCA                 |     344.450.000 | PPN Keluaran                   |     105.600.000 |
| Piutang Dagang           |               0 | Utang PPh 21 Karyawan          |               0 |
| Persediaan Barang Dagang |      60.000.000 | Pinjaman Bank Jangka Pendek    |      56.000.000 |
| PPN Masukan              |      79.200.000 | **Total Liabilitas**           | **222.650.000** |
| Peralatan Toko           |      60.000.000 | Modal Pemilik                  |     290.000.000 |
| Akumulasi Penyusutan     |    (13.750.000) | Laba Ditahan                   |      27.050.000 |
|                          |                 | **Total Ekuitas**              | **317.050.000** |
| **Total Aset**           | **539.700.000** | **Total Liabilitas + Ekuitas** | **539.700.000** |

**Verifikasi wajib**: Total Aset = Total Liabilitas + Ekuitas = **539.700.000** persis (persamaan akuntansi dasar). Laba Ditahan 27.050.000 di sini adalah bukti closing entry file 04 sudah berjalan benar — kalau masih 0, berarti Close Fiscal Year belum dilakukan atau laporan ini masih membaca tanggal setelah 2025 saja (cek filter tanggal).

## 2. Neraca (Balance Sheet) — 31 Agustus 2026 (Bulan Berjalan)

| Aset                     |                 | Liabilitas & Ekuitas                                       |                 |
| ------------------------ | --------------: | ---------------------------------------------------------- | --------------: |
| Kas Kecil                |       9.700.000 | Utang Dagang                                               |      55.500.000 |
| Bank BCA                 |     355.365.000 | PPN Keluaran                                               |     185.240.000 |
| Piutang Dagang           |               0 | Utang PPh 21 Karyawan                                      |         825.000 |
| Persediaan Barang Dagang |      90.000.000 | Pinjaman Bank Jangka Pendek                                |      24.000.000 |
| PPN Masukan              |     130.900.000 | **Total Liabilitas**                                       | **265.565.000** |
| Peralatan Toko           |      60.000.000 | Modal Pemilik                                              |     290.000.000 |
| Akumulasi Penyusutan     |    (23.750.000) | Laba Ditahan (dari Close FY2025)                           |      27.050.000 |
|                          |                 | Laba Berjalan FY2026 (Jan-Ags, belum di-closing-entry-kan) |      39.600.000 |
|                          |                 | **Total Ekuitas**                                          | **356.650.000** |
| **Total Aset**           | **622.215.000** | **Total Liabilitas + Ekuitas**                             | **622.215.000** |

**Sebab-akibat — "Laba Berjalan" vs "Laba Ditahan":** sampai FY2026 di-Close (belum dilakukan di suite ini, karena "bulan berjalan" masih Agustus), sistem menghitung baris Ekuitas "Laba Berjalan" langsung dari selisih akun Pendapatan−Beban FY2026 yang MASIH TERBUKA (bukan dari akun 3102) — kalau laporan Neraca kamu TIDAK punya baris terpisah untuk ini (cuma Modal Pemilik + Laba Ditahan tanpa Laba Berjalan), berarti Total Ekuitas versi UI akan tampak "kurang" 39.600.000 dari Total Aset — bukan bug, itu tanda laporan tidak menghitung laba berjalan periode terbuka secara eksplisit; cek behavior aktual dan catat sebagai temuan kalau kejadian.

| Skenario                               | Langkah di UI                                                       | Hasil                                                                                |
| -------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Positif — Neraca FY2025                | Buka **Reports → Balance Sheet**, filter tanggal per **2025-12-31** | Cocok dengan tabel §1, Total Aset = Total Liabilitas+Ekuitas = 539.700.000           |
| Positif — Neraca FY2026 YTD            | Ulangi filter tanggal per **2026-08-31**                            | Cocok dengan tabel §2, Total Aset = Total Liabilitas+Ekuitas = 622.215.000           |
| **Positif — akun kontra tampil benar** | Cek baris Akumulasi Penyusutan di kedua laporan                     | Tampil sebagai pengurang di sisi Aset (bukan ditambahkan atau dipisah ke Liabilitas) |
| Netralisasi                            | — (laporan read-only)                                               |                                                                                      |

## 3. Laba Rugi (Income Statement) — FY2025 vs FY2026 Year-to-Date

| Komponen                                  |  FY2025 (Jan-Des) | FY2026 (Jan-Ags, 8 bulan) |
| ----------------------------------------- | ----------------: | ------------------------: |
| Penjualan Barang Dagang                   |       960.000.000 |               724.000.000 |
| **(-) Harga Pokok Penjualan**             |     (600.000.000) |             (440.000.000) |
| **Laba Kotor**                            |   **360.000.000** |           **284.000.000** |
| Beban Sewa Toko                           |      (96.000.000) |              (70.400.000) |
| Beban Gaji Karyawan                       |     (180.000.000) |             (132.000.000) |
| Beban Listrik & Air                       |      (24.000.000) |              (17.600.000) |
| Beban Penyusutan Peralatan Toko           |      (13.750.000) |              (10.000.000) |
| Beban Selisih Kas                         |         (200.000) |                 (100.000) |
| Beban Iklan & Promosi                     |       (8.000.000) |               (6.000.000) |
| Beban Administrasi Bank                   |                 0 |                 (300.000) |
| Beban Bunga Pinjaman                      |      (11.000.000) |               (8.000.000) |
| **Total Beban Operasional (di luar HPP)** | **(332.950.000)** |         **(244.400.000)** |
| **Laba Bersih**                           |    **27.050.000** |            **39.600.000** |

**Catatan penting — kenapa FY2026 (baru 8 bulan) sudah lebih untung dari FY2025 (12 bulan penuh):** omzet naik 10% dari FY2025, TAPI beban Penyusutan & Bunga Pinjaman **TIDAK ikut naik** (aset & jadwal pinjaman tetap) — margin per bulan jadi lebih tebal di FY2026. Kalau mau bandingkan apple-to-apple, hitung **rata-rata laba per bulan**: FY2025 = 27.050.000 / 12 = 2.254.167/bulan, FY2026 YTD = 39.600.000 / 8 = **4.950.000/bulan** — pertumbuhan margin per bulan yang sehat, bukan cuma karena periode lebih pendek.

| Skenario             | Langkah di UI                                                                           | Hasil                                       |
| -------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------- |
| Positif — FY2025     | Buka **Reports → Income Statement**, filter Date From `2025-01-01` Date To `2025-12-31` | Cocok tabel di atas, Laba Bersih 27.050.000 |
| Positif — FY2026 YTD | Ulangi filter Date From `2026-01-01` Date To `2026-08-31`                               | Cocok tabel di atas, Laba Bersih 39.600.000 |
| Netralisasi          | — (laporan read-only)                                                                   |                                             |

## 4. Arus Kas (Cash Flow Statement) — FY2025 vs FY2026 Year-to-Date

**Metode:** langsung (direct method) berbasis `cash_flow_section` per Chart of Account Type (Operating/Investing/Financing — lihat `../accounting/00-...md` §2). "Kas & Setara Kas" di sini = Kas Kecil + Bank BCA gabungan (transfer internal antar keduanya otomatis netral, tidak masuk laporan).

| Aktivitas                                        | FY2025 (Jan-Des) | FY2026 (Jan-Ags) |
| ------------------------------------------------ | ---------------: | ---------------: |
| **Arus Kas Operasi**                             |                  |                  |
| Penerimaan dari pelanggan (tunai)                |    1.065.600.000 |      781.440.000 |
| Pembayaran beban operasional (sewa+gaji+listrik) |    (295.500.000) |    (216.700.000) |
| PPN Masukan atas pembelian aset (dibayar tunai)  |      (6.600.000) |                0 |
| Pencairan pinjaman bank ⚠️                        |      100.000.000 |                0 |
| Pembayaran utang dagang                          |    (671.550.000) |    (527.250.000) |
| Cicilan pinjaman bank (pokok+bunga) ⚠️            |     (55.000.000) |     (40.000.000) |
| Setor PPh 21 karyawan                            |      (4.500.000) |      (2.475.000) |
| Penerimaan piutang dagang                        |                0 |       22.200.000 |
| Beban administrasi bank                          |                0 |        (300.000) |
| Beban iklan & promosi                            |      (8.000.000) |      (6.000.000) |
| Selisih kas opname                               |        (200.000) |        (100.000) |
| **Kas Bersih dari Aktivitas Operasi**            |  **124.250.000** |   **10.815.000** |
| **Arus Kas Investasi**                           |                  |                  |
| Pembelian Peralatan Toko                         |     (60.000.000) |                0 |
| **Kas Bersih dari Aktivitas Investasi**          | **(60.000.000)** |            **0** |
| **Arus Kas Pendanaan**                           |                  |                  |
| Setoran modal awal pemilik                       |      300.000.000 |                0 |
| Prive pemilik                                    |     (10.000.000) |                0 |
| **Kas Bersih dari Aktivitas Pendanaan**          |  **290.000.000** |            **0** |
| **Kenaikan (Penurunan) Kas Bersih**              |  **354.250.000** |   **10.815.000** |
| Saldo Kas Awal Periode                           |                0 |      354.250.000 |
| **Saldo Kas Akhir Periode**                      |  **354.250.000** |  **365.065.000** |

**Verifikasi silang**: Saldo Kas Akhir = Kas Kecil + Bank BCA di Neraca periode yang sama — FY2025: 9.800.000 + 344.450.000 = 354.250.000 ✓. FY2026 YTD: 9.700.000 + 355.365.000 = 365.065.000 ✓.

**⚠️ Temuan yang WAJIB dicek terhadap hasil sistem sungguhan (bukan diasumsikan benar):** akun **2105 Pinjaman Bank Jangka Pendek** ber-tipe **Liabilitas Jangka Pendek**, dan tipe itu di-set `cash_flow_section: operating` untuk SEMUA akun di tipe itu (lihat tabel §2 `../accounting/00-...md`) — artinya **pencairan & cicilan pinjaman bank kemungkinan besar akan muncul di Arus Kas OPERASI, bukan PENDANAAN**, padahal secara akuntansi seharusnya pinjaman bank (utang berbunga jangka pendek/panjang) itu aktivitas **Pendanaan (Financing)**. Ini konsekuensi dari desain sistem yang menyimpan `cash_flow_section` di level **Chart of Account TYPE**, bukan per akun individual — sama seperti temuan serupa yang sudah dicatat di suite `accounting-rumah-sakit/04-...md` (pemisahan pokok vs bunga cicilan pinjaman ke Financing vs Operating). Tabel di atas SENGAJA menempatkan 2 baris pinjaman ini di kolom Operasi (ditandai ⚠️) sebagai simulasi hasil sistem apa adanya — **kalau hasil UI kamu berbeda (mis. ada logika khusus yang mendeteksi akun ini sebagai Financing), berarti sudah ada perbaikan, catat sebagai info positif, bukan gap**.

| Skenario                                           | Langkah di UI                                                                                                                  | Hasil                                                                                                                                                                                                  |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif — Arus Kas FY2025                          | Buka **Reports → Cash Flow Statement**, filter Date From `2025-01-01` Date To `2025-12-31`                                     | Kas Bersih 354.250.000, cocok Neraca §1                                                                                                                                                                |
| Positif — Arus Kas FY2026 YTD                      | Ulangi filter `2026-01-01` s/d `2026-08-31`                                                                                    | Kas Bersih 10.815.000, saldo akhir 365.065.000, cocok Neraca §2                                                                                                                                        |
| **Positif — verifikasi klasifikasi Pinjaman Bank** | Cek section (Operating/Investing/Financing) tempat baris "Pencairan pinjaman bank" & "Cicilan pinjaman bank" muncul di laporan | Bandingkan dengan catatan ⚠️ di atas — laporkan sebagai temuan struktural kalau memang muncul di Operating (bukan bug baru, tapi keterbatasan desain `cash_flow_section` per-Type yang sudah diketahui) |
| Netralisasi                                        | — (laporan read-only)                                                                                                          |                                                                                                                                                                                                        |

## Ringkasan Akhir Suite

- **20 bulan berturut-turut (Januari 2025 - Agustus 2026), 176 jurnal, semua balanced** — cek [`03-general-ledger-trial-balance.id.md`](./03-general-ledger-trial-balance.id.md) §1 untuk Trial Balance final
- **FY2025 sudah Closed** dengan closing entry presisi (Laba Bersih 27.050.000 → Laba Ditahan) — [`04-tutup-periode-dan-tahun-fiskal.id.md`](./04-tutup-periode-dan-tahun-fiskal.id.md)
- **FY2026 masih berjalan** (Laba Berjalan Jan-Ags 39.600.000, belum di-closing-entry-kan) — periode Sep-Des 2026 sudah tersedia (di-generate di file 00) untuk lanjut suite ini kapan pun "bulan berjalan" maju
- Setiap bulan minimal 5 transaksi (2 fundamental + minimal 3 tambahan) — total memenuhi syarat di semua 20 bulan tanpa kecuali

## Referensi Silang

- [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) — master data & modal awal
- [`03-general-ledger-trial-balance.id.md`](./03-general-ledger-trial-balance.id.md) — sumber Trial Balance yang jadi dasar semua angka di file ini
- [`04-tutup-periode-dan-tahun-fiskal.id.md`](./04-tutup-periode-dan-tahun-fiskal.id.md) — closing entry FY2025 yang mengisi Laba Ditahan
- [`../accounting/04-laporan-keuangan.id.md`](../accounting/04-laporan-keuangan.id.md) — versi test case laporan keuangan yang lebih sederhana (1 tahun saja)
- [`../accounting-rumah-sakit/04-laporan-keuangan-per-departemen.id.md`](../accounting-rumah-sakit/04-laporan-keuangan-per-departemen.id.md) — suite lain yang juga mendokumentasikan temuan klasifikasi pokok vs bunga pinjaman di Arus Kas
