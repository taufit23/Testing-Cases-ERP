---
title: (Construction / Project Based) — 01. Jurnal Progres & Retensi
category: accounting-construction
description: Skenario pengujian jurnal manual arus konstruksi PT Bangun Persada — uang muka, pengakuan pendapatan progresif (percentage of completion), retensi piutang/utang, dan tagihan subkontraktor. Dimensi Business Unit per proyek.
visibility: internal
---

# 01. Jurnal Progres & Retensi

> **Ciri Khas Skenario**: Retensi (piutang/utang ditahan 5%), amortisasi uang muka per termin, pengakuan pendapatan berbasis progres fisik (Percentage of Completion). Nilai kontrak Proyek Gedung Kantor A (PRJ-GDA) = Rp1.000.000.000 (di luar PPN).
>
> **Alur wajib**: setiap jurnal harus **`create` dulu, baru `post` terpisah** (`PUT accounting/journals/post`) — `create` HANYA membuat header+baris berstatus `JRN_PENDING_REVIEW` (kalau baris balance) dan **belum menyentuh GL sama sekali**; GL baru terbentuk saat `post`. Jurnal tidak balance (total debit ≠ total kredit) tetap di status draft dan tidak masuk approval/posting. Lihat `App\Http\Controllers\Accounting\Journal::create()`/`post()`.
> Setiap baris jurnal wajib `account_id` (harus ada di `chart_of_accounts`) dan minimal 2 baris (`lines: min:2`). Dimensi proyek diisi per baris via `business_unit_id` (nullable, tapi WAJIB diisi konsisten di semua baris transaksi ini supaya laporan per proyek di file 02/04 akurat).

**Sebab-akibat kalau `business_unit_id` lupa/tidak konsisten:** jurnalnya tetap sukses & balanced (tidak ada error apapun), tapi transaksi itu "hilang" dari breakdown per proyek di file 02 §2 dan file 04 — bukan berarti datanya salah, cuma tidak akan ketahuan itu punya proyek yang mana. Istilah uang muka, amortisasi uang muka, retensi, dan pengakuan pendapatan progresif yang dipakai di T1-T7 di bawah sudah dijelaskan di [`00-profil-perusahaan-dan-master-data.id.md`](./00-profil-perusahaan-dan-master-data.id.md) §"Istilah Khusus Proyek Konstruksi" — baca dulu kalau ada istilah yang belum familiar.

## 1. Jurnal T1 — Terima Uang Muka Proyek A 20% (PRJ-GDA)

| Akun                              |           Debit |          Kredit |
| --------------------------------- | --------------: | --------------: |
| AST-01 Bank Mandiri Proyek        |     222.000.000 |               — |
| LIA-02 Uang Muka Proyek Diterima  |               — |     200.000.000 |
| LIA-04 PPN Keluaran (11% × 200jt) |               — |      22.000.000 |
| **Total**                         | **222.000.000** | **222.000.000** |

Dimensi: `business_unit_id` = PRJ-GDA di semua baris.

**Sebab-akibat:** perhatikan tidak ada baris "Pendapatan" sama sekali di jurnal ini — uang 222 juta yang masuk BUKAN pendapatan, murni utang (LIA-02) ke pemilik proyek. Kalau ada yang keliru mencatat uang muka LANGSUNG sebagai Pendapatan Progres (PDT-01), Laba Rugi bulan ini akan kelihatan untung besar padahal belum ada pekerjaan yang benar-benar selesai — kesalahan klasik yang bikin laporan menyesatkan pemilik usaha.

## 2. Jurnal T2 — Pengakuan Progres 30% & Retensi 5% (PRJ-GDA)

Nilai progres tertagih = 30% × 1.000.000.000 = 300.000.000. Retensi ditahan pemilik proyek 5% × 300jt = 15.000.000. Amortisasi uang muka = 20% (proporsi DP terhadap kontrak) × 300jt = 60.000.000. Piutang progres bersih = 300jt − 15jt − 60jt = 225.000.000.

| Akun                             |           Debit |          Kredit |
| -------------------------------- | --------------: | --------------: |
| AST-02 Piutang Progres Proyek    |     225.000.000 |               — |
| AST-03 Piutang Retensi           |      15.000.000 |               — |
| LIA-02 Uang Muka Proyek Diterima |      60.000.000 |               — |
| PDT-01 Pendapatan Progres Proyek |               — |     300.000.000 |
| **Total**                        | **300.000.000** | **300.000.000** |

Dimensi: `business_unit_id` = PRJ-GDA. (PPN atas termin ini sudah tercakup di uang muka T1 — skenario ini tidak menagih PPN kedua kali di baris progres.)

**Sebab-akibat:** ini jurnal paling padat konsep di suite ini — 4 baris sekaligus menunjukkan KENAPA Piutang Progres (225jt) lebih kecil dari nilai progres kotor (300jt): 15jt "dipotong" retensi (belum boleh ditagih sampai masa pemeliharaan selesai) dan 60jt "dipotong" karena sudah dibayar duluan lewat uang muka T1 (kalau tetap ditagih penuh, pemilik proyek akan dianggap bayar dobel). Kalau salah satu dari 2 pemotongan ini lupa dimasukkan ke jurnal, Piutang Progres yang tercatat akan lebih besar dari yang SEHARUSNYA bisa ditagih ke pemilik proyek — potensi menagih customer melebihi hak kontraktual.

## 3. Jurnal T3 — Tagihan Subkontraktor CV Baja Perkasa dengan Retensi Utang 5% (PRJ-GDA)

| Akun                               |           Debit |          Kredit |
| ---------------------------------- | --------------: | --------------: |
| BBN-02 Beban Subkontraktor         |     100.000.000 |               — |
| LIA-01 Utang Subkontraktor         |               — |      95.000.000 |
| LIA-03 Utang Retensi Subkontraktor |               — |       5.000.000 |
| **Total**                          | **100.000.000** | **100.000.000** |

Dimensi: `business_unit_id` = PRJ-GDA.

**Sebab-akibat:** perhatikan arahnya KEBALIKAN dari T2 — di T2 kontraktor yang DITAHAN retensinya oleh pemilik proyek (piutang, uang milik kontraktor yang belum bisa diambil). Di T3 ini kontraktor sendiri yang MENAHAN retensi subkontraktornya (utang, uang milik subkontraktor yang belum dibayar kontraktor). Perusahaan yang sama bisa berperan sebagai "yang ditahan" dan "yang menahan" sekaligus tergantung dengan siapa dia bertransaksi — kalau arah ini terbalik saat dicatat, Utang Subkontraktor akan under/overstated.

## 4. Jurnal T4 — Pelunasan Sebagian Utang Subkontraktor (PRJ-GDA)

| Akun                       |          Debit |         Kredit |
| -------------------------- | -------------: | -------------: |
| LIA-01 Utang Subkontraktor |     95.000.000 |              — |
| AST-01 Bank Mandiri Proyek |              — |     95.000.000 |
| **Total**                  | **95.000.000** | **95.000.000** |

## 5. Jurnal T5 — Pencairan Retensi Subkontraktor setelah Masa Pemeliharaan (PRJ-GDA)

| Akun                               |         Debit |        Kredit |
| ---------------------------------- | ------------: | ------------: |
| LIA-03 Utang Retensi Subkontraktor |     5.000.000 |             — |
| AST-01 Bank Mandiri Proyek         |             — |     5.000.000 |
| **Total**                          | **5.000.000** | **5.000.000** |

**Sebab-akibat (T4 & T5):** T4 melunasi Utang Subkontraktor tapi SENGAJA cuma 95jt (bukan 100jt) — sisa 5jt itu adalah retensi yang ditahan (dicatat di T3), belum boleh dibayar sampai masa pemeliharaan selesai. T5 baru mencairkannya belakangan sebagai transaksi terpisah. Kalau retensi ini malah ikut dibayar penuh di T4, kontraktor kehilangan "jaminan" kualitas pekerjaan subkontraktor lebih awal dari seharusnya.

## 6. Jurnal T6 — Progres 25% & Uang Muka Proyek Jembatan B (PRJ-JMB, tanpa retensi — proyek publik, jaminan pemeliharaan diatur di luar sistem)

Uang muka 15% × 800.000.000 = 120.000.000 + PPN 11% = 13.200.000, kas masuk 133.200.000.

| Akun                             |           Debit |          Kredit |
| -------------------------------- | --------------: | --------------: |
| AST-01 Bank Mandiri Proyek       |     133.200.000 |               — |
| LIA-02 Uang Muka Proyek Diterima |               — |     120.000.000 |
| LIA-04 PPN Keluaran              |               — |      13.200.000 |
| **Total**                        | **133.200.000** | **133.200.000** |

Dimensi: `business_unit_id` = PRJ-JMB.

## 7. Jurnal T7 — Pemakaian Bahan Material Konstruksi untuk Proyek A (PRJ-GDA)

| Akun                                        |          Debit |         Kredit |
| ------------------------------------------- | -------------: | -------------: |
| BBN-01 Beban Pokok Proyek (Bahan & Upah)    |     40.000.000 |              — |
| AST-04 Persediaan Bahan Material Konstruksi |              — |     40.000.000 |
| **Total**                                   | **40.000.000** | **40.000.000** |

Dimensi: `business_unit_id` = PRJ-GDA.

## 2. Skenario Pengujian

| Skenario | Detail                                                                                               | Hasil                                                                                                                                                                                                                                                                                                                                                                 |
| -------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif  | `POST accounting/journals/create` T1 (3 baris, balanced, dimensi PRJ-GDA).                           | 201, header status `JRN_PENDING_REVIEW`, `posted_at: null` — belum ada baris di `general_ledgers`.                                                                                                                                                                                                                                                                    |
| Positif  | `PUT accounting/journals/post` atas T1.                                                              | 200, `posted_at` terisi, status berubah ke status "posted" branch (default `default_general_journal_post_status`), GL 3 baris terbentuk untuk PRJ-GDA.                                                                                                                                                                                                                |
| Positif  | Create + post T2 s.d. T7 dengan urutan sama (create dulu, baru post).                                | Tiap jurnal 201 lalu 200, total debit = total kredit di tiap jurnal, GL bertambah sesuai baris.                                                                                                                                                                                                                                                                       |
| Positif  | `GET/POST accounting/journals/show` slug T2, cek `pending_approval_request`.                         | `null` kalau `requires_journal_approval` OFF di `purchasing/purchase-config` branch — approval gate manual journal reuse flag yang sama dengan Purchasing (lihat `Journal::requiresJournalApproval()`).                                                                                                                                                               |
| Negatif  | `create` dengan `lines` hanya 1 baris.                                                               | 422, `lines` minimal 2 baris.                                                                                                                                                                                                                                                                                                                                         |
| Negatif  | `create` dengan total debit ≠ total kredit (mis. T2 tapi Piutang Progres ditulis 230jt bukan 225jt). | 201 tetap terbuat TAPI berstatus draft (bukan `JRN_PENDING_REVIEW`) — jurnal tidak balance tidak eligible approval/posting sampai dikoreksi. `post` atas jurnal ini harus dicoba dan **tetap bisa di-post** karena `post()` sendiri tidak re-cek balance (hanya cek `posted_at` & approval) — dokumentasikan sebagai potensi gap kalau ditemukan saat testing manual. |
| Negatif  | `PUT post` dua kali atas jurnal yang sama.                                                           | Error "content.journal_already_posted".                                                                                                                                                                                                                                                                                                                               |
| Negatif  | `PUT update` (edit baris) pada jurnal yang sudah `posted_at` terisi.                                 | Error "content.journal_already_posted" — jurnal posted immutable, koreksi harus lewat `reverse`.                                                                                                                                                                                                                                                                      |
| Negatif  | `account_id` di salah satu baris tidak ada di `chart_of_accounts`.                                   | 422, `lines.*.account_id` invalid.                                                                                                                                                                                                                                                                                                                                    |
| Positif  | `POST accounting/journals/reverse` atas T4 (sudah posted) dengan tanggal baru.                       | 201, jurnal baru `REV-{code}` terbuat, baris debit/kredit dibalik dari T4, `posted_at` langsung terisi (reversal langsung posted), T4 asli `is_reversed: true`. GL T4 asli TIDAK dihapus — total efek T4+reversal = 0 di setiap akun (additive, bukan delete-lalu-flip).                                                                                              |
| Negatif  | `reverse` atas jurnal yang belum `posted_at` (masih draft/pending review).                           | Error "content.journal_not_posted".                                                                                                                                                                                                                                                                                                                                   |
| Negatif  | `reverse` dua kali atas jurnal yang sama.                                                            | Error "content.journal_already_reversed".                                                                                                                                                                                                                                                                                                                             |

## Netralisasi

- Reverse semua jurnal T1-T7 (kecuali T4 yang sudah direverse di skenario test) via `accounting/journals/reverse` supaya saldo GL proyek kembali ke saldo awal — JANGAN hapus jurnal yang sudah `posted_at` (delete ditolak backend untuk jurnal posted, lihat `Journal::delete()`).
- Jurnal masih draft (unbalanced test case) boleh langsung `delete` karena belum posted.
