---
title: (Hospitality / Hotel) — 04. Laporan Keuangan Konsolidasi & per Departemen
category: accounting-hospitality
description: Neraca (Balance Sheet), Laba Rugi (Income Statement, konsolidasi & breakdown per departemen), dan Arus Kas — direkonsiliasi silang terhadap file 01-02.
visibility: internal
---

# 04. Laporan Keuangan Konsolidasi & per Departemen

> Prasyarat: [`02-general-ledger-trial-balance-per-departemen.id.md`](./02-general-ledger-trial-balance-per-departemen.id.md) — Trial Balance balanced 573.815.000, periode Februari BELUM di-close-fiscal-year (state "sebelum closing", lihat catatan urutan di file `03` §4). Endpoint: `POST reports/{income-statement|balance-sheet|cash-flow-statement}`.

## 1. Neraca / Balance Sheet (**Balance Sheet**)

| Skenario | Payload kunci                                       | Hasil                                                                                                                                                                                                                                                                     |
| -------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `{as_of_date:"2026-02-06"}`                         | 200 — **Total Aset = 573.815.000**; **Total Liabilitas = 138.769.545**; **Total Ekuitas** = Modal Pemilik 452.000.000 + Laba Berjalan (16.954.545) = **435.045.455**; identitas Aset = Liabilitas + Ekuitas → 573.815.000 = 138.769.545 + 435.045.455 = **573.815.000** ✓ |
| Positif  | Cek breakdown `AST-03 Bank Mandiri Valas` di Neraca | Muncul di baris Aset Lancar dengan nilai **162.800.000** (IDR, hasil konversi — laporan keuangan TIDAK menampilkan mata uang asing mentah)                                                                                                                                |

## 2. Laba Rugi / Income Statement (**Income Statement**)

| Skenario                                      | Payload kunci                                                                   | Hasil                                                                                                                                                                                                                                    |
| --------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif — konsolidasi                         | `{start_date:"2026-02-01", end_date:"2026-02-06"}`                              | 200 — Total Pendapatan = 4.545.455+2.000.000+1.500.000 = **8.045.455**; Total Beban = **25.000.000**; **Net Income = (16.954.545)** (rugi)                                                                                               |
| Positif — filter per departemen (DEPT-ROM)    | `{start_date:"2026-02-01", end_date:"2026-02-06", business_unit_id:<DEPT-ROM>}` | 200 — Pendapatan Kamar **4.545.455**, tidak ada beban bertag `DEPT-ROM` di periode ini (Beban Gaji §1.7 tanpa dimensi) → segmen ini profitable murni dari sisi pendapatan tercatat                                                       |
| Positif — filter DEPT-FNB                     | `{..., business_unit_id:<DEPT-FNB>}`                                            | 200 — Pendapatan Restoran **2.000.000**                                                                                                                                                                                                  |
| Positif — filter DEPT-SPA                     | `{..., business_unit_id:<DEPT-SPA>}`                                            | 200 — Pendapatan Spa **1.500.000**                                                                                                                                                                                                       |
| **Positif — verifikasi total per departemen** | Jumlahkan pendapatan 3 filter di atas                                           | 4.545.455+2.000.000+1.500.000 = **8.045.455**, sama persis dengan Total Pendapatan konsolidasi — Beban Gaji (25.000.000, tanpa dimensi) TIDAK ikut ke breakdown manapun, hanya muncul di laporan konsolidasi (perilaku benar, bukan gap) |

## 3. Arus Kas / Cash Flow Statement (**Cash Flow Statement**)

| Skenario                             | Payload kunci                                       | Hasil                                                                                                                                                                                                                                                                    |
| ------------------------------------ | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif                              | `{start_date:"2026-02-01", end_date:"2026-02-06"}`  | 200 — Arus Kas Operasi mencerminkan penerimaan deposit (§1.1, §1.2), penerimaan POS (§1.4, §1.5), dan pembayaran gaji (§1.7); tidak ada aktivitas Investasi/Pendanaan di periode ini (belum ada akuisisi aset — file `05`)                                               |
| Positif — cocok silang dengan Neraca | Kenaikan/penurunan kas bersih dari laporan Arus Kas | HARUS sama dengan selisih saldo kas+bank (`AST-01`+`AST-02`+`AST-03`) sebelum vs sesudah periode: (13.885.000+331.250.000+162.800.000) − (10.000.000+350.000.000+155.000.000) = 507.935.000−515.000.000 = **−7.065.000** — verifikasi angka ini muncul persis di laporan |

## Referensi Silang

- [`01-jurnal-booking-dan-revenue-recognition.id.md`](./01-jurnal-booking-dan-revenue-recognition.id.md) — sumber seluruh angka
- [`03-tutup-periode-bulanan-dan-tahun-fiskal.id.md`](./03-tutup-periode-bulanan-dan-tahun-fiskal.id.md) — angka Laba Rugi di atas berubah signifikan (Pendapatan/Beban jadi 0, Laba Ditahan −16.954.545) setelah Close Fiscal Year §4 dijalankan — jangan dites bersamaan
