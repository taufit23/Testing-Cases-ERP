# 02. Paket, Onboard Client, dan Add-on

Paket: **Starter** (POS, 3 user, 1 outlet), **Business** (POS, Inventori, Pembelian, Penjualan, 10 user, 1 outlet), **Enterprise** (Business + Akuntansi, Keuangan, HRM, 25 user). Add-on: Restoran, Rental, Manufaktur, Pertambangan. "Outlet" = cabang (`max_branches`).

## Positif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 2.1 | `core/module-packages`: lihat daftar | 3 paket aktif; 6 paket preset lama nonaktif; kolom batas bawaan terlihat |
| 2.2 | `core/providers/onboard-client` untuk Klien A: pilih Mitra, paket Starter | Batas user 3 dan outlet 1 terisi otomatis |
| 2.3 | Isi provider, cabang, user admin, role baru, simpan | Satu transaksi sukses; kembali ke `core/providers`; Klien A terlihat |
| 2.4 | Login sebagai admin Klien A | Sidebar hanya berisi modul paket Starter (POS) dan modul inti |
| 2.5 | Onboard Klien B: Business + add-on Restoran | Modul Restoran ikut muncul di sidebar Klien B |
| 2.6 | Onboard Klien C tanpa Mitra, paket Enterprise | Mitra kosong (klien langsung); HRM dan Akuntansi aktif |
| 2.7 | Aktifkan add-on Manufaktur pada Klien C lewat `core/modules` | Konfigurasi Manufaktur dan pemetaan COA otomatis terbentuk (4 fungsi), akun 1416, 5542-5545 ada |
| 2.8 | Isi batas user secara eksplisit di form provider (mis. 5 pada paket Starter) | Angka eksplisit menang atas batas bawaan paket |
| 2.9 | Buat cabang baru milik klien yang berhak Manufaktur | Konfigurasi dan pemetaan COA ikut dibuat untuk cabang baru |

## Negatif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 2.10 | Onboard dengan email user yang sudah ada tanpa memilih "gunakan yang sudah ada" | Validasi menolak, tidak ada data setengah jadi (transaksi rollback) |
| 2.11 | Onboard sebagai admin biasa | Halaman/route ditolak (butuh izin onboard-client) |
| 2.12 | Klien A (Starter) membuka halaman modul Akuntansi lewat URL | Ditolak / tidak tersedia |
| 2.13 | Klien A membuat cabang kedua saat batas 1 outlet | Ditolak keras |
| 2.14 | Klien tanpa Manufaktur: cek COA | Tidak ada akun 1416, 5542-5545, 2112 |

## Netralisasi

Tangguhkan klien uji setelah selesai (klien dengan riwayat rekap tagihan tidak bisa dihapus).
