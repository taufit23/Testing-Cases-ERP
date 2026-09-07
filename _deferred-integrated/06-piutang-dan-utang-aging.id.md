---
title: — DEFERRED. Piutang & Utang (AR/AP Aging)
category: Testing
description: DIPINDAHKAN keluar dari suite testing Accounting standalone (2026-07-31) karena butuh modul Sales/Purchasing (SalesInvoice/PurchaseInvoice) untuk isi data test — akan digarap ulang sebagai bagian test case "Accounting terintegrasi modul lain". Konten di bawah tetap disimpan sebagai draf/referensi.
visibility: internal
---

# DEFERRED — Piutang & Utang (AR/AP Aging)

> ⚠️ **File ini SENGAJA dikeluarkan dari folder `../accounting/` (suite testing Accounting standalone)** per keputusan eksplisit user 2026-07-31: testing Accounting untuk saat ini dibatasi ketat ke ruang lingkup modul Accounting sendiri, TIDAK merembet ke ranah Purchase Order/Sales Order maupun dokumen turunannya (Sales Invoice, Purchase Invoice). Laporan AR/AP Aging (**AR Aging**/**AP Aging**) secara struktural butuh dokumen `SalesInvoice`/`PurchaseInvoice` yang notabene milik modul Sales/Purchasing — jadi tidak bisa masuk suite "berdiri sendiri".
>
> **Status: draf disimpan untuk dipakai ulang nanti**, saat user minta dibuatkan test case "Accounting terintegrasi dengan modul lain" (bukan dihapus). Jangan jalankan test case di bawah ini sampai saat itu tiba — dan saat digarap ulang, kemungkinan besar strukturnya perlu disesuaikan supaya nyambung dengan alur P2P/O2C penuh (lihat `../../testing-flow-core-to-purchasing.id.md`/`../../testing-flow-core-to-sales.id.md`), bukan cuma di-drop begitu saja ke folder aktif.
>
> Konten asli di bawah ini (ditulis 2026-07-31) dibiarkan apa adanya sebagai referensi awal.

---

# 06. Piutang & Utang (AR/AP Aging)

> **Dependensi penting**: laporan ini (**AR Aging**, **AP Aging**) membaca langsung dari model `SalesInvoice`/`PurchaseInvoice` — bukan dari modul Accounting itu sendiri. Artinya untuk mengisi data test di file ini, perlu ada dokumen Sales Invoice (modul Sales) dan Purchase Invoice (modul Purchasing, **saat ini WAJIB punya Purchase Order** — lihat `accounting-module-overhaul-plan.id.md` Phase 5 §5.1.C untuk rencana bikin ini opsional). Kalau modul Sales/Purchasing belum ditest terpisah, lihat [`../../testing-flow-core-to-purchasing.id.md`](../../testing-flow-core-to-purchasing.id.md) dan [`../../testing-flow-core-to-sales.id.md`](../../testing-flow-core-to-sales.id.md) untuk setup dasarnya dulu.
>
> Prasyarat: Contact customer "PT Mitra Grosir Indonesia" & supplier "CV Sumber Pangan Nusantara" dari §00 sudah ada. Akun `Piutang Dagang` (1103) & `Utang Dagang` (2101) sudah ber-flag `is_ar_control_account`/`is_ap_control_account`.

## 6.1 Siapkan Variasi Piutang (AR) — 5 Invoice dengan Umur Berbeda

Asumsi tanggal "hari ini" testing = **2026-03-15**. Buat 5 Sales Invoice ke "PT Mitra Grosir Indonesia" dengan tanggal jatuh tempo berbeda supaya masuk ke 5 bucket aging yang berbeda:

| #   | Tanggal Invoice | Jatuh Tempo | Total         | Status Bayar                                       | Bucket yang diharapkan                                  |
| --- | --------------- | ----------- | ------------- | -------------------------------------------------- | ------------------------------------------------------- |
| 1   | 2026-03-10      | 2026-03-25  | Rp 15.000.000 | Belum bayar                                        | **Current** (belum jatuh tempo)                         |
| 2   | 2026-02-20      | 2026-03-07  | Rp 22.000.000 | Belum bayar                                        | **1-30 hari** (telat ~8 hari dari 15 Maret)             |
| 3   | 2026-01-25      | 2026-02-09  | Rp 18.500.000 | Belum bayar                                        | **31-60 hari** (telat ~34 hari)                         |
| 4   | 2025-12-20      | 2026-01-04  | Rp 30.000.000 | Belum bayar                                        | **61-90 hari** (telat ~70 hari)                         |
| 5   | 2025-11-01      | 2025-11-16  | Rp 12.000.000 | Belum bayar                                        | **90+ hari** (telat ~119 hari)                          |
| 6   | 2026-03-01      | 2026-03-16  | Rp 8.000.000  | **Lunas penuh**                                    | Tidak boleh muncul di aging sama sekali                 |
| 7   | 2026-02-01      | 2026-02-16  | Rp 20.000.000 | **Bayar sebagian** (Rp 12.000.000 dari 20.000.000) | Sisa Rp 8.000.000 masuk bucket sesuai umur (31-60 hari) |

## 6.2 AR Aging (**AR Aging**)

| Skenario                                                    | Payload                                                                                                                              | Hasil                                                                                                                                                                                                                                 |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                                     | `POST reports/ar-aging {as_of_date:"2026-03-15"}`                                                                                    | Baris untuk invoice #1-5 & sisa invoice #7 muncul, terklasifikasi sesuai bucket di tabel §6.1                                                                                                                                         |
| **Positif — invoice lunas tidak muncul**                    | Cek invoice #6 tidak ada di daftar                                                                                                   | Invoice yang `total <= paid_amount` benar-benar dikeluarkan dari daftar outstanding                                                                                                                                                   |
| **Positif — bayar sebagian**                                | Cek invoice #7                                                                                                                       | Nilai outstanding yang ditampilkan Rp 8.000.000 (sisa), BUKAN Rp 20.000.000 (total awal)                                                                                                                                              |
| **Positif — badge hari terlambat**                          | Cek tiap baris                                                                                                                       | `days_past_due` per invoice sesuai perhitungan manual (as_of_date − due_date)                                                                                                                                                         |
| **Positif — banner rekonsiliasi GL**                        | Cek response bagian reconciliation                                                                                                   | Total AR Aging (jumlah semua outstanding) HARUS SAMA dengan saldo akun `Piutang Dagang` (1103) di GL per `as_of_date` — banner tampil "cocok"/`configured:true` karena akun sudah ber-flag `is_ar_control_account` (fix Phase 4 §4.0) |
| **Negatif — sengaja bikin selisih (test deteksi mismatch)** | Buat 1 jurnal manual yang men-debit langsung akun Piutang Dagang (mis. Rp 5.000.000, tanpa lewat Sales Invoice) → cek ulang AR Aging | Total subledger (dari invoice) vs GL (termasuk jurnal manual tadi) sekarang **selisih Rp 5.000.000** — banner harus mendeteksi ini sebagai mismatch, bukan diam-diam menampilkan angka yang salah                                     |
| Netralisasi                                                 | Reverse jurnal manual test di atas; jangan hapus invoice yang sudah dipakai test lain                                                |

## 6.3 Siapkan Variasi Utang (AP) — Pola Sama, Sisi Supplier

Ulangi pola §6.1 tapi untuk Purchase Invoice ke "CV Sumber Pangan Nusantara" — minimal 3 variasi cukup (current, 31-60 hari, lunas) untuk membuktikan pola yang sama jalan di sisi AP:

| #   | Tanggal Invoice | Jatuh Tempo | Total         | Status Bayar | Bucket       |
| --- | --------------- | ----------- | ------------- | ------------ | ------------ |
| 1   | 2026-03-05      | 2026-04-04  | Rp 40.000.000 | Belum bayar  | Current      |
| 2   | 2026-01-20      | 2026-02-19  | Rp 25.000.000 | Belum bayar  | 31-60 hari   |
| 3   | 2026-02-25      | 2026-03-27  | Rp 10.000.000 | Lunas penuh  | Tidak muncul |

## 6.4 AP Aging (**AP Aging**)

| Skenario                      | Payload                                                 | Hasil                                                                                   |
| ----------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Positif                       | `POST reports/ap-aging {as_of_date:"2026-03-15"}`       | Sama polanya dengan §6.2 — invoice #1-2 muncul di bucket masing-masing, #3 tidak muncul |
| Positif — banner rekonsiliasi | Total AP Aging = saldo akun `Utang Dagang` (2101) di GL | `configured:true`                                                                       |
| Netralisasi                   | —                                                       |

## 6.5 Cross-Check dengan Jurnal Manual (§01.9 poin a-d)

Kalau file [`01-jurnal-manual.id.md`](./01-jurnal-manual.id.md) §1.9 poin a-d sudah dites (pembelian/penjualan kredit + pelunasan via jurnal manual, BUKAN via dokumen Sales/Purchase Invoice), **JANGAN campur** kedua sumber data ini dalam satu perhitungan reconciliation — poin a-d di file 01 juga menyentuh akun Piutang/Utang Dagang tapi TIDAK tercatat sebagai `SalesInvoice`/`PurchaseInvoice`, jadi tidak akan muncul di AR/AP Aging report sama sekali (report ini murni baca dari 2 model itu, bukan dari GL). Ini **pembeda penting** yang perlu dipahami tester:

- **AR/AP Aging** = berbasis dokumen invoice (per-customer/supplier, per-invoice detail, ada `days_past_due`).
- **Saldo Piutang Dagang/Utang Dagang di GL** = berbasis SEMUA jurnal yang pernah menyentuh akun itu, termasuk dari jurnal manual di luar invoice.

Kalau keduanya dipakai bersamaan (invoice DAN jurnal manual sama-sama posting ke akun yang sama), banner rekonsiliasi §6.2/§6.4 akan menunjukkan mismatch — itu **kondisi nyata**, bukan bug, karena AR Aging memang tidak pernah tahu soal jurnal manual di §01.9. Dokumentasikan sebagai keterbatasan desain kalau ditemukan saat testing gabungan.

## Referensi Silang

- [`../../accounting-module-overhaul-plan.id.md`](../../accounting-module-overhaul-plan.id.md) — Phase 3 item #12 (AR/AP Aging full-stack), Phase 4 §4.2.A (bug ChartOfAccounts field-drop yang dulu bikin banner selalu "not configured" — SUDAH DIPERBAIKI), Phase 5 §5.1.C (rencana PurchaseInvoice standalone tanpa PO wajib)
- [`01-jurnal-manual.id.md`](./01-jurnal-manual.id.md) §1.9 — jalur alternatif pencatatan piutang/utang via jurnal manual (beda sumber data, lihat §6.5)
