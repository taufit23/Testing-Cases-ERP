---
title: — 07. Rekonsiliasi Bank
category: Accounting 1
description: Test case Bank Reconciliation untuk skenario PT Retail Nusantara Jaya — beberapa variasi selisih saldo buku vs rekening koran yang umum terjadi di ritel (biaya admin bank, setoran dalam perjalanan, transfer belum cair).
visibility: internal
---

# 07. Rekonsiliasi Bank

> Endpoint **Bank Accounts** dan **Bank Reconciliations** (namespace `Finance`). **Cakupan saat ini header-level saja** — selisih saldo dicatat manual per bulan, BELUM ada matching baris transaksi ke GL otomatis (tabel `bank_reconciliation_lines` ada di skema tapi belum dipakai controller). Ini bukan bug, sudah tercatat di roadmap (`accounting-module-overhaul-plan.id.md` Phase 5 §5.3 Fase 4).

## Konsep Dasar Tambahan (Khusus File Ini)

**Rekonsiliasi bank** = proses mencocokkan 2 catatan yang HARUSNYA sama tapi seringkali beda karena beda waktu pencatatan: **saldo buku** (`closing_balance`, angka di sistem ERP ini, dari GL) vs **saldo rekening koran** (`statement_balance`, angka resmi dari bank). Kalau tidak persis sama, itu bukan otomatis berarti ada yang salah — selisihnya biasanya karena TIMING, bukan kesalahan (lihat 3 contoh kasus umum di §7.3: biaya admin bank yang belum sempat dicatat di buku, setoran yang sudah dicatat tapi belum "nongol" di rekening koran, atau transfer keluar yang sudah dicatat tapi uangnya belum benar-benar terpotong bank). Tujuan proses ini adalah MEMASTIKAN selisihnya bisa dijelaskan semua — bukan memaksa kedua angka jadi identik.

## 7.1 Setup Bank Account

| Skenario    | Langkah di UI                                                                                                                                                                                                                                                                                                                                                                                                     | Hasil                                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Positif     | Buka **Finance → Bank Accounts** (`/finance/bank-accounts`) → klik **+ Create Bank Account** → isi Account Name `BCA Operasional`, Bank Name `Bank Central Asia`, Account Number `1234567890`, pilih Currency IDR, Opening Balance `0`, pilih Chart of Account `Bank BCA 1102` → klik **Save**                                                                                                                | Toast sukses "Bank account created" → baris baru muncul di tabel list, terhubung ke COA Bank BCA yang sudah dipakai di semua jurnal §01      |
| Negatif     | Di form yang sama, pilih Chart of Account yang mengarah ke akun dengan `is_cash_account:false`                                                                                                                                                                                                                                                                                                                    | Cek behavior aktual — idealnya form menolak submit dengan pesan validasi/warning, laporkan kalau ternyata form tetap menyimpan tanpa guard |
| Netralisasi | Buka menu titik-tiga (⋮) di baris akun bank test → **Delete** → konfirmasi di modal — pastikan belum dipakai reconciliation manapun                                                                                                                                                                                                                                                                              | Baris hilang dari list                                                                                            |

## 7.2 Rekonsiliasi Bulan Januari — Skenario "Cocok Sempurna"

Saldo GL Bank BCA akhir Januari 2026 (hasil hitung dari seluruh transaksi §00 §9.3 + §01, dengan asumsi §1.7 sudah mengoreksi sewa ke Rp 18.000.000): **Rp 290.200.000** — rincian:

| Sumber                                         |              Debit |      Kredit |
| ---------------------------------------------- | -----------------: | ----------: |
| Saldo awal (§00 §9.3, `finance/bank-accounts`) |         75.000.000 |             |
| §1.1 Setoran modal awal                        |        500.000.000 |             |
| §1.2 Pembelian persediaan tunai                |                    | 111.000.000 |
| §1.4 Beban sewa toko (setelah koreksi §1.7)    |                    |  18.000.000 |
| §1.4 Beban gaji karyawan                       |                    |  80.000.000 |
| §1.9b Pembayaran utang dagang                  |                    |  40.000.000 |
| §1.9d Penerimaan piutang                       |         22.200.000 |             |
| §1.9g Setor kas ke bank                        |         30.000.000 |             |
| §1.9i Prive pemilik                            |                    |  10.000.000 |
| §1.9j Gaji dengan potongan PPh 21 (net kas)    |                    |  78.000.000 |
| **Saldo akhir (closing_balance)**              | **Rp 290.200.000** |             |

| Skenario           | Langkah di UI                                                                                                                                                                                                                                                                                                                                                                             | Hasil                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| Positif            | Buka **Finance → Bank Reconciliations** (`/finance/bank-reconciliations`) → klik **+ Create** → di form create pilih Bank Account, isi Period Start `2026-01-01`, Period End `2026-01-31`, Opening Balance `0`, Closing Balance `290.200.000`, Statement Balance `290.200.000` (lihat kotak "Difference" di form otomatis terhitung) → klik **Save**, konfirmasi modal save → **Save** | Toast sukses, redirect ke halaman detail — kartu "Difference" menampilkan Rp 0, badge status `draft` |
| Positif — complete | Di halaman detail reconciliation tsb, klik tombol **Complete** di navbar → modal konfirmasi muncul (tombol ini hanya aktif kalau status masih `draft`) → klik **Complete**                                                                                                                                                                                                              | Toast sukses, badge status berubah jadi `completed`             |
| Netralisasi        | Di halaman detail (selama status masih `draft`), klik tombol **Delete** di navbar → konfirmasi di modal                                                                                                                                                                                                                                                                                  | Reconciliation hilang dari list; tombol Delete otomatis disabled kalau status sudah `completed` |

## 7.3 Variasi Selisih — Kasus Umum Retail

Untuk tiap skenario, buka **Finance → Bank Reconciliations → + Create**, isi Bank Account + Period Start/End sama seperti §7.2, lalu isi Closing Balance & Statement Balance sesuai kolom tabel di bawah, perhatikan kotak "Difference" yang otomatis terhitung live di form sebelum **Save** (jangan campur skenario dalam 1 reconciliation, supaya jelas selisih mana yang diuji):

| #                        | Skenario Selisih                                      | Deskripsi Kasus Nyata                                                                                                                                      | `closing_balance` (buku)    | `statement_balance` (rekening koran) | `difference` yang diharapkan                                                                            |
| ------------------------ | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| a                        | **Biaya admin bank belum dicatat**                    | Bank potong biaya admin bulanan Rp 15.000, belum ada jurnal manual untuk ini                                                                               | Rp 290.200.000 (lihat §7.2) | Rp 290.185.000                       | Rp 15.000 (buku lebih tinggi dari statement)                                                            |
| b                        | **Setoran dalam perjalanan (deposit in transit)**     | Setoran tunai akhir bulan (§01.9 poin g, Rp 30.000.000) sudah dicatat di buku tapi baru efektif di rekening koran 2 hari kemudian (masuk bulan berikutnya) | Rp 290.200.000 (lihat §7.2) | Rp 260.200.000                       | Rp 30.000.000 (buku lebih tinggi, karena setoran belum ter-reflect di statement)                        |
| c                        | **Transfer keluar belum cair (outstanding transfer)** | Pembayaran gaji (§01.4, Rp 80.000.000) sudah dicatat keluar di buku tapi belum terpotong di rekening koran (transfer terjadwal, belum diproses bank)       | Rp 290.200.000 (lihat §7.2) | Rp 370.200.000                       | Rp -80.000.000 (statement lebih tinggi, karena dana belum benar-benar keluar)                           |
| d                        | **Kesalahan input nominal**                           | Akuntan salah input Statement Balance di form (typo, 1 digit kurang)                                                                                       | —                           | (sengaja salah ketik)                | Kotak "Difference" di form/detail menampilkan nilai besar & tidak masuk akal (dan warna berubah merah) — WAJIB dicek manual sebelum klik **Complete**, jangan asal klik selesai |
| Positif (semua poin a-c) | Setelah **Save**, lihat halaman detail reconciliation | Kartu "Difference" di halaman detail sesuai kolom terakhir tabel di atas — pembuktian kalkulasi selisih backend benar                                                                     |
| Netralisasi              | Di halaman detail tiap reconciliation test, klik **Delete** (selama status masih `draft`)        |

## 7.4 Keterbatasan yang Sudah Diketahui

Setelah menemukan selisih (§7.3), sistem **tidak** punya cara mencocokkan baris transaksi individual (mis. tandai "biaya admin Rp 15.000 ini match dengan baris apa") — akuntan cuma bisa mencatat nominal selisih total di level header, lalu membuat jurnal koreksi manual terpisah (`Dr Beban Administrasi Bank / Cr Bank BCA` untuk kasus a) via [`01-jurnal-manual.id.md`](./01-jurnal-manual.id.md). Ini keterbatasan yang sudah diketahui, bukan bug — tercatat di roadmap Fase 4 untuk dibangun (matching baris-ke-GL, WAJIB extend sistem yang ada, bukan sistem baru).

⚠️ **Dikonfirmasi di FE (`finance/bank-reconciliations/[slug].vue`)**: bagian "Reconciliation Lines" di halaman detail cuma tabel tampilan read-only (tanggal, deskripsi, nominal, tipe, ikon cleared/tidak) — TIDAK ada checkbox atau tombol aksi apapun untuk mencocokkan baris ke GL. Kalau tester mau memverifikasi ini masih benar-benar belum ada, cukup buka halaman detail reconciliation manapun yang punya baris dan pastikan tidak ada elemen interaktif di tabel tersebut.

## Referensi Silang

- [`../../accounting-module-overhaul-plan.id.md`](../../accounting-module-overhaul-plan.id.md) — Phase 3 item #8 (Bank Reconciliation header-level, peringatan jangan bikin sistem paralel), Phase 5 §5.3 Fase 4 (roadmap line-matching)
- [`01-jurnal-manual.id.md`](./01-jurnal-manual.id.md) — cara mencatat jurnal koreksi hasil temuan rekonsiliasi
