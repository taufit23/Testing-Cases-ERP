# 04. Penangguhan Klien dan Isolasi Data

## Penangguhan (klien menunggak atau kredensial bocor)

### Positif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 4.1 | `core/providers`: Suspend Klien A dengan alasan | Badge Suspended, alasan terlihat saat hover |
| 4.2 | User Klien A mencoba login | 403 `provider_suspended`, pesan jelas |
| 4.3 | User Klien A yang sedang login melakukan request apa pun | 403 yang sama, FE menampilkan toast sekali lalu logout |
| 4.4 | Platform owner tetap bisa login dan membuka data klien tertangguhkan | Tidak diblokir |
| 4.5 | Halaman publik berbasis token klien A (link penawaran, QR restoran, lamaran kerja) | Tertutup. Verifikasi QR dokumen tetap hidup |
| 4.6 | Restore access Klien A | User bisa login lagi, data utuh |

### Negatif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 4.7 | Suspend tanpa alasan | Ditolak (alasan wajib) |
| 4.8 | Admin non-owner memanggil `core/providers/suspend` | 403 |

## Isolasi antar klien

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 4.9 | Login admin Klien A; buka daftar kontak, produk, jurnal | Hanya data cabang Klien A |
| 4.10 | Panggil `show` dengan id/slug dokumen milik Klien B | "Not found in branch", bukan datanya |
| 4.11 | Admin Klien A mencari menu `core/*` milik platform | Tidak tersedia |
| 4.12 | Setelah `permission:sync` baru, admin Klien A tetap tidak bisa membuka halaman owner | Tetap ditolak |

## Kerahasiaan data karyawan di dalam satu klien

Izin `hrm.employees.view-confidential` dan saklar `restrict_confidential_employee_data` di `hrm/hrm-configs`.

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 4.13 | Role staf tanpa izin: buka `hrm/employees`, lihat data karyawan lain | Kolom gaji, NIK, NPWP, rekening tidak ada |
| 4.14 | Role staf yang sama: buka profil karyawan lain, kartu gaji | Pesan tidak punya akses; `salary-structure` 403 |
| 4.15 | Role staf: daftar slip gaji | Hanya slip milik sendiri; membuka slip orang lain 403 |
| 4.16 | Role staf: dropdown karyawan (`options`) | Tanpa `basic_salary` |
| 4.17 | Role HR dengan izin `view-confidential`: ulangi 4.13 sampai 4.16 | Semua data terlihat |
| 4.18 | Role staf mengedit data karyawan lain (field non-rahasia) lalu simpan | NIK, NPWP, rekening, gaji di database tidak berubah (tidak terhapus) |
| 4.19 | Matikan saklar pembatasan di HRM Configs | Semua role dengan akses halaman melihat data seperti semula |
| 4.20 | Karyawan membuka slip gaji dan data dirinya sendiri | Selalu terlihat, tanpa izin khusus |

## Netralisasi

Restore Klien A; hidupkan kembali saklar kerahasiaan (bawaan aktif).
