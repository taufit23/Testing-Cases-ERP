# 01. Platform Owner dan Akses Platform

Halaman yang dikunci `users.is_platform_owner`: `dashboard/core`, semua `core/landing-*`, `core/partners`, `core/billing-prices`, `core/partner-statements`, `core/modules`, `core/module-packages`, `core/branch-menu-templates`, `hrm/payroll-tax-reference`. Penyebab bug lama: flag belum diisi di database; kini bisa dikelola dari `core/users`.

## Positif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 1.1 | Logout lalu login sebagai lgrtaufit@gmail.com, buka `dashboard/core` | Dashboard tampil, tidak ada layar "restricted to the platform owner" |
| 1.2 | Buka `core/landing-banners` | Halaman tampil, tombol tambah aktif |
| 1.3 | Di `core/users`, menu baris user lain: pilih "Make platform owner", isi PIN owner, konfirmasi | Toast sukses, badge Platform Owner muncul di kolom roles |
| 1.4 | User tadi logout, login ulang, buka `core/landing-banners` | Halaman tampil (owner kedua terdeteksi) |
| 1.5 | Owner kedua tanpa PIN: setelah login muncul modal buat PIN, tidak bisa ditutup | PIN tersimpan, modal hilang |
| 1.6 | Owner pertama pilih "Remove platform owner access" pada owner kedua, isi PIN | Toast sukses, badge hilang; login ulang owner kedua kena layar restricted |
| 1.7 | Cek activity log | Ada catatan update user untuk grant dan revoke |

## Negatif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 1.8 | Akun admin biasa (bukan owner) buka `dashboard/core` dan `core/partners` | Layar/403 restricted to the platform owner |
| 1.9 | Akun admin biasa: menu "Make platform owner" pada baris user | Disabled (tidak hilang) |
| 1.10 | Panggil `PUT core/users/set-platform-owner` langsung sebagai non-owner | 403 |
| 1.11 | Grant owner dengan PIN kosong atau salah | 422, flag tidak berubah |
| 1.12 | Owner mencabut akses dirinya sendiri | 422, ditolak |
| 1.13 | Cabut owner terakhir yang tersisa (via API, dari akun owner lain yang lalu dicabut juga) | Ditolak: minimal satu owner harus tersisa |
| 1.14 | Role admin klien baru dibuat dan `permission:sync` dijalankan | Admin klien tetap tidak bisa membuka halaman owner |

## Netralisasi

Cabut owner kedua (kasus 1.6), pastikan lgrtaufit@gmail.com tetap owner.
