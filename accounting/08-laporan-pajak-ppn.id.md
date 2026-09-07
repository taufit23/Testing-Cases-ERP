---
title: — 08. Laporan Pajak (PPN)
category: Accounting 1
description: Test case reports/tax-summary (rekap PPN Masukan/Keluaran) untuk skenario PT Retail Nusantara Jaya sebagai PKP. Mencakup catatan tegas soal PPh withholding & e-Faktur/e-Bupot yang BELUM diimplementasikan.
visibility: internal
---

# 08. Laporan Pajak (PPN)

> **Cakupan saat ini SENGAJA dipersempit** — hanya rekap PPN Masukan/Keluaran dari `journal_taxes`. **PPh withholding (PPh 21/23/4(2)) dan e-Faktur/e-Bupot export BELUM ADA sama sekali** — jangan laporkan ini sebagai bug, sudah tercatat eksplisit di roadmap (`accounting-module-overhaul-plan.id.md` Phase 4 §4.3 & §4.4, item 4.5.2) sebagai item yang **blocked menunggu klarifikasi jenis PPh & spek DJP dari owner/konsultan pajak** — bukan sesuatu yang bisa ditebak dari testing. Halaman UI: **Reports → Tax Summary** (`/reports/tax-summary`), endpoint di baliknya `POST reports/tax-summary`.

## Konsep Dasar Tambahan (Khusus File Ini)

PPN Keluaran (dipungut dari pelanggan) dan PPN Masukan (dibayar ke supplier) sudah dijelaskan di glosarium file 00. Yang perlu ditambah di sini: **`net_payable`** = PPN Keluaran dikurangi PPN Masukan, dan artinya kebalikan dari intuisi biasa —
- **Positif (net_payable > 0)** = perusahaan MASIH HARUS SETOR selisihnya ke negara (PPN yang dipungut dari pelanggan lebih besar dari yang sudah dibayar ke supplier).
- **Negatif (net_payable < 0)** = perusahaan justru LEBIH BAYAR / punya kredit pajak (PPN Masukan lebih besar) — wajar terjadi di bulan-bulan awal usaha yang banyak belanja stok tapi belum banyak jualan, seperti kasus §8.2 di bawah.

## 8.1 Sumber Data untuk Test Ini

Gunakan transaksi dari [`01-jurnal-manual.id.md`](./01-jurnal-manual.id.md):

| Sumber                                          | Jenis PPN                 | Nominal                                    |
| ----------------------------------------------- | ------------------------- | ------------------------------------------ |
| §1.2 (pembelian tunai persediaan)               | PPN Masukan               | Rp 11.000.000                              |
| §1.3 (penjualan tunai Toko Pusat + Toko Cabang) | PPN Keluaran              | Rp 5.500.000 + Rp 3.300.000 = Rp 8.800.000 |
| §1.9 poin a (pembelian kredit)                  | PPN Masukan               | Rp 8.800.000                               |
| §1.9 poin c (penjualan kredit)                  | PPN Keluaran              | Rp 2.200.000                               |
| §1.9 poin e (retur pembelian)                   | PPN Masukan (mengurangi)  | −Rp 1.100.000                              |
| §1.9 poin f (retur penjualan)                   | PPN Keluaran (mengurangi) | −Rp 550.000                                |

**Total kalau semua transaksi di atas sudah dijalankan**: PPN Masukan = Rp 18.700.000, PPN Keluaran = Rp 10.450.000.

## 8.2 Rekap PPN Masukan/Keluaran (**Tax Summary**)

| Skenario                                                        | Langkah di UI                                                                                                                                                                                        | Hasil                                                                                                                                                                                                                                               |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — minimal (§1.2 & §1.3 saja)                            | Buka **Reports → Tax Summary** (`/reports/tax-summary`) → isi Start Date `2026-01-01`, End Date `2026-01-31` → klik **Run Report**                                                                     | Kartu "Total PPN Masukan" `Rp 11.000.000`, "Total PPN Keluaran" `Rp 8.800.000`, "Net Payable" `-Rp 2.200.000` berwarna hijau/success (negatif = lebih bayar/kredit pajak — wajar untuk bulan pertama usaha yang banyak beli stok awal)                                                             |
| **Positif — lengkap (semua §1.9 poin a/c/e/f ikut dijalankan)** | Sama seperti di atas, tapi perlebar rentang Start Date/End Date supaya mencakup semua transaksi §1.9 → klik **Run Report** lagi                                                | Total PPN Masukan `Rp 18.700.000`, Total PPN Keluaran `Rp 10.450.000`, Net Payable `-Rp 8.250.000`                                                                                                                                                              |
| **Positif — verifikasi klasifikasi otomatis**                   | Setelah Run Report, cek isi tabel "PPN Masukan" dan "PPN Keluaran" di kedua kartu hasil (kolom kode akun, nama akun, nama pajak & rate)                                                      | Baris dari akun `PPN Masukan` (tipe Aset Lancar, category=asset) muncul di kartu/tabel "PPN Masukan"; baris dari akun `PPN Keluaran` (tipe Liabilitas, category=liability) muncul di kartu/tabel "PPN Keluaran" — klasifikasi murni dari `category` akun, bukan nama akun |
| **Positif — retur mengurangi total dengan benar (regression check bug retur menambah bukan mengurangi)** | Jalankan **Run Report** SEBELUM jurnal retur pembelian (§1.9e) di-post, catat "Total PPN Masukan" di kartu, lalu post jurnal retur via [`01-jurnal-manual.id.md`](./01-jurnal-manual.id.md), lalu klik **Run Report** lagi untuk rentang tanggal yang sama | Angka "Total PPN Masukan" di kartu berkurang Rp 1.100.000 setelah retur — **BUKAN bertambah**. Ini regression check untuk bug nyata yang sempat terjadi: `ReportController::taxSummary()` dulu (sebelum 2026-08-10) menjumlah `journal_taxes.amount` tanpa peduli arah debit/kredit baris jurnalnya — baris retur yang MENGKREDITKAN PPN Masukan (untuk menguranginya) malah ikut TERTAMBAH ke total, bukan mengurangi. Sudah difix dengan netting sesuai `normal_balance` akun (asset=debit−credit, liability=credit−debit). Kalau angka "Total PPN Masukan"/"Total PPN Keluaran" naik setelah ada retur (bukan turun), ini regresi ke bug lama — laporkan segera. Angka final yang benar untuk skenario lengkap §8.1 (semua §1.9 poin a/c/e/f) adalah PPN Masukan **Rp 18.700.000**, PPN Keluaran **Rp 10.450.000** — kalau muncul Rp 20.900.000/Rp 11.550.000 (nilai buggy, retur dihitung dua kali karena ditambah bukan dikurangi), itu tanda bug lama kembali |
| Negatif                                                         | Isi Start Date/End Date rentang tanpa transaksi berpajak sama sekali → klik **Run Report**                                                                                                    | Kedua tabel menampilkan "No data", semua kartu total menunjukkan `Rp 0` — bukan error/toast merah                                                                                                                                                          |
| Netralisasi                                                     | — (halaman read-only, tidak ada data yang tersimpan/perlu dihapus)                                                                                                   |

## 8.3 Yang TIDAK Diuji di File Ini (Keterbatasan Disengaja, Bukan Kelalaian)

- **PPh 21/23/4(2) withholding** — tidak ada laporan atau perhitungan otomatis apapun untuk pajak penghasilan yang dipotong dari transaksi (mis. PPh 23 atas jasa dari vendor, PPh 4(2) final atas sewa toko kalau disewa dari pihak lain). Kalau perusahaan butuh ini, harus dicatat manual via jurnal (lihat contoh PPh 21 karyawan di [`01-jurnal-manual.id.md`](./01-jurnal-manual.id.md) §1.9 poin j) — TIDAK ada laporan rekap otomatisnya.
- **e-Faktur / e-Bupot export** — tidak ada fitur export format apapun untuk diunggah ke portal DJP/Coretax. Pencatatan PPN di sistem ini murni untuk kebutuhan pembukuan internal, BUKAN pengganti aplikasi e-Faktur resmi.
- **Kalau owner/konsultan pajak sudah memberi klarifikasi scope** (jenis PPh relevan, format e-Faktur target), file test case baru perlu ditambahkan di sini — JANGAN modifikasi test case §8.1-8.2 di atas untuk "menambah-nambahkan" ekspektasi PPh yang belum diimplementasikan.

## Referensi Silang

- [`../../accounting-module-overhaul-plan.id.md`](../../accounting-module-overhaul-plan.id.md) — Phase 3 item #11 & Phase 4 §4.3 (scope PPN-only disengaja, blocker PPh/e-Faktur)
- [`01-jurnal-manual.id.md`](./01-jurnal-manual.id.md) §1.9 — sumber transaksi PPN yang dipakai file ini
