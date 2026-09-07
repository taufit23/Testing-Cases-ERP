---
title: — Rencana Otomasi Playwright (suite accounting)
category: Accounting 1
description: Peta pengerjaan spec Playwright untuk suite PT Retail Nusantara Jaya — tiap file dokumentasi di folder ini dipetakan ke 1+ spec file di FEAccounting/tests/e2e/scenarios/accounting/.
visibility: internal
---

# Rencana Otomasi Playwright — suite `accounting/`

Suite ini yang PERTAMA dikerjakan (per README.md: "fondasi, kerjakan pertama", dan §1-§8 file `00` sudah pernah ditest manual penuh oleh user). Spec Playwright-nya ada di repo `FEAccounting`, folder `tests/e2e/scenarios/accounting/` — **bukan** di sini (folder ini cuma dokumentasi test case-nya).

**Cara jalanin**: `pnpm test tests/e2e/scenarios/accounting/<file>.spec.ts` (atau `pnpm test:ui` lalu pilih manual) dari `FEAccounting`.

**Aturan main**: tiap suite SELALU mulai dengan `00-provider.spec.ts` — bikin provider (tenant) + branch + user + role baru via `core/providers/onboard-client`, supaya semua transaksi di spec berikutnya jalan di branch yang terisolasi (bukan numpang di branch akun testing yang dipakai suite lain). Spec 01 dst login pakai akun scenario sendiri (`fixtures.ts`), bukan akun `TEST_EMAIL` bersama.

## Peta pengerjaan

| # | Dokumen sumber | Spec file (rencana) | Status |
| --- | --- | --- | --- |
| 0 | — (tidak ada dokumen `.md` khusus, provider dibuat implisit di awal `00-profil-perusahaan...`) | `00-provider.spec.ts` | ✅ Dibuat (2026-09-06), **belum pernah dijalankan** — selector masih asumsi pertama, kemungkinan perlu 1-2 ronde perbaikan begitu run pertama gagal (pola yang sama seperti `auth.setup.ts` dulu) |
| 1 | `00-profil-perusahaan-dan-master-data.id.md` §1-§8 (Currency, COA Type, COA, Fiscal Year, Accounting Period, Business Unit, Tax, Contact) | `01-master-data.spec.ts` | ⬜ Belum dibuat |
| 2 | `00-profil-perusahaan-dan-master-data.id.md` §9 (Saldo Awal / Opening Balance) | `02-opening-balance.spec.ts` | ⬜ Belum dibuat |
| 3 | `01-jurnal-manual.id.md` | `03-jurnal-manual.spec.ts` | ⬜ Belum dibuat |
| 4 | `02-general-ledger-neraca-saldo.id.md` | `04-general-ledger.spec.ts` | ⬜ Belum dibuat |
| 5 | `03-tutup-periode-dan-tahun-fiskal.id.md` | `05-tutup-periode.spec.ts` | ⬜ Belum dibuat |
| 6 | `04-laporan-keuangan.id.md` | `06-laporan-keuangan.spec.ts` | ⬜ Belum dibuat |
| 7 | `05-anggaran-budget.id.md` | `07-anggaran.spec.ts` | ⬜ Belum dibuat |
| 8 | `06-aset-tetap-dan-penyusutan.id.md` | `08-aset-tetap.spec.ts` | ⬜ Belum dibuat |
| 9 | `07-rekonsiliasi-bank.id.md` | `09-rekonsiliasi-bank.spec.ts` | ⬜ Belum dibuat |
| 10 | `08-laporan-pajak-ppn.id.md` | `10-laporan-ppn.spec.ts` | ⬜ Belum dibuat |
| 11 | `09-skenario-lanjutan-dan-edge-case-lapangan.id.md` | `11-edge-cases.spec.ts` | ⬜ Belum dibuat — dikerjakan PALING TERAKHIR (butuh baseline semua spec lain, sama seperti versi manualnya) |

## Catatan pelaksanaan

- **`--ollama-only`/DB dev/dst dari sesi translation tidak relevan di sini** — spec ini murni Playwright biasa, jalan lewat `pnpm test`.
- Target BASE_URL bebas (`localhost:3000` atau `https://ranahku.web.id` via `BASE_URL=...`), TAPI kalau target `ranahku.web.id`, provider/data yang dibuat `00-provider.spec.ts` akan **benar-benar masuk ke database yang sedang dipakai FE itu** (production atau dev, tergantung Origin — lihat `SwitchDatabaseByOrigin`). Disarankan selalu jalan dari `localhost:3000` (otomatis kena `erp_development` per setup 2026-09-06) supaya aman diulang-ulang.
- Setiap spec file BARU wajib prefix nomor 2-digit (`01-`, `02-`, ...) mengikuti urutan dokumen sumber, bukan urutan file `.md` originalnya — supaya `provider` selalu jelas nomor 00 dan urutan eksekusi logis dari `pnpm test tests/e2e/scenarios/accounting/` (Playwright jalanin file sesuai urutan nama, alfabetis).
- Kalau 1 dokumen sumber isinya sangat panjang/banyak sub-skenario (mis. `01-jurnal-manual.id.md` yang punya 11 variasi transaksi), spec-nya BOLEH dipecah jadi beberapa `test()` block dalam 1 file (bukan 1 file per variasi) — jaga jumlah file tetap 1:1 dengan dokumen sumber kalau memungkinkan.
- Update kolom Status di tabel atas SETIAP kali sebuah spec baru dibuat/direvisi/berhasil dijalankan penuh oleh user — supaya progres kelihatan across sesi (masalah utama yang bikin suite ini "gak pernah selesai" adalah TIDAK ada tracking progres per-sesi sebelumnya).
