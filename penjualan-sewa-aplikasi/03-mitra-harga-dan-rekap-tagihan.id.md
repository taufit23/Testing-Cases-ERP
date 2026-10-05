# 03. Mitra, Harga Dasar, dan Rekap Tagihan Bulanan

Rumus tagihan per klien = harga paket + tiap add-on + (user aktif di atas batas paket x harga user) + (cabang di atas batas paket x harga outlet). User aktif = bukan owner platform, aktif, login minimal sekali di bulan itu. Klien tertangguhkan ditagih 0.

## Positif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 3.1 | `core/billing-prices`: buka | Harga seeder terlihat sesuai tabel prasyarat |
| 3.2 | `core/partners`: buat Mitra Reseller Uji | Tersimpan; muncul di pemilih Mitra provider |
| 3.3 | Kaitkan Klien A dan B ke Mitra; ubah Klien A menjadi klien langsung lalu kembalikan | Mitra bisa dikosongkan dan diisi lagi |
| 3.4 | Login bergantian sebagai user Klien A di bulan berjalan sampai 4 user aktif (batas 3) | Rekap: 1 user tambahan = 40.000 |
| 3.5 | Tambah 1 cabang di Klien B (batas dinaikkan owner dulu) | Rekap: 1 outlet tambahan = 200.000 |
| 3.6 | Setelah bulan berakhir (atau `billing:snapshot --period=YYYY-MM`), tekan Buat rekap di `core/partner-statements` | Baris per klien dengan paket, add-on, user/outlet tambahan, total |
| 3.7 | `core/partner-overview` | Per Mitra: user aktif vs batas, cabang vs batas, tanda mendekati (80%) dan melewati batas |
| 3.8 | Finalisasi rekap yang harganya lengkap | Status final |
| 3.9 | Ubah harga paket, buat ulang rekap | Baris final tidak berubah; baris draft dihitung ulang |
| 3.10 | Buka kembali rekap final, buat ulang | Dihitung ulang dengan harga terbaru |
| 3.11 | Ekspor PDF dan Excel | Berkas terunduh, angka sama dengan layar, teks mengikuti bahasa pengguna |

## Negatif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 3.12 | Kosongkan harga add-on yang dipakai, coba finalisasi | Diblokir dengan peringatan harga belum diatur |
| 3.13 | Klien tanpa paket, coba finalisasi | Diblokir dengan peringatan tanpa paket |
| 3.14 | Hapus Mitra yang masih punya klien atau riwayat tagihan | Ditolak |
| 3.15 | Akun admin klien membuka `core/billing-prices` | Ditolak (owner only) |
| 3.16 | Login sebagai owner platform di bulan itu | Tidak dihitung sebagai user aktif |
| 3.17 | Klien tertangguhkan di bulan itu | Total 0 |

## Netralisasi

Buka kembali dan hapus rekap draft uji; lepas klien dari Mitra sebelum menghapus Mitra uji.
