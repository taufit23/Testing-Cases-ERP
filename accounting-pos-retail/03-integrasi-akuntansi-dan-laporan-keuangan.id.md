---
title: — 03. Integrasi Akuntansi & Laporan Keuangan
category: Accounting + POS
description: Verifikasi Journal & General Ledger yang terbentuk otomatis dari transaksi POS di file 02, Trial Balance, tutup periode, dan Laporan Keuangan — termasuk catatan wajib soal gap HPP/COGS yang TIDAK diposting otomatis oleh POS.
visibility: internal
---

# 03. Integrasi Akuntansi & Laporan Keuangan

> Mengasumsikan [`00-...md`](./00-profil-perusahaan-dan-master-data.id.md), [`01-...md`](./01-setup-toko-warehouse-dan-cash-session.id.md), dan [`02-transaksi-pos-harian.id.md`](./02-transaksi-pos-harian.id.md) sudah dikerjakan.

## ⚠️ Catatan Wajib: POS TIDAK Memposting HPP/COGS Otomatis

**Sebab-akibat:** sama seperti gap yang sudah didokumentasikan di suite Sales (`sales/02-so-integrasi-accounting.id.md` dan `sales-coretax/02-so-integrasi-accounting.id.md`), `JournalPostingService::buildPosTransactionFunctionalityLines()` HANYA memposting 3 baris — Debit `pos_cash`, Credit `sales_revenue`, Credit `ppn_keluaran`. **Tidak ada baris Debit HPP / Credit Persediaan** karena tidak ada kolom cost/average-cost per produk di sistem ini.

**Konsekuensi yang HARUS diverifikasi saat testing:**

- Akun **1104 Persediaan Barang Dagang** TIDAK akan pernah berkurang otomatis dari transaksi POS manapun di file 02 — saldonya tetap 40.000.000 (dari §7 file 00) walau stok fisik (`sku_stocks`) sudah berkurang lewat mekanisme inventory terpisah.
- Akun **5101 Harga Pokok Penjualan** akan tetap 0 kecuali diisi manual.
- Kalau mau Laba Rugi mencerminkan margin kotor sungguhan, HARUS ditambah jurnal manual "Pengakuan HPP" (pola sama seperti `accounting-retail-tahun-berjalan/`) — opsional, dokumentasikan di §5 kalau mau dites.

## 1. Verifikasi Journal per Transaksi POS

**Halaman:** `accounting/journals` — cari jurnal dengan referensi ke `pos_transactions` (biasanya muncul di description/reference field, cek pola aktual).

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif — T1 (tunai) | Buka Journal hasil T1 (130.000 + PPN 11% = 14.300) | Debit `<Kas Hasil Penjualan POS>` 144.300; Credit `<Penjualan Barang Dagang>` 130.000; Credit `<PPN Keluaran>` 14.300 — Balanced |
| Positif — T3 (QRIS + diskon) | Buka Journal hasil T3 | Credit `sales_revenue` = subtotal SETELAH diskon (bukan sebelum) — pastikan `discount_amount` sudah dikurangi sebelum PPN dihitung |
| Positif — T4 (split payment) | Buka Journal hasil T4 | HANYA 1 baris Debit `pos_cash` sebesar TOTAL (gabungan tunai+kartu) — TIDAK terpecah 2 baris per metode pembayaran (sesuai catatan verifikasi §5 file 00) |
| Positif — T6 (void setelah completed) | Cek Journal dari transaksi yang di-void di file 02 §6 | Journal asli sudah di-reverse (additive, bukan dihapus — pola sama seperti `Journal::reverse()`) sehingga saldo `pos_cash`/`sales_revenue`/`ppn_keluaran` net kembali ke posisi sebelum transaksi itu |
| Positif — T7 (refund) | Cek Journal kontra dari refund | Debit `<Penjualan Barang Dagang>` (mengurangi revenue) dan/atau Credit `<Kas Hasil Penjualan POS>` sebesar nilai refund (1x Minyak Goreng + PPN-nya) — bukan Debit HPP (karena HPP memang tidak pernah diposting, lihat catatan di atas) |
| Negatif | Coba **Reverse manual** salah satu Journal hasil POS dari halaman Journals (di luar alur void resmi) | Verifikasi: apakah sistem membiarkan reverse manual terhadap jurnal yang sumbernya otomatis dari POS — kalau ya, catat sebagai potensi gap (jurnal POS jadi tidak sinkron dengan status transaksi POS-nya) |
| Netralisasi | Tidak perlu reverse manual — semua sudah konsisten lewat alur void/refund resmi | |

## 2. Trial Balance

**Halaman:** `accounting/general-ledger/trial-balance`, filter periode Agustus 2026.

Hitung manual dulu total yang diharapkan dari seluruh transaksi file 02 (jumlahkan tiap Debit `pos_cash` dari T1-T5+T8, dikurangi void T6 dan refund T7) sebelum buka Trial Balance, supaya ada acuan pembanding.

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif | Buka Trial Balance Agustus 2026 | Total Debit = Total Kredit (`is_balanced:true`); saldo `<Kas Hasil Penjualan POS>` = akumulasi net semua transaksi POS completed (T1+T2+T3+T4+T5+T8, dikurangi T6-void dan T7-refund) |
| Positif — filter per toko | Buka **Summary by Account**, filter `business_unit_id = BU-CP` | Hanya transaksi Toko Cempaka Putih (T1-T7) yang muncul, T8 (Kelapa Dua) TIDAK ikut |
| Negatif | Filter Trial Balance ke periode SEBELUM Agustus 2026 (mis. Juli 2026) | Kosong — tidak ada transaksi karena perusahaan baru mulai 1 Agustus 2026 (§Profil file 00) |
| Netralisasi | Tidak ada, murni report read-only | |

## 3. Tutup Periode Agustus 2026

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif | **Accounting Period** → periode Agustus 2026 → **Close** | `is_closed:true` |
| Negatif | Coba buat transaksi POS baru (New Sale) setelah periode Agustus ditutup, tanggal transaksi masih 2026-08-xx | Verifikasi: apakah `pos-transactions/create` ikut cek Accounting Period terbuka seperti Journal manual, atau POS tidak terikat validasi periode sama sekali (celah kalau ternyata tidak dicek) — catat sebagai temuan |
| Negatif | Coba **Void**/**Refund** transaksi POS yang jurnalnya ada di periode yang SUDAH closed | Verifikasi: ditolak (immutability periode closed) atau tetap diizinkan (celah) |
| Netralisasi | **Reopen** periode kalau perlu lanjut testing lebih jauh | |

## 4. Laporan Keuangan

**Halaman:** `reports/income-statement`, `reports/balance-sheet`, `reports/cash-flow-statement`.

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif — Laba Rugi | Buka Income Statement Agustus 2026 | Pendapatan = total `sales_revenue` net (setelah void/refund); Beban HPP = 0 (lihat catatan wajib di atas) — Laba Kotor = Laba Bersih (tidak realistis secara bisnis, TAPI benar sesuai desain sistem saat ini) |
| Positif — Neraca | Buka Balance Sheet per 2026-08-31 | Kas Hasil Penjualan POS + Bank BCA + Kas Kecil + Persediaan (tetap 40.000.000, tidak berkurang) + Peralatan Toko = Modal Pemilik + Laba Berjalan |
| Positif — Arus Kas | Buka Cash Flow Statement | Seluruh penerimaan POS masuk Arus Kas Operasi (`cash_flow_section` akun 1103 harus `operating`) | 
| Negatif | Filter laporan keuangan per toko (`business_unit_id`) | Verifikasi: apakah `reports/income-statement` dkk mendukung filter dimensi ini (pola di suite lain menunjukkan endpoint `reports/*` UMUMNYA TIDAK mendukung filter business unit, hanya `accounting/general-ledger/summary-by-account` yang mendukung — cek §2 di atas sebagai gantinya) |
| Netralisasi | Tidak ada, murni report read-only | |

## 5. (Opsional) Jurnal Manual Pengakuan HPP

Kalau mau menguji margin kotor yang realistis (bukan wajib untuk suite ini, tapi berguna untuk membandingkan dengan pola `accounting-retail-tahun-berjalan/`):

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif | Hitung manual HPP dari qty terjual (harga modal per SKU, misal asumsikan margin 30% dari harga jual) → Create Journal manual, Date `2026-08-03`, Description "Pengakuan HPP penjualan harian" → Debit `<Harga Pokok Penjualan>`, Credit `<Persediaan Barang Dagang>` sebesar HPP terhitung → Post | Persediaan berkurang manual, Laba Rugi mencerminkan margin kotor sungguhan |
| Netralisasi | Reverse jurnal ini kalau cuma mau demonstrasi, bukan bagian permanen suite | |

## Ringkasan Verifikasi yang Wajib Dicatat Hasilnya

- [ ] Journal per transaksi POS (tunai/kartu/QRIS/split/void/refund) sesuai §1
- [ ] Trial Balance balanced, saldo `pos_cash` sesuai hitungan manual (§2)
- [ ] Temuan: apakah split payment/kartu/QRIS semua masuk 1 akun `pos_cash` yang sama (§5 file 00 & §1 di atas) — dan apakah ini seharusnya dipisah per metode pembayaran
- [ ] Temuan: apakah `pos-transactions/create`/`void`/`refund` menghormati Accounting Period closed (§3)
- [ ] Konfirmasi eksplisit: Persediaan & HPP TIDAK bergerak otomatis dari POS (§ Catatan Wajib di atas) — dampaknya ke Laba Rugi & Neraca
