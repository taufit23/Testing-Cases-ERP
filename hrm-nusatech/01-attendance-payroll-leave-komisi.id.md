---
title: Test Case HRM (NUSATECH) — 01. Attendance, Payroll, Leave, & Komisi Sales Toko
category: HRM Nusatech
description: 30 karyawan konsultan IT + staff toko, semua dalam 1 branch PT NUSATECH — attendance, payroll bulanan, cuti, dan komisi penjualan retail, dibedakan via department/position (bukan business_unit_id).
visibility: internal
---

# 01. Attendance, Payroll, Leave, & Komisi Sales Toko

> Skenario: **PT NUSATECH**, 1 branch tunggal. 30 karyawan (konsultan IT, project manager, admin) + staff toko (kasir/sales, teknisi servis) — SEMUANYA di branch yang sama.
>
> ⚠️ **`employees` TIDAK punya kolom `business_unit_id`** (dicek di migration `create_employees_table` — hanya ada `position_id` dan `department_id`, keduanya nullable FK ke `positions`/`departments`). Jadi pembeda "karyawan konsultan" vs "staff toko" di file ini BUKAN via Business Unit, melainkan via **Department** (`departments.name`) dan **Position** (`positions.name`) seperti biasa — field yang memang ada di skema. Jangan mengarang payload `business_unit_id` di `employees/create`.
>
> Format pengujian: **Positif** / **Negatif** / **Netralisasi**. Endpoint utama: `hrm/departments`, `hrm/positions`, `hrm/employees`, `hrm/attendances` (perlu dicek nama controller aktual — file ini pakai path generik `hrm/*` sesuai `routes/hrm.php`), `hrm/leave-types`, `hrm/leaves`, `hrm/leave-balances`, `hrm/payroll-periods`, `hrm/payroll-items`, `hrm/payslips`, `hrm/salary-components`, `hrm/commission-rules`, `hrm/commissions`, `hrm/bpjs-settings`.

## 1. Departments & Positions (Divisi Konsultasi/Managed Services)

| Skenario    | Detail                                                                                                     | Hasil                                                              |
| ----------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Positif     | `departments/create` — "Divisi Konsultasi & Proyek IT", "Divisi Managed Services", "Admin & Finance"       | 3 department terdaftar (branch PT NUSATECH)                        |
| Positif     | `positions/create` — "IT Consultant", "Project Manager", "Network Engineer", "Finance Staff", "HR & Admin" | 5 posisi terdaftar, masing-masing terhubung department yang sesuai |
| Netralisasi | Hapus department/position test kalau belum ada employee yang mereferensikannya                             |

## 2. Departments & Positions (Divisi Toko Elektronik)

| Skenario | Detail                                                                                                                                                                                                             | Hasil                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Positif  | `departments/create` — "Sales & Kasir Toko", "Servis & Teknisi" (branch yang sama — department tetap branch-scoped, tapi karena cuma 1 branch, cukup dibedakan lewat nama department, bukan lewat branch terpisah) | 2 department terdaftar, dalam branch yang sama dengan department §1, dibedakan murni via nama |
| Positif  | `positions/create` — "Sales Associate", "Teknisi Servis Laptop/PC"                                                                                                                                                 | 2 posisi terdaftar                                                                            |

## 3. Employees

| Skenario                                | Detail                                                                                                                                                                                                                               | Hasil                                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Positif — 30 karyawan konsultan/Managed | `employees/create` (atau `create-bulk` kalau tersedia) — isi minimal representative sample (mis. 5-10 record nyata untuk test, sisanya boleh data dummy) dengan `department_id`/`position_id` sesuai §1, `base_salary` sesuai posisi | Karyawan terdaftar, `employee_number` auto-generate                                                               |
| Positif — staff Toko Elektronik         | `employees/create` untuk 3-5 staff (Sales Associate, Teknisi) dengan `department_id`/`position_id` §2                                                                                                                                | Karyawan terdaftar, branch sama dengan §1 — pembeda cuma `department_id`, BUKAN branch/BU terpisah lagi           |
| Negatif                                 | `create` employee dengan `department_id`/`position_id` yang tidak ada / bukan milik branch PT NUSATECH                                                                                                                               | 422 — validasi FK tetap berlaku walau branch tunggal                                                              |
| Positif                                 | `employees/options` (permission-free dropdown)                                                                                                                                                                                       | Muncul list ringkas untuk dipakai modul lain (payroll, komisi) — [[feedback_dropdown_options_permission_pattern]] |
| Netralisasi                             | `delete` employee test kalau belum ada payroll/attendance/leave terkait                                                                                                                                                              |

## 4. Attendance

| Skenario    | Detail                                                                                                                                               | Hasil                                                                          |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Positif     | `attendances/create` (atau clock-in/out kalau ada endpoint terpisah) — beberapa hari kerja Agustus 2026 untuk sample karyawan konsultan & staff toko | Record attendance tersimpan per employee per tanggal                           |
| Negatif     | Duplikat attendance untuk employee+tanggal yang sama                                                                                                 | Ditolak/di-overwrite — verifikasi behavior aktual, catat kalau tidak ada guard |
| Netralisasi | Hapus attendance test yang tidak dipakai perhitungan payroll final                                                                                   |

## 5. Leave (Cuti)

| Skenario    | Detail                                                                                                | Hasil                                                                                                                |
| ----------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Positif     | `leave-types/create` — "Cuti Tahunan", "Cuti Sakit", "Cuti Melahirkan" (kalau belum ada default)      | Tersimpan                                                                                                            |
| Positif     | `leave-balances` untuk 1 karyawan konsultan — pastikan saldo cuti tahunan awal (mis. 12 hari) ter-set | Saldo tersedia sebelum pengajuan cuti                                                                                |
| Positif     | `leaves/create` — pengajuan Cuti Tahunan 3 hari untuk 1 konsultan IT (bentrok jadwal proyek klien?)   | 201, status `pending`/`submitted`                                                                                    |
| Negatif     | `create` Leave dengan durasi melebihi saldo `leave-balances` tersisa                                  | Ditolak, atau lolos tanpa validasi saldo — verifikasi behavior aktual, catat sebagai gap kalau tidak ada guard saldo |
| Positif     | `approve` Leave                                                                                       | Status `approved`, `leave-balances` berkurang sesuai durasi                                                          |
| Netralisasi | `cancel`/`delete` Leave test, kembalikan saldo cuti kalau sempat berkurang                            |

## 6. Payroll — Divisi Konsultasi/Managed Services (gaji tetap)

| Skenario    | Detail                                                                                                   | Hasil                                                                                                                                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Positif     | `salary-components/create` — "Gaji Pokok", "Tunjangan Transport", "Tunjangan Komunikasi (IT Consultant)" | Komponen gaji tersedia untuk di-attach ke employee/payroll                                                                                                                                                   |
| Positif     | `bpjs-settings` — set persentase BPJS Kesehatan & Ketenagakerjaan sesuai regulasi (`tax-reference`)      | Konfigurasi tersimpan, dipakai perhitungan potongan payroll                                                                                                                                                  |
| Positif     | `payroll-periods/create` untuk Agustus 2026 → `process`                                                  | 201 → payroll periode diproses (1 periode untuk SEMUA karyawan branch PT NUSATECH, konsultan maupun staff toko), `payroll-items` (browse) muncul per karyawan (gaji pokok + tunjangan − potongan BPJS/PPh21) |
| Positif     | `payroll-items/update` — koreksi manual 1 item (mis. lembur proyek urgent klien)                         | Nilai payroll item ter-update sebelum approve final                                                                                                                                                          |
| Positif     | `payroll-periods/approve` → `mark-paid`                                                                  | Status `paid`, siap generate payslip                                                                                                                                                                         |
| Positif     | `payslips/generate` → `approve` → `download-pdf`                                                         | Payslip per karyawan tersedia, PDF ter-generate                                                                                                                                                              |
| Negatif     | `mark-paid` payroll period yang belum `approve`                                                          | Ditolak — urutan status wajib dilewati                                                                                                                                                                       |
| Netralisasi | Payroll yang sudah `paid` adalah state akhir wajar — koreksi lewat periode berikutnya, bukan reverse     |

## 7. Payroll — Staff Toko (gaji + potensi komisi)

> **Revisi arsitektur**: sebelumnya payroll staff toko diproses di `payroll-periods` TERPISAH (branch beda). Sekarang staff toko masuk **1 periode payroll yang sama** dengan konsultan (§6) — karena cuma 1 branch, `payroll-periods` untuk Agustus 2026 sudah otomatis mencakup SEMUA karyawan (konsultan + staff toko) sekaligus. Tidak ada lagi "proses payroll kedua kalinya".

| Skenario | Detail                                                                                                                                                  | Hasil                                                                               |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Positif  | Cek `payroll-items` hasil §6 — pastikan baris staff toko (Sales Associate, Teknisi) muncul dalam periode Agustus 2026 yang SAMA, bukan periode terpisah | `payroll-items` browse menampilkan gabungan seluruh employee, apapun department-nya |
| Positif  | `payslips/generate` untuk staff toko                                                                                                                    | Payslip tersedia, termasuk baris Komisi kalau ada (lihat §8)                        |

## 8. Komisi Sales Toko (**Commission Rules**, **Commissions**)

> Relevan karena Divisi Toko Elektronik punya profil sales retail — cek fitur `commission_rules` di HRM (referensi [[project_pos_terminal_shortcuts_and_quick_access]] soal komisi sales toko di modul lain, tapi di sini fokus HRM-nya).

| Skenario    | Detail                                                                                                                                 | Hasil                                                                                                                                                                                                                                                                         |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Positif     | `commission-rules/create` — "Komisi Sales Associate 2% dari nilai penjualan unit elektronik"                                           | Rule tersimpan, terhubung ke posisi "Sales Associate"                                                                                                                                                                                                                         |
| Positif     | `commissions/create` — hitung komisi 1 Sales Associate dari penjualan SO retail file `sales-nusatech/02` (57.165.000 × 2% = 1.143.300) | 201, status `pending`                                                                                                                                                                                                                                                         |
| Negatif     | `create` Commission untuk employee yang bukan posisi "Sales Associate" (mis. Teknisi Servis)                                           | Ditolak/tidak relevan — verifikasi behavior aktual, catat kalau tidak ada validasi posisi                                                                                                                                                                                     |
| Positif     | `commissions/mark-paid`                                                                                                                | Status `paid`, idealnya muncul di payslip periode terkait — verifikasi apakah `payslips/generate` otomatis menarik data `commissions` atau HARUS ditambahkan manual sebagai `salary-components` tambahan (dokumentasikan behavior aktual, jangan asumsikan otomatis nyambung) |
| Netralisasi | Batalkan Commission test sebelum `mark-paid` kalau salah input                                                                         |

## Ringkasan

- [ ] 30 karyawan konsultan/Managed Services (representative sample) + department/position 3+5
- [ ] Staff Toko Elektronik (representative sample) + department/position 2+2, branch SAMA dengan konsultan
- [ ] Attendance & Leave berjalan untuk semua employee (1 branch)
- [ ] Payroll Agustus 2026 selesai `paid` dalam **1 periode gabungan** (bukan lagi 2 periode terpisah per branch)
- [ ] Komisi Sales Associate terhitung dari 1 transaksi SO retail

## Referensi Silang

- [`../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md`](../accounting-nusatech/00-profil-perusahaan-dan-master-data.id.md)
- [`../sales-nusatech/02-so-integrasi-accounting.id.md`](../sales-nusatech/02-so-integrasi-accounting.id.md) — sumber nilai penjualan untuk komisi
- [[feedback_dropdown_options_permission_pattern]]
