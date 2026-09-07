---
title: (Construction / Project Based) — 05. Aset Tetap (Alat Berat) & Anggaran
category: accounting-construction
description: Register Excavator sebagai Fixed Asset (garis lurus), jalankan penyusutan bulanan, pelepasan aset, dan Budget vs Actual per proyek PT Bangun Persada.
visibility: internal
---

# 05. Aset Tetap (Alat Berat) & Anggaran

> Endpoint Fixed Assets: **Assets — `{list|show|create|update|delete|calculate-depreciation|run-depreciation}`**, **Disposals — `{list|show|create|delete}`** (semua `POST` kecuali `update`=`PUT`, `delete`=`DELETE`). Endpoint Budget: **Budgets — `{list|show|create|update|delete|vs-actual}`**.
>
> Istilah dasar aset tetap/penyusutan (nilai residu, masa manfaat, book value, garis lurus) dan Budget vs Actual/variance sudah dijelaskan di `../accounting/06-aset-tetap-dan-penyusutan.id.md` dan `../accounting/05-anggaran-budget.id.md`. Istilah baru khusus di file ini: **Gain/Loss Pelepasan Aset** dan **Variance Favorable/Unfavorable**, dijelaskan di `00-profil-perusahaan-dan-master-data.id.md` §"Istilah Khusus Proyek Konstruksi".

## 1. Register Aset Tetap — Excavator (**Assets — `create`**)

| Field                     | Nilai                                  |
| ------------------------- | -------------------------------------- |
| `name`                    | Excavator Komatsu PC200                |
| `category`                | `equipment`                            |
| `acquisition_date`        | 2026-01-10                             |
| `acquisition_cost`        | 900.000.000                            |
| `salvage_value`           | 60.000.000                             |
| `useful_life_months`      | 60 (5 tahun)                           |
| `depreciation_method`     | `straight_line`                        |
| `asset_account_id`        | AST-05 Alat Berat (Excavator)          |
| `depreciation_account_id` | BBN-03 Beban Penyusutan Alat Berat     |
| `accum_dep_account_id`    | AST-06 Akumulasi Penyusutan Alat Berat |

Penyusutan bulanan garis lurus = (900.000.000 − 60.000.000) / 60 = **14.000.000/bulan**.

> Catatan: **Assets — `create`** TIDAK punya field `business_unit_id` — model `FixedAsset` tidak menyimpan dimensi proyek sama sekali (lihat validator `FixedAssets::create()`). Kalau alat berat dipakai bergantian di 2 proyek, sistem TIDAK bisa mengalokasikan biaya penyusutannya per proyek secara otomatis — dokumentasikan sebagai keterbatasan, jangan buat test case yang mengharap breakdown penyusutan per Business Unit.

> **Kontrak field asli Assets — `create`** (verifikasi baca kode langsung, `App\Http\Controllers\Finance\FixedAssets::create()`): `asset_code` TIDAK bisa diisi manual — server SELALU generate sendiri format `FA/{tahun}/{urutan}`, field ini di-strip diam-diam kalau dikirim di payload. `category` HANYA menerima salah satu dari 6 nilai fix: `land|building|vehicle|equipment|furniture|intangible` — payload §1 di atas sudah pakai `equipment` yang valid. Nama field nilai sisa yang benar adalah `salvage_value` (bukan `residual_value`). `current_book_value` saat registrasi = **full `acquisition_cost`** (BUKAN dikurangi `salvage_value` di muka) — book value baru turun setelah penyusutan beneran di-run.

**Sebab-akibat:** karena alat berat tidak bisa dipecah kepemilikannya per proyek (lihat catatan di atas), kalau Excavator ini nanti dipakai bergantian di PRJ-GDA dan PRJ-JMB, biaya penyusutannya akan SELALU numpuk ke satu tempat (tidak terhubung `business_unit_id` sama sekali) — laporan Laba Rugi per proyek (kalau nanti dibuat manual lewat filter GL seperti catatan gap di file 04) TIDAK akan pernah menampilkan beban penyusutan alat berat di proyek manapun secara otomatis. Ini bukan salah input, murni keterbatasan struktur data yang harus disiasati manual (mis. jurnal alokasi manual per proyek berdasarkan estimasi pemakaian) kalau memang dibutuhkan akurasi biaya per proyek.

## 2. Skenario Pengujian — Fixed Assets & Depresiasi

| Skenario | Detail                                                                                                       | Hasil                                                                                                                                                                                                                                                                                                                 |
| -------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `fixed-assets/assets/create` dengan payload §1.                                                              | 201, `asset_code` auto-generate format `FA/2026/0001`, `current_book_value` = **900.000.000** (= full `acquisition_cost`, `salvage_value` belum dipotong sama sekali karena belum ada penyusutan berjalan), `accumulated_depreciation: 0`, `status: active`.                                                                                 |
| Positif  | `fixed-assets/assets/calculate-depreciation` dengan `as_of_date: 2026-03-31`.                                | Read-only, mengembalikan `schedule` 2 baris (Feb, Mar 2026 — bulan pertama dihitung mulai bulan SETELAH `acquisition_date`), masing-masing `depreciation_amount: 14.000.000`, `book_value_after` turun 14jt tiap baris — TIDAK menulis apapun ke DB.                                                                  |
| Positif  | `fixed-assets/assets/run-depreciation` dengan `period_date: 2026-02-01`.                                     | 201, `AssetDepreciation` row terbuat (`depreciation_amount: 14.000.000`, `book_value_after: 826.000.000`), asset `current_book_value` ter-update, DAN jurnal 2-baris otomatis terbuat+posted (Dr BBN-03 14.000.000 / Cr AST-06 14.000.000) karena `depreciation_account_id`+`accum_dep_account_id` sudah diisi di §1. |
| Positif  | `run-depreciation` lagi dengan `period_date: 2026-02-01` (periode yang sama).                                | `skipped: 1, created: 0` — idempotent, tidak dobel posting untuk periode yang sama.                                                                                                                                                                                                                                   |
| Positif  | `run-depreciation` dengan `period_date: 2026-03-01`.                                                         | `created: 1`, `book_value_after: 812.000.000`, jurnal kedua terbuat.                                                                                                                                                                                                                                                  |
| Negatif  | `fixed-assets/assets/create` tanpa `depreciation_account_id`/`accum_dep_account_id`.                         | 201 tetap berhasil (field-field itu `nullable`) TAPI `run-depreciation` untuk aset ini akan skip posting jurnal (asset tetap dibuat `AssetDepreciation`-nya, `is_posted` tetap `false`) — dokumentasikan sebagai silent partial-success, bukan error keras.                                                           |
| Negatif  | `fixed-assets/assets/delete` untuk aset yang sudah punya riwayat `AssetDepreciation` dan `status != active`. | Error "content.cannot_delete_has_depreciations".                                                                                                                                                                                                                                                                      |
| Negatif  | `run-depreciation` untuk aset dengan `current_book_value <= salvage_value` (sudah fully depreciated).        | `skipped` bertambah, tidak membuat baris baru — aset tidak disusutkan di bawah nilai residu.                                                                                                                                                                                                                          |

**Sebab-akibat:** baris "idempotent" (`run-depreciation` diulang untuk periode yang sama) itu pengaman penting — kalau tidak ada, klik tombol dua kali tanpa sengaja akan membebankan penyusutan DOBEL untuk bulan yang sama, bikin Beban Penyusutan di Laba Rugi kelewat besar dan `current_book_value` turun lebih cepat dari yang seharusnya. Baris "tanpa `depreciation_account_id`" juga penting diperhatikan: aset TETAP bisa dibuat & disusutkan (tercatat di `AssetDepreciation`) walau tidak pernah masuk GL — kalau ini terjadi tanpa disadari, `current_book_value` di halaman Aset akan turun tapi Neraca (file 04) tidak pernah berubah, dua sumber data jadi tidak sinkron.

## 3. Pelepasan Aset (**Disposals — `create`**)

Skenario: Excavator dijual setelah 3 bulan penyusutan (Feb-Apr 2026, asumsikan bulan April juga sudah di-run, `current_book_value` = 798.000.000), dijual seharga 750.000.000.

| Field               |          Nilai |
| ------------------- | -------------: |
| `fixed_asset_id`    | (id Excavator) |
| `disposal_date`     |     2026-04-15 |
| `disposal_type`     |         `sold` |
| `disposal_proceeds` |    750.000.000 |

Gain/Loss = 750.000.000 − 798.000.000 = **rugi pelepasan 48.000.000**.

| Skenario                                       | Detail                                                                                               | Hasil                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif                                        | `fixed-assets/disposals/create` dengan payload di atas.                                              | 201, `book_value_at_disposal: 798.000.000`, `gain_loss: -48.000.000`, asset `status` berubah jadi `sold`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Negatif (GAP nyata, bukan test case biasa)** | Cek apakah rugi pelepasan 48.000.000 otomatis masuk ke GL/jurnal.                                    | **TIDAK** — `AssetDisposals::create()` (`app/Http/Controllers/Finance/AssetDisposals.php`) HANYA menyimpan row `asset_disposals` dan mengubah `status` aset; tidak ada pemanggilan `JournalPostingService` sama sekali. Rugi/laba pelepasan harus diposting MANUAL lewat `accounting/journals/create` (mis. Dr Bank 750.000.000, Dr Akumulasi Penyusutan 102.000.000 [900jt−798jt book value tersisa dari cost, sesuaikan dengan accumulated_depreciation aktual], Dr Rugi Pelepasan Aset 48.000.000 / Cr Alat Berat 900.000.000) — dokumentasikan sebagai keterbatasan fitur untuk suite ini, jangan asumsikan GL otomatis konsisten setelah disposal. |
| Negatif                                        | `fixed-assets/disposals/create` untuk aset dengan `status != active` (mis. sudah `sold` sebelumnya). | Error "content.asset_not_active".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

**Sebab-akibat:** baris "GAP nyata" ini penting dipahami sebelum lanjut testing — kalau kamu jual/lepas aset lewat endpoint ini lalu berharap Neraca (file 04) otomatis mencerminkan rugi 48 juta itu, kamu akan salah simpul "laporan ini bug" padahal memang belum ada mekanisme otomatisnya. Selama jurnal koreksi manual belum diposting, aset yang sudah "dijual" di `fixed-assets` itu masih nyangkut nilainya di akun AST-05/AST-06 GL — dua sumber data (modul Fixed Assets vs GL/Neraca) akan terlihat tidak sinkron sampai jurnal manual itu benar-benar dibuat.

## 4. Anggaran (Budget vs Actual) per Proyek

Budget bulan Januari 2026 untuk PRJ-GDA (`accounting/budgets/create`, `fiscal_year_id` FY2026):

| `account_id`                     | `business_unit_id` | `period_month` | `budgeted_amount` |
| -------------------------------- | ------------------ | -------------- | ----------------: |
| PDT-01 Pendapatan Progres Proyek | PRJ-GDA            | 2026-01-01     |       280.000.000 |
| BBN-01 Beban Pokok Proyek        | PRJ-GDA            | 2026-01-01     |        50.000.000 |
| BBN-02 Beban Subkontraktor       | PRJ-GDA            | 2026-01-01     |        90.000.000 |

Actual Januari 2026 (dari file 01/02): Pendapatan 300.000.000, Beban Pokok 40.000.000, Beban Subkon 100.000.000.

| Skenario | Detail                                                                                                                                                                       | Hasil                                                                                                                                                                                                                                                                                                 |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `accounting/budgets/create` dengan 3 baris di atas.                                                                                                                          | 201, `status: draft`.                                                                                                                                                                                                                                                                                 |
| Positif  | `accounting/budgets/vs-actual` dengan `slug` budget di atas (setelah T1-T7 posted).                                                                                          | Pendapatan: budgeted 280jt, actual 300jt, variance **+20.000.000** (over-achieve, favorable). Beban Pokok: budgeted 50jt, actual 40jt, variance **−10.000.000** (under-budget, favorable buat beban). Beban Subkon: budgeted 90jt, actual 100jt, variance **+10.000.000** (over-budget, unfavorable). |
| Negatif  | `accounting/budgets/create` dengan `lines.*.budgeted_amount` bernilai negatif (mis. −5.000.000).                                                                             | 422, `budgeted_amount` gagal validasi `min:0` — pesan Laravel default (bukan pesan custom "422 Invalid amount" seperti draf sebelumnya), field yang gagal: `lines.0.budgeted_amount`.                                                                                                                 |
| Negatif  | `accounting/budgets/update` untuk slug yang tidak ada di branch aktif.                                                                                                       | Error "content.not_found_in_branch".                                                                                                                                                                                                                                                                  |
| Negatif  | `accounting/budgets/vs-actual` untuk budget dengan `lines.*.account_id` yang sudah dihapus dari COA (skenario edge-case, biasanya tidak terjadi karena COA hard-referenced). | Perlu diverifikasi manual — `vsActual()` eager-load `lines.account.type`, kalau akun ternyata sudah tidak ada akan null-pointer di `$line->account->type` — laporkan sebagai temuan kalau reproduksi berhasil.                                                                                        |

## Netralisasi

- `fixed-assets/disposals/delete` untuk row disposal test, lalu set kembali `status: active` pada Excavator secara manual (tidak ada endpoint "undo disposal" otomatis — cek apakah delete disposal juga mengembalikan status aset; kalau tidak, update manual via `fixed-assets/assets/update`).
- Hapus `AssetDepreciation` test run tidak bisa lewat API (tidak ada endpoint delete untuk depreciation record) — kalau perlu reset total, hapus langsung asetnya (`fixed-assets/assets/delete`, hanya berhasil kalau tidak ada riwayat depresiasi ATAU status `active` — lihat guard §2) dan buat ulang.
- Hapus Budget test (`accounting/budgets/delete`).
