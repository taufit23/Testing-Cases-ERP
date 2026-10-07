---
title: Ranahku — Fitur Baru Sejak 15 September 2026 (Disusun Mengikuti Urutan Kerja)
description: Pengujian fitur yang lahir sesudah berkas 00–03 ditulis (rekrutmen, absensi siklus dan geofence, cuti mandiri dan setengah hari, perubahan status karyawan, cut-off payroll, kerahasiaan data karyawan, format tanggal, impor massal, pajak per item PO, Document Export Settings, mesin kasir, pengungkapan AI dan permintaan data pribadi, batas paket, langganan). Setiap blok diberi titik sisip pada urutan kerja Ranahku supaya data dan prasyaratnya tetap berurutan.
---

# Ranahku — Fitur Baru Sejak 15 September 2026

> Disusun 2026-10-07 dari 162 entri changelog sejak 2026-09-15. Fitur lama sudah ada di berkas 04–09 (valuasi, Manufaktur, Pertambangan, akuntansi terpusat,
> kasir lanjutan, dll.). Berkas ini menambah **fitur yang belum punya langkah uji** dan menjaga **urutan kerja**: master data dan pengaturan dulu, baru transaksi,
> baru modul lanjutan dan lintas modul. Tiap fitur ditulis sebagai bagian dari urutan itu, bukan sebagai daftar terpisah.

## 0. Urutan Kerja Gabungan (patokan seluruh penguji)

| Urutan | Berkas dan tahap | Isi |
| --- | --- | --- |
| 1 | `00` | Baca profil perusahaan (tidak ada langkah input) |
| 2 | `01` Tahap 1–12 | Master data dan konfigurasi jurnal. **Sisipkan blok BK di titik yang tertulis di bawah** |
| 3 | `02` Tahap A–F | Transaksi inti. **Sisipkan blok BL dan BM setelah Tahap F** |
| 4 | `03` Tahap G–X | Modul lanjutan |
| 5 | `04` Tahap Y–AH | Halaman yang belum tersentuh dan fitur baru tahap pertama |
| 6 | `05` Tahap AI–AP | Akuntansi mendalam |
| 7 | `06` Tahap AQ–AV | Kasus bisnis per modul |
| 8 | `07` Tahap AW–BB | Siklus penuh dan uji prinsip |
| 9 | `08` | Peta suite sumber dan skenario analog |
| 10 | `09` Tahap BD–BJ | Validasi, penjaga, kasus batas |
| 11 | `10` Tahap BK–BO (berkas ini) | Fitur baru sejak 15 September, sesuai titik sisip |
| 12 | `11` | Uji ulang temuan yang sudah selesai diperbaiki |

### Titik sisip blok berkas ini ke urutan 01–03

| Blok | Isi | Kerjakan setelah | Sebelum |
| --- | --- | --- | --- |
| BK1 | Format tanggal | `01` Tahap 1 (Struktur Dasar) | Tahap 2 |
| BK2 | Impor Excel dan aksi massal master data | `01` Tahap 5, 6, 9 (saat membuat banyak data) | Tahap 10 |
| BK3 | Pengaturan SDM: template katalog, siklus payroll, geofence, alur cuti, kerahasiaan | `01` Tahap 9 (SDM) | Tahap 10 |
| BK4 | Pajak per item, tipe pajak, konfigurasi pembelian satu halaman, vendor logistik | `01` Tahap 3 dan 11.6 | Tahap 12 |
| BK5 | Mesin kasir, perangkat, pemantauan | `01` Tahap 11.3 | Tahap 11.4 |
| BK6 | Document Export Settings (kop dan format angka dokumen) | `01` Tahap 12 | `02` Tahap A |
| BL1–BL6 | Rekrutmen, absensi siklus, cuti, perubahan status, payroll cut-off | `02` Tahap F (SDM) | `03` Tahap G |
| BM1–BM5 | Pembelian pajak per item, dokumen PDF dan Excel, kasir perangkat, permintaan data | `02` Tahap C dan E | `03` Tahap G |
| BN | Keamanan, privasi AI, batas paket, langganan | `03` Tahap X | `04` |
| BO | Lintas fitur dan uji ulang | Setelah `09` | `11` |

> **Aturan:** tahap dengan kolom *Sebelum* tidak boleh dikerjakan setelah tahap itu, karena datanya menjadi prasyarat tahap berikutnya.

---

## BLOK BK — Pengaturan dan Master Data Susulan (kerjakan di dalam urutan berkas 01)

### BK1. Format tanggal (setelah 01 Tahap 1)

Rujukan: manual `konfigurasi-umum/08` (App Setup dan Branch Setup).

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BK1.1 | Buka daftar Jurnal, Produk, Pajak, Status, Pengguna | Kolom *Dibuat* dan *Diubah* tampil **DD-MM-YYYY** (mis. `10-09-2026`), bukan `10/9/2026` dan bukan `2026-09-10T00:00:00.000000Z` | ⬜ |
| BK1.2 | **Branch Setup** → `date_format` = `YYYY-MM-DD`, simpan, muat ulang | Semua halaman di atas berganti format; cabang lain (bila ada) tidak berubah | ⬜ |
| BK1.3 | Coba `D MMM YYYY` dan `MM/DD/YYYY` | Format mengikuti pilihan; nilai tak dikenal (mis. `XYZ`) kembali ke `DD-MM-YYYY` | ⬜ |
| BK1.4 | Kembalikan ke `DD-MM-YYYY` | Konsisten sampai akhir pengujian (berkas 02 dan 03 memakai tanggal ini) | ⬜ |

### BK2. Impor Excel dan aksi massal pada master data (di sela 01 Tahap 5, 6, 9)

Rujukan: manual `konfigurasi-umum`, standar pola impor produk.

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| BK2.1 | Kriteria KPI | **Import dari Excel**: unduh template, isi 3 baris (satu sengaja cacat), unggah | Pratinjau per baris menandai baris cacat; hanya baris sah yang diimpor; template tidak kosong | ⬜ |
| BK2.2 | Aturan Cashback, Tipe Dokumen Legal | Impor dan **Bulk Actions** (aktifkan, nonaktifkan, hapus) | Aksi massal meminta konfirmasi; ringkasan berhasil/gagal tampil | ⬜ |
| BK2.3 | Kriteria KPI bersekor | Hapus massal kriteria yang sudah punya skor | Ditolak untuk yang bersekor, yang lain terproses | ⬜ |
| BK2.4 | Tingkat Member | Impor Excel dan Bulk Actions; hapus massal tingkat yang masih punya anggota | Yang punya anggota tidak terhapus | ⬜ |
| BK2.5 | Unduh template saat server gagal | Matikan jaringan sebentar lalu unduh | Pesan kesalahan server tampil di layar (bukan layar kosong) | ⬜ |
| BK2.6 | Tipe Jurnal Umum | Buka halaman | Hanya nama dan keterangan yang bisa diubah; tombol tambah dan hapus tidak ada (semua tipe sudah dipakai jurnal) | ⬜ |
| BK2.7 | Sales Channels | **Auto map dari Chart of Accounts** pada channel yang akunnya kosong; isi satu channel manual lebih dulu | Channel kosong terisi akun pendapatan; channel yang sudah dipilih manual **tidak ditimpa** | ⬜ |
| BK2.8 | Kontak baru | Buat kontak | **Mata uang** terisi otomatis dengan mata uang cabang (IDR); kolom Tipe berwarna berbeda per tipe | ⬜ |
| BK2.9 | Form tambah massal (kontak, gudang, satuan, pajak, akun, jabatan) | Buka Add Bulk | Tombol **Add Row** di sisi kanan; baris bisa ditambah dan dihapus | ⬜ |

### BK3. Pengaturan SDM susulan (setelah 01 Tahap 9, sebelum Tahap 10)

Rujukan: manual `hrm/01`, `hrm/05`, `hrm/06`, `hrm/15`.

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| BK3.1 | Departments | Buat departemen induk "Operasional" dan anak "Toko", "Dapur" | Induk tersimpan dan tampil benar di daftar dan di form edit; ubah dan hapus bekerja (perbaikan slug) | ⬜ |
| BK3.2 | Attendance Statuses | Tidak ada tombol Tambah; pakai **Gunakan Template** (Hadir, Alpa, Izin, dst.) | Nama, warna, dan aktif bisa diubah; kode bawaan tidak bisa diubah | ⬜ |
| BK3.3 | Employment Types | **Gunakan Template**: Tetap, Kontrak, **Masa Percobaan (PROBATION)** | Template Masa Percobaan punya tanggal akhir kontrak wajib; template terdaftar di katalog | ⬜ |
| BK3.4 | Referensi Pajak Penghasilan (PTKP) | Buka halaman | Nominal tampil sebagai angka rapi sebelum diklik (bukan `54undefined000`) | ⬜ |
| BK3.5 | HRM Configs → Siklus Payroll | Pilih **Calendar month**; lalu **Tanggal cut-off** = 25; lalu **End of month** | Pratinjau siklus tampil: cut-off 25 membuat Oktober berjalan 26 September–25 Oktober; End of month berjalan hari terakhir bulan; perubahan tidak mengubah periode yang sudah ada | ⬜ |
| BK3.6 | HRM Configs → Absensi | Aktifkan **Area cakupan**, isi radius 100 m, klik peta atau geser pin untuk titik pusat | Pusat bawaan = lokasi cabang bila tidak diisi; tersimpan dan terbaca ulang | ⬜ |
| BK3.7 | HRM Configs → Alur Kerja | Aktifkan **Setujui langsung cuti yang diajukan HRD** | Hanya berlaku bila persetujuan cuti aktif; tersimpan | ⬜ |
| BK3.8 | HRM Configs → Kerahasiaan | Periksa saklar **restrict confidential employee data** | Bawaan **aktif**; dicatat siapa yang boleh melihat gaji, NIK, rekening | ⬜ |
| BK3.9 | Leave Types | Buat "Cuti Tahunan" dengan **Allow half day** aktif | Opsi setengah hari muncul pada form pengajuan hanya untuk jenis ini | ⬜ |
| BK3.10 | Approval Workflow Configs | Pada alur Cuti buat tiga langkah: Manajer (**harus satu departemen dengan karyawan**), HRD, Direktur | Saklar satu-departemen ada di form dan di edit massal; tersimpan | ⬜ |
| BK3.11 | Employees | Isi **ID Mesin Absensi** (attendance PIN) pada dua karyawan | Tersimpan; dipakai untuk mencocokkan log mesin (BL3) | ⬜ |
| BK3.12 | Roles | Beri role HR izin **view-confidential**; role lain tidak | Izin tampil di daftar izin; Admin otomatis memilikinya | ⬜ |

### BK4. Pajak, pembelian, dan vendor logistik (setelah 01 Tahap 3 dan 11.6)

Rujukan: manual `purchasing/01`, `purchasing/12`, changelog pajak per item.

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| BK4.1 | Taxes | Pada tiap pajak pilih **Tax Type**: PPN-IN dan PPN-OUT = `vat`; PPH23 dan PPH21 = `withholding`; tambah satu `import_duty` bila perlu | Tipe tersimpan dan tampil di daftar; Quick Create Tax juga menawarkan tipe | ⬜ |
| BK4.2 | Taxes → Template | Gunakan template pajak | Tipe terisi dari template | ⬜ |
| BK4.3 | Product SKU → **Default Purchase Taxes** | Pilih PPN-IN pada Beras Premium 5 kg dan PPN-IN pada ATK | Tersimpan; hanya pajak milik cabang aktif yang bisa dipilih | ⬜ |
| BK4.4 | Purchasing → **Purchase Configs** | Buka halaman; pastikan **tidak ada** menu terpisah "Purchase Journal Configuration" | Semua pengaturan alur, persetujuan, mode jurnal, dan pemetaan akun ada di satu halaman | ⬜ |
| BK4.5 | Purchase Configs → pemetaan akun | Tekan **Auto-map dari Bagan Akun** | Sembilan fungsi utama terpetakan **dan** lima fungsi biaya logistik (beban logistik, selisih biaya, landed cost clearing, biaya yang ditagih ulang, utang pajak potong); tidak lagi "tidak ada yang dipetakan" | ⬜ |
| BK4.6 | Contacts | Buat atau ubah "Ekspedisi Cepat Nusantara": saklar **Vendor Logistik** aktif, tipe tetap supplier | Lencana "Vendor Logistik" tampil; filter kontak punya opsi vendor logistik; supplier biasa tidak berubah | ⬜ |
| BK4.7 | Charge Invoice | Buka form Tagihan Biaya Logistik | Hanya kontak vendor logistik yang menjadi pilihan utama pemasok tagihan | ⬜ |

### BK5. Mesin kasir (setelah 01 Tahap 11.3)

Rujukan: manual `pos/01`, `konfigurasi-umum/16`.

| # | Halaman | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| BK5.1 | Cash Registers | Buat "Kasir Toko 1" dan petakan ke gudang **Gudang Toko Retail** (tipe store) | Hanya gudang bertipe store yang bisa dipilih; saat buka sesi gudang terkunci mengikuti mesin | ⬜ |
| BK5.2 | Cash Registers | Buat "Kasir Dapur" dan petakan ke **Meja** restoran (Meja 1–6) | Daftar "Meja yang dilayani" membaca master Meja modul Restoran (diisi di Restaurant → Tables, bukan di sini) | ⬜ |
| BK5.3 | Mesin berisi sesi terbuka | Ubah gudang mesin saat sesi terbuka | Ditolak | ⬜ |
| BK5.4 | POS Configs → **Register device binding** | Aktifkan | Pengikatan perangkat nyala (BM3) | ⬜ |
| BK5.5 | POS Configs → pemantauan | Isi **register_idle_alert_days** = 3 dan **session_open_alert_hours** = 12 | Tersimpan; nilai 0 mematikan peringatan | ⬜ |
| BK5.6 | Cash Registers → kolom | Lihat tabel | Kolom Toko, Aktivitas, dan Perangkat tampil; ada penanda mesin menganggur atau sesi terlalu lama | ⬜ |

### BK6. Document Export Settings (setelah 01 Tahap 12, sebelum transaksi 02)

Rujukan: manual `konfigurasi-umum/18`. Halaman: **Pengaturan tampilan PDF** (`client-master/pdf-layout-settings`).

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BK6.1 | Tab **Letterhead**: isi NPWP, baris kontak, posisi dan ukuran logo, kop terbagi/bertumpuk, posisi QR | Pratinjau langsung berubah; **Refresh** memuat ulang; tidak ada error pratinjau | ⬜ |
| BK6.2 | Tab **Appearance**: font, ukuran, margin, rata judul, watermark | Pratinjau mengikuti | ⬜ |
| BK6.3 | Gaya angka dan tanggal | Pilih gaya Indonesia (1.234,56); simpan | Berlaku di PDF dokumen dan laporan; bila tidak diubah gaya lama (1,234.56) tetap | ⬜ |
| BK6.4 | Label tanda tangan | Isi dua label (Dibuat oleh, Disetujui oleh) | Simpan tidak error; label muncul di PDF | ⬜ |
| BK6.5 | **Pop out** pratinjau | Buka jendela melayang; geser, ubah ukuran, maksimalkan (klik dua kali header), minimalkan lalu pulihkan dari pil | Form tetap bisa diedit; posisi dan ukuran diingat; dropdown jenis dokumen mengganti pratinjau | ⬜ |
| BK6.6 | Pengaturan per jenis dokumen | Ubah pengaturan khusus Quotation, lalu PO | Tiap jenis memakai pengaturannya; jenis lain mengikuti bawaan | ⬜ |
| BK6.7 | Unduh PDF satu PO dan satu laporan | Setelah BK6.1–BK6.4 | Kop, nomor halaman, format angka, tanda tangan sesuai pengaturan; ekspor Excel laporan mengikuti pengaturan cabang | ⬜ |

---

## BLOK BL — Alur SDM Susulan (kerjakan setelah 02 Tahap F, sebelum 03 Tahap G)

Prasyarat: berkas 01 Tahap 9 dan blok BK3 selesai; payroll September (02 Tahap F) sudah dijalankan.

### BL1. Rekrutmen lengkap

Rujukan: manual `hrm/04`.

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BL1.1 | Buka lowongan "Staf Pendampingan Pelanggan" (Job Vacancy), lalu **Generate Public Link** | Tautan publik dengan masa berlaku dibuat; **satu tautan bisa dipakai banyak pelamar** sampai kedaluwarsa | ⬜ |
| BL1.2 | Buka tautan di jendela tanpa login; isi dan kirim formulir dua pelamar | Lamaran masuk ke daftar dengan sumber "publik"; pengiriman beruntun dibatasi (throttle) | ⬜ |
| BL1.3 | Buka tautan yang sudah kedaluwarsa (ubah masa berlaku) | Ditolak dengan pesan kedaluwarsa | ⬜ |
| BL1.4 | Detail pelamar | Menampilkan **lowongan yang dilamar** dan riwayat status | ⬜ |
| BL1.5 | Hrm → **Job Interviews** | Jadwalkan wawancara (tanggal, pewawancara); halaman daftar wawancara terbuka (bukan "Page not found") | Status `scheduled` → `completed`/`cancelled`; status lamaran ikut berubah | ⬜ |
| BL1.6 | **Job Offers** | Buat penawaran untuk pelamar lolos; kirim | Status `draft → sent → accepted/declined`; **perpindahan ke tahap penawaran butuh persetujuan** (alur approval) | ⬜ |
| BL1.7 | Penawaran diterima | Terima penawaran | Pelamar dapat dilanjutkan menjadi karyawan; data terbawa | ⬜ |
| BL1.8 | Lompat status | Coba memindahkan lamaran langsung ke `offered` tanpa wawancara | Ditolak atau mengikuti alur yang ditetapkan (tidak bebas lompat) | ⬜ |

### BL2. Absensi siklus, geofence, dan mesin

Rujukan: manual `hrm/05`.

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BL2.1 | Setelah BK3.5, tunggu proses malam atau jalankan perintahnya | Catatan harian terbentuk untuk semua karyawan aktif sampai akhir siklus: hari kerja = **Terjadwal**, hari libur/non-kerja = **Libur** | ⬜ |
| BL2.2 | Karyawan Check in dari dashboard karyawan | Peta dengan **lingkaran area cakupan** dan posisi bergerak; tombol aktif hanya **di dalam area**; **jam dicatat server** (bukan jam perangkat) | ⬜ |
| BL2.3 | Check in dari luar area | Tombol nonaktif dengan penjelasan; panggilan API tetap ditolak server | ⬜ |
| BL2.4 | Check in pada hari Terjadwal | Catatan hari itu **diperbarui** (bukan dibuat ganda) | ⬜ |
| BL2.5 | Hari Terjadwal yang lewat jam akhir shift tanpa check in | Otomatis menjadi **Alpa** | ⬜ |
| BL2.6 | Daftar absensi | Filter karyawan, tanggal, status; bawaan bulan berjalan; tanggal rapi | ⬜ |
| BL2.7 | Absensi yang periode payroll-nya sudah diproses | Ditandai **terkunci**, tidak bisa diubah atau dihapus; koreksi lewat **Penyesuaian Absensi** | ⬜ |
| BL2.8 | **Mesin Absensi**: daftarkan mesin, lihat token, endpoint, pemetaan field | Mesin tersimpan; **Log Mesin** menampilkan data yang masuk | ⬜ |
| BL2.9 | Punch dari mesin untuk karyawan yang ID Mesinnya belum diisi | Tercatat sebagai tidak cocok; setelah ID Mesin diisi (BK3.11) **proses ulang** menjadikannya absensi sah | ⬜ |
| BL2.10 | **Rekap Absensi** | Pilih periode gaji (tidak bisa ke depan; bawaan periode berjalan): jumlah per status, jam kerja, menit terlambat, lembur per karyawan cocok dengan catatan harian | ⬜ |
| BL2.11 | Detail rekap satu karyawan | Absensi harian, saldo cuti, dan pengajuan cuti periode itu | ⬜ |
| BL2.12 | Dashboard HRM | Pada hari cut-off dan dua hari sesudahnya muncul pengingat dengan tombol ke rekap periode | ⬜ |

### BL3. Cuti

Rujukan: manual `hrm/06`.

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BL3.1 | Karyawan biasa membuka **Cuti Saya** | Saldo per jenis tampil; hanya data miliknya; akun harus terhubung ke data karyawan (bila tidak, pesan jelas) | ⬜ |
| BL3.2 | Ajukan cuti dari Cuti Saya | **Selalu melewati persetujuan**, apa pun pengaturan lain | ⬜ |
| BL3.3 | Batalkan pengajuan yang belum diputuskan | Berhasil; yang sudah diputuskan tidak bisa dibatalkan di sini | ⬜ |
| BL3.4 | Ajukan cuti **setengah hari** | Hanya jenis yang mengizinkan; tanggal mulai = selesai; pilih periode (pagi/siang); `total_days` = 0,5; saldo berkurang 0,5 | ⬜ |
| BL3.5 | HRD mengajukan cuti untuk karyawan lain dengan opsi *Setujui langsung* aktif | Langsung berstatus disetujui; cuti yang diajukan seseorang untuk dirinya sendiri **tetap** melewati persetujuan | ⬜ |
| BL3.6 | Persetujuan satu departemen | Manajer departemen lain mencoba menyetujui cuti karyawan Toko | Tombol Setujui/Revisi/Tolak **nonaktif dengan tooltip alasan**; panggilan API ditolak; Manajer departemen yang sama bisa | ⬜ |
| BL3.7 | Pembanding departemen | Cuti diajukan HRD atas nama karyawan Toko | Pembanding memakai departemen **karyawan yang cuti**, bukan yang mengetik | ⬜ |
| BL3.8 | Karyawan atau atasan tanpa departemen | Atasan tanpa data karyawan mencoba menyetujui langkah satu-departemen | Ditolak (tidak ada gerbang yang terbuka diam-diam) | ⬜ |
| BL3.9 | Detail pengajuan | Nomor pengajuan di daftar membuka halaman detail; tanggal rapi; baris cuti pending di dashboard membuka detail | ⬜ |
| BL3.10 | Saldo Cuti | Cari dan filter karyawan di popover filter | Hasil tersaring; saldo cocok dengan pengajuan disetujui | ⬜ |

### BL4. Perubahan status karyawan

Rujukan: manual `hrm/15`.

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BL4.1 | Karyawan baru diberi jenis **Masa Percobaan** dengan tanggal akhir kontrak 90 hari | Dashboard HRM menampilkan widget *Kontrak akan berakhir* (jendela 90 hari) | ⬜ |
| BL4.2 | Detail karyawan → **Change Employment Status**: ke Tetap, isi alasan, gaji baru opsional | Pengajuan tersimpan; bila approval aktif menunggu persetujuan | ⬜ |
| BL4.3 | Setujui | Jenis karyawan dan tanggal berlaku berubah; panel **Employment History** mencatat dari/ke; gaji baru berlaku mulai tanggal efektif; notifikasi terkirim | ⬜ |
| BL4.4 | Tolak dan batalkan | Pengajuan ditolak/dibatalkan tidak mengubah data | ⬜ |
| BL4.5 | Widget kontrak | Setelah menjadi Tetap tanpa tanggal akhir, karyawan hilang dari widget | ⬜ |

### BL5. Payroll dengan cut-off dan kerahasiaan

Rujukan: manual `hrm/09`, `hrm/10`.

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BL5.1 | Buat periode payroll dengan cut-off 25 | Rentang tanggal tampil di periode dan **dibekukan** saat dibuat; perubahan cut-off tidak mengubah periode lama | ⬜ |
| BL5.2 | **Generate Payslip** | Ada opsi memilih periode payroll; potongan BPJS dan PPh 21 terisi dari referensi (bukan nol) | ⬜ |
| BL5.3 | Karyawan membuka **Slip Gaji Saya** dan **Koreksi Absensi Saya** | Hanya miliknya; koreksi masuk antrean HR | ⬜ |
| BL5.4 | Pengguna tanpa izin *view-confidential* membuka daftar karyawan dan opsi | Kolom gaji pokok, NIK, NPWP, status PTKP, bank, rekening, PIN absensi **tersembunyi** untuk karyawan lain; milik sendiri tetap terlihat | ⬜ |
| BL5.5 | Pengguna tanpa izin membuka struktur gaji, komponen gaji karyawan, slip karyawan lain, PDF slip | Ditolak 403; daftar slip hanya milik sendiri | ⬜ |
| BL5.6 | Urut atau cari berdasarkan kolom rahasia | Ditolak 403 untuk pengguna tanpa hak | ⬜ |
| BL5.7 | Edit karyawan oleh pengguna tanpa hak | Nilai rahasia **tidak tertimpa kosong** saat simpan | ⬜ |
| BL5.8 | Matikan saklar kerahasiaan di HRM Configs | Pembatasan hilang untuk cabang itu; nyalakan kembali | ⬜ |
| BL5.9 | Payroll September dibandingkan jurnal | Total slip = jurnal gaji (berkas 07 AW-4) | ⬜ |

---

## BLOK BM — Pembelian, Dokumen, Kasir, dan Data Pribadi (setelah 02 Tahap C dan E)

### BM1. Pajak per item pada Purchase Order

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BM1.1 | Buat PO dari PQ atau baru; pilih item Beras Premium 5 kg | Pajak bawaan SKU (PPN-IN) terisi otomatis per baris | ⬜ |
| BM1.2 | Tambah dua pajak pada satu item: PPN-IN dan PPh 23 | Lencana **+/−** per pajak; PPN menambah, PPh mengurangi; total PO benar | ⬜ |
| BM1.3 | Detail PO | Kolom Pajak per item dengan lencana dan nominal | ⬜ |
| BM1.4 | Jurnal dari PO ke GR dan PI | Pajak per item terbawa ke jurnal (PPN masukan dan utang potong) | ⬜ |
| BM1.5 | SO: opsi sumber SO menampilkan **nama pelanggan** | Pilihan SO di dokumen turunan menunjukkan pelanggan | ⬜ |
| BM1.6 | Quotation dan SO | Belum memakai pajak per item (dicatat bila diharapkan) | ⬜ |

### BM2. Dokumen PDF dan Excel sesuai Document Export Settings

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BM2.1 | Unduh PDF: Quotation, SO, PO, PI, RFQ, Charge Invoice, Slip Gaji | Semua memakai kop, footer, nomor halaman, format angka dan tanggal yang diatur di BK6 | ⬜ |
| BM2.2 | Ganti bahasa pengguna lalu unduh PDF | Judul dan label dokumen mengikuti bahasa; catat teks yang masih tetap (label kolom, "Pemasok", "Subtotal") sebagai gap penerjemahan | ⬜ |
| BM2.3 | Ekspor Excel dari lima laporan | Format dan judul mengikuti pengaturan cabang | ⬜ |
| BM2.4 | Dokumen dengan logo besar dan kop terpisah | Kop tidak terpotong (regresi overflow) | ⬜ |

### BM3. Kasir dengan mesin terikat perangkat

Prasyarat: BK5 selesai, dua perangkat atau dua profil browser.

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BM3.1 | Perangkat A membuka sesi di Kasir Toko 1 | Mesin terkunci ke perangkat A | ⬜ |
| BM3.2 | Perangkat B mencoba membuka sesi di mesin yang sama | Ditolak (`register_device_mismatch`) dengan pesan jelas | ⬜ |
| BM3.3 | Manajer menekan **release the locked device** | Perangkat B kini bisa; perangkat A kehilangan kunci | ⬜ |
| BM3.4 | Buka sesi dengan gudang selain gudang mesin | Ditolak | ⬜ |
| BM3.5 | Biarkan mesin menganggur melewati ambang dan sesi terbuka melewati jam batas | Notifikasi peringatan mesin menganggur dan sesi lupa ditutup muncul pada waktu pemeriksaan harian (perintah terjadwal 08.00) | ⬜ |
| BM3.6 | Cara hitung kas tutup sesi | Uji tiga mode (hanya jumlah, per pecahan, gabungan) dan penanganan selisih (lihat Z5, Z12) | ⬜ |

### BM4. Permintaan data pribadi dan anonimisasi

Rujukan: manual `konfigurasi-umum/24`.

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BM4.1 | **Data Subject Requests**: cari karyawan, **Ekspor** | JSON memuat karyawan lengkap: keluarga, kontak darurat, akun login, slip gaji, absensi, cuti | ⬜ |
| BM4.2 | Ekspor member (kontak pelanggan) | Memuat alamat, rekening, faktur penjualan; pelanggan umum dan pemasok tidak termasuk | ⬜ |
| BM4.3 | **Anonimkan** satu karyawan uji yang sudah tidak aktif | Nama dan data pribadi teranonimkan; **PIN absensi dikosongkan**; log mesin tidak lagi memuat PIN; mesin tidak bisa mencocokkan orang itu | ⬜ |
| BM4.4 | Dokumen lama | Slip dan absensi lama tetap ada sebagai data anonim (tidak hilang) | ⬜ |
| BM4.5 | Riwayat permintaan | Setiap ekspor dan anonimisasi tercatat dengan siapa dan kapan | ⬜ |

### BM5. Lampiran dokumen dan Page Education

| # | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- |
| BM5.1 | Lampirkan berkas pada Production Order, Production Log, Hauling, Royalty, Survey (Manufaktur dan Pertambangan) | Unggah, daftar, dan hapus lampiran berfungsi; mengikuti mesin lampiran terpusat | ⬜ |
| BM5.2 | Ikon **?** di navbar pada halaman index, create, edit, dan detail dari 10 modul | Panel pendidikan tampil dengan teks yang relevan; tidak ada halaman tanpa ikon | ⬜ |

---

## BLOK BN — Keamanan, Privasi AI, Batas Paket, Langganan (setelah 03 Tahap X)

Sisi **klien**; pengelolaan paket dan langganan adalah tugas pemilik platform (suite `penjualan-sewa-aplikasi`).

| # | Fitur | Langkah | Yang diperiksa | OK |
| --- | --- | --- | --- | --- |
| BN1 | Pengungkapan AI | Admin klien membuka widget AI pertama kali | Muncul teks pengungkapan dan chat **tidak bisa dipakai** sampai dikonfirmasi; setelah konfirmasi chat jalan; konfirmasi dicatat | ⬜ |
| BN2 | Versi pengungkapan | (Dengan bantuan developer) naikkan versi teks | Semua cabang diminta konfirmasi ulang | ⬜ |
| BN3 | Autentikasi dua langkah | Aktifkan, simpan kode pemulihan, login ulang | Kode dipakai sekali; kode pemulihan dipakai sekali; mematikan butuh password dan kode | ⬜ |
| BN4 | Pembatasan percobaan login | Salah password berulang | Ada penundaan/pembatasan (throttle) dengan pesan jelas | ⬜ |
| BN5 | Batas paket | Dengan paket berbatas (mis. pengguna 3): tambah pengguna ke-4, cabang, karyawan, atau meja kasir melebihi batas | Penambahan ditolak dengan pesan kuota (pengguna atau cabang sesuai aturan paket); batas kosong berarti tanpa batas | ⬜ |
| BN6 | Modul mengikuti paket | Bandingkan menu sebelum dan sesudah paket berganti | Modul dan izin yang tidak ada di paket hilang dari menu dan daftar izin; tidak ada tautan menuju halaman yang tidak bisa dibuka | ⬜ |
| BN7 | Bahasa terkunci paket | Buka pemilih bahasa pada paket tanpa bahasa tambahan | Bahasa lain terkunci dengan tulisan *upgrade*; memilihnya membawa ke halaman langganan | ⬜ |
| BN8 | Halaman **Subscription** | Buka Settings → Subscription | Paket, status (`trialing`, `pending_payment`, `active`, `past_due`, `cancelled`, `expired`), tanggal berikut, pemakaian pengguna/cabang terhadap batas, tagihan | ⬜ |
| BN9 | Ajukan ganti paket | Pilih paket publik lain | Satu permintaan menunggu per langganan; klien tidak bisa mengubah langganannya sendiri | ⬜ |
| BN10 | Penangguhan | (Pemilik menangguhkan klien uji) login dan akses API | Login ditolak dengan pesan penangguhan; data tidak dihapus; pemulihan memulihkan akses; tugas terjadwal tidak memproses klien tertangguhkan | ⬜ |
| BN11 | Masa tenggang | Langganan lewat jatuh tempo | Status `past_due` lalu `expired` mengikuti masa tenggang; setelah pembayaran dikonfirmasi akses pulih | ⬜ |

---

## BLOK BO — Lintas Fitur Baru

| # | Skenario | Pemeriksaan angka atau perilaku | OK |
| --- | --- | --- | --- |
| BO1 | **Karyawan dari rekrutmen sampai gaji** | Pelamar lewat tautan publik → wawancara → penawaran disetujui → karyawan → jadwal → absensi (geofence) → cuti setengah hari → payroll dengan cut-off → slip sendiri. Total hari kerja, potongan cuti, dan gaji kotor-bersih cocok | ⬜ |
| BO2 | **Perubahan status memengaruhi payroll** | Probation ke Tetap tengah periode dengan gaji baru: payroll membagi dua dengan benar atau memakai gaji efektif | ⬜ |
| BO3 | **Pajak per item sampai laporan pajak** | PO dengan PPN-IN dan PPh 23 per item → GR → PI → Tax Summary: PPN Masukan dan utang potong cocok dengan angka per item | ⬜ |
| BO4 | **Landed cost vendor logistik** | Tagihan ekspedisi (vendor logistik) untuk GR → nilai persediaan naik → laporan Landed Cost dan Hutang Logistik → HPP saat dijual | ⬜ |
| BO5 | **Kerahasiaan lintas modul** | Pengguna tanpa hak mencoba memperoleh gaji lewat: daftar karyawan, opsi, `additionalRelations` di modul lain, pencarian, pengurutan, ekspor, PDF | Tidak ada jalan yang membocorkan | ⬜ |
| BO6 | **Format tanggal di seluruh pohon menu** | Ganti format di BK1.2 lalu telusuri 15 halaman acak (daftar, detail, laporan, PDF) | Semua mengikuti; tidak ada `Invalid Date` atau ISO mentah | ⬜ |
| BO7 | **Anonimisasi tidak merusak laporan** | Setelah BM4.3: laporan payroll, absensi, dan neraca tetap seimbang | ⬜ |
| BO8 | **Paket berbatas dan semua pembuatan data** | Dengan batas kasir 1: BK5 membuat mesin kedua | Ditolak jelas; mesin pertama tidak terganggu | ⬜ |

---

## Daftar Periksa Cepat (urut kerja)

- [ ] BK1 (setelah 01 Tahap 1) · [ ] BK2 (di sela Tahap 5, 6, 9) · [ ] BK3 (setelah Tahap 9) · [ ] BK4 (Tahap 3, 11.6) · [ ] BK5 (Tahap 11.3) · [ ] BK6 (Tahap 12)
- [ ] BL1–BL5 (setelah 02 Tahap F)
- [ ] BM1–BM5 (setelah 02 Tahap C dan E)
- [ ] BN1–BN11 (setelah 03 Tahap X)
- [ ] BO1–BO8 (setelah berkas 09)
- [ ] Uji ulang temuan selesai: berkas `11`
