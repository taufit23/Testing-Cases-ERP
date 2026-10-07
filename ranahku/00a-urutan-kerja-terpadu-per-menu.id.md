---
title: Ranahku — Urutan Kerja Terpadu per Menu (Satu Kunjungan per Halaman)
description: Menyusun ulang seluruh butir uji dari berkas 01 sampai 11 menjadi satu jalur kerja berdasarkan halaman aplikasi, sehingga penguji membuka setiap halaman sekali: semua pengaturan dan master data dikerjakan per halaman (Fase B), semua transaksi per modul (Fase C), akuntansi dan penutupan di akhir (Fase D), lalu uji lintas, peran, dan regresi (Fase E). Setiap butir uji muncul tepat satu kali.
---

# Ranahku — Urutan Kerja Terpadu per Menu

> Disusun 2026-10-07. Berkas 01–11 adalah **katalog** butir uji, ditulis menurut topik dan tanggal ditemukan; membacanya berurutan membuat penguji
> membuka halaman yang sama berkali-kali (mis. POS Configs delapan kali, Inventory Config enam kali) dan berpindah akun berulang. Berkas ini adalah **jalur kerja**:
> urutan sesi yang mengerjakan semua butir, satu halaman atau satu modul sekali jalan, tanpa melanggar ketergantungan data.
>
> **Aturan pakai**
> 1. Ikuti sesi dari atas ke bawah. Tiap sesi menyebut halaman yang dibuka, akun yang dipakai, dan sesi yang harus selesai lebih dulu.
> 2. Langkah rinci tiap butir tetap ada di berkas sumbernya (kolom *Berkas*); berkas ini hanya mengatur **kapan dan di mana**.
> 3. Butir `01`, `02`, `03` tidak punya nomor per baris; sesi menyebutnya lewat tahap (kolom *Rujukan berkas 01–03*).
> 4. Butir negatif ("coba hal yang salah") dikerjakan **di halaman yang sama dengan butir positifnya**, saat Anda sudah berada di sana. Beberapa butir negatif sengaja
>    ditaruh sebelum pengaturan yang menutup celahnya (ditandai "sebelum").
> 5. Hasil: centang kolom OK; temuan dicatat sesuai format di berkas 06.
>
> **Prinsip penyusunan:** (a) pengaturan lebih dulu, baru transaksi, baru laporan, baru penutupan, karena penutupan periode mengunci posting; (b) satu halaman satu kali;
> (c) satu akun satu kali: butir yang butuh login lain dikumpulkan di Sesi E02; (d) hal yang merusak atau mengunci (tahun uji `FY-TEST`, cabang uji, penutupan periode) paling akhir.

## Peta Sesi

| Fase | Sesi | Judul |
| --- | --- | --- |
| FASE B | B01 | Pengaturan cabang dan format tanggal |
| FASE B | B02 | Struktur dasar: mata uang, tahun buku, kegiatan usaha |
| FASE B | B03 | Bagan akun, tipe akun, tipe jurnal, dan pajak |
| FASE B | B04 | Pengaturan persediaan dan valuasi |
| FASE B | B05 | Gudang dan master restoran |
| FASE B | B06 | Pemasok dan pelanggan |
| FASE B | B07 | Produk: kategori, satuan, produk toko, menu, layanan sewa |
| FASE B | B08 | SDM: departemen, jabatan, karyawan, jenis cuti, referensi pajak, KPI |
| FASE B | B09 | Rekening bank dan saldo awal |
| FASE B | B10 | Konfigurasi Sales dan Sales Channel |
| FASE B | B11 | Konfigurasi Kasir (POS) dan Meja Kasir |
| FASE B | B12 | Konfigurasi Restoran dan Rental |
| FASE B | B13 | Konfigurasi Pembelian dan biaya logistik |
| FASE B | B14 | Konfigurasi SDM dan Payroll |
| FASE B | B15 | Konfigurasi Manufaktur dan Pertambangan |
| FASE B | B16 | Persetujuan: alur dan ambang |
| FASE B | B17 | Master pelengkap, metode bayar, dan kop dokumen |
| FASE C | C01 | Pembelian |
| FASE C | C02 | Persediaan |
| FASE C | C03 | Kanvasing dan Penjualan |
| FASE C | C04 | Kasir toko (POS) |
| FASE C | C05 | Rumah makan |
| FASE C | C06 | Manufaktur (Dapur Produksi) |
| FASE C | C07 | Pertambangan (Tambang Pasir Percontohan) |
| FASE C | C08 | Rental |
| FASE C | C09 | SDM: rekrutmen, absensi, perubahan status, payroll |
| FASE D | D01 | Valuasi persediaan (laporan dan jurnal) |
| FASE D | D02 | Jurnal manual dan kasus mata uang asing |
| FASE D | D03 | Aset tetap dan penyusutan |
| FASE D | D04 | Rekonsiliasi bank |
| FASE D | D05 | Anggaran |
| FASE D | D06 | Buku besar dan neraca saldo |
| FASE D | D07 | Laporan pajak |
| FASE D | D08 | Laporan keuangan |
| FASE D | D09 | Periode dan tahun buku (paling akhir, bersifat mengunci) |
| FASE D | D10 | Akuntansi terpusat (cabang uji) |
| FASE E | E01 | Siklus penuh, kasus keuangan, dan uji prinsip |
| FASE E | E02 | Uji peran dan hak akses (satu kali login per akun) |
| FASE E | E03 | Akun, keamanan, privasi, paket, dan langganan |
| FASE E | E04 | Sapuan akhir: dashboard, bahasa, ekspor, hapus, muat ulang, log |
| FASE E | E05 | Uji ulang temuan yang sudah diperbaiki |

## Akun dan Peralatan (siapkan sekali di awal)

| Peran | Dipakai di sesi | Catatan |
| --- | --- | --- |
| Admin (pemilik cabang Ranahku) | hampir semua | Akun utama; password karyawan disamakan di berkas 01 Tahap 9 |
| Kasir (Fitri Handayani) | C04, C05 | Profil browser terpisah agar sesi kasir dan admin berjalan berdampingan |
| HR (Yoga Pratama) dan Manajer | C09, E02 | Izin *view-confidential* hanya untuk HR |
| Karyawan biasa (non-HR) | E02 | Untuk uji slip sendiri, cuti, kerahasiaan |
| Direktur (Arman Halim) | E02 | Persetujuan bertingkat |

Gunakan **tiga profil browser** (Admin, Kasir, Karyawan/HR bergantian) agar tidak keluar-masuk akun. Untuk uji perangkat terikat (BM3) siapkan satu profil lagi.


---

# FASE B — Pengaturan dan Master Data (satu kunjungan per halaman)


## Sesi B01 — Pengaturan cabang dan format tanggal

- **Halaman:** Client Master → Branch Setup (dan App Setup)
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** —
- **Rujukan berkas 01–03:** `01` Tahap 1.1 (pastikan cabang aktif = Ranahku)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| Y14 | 04 | Client Master → Branch Setup | ⬜ |
| BK1.1 | 10 | Buka daftar Jurnal, Produk, Pajak, Status, Pengguna | ⬜ |
| BK1.2 | 10 | Branch Setup → `date_format` = `YYYY-MM-DD`, simpan, muat ulang | ⬜ |
| BK1.3 | 10 | Coba `D MMM YYYY` dan `MM/DD/YYYY` | ⬜ |
| BK1.4 | 10 | Kembalikan ke `DD-MM-YYYY` | ⬜ |

## Sesi B02 — Struktur dasar: mata uang, tahun buku, kegiatan usaha

- **Halaman:** Client Master → Currencies, Exchange Rates, Fiscal Year, Accounting Period, Business Units
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B01
- **Rujukan berkas 01–03:** `01` Tahap 1.2–1.4; Siapkan juga tahun uji `FY-TEST` (generate bulanan, mingguan, kuartalan; satu pasang periode tumpang tindih; satu tahun dengan satu periode) agar tidak kembali ke halaman ini nanti. Isi mata uang USD dan dua kurs (15.800 aktif, 16.000 belum aktif).

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| BD3 | 09 | Buat mata uang `IDR` dua kali di cabang yang sama | ⬜ |
| BD4 | 09 | Buat Business Unit dengan `default_unit_type` di luar `cost/profit/bot | ⬜ |
| BD5 | 09 | Buat Business Unit dengan kode duplikat | ⬜ |
| BD7 | 09 | Kirim id milik cabang lain (akun, kegiatan, gudang) pada payload | ⬜ |
| BD8 | 09 | Pakai `business_unit_id` cabang lain pada laporan | ⬜ |
| BD9 | 09 | Generate periode untuk Fiscal Year yang sama dua kali | ⬜ |
| BD10 | 09 | Setelah generate, hitung periode | ⬜ |
| BD11 | 09 | Daftar mata uang dengan kurs `0` atau negatif | ⬜ |
| BD12 | 09 | Jurnal mata uang asing tanpa kurs aktif | ⬜ |

## Sesi B03 — Bagan akun, tipe akun, tipe jurnal, dan pajak

- **Halaman:** Client Master → Chart of Account Type, Chart of Accounts, General Journal Type, Taxes
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B02
- **Rujukan berkas 01–03:** `01` Tahap 2 (tipe akun, 45 akun) dan Tahap 3 (5 pajak)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| Y5 | 04 | Client Master → General Journal Type | ⬜ |
| Y6 | 04 | Client Master → Chart of Account Type | ⬜ |
| BD1 | 09 | Buat Chart of Account dengan kode duplikat (`1-110` dua kali) | ⬜ |
| BD2 | 09 | Buat tipe akun dengan Code duplikat | ⬜ |
| BK2.6 | 10 | Tipe Jurnal Umum | ⬜ |
| BK4.1 | 10 | Taxes | ⬜ |
| BK4.2 | 10 | Taxes → Template | ⬜ |

## Sesi B04 — Pengaturan persediaan dan valuasi

- **Halaman:** Inventory → Config
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B03
- **Rujukan berkas 01–03:** `01` Tahap 11.1 (pemetaan akun persediaan)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AA1 | 04 | Inventory → Config | ⬜ |
| AA2 | 04 | Inventory → Config | ⬜ |
| AA5 | 04 | Inventory → Config | ⬜ |
| AA9 | 04 | Inventory → Config | ⬜ |

## Sesi B05 — Gudang dan master restoran

- **Halaman:** Client Master → Warehouses; Restaurant → Areas, Tables, Kitchen Stations
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B03
- **Rujukan berkas 01–03:** `01` Tahap 4 dan Tahap 7.5

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| BH1 | 09 | Buat gudang dengan cabang selain cabang aktif | ⬜ |

## Sesi B06 — Pemasok dan pelanggan

- **Halaman:** Client Master → Contacts (+ alamat dan rekening bank)
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B03
- **Rujukan berkas 01–03:** `01` Tahap 5

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| Y12 | 04 | Client Master → Contact Addresses dan Contact Bank Accounts | ⬜ |
| BD16 | 09 | Kontak bertipe `customer` dipilih sebagai pemasok | ⬜ |
| BK2.8 | 10 | Kontak baru | ⬜ |
| BK2.9 | 10 | Form tambah massal (kontak, gudang, satuan, pajak, akun, jabatan) | ⬜ |
| BK4.6 | 10 | Contacts | ⬜ |

## Sesi B07 — Produk: kategori, satuan, produk toko, menu, layanan sewa

- **Halaman:** Client Master → Product Categories, Product Units, Products/SKUs, Price Lists, Modifiers, Recipes, Print Labels
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B03, B05, B06
- **Rujukan berkas 01–03:** `01` Tahap 6 (6.1–6.5), Tahap 7.1–7.4, Tahap 8; Tambahkan produk bahan segar (Sayur Campur, Ayam Potong, Telur Ayam) dan beri **Sales Channel** pada semua menu

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AA3 | 04 | Client Master → Products → menu SKU → Inventory Valuation | ⬜ |
| Y3 | 04 | Client Master → Product Modifiers | ⬜ |
| Y4 | 04 | Client Master → Product Recipes | ⬜ |
| Z10 | 04 | Client Master → Products → Print Labels | ⬜ |
| BD6 | 09 | Buat produk dengan kategori teks bebas di luar daftar (bila ada enum) | ⬜ |
| BD15 | 09 | Produk dengan SKU duplikat di cabang yang sama | ⬜ |
| BK4.3 | 10 | Product SKU → Default Purchase Taxes | ⬜ |

## Sesi B08 — SDM: departemen, jabatan, karyawan, jenis cuti, referensi pajak, KPI

- **Halaman:** HRM → Departments, Positions, Employees, Leave Types, Attendance Statuses, Employment Types, BPJS dan Payroll Tax Reference, Organization Structure, Salary Components, Attendance Devices, KPI; Roles
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B03
- **Rujukan berkas 01–03:** `01` Tahap 9 (9.1–9.5)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AE1 | 04 | HRM → Organization Structure | ⬜ |
| AE2 | 04 | HRM → Salary Components | ⬜ |
| AE3 | 04 | HRM → Attendance Devices | ⬜ |
| Y13 | 04 | Client Master → KPI Criteria (di SDM: Activity Types dan Employee Acti | ⬜ |
| BH13 | 09 | Buat karyawan dengan departemen/jabatan yang tidak ada atau milik caba | ⬜ |
| BK2.1 | 10 | Kriteria KPI | ⬜ |
| BK3.1 | 10 | Departments | ⬜ |
| BK3.2 | 10 | Attendance Statuses | ⬜ |
| BK3.3 | 10 | Employment Types | ⬜ |
| BK3.4 | 10 | Referensi Pajak Penghasilan (PTKP) | ⬜ |
| BK3.9 | 10 | Leave Types | ⬜ |
| BK3.11 | 10 | Employees | ⬜ |
| BK3.12 | 10 | Roles | ⬜ |

## Sesi B09 — Rekening bank dan saldo awal

- **Halaman:** Finance → Bank Accounts; Client Master → Chart of Accounts Balances
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B02, B03
- **Rujukan berkas 01–03:** `01` Tahap 10 (10.1 dan 10.2)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AO1 | 05 | Rekening bank | ⬜ |
| BD13 | 09 | Buat akun bank dengan akun COA non-kas | ⬜ |
| BD17 | 09 | Buat saldo awal sebelum ada akun bertanda Ekuitas Saldo Awal (`3-103`) | ⬜ |
| BD18 | 09 | Setelah `3-103` ada, buat saldo awal Kas Kecil 3.000.000 | ⬜ |
| BD19 | 09 | Buat dua akun bertanda Ekuitas Saldo Awal | ⬜ |
| BD20 | 09 | Buat saldo awal untuk akun yang `balance_required` tidak diaktifkan (m | ⬜ |
| BD21 | 09 | `opening_balance` berisi teks atau mata uang yang tidak ada | ⬜ |
| BD22 | 09 | Saldo awal akun kewajiban (Utang Usaha) | ⬜ |
| BD23 | 09 | Saldo awal memakai field debit/kredit total (`debit_total`, `credit_to | ⬜ |
| BD24 | 09 | Saldo awal akun bank dengan mata uang asing | ⬜ |
| BD25 | 09 | Ubah saldo awal setelah dipakai transaksi | ⬜ |
| BD26 | 09 | Saldo di tabel saldo awal vs buku besar | ⬜ |
| BD27 | 09 | Total saldo awal | ⬜ |
| BD28 | 09 | Modal awal dan neraca pembuka dibandingkan berkas 00 | ⬜ |
| BJ8 | 09 | Rekening bank USD | ⬜ |
| BJ9 | 09 | Saldo awal akun kewajiban valas | ⬜ |

## Sesi B10 — Konfigurasi Sales dan Sales Channel

- **Halaman:** Sales → Sales Configs, Sales Journal Configuration; Client Master → Sales Channels
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B09
- **Rujukan berkas 01–03:** `01` Tahap 11.2

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AF1 | 04 | Sales → Sales Configs | ⬜ |
| BF12 | 09 | Sales Config belum disetel lalu terbitkan faktur dengan jurnal | ⬜ |
| BK2.7 | 10 | Sales Channels | ⬜ |

## Sesi B11 — Konfigurasi Kasir (POS) dan Meja Kasir

- **Halaman:** POS → POS Configs, Cash Registers, Cash Denominations
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B05, B09
- **Rujukan berkas 01–03:** `01` Tahap 11.3

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| Z1 | 04 | Client Master → Cash Registers | ⬜ |
| Z4 | 04 | Client Master → Cash Denominations | ⬜ |
| Z5 | 04 | POS → POS Configs (hitung kas) | ⬜ |
| Z8 | 04 | POS → POS Configs → Struk | ⬜ |
| Z9 | 04 | POS → POS Configs → pengaturan lain | ⬜ |
| BG17 | 09 | Buat transaksi sebelum fungsi jurnal kasir (kas, pendapatan, PPN) dipe | ⬜ |
| BK5.1 | 10 | Cash Registers | ⬜ |
| BK5.2 | 10 | Cash Registers | ⬜ |
| BK5.3 | 10 | Mesin berisi sesi terbuka | ⬜ |
| BK5.4 | 10 | POS Configs → Register device binding | ⬜ |
| BK5.5 | 10 | POS Configs → pemantauan | ⬜ |
| BK5.6 | 10 | Cash Registers → kolom | ⬜ |

## Sesi B12 — Konfigurasi Restoran dan Rental

- **Halaman:** Restaurant → Config; Rental → Rental Configs
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B05, B09
- **Rujukan berkas 01–03:** `01` Tahap 11.4 dan 11.5

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AF2 | 04 | Rental → Rental Configs | ⬜ |

## Sesi B13 — Konfigurasi Pembelian dan biaya logistik

- **Halaman:** Purchasing → Purchase Configs, Purchase Charge Configs
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B06, B09
- **Rujukan berkas 01–03:** `01` Tahap 11.6

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AB1 | 04 | Purchasing → Purchase Configs | ⬜ |
| AB9 | 04 | Purchasing → Purchase Charge Configs | ⬜ |
| BE24 | 09 | Konfigurasi akun pembelian belum dipetakan lalu export jurnal | ⬜ |
| BK4.4 | 10 | Purchasing → Purchase Configs | ⬜ |
| BK4.5 | 10 | Purchase Configs → pemetaan akun | ⬜ |

## Sesi B14 — Konfigurasi SDM dan Payroll

- **Halaman:** HRM → HRM Configs, Payroll Journal Configuration
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B08, B09
- **Rujukan berkas 01–03:** `01` Tahap 11.7

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| BK3.5 | 10 | HRM Configs → Siklus Payroll | ⬜ |
| BK3.6 | 10 | HRM Configs → Absensi | ⬜ |
| BK3.7 | 10 | HRM Configs → Alur Kerja | ⬜ |
| BK3.8 | 10 | HRM Configs → Kerahasiaan | ⬜ |

## Sesi B15 — Konfigurasi Manufaktur dan Pertambangan

- **Halaman:** Manufacturing → Config, Work Centers; Mining → Config, Sites, Pits, Equipment, Quality Parameters, Stockpiles
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B05, B09
- **Rujukan berkas 01–03:** Aktifkan modul untuk cabang (paket) sebelum membuka halaman; petakan akun (auto-map)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AC1 | 04 | Manufacturing → Config | ⬜ |
| AC2 | 04 | Manufacturing → Work Centers | ⬜ |
| AD1 | 04 | Mining → Config | ⬜ |
| AD2 | 04 | Mining → Sites, Pits, Equipment, Quality Parameters, Stockpiles | ⬜ |

## Sesi B16 — Persetujuan: alur dan ambang

- **Halaman:** Client Master → Approval Workflow Configs, Approval Amount Thresholds
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B08, B13, B14, B15
- **Rujukan berkas 01–03:** `01` (peran hasil Tahap 9)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| Y7 | 04 | Client Master → Approval Workflow Configs | ⬜ |
| Y8 | 04 | Client Master → Approval Amount Thresholds | ⬜ |
| BK3.10 | 10 | Approval Workflow Configs | ⬜ |

## Sesi B17 — Master pelengkap, metode bayar, dan kop dokumen

- **Halaman:** Client Master → Payment Methods, Payment Terms, Order Types, Charge Types, Transaction Paterns, Legal Document Types, Member Tiers, Cashback Rules, Discounts, Cost Centers, Expense Categories; Pengaturan tampilan PDF
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B03
- **Rujukan berkas 01–03:** `01` Tahap 12; `03` Tahap N (hanya bagian master: Cost Centers, Discounts, Cashback Rules, Member Tiers, Expense Categories)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| Y1 | 04 | Client Master → Order Types | ⬜ |
| Y2 | 04 | Client Master → Charge Types | ⬜ |
| Y9 | 04 | Client Master → Transaction Patern Types dan Transaction Paterns | ⬜ |
| Y10 | 04 | Client Master → Legal Document Types | ⬜ |
| Y16 | 04 | Pengaturan tampilan PDF (PDF Layout Settings) | ⬜ |
| BK2.2 | 10 | Aturan Cashback, Tipe Dokumen Legal | ⬜ |
| BK2.4 | 10 | Tingkat Member | ⬜ |
| BK2.5 | 10 | Unduh template saat server gagal | ⬜ |
| BK6.1 | 10 | Tab Letterhead: isi NPWP, baris kontak, posisi dan ukuran logo, kop te | ⬜ |
| BK6.2 | 10 | Tab Appearance: font, ukuran, margin, rata judul, watermark | ⬜ |
| BK6.3 | 10 | Gaya angka dan tanggal | ⬜ |
| BK6.4 | 10 | Label tanda tangan | ⬜ |
| BK6.5 | 10 | Pop out pratinjau | ⬜ |
| BK6.6 | 10 | Pengaturan per jenis dokumen | ⬜ |

---

# FASE C — Transaksi per Modul (satu kunjungan per modul)


## Sesi C01 — Pembelian

- **Halaman:** Purchasing → Purchase Requests, Quotations, Orders, Goods Receipts, Invoices, Payment Bills, Returns, Charge Invoices, Charge Inbox, Blanket Agreements
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** Fase B selesai
- **Rujukan berkas 01–03:** `02` Tahap E (E.1–E.3); `03` Tahap P (bagian Blanket Agreements)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AA4 | 04 | Pembelian → Goods Receipt | ⬜ |
| AA7 | 04 | Client Master → Products → Inventory Valuation | ⬜ |
| AB2 | 04 | Purchasing → Purchase Requests | ⬜ |
| AB3 | 04 | Purchasing → Purchase Quotations | ⬜ |
| AB4 | 04 | PR → Compare Quotations | ⬜ |
| AB5 | 04 | Compare Quotations | ⬜ |
| AB6 | 04 | Purchasing → Purchase Orders | ⬜ |
| AB7 | 04 | PO | ⬜ |
| AB8 | 04 | Contacts → pemasok | ⬜ |
| AB10 | 04 | Purchasing → Purchase Charge Invoices | ⬜ |
| AB11 | 04 | Charge Invoice | ⬜ |
| AB12 | 04 | Purchasing → Purchase Charge Inbox | ⬜ |
| AB14 | 04 | Purchasing → Blanket Agreements (ulang bila belum di Tahap P) | ⬜ |
| AQ1 | 06 | Pembelian rutin | ⬜ |
| AQ2 | 06 | Pemasok baru | ⬜ |
| AQ3 | 06 | Pembelian darurat | ⬜ |
| AQ4 | 06 | Harga pemasok berubah | ⬜ |
| AQ5 | 06 | Permintaan pembelian dan persetujuan | ⬜ |
| AQ6 | 06 | Bandingkan pemasok | ⬜ |
| AQ7 | 06 | Persetujuan bertingkat | ⬜ |
| AQ8 | 06 | Perubahan setelah persetujuan | ⬜ |
| AQ9 | 06 | Pengiriman bertahap | ⬜ |
| AQ10 | 06 | Barang kurang | ⬜ |
| AQ11 | 06 | Barang rusak | ⬜ |
| AQ12 | 06 | Pembelian jasa | ⬜ |
| AQ13 | 06 | Kontrak dan pembelian berulang | ⬜ |
| AQ14 | 06 | Faktur sebagian | ⬜ |
| AQ15 | 06 | Faktur melebihi PO | ⬜ |
| AQ16 | 06 | Barang datang, faktur belum | ⬜ |
| AQ17 | 06 | PO dibatalkan | ⬜ |
| AQ18 | 06 | Pemasok gagal memenuhi | ⬜ |
| AQ19 | 06 | Pembelian berdasarkan anggaran | ⬜ |
| AQ20 | 06 | Pembelian aset | ⬜ |
| AQ21 | 06 | Biaya tambahan | ⬜ |
| AQ22 | 06 | Pertanyaan manajemen | ⬜ |
| BE1 | 09 | Submit PR tanpa satu item pun | ⬜ |
| BE2 | 09 | Buat PR dengan cabang selain cabang aktif | ⬜ |
| BE3 | 09 | Tier harga PQ dengan kontak bukan pemasok | ⬜ |
| BE4 | 09 | Hapus item PQ yang sudah dipakai pada tier harga | ⬜ |
| BE5 | 09 | PO dengan qty 0 atau negatif | ⬜ |
| BE6 | 09 | PO dengan kontak bertipe pelanggan | ⬜ |
| BE7 | 09 | PR ditolak, lalu langsung Submit lagi | ⬜ |
| BE8 | 09 | PO tanpa PQ ketika konfigurasi tidak mewajibkan PQ | ⬜ |
| BE9 | 09 | PO tanpa PQ ketika konfigurasi mewajibkan PQ | ⬜ |
| BE10 | 09 | Buat PO dari PR yang belum disetujui (persetujuan PR aktif) | ⬜ |
| BE11 | 09 | Goods Receipt melebihi sisa PO (PO 50, terima 60) | ⬜ |
| BE12 | 09 | GR kedua untuk PO yang sudah diterima penuh | ⬜ |
| BE13 | 09 | Export jurnal GR yang sudah pernah diekspor | ⬜ |
| BE14 | 09 | Purchase Invoice dengan qty lebih besar dari GR | ⬜ |
| BE15 | 09 | Invoice tanpa GR ketika konfigurasi mengizinkan | ⬜ |
| BE16 | 09 | Invoice tanpa GR ketika konfigurasi mewajibkan GR | ⬜ |
| BE17 | 09 | Bayar (create/mark-paid) sebelum Purchase Invoice disetujui | ⬜ |
| BE18 | 09 | Bayar melebihi sisa utang faktur | ⬜ |
| BE19 | 09 | Export jurnal faktur yang sudah diekspor | ⬜ |
| BE20 | 09 | Pembayaran dengan metode tanpa akun terpetakan | ⬜ |
| BE21 | 09 | PO dengan produk tak ada di cabang ini | ⬜ |
| BE22 | 09 | Ubah pemasok pada PO yang sudah punya GR | ⬜ |
| BE23 | 09 | Hapus PO yang sudah punya GR | ⬜ |
| BK4.7 | 10 | Charge Invoice | ⬜ |
| BK6.7 | 10 | Unduh PDF satu PO dan satu laporan | ⬜ |
| BM1.1 | 10 | Buat PO dari PQ atau baru; pilih item Beras Premium 5 kg | ⬜ |
| BM1.2 | 10 | Tambah dua pajak pada satu item: PPN-IN dan PPh 23 | ⬜ |
| BM1.3 | 10 | Detail PO | ⬜ |
| BM1.4 | 10 | Jurnal dari PO ke GR dan PI | ⬜ |

## Sesi C02 — Persediaan

- **Halaman:** Inventory → Stock Transfers, Stock Adjustments, Stock Takes, Buffer Stock, Lots, Serials, Consignment, Stock History
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** C01
- **Rujukan berkas 01–03:** `03` Tahap J dan Tahap S

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AA12 | 04 | Inventory → Stock Takes | ⬜ |
| AA13 | 04 | Client Master → Stock Movements (Pergerakan Stok) | ⬜ |
| AA14 | 04 | Inventory → Stock History | ⬜ |
| AU1 | 06 | Barang masuk | ⬜ |
| AU2 | 06 | Barang digunakan | ⬜ |
| AU3 | 06 | Stok rusak | ⬜ |
| AU4 | 06 | Stok fisik berbeda | ⬜ |
| AU5 | 06 | Stok minimum dan reorder | ⬜ |
| AU6 | 06 | Masuk bertahap | ⬜ |
| AU7 | 06 | Keluar lewat penjualan | ⬜ |
| AU8 | 06 | Backorder | ⬜ |
| AU9 | 06 | Banyak gudang dan transfer | ⬜ |
| AU10 | 06 | Satuan berbeda | ⬜ |
| AU11 | 06 | Satuan berat | ⬜ |
| AU12 | 06 | Batch | ⬜ |
| AU13 | 06 | Tanggal kedaluwarsa | ⬜ |
| AU14 | 06 | Nomor seri | ⬜ |
| AU15 | 06 | Retur pelanggan dan pemasok | ⬜ |
| AU16 | 06 | Penyesuaian stok | ⬜ |
| AU17 | 06 | Stok tercadang | ⬜ |
| AU18 | 06 | Beli dan jual bersamaan | ⬜ |
| AU19 | 06 | Produksi | ⬜ |
| AU20 | 06 | Paket/bundle | ⬜ |
| AU21 | 06 | Konsinyasi | ⬜ |
| AU22 | 06 | Barang milik pelanggan | ⬜ |
| AU23 | 06 | Dalam perjalanan | ⬜ |
| AU24 | 06 | Kehilangan stok | ⬜ |
| AU25 | 06 | Barang gratis | ⬜ |
| AU26 | 06 | Stok negatif | ⬜ |
| BH2 | 09 | Post Stock Adjustment tanpa Submit lebih dulu (bila status mensyaratka | ⬜ |
| BH3 | 09 | Stock Adjustment dengan unit cost 0 pada item selisih | ⬜ |
| BH4 | 09 | Hapus pemetaan akun `inventory_loss` lalu ulangi skenario susut | ⬜ |
| BH5 | 09 | Nomor seri duplikat | ⬜ |
| BH6 | 09 | Opname dengan hasil fisik lebih kecil dari sistem | ⬜ |
| BH7 | 09 | Selesaikan opname dua kali | ⬜ |
| BH8 | 09 | Transfer stok melebihi stok | ⬜ |
| BH9 | 09 | Terima transfer melebihi yang dikirim | ⬜ |
| BH10 | 09 | Pergerakan stok manual tanpa alasan | ⬜ |
| BH11 | 09 | Hapus gudang yang masih berisi stok | ⬜ |
| BH12 | 09 | Penyesuaian akhir stok negatif | ⬜ |

## Sesi C03 — Kanvasing dan Penjualan

- **Halaman:** Canvassing → Visits, Orders, Collections, Targets, Routes, Custodies, Competitors; Sales → Quotations, Orders, Deliveries, Invoices, Payment Bills, Returns
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** C01, C02
- **Rujukan berkas 01–03:** `02` Tahap A, B, C.2, D.2; `03` Tahap K dan Tahap R

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AA8 | 04 | Sales → Sales Delivery → Create | ⬜ |
| AR1 | 06 | Pesanan langsung | ⬜ |
| AR2 | 06 | Pesanan katering | ⬜ |
| AR3 | 06 | Perubahan pesanan | ⬜ |
| AR4 | 06 | Pembatalan | ⬜ |
| AR5 | 06 | Pelanggan minta tempo | ⬜ |
| AR6 | 06 | Barang tidak cukup | ⬜ |
| AR7 | 06 | Pengiriman sebagian | ⬜ |
| AR8 | 06 | Jasa dan kontrak | ⬜ |
| AR9 | 06 | Pembayaran bertahap | ⬜ |
| AR10 | 06 | Perubahan lingkup | ⬜ |
| AR11 | 06 | Pelanggan baru | ⬜ |
| AR12 | 06 | Harga khusus pelanggan | ⬜ |
| AR13 | 06 | Diskon | ⬜ |
| AR14 | 06 | Harga berubah setelah pesanan | ⬜ |
| AR15 | 06 | Pembatalan sebagian oleh pelanggan | ⬜ |
| AR16 | 06 | Retur barang | ⬜ |
| AR17 | 06 | Barang ditolak | ⬜ |
| AR18 | 06 | Pengiriman terlambat | ⬜ |
| AR19 | 06 | Dari penawaran | ⬜ |
| AR20 | 06 | Uang muka | ⬜ |
| AR21 | 06 | Pembayaran sebagian dan tidak membayar | ⬜ |
| AR22 | 06 | Pertanyaan manajemen | ⬜ |
| BC1 | 08 | Faktur sewa disengketakan sebagian (klaim ditolak sebagian) | ⬜ |
| BC2 | 08 | Pembayar berbeda untuk satu layanan (BPJS vs asuransi vs tunai) | ⬜ |
| BC3 | 08 | Diskon sebagai kontra-pendapatan (beasiswa/potongan SPP) | ⬜ |
| BC9 | 08 | Penagihan berulang bulanan | ⬜ |
| BF1 | 09 | Sales Order dengan SKU yang sama di dua baris | ⬜ |
| BF2 | 09 | Quotation: Customer Accept sebelum status Sent | ⬜ |
| BF3 | 09 | SO tanpa quotation ketika `require_quotation_for_so` aktif | ⬜ |
| BF4 | 09 | SO dengan qty 0 | ⬜ |
| BF5 | 09 | Setujui SO melebihi batas kredit pelanggan (batas dikecilkan untuk uji | ⬜ |
| BF6 | 09 | Kode diskon yang sudah dinonaktifkan | ⬜ |
| BF7 | 09 | Kode diskon kedaluwarsa atau melebihi kuota pemakaian | ⬜ |
| BF8 | 09 | Delivery melebihi sisa SO | ⬜ |
| BF9 | 09 | Invoice melebihi nilai SO | ⬜ |
| BF10 | 09 | Export jurnal faktur yang sudah diekspor | ⬜ |
| BF11 | 09 | Terima pembayaran melebihi sisa piutang | ⬜ |
| BF13 | 09 | Retur penjualan tanpa akun retur/kontra pendapatan | ⬜ |
| BF14 | 09 | Delivery: apakah menyentuh buku besar? | ⬜ |
| BF15 | 09 | Ubah pelanggan pada SO yang sudah punya delivery | ⬜ |
| BF16 | 09 | Hapus SO yang sudah punya faktur | ⬜ |
| BF17 | 09 | Penjualan jasa (tanpa stok) memilih gudang | ⬜ |
| BF18 | 09 | Perpanjangan kontrak bulanan | ⬜ |
| BM1.5 | 10 | SO: opsi sumber SO menampilkan nama pelanggan | ⬜ |
| BM1.6 | 10 | Quotation dan SO | ⬜ |

## Sesi C04 — Kasir toko (POS)

- **Halaman:** POS → Cash Sessions, POS Transactions, Customer Display, Cashier Deposits
- **Akun:** Kasir (Fitri) dan Admin (dua profil browser)
- **Prasyarat:** C02, B11
- **Rujukan berkas 01–03:** `02` Tahap C.1 dan C.3; `03` Tahap P (bagian POS)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| Z2 | 04 | POS → Cash Sessions | ⬜ |
| Z3 | 04 | POS → POS Transactions | ⬜ |
| Z6 | 04 | POS → transaksi | ⬜ |
| Z7 | 04 | POS → Customer Display | ⬜ |
| Z11 | 04 | POS → Cashier Deposits (Client Master) | ⬜ |
| Z12 | 04 | POS → tutup sesi | ⬜ |
| AS1 | 06 | Retail sederhana | ⬜ |
| AS2 | 06 | Pembeli tidak terdaftar | ⬜ |
| AS3 | 06 | Pembeli terdaftar/member | ⬜ |
| AS4 | 06 | Banyak metode bayar | ⬜ |
| AS5 | 06 | Bayar lebih | ⬜ |
| AS6 | 06 | Bayar kurang | ⬜ |
| AS7 | 06 | Diskon per item dan seluruh transaksi | ⬜ |
| AS8 | 06 | Promo dan promo waktu | ⬜ |
| AS9 | 06 | Diskon member dan tingkat member | ⬜ |
| AS10 | 06 | Poin/loyalti dan cashback | ⬜ |
| AS11 | 06 | Retur produk | ⬜ |
| AS12 | 06 | Refund sebagian dan penuh | ⬜ |
| AS13 | 06 | Refund lewat metode berbeda | ⬜ |
| AS14 | 06 | Salah harga / salah produk | ⬜ |
| AS15 | 06 | Void sebelum dan sesudah bayar | ⬜ |
| AS16 | 06 | Pelanggan mengubah pesanan | ⬜ |
| AS17 | 06 | Tahan transaksi | ⬜ |
| AS18 | 06 | Perubahan harga | ⬜ |
| AS19 | 06 | Promo bertumpuk dan diskon manual | ⬜ |
| AS20 | 06 | Shift kasir | ⬜ |
| AS21 | 06 | Kas keluar dan kas masuk | ⬜ |
| AS22 | 06 | Tutup shift | ⬜ |
| AS23 | 06 | Kas lebih dan kurang | ⬜ |
| AS24 | 06 | Pembayaran gagal | ⬜ |
| AS25 | 06 | Pembayaran ganda | ⬜ |
| AS26 | 06 | Beda outlet | ⬜ |
| AS27 | 06 | POS offline | ⬜ |
| AS28 | 06 | POS tidak bisa dipakai | ⬜ |
| AS29 | 06 | Stok tidak cukup | ⬜ |
| AS30 | 06 | Retur tanpa struk | ⬜ |
| AS31 | 06 | Struk ulang | ⬜ |
| AS32 | 06 | Riwayat transaksi | ⬜ |
| AS33 | 06 | Kinerja kasir | ⬜ |
| AS34 | 06 | Transaksi mencurigakan | ⬜ |
| AS35 | 06 | Tutup harian | ⬜ |
| AS36 | 06 | Transaksi ≠ pembayaran | ⬜ |
| AS37 | 06 | Transaksi ≠ kas | ⬜ |
| AS38 | 06 | Penjualan ≠ laba | ⬜ |
| AS39 | 06 | Keluhan pelanggan | ⬜ |
| AS40 | 06 | Pertanyaan manajemen | ⬜ |
| BG1 | 09 | Buka sesi kasir di gudang bertipe pusat/central | ⬜ |
| BG2 | 09 | Buka sesi dengan gudang milik cabang lain | ⬜ |
| BG3 | 09 | Buka sesi kedua di meja/gudang yang sama saat sesi pertama masih terbu | ⬜ |
| BG4 | 09 | Satu kasir membuka dua sesi | ⬜ |
| BG5 | 09 | Tutup sesi yang sudah tertutup | ⬜ |
| BG6 | 09 | Buat transaksi pada sesi yang sudah tertutup | ⬜ |
| BG7 | 09 | Bayar tunai dengan uang diterima < total | ⬜ |
| BG8 | 09 | Dua baris pembayaran yang totalnya ≠ total transaksi | ⬜ |
| BG9 | 09 | Pembayaran QRIS dibatalkan atau timeout | ⬜ |
| BG10 | 09 | Tahan transaksi (hold) | ⬜ |
| BG11 | 09 | Panggil kembali transaksi yang sudah selesai atau di-void | ⬜ |
| BG12 | 09 | Void transaksi yang sudah void | ⬜ |
| BG13 | 09 | Refund melebihi qty yang dibeli (beli 5, refund 10) | ⬜ |
| BG14 | 09 | Refund transaksi yang sudah void | ⬜ |
| BG15 | 09 | Jual barang yang stoknya 0 di gudang ini tetapi ada di gudang toko lai | ⬜ |
| BG16 | 09 | Transfer stok melebihi stok tersedia di pusat | ⬜ |
| BG18 | 09 | Bayar dengan kartu debit dan QRIS | ⬜ |
| BG19 | 09 | HPP kasir | ⬜ |
| BM3.1 | 10 | Perangkat A membuka sesi di Kasir Toko 1 | ⬜ |
| BM3.2 | 10 | Perangkat B mencoba membuka sesi di mesin yang sama | ⬜ |
| BM3.3 | 10 | Manajer menekan release the locked device | ⬜ |
| BM3.4 | 10 | Buka sesi dengan gudang selain gudang mesin | ⬜ |
| BM3.5 | 10 | Biarkan mesin menganggur melewati ambang dan sesi terbuka melewati jam | ⬜ |
| BM3.6 | 10 | Cara hitung kas tutup sesi | ⬜ |

## Sesi C05 — Rumah makan

- **Halaman:** Restaurant → Bookings, Orders, Order Items, Tables, Kitchen Display, Floor Plan, Menu
- **Akun:** Kasir/Pelayan dan Admin
- **Prasyarat:** C02, B05
- **Rujukan berkas 01–03:** `02` Tahap D.1; `03` Tahap O

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AT1 | 06 | Restoran baru buka | ⬜ |
| AT2 | 06 | Tamu datang tanpa reservasi | ⬜ |
| AT3 | 06 | Reservasi | ⬜ |
| AT4 | 06 | Tamu terlambat | ⬜ |
| AT5 | 06 | Tamu tidak datang | ⬜ |
| AT6 | 06 | Status meja | ⬜ |
| AT7 | 06 | Pindah meja | ⬜ |
| AT8 | 06 | Gabung dan pisah meja | ⬜ |
| AT9 | 06 | Jumlah tamu berubah | ⬜ |
| AT10 | 06 | Pesanan pertama dan tambahan | ⬜ |
| AT11 | 06 | Batal item | ⬜ |
| AT12 | 06 | Modifier | ⬜ |
| AT13 | 06 | Menu habis | ⬜ |
| AT14 | 06 | Bahan habis | ⬜ |
| AT15 | 06 | Pesanan ke dapur | ⬜ |
| AT16 | 06 | Status dapur | ⬜ |
| AT17 | 06 | Siap sebagian | ⬜ |
| AT18 | 06 | Dapur terlambat dan prioritas | ⬜ |
| AT19 | 06 | Pesanan salah | ⬜ |
| AT20 | 06 | Sisa makanan dan bahan rusak | ⬜ |
| AT21 | 06 | Resep dan perubahan resep | ⬜ |
| AT22 | 06 | Ukuran porsi dan combo | ⬜ |
| AT23 | 06 | Bungkus dan antar | ⬜ |
| AT24 | 06 | Status antar dan mitra | ⬜ |
| AT25 | 06 | Permintaan dan keluhan tamu | ⬜ |
| AT26 | 06 | Gratis dan diskon manajer | ⬜ |
| AT27 | 06 | Service charge dan pajak | ⬜ |
| AT28 | 06 | Pisah tagihan dan pisah item | ⬜ |
| AT29 | 06 | Gabung tagihan | ⬜ |
| AT30 | 06 | Tamu pergi tanpa bayar | ⬜ |
| AT31 | 06 | Pembayaran dan multi pembayaran | ⬜ |
| AT32 | 06 | Refund dan void | ⬜ |
| AT33 | 06 | Tutup meja dan bersihkan | ⬜ |
| AT34 | 06 | Shift pelayan, dapur, kasir | ⬜ |
| AT35 | 06 | Tutup harian | ⬜ |
| AT36 | 06 | Jam sibuk dan kinerja menu | ⬜ |
| AT37 | 06 | Profitabilitas menu | ⬜ |
| AT38 | 06 | Pelanggan langganan dan member | ⬜ |
| AT39 | 06 | Deposit reservasi dan no-show | ⬜ |
| AT40 | 06 | Stok teoritis vs aktual | ⬜ |
| AT41 | 06 | Permintaan bahan dapur dan pengiriman pemasok | ⬜ |
| AT42 | 06 | Keamanan pangan dan menu dinonaktifkan sementara | ⬜ |
| AT43 | 06 | Puncak pelanggan dan dapur kelebihan beban | ⬜ |
| AT44 | 06 | Self-order QR | ⬜ |
| AT45 | 06 | Pertanyaan manajemen | ⬜ |
| BG20 | 09 | Restoran: sesi meja tanpa area/meja/kitchen station | ⬜ |
| BG21 | 09 | Pesan menu yang tidak diberi Sales Channel | ⬜ |
| BG22 | 09 | Menu tanpa resep tetapi menu bahan lain | ⬜ |
| BG23 | 09 | Reservasi tumpang tindih pada meja yang sama | ⬜ |
| BG24 | 09 | Tutup meja dengan pesanan belum dibayar | ⬜ |

## Sesi C06 — Manufaktur (Dapur Produksi)

- **Halaman:** Manufacturing → Bills of Materials, Routings, Production Orders; Approvals
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** C02, B15, B16
- **Rujukan berkas 01–03:** —

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AC3 | 04 | Manufacturing → Bills of Materials | ⬜ |
| AC4 | 04 | Manufacturing → Routings | ⬜ |
| AC5 | 04 | Manufacturing → Production Orders | ⬜ |
| AC6 | 04 | Approvals → Approval Requests | ⬜ |
| AC7 | 04 | Production Order → Materials | ⬜ |
| AC8 | 04 | Production Order → Cancel | ⬜ |
| AC9 | 04 | Production Order → Operations | ⬜ |
| AC10 | 04 | Production Order → Complete | ⬜ |
| AC11 | 04 | Production Order | ⬜ |
| BM5.1 | 10 | Lampirkan berkas pada Production Order, Production Log, Hauling, Royal | ⬜ |

## Sesi C07 — Pertambangan (Tambang Pasir Percontohan)

- **Halaman:** Mining → Production Logs, Haulings, Royalty Rates, Royalties, Survey Reconciliations
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B15
- **Rujukan berkas 01–03:** —

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AD3 | 04 | Mining → Production Logs | ⬜ |
| AD4 | 04 | Production Logs → Verify | ⬜ |
| AD5 | 04 | Mining → Haulings | ⬜ |
| AD6 | 04 | Haulings | ⬜ |
| AD7 | 04 | Haulings | ⬜ |
| AD8 | 04 | Mining → Royalty Rates | ⬜ |
| AD9 | 04 | Mining → Royalties | ⬜ |
| AD10 | 04 | Royalties | ⬜ |
| AD11 | 04 | Royalties | ⬜ |
| AD12 | 04 | Production Logs | ⬜ |
| AD13 | 04 | Mining → Survey Reconciliations | ⬜ |

## Sesi C08 — Rental

- **Halaman:** Rental → Assets, Quotations, Orders, Invoices, Payment Bills, Returns, Usage Entries
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** B12
- **Rujukan berkas 01–03:** `03` Tahap G

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AF3 | 04 | Rental → Assets | ⬜ |
| AF4 | 04 | Rental → Orders | ⬜ |
| AF5 | 04 | Rental → Orders → Complete | ⬜ |
| AF6 | 04 | Rental → Returns | ⬜ |

## Sesi C09 — SDM: rekrutmen, absensi, perubahan status, payroll

- **Halaman:** HRM → Job Vacancies, Applications, Interviews, Offers, Attendances, Recaps, Device Logs, Status Changes, Payroll Periods, Payslips, Commissions, Activity Logs; Data Subject Requests
- **Akun:** Admin dan HR
- **Prasyarat:** B08, B14, C03
- **Rujukan berkas 01–03:** `02` Tahap F (F.1–F.2); `03` Tahap L dan Tahap Q (bagian HRM)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AE4 | 04 | HRM → Attendance Device Logs | ⬜ |
| AE5 | 04 | HRM → Attendance Recaps | ⬜ |
| AE6 | 04 | HRM → Employee Status Changes | ⬜ |
| AE7 | 04 | HRM → Job Vacancies → Job Interviews | ⬜ |
| AE8 | 04 | HRM → Job Offers | ⬜ |
| AE11 | 04 | HRM → Employee Activity Logs (lanjut Y13) | ⬜ |
| Y11 | 04 | Client Master → Data Subject Requests | ⬜ |
| AV1 | 06 | Karyawan baru | ⬜ |
| AV2 | 06 | Pindah posisi | ⬜ |
| AV3 | 06 | Tidak masuk | ⬜ |
| AV4 | 06 | Lembur | ⬜ |
| AV5 | 06 | Banyak pola kerja | ⬜ |
| AV6 | 06 | Transfer departemen | ⬜ |
| AV7 | 06 | Dipindah sementara | ⬜ |
| AV8 | 06 | Keterlambatan | ⬜ |
| AV9 | 06 | Remote | ⬜ |
| AV10 | 06 | Cuti | ⬜ |
| AV11 | 06 | Atasan cuti | ⬜ |
| AV12 | 06 | Resign | ⬜ |
| AV13 | 06 | Pindah di tengah bulan | ⬜ |
| AV14 | 06 | Dua jenis jadwal | ⬜ |
| AV15 | 06 | Salah catat kehadiran | ⬜ |
| AV16 | 06 | Bekerja di hari libur | ⬜ |
| AV17 | 06 | Lembur tidak disetujui | ⬜ |
| AV18 | 06 | Pinjaman karyawan | ⬜ |
| AV19 | 06 | Penggantian biaya | ⬜ |
| AV20 | 06 | Karyawan lintas outlet | ⬜ |
| AV21 | 06 | Atasan berbeda per unit | ⬜ |
| AV22 | 06 | Payroll bulanan | ⬜ |
| AV23 | 06 | Komisi sales | ⬜ |
| AV24 | 06 | "Apakah saya sebagai HR bisa menjawab?" | ⬜ |
| BC8 | 08 | Komisi persentase (fee dokter persen) | ⬜ |
| BH14 | 09 | Absensi ganda untuk karyawan dan tanggal yang sama | ⬜ |
| BH15 | 09 | Cuti melebihi saldo cuti | ⬜ |
| BH16 | 09 | Cuti dengan tanggal selesai sebelum mulai | ⬜ |
| BH17 | 09 | Tandai payroll dibayar sebelum disetujui | ⬜ |
| BH18 | 09 | Generate payroll dua kali untuk periode yang sama | ⬜ |
| BH19 | 09 | Komisi untuk karyawan di posisi non-sales | ⬜ |
| BH20 | 09 | Karyawan tanpa NPWP atau data pajak lengkap masuk payroll | ⬜ |
| BH21 | 09 | Ubah absensi yang sudah terkunci payroll | ⬜ |
| BH23 | 09 | Jenis cuti baru: toggle berbayar/persetujuan/aktif saat Create | ⬜ |
| BK2.3 | 10 | Kriteria KPI bersekor | ⬜ |
| BL1.1 | 10 | Buka lowongan "Staf Pendampingan Pelanggan" (Job Vacancy), lalu Genera | ⬜ |
| BL1.2 | 10 | Buka tautan di jendela tanpa login; isi dan kirim formulir dua pelamar | ⬜ |
| BL1.3 | 10 | Buka tautan yang sudah kedaluwarsa (ubah masa berlaku) | ⬜ |
| BL1.4 | 10 | Detail pelamar | ⬜ |
| BL1.5 | 10 | Hrm → Job Interviews | ⬜ |
| BL1.6 | 10 | Job Offers | ⬜ |
| BL1.7 | 10 | Penawaran diterima | ⬜ |
| BL1.8 | 10 | Lompat status | ⬜ |
| BL2.1 | 10 | Setelah BK3.5, tunggu proses malam atau jalankan perintahnya | ⬜ |
| BL2.2 | 10 | Karyawan Check in dari dashboard karyawan | ⬜ |
| BL2.3 | 10 | Check in dari luar area | ⬜ |
| BL2.4 | 10 | Check in pada hari Terjadwal | ⬜ |
| BL2.5 | 10 | Hari Terjadwal yang lewat jam akhir shift tanpa check in | ⬜ |
| BL2.6 | 10 | Daftar absensi | ⬜ |
| BL2.7 | 10 | Absensi yang periode payroll-nya sudah diproses | ⬜ |
| BL2.8 | 10 | Mesin Absensi: daftarkan mesin, lihat token, endpoint, pemetaan field | ⬜ |
| BL2.9 | 10 | Punch dari mesin untuk karyawan yang ID Mesinnya belum diisi | ⬜ |
| BL2.10 | 10 | Rekap Absensi | ⬜ |
| BL2.11 | 10 | Detail rekap satu karyawan | ⬜ |
| BL2.12 | 10 | Dashboard HRM | ⬜ |
| BL4.1 | 10 | Karyawan baru diberi jenis Masa Percobaan dengan tanggal akhir kontrak | ⬜ |
| BL4.2 | 10 | Detail karyawan → Change Employment Status: ke Tetap, isi alasan, gaji | ⬜ |
| BL4.3 | 10 | Setujui | ⬜ |
| BL4.4 | 10 | Tolak dan batalkan | ⬜ |
| BL4.5 | 10 | Widget kontrak | ⬜ |
| BL5.1 | 10 | Buat periode payroll dengan cut-off 25 | ⬜ |
| BL5.2 | 10 | Generate Payslip | ⬜ |
| BL5.9 | 10 | Payroll September dibandingkan jurnal | ⬜ |
| BM4.1 | 10 | Data Subject Requests: cari karyawan, Ekspor | ⬜ |
| BM4.2 | 10 | Ekspor member (kontak pelanggan) | ⬜ |
| BM4.3 | 10 | Anonimkan satu karyawan uji yang sudah tidak aktif | ⬜ |
| BM4.4 | 10 | Dokumen lama | ⬜ |
| BM4.5 | 10 | Riwayat permintaan | ⬜ |

---

# FASE D — Akuntansi, Laporan, dan Penutupan (setelah semua transaksi)


## Sesi D01 — Valuasi persediaan (laporan dan jurnal)

- **Halaman:** Inventory → Valuation (Retail Method, Close Purchase Variance); Inventory → Config
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** Fase C selesai
- **Rujukan berkas 01–03:** Nyalakan "Retail method result = boleh dijurnal" dan pemetaan akun penutup di Inventory Config sebelum menekan Post (bagian AA11)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AA6 | 04 | Inventory → Valuation → Close Purchase Variance | ⬜ |
| AA10 | 04 | Inventory → Valuation → Retail Method | ⬜ |
| AA11 | 04 | Inventory → Config → "Retail method result" | ⬜ |

## Sesi D02 — Jurnal manual dan kasus mata uang asing

- **Halaman:** Accounting → Journals; Client Master → Exchange Rates
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** D01
- **Rujukan berkas 01–03:** `03` Tahap I (bagian jurnal manual); Buat transaksi baku `JT-01` sampai `JT-18` di sini

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AI1 | 05 | Jurnal seimbang sederhana | ⬜ |
| AI2 | 05 | Jurnal tidak seimbang | ⬜ |
| AI3 | 05 | Kurang dari dua baris | ⬜ |
| AI4 | 05 | Akun atau kegiatan tidak ada | ⬜ |
| AI5 | 05 | Tiga baris dengan akun pajak | ⬜ |
| AI6 | 05 | Pemisahan kegiatan | ⬜ |
| AI7 | 05 | Jurnal beberapa kegiatan dalam satu transaksi | ⬜ |
| AI8 | 05 | Buat seluruh transaksi baku | ⬜ |
| AI9 | 05 | Alokasi biaya bersama | ⬜ |
| AI10 | 05 | Mode tanpa approval jurnal | ⬜ |
| AI11 | 05 | Mode dengan approval jurnal | ⬜ |
| AI12 | 05 | Approval berjenjang | ⬜ |
| AI13 | 05 | Bypass approval via API | ⬜ |
| AI14 | 05 | Tolak approval | ⬜ |
| AI15 | 05 | Post ganda | ⬜ |
| AI17 | 05 | Post-bulk | ⬜ |
| AI18 | 05 | Reverse dasar | ⬜ |
| AI19 | 05 | Reverse draft | ⬜ |
| AI20 | 05 | Reverse ganda | ⬜ |
| AI21 | 05 | Reverse dari reverse | ⬜ |
| AI22 | 05 | Recreate Journal | ⬜ |
| AI23 | 05 | Create Bulk dan Edit Bulk | ⬜ |
| AI24 | 05 | Hapus draft | ⬜ |
| AI25 | 05 | Pendapatan diterima dimuka tahunan | ⬜ |
| AI26 | 05 | Paket voucher prabayar (korporat) | ⬜ |
| AI27 | 05 | Termin pendampingan implementasi | ⬜ |
| AI28 | 05 | Retensi pelanggan (analog retensi konstruksi) | ⬜ |
| AI29 | 05 | Selisih kas kasir | ⬜ |
| AI30 | 05 | Selisih kas lebih | ⬜ |
| AI31 | 05 | Refund pelanggan atas sewa | ⬜ |
| AI32 | 05 | Biaya payment gateway | ⬜ |
| AI33 | 05 | Pelunasan dengan potongan PPh 23 | ⬜ |
| AI34 | 05 | Pinjaman dan cicilan | ⬜ |
| AI35 | 05 | Pajak daerah restoran | ⬜ |
| AI36 | 05 | Beban dengan mata uang asing (langganan cloud USD) | ⬜ |
| AI37 | 05 | Jurnal bertanggal masa depan | ⬜ |
| AI38 | 05 | Jurnal ke tanggal tanpa periode | ⬜ |
| AI39 | 05 | Netralisasi | ⬜ |
| BC6 | 08 | Selisih kurs realisasi | ⬜ |
| BC7 | 08 | Dana titipan tidak boleh dipakai operasional | ⬜ |
| BC10 | 08 | Opname kas kecil akhir bulan | ⬜ |
| BC11 | 08 | Koreksi dengan Reverse dan Recreate | ⬜ |
| BC12 | 08 | Pelunasan piutang awal | ⬜ |
| BI1 | 09 | Pelunasan/pengakuan yang melebihi saldo kewajiban: amortisasi Pendapat | ⬜ |
| BI2 | 09 | Write-off piutang melebihi sisa piutang `1-120` | ⬜ |
| BI3 | 09 | Redemption voucher melebihi saldo voucher | ⬜ |
| BI4 | 09 | Bayar komisi melebihi saldo akrual (akrual 1.285.000, bayar 2.000.000) | ⬜ |
| BI5 | 09 | Pendapatan restoran tanpa memisahkan PB1 | ⬜ |
| BI6 | 09 | Jurnal tanpa akun berflag pajak | ⬜ |
| BI7 | 09 | Memakai rekening deposit/penampung untuk beban operasional | ⬜ |
| BI8 | 09 | Dua akun berflag Laba Ditahan atau Ekuitas Saldo Awal | ⬜ |
| BJ1 | 09 | Utang valas | ⬜ |
| BJ2 | 09 | Posting dan GL | ⬜ |
| BJ3 | 09 | Aktifkan kurs baru | ⬜ |
| BJ4 | 09 | Jebakan pelunasan naif | ⬜ |
| BJ5 | 09 | Pelunasan benar (3 baris) | ⬜ |
| BJ6 | 09 | Untung kurs | ⬜ |
| BJ7 | 09 | Mata uang tanpa kurs aktif | ⬜ |
| BJ12 | 09 | Reverse jurnal valas | ⬜ |
| BJ13 | 09 | Revaluasi akhir bulan | ⬜ |

## Sesi D03 — Aset tetap dan penyusutan

- **Halaman:** Fixed Assets → Assets, Disposals
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** D02
- **Rujukan berkas 01–03:** `03` Tahap H

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AN1 | 05 | Registrasi tiga aset | ⬜ |
| AN2 | 05 | Masa manfaat tidak valid | ⬜ |
| AN3 | 05 | Hubungkan akun lewat Edit | ⬜ |
| AN4 | 05 | Penyusutan garis lurus | ⬜ |
| AN5 | 05 | Penyusutan saldo menurun | ⬜ |
| AN6 | 05 | Penyusutan ganda | ⬜ |
| AN7 | 05 | Nilai buku tidak di bawah residu | ⬜ |
| AN11 | 05 | Pelepasan aset (jual) | ⬜ |
| AN12 | 05 | Pelepasan karena rusak | ⬜ |
| AN13 | 05 | Hapus aset berriwayat | ⬜ |
| AN14 | 05 | Aset yang sudah dilepas | ⬜ |

## Sesi D04 — Rekonsiliasi bank

- **Halaman:** Finance → Bank Reconciliations
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** D02, D03
- **Rujukan berkas 01–03:** `03` Tahap N (bagian Bank Reconciliations)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AO2 | 05 | Cocok sempurna | ⬜ |
| AO3 | 05 | Biaya admin bank belum dicatat | ⬜ |
| AO4 | 05 | Setoran dalam perjalanan | ⬜ |
| AO5 | 05 | Transfer keluar belum cair | ⬜ |
| AO6 | 05 | Kesalahan input nominal | ⬜ |
| AO7 | 05 | Complete saat masih selisih | ⬜ |
| AO8 | 05 | Guard setelah selesai | ⬜ |
| AO9 | 05 | Multi rekening | ⬜ |
| AO10 | 05 | Penyelesaian payment gateway | ⬜ |
| AO11 | 05 | Setoran kasir dengan selisih | ⬜ |
| BI21 | 09 | Dua rekening bank untuk satu jurnal | ⬜ |
| BJ11 | 09 | Rekonsiliasi bank USD | ⬜ |

## Sesi D05 — Anggaran

- **Halaman:** Accounting → Budgets
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** D02
- **Rujukan berkas 01–03:** `03` Tahap I (bagian Budgets)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AM1 | 05 | Buat anggaran | ⬜ |
| AM2 | 05 | Fiscal year kosong | ⬜ |
| AM3 | 05 | Baris kembar | ⬜ |
| AM4 | 05 | Jumlah negatif | ⬜ |
| AM5 | 05 | Periode tahun tertutup | ⬜ |
| AM6 | 05 | Realisasi untuk uji | ⬜ |
| AM7 | 05 | Budget vs Actual | ⬜ |
| AM8 | 05 | Pemisahan per kegiatan | ⬜ |
| AM9 | 05 | Status | ⬜ |
| AM10 | 05 | Pembagian tahunan tidak habis dibagi 12 | ⬜ |
| AM11 | 05 | Hapus anggaran | ⬜ |

## Sesi D06 — Buku besar dan neraca saldo

- **Halaman:** Accounting → General Ledger; Reports → Trial Balance
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** D02, D03, D04
- **Rujukan berkas 01–03:** `03` Tahap I (bagian General Ledger)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AJ1 | 05 | Detail ledger Bank Operasional | ⬜ |
| AJ2 | 05 | Summary by Account | ⬜ |
| AJ3 | 05 | Neraca Saldo (Trial Balance) | ⬜ |
| AJ4 | 05 | Dua endpoint neraca saldo | ⬜ |
| AJ5 | 05 | Filter kegiatan SEWA | ⬜ |
| AJ6 | 05 | Filter kegiatan RETAIL | ⬜ |
| AJ7 | 05 | Filter kegiatan RESTO | ⬜ |
| AJ8 | 05 | Konsolidasi = jumlah kegiatan | ⬜ |
| AJ9 | 05 | Persediaan tanpa dimensi | ⬜ |
| AJ10 | 05 | Biaya bersama tanpa kegiatan | ⬜ |
| AJ11 | 05 | Transfer antar kegiatan | ⬜ |
| AJ12 | 05 | Reverse tercermin di GL | ⬜ |
| AJ13 | 05 | Ekspor | ⬜ |
| BI9 | 09 | Akun kontra-aset (Akumulasi Penyusutan `1-209`) | ⬜ |
| BI10 | 09 | Akun kontra-pendapatan (diskon, retur) | ⬜ |
| BI11 | 09 | Arus kas tidak dobel | ⬜ |
| BI12 | 09 | Jumlah dimensi = konsolidasi | ⬜ |
| BI13 | 09 | Baris tanpa kegiatan tidak hilang | ⬜ |
| BI14 | 09 | Aktual anggaran bertanda benar | ⬜ |
| BI15 | 09 | Presisi angka besar | ⬜ |
| BI16 | 09 | Dua trial balance identik | ⬜ |
| BI17 | 09 | Akun dengan banyak baris | ⬜ |
| BI18 | 09 | `as_of_date` sebelum transaksi | ⬜ |
| BI22 | 09 | Jurnal 5 baris vs dua jurnal | ⬜ |
| BI23 | 09 | Dimensi tidak merata | ⬜ |
| BI24 | 09 | Margin sangat tinggi bulan ini | ⬜ |
| BJ10 | 09 | Neraca Saldo dan Neraca tetap IDR | ⬜ |

## Sesi D07 — Laporan pajak

- **Halaman:** Reports → Tax Summary
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** D06
- **Rujukan berkas 01–03:** —

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AP1 | 05 | Rekap PPN minimal | ⬜ |
| AP2 | 05 | Rekap PPN lengkap | ⬜ |
| AP3 | 05 | Klasifikasi otomatis | ⬜ |
| AP4 | 05 | Retur mengurangi | ⬜ |
| AP5 | 05 | Periode tanpa transaksi | ⬜ |
| AP6 | 05 | Setor PPN | ⬜ |
| AP7 | 05 | Setor PB1 dan PPh 21 | ⬜ |
| AP8 | 05 | Uang muka PPh 23 | ⬜ |
| AP9 | 05 | Pajak pada dokumen operasional | ⬜ |

## Sesi D08 — Laporan keuangan

- **Halaman:** Reports → Balance Sheet, Income Statement, Cash Flow Statement, Landed Cost, Logistics Payables
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** D06, D07
- **Rujukan berkas 01–03:** `03` Tahap I (bagian laporan keuangan)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AB13 | 04 | Reports → Landed Cost dan Logistics Payables | ⬜ |
| AL1 | 05 | Laba Rugi konsolidasi | ⬜ |
| AL2 | 05 | Laba Rugi per kegiatan | ⬜ |
| AL3 | 05 | Neraca | ⬜ |
| AL4 | 05 | Neraca setelah tutup tahun uji | ⬜ |
| AL5 | 05 | Arus Kas | ⬜ |
| AL6 | 05 | Neraca Saldo historis | ⬜ |
| AL7 | 05 | Uji kewajaran | ⬜ |
| AL8 | 05 | Konsistensi antar laporan | ⬜ |
| AL9 | 05 | Ekspor | ⬜ |
| AN8 | 05 | Verifikasi neraca | ⬜ |
| AN9 | 05 | Laba rugi | ⬜ |

## Sesi D09 — Periode dan tahun buku (paling akhir, bersifat mengunci)

- **Halaman:** Client Master → Accounting Period, Fiscal Year (gunakan `FY-TEST` untuk uji destruktif)
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** D08
- **Rujukan berkas 01–03:** Kerjakan terakhir di bidang akuntansi: penutupan mengunci posting

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AF10 | 04 | Accounting → Fiscal Year | ⬜ |
| AI16 | 05 | Post ke periode tertutup | ⬜ |
| AK1 | 05 | Tutup periode dengan jurnal draft | ⬜ |
| AK2 | 05 | Tutup periode sukses | ⬜ |
| AK3 | 05 | Guard periode berikutnya wajib ada dan terbuka | ⬜ |
| AK4 | 05 | Tutup periode yang menaungi hari ini | ⬜ |
| AK5 | 05 | Kunci periode | ⬜ |
| AK6 | 05 | Reverse jurnal pada periode tertutup | ⬜ |
| AK7 | 05 | Buka kembali periode | ⬜ |
| AK8 | 05 | Periode tumpang tindih | ⬜ |
| AK9 | 05 | Celah periode | ⬜ |
| AK10 | 05 | Aksi massal campuran | ⬜ |
| AK11 | 05 | Penyusutan terlambat setelah periode tertutup | ⬜ |
| AK12 | 05 | Dashboard periode | ⬜ |
| AK13 | 05 | Tutup tahun: periode belum semua tertutup | ⬜ |
| AK14 | 05 | Tutup tahun: tidak ada akun Laba Ditahan | ⬜ |
| AK15 | 05 | Tutup tahun: lebih dari satu akun Laba Ditahan | ⬜ |
| AK16 | 05 | Tutup tahun sukses (FY-TEST dengan data) | ⬜ |
| AK17 | 05 | Tutup tahun dua kali | ⬜ |
| AK18 | 05 | Buka kembali tahun buku | ⬜ |
| AK19 | 05 | Pembukaan tahun berikutnya | ⬜ |
| AK20 | 05 | Dua tahun buku berjalan (pola retail tahun berjalan) | ⬜ |
| AN10 | 05 | Penyusutan terlambat | ⬜ |
| BC4 | 08 | Periode mingguan dan kuartalan | ⬜ |
| BC5 | 08 | Saldo awal tengah tahun dan lintas tahun | ⬜ |
| BI19 | 09 | Tutup periode sebelum akhir periode | ⬜ |
| BI20 | 09 | Lock sebelum Close, Lock dua kali, Close dua kali, Reopen periode terb | ⬜ |

## Sesi D10 — Akuntansi terpusat (cabang uji)

- **Halaman:** Client Master → Branch Manage
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** D09
- **Rujukan berkas 01–03:** —

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AF7 | 04 | Client Master → Branch Manage | ⬜ |
| AF8 | 04 | Cabang uji | ⬜ |
| AF9 | 04 | Cabang uji | ⬜ |

---

# FASE E — Lintas Modul, Peran, dan Penutup


## Sesi E01 — Siklus penuh, kasus keuangan, dan uji prinsip

- **Halaman:** Lintas halaman (Laporan, kartu pelanggan/pemasok/karyawan, Stock History)
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** Fase D selesai
- **Rujukan berkas 01–03:** `07` Tahap AW (AW-1 sampai AW-6, tabel tanpa nomor)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AG1 | 04 | Pembelian → Persediaan → Penjualan → HPP. Beli 100 pcs @ 5.000 (PO → G | ⬜ |
| AG2 | 04 | Kasir → Tutup sesi → Setoran → Kas. Lakukan 5 transaksi tunai dan 2 no | ⬜ |
| AG3 | 04 | Restoran → Resep → Stok → HPP. Pesanan 10 porsi menu beresep (Y4), bay | ⬜ |
| AG4 | 04 | Manufaktur → Persediaan → Penjualan. Jual 20 porsi Paket Nasi Kotak (A | ⬜ |
| AG5 | 04 | Valuasi → Laporan. Setelah AA4–AA11, buka Neraca, Buku Besar Persediaa | ⬜ |
| AG6 | 04 | Tambang → Royalti → Kas. Setelah AD9–AD10, buka Buku Besar akun Beban  | ⬜ |
| AG7 | 04 | Sewa banyak unit → Faktur → Bayar. Order AF4 → Rental Invoice → Paymen | ⬜ |
| AX1 | 07 | Pembelian dengan selisih | ⬜ |
| AX2 | 07 | Pembelian dengan diskon | ⬜ |
| AX3 | 07 | Retur pembelian | ⬜ |
| AX4 | 07 | Uang muka pemasok | ⬜ |
| AX5 | 07 | Penjualan tunai | ⬜ |
| AX6 | 07 | Penjualan POS dan restoran | ⬜ |
| AX7 | 07 | Pemborosan dapur | ⬜ |
| AX8 | 07 | Pinjaman karyawan | ⬜ |
| AX9 | 07 | Penggantian biaya karyawan | ⬜ |
| AX10 | 07 | Beban operasional | ⬜ |
| AX11 | 07 | Beban dibayar dimuka | ⬜ |
| AX12 | 07 | Akrual | ⬜ |
| AX13 | 07 | Kredit pelanggan | ⬜ |
| AX14 | 07 | Kredit pemasok | ⬜ |
| AX15 | 07 | Pembayaran sebagian | ⬜ |
| AX16 | 07 | Satu pembayaran beberapa faktur | ⬜ |
| AX17 | 07 | Pembayaran terlambat | ⬜ |
| AX18 | 07 | Pelanggan menunggak | ⬜ |
| AX19 | 07 | Pemasok jatuh tempo | ⬜ |
| AX20 | 07 | Manajemen kas | ⬜ |
| AX21 | 07 | Selisih kas | ⬜ |
| AX22 | 07 | Pajak | ⬜ |
| AY1 | 07 | Jurnal penyesuaian | ⬜ |
| AY2 | 07 | Tutup periode | ⬜ |
| AY3 | 07 | Mundur tanggal | ⬜ |
| AY4 | 07 | Banyak titik jual | ⬜ |
| AY5 | 07 | Pusat biaya | ⬜ |
| AY6 | 07 | Proyek pendampingan | ⬜ |
| AY7 | 07 | Pembelian ke proyek | ⬜ |
| AY8 | 07 | Penjualan ke proyek | ⬜ |
| AY9 | 07 | Profitabilitas | ⬜ |
| AZ1 | 07 | Total penjualan hari itu | ⬜ |
| AZ2 | 07 | Kas | ⬜ |
| AZ3 | 07 | Stok | ⬜ |
| AZ4 | 07 | Piutang dan utang | ⬜ |
| AZ5 | 07 | Pajak | ⬜ |
| AZ6 | 07 | Absensi | ⬜ |
| AZ7 | 07 | Neraca saldo | ⬜ |
| AZ8 | 07 | Bisnis penuh | ⬜ |
| AZ9 | 07 | Pelanggan penuh | ⬜ |
| AZ10 | 07 | Pemasok penuh | ⬜ |
| AZ11 | 07 | Karyawan penuh | ⬜ |
| AZ12 | 07 | Restoran penuh | ⬜ |
| AZ13 | 07 | Persediaan penuh | ⬜ |
| AZ14 | 07 | Rekonsiliasi akuntansi | ⬜ |
| BA1 | 07 | "Mengapa" | ⬜ |
| BA2 | 07 | "Mundur" (Reverse) | ⬜ |
| BA3 | 07 | "Satu transaksi" | ⬜ |
| BA4 | 07 | "Satu rupiah" | ⬜ |
| BA5 | 07 | "Satu barang" | ⬜ |
| BA6 | 07 | "Satu pelanggan" | ⬜ |
| BA7 | 07 | "Satu pemasok" | ⬜ |
| BA8 | 07 | "Satu karyawan" | ⬜ |
| BA9 | 07 | Tidak ada data hilang | ⬜ |
| BA10 | 07 | Tidak ada uang muncul dari ketiadaan | ⬜ |
| BA11 | 07 | Tidak ada uang hilang | ⬜ |
| BA12 | 07 | Tidak ada stok muncul | ⬜ |
| BA13 | 07 | Tidak ada stok hilang | ⬜ |
| BA14 | 07 | "Akuntansi adalah hakim" | ⬜ |
| BO1 | 10 | Karyawan dari rekrutmen sampai gaji | ⬜ |
| BO2 | 10 | Perubahan status memengaruhi payroll | ⬜ |
| BO3 | 10 | Pajak per item sampai laporan pajak | ⬜ |
| BO4 | 10 | Landed cost vendor logistik | ⬜ |
| BO7 | 10 | Anonimisasi tidak merusak laporan | ⬜ |

## Sesi E02 — Uji peran dan hak akses (satu kali login per akun)

- **Halaman:** Login bergantian: Karyawan biasa → Kasir → Staf Gudang → HR → Manajer → Direktur; Approvals → Approval Requests
- **Akun:** Banyak akun (profil browser terpisah)
- **Prasyarat:** E01
- **Rujukan berkas 01–03:** `03` Tahap M (approval sungguhan); Urutkan sesuai akun: semua langkah satu akun dikerjakan sekaligus

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AE9 | 04 | HRM → My Leave Requests, My Attendance Adjustments, My Payslips | ⬜ |
| AE10 | 04 | HRM → Payslips | ⬜ |
| AG8 | 04 | Persetujuan lintas dokumen. Aktifkan persetujuan untuk PO, Production  | ⬜ |
| AG9 | 04 | Akses antar peran. Login sebagai Kasir, Staf Gudang, Staf Akunting, HR | ⬜ |
| BB1 | 07 | Pemilik (Arman Halim) | ⬜ |
| BB2 | 07 | Keuangan (Sofyan Nugroho) | ⬜ |
| BB3 | 07 | Auditor | ⬜ |
| BH22 | 09 | Karyawan biasa membuka halaman data gaji karyawan lain | ⬜ |
| BL3.1 | 10 | Karyawan biasa membuka Cuti Saya | ⬜ |
| BL3.2 | 10 | Ajukan cuti dari Cuti Saya | ⬜ |
| BL3.3 | 10 | Batalkan pengajuan yang belum diputuskan | ⬜ |
| BL3.4 | 10 | Ajukan cuti setengah hari | ⬜ |
| BL3.5 | 10 | HRD mengajukan cuti untuk karyawan lain dengan opsi Setujui langsung a | ⬜ |
| BL3.6 | 10 | Persetujuan satu departemen | ⬜ |
| BL3.7 | 10 | Pembanding departemen | ⬜ |
| BL3.8 | 10 | Karyawan atau atasan tanpa departemen | ⬜ |
| BL3.9 | 10 | Detail pengajuan | ⬜ |
| BL3.10 | 10 | Saldo Cuti | ⬜ |
| BL5.3 | 10 | Karyawan membuka Slip Gaji Saya dan Koreksi Absensi Saya | ⬜ |
| BL5.4 | 10 | Pengguna tanpa izin view-confidential membuka daftar karyawan dan opsi | ⬜ |
| BL5.5 | 10 | Pengguna tanpa izin membuka struktur gaji, komponen gaji karyawan, sli | ⬜ |
| BL5.6 | 10 | Urut atau cari berdasarkan kolom rahasia | ⬜ |
| BL5.7 | 10 | Edit karyawan oleh pengguna tanpa hak | ⬜ |
| BL5.8 | 10 | Matikan saklar kerahasiaan di HRM Configs | ⬜ |
| BO5 | 10 | Kerahasiaan lintas modul | ⬜ |

## Sesi E03 — Akun, keamanan, privasi, paket, dan langganan

- **Halaman:** Settings → Account, Appearance, Security, Subscription; widget AI; Help; Changelog
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** E02
- **Rujukan berkas 01–03:** —

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AF11 | 04 | Settings → Security | ⬜ |
| AF12 | 04 | Settings → Security → PIN Override | ⬜ |
| AF13 | 04 | Settings → Appearance dan ikon tema di sidebar | ⬜ |
| AF14 | 04 | Settings → Subscription | ⬜ |
| AF15 | 04 | Help dan Changelog | ⬜ |
| BN1 | 10 | Pengungkapan AI | ⬜ |
| BN2 | 10 | Versi pengungkapan | ⬜ |
| BN3 | 10 | Autentikasi dua langkah | ⬜ |
| BN4 | 10 | Pembatasan percobaan login | ⬜ |
| BN5 | 10 | Batas paket | ⬜ |
| BN6 | 10 | Modul mengikuti paket | ⬜ |
| BN7 | 10 | Bahasa terkunci paket | ⬜ |
| BN8 | 10 | Halaman Subscription | ⬜ |
| BN9 | 10 | Ajukan ganti paket | ⬜ |
| BN10 | 10 | Penangguhan | ⬜ |
| BN11 | 10 | Masa tenggang | ⬜ |
| BO8 | 10 | Paket berbatas dan semua pembuatan data | ⬜ |

## Sesi E04 — Sapuan akhir: dashboard, bahasa, ekspor, hapus, muat ulang, log

- **Halaman:** Dashboard (semua modul); lintas halaman; Branch Logs; Branch Translations
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** E03
- **Rujukan berkas 01–03:** `03` Tahap T–X (hanya bagian yang terlihat klien)

| Butir | Berkas | Ringkas | OK |
| --- | --- | --- | --- |
| AC12 | 04 | Dashboard → Manufacturing | ⬜ |
| AD14 | 04 | Dashboard → Mining | ⬜ |
| AG10 | 04 | Terjemahan. Ganti bahasa ke Inggris lalu Indonesia pada tiga halaman d | ⬜ |
| AG11 | 04 | Ekspor. Ekspor Excel dan PDF dari lima halaman daftar dan lima laporan | ⬜ |
| AG12 | 04 | Muat ulang dan konsistensi. Pada setiap halaman daftar yang disentuh d | ⬜ |
| AG13 | 04 | Hapus dan batalkan. Coba menghapus data master yang sudah dipakai tran | ⬜ |
| Y15 | 04 | Client Master → Branch Translations dan Branch Logs | ⬜ |
| BD14 | 09 | Hapus master data yang sudah dipakai transaksi (kategori, satuan, pela | ⬜ |
| BM2.1 | 10 | Unduh PDF: Quotation, SO, PO, PI, RFQ, Charge Invoice, Slip Gaji | ⬜ |
| BM2.2 | 10 | Ganti bahasa pengguna lalu unduh PDF | ⬜ |
| BM2.3 | 10 | Ekspor Excel dari lima laporan | ⬜ |
| BM2.4 | 10 | Dokumen dengan logo besar dan kop terpisah | ⬜ |
| BM5.2 | 10 | Ikon ? di navbar pada halaman index, create, edit, dan detail dari 10  | ⬜ |
| BO6 | 10 | Format tanggal di seluruh pohon menu | ⬜ |

## Sesi E05 — Uji ulang temuan yang sudah diperbaiki

- **Halaman:** Sesuai tiap temuan
- **Akun:** Admin (akun pemilik cabang)
- **Prasyarat:** E04
- **Rujukan berkas 01–03:** Berkas `11` (83 temuan)

_Tidak ada butir bernomor; ikuti rujukan di atas._

---

# Lampiran — Pemeriksaan Kelengkapan

- Jumlah butir bernomor di berkas 04–10: **785**, semuanya ditempatkan tepat satu kali di sesi di atas (diperiksa otomatis saat berkas ini disusun).
- Jumlah sesi: **41** (Fase B 17, Fase C 9, Fase D 10, Fase E 5).
- Berkas 11 (83 temuan) dikerjakan di Sesi E05; berkas 08 (peta) dipakai sebagai rujukan, bukan daftar kerja.

## Bila ada butir baru

Tambahkan butir ke berkas sumbernya, lalu masukkan nomornya ke sesi halaman yang sama di berkas ini (jangan membuat sesi baru kecuali halamannya belum pernah disebut).

