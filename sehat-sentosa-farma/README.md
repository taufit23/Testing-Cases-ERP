# PT Sehat Sentosa Farma: Panduan Pengujian Masif (Masa Trial)

Satu file ini adalah **peta jalan** untuk menjalankan seluruh suite di folder ini dari awal sampai akhir. Isi kasus ujinya tetap ada di file bernomor
(`00` sampai `99`); README ini hanya menentukan **urutan, jadwal, dan centang progres** supaya tidak ada yang tertinggal.

- **Akun uji:** Dr. Rahmat Hidayat, `rahmadhidayat@mail.com` (hasil pengajuan `/subscribe`, nomor ONB-202610-0001).
- **Paket:** Enterprise Full, siklus bulanan, status `trialing`.
- **Batas trial:** **5 November 2026**. Hari ke-1 = 22 Oktober 2026, jadi tersedia sekitar **15 hari kerja uji**. Jadwal di bagian 3 mengikuti batas ini.
- **Periode data uji:** Oktober 2026 (angka acuan di file `01` dihitung untuk bulan ini).

---

## 0. Baca ini dulu (5 menit)

1. **Pastikan ini bukan data produksi.** File `00` mensyaratkan pengujian di database uji. Kalau `ranahku.web.id` adalah lingkungan produksi,
   pertimbangkan memakai lingkungan dev untuk bagian yang menulis banyak data (persediaan, jurnal, payroll, tutup periode). Tutup periode dan tahun
   fiskal **tidak bisa dibatalkan dengan mudah**, jadi jadikan langkah paling akhir.
2. **Cara membaca satu baris kasus** (aturan dari file `00` bagian 5):
   - **Positif**: jalur normal harus berhasil dan efeknya terlihat di modul lain.
   - **Negatif**: harus ditolak dengan pesan jelas, bukan gagal diam-diam atau error server.
   - **Aturan manual**: lakukan sesuai aturan, lalu langgar aturannya, dan lihat penolakannya.
   - **Peran tanpa izin**: tombol harus **terlihat tetapi nonaktif dengan tooltip alasan** (bukan hilang), dan endpoint menjawab **403**.
   - **Netralisasi**: cara mengembalikan data ke keadaan semula. Kerjakan hanya kalau file berikutnya butuh data awal itu.
3. **Kalau bingung "ini diinput di mana":** ada tiga petunjuk di dalam suite.
   - **File `00` bagian 1.2**: tabel tiap atribut profil perusahaan, tingkatnya (perusahaan atau cabang), menu dan alamat halamannya, serta isi yang dipakai. Bagian 3 memuat input mitra, produk, gudang, akun, dan saldo awal. **Bagian 4.1** memuat urutan memasukkan data acuan.
   - **Setiap bagian di file `02` sampai `20`** diawali baris **Input di** (menu sidebar dan alamat halaman, diambil dari bab manual book) dan di atasnya ada **Dikerjakan oleh** (peran) serta **Cabang aktif**.
   - **File `01`** punya kolom **Halaman input** di setiap langkah, dan `00a` punya tabel alamat halaman perjalanan berlangganan.
   Beberapa hal **memang tidak punya tempat input** (mis. status PKP, merek di profil perusahaan, persediaan awal). Itu dijelaskan di tempatnya, bukan kesalahanmu.
4. **Baris berlabel "(draf)"** dirancang model lokal dari isi manual book. Cocokkan dulu dengan layar sebenarnya. Kalau barisnya tidak masuk akal,
   catat sebagai "kasus tidak valid", bukan sebagai bug aplikasi.
5. **Angka acuan di file `01` jangan diubah.** Kalau hasil di layar beda, catat sebagai temuan.
6. **Satu klien, satu trial.** Jalur penangguhan, ganti paket, dan berhenti berlangganan (`00a` S14 sampai S18) mengubah status langganan
   dan bisa mengunci akun uji. Kerjakan **paling akhir**, atau pakai klien uji kedua.
7. Setiap temuan dicatat di tabel **bagian 6** (jangan hanya diingat).

### Ringkasan beban kerja

| Kelompok | File | Jumlah baris kasus |
| --- | --- | ---: |
| Pondasi | `00`, `00a`, `02`, `03`, `04` | 289 (+ alur `00a` S1 sampai S20) |
| Transaksi inti | `05` Pembelian, `06` Persediaan, `07` Penjualan | 197 |
| Penjualan lapangan dan ritel | `08` Kanvasing, `09` POS, `10` Restoran | 166 |
| Produksi dan aset operasional | `11` Manufaktur, `12` Pertambangan, `13` Sewa | 132 |
| Akuntansi, keuangan, SDM, proyek | `14`, `15`, `16`, `17` | 249 |
| Pelaporan dan publik | `18`, `19`, `20` | 36 |
| Alur terpadu lintas modul | `01` (langkah 1 sampai 40) | 40 langkah |
| Kebutuhan bisnis dan celah | `21`, `95`, `96`, `97` | 84 baris uji celah |
| Izin dan batas | `98` | 49 |
| Penutup | `99` peta cakupan | pemeriksaan akhir |

---

## 1. Urutan umum (jangan dibalik)

```
FASE A  Pondasi         00a (sisa)  →  02  →  03  →  04
FASE B  Alur terpadu    01 bagian A  →  B  →  C  →  D  →  E     ← dikerjakan BERSAMAAN dengan file modul
FASE C  Kedalaman modul 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17
FASE D  Pelaporan       18 → 19 → 20
FASE E  Penutupan       01 bagian F  →  98  →  99
FASE F  Celah           21 → (95, 96, 97 sebagai referensi)
FASE G  Berisiko        00a S13 sampai S20 (ganti paket, tunggakan, tangguh, berhenti), tutup periode
```

**Cara menggabungkan file `01` dengan file modul:** kerjakan satu langkah di `01` (angka acuan), lalu langsung buka file modulnya dan jalankan semua
baris Positif, Negatif, dan Aturan manual untuk bagian terkait. Dengan begitu data transaksi dari `01` ikut dipakai sebagai bahan uji modul.

---

## 2. Status saat ini (sudah tercapai)

Bagian dari `00a` Fase 1 sampai 3 sudah terbukti jalan lewat uji nyata. Centang yang sudah, sisanya tetap dikerjakan:

- [x] S1, S2: halaman `/subscribe` tampil dengan paket aktif dan publik
- [x] S3: pengajuan terkirim, halaman status tampil
- [x] S4, S4a: pengajuan muncul di Core → Subscriptions → Onboarding
- [x] S5: owner menyetujui, perusahaan, cabang, akun, dan langganan terbentuk
- [x] S7: halaman status berubah menjadi "Langganan Anda aktif"
- [x] S8: login dengan akun yang dipilih calon klien berhasil
- [ ] Tahap **First Login** di halaman onboarding berubah centang (cek setelah refresh)
- [ ] S3a, S3b: kasus negatif pengajuan (email dobel, kata sandi pendek, persetujuan tidak dicentang, token salah)
- [ ] S5a, S5b, S6, S6a: setujui dua kali, tolak tanpa alasan, tolak dengan alasan, peran non-owner
- [ ] S9, S10: halaman Langganan dan menu hanya berisi modul paket

---

## 3. Jadwal 15 hari (22 Okt sampai 5 Nov 2026)

Tanggal bisa digeser. Yang penting urutan fasenya. Jadwal sengaja menyisakan 3 hari penyangga di akhir.

| Hari | Tanggal | Fokus | File dan bagian |
| ---: | --- | --- | --- |
| 1 | Kam 22 Okt | Pondasi akun dan langganan | Bagian 2 di atas; `00a` Fase 1 sampai 4; `02` §9 sampai §10 (masuk, bantuan, pengaturan akun) |
| 2 | Jum 23 Okt | Master data dasar | `00` §1.2 dan §4.1 (urutan input data acuan), lalu `00` §3; `03` §1 sampai §9 (mata uang, gudang, kategori, pembayaran, fiscal year, status, permission, app setup) |
| 3 | Sab 24 Okt | Master data lanjutan | `03` §10 sampai §23; `01` langkah 2 sampai 5 |
| 4 | Min 25 Okt | Persetujuan dan AI | `04` §1 sampai §5; ulangi `01` langkah 4 |
| 5 | Sen 26 Okt | Pembelian | `01` langkah 6 sampai 10; `05` §1 sampai §12 |
| 6 | Sel 27 Okt | Persediaan | `01` langkah 11 dan 22; `06` §1 sampai §6 |
| 7 | Rab 28 Okt | Penjualan | `01` langkah 12 sampai 14; `07` §1 sampai §9 |
| 8 | Kam 29 Okt | Kanvasing dan POS | `01` langkah 15 sampai 18; `08` §1 sampai §8; `09` §1 sampai §7 |
| 9 | Jum 30 Okt | Restoran, manufaktur, tambang | `01` langkah 19 sampai 22; `10`, `11`, `12` |
| 10 | Sab 31 Okt | Sewa, aset, biaya | `01` langkah 23, 27, 28; `13`; `14` §7; `15` |
| 11 | Min 1 Nov | SDM dan proyek | `01` langkah 24 sampai 26; `16` §1 sampai §14; `17` §1 sampai §6 |
| 12 | Sen 2 Nov | Akuntansi dan pelaporan | `14` §1 sampai §10 (tanpa tutup periode); `18`; `19`; `20` |
| 13 | Sel 3 Nov | Izin, isolasi, batas, celah | `98` penuh; `21` penuh; `01` langkah 31 sampai 40 |
| 14 | Rab 4 Nov | Fase berisiko | `00a` S13 sampai S20; `14` §4 (tutup periode); `01` langkah 29 dan 30 |
| 15 | Kam 5 Nov | Penutup dan rekap | `99` peta cakupan, tabel temuan bagian 6, keputusan |

**Kalau waktu tidak cukup, potong dari bawah:** Fase G dan `21` bisa ditunda tanpa merusak yang lain. Pondasi (`02`, `03`) dan transaksi inti
(`05`, `06`, `07`, `14`) jangan dikorbankan, karena modul lain bergantung padanya.

---

## 4. Checklist per fase

Centang `[x]` setelah **semua baris** bagian itu dijalankan (Positif, Negatif, Aturan manual, Peran tanpa izin). Kalau ada yang gagal, centang
tetap diberikan setelah temuannya masuk tabel bagian 6.

### FASE A. Pondasi

**`00b` Tipe akun dan akun acuan**
- [ ] §2 delapan tipe akun dibuat
- [ ] §3 empat puluh akun dibuat (modul Manufaktur, Pertambangan, Sewa boleh menyusul)
- [ ] §4 akun dihubungkan ke konfigurasi tiap modul sebelum modul itu diuji
- [ ] §5 saldo awal 1 Okt, Trial Balance seimbang Rp 500.000.000
- [ ] §6 kasus uji data akun

**`00` Profil dan prasyarat**
- [ ] Seluruh cabang, peran, dan pengguna uji dibuat (tabel §1 dan §2)
- [ ] Mitra, produk, gudang sesuai §3
- [ ] 8 tipe akun dan 40 akun dibuat **sesuai `00b`** (klien baru mulai dengan COA kosong), akun saldo awal ditandai, akun dihubungkan ke tiap modul (`00b` §4)
- [ ] Saldo awal 1 Okt: Bank Operasional dan Modal Pemilik masing-masing Rp 500.000.000

**`00a` Perjalanan berlangganan**
- [ ] Fase 1 (S1 sampai S3b): calon klien, tanpa login
- [ ] Fase 2 (S4 sampai S6a): keputusan owner
- [ ] Fase 3 (S7 sampai S10): calon klien menjadi klien
- [ ] Fase 4 (S11, S12): klien menyiapkan perusahaan, termasuk uji batas paket (cabang, pengguna, karyawan)
- [ ] Jalur lain: lead dari formulir minat, onboarding oleh owner, provision
- [ ] Tabel kasus negatif dan batas

**`02` Platform dan akun**
- [ ] §1 Provider, cabang, pengguna, peran, izin, lisensi
- [ ] §2 Paket, langganan, harga, modul, mitra
- [ ] §3 Template master data keuangan dan akuntansi
- [ ] §4 Template master data operasional, status, menu
- [ ] §5 Konten landing page
- [ ] §6 Terjemahan, bahasa, data acuan, lampiran, log
- [ ] §7 Dashboard platform, langganan, monitor notifikasi
- [ ] §8 Akun gateway platform dan kode kanal bank
- [ ] §9 Masuk ke aplikasi, pusat bantuan, riwayat perubahan
- [ ] §10 Pengaturan akun saya: tampilan, keamanan, langganan

> Catatan: bagian `02` yang khusus **platform owner** (§1 sampai §8) dijalankan dengan akun owner, bukan akun Dr. Rahmat. Akun Dr. Rahmat
> hanya relevan untuk §9 dan §10.

**`03` Konfigurasi umum dan master data**
- [ ] §1 Mata uang
- [ ] §2 Warehouse
- [ ] §3 Kategori dan satuan produk
- [ ] §4 Metode pembayaran dan tipe order
- [ ] §5 Fiscal year dan accounting period
- [ ] §6 Status setup
- [ ] §7 Permissions
- [ ] §8 App setup dan integration configs
- [ ] §9 Cost centers
- [ ] §10 Product catalog
- [ ] §11 Kontak (supplier dan customer)
- [ ] §12 User dan role
- [ ] §13 Pajak dan daftar harga
- [ ] §14 Manajemen cabang
- [ ] §15 Produk lanjutan: varian, modifier, resep
- [ ] §16 Cash register dan sales channel
- [ ] §17 Kurs mata uang per cabang
- [ ] §18 Pengaturan tampilan PDF
- [ ] §19 Denominasi uang dan deposit kasir
- [ ] §20 Pola transaksi
- [ ] §21 Tipe dokumen legal dan permintaan data pribadi
- [ ] §22 Tata letak menu dan log pribadi
- [ ] §23 Pergerakan stok

**`04` Inti, persetujuan, dan asisten AI**
- [ ] §1 Konfigurasi approval workflow lintas modul
- [ ] §2 Asisten AI in-app
- [ ] §3 Cara dapat API key AI provider
- [ ] §4 Memproses approval request (sisi approver)
- [ ] §5 Agen AI, aksi, mode tutorial, rangkaian, jadwal

### FASE B dan C. Transaksi dan modul

Tiap modul: kerjakan langkah `01` yang disebut, lalu baris modul. Kolom **Hubungan angka** adalah pemeriksaan lintas modul yang paling mudah terlewat.

**`05` Pembelian** (`01` langkah 6 sampai 10)
- [ ] §1 Konfigurasi alur purchasing
- [ ] §2 Purchase request
- [ ] §3 Purchase quotation
- [ ] §4 Purchase order
- [ ] §5 Goods receipt
- [ ] §6 Purchase invoice
- [ ] §7 Purchase payment bill
- [ ] §8 Purchase return
- [ ] §9 Verifikasi purchasing ke akuntansi
- [ ] §10 Tagihan biaya logistik (landed cost)
- [ ] §11 Blanket agreement
- [ ] §12 Konfigurasi biaya tambahan pembelian
- [ ] Hubungan angka: PO 16.650.000, stok OBT-001 = 2.000 dan OBT-002 = 1.000, utang usaha 27.750.000 setelah langkah 9

**`06` Persediaan** (`01` langkah 7, 11, 22)
- [ ] §1 Konfigurasi inventory
- [ ] §2 Stock adjustment
- [ ] §3 Stock transfer
- [ ] §4 Stock take (opname)
- [ ] §5 Stock lots dan serials
- [ ] §6 Consignment settlements
- [ ] Hubungan angka: transfer ke Bandung tidak mengubah nilai persediaan gabungan

**`07` Penjualan** (`01` langkah 12 sampai 14)
- [ ] §1 Konfigurasi alur sales
- [ ] §2 Quotation
- [ ] §3 Sales order
- [ ] §4 Sales delivery
- [ ] §5 Sales invoice
- [ ] §6 Sales payment bill
- [ ] §7 Sales return
- [ ] §8 Verifikasi sales ke akuntansi
- [ ] §9 Konfigurasi jurnal penjualan
- [ ] Hubungan angka: total 6.882.000, HPP 4.300.000, laba kotor 1.900.000, sisa piutang 2.882.000

**`08` Kanvasing** (`01` langkah 15, 16)
- [ ] §1 Wilayah dan rute
- [ ] §2 Target penjualan
- [ ] §3 Titipan stock sales
- [ ] §4 Kunjungan dan order lapangan
- [ ] §5 Penagihan lapangan
- [ ] §6 Competitor tracking
- [ ] §7 Kunjungan ke calon pelanggan
- [ ] §8 Konfigurasi canvassing

**`09` POS** (`01` langkah 17, 18)
- [ ] §1 Setup toko dan cash session
- [ ] §2 Transaksi penjualan
- [ ] §3 Void dan refund
- [ ] §4 Tutup cash session
- [ ] §5 Verifikasi POS ke akuntansi
- [ ] §6 Konfigurasi POS lanjutan
- [ ] §7 Diskon, promo, member tier, cashback
- [ ] Hubungan angka: stok OBT-001 Bandung 455 setelah retur 5 strip

**`10` Restoran** (`01` langkah 19)
- [ ] §1 Konfigurasi restoran
- [ ] §2 Menu dan kitchen routing
- [ ] §3 Pemesanan dan order meja
- [ ] §4 Kitchen display system dan order items
- [ ] §5 Reservasi meja
- [ ] §6 QR self-order

**`11` Manufaktur** (`01` langkah 21)
- [ ] §1 Konfigurasi manufaktur dan work center
- [ ] §2 Bill of materials
- [ ] §3 Routing produksi
- [ ] §4 Production order
- [ ] Hubungan angka: HPP Jamu Kunyit Asam 380 per sachet, biaya bahan 760.000 untuk 2 batch

**`12` Pertambangan** (`01` langkah 20)
- [ ] §1 Konfigurasi tambang
- [ ] §2 Parameter kualitas
- [ ] §3 Produksi dan hauling
- [ ] §4 Stockpile
- [ ] §5 Royalti
- [ ] §6 Rekonsiliasi survey

**`13` Sewa** (`01` langkah 23)
- [ ] §1 Konfigurasi alur rental
- [ ] §2 Rental assets
- [ ] §3 Rental quotation
- [ ] §4 Rental order
- [ ] §5 Usage entries
- [ ] §6 Rental invoice
- [ ] §7 Rental payment bill
- [ ] §8 Rental return
- [ ] §9 Verifikasi rental ke akuntansi
- [ ] Hubungan angka: sewa 315.000, deposit 300.000, deposit kembali 250.000 setelah denda 50.000

**`14` Akuntansi dan aset tetap** (`01` langkah 5, 27, 29)
- [ ] §1 Setup master data dan saldo awal
- [ ] §2 Jurnal manual
- [ ] §3 General ledger dan neraca saldo
- [ ] §5 Laporan keuangan
- [ ] §6 Anggaran
- [ ] §7 Aset tetap dan penyusutan (autoclave 60.000.000, penyusutan 1.000.000 per bulan)
- [ ] §8 Rekonsiliasi bank
- [ ] §9 Laporan pajak PPN
- [ ] §10 Chart of accounts: tree view, saldo akun, jenis jurnal
- [ ] §4 Tutup periode dan tahun fiskal (**dikerjakan paling akhir, Fase G**)

**`15` Keuangan** (`01` langkah 14, 28)
- [ ] §1 Kategori dan pencatatan biaya (biaya listrik 2.500.000 butuh persetujuan)
- [ ] §2 Pembayaran online, rute penyedia, penyelesaian dana (kunci **sandbox** saja)

**`16` SDM** (`01` langkah 24, 25)
- [ ] §1 Konfigurasi HRM
- [ ] §2 Struktur organisasi
- [ ] §3 Data karyawan
- [ ] §4 Rekrutmen
- [ ] §5 Absensi
- [ ] §6 Cuti
- [ ] §7 Komponen gaji
- [ ] §8 Referensi pajak dan BPJS
- [ ] §9 Proses payroll
- [ ] §10 Slip gaji karyawan
- [ ] §11 Mapping jurnal payroll
- [ ] §12 Komisi sales
- [ ] §13 Perubahan status karyawan
- [ ] §14 Log aktivitas, tipe aktivitas, kriteria KPI

**`17` Proyek dan tugas** (`01` langkah 26)
- [ ] §1 Pengaturan proyek, tipe tugas, label, peran
- [ ] §2 Proyek, tugas, dan tampilan
- [ ] §3 Catatan waktu, tarif, penagihan, alokasi
- [ ] §4 Integrasi Git (GitHub, GitLab)
- [ ] §5 Otomasi, webhook, portal klien, change request, tiket
- [ ] §6 Laporan, dasbor, logbook, asisten AI

### FASE D. Pelaporan

**`18` Dasbor**
- [ ] §1 Dashboard akuntansi, penjualan, pembelian, inventori
- [ ] §2 Dashboard POS, restoran, canvassing, manufaktur, pertambangan
- [ ] §3 Dashboard HRM, karyawan, pemakaian AI

**`19` Laporan**
- [ ] §1 Laporan lintas modul (cocokkan angka dengan daftar sumber)

**`20` Halaman publik** (tanpa login)
- [ ] §1 Pelamar, penawaran, restoran, pengiriman pemasok

### FASE E. Penutupan

**`01` Alur terpadu, bagian F dan hubungan angka**
- [ ] Langkah 29: rekonsiliasi bank dan persediaan, neraca saldo, laba rugi, neraca, arus kas, ringkasan pajak, anggaran vs aktual
- [ ] Langkah 30: dasbor, asisten AI (jawaban stok Paracetamol di Pusat = **800**), tautan publik
- [ ] Enam "Hubungan angka yang harus selalu benar" (persediaan = nilai stok, utang usaha = umur utang, piutang = umur piutang, PPN keluaran minus masukan = akun PPN, neraca saldo seimbang, kas fisik POS)

**`98` Izin, isolasi, paket, kasus batas**
- [ ] §1 Izin per peran
- [ ] §2 Isolasi antar klien dan antar cabang
- [ ] §3 Paket langganan dan fitur terkunci
- [ ] §4 Kasus batas angka
- [ ] §5 Pola tampilan di semua halaman transaksi
- [ ] §6 Bahasa dan teks

**`99` Peta cakupan**
- [ ] Setiap bab manual book punya jejak hasil uji (tidak ada bab yang belum disentuh)

### FASE F. Celah kebutuhan bisnis (`21`)

Bagian ini **sengaja** menguji hal yang mungkin belum ada. Hasilnya bahan prioritas pengembangan, bukan daftar bug.
Untuk setiap baris, catat salah satu: **Didukung penuh**, **Sebagian**, atau **Belum ada** (nomor celah G.. mengacu ke `95`).

- [ ] A. Obat: batch, kedaluwarsa, penarikan (`01` langkah 31 sampai 33)
- [ ] B. Obat terkontrol, resep, pelayanan apotek (langkah 34, 35)
- [ ] C. PBF dan distribusi (langkah 36)
- [ ] D. Klinik pratama dan laboratorium (langkah 38, 39)
- [ ] E. Produksi obat tradisional (langkah 40)
- [ ] F. Alat kesehatan dan sewa
- [ ] G. SDM tenaga kesehatan (langkah 37)
- [ ] H. Keuangan, pajak, grup
- [ ] I. Kepatuhan dan mutu

### FASE G. Berisiko (kerjakan terakhir)

Mengubah status langganan atau mengunci periode. Jangan dikerjakan sebelum semua fase lain selesai.

- [ ] `00a` S13: klien minta ganti paket atau add-on
- [ ] `00a` S14: owner ganti paket (turun di bawah pemakaian harus ditolak dengan rincian batas)
- [ ] `00a` S15: tagihan periode berikutnya terbit (jalankan job harian)
- [ ] `00a` S16: tunggakan menjadi Past due lalu Suspended (data tidak hilang, login ditolak)
- [ ] `00a` S17: pembayaran tunggakan memulihkan akses
- [ ] `00a` S18: berhenti berlangganan dan reaktivasi
- [ ] `00a` S19, S20: dashboard langganan, rekap mitra
- [ ] `00a` mode produksi `on_payment` (P1 sampai P4), lalu kembalikan setelan
- [ ] `14` §4: tutup periode Oktober dan tahun fiskal

---

## 5. Aturan lintas modul yang harus dicek di SETIAP halaman

Ini dari `98` §5 dan standar proyek. Cukup dicek sekilas di setiap halaman baru yang dibuka, jangan menunggu `98`.

- [ ] Tombol aksi yang tidak boleh dipakai **terlihat tetapi nonaktif dengan tooltip alasan**, bukan hilang
- [ ] Halaman transaksi berupa **halaman terpisah**, bukan modal; simpan lewat konfirmasi dulu
- [ ] Setelah membuat dokumen, aplikasi pindah ke **halaman detail**, bukan kembali ke daftar
- [ ] Ada tombol **Refresh** di halaman daftar dan detail
- [ ] Spinner saat memuat; daftar memakai tabel standar dengan keadaan kosong yang wajar
- [ ] Teks tampil dalam bahasa yang dipilih (ganti ke Inggris dan cek ada teks yang tidak ikut berubah)
- [ ] Nomor dokumen memakai awalan dari pengaturan cabang
- [ ] Uang memakai input mata uang; jumlah memakai format qty yang sama di semua halaman
- [ ] Tidak ada error di console browser saat membuka halaman (buka DevTools sekali di awal)

---

## 6. Catatan temuan (isi sambil menguji)

Salin baris ini untuk tiap temuan. Satu baris, satu masalah.

| ID | File dan kasus | Yang dilakukan | Hasil yang diharapkan | Hasil di layar | Tingkat | Status |
| --- | --- | --- | --- | --- | --- | --- |
| T-001 | contoh: `05` §6 faktur | bayar lebih dari sisa | ditolak | diterima | Tinggi | Baru |

**Tingkat:** Kritis (data salah atau bocor, angka jurnal salah), Tinggi (fitur utama tidak jalan), Sedang (jalan tapi membingungkan atau salah pesan),
Rendah (kosmetik, teks), Celah (fitur memang belum ada, masuk register `95`).
**Status:** Baru, Dianalisis, Diperbaiki, Diverifikasi ulang, Ditutup, Bukan bug.

---

## 7. Setelah selesai

1. Isi centang di bagian 4; semua kotak yang masih kosong harus punya alasan tertulis (ditunda, tidak berlaku, bergantung celah).
2. Pindahkan temuan jenis **Celah** ke `95-daftar-celah-dan-usulan-perbaikan.id.md` bila belum terdaftar.
3. Cocokkan dengan `99-peta-cakupan.id.md`: tidak boleh ada bab manual book tanpa jejak uji.
4. Kembalikan setelan uji: `subscription_self_service_activation` kembali ke `on_payment`, dan bersihkan atau arsipkan data uji sesuai
   bagian "Netralisasi" di `00a` dan `01`.

---

## Peta file

| File | Isi |
| --- | --- |
| `00` | Profil perusahaan, cabang, peran, data acuan, urutan kerja |
| `00b` | **Tipe akun dan 40 akun acuan**, saldo awal, penghubung akun ke modul, kasus uji data akun |
| `00a` | Perjalanan berlangganan klien (titik awal) |
| `01` | Alur bisnis terpadu, 40 langkah dengan angka acuan |
| `02` sampai `04` | Platform, konfigurasi umum, persetujuan, AI |
| `05` sampai `07` | Pembelian, persediaan, penjualan |
| `08` sampai `10` | Kanvasing, POS, restoran |
| `11` sampai `13` | Manufaktur, pertambangan, sewa |
| `14` sampai `17` | Akuntansi, keuangan, SDM, proyek |
| `18` sampai `20` | Dasbor, laporan, halaman publik |
| `21` | Kebutuhan bisnis kesehatan dan uji celah |
| `95` | Daftar celah dan usulan perbaikan |
| `96`, `97` | Riset bisnis dan referensi Odoo (bacaan, tidak diuji) |
| `98` | Izin, isolasi, paket, kasus batas |
| `99` | Peta cakupan bab manual book |
