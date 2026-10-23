Kamu bekerja di repo Laravel "erpApiServices" (backend ERP multi-tenant, PostgreSQL, Pest). Tugasmu: menulis tes Pest untuk modul **{{MODUL}}** dari dokumen uji, untuk celah yang belum tercakup. Dokumen dan komentar dalam Bahasa Indonesia; kode dan nama tes mengikuti gaya yang sudah ada.

ATURAN KERAS
- Jangan menyentuh produksi. Repo tidak membawa .env; pakai HANYA database lokal `erp_test` (tests/TestCase.php memang menolak yang lain).
- Branch kerja: `test/{{SLUG}}`. Jangan push ke `main`. Jangan mengubah kode aplikasi (app/, routes/, database/migrations): bila tes menemukan bug, JANGAN diperbaiki; tulis di laporan dan tandai tesnya dengan `->todo()` atau `->skip('bug: ...')` plus penjelasan.
- Jangan menjalankan seluruh suite. Jalankan hanya berkas tesmu dan paling banyak dua berkas tes lama sebagai pembanding.
- Bila macet lebih dari tiga percobaan pada hal yang sama, BERHENTI dan laporkan.
- Jangan menulis ulang tes yang sudah ada. Baca dulu tests/Feature untuk modul ini (cari nama berkas dan isi) dan hanya tambahkan yang belum ada.

LANGKAH 1: LINGKUNGAN
VM ini Ubuntu 24.04 (PHP 8.3, Composer, PostgreSQL 16 sudah terpasang, belum menyala). `service postgresql start`; sandi postgres `postgres`; buat database `erp_test` bila belum ada. `cp .env.testing.example .env.testing` (DB_PASSWORD=postgres), `composer install --no-interaction`, lalu migrate dan db:seed ke erp_test dengan variabel lingkungan DB_* yang menimpa seperti di tests/README.md.

LANGKAH 2: BACA ACUAN
- Pola tes yang benar: baca tests/README.md, tests/Support/Tenants.php, dan satu tes alur yang mirip (mis. tests/Feature/PurchasingFlowTest.php atau SalesFlowTest.php). Pakai pola yang sama: tes berjalan lewat router asli (postJson ke /api/...), pengguna dan cabang dari helper Tenants, setiap tes dibungkus transaksi.
- Dokumen uji untuk modul ini: coba `git clone https://github.com/taufit23/Testing-Cases-ERP.git /tmp/cases` dan baca `/tmp/cases/sehat-sentosa-farma/{{FILE_DOKUMEN}}` serta langkah {{LANGKAH_01}} di `/tmp/cases/sehat-sentosa-farma/01-alur-bisnis-terpadu-lintas-modul.id.md`. Bila clone gagal (tidak ada akses), BERHENTI dan laporkan; jangan mengarang isi dokumennya.

LANGKAH 3: TULIS TES
1. Pilih baris dokumen yang bisa diuji lewat HTTP: jalur Positif, Negatif (harus ditolak dengan pesan jelas, bukan error server), aturan tegas manual, dan "peran tanpa izin harus 403". Abaikan baris berlabel "(draf)" yang tidak masuk akal terhadap kode; catat alasannya.
2. Untuk angka acuan di file 01 (mis. total PO 16.650.000, HPP 4.300.000), tegaskan HUBUNGAN angka (stok bertambah sebesar qty diterima, utang usaha sama dengan faktur belum lunas, jurnal seimbang), bukan hanya satu angka; angka mutlak hanya bila data tes persis sama dengan data acuan.
3. Satu berkas: `tests/Feature/{{NAMA_BERKAS}}Test.php`. Nama fungsi pembantu harus unik (awali dengan nama modul) supaya tidak bentrok dengan berkas tes lain yang dimuat bersamaan.
4. Jalankan berkasmu sampai hijau (kecuali yang sengaja ditandai bug).

LANGKAH 4: LAPORAN
Tulis docs/laporan-tes-{{SLUG}}.id.md: tabel baris dokumen yang diuji (nomor atau judul), nama tes, hasil (lulus, bug, tidak berlaku) dan alasan; daftar bug yang ditemukan dengan langkah reproduksi; baris dokumen yang tidak bisa diuji lewat HTTP dan kenapa. Commit di branch `test/{{SLUG}}` dan push branch itu. Balas dengan ringkasan satu paragraf dan jumlah tes lulus, bug, dan dilewati.
