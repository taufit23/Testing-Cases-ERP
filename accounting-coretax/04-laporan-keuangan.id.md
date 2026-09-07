---
title: (CORETAX) — 04. Laporan Keuangan
category: accounting-coretax
description: Neraca, Laba Rugi, dan Arus Kas untuk branch Pusat setelah transaksi file 01, sebelum dan sesudah tutup periode Agustus.
visibility: internal
---

# 04. Laporan Keuangan

> Prasyarat: [`01`](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md)-[`03`](./03-tutup-periode-dan-tahun-fiskal.id.md).

## 1. Laba Rugi (Income Statement)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Laba Rugi periode Agustus 2026 | `reports/income-statement {date_from:"2026-08-01", date_to:"2026-08-31"}` | Revenue = `4001` 22.000.000 + `4501` 3.000.000 = **25.000.000**; Expense = `5001` 27.000.000 (Pembelian) + `5501` 20.000.000 (Beban Gaji) + `5502` 2.650.000 (Beban Operasional Lainnya) = **49.650.000**; **Net Income = 25.000.000 − 49.650.000 = −24.650.000 (rugi)** — cocokkan persis dengan [ringkasan file 01](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md#ringkasan-saldo-setelah-file-01-t1-t14-posted-t2-di-reverse--dari-seeder) |
| Laba Rugi setelah close Agustus | Endpoint sama, cek apakah hasil beda sebelum/sesudah closed (ekspektasi sama persis, closing cuma ngunci input baru bukan ubah angka historis) | Identik dengan baris di atas |
| **Verifikasi formula HPP** | Cek apakah `reports/income-statement` menjumlah SEMUA akun `category:expense` flat (termasuk `5001` Pembelian ATAU malah `5008`/`5009` Persediaan Awal/Akhir, berpotensi double-count kalau keduanya kejumlah), atau ada formula COGS = Persediaan Awal + Pembelian − Persediaan Akhir yang mengeliminasi salah satunya | Belum terverifikasi dari pembacaan kode — angka Expense 49.650.000 di atas ASUMSI flat-sum semua akun expense yang tersentuh transaksi (`5001`+`5501`+`5502`, TIDAK termasuk `5008` karena tidak ada transaksi ke situ di file 01). Kalau hasil aktual beda, itu bukan bug — cukup catat formula sebenarnya |

## 2. Neraca (Balance Sheet)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Neraca per 2026-08-31 | `reports/balance-sheet {as_of:"2026-08-31"}` | Total Aset = Total Liabilitas + Ekuitas — **verifikasi apakah rugi bersih (−10.000.000) sudah tercermin** di sisi Ekuitas (biasanya lewat Laba Ditahan berjalan / current-period earnings), sebelum Close Fiscal Year benar-benar dilakukan (closing entry belum terjadi di titik ini karena FY2026 sengaja belum di-close, lihat file 03 §4) |
| `is_balanced` flag | Field `is_balanced` di response | Harus `true` — kalau `false`, ini bug nyata (dashboard endpoint `dashboard/accounting/list` juga expose flag yang sama, lihat `outputTest.json` contoh session lain — cross-check kalau ada penyimpangan) |

## 3. Arus Kas (Cash Flow Statement)

| Skenario | Payload kunci | Hasil |
| --- | --- | --- |
| Arus Kas Agustus 2026, metode langsung | `reports/cash-flow-statement {date_from:"2026-08-01", date_to:"2026-08-31"}` | Operating: T3 (+11.100.000 penjualan tunai), T4 (−18.500.000 gaji) → verifikasi T1 (setoran modal 50jt) masuk **Financing**, bukan Operating (akun `3101` Modal punya `cash_flow_section: financing` dari `chart_of_accounts_types` — lihat file 00 §1). T5 (pelunasan piutang 30jt) — cek section-nya (biasanya Operating karena akun sumber `1121` Piutang bertipe `DAGANG-ASSET` dengan `cash_flow_section: operating`) |
| Akun kas yang dihitung | Field `is_cash_account` cuma di `1101`&`1102` (lihat file 00 §2) | Pastikan laporan HANYA menjumlah pergerakan 2 akun ini sebagai "kas", bukan semua akun `DAGANG-ASSET` |

## Referensi Silang

- [`01-jurnal-manual-dan-verifikasi-saldo-awal.id.md`](./01-jurnal-manual-dan-verifikasi-saldo-awal.id.md) — sumber angka
- [`02-general-ledger-dan-trial-balance.id.md`](./02-general-ledger-dan-trial-balance.id.md) — Trial Balance harus konsisten dengan Neraca di sini
