---
title: — 02. Transaksi POS Harian
category: Accounting + POS
description: Penjualan POS tunai/kartu/QRIS/split payment, hold & resume order, void, dan refund di 2 toko selama 1 hari operasional — lalu tutup Cash Session di akhir hari.
visibility: internal
---

# 02. Transaksi POS Harian

> Mengasumsikan [`00-...md`](./00-profil-perusahaan-dan-master-data.id.md) dan [`01-setup-toko-warehouse-dan-cash-session.id.md`](./01-setup-toko-warehouse-dan-cash-session.id.md) sudah dikerjakan — kedua Cash Session (Toko Cempaka Putih & Toko Kelapa Dua) harus `status:open` sebelum mulai bagian ini.
>
> **Halaman/Endpoint:** `pos/pos-transactions` (`create`, `void`, `hold`, `resume`, `refund`).

## Ringkasan Transaksi Hari Ini (2026-08-03, Toko Cempaka Putih kecuali disebutkan lain)

| # | Skenario | Item | Payment | Total (approx) |
| --- | --- | --- | --- | --- |
| T1 | Penjualan tunai sederhana | 2x Beras 5kg | Tunai | 130.000 + PPN |
| T2 | Penjualan kartu debit | 5x Minyak Goreng 1L | Kartu Debit/Kredit | 90.000 + PPN |
| T3 | Penjualan QRIS dengan diskon | 3x Indomie Goreng, diskon 10% | QRIS | ~36.450 + PPN |
| T4 | Split payment | 1x Beras + 2x Minyak Goreng | Tunai 50.000 + Kartu sisanya | 101.000 + PPN |
| T5 | Hold lalu Resume | 1x Indomie (pelanggan lupa bawa uang, ditinggal dulu) | Tunai (saat resume) | 13.500 + PPN |
| T6 | Void transaksi salah input | 10x Beras (salah input, seharusnya 1x) | Tunai (dibatalkan sebelum bayar) | 650.000 + PPN |
| T7 | Refund sebagian | Refund 1x Minyak Goreng dari T2 (rusak) | — | −18.000 + PPN |
| T8 (Toko Kelapa Dua) | Penjualan tunai | 4x Beras 5kg | Tunai | 260.000 + PPN |

## 1. Penjualan Tunai — T1

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif | **POS Transactions** → **+ New Sale** → pilih Cash Session Toko Cempaka Putih (auto dari sesi aktif) → tambah 2x "Beras 5kg" → Payment Method "Tunai", Amount Tendered `150.000` → **Complete** | Transaksi `status:completed`, `change_amount` terhitung otomatis (150.000 − total), stok Toko Cempaka Putih Beras berkurang 2 |
| Negatif | Amount Tendered LEBIH KECIL dari total (mis. `100.000` untuk transaksi 130.000+PPN) untuk payment method Tunai | Ditolak — tendered harus ≥ total untuk pembayaran tunai penuh |
| Netralisasi | Void transaksi ini SETELAH selesai testing (§6 di bawah, kalau mau bersihkan) — kalau tidak, biarkan jadi bagian riwayat harian | |

## 2. Penjualan Kartu — T2

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif | New Sale → 5x "Minyak Goreng 1L" → Payment Method "Kartu Debit/Kredit" → **Complete** | `status:completed`, TIDAK ada `change_amount` (kartu selalu pas) |
| Netralisasi | Refund sebagian di §7 (T7) memakai transaksi ini sebagai sumber | |

## 3. Penjualan QRIS dengan Diskon — T3

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif | New Sale → 3x "Indomie Goreng" → apply Discount 10% (kalau ada fitur discount per-transaksi/per-item di POS, gunakan; kalau tidak ada, catat sebagai gap) → Payment Method "QRIS" → generate QR (gateway Midtrans) → simulasikan pembayaran sukses | `status:completed` (atau `pending` menunggu webhook `midtransWebhook`/polling `gatewayStatus` — dokumentasikan alur aktual), `discount_amount` terhitung di subtotal |
| Negatif | QRIS timeout / dibatalkan customer sebelum bayar | Verifikasi: transaksi tetap `pending` selamanya atau ada auto-expire? Catat sebagai temuan kalau tidak ada mekanisme expire | |
| Netralisasi | Tidak perlu reverse, transaksi wajar | |

## 4. Split Payment — T4

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif | New Sale → 1x Beras + 2x Minyak Goreng → di bagian Payment, tambah 2 baris: Tunai `50.000` + Kartu sisanya → **Complete** | `status:completed`, `pos_payments` berisi 2 baris dengan `payment_method_id` berbeda, total keduanya = total transaksi |
| Negatif | Total kedua baris payment TIDAK sama dengan total transaksi (kurang atau lebih) | Ditolak validasi |
| Netralisasi | Tidak perlu reverse | |

## 5. Hold & Resume — T5

**Sebab-akibat:** simulasi pelanggan yang keranjangnya sudah diinput kasir tapi belum bayar (lupa bawa uang, nunggu teman, dll) — kasir bisa `hold` order-nya supaya bisa layani pelanggan lain dulu, lalu `resume` saat pelanggan itu balik.

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif — hold | New Sale → 1x Indomie Goreng → klik **Hold** (belum pilih payment) | Order tersimpan `status:held`, TIDAK mengurangi stok (atau mengurangi — verifikasi behavior aktual, catat sebagai temuan kalau stok berkurang saat hold padahal belum tentu jadi dibeli) |
| Positif — resume | Dari list "Held Orders" → pilih order tadi → **Resume** → lanjutkan bayar Tunai → **Complete** | `status:completed`, keranjang & item sama seperti saat di-hold |
| Negatif | Coba **Resume** order yang sudah `completed`/`voided` | Ditolak |
| Netralisasi | Tidak perlu reverse | |

## 6. Void Transaksi Salah Input — T6

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif | New Sale → 10x Beras (salah input) → SEBELUM bayar, klik **Cancel/Void** (atau kalau harus complete dulu baru void — sesuaikan urutan dengan UI aktual) | Order `status:voided`, stok TIDAK berkurang (kalau void sebelum complete) atau stok dikembalikan (kalau void setelah complete — verifikasi kedua jalur) |
| Positif — void setelah completed | Buat transaksi kecil tunai (mis. 1x Indomie), **Complete**, lalu **Void** dari halaman detail | `status:voided`, verifikasi: apakah Journal yang sudah terposting ikut ke-reverse otomatis (`reverseForDocument()`), dan apakah stok dikembalikan ke `sku_stocks` |
| Negatif | Void transaksi yang statusnya sudah `voided` | Ditolak/idempoten |
| Netralisasi | Tidak perlu apa-apa lagi, void SUDAH jadi bentuk netralisasi | |

## 7. Refund Sebagian — T7 (dari T2)

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif | Buka detail transaksi T2 (5x Minyak Goreng, kartu) → **Refund** → pilih 1x Minyak Goreng sebagai item yang dikembalikan (rusak), alasan "Barang rusak saat dicek pelanggan" → **Process Refund** | `pos_transaction_refunds` + `refund_items` tercatat, stok Minyak Goreng Toko Cempaka Putih bertambah 1, jurnal kontra otomatis terbentuk (mirrored dari `buildPosRefundFunctionalityLines()` — Debit `sales_revenue`, Credit `pos_cash` sebesar nilai refund) |
| Negatif | Refund qty LEBIH BESAR dari qty yang dibeli di transaksi asli (refund 10x padahal beli cuma 5x) | Ditolak validasi over-refund |
| Negatif | Refund transaksi yang sudah `voided` | Ditolak — tidak masuk akal refund transaksi yang batal |
| Netralisasi | Refund SUDAH jadi bentuk netralisasi parsial transaksi asli | |

## 8. Toko Kelapa Dua — T8 (verifikasi isolasi antar toko)

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif | New Sale di Cash Session Toko Kelapa Dua → 4x Beras 5kg → Tunai `300.000` → Complete | `status:completed`, stok yang berkurang HARUS dari warehouse Toko Kelapa Dua, BUKAN Toko Cempaka Putih |
| Negatif | Dari sesi Toko Kelapa Dua, coba jual produk yang stoknya 0 di warehouse itu tapi masih ada di Toko Cempaka Putih | Ditolak — stok per-warehouse, tidak boleh "nyerempet" warehouse toko lain |
| Netralisasi | Tidak perlu reverse | |

## 9. Tutup Cash Session Akhir Hari

Lanjutan dari [`01-setup-toko-warehouse-dan-cash-session.id.md`](./01-setup-toko-warehouse-dan-cash-session.id.md) §4 — sekarang datanya sudah ada untuk dihitung.

| Skenario | Langkah di UI | Hasil |
| --- | --- | --- |
| Positif — hitung expected Cempaka Putih | Buka **Cash Sessions → Report** pada sesi Cempaka Putih SEBELUM close | `expected_balance` = opening (500.000) + total tunai masuk (T1 + porsi tunai T4 + T5 − kalau ada void/refund tunai) — bandingkan dengan hitungan manual dari T1/T4/T5 |
| Positif — close pas | **Close** dengan Closing Balance = `expected_balance` hasil hitungan | `status:closed`, selisih 0 |
| Positif — close Kelapa Dua | **Close** sesi Kelapa Dua dengan Closing Balance sesuai T8 | `status:closed` |
| Netralisasi | Tidak perlu apa-apa lagi — lanjut ke file 03 untuk verifikasi GL | |
