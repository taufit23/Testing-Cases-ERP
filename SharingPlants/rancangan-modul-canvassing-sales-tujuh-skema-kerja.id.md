# Rancangan Modul Canvassing Sales: Memenuhi Tujuh Cara Kerja Sales Lapangan

Panduan umum untuk tim yang membangun atau menilai fitur kunjungan sales lapangan (canvassing) pada sistem ERP atau CRM.
Isinya konsep, hasil riset dari sumber publik, dan usulan rancangan. Tidak menyebut produk, perusahaan, atau data pihak tertentu.

## 1. Intinya

Satu hal paling penting dalam canvassing bukan wilayah, melainkan **siapa pemilik prospek dan pelanggan**.
Wilayah bisa digambar ulang dan target bisa berubah tiap bulan. Tetapi kalau pemilik prospek atau pelanggan tidak jelas,
ujungnya sales saling rebut hasil kunjungan.

Karena itu rancangan ini berpegang pada empat hal:

1. **Kepemilikan jadi pusat.** Setiap perubahan pemilik tercatat, ada aturan siapa boleh memindahkan, dan data ganda dicegah.
2. **Cara kerja dipilih lewat pengaturan,** bukan dikunci. Perusahaan memilih cara yang cocok, dan bisa berbeda untuk tiap sales.
3. **Tidak terlalu ketat, tidak terlalu longgar.** Bawaannya memberi peringatan; larangan keras dipilih sendiri oleh perusahaan.
4. **Aturan yang sama di mana pun.** Aturan kepemilikan berlaku sama dari layar mana pun data dimasukkan.

## 2. Tujuh cara kerja sales

| # | Cara kerja | Maksudnya | Cocok untuk |
| --- | --- | --- | --- |
| 1 | **Per wilayah** | Atasan menentukan area; sales hanya bekerja di areanya | Distribusi, barang konsumsi |
| 2 | **Per target (bebas)** | Sales bebas ke mana saja; yang dinilai target: jumlah kunjungan, prospek baru, omzet. Perlu lokasi GPS dan kejelasan pemilik prospek | Mengejar pelanggan baru |
| 3 | **Gabungan wilayah dan target** | Punya wilayah utama dan target; boleh ke wilayah lain dengan aturan | Paling fleksibel, paling banyak dipakai |
| 4 | **Per rute** | Yang ditentukan adalah rute kunjungan, mis. Senin toko A, B, C; Selasa toko D, E | Pelanggan tetap |
| 5 | **Per kelompok pelanggan** | Dibagi menurut jenis pelanggan, bukan lokasi: industri, sekolah, rumah sakit, ritel | Menjual ke segmen tertentu |
| 6 | **Pelanggan punya pemilik tetap** | Setiap pelanggan dipegang satu sales, walau lokasinya berubah | Penjualan antarperusahaan dan proyek |
| 7 | **Rebutan lead lewat kumpulan bersama** | Lead masuk ke satu kumpulan; sales bebas mengambil; yang sudah diambil terkunci atas nama pengambilnya | Tim dengan lead dari banyak sumber |

Yang minimal harus ada: pembagian wilayah, pembagian target, laporan kunjungan, absen lokasi (GPS), kepemilikan prospek, dan perencanaan
rute (boleh menyusul).

## 3. Masalah yang sering muncul

Berdasarkan pola umum, bukan temuan atas sistem tertentu. Bisa dipakai sebagai daftar periksa.

| Bidang | Masalah yang sering terjadi |
| --- | --- |
| Wilayah | Kunjungan di luar wilayah hanya memunculkan pemberitahuan, tidak bisa dilarang. Wilayah prospek diisi manual. Wilayah dua sales bisa saling tumpang-tindih tanpa ada yang menyadari |
| Target | Hanya omzet dan jumlah barang. Tidak ada target jumlah kunjungan, prospek baru, pelanggan baru, atau penagihan |
| Gabungan | Tidak ada konsep "wilayah utama boleh meluas dengan aturan"; kunjungan di luar wilayah tidak ditandai |
| Rute | Kunjungan di luar rute tidak ditandai. Tidak ada ukuran seberapa patuh sales pada rutenya |
| Kelompok pelanggan | Tidak ada daftar kelompok pelanggan, pembagian sales per kelompok, atau target per kelompok |
| Kepemilikan | Pemilik bisa diganti begitu saja tanpa catatan dan alasan. Data ganda tidak dicegah. Pemilik hilang saat prospek berubah jadi pelanggan. Sales bisa mengunjungi pelanggan milik sales lain tanpa tanda. Pemilik yang sudah tidak aktif tidak pernah dilepas |
| Kumpulan lead | Tidak ada cara mengambil lead, batas jumlah, batas waktu, atau pengembalian lead yang terbengkalai |
| Data ganda antarfitur | Satu calon pelanggan bisa tercatat di beberapa tempat dengan pemilik berbeda |

## 4. Riset dari sumber publik

Sebagian besar sumber adalah blog perusahaan penyedia aplikasi atau konsultan. Angka-angkanya patut dipakai sebagai contoh, bukan standar.

### 4.1 Pembagian wilayah dan kepemilikan pelanggan
- Ada tiga cara membagi wilayah: **menurut peta**, **menurut daftar pelanggan tertentu**, dan **gabungan keduanya**. Gabungan paling fleksibel,
  tetapi butuh aturan main tertulis supaya sales tahu mana yang menjadi miliknya.
  ([Spotio](https://spotio.com/blog/sales-territory-design/), [Pedowitz Group](https://www.pedowitzgroup.com/whats-the-best-territory-planning-approach))
- Rebutan dicegah dengan pemilik utama yang jelas, aturan khusus untuk pelanggan di perbatasan wilayah, pengecekan data ganda otomatis, dan
  kebijakan tertulis soal pemindahan pelanggan.
  ([Traction Complete](https://tractioncomplete.com/articles/salesforce-territory-management-best-practices/))
- Sebaiknya aturan diumumkan lebih dulu, perubahan wilayah diberi masa persiapan (satu sumber menyebut 30 hari), dan ada jalur keberatan.
- Cek data ganda dipasang sebelum data masuk. Lead yang kembali sebaiknya diberikan ke sales yang dulu menanganinya, dan selalu ada jalur
  cadangan untuk lead yang tidak cocok dengan aturan mana pun.
  ([LeadAngel](https://www.leadangel.com/blog/operations/lead-routing-salesforce/), [Kubaru](https://kubaru.io/blog/salesforce-assignment-rules/))

### 4.2 Kumpulan lead bersama
- Biasanya ada **batas jumlah lead** yang boleh diambil (contoh dari sumber: 10 sampai 20 per hari, atau berhenti bila sudah memegang 25 lead
  yang belum selesai), **batas waktu** (lead yang tidak disentuh dikembalikan), dan **pengembalian bertahap** untuk lead yang lama diam
  (contoh: 7 hari ke tahap perawatan, 14 hari ke kumpulan daur ulang, 30 hari diarsipkan). Kepemilikan baru berpindah saat lead diambil.
  ([Rework](https://resources.rework.com/libraries/lead-management/lead-pool-management),
  [Sierra Interactive](https://help.sierrainteractive.com/helpcenter/setting-up-and-managing-sierra-lead-ponds-manager-guide),
  [MyPhoner](https://myphoner.help/en/articles/9177509-manage-lead-recycling))

### 4.3 Rute kunjungan dan ukuran kinerja
- Rencana kunjungan menetapkan siklus datang ke tiap toko; seberapa sering bisa dibedakan menurut kelas toko. Kepatuhan pada rute harus
  diukur, karena tanpa itu rute nyata cepat menyimpang dari rencana.
  ([BeatRoute](https://beatroute.io/platform/visit-planning-software/), [HelloGrowth](https://hellogrowthcrm.com/blog/beat-planning-guide-fmcg))
- Ukuran yang lazim dipakai:
  - ***Strike rate***: berapa persen kunjungan yang menghasilkan pesanan (contoh patokan 60 sampai 75%).
  - **Cakupan toko**: berapa persen toko yang sudah dikunjungi dalam satu periode.
  - **Cakupan efektif**: kunjungan terencana ke toko prioritas dibanding jumlah toko prioritas.
  - **Kunjungan yang berhasil**: jumlah kunjungan yang berujung transaksi.

  Cakupan menunjukkan arah lebih awal; pencapaian target adalah hasil akhirnya.
  ([Massist](https://blog.massistcrm.com/10-kpis-every-fmcg-sales-manager-must-track-with-benchmarks), [FieldAssist](https://fieldassist.in/blog/6-fmcg-sales-metrics-to-track))
- Tidak ditemukan sumber khusus tentang praktik distributor di Indonesia soal kunjungan di luar rute, dan tidak ada ukuran baku untuk
  "toko baru". Keduanya perlu dibicarakan dengan pengguna. Sebagai awal cukup dihitung berapa toko baru aktif per bulan.

## 5. Rancangan

### 5.1 Pengaturan cara kerja sales

Satu pengaturan untuk satu perusahaan atau cabang, yang bisa diganti untuk sales tertentu:

| Yang diatur | Pilihan | Saran awal | Untuk cara kerja nomor |
| --- | --- | --- | --- |
| Kalau sales kerja di luar wilayah | diabaikan, diberi peringatan, dilarang | diberi peringatan | 1, 3 |
| Boleh mengunjungi siapa | hanya miliknya dan wilayahnya; boleh di luar tetapi ditandai; bebas | boleh di luar tetapi ditandai | 1, 2, 3 |
| Tindakan bila di luar wilayah | diizinkan, manajer diberi tahu, perlu persetujuan | manajer diberi tahu | 3 |
| Kunjungan harus sesuai rute | tidak, diberi peringatan, dilarang | tidak | 4 |
| Aturan kepemilikan | ketat (satu pemilik, pindah harus disetujui), siapa cepat dia dapat, atau bersama (pemilik utama dan pendukung) | ketat | 6 |
| Kumpulan lead bersama | dipakai atau tidak, batas ambil, batas waktu, aturan daur ulang | tidak dipakai | 7 |
| Pembagian sales per kelompok pelanggan | dipakai atau tidak | tidak dipakai | 5 |

Satu cara kerja dibentuk dengan menggabungkan beberapa pilihan, bukan satu tombol saja. Contoh: **per wilayah** = hanya boleh mengunjungi
miliknya + dilarang di luar wilayah. **Bebas** = bebas mengunjungi + siapa cepat dia dapat. **Gabungan** = boleh di luar tetapi ditandai +
manajer diberi tahu. Sediakan juga **paket pilihan siap pakai** untuk tujuh cara kerja ini, supaya admin cukup memilih nama.

### 5.2 Aturan kepemilikan (bagian terpenting)

Setiap perubahan pemilik dicatat: siapa, dari siapa ke siapa, kapan, apa alasannya, dan siapa yang menyetujui bila perlu.

1. **Satu pemilik utama** untuk setiap prospek dan pelanggan; pada mode bersama ada pendukung.
2. **Terkunci.** Sales lain tidak bisa mendaftarkan data ganda atau mengganti pemilik lewat ubah data biasa. Pemilik hanya bisa dipindah
   lewat menu pemindahan khusus.
3. **Pemindahan** butuh izin dan alasan, dan bisa disertai persetujuan bila perusahaan menghendaki.
4. **Cek data ganda saat memasukkan data** (prospek baru, pelanggan baru dari lapangan, impor). Cocokkan nomor telepon, nama, dan kedekatan
   lokasi. Hasilnya: ditolak, atau muncul pesan "sudah dimiliki oleh si A" dengan tombol minta pemindahan. Pelanggan di perbatasan diputuskan manajer.
5. **Pemilik yang lama tidak aktif dilepas.** Bila selama sekian hari tidak ada kegiatan, pemilik diberi peringatan dulu, lalu dilepas ke
   kumpulan bersama. Jumlah harinya ditetapkan tiap perusahaan.
6. **Pemilik ikut berpindah** saat prospek menjadi pelanggan dan saat pelanggan didaftarkan cepat di lapangan.
7. **Satu calon pelanggan, satu catatan,** walau tersebar di beberapa fitur, dengan pengecekan data ganda di antaranya.
8. **Kunjungan ke pelanggan milik sales lain** tunduk pada aturan kepemilikan. Hasil penjualan tetap atas nama pemilik kecuali kebijakan
   menentukan lain (mis. kredit dibagi).
9. **Perubahan wilayah diumumkan lebih dulu** dan berlaku mulai tanggal yang ditentukan.

### 5.3 Kumpulan lead bersama

- Lead tanpa pemilik masuk ke kumpulan (dari impor, formulir di situs, atau lead yang dilepas).
- Kalau dua sales menekan "ambil" bersamaan, hanya satu yang berhasil.
- Yang bisa diatur: batas ambil per hari, batas lead yang belum selesai per sales, batas waktu setelah diambil, dan prioritas lead di wilayah sendiri.
- Setelah diambil, lead terkunci dan tercatat siapa pengambilnya.

### 5.4 Target yang lebih lengkap

Selain omzet dan jumlah barang: jumlah kunjungan, prospek baru, pelanggan baru, penagihan, dan *strike rate*. Target bisa dipasang untuk
sales, wilayah, atau kelompok pelanggan. Pencapaian dihitung otomatis dari data yang sudah ada, dan tampil berdampingan dengan target.

### 5.5 Kelompok pelanggan

Daftar kelompok pelanggan per perusahaan (industri, sekolah, rumah sakit, ritel, dan seterusnya) yang menempel pada pelanggan dan prospek,
pembagian sales per kelompok dengan tanggal berlaku, target per kelompok, dan penyaring kelompok di daftar prospek, rute, dan laporan. Bisa
digabung dengan pembagian wilayah.

### 5.6 Rute dan ukuran kepatuhan

Tandai kunjungan di luar rute, dan tampilkan *strike rate*, cakupan toko, cakupan efektif, dan kunjungan yang berhasil. Tambahan yang
opsional: usulan urutan kunjungan menurut jarak.

### 5.7 Wilayah terisi otomatis

Saat prospek dibuat di lapangan, wilayahnya diisi dari lokasi GPS, dan muncul peringatan bila lokasinya ternyata masuk wilayah sales lain.

## 6. Tahapan kerja

| Tahap | Isi | Catatan |
| --- | --- | --- |
| 0 | Cek sisa dugaan pada sistem yang ada: apakah pemilik ikut berpindah, siapa yang dapat kredit penjualan, layar mana yang masih bisa mengganti pemilik | Hanya memeriksa, singkat |
| 1 | **Aturan kepemilikan:** pencatatan perubahan, menu pemindahan, penguncian, pemilik ikut berpindah, cek data ganda | Paling penting |
| 2 | **Pengaturan cara kerja sales** dan paket pilihan untuk tujuh cara kerja; penanganan kerja di luar wilayah | Cara kerja 1, 2, 3 |
| 3 | **Kumpulan lead bersama** dengan batas ambil, batas waktu, dan pengembalian | Cara kerja 7 |
| 4 | **Target yang lebih lengkap** dan laporan pencapaian | Cara kerja 2, 3 |
| 5 | **Kelompok pelanggan** | Cara kerja 5 |
| 6 | Rute: tanda di luar rute dan ukuran kepatuhan | Cara kerja 4 |
| 7 | Satu catatan untuk satu calon pelanggan di semua fitur | Menutup tumpang-tindih |
| 8 | Wilayah terisi otomatis, laporan konflik kepemilikan, pelepasan otomatis | Penyempurnaan |

Tahap 1 didahulukan karena yang lain bergantung padanya. Tanpa kepemilikan yang tegas, wilayah, target, dan kumpulan lead hanya
memindahkan rebutan ke tempat lain.

## 7. Hal yang perlu diwaspadai

- Menutup cara mengganti pemilik lewat ubah data biasa bisa memengaruhi layar lain yang selama ini memakainya. Periksa dulu semuanya.
- Data lama: prospek dan pelanggan dengan pemilik ganda atau kosong perlu dirapikan sekali sebelum penguncian berlaku.
- Angka batas hari dan batas ambil di sumber hanya contoh; tentukan bersama pengguna.
- Aturan untuk pelanggan di perbatasan dan pembagian kredit penjualan adalah keputusan bisnis, jadi sebaiknya bisa diatur, bukan dikunci.
- Sumber riset sebagian besar blog penyedia aplikasi; angkanya aturan praktis.
