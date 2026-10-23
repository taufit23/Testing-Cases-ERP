Kamu bekerja di repo Laravel "erpApiServices" (backend ERP multi-tenant, PostgreSQL, Pest). Tugas sesi percontohan ini ada dua: (1) membuktikan suite tes bisa jalan di VM cloud ini, (2) memetakan modul yang belum punya tes. Tulis semua dokumen dalam Bahasa Indonesia.

ATURAN KERAS
- Jangan menyentuh produksi atau kredensial apa pun. Repo ini tidak membawa .env; pakai HANYA database lokal `erp_test`.
- Jangan push ke branch `main`. Kerjakan di branch baru bernama `test/peta-celah` dan hanya push branch itu.
- Jangan mengubah kode aplikasi (app/, routes/, database/migrations). Satu-satunya berkas yang boleh kamu tambah adalah docs/peta-celah-tes.id.md.
- Jangan menjalankan seluruh suite (bisa sangat lama dan mengunci database). Jalankan tes per berkas saja, dan batasi diri ke tiga berkas tes sebagai bukti.
- Bila Postgres tidak bisa dinyalakan atau composer install gagal, BERHENTI dan laporkan penyebab persisnya; jangan mencari jalan memutar yang berisiko.

LANGKAH 1: SIAPKAN LINGKUNGAN
1. Baca tests/README.md (cara menyiapkan database tes). VM ini Ubuntu 24.04 dan sudah memiliki PHP 8.3, Composer, dan PostgreSQL 16 (belum menyala).
2. `service postgresql start`, lalu pastikan user postgres berkata sandi `postgres` dan database `erp_test` ada: `su postgres -c "psql -c \"ALTER USER postgres PASSWORD 'postgres'\""` dan `su postgres -c "createdb erp_test"` bila belum ada.
3. `cp .env.testing.example .env.testing`, isi DB_PASSWORD=postgres. Jalankan `composer install --no-interaction`. Bila ekstensi PHP yang dibutuhkan kurang (pgsql, mbstring, bcmath, gd, dll.), pasang dengan apt.
4. Migrasi dan seed ke erp_test dengan variabel lingkungan yang menimpa (sesuai tests/README.md): DB_CONNECTION=pgsql DB_HOST=127.0.0.1 DB_PORT=5432 DB_USERNAME=postgres DB_PASSWORD=postgres DB_DATABASE=erp_test php artisan migrate --force lalu db:seed --force. Catat berapa lama tiap langkah dan apakah ada error.
5. Jalankan tiga berkas tes yang sudah ada sebagai bukti, satu per satu: `vendor/bin/pest tests/Feature/SalesFlowTest.php`, `vendor/bin/pest tests/Feature/PurchasingFlowTest.php`, `vendor/bin/pest tests/Feature/AiUiControlTest.php`. Catat hasil (lulus atau gagal, jumlah tes, durasi). Bila ada yang gagal, catat pesan galat dan penyebab yang kamu duga (apakah masalah lingkungan atau masalah kode); jangan memperbaiki kode.

LANGKAH 2: PETA CELAH TES
Tujuan: daftar modul yang tidak (atau hampir tidak) tercakup tes. Caranya tanpa menjalankan tes:
1. Daftar semua rute API berubah-data (POST/PUT/DELETE) dari routes/*.php, dikelompokkan per modul (segmen pertama setelah api/, mis. sales, purchasing, inventory, accounting, hrm, pos, restaurant, manufacturing, mining, rental, canvassing, projects, finance, fixed-assets, partnerships, client-master, core).
2. Untuk tiap modul, hitung berapa rute yang URI-nya (atau nama controller-nya) muncul di tests/Feature/*.php. Ini perkiraan kasar lewat pencarian teks, bukan coverage sungguhan; katakan begitu.
3. Untuk tiap modul tulis: jumlah rute, jumlah rute yang tersentuh tes, daftar berkas tes yang menyentuhnya, dan 5 sampai 10 rute penting yang belum tersentuh sama sekali (prioritaskan yang menyentuh uang, stok, jurnal, persetujuan, atau data lintas-cabang).
4. Urutkan modul dari yang paling tidak tercakup. Beri rekomendasi 8 modul teratas untuk ditulis tesnya, dengan alasan satu kalimat tiap modul.

LANGKAH 3: LAPORAN
Tulis docs/peta-celah-tes.id.md berisi: (a) hasil bukti lingkungan (langkah 1), termasuk waktu dan kendala, (b) tabel peta celah per modul, (c) rekomendasi 8 modul. Commit di branch test/peta-celah dan push branch itu. Lalu balas dengan ringkasan: apakah lingkungan berhasil (ya atau tidak, plus kendala), tiga hasil tes, dan 8 modul teratas.
