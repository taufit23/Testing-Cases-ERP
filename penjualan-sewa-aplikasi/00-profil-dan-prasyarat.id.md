# Penjualan dan Penyewaan Aplikasi: Profil dan Prasyarat

Suite ini menguji aplikasi ERP sebagai produk yang **disewakan** (langganan bulanan) oleh pemilik platform langsung atau lewat Mitra (reseller). Semua kasus dijalankan sebagai **platform owner** kecuali disebut lain.

## Skenario

| Peran | Nama | Keterangan |
| --- | --- | --- |
| Platform owner | lgrtaufit@gmail.com | Pemilik aplikasi, `is_platform_owner = true`, punya PIN owner |
| Platform owner kedua | Owner Uji 2 | Dibuat di kasus 01, dicabut di netralisasi |
| Mitra | Mitra Reseller Uji | Reseller yang membawa 2 klien |
| Klien A | PT Kopi Senja (via Mitra) | Paket Starter, 1 outlet, 3 user |
| Klien B | PT Retail Maju (via Mitra) | Paket Business + add-on Restoran |
| Klien C | CV Langsung Uji | Klien langsung, paket Enterprise |

## Prasyarat

1. `migrate:all`, `seed:all`, lalu `permission:sync` sudah dijalankan (route owner, paket, harga, dan `hrm.employees.view-confidential` baru ada setelah sync).
2. Harga dasar seeder ada: Starter 300.000, Business 1.300.000, Enterprise 3.000.000, user tambahan 40.000, outlet tambahan 200.000, add-on Restoran dan Rental 600.000, Manufaktur dan Pertambangan 1.200.000.
3. Login sebagai platform owner dan PIN owner sudah diset (jika belum, `OwnerPinSetupModal` muncul dan harus diisi dulu).

## Cakupan dan batas

- **Tercakup:** sewa bulanan (paket, add-on, user/outlet tambahan), Mitra, rekap tagihan, penangguhan, isolasi data antar klien, kelola owner.
- **Tidak tercakup, memang belum ada fiturnya:** pelacakan status bayar tagihan dan portal Mitra (di luar cakupan keputusan owner), serta **jual putus / lisensi self-hosted** (tidak ada fitur lisensi atau aktivasi terpisah; saat ini hanya model sewa multi-tenant).

## Urutan

| File | Isi |
| --- | --- |
| `01-owner-dan-akses-platform.id.md` | Platform owner, kelola owner, PIN, halaman yang dikunci owner |
| `02-paket-onboarding-dan-add-on.id.md` | Paket, Onboard Client, batas, add-on, provisioning modul |
| `03-mitra-harga-dan-rekap-tagihan.id.md` | Mitra, harga dasar, rekap bulanan, finalisasi, ekspor |
| `04-penangguhan-dan-isolasi-data-klien.id.md` | Suspend/resume, isolasi antar klien, kerahasiaan gaji |
