---
title: (PT Sehat Sentosa Farma) — 00a. Perjalanan Berlangganan Klien (Titik Awal Suite)
category: sehat-sentosa-farma
description: Suite dimulai dari calon klien yang berlangganan sendiri lewat halaman pendaftaran (/subscribe), memilih paket dan layanan, lalu pemilik platform menyetujui dan langganan dimulai. Mode uji menjadikan persetujuan sebagai pengganti pembayaran. Memuat juga jalur lead lama, penagihan berkala, ganti paket, penangguhan, dan berhenti.
visibility: internal
---

# 00a. Perjalanan Berlangganan Klien

> **Titik awal suite ini.** PT Sehat Sentosa Farma **belum ada** di aplikasi. Yang ada hanya platform (landing page, paket langganan, akun platform owner) dan seorang calon klien:
> **Dr. Rahmat Hidayat**, direktur, yang ingin memakai aplikasi untuk grupnya. Semua data perusahaan di file `00` lahir dari alur ini, bukan dimasukkan lebih dulu oleh admin.
>
> **Aktor:** *Calon klien* (belum login), *Platform Owner* (pemilik aplikasi), *Klien* (Dr. Rahmat setelah punya akun), *Mitra* (reseller, opsional).
>
> **Pendaftaran mandiri sudah ada (2026-10-20).** Calon klien membuka `/subscribe`, memilih paket (dan modul tambahan), mengisi perusahaan dan akunnya (termasuk kata sandi pilihan sendiri), lalu mengirim pengajuan.
> **Tidak ada yang terbentuk sebelum pemilik platform menyetujui.** Manual: `erpApiServices/docs/manualBook/platform-owner/09-pendaftaran-mandiri-klien.md`.
>
> **Mode uji (yang dipakai suite ini).** Pengaturan platform `subscription_self_service_activation` bernilai **`on_approval`**: saat pemilik platform menyetujui, tagihan pertama langsung ditandai lunas
> (metode "lain", referensi `approved-by-platform-owner`) sehingga **langganan aktif seketika**, tanpa membayar. Di produksi nilainya `on_payment` (bawaan): persetujuan membuat perusahaan, lalu langganan mulai
> dengan uji coba atau **menunggu pembayaran** tagihan pertama. Bagian "Mode produksi" di bawah menguji jalur pembayaran sungguhan.
>
> **Prasyarat teknis:** database uji; satu akun platform owner; paket langganan uji **"Paket Grup Kesehatan"** yang aktif dan publik (paket modul berisi Pembelian, Persediaan, Penjualan, Kanvasing, POS, Restoran,
> Manufaktur, Pertambangan, Sewa, Akuntansi, Keuangan, Aset Tetap, SDM, Proyek; batas 5 cabang, 20 pengguna, 50 karyawan; uji coba 14 hari; harga bulanan dan tahunan) dan satu paket pembanding yang lebih kecil;
> `subscription_self_service_enabled` = benar. Untuk jalur pembayaran: akun gateway platform sandbox (panduan: `erpApiServices/docs/panduan-uji-kredensial-pembayaran.id.md`).
> Email otomatis belum aktif (SMTP ditahan, celah **G37** di [`95`](./95-daftar-celah-dan-usulan-perbaikan.id.md)): calon klien mengikuti perkembangan dari halaman status.

## Fase 1. Calon klien menemukan dan memilih (tanpa login)

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S1 | Calon klien | Buka halaman depan: banner, fitur, modul, harga, testimoni, FAQ, profil | Semua bagian tampil sesuai pengaturan landing; bagian tersembunyi tidak tampil; tombol **Mulai Berlangganan** ada di navbar (desktop dan menu seluler) | Landing berjalan tanpa login; tidak ada data internal; judul dan meta halaman terisi, peta situs dan robots tersedia |
| S2 | Calon klien | Klik **Mulai Berlangganan** (atau buka `/subscribe?plan=<slug>`) | Halaman pendaftaran tampil dengan paket aktif dan publik: harga bulanan atau tahunan (ada pengalih siklus), masa uji coba, batas cabang, pengguna, karyawan, dan modul yang termasuk; paket dari tautan terpilih otomatis | Paket nonaktif atau tidak publik tidak tampil; paket tanpa harga siklus itu ditolak saat kirim; bila pendaftaran mandiri dimatikan, halaman menyatakan tidak tersedia |
| S3 | Calon klien | Pilih **Paket Grup Kesehatan**, siklus bulanan; **tidak** memilih uji coba; tambah modul tambahan yang belum ada di paket; isi perusahaan "PT Sehat Sentosa Farma", kontak Dr. Rahmat, telepon, cabang pertama "Kantor Pusat & Distribusi Jakarta", kata sandi pilihan sendiri; centang persetujuan; **Kirim Pengajuan** | Berpindah ke halaman **status** berisi nomor ONB, perusahaan, paket, dan "Menunggu persetujuan"; halaman menyegarkan diri tiap 15 detik | Modul yang sudah termasuk paket tidak muncul sebagai tambahan; uji coba hanya bisa dicentang bila paket menyediakannya; tombol kirim nonaktif sampai kolom wajib, kata sandi sama, dan persetujuan terpenuhi |
| S3a | Calon klien | Kasus negatif pengajuan | Ditolak dengan pesan per kolom, tanpa membuat data | Email kontak sudah terdaftar sebagai perusahaan atau pengguna, atau sudah ada pengajuan tertunda dengan email sama: ditolak; kata sandi kurang dari 8 atau tidak sama: ditolak; persetujuan tidak dicentang: ditolak; telepon bukan angka: ditolak; kolom jebakan terisi: dijawab seperti sukses tetapi tidak menyimpan apa pun; lebih dari 5 pengajuan per menit: dibatasi |
| S3b | Calon klien | Buka halaman status dengan token salah atau tanpa token | Pesan "pengajuan tidak ditemukan" dan tautan membuat pengajuan baru | Token tidak dapat ditebak; tidak membocorkan jenis onboarding lain |

## Fase 2. Pemilik platform memutuskan (mode uji: persetujuan = langganan dimulai)

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S4 | Owner | Buka **Core → Subscriptions → Onboarding**: pengajuan tampil dengan label **Pengajuan mandiri** dan tahap **Persetujuan** | Daftar memuat nomor, perusahaan, paket, sumber, tahap, kemajuan; baris pengajuan baru bertanda menunggu | Hanya platform owner melihat halaman ini; peran lain 403; lead Qualified dari pengajuan terlihat di Landing Leads |
| S4a | Owner | Buka detail: paket, siklus, modul tambahan, data perusahaan dan akun | Data sama dengan yang dikirim; **kata sandi tidak terlihat** | Tombol **Provision** nonaktif dengan tooltip "pengajuan mandiri dibuat dengan menyetujuinya" |
| S5 | Owner | Klik **Setujui pengajuan**, konfirmasi | Dalam **satu transaksi** terbentuk: provider, cabang pertama (menjadi cabang utama), akun utama dengan kata sandi pilihan calon klien, peran awal dengan izin klien saja, langganan. Mode uji: tagihan pertama **lunas** dan langganan **Active** seketika; tahap persetujuan, provisioned, dan kredensial selesai | Langganan Active (bukan Awaiting payment); tagihan berstatus Paid dengan referensi `approved-by-platform-owner`; hash kata sandi dihapus dari pengajuan; provider punya batas dan modul sesuai paket ditambah modul tambahan |
| S5a | Owner | Setujui pengajuan yang sama dua kali, atau pengajuan yang sudah ditolak | Ditolak: "sudah diputuskan" | Tidak ada perusahaan ganda |
| S5b | Owner | Persetujuan gagal di tengah (mis. email akun sudah dipakai) | Tidak ada data setengah jadi | Provider, cabang, pengguna, langganan tidak tersisa |
| S6 | Owner | Pengajuan lain: klik **Tolak pengajuan** tanpa alasan, lalu dengan alasan | Tanpa alasan: ditolak; dengan alasan: pengajuan berstatus tidak disetujui, hash kata sandi dihapus, lead ditutup | Setelah ditolak tidak bisa disetujui atau di-provision |
| S6a | Peran lain | Panggil setujui atau tolak dengan token non-owner | 403 | Pengajuan tetap menunggu |

## Fase 3. Calon klien menjadi klien

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S7 | Calon klien | Halaman status (otomatis menyegarkan) | Berubah menjadi "Langganan Anda aktif" dengan email akun dan tombol **Masuk**; tidak ada tagihan tertunda di mode uji | Setelah ditolak: alasan tampil dan tautan pengajuan baru |
| S8 | Klien | **Masuk** dengan email dan kata sandi yang dipilihnya saat mendaftar; ubah kata sandi; aktifkan verifikasi dua langkah | Masuk berhasil tanpa langkah serah kredensial; tahap **first login** selesai dan onboarding **completed** | Kata sandi salah berulang dibatasi; sesi kedaluwarsa kembali ke login; 2FA diminta bila aktif |
| S9 | Klien | **Pengaturan → Langganan** | Paket, status Active, periode, batas, fitur yang termasuk atau bisa ditambah | Hanya langganan perusahaannya |
| S10 | Klien | Menu hanya memuat modul paket ditambah modul tambahan yang dipilih saat mendaftar | Aplikasi "dimulai berdasarkan layanan yang dipilih" | Modul di luar pilihan: menu hilang dan endpoint 403 |

## Fase 4. Klien menyiapkan perusahaannya (mulai dari sini file `00` dikerjakan oleh klien)

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S11 | Klien | Tambah cabang lain (Apotek Bandung, Klinik Bekasi, Pabrik Sukabumi, Kafe, ...), pengguna, peran, karyawan | Terbentuk sesuai batas paket | Melebihi batas cabang, pengguna, atau karyawan ditolak dengan pesan batas paket; data lama tidak terhapus; peran klien hanya bisa memberi izin yang ia miliki |
| S12 | Klien | Atur master data, template, alur persetujuan, saldo awal (file `00` dan `01` bagian A) | Siap bertransaksi | Menu hanya modul paket |

## Fase 5. Perjalanan langganan sesudah berjalan

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S13 | Klien | **Minta ganti paket atau tambah add-on** (mis. fitur "Biaya logistik dan landed cost") | Permintaan tercatat (tanpa izin khusus, hanya perusahaannya) | Permintaan ganda untuk hal sama ditolak atau digabung |
| S14 | Owner | Proses di **Subscription dashboard**, lalu **Change plan** | Batas dan modul langsung mengikuti paket baru; tagihan berikut memakai harga baru | Turun paket di bawah pemakaian (mis. 8 cabang ke batas 5) ditolak dengan rincian batas yang terlampaui; fitur dicabut: menu hilang dan 403 |
| S15 | Sistem | Tagihan periode berikutnya terbit seminggu sebelum periode berakhir (*Run daily job now* untuk mempercepat) | Tagihan baru Unpaid | Tidak terbit ganda; klien yang berhenti di akhir periode tidak ditagih |
| S16 | Sistem dan Owner | Klien tidak membayar: jalankan job harian setelah jatuh tempo | **Past due**, lalu **Suspended** setelah masa tenggang | Klien tertangguhkan: login dan semua API menolak (kecuali keluar), halaman publik klien tertutup, **data tidak hilang** |
| S17 | Klien dan Owner | Klien membayar tagihan tertunggak (tautan bayar publik atau **Mark as paid**) | **Active**, akses pulih | Webhook pembayaran memulihkan akses tanpa tindakan owner |
| S18 | Klien dan Owner | **Berhenti berlangganan** (akhir periode atau sekarang) dengan alasan | Akses sampai periode habis atau langsung tertangguhkan | Alasan wajib; **Reactivate** menerbitkan tagihan baru dan akses kembali setelah dibayar |
| S19 | Owner | Dashboard langganan dan dashboard platform | Angka cocok dengan daftar langganan dan tagihan | Angka sama dengan hasil filter di daftar |
| S20 | Mitra dan Owner | Klien lewat **Mitra**: rekap tagihan mitra, finalisasi, ekspor | Rekap hanya memuat klien mitra itu | Rekap final tidak berubah; dibuka kembali hanya dengan aksi khusus |

## Mode produksi: langganan mulai setelah dibayar (`on_payment`)

Ulangi S3 sampai S7 dengan `subscription_self_service_activation` = `on_payment` dan paket tanpa uji coba.

| # | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- |
| P1 | Owner menyetujui pengajuan | Perusahaan, akun, dan langganan terbentuk; langganan **Awaiting payment**; tagihan pertama **Unpaid** | Halaman status menampilkan tagihan (nomor, jumlah, jatuh tempo) dan tombol **Bayar tagihan** |
| P2 | Klien membuka **tautan bayar publik** dan membayar lewat QRIS akun gateway platform (sandbox; simulasikan bayar di dashboard penyedia) | Setelah webhook: tagihan **Paid**, periode diperpanjang, langganan **Active** | Token salah atau kedaluwarsa seperti tidak ada; tagihan lunas tidak bisa dibayar lagi; webhook ganda hanya mencatat sekali; nominal di luar batas penyedia ditolak |
| P3 | Alternatif: owner **Mark as paid** (transfer bank, tunai, lain) dengan referensi | Tagihan lunas, langganan aktif | Tagihan **Voided** tidak bisa dilunasi |
| P4 | Pengajuan dengan uji coba (paket punya masa uji coba, dicentang) | Langganan **Trial** tanpa tagihan; tagihan pertama terbit di akhir uji coba | Tahap pembayaran dianggap selesai (trial) |

## Jalur lain: lead dan onboarding oleh owner (tetap ada)

Calon klien yang tidak memakai `/subscribe` bisa mengirim **formulir minat** di landing (lead berstatus Baru); owner menindaklanjuti di **Landing Leads**, membuat **Client Onboarding** dari lead itu, lalu **Provision**,
tagihan, **serah kredensial**, dan login pertama. Uji: validasi formulir (nama dan email wajib, batas laju 10 per menit), status lead Baru, Sudah Dihubungi, Qualified, Closed; onboarding dari lead (telepon angka 6 sampai 15
digit, kode pos 5 digit); provision atomik dan tidak bisa dua kali; peran milik klien lain tidak bisa dipinjam; izin awal hanya izin klien; tahap onboarding diturunkan dari data nyata.

## Kasus negatif dan batas yang menyeluruh

| Skenario | Hasil yang diharapkan |
| --- | --- |
| Peran selain owner memanggil endpoint onboarding, langganan, tagihan, lead, setujui, tolak | 403; tidak ada data bocor |
| Pendaftaran mandiri dimatikan (`subscription_self_service_enabled` salah) lalu kirim pengajuan | Ditolak (403) dan halaman `/subscribe` menyatakan tidak tersedia |
| Modul tambahan yang inti atau nonaktif dikirim di pengajuan | Ditolak dengan pesan modul tidak dapat ditambahkan |
| Tautan pembayaran klien A dibuka dengan token B | Seperti tautan tidak ada |
| Klien tertangguhkan memanggil API setelah login lama | Ditolak dengan pesan penangguhan; sesi lama tidak lolos |
| Klien memanggil endpoint ganti paket milik perusahaan lain | Ditolak |
| Pembayaran tagihan dengan nominal berbeda | Ditolak atau ditandai perlu ditinjau; saldo tagihan konsisten |
| Mode uji `on_approval` dibiarkan menyala di produksi | **Risiko**: setiap persetujuan memberi langganan gratis. Pastikan nilainya `on_payment` sebelum rilis |

## Hubungan angka dan data yang harus benar sesudah persetujuan (mode uji)

1. Tagihan pertama berstatus Paid dengan jumlah = harga paket (+ add-on) sesuai siklus; periode berakhir = awal periode + satu siklus.
2. Provider memiliki tepat satu cabang (cabang utama), satu pengguna utama, dan satu peran awal sampai klien menambahkan.
3. Modul aktif klien = modul paket + modul tambahan yang dipilih; batas angka = batas paket.
4. Tahap onboarding turun dari data nyata: requested, plan selected, approval, provisioned, payment, credentials handed, first login.

## Netralisasi

Pada database uji: batalkan langganan uji lalu pakai salinan database baru (`erp_scratch`). Kembalikan `subscription_self_service_activation` ke `on_payment` setelah uji. Jangan menghapus tagihan lunas atau data klien di produksi.
