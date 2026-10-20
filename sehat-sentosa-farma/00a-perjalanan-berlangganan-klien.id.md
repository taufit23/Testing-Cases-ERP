---
title: (PT Sehat Sentosa Farma) — 00a. Perjalanan Berlangganan Klien (Titik Awal Suite)
category: sehat-sentosa-farma
description: Suite dimulai dari calon klien yang menemukan aplikasi di landing page, bukan dari admin yang memasukkan data perusahaan. Alur: landing, paket, formulir minat, tindak lanjut owner, onboarding, tagihan dan pembayaran, serah kredensial, login pertama, penagihan berkala, ganti paket, penangguhan, berhenti.
visibility: internal
---

# 00a. Perjalanan Berlangganan Klien

> **Titik awal suite ini.** PT Sehat Sentosa Farma **belum ada** di aplikasi. Yang ada hanya platform (landing page, paket langganan, akun platform owner) dan seorang calon klien:
> **Dr. Rahmat Hidayat**, direktur, yang ingin memakai aplikasi untuk grupnya. Semua data perusahaan di file `00` lahir dari alur ini, bukan dimasukkan lebih dulu oleh admin.
>
> **Aktor:** *Calon klien* (belum login), *Platform Owner* (pemilik aplikasi, akun owner), *Klien* (Dr. Rahmat setelah punya akun), *Mitra* (reseller, opsional).
> **Kenyataan penting dari kode:** berlangganan di aplikasi ini **digerakkan owner** (formulir minat, lalu owner membuat onboarding dan memprovisi). **Pendaftaran mandiri** (calon klien memilih paket,
> membayar, dan perusahaan terbentuk otomatis tanpa owner) **belum ada**; baris S3a menguji hal itu sebagai celah **G36** di [`95`](./95-daftar-celah-dan-usulan-perbaikan.id.md).
> Pengiriman email otomatis (tagihan, kredensial) bergantung SMTP yang saat ini ditahan, jadi bagian itu dicatat sebagai **G37** dan langkahnya dilakukan manual.
>
> **Prasyarat teknis:** database uji; satu akun platform owner; paket langganan uji ("Paket Grup Kesehatan" memuat modul Pembelian, Persediaan, Penjualan, Kanvasing, POS, Restoran, Manufaktur,
> Pertambangan, Sewa, Akuntansi, Keuangan, Aset Tetap, SDM, Proyek; batas 5 cabang, 20 pengguna, 50 karyawan; masa uji coba 14 hari; harga bulanan dan tahunan); akun gateway platform
> sandbox untuk pembayaran tagihan (panduan: `erpApiServices/docs/panduan-uji-kredensial-pembayaran.id.md`).

## Fase 1. Calon klien menemukan dan membandingkan (tanpa login)

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S1 | Calon klien | Buka halaman depan situs: banner, fitur, modul (produk), testimoni, klien, FAQ, profil pemilik, tim | Semua bagian tampil sesuai pengaturan landing; bagian yang disembunyikan di pengaturan tidak tampil; teks mengikuti bahasa pilihan | Landing berjalan tanpa login; tidak ada data internal; judul dan meta halaman terisi (SEO), peta situs dan robots tersedia |
| S2 | Calon klien | Lihat daftar **paket langganan** dan harga (bulanan/tahunan), modul termasuk, batas, masa uji coba | Hanya paket aktif yang bisa dipesan tampil; harga dan masa uji coba sesuai master paket | Paket nonaktif tidak tampil; harga tahunan terbaca terhadap bulanan; tidak ada paket tanpa harga |
| S3 | Calon klien | Isi **formulir minat**: nama, email, telepon, perusahaan "PT Sehat Sentosa Farma", modul diminati "Persediaan, POS, Pembelian", pesan, sumber | Lead berstatus **Baru** tercatat dengan alamat IP; layar konfirmasi | Validasi: nama dan email wajib, email berformat benar; kirim lebih dari 10 kali per menit ditolak (pembatas laju); kolom pesan dibatasi panjangnya |
| S3a | Calon klien | **Daftar langsung dan bayar tanpa menunggu owner** | Idealnya: pilih paket, isi data perusahaan dan akun, bayar, perusahaan dan akun aktif otomatis | **Belum ada** (G36): hanya formulir minat. Catat sebagai temuan |

## Fase 2. Platform Owner menindaklanjuti dan menyiapkan klien

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S4 | Owner | Buka **Landing Leads**, filter Baru, buka lead Dr. Rahmat; ubah status ke **Sudah Dihubungi** lalu **Qualified**, tulis catatan internal | Status dan catatan tersimpan; catatan tidak terlihat publik | Hanya platform owner yang melihat Landing Leads (peran lain 403); lead bisa dihapus setelah konfirmasi |
| S5 | Owner | Buat **Client Onboarding** dari lead itu: perusahaan, kontak, plan "Paket Grup Kesehatan", siklus bulanan, **dengan uji coba**, paket modul, add-on yang dibeli, nama dan alamat cabang pertama "Kantor Pusat & Distribusi Jakarta", akun utama Dr. Rahmat | Onboarding bernomor unik, tahap: **requested** dan **plan selected** selesai; tahap lain menunggu | Telepon hanya angka (6 sampai 15 digit); kode pos 5 digit; email akun berformat benar; dua pembuat serentak tidak menghasilkan nomor ganda; peran lain 403 |
| S6 | Owner | Jalankan **Provision** pada onboarding | Dalam **satu transaksi**: provider, langganan, cabang pertama, pengguna dan peran terbentuk dan terhubung ke onboarding; tahap **provisioned** selesai; langganan berstatus **Trial** (karena dipilih uji coba) | Provision gagal di tengah tidak meninggalkan data setengah jadi; provision kedua kali pada onboarding yang sama ditolak; peran milik klien lain tidak bisa dipinjam; izin peran awal hanya yang boleh dimiliki klien (bukan izin platform) |
| S7 | Owner | Periksa hasil provisioning | Provider punya batas sesuai paket (cabang, pengguna, karyawan, kasir) dan modul sesuai paket; menu klien hanya memuat modul itu | Modul di luar paket: menu hilang dan endpoint 403; batas angka tertulis di provider |

## Fase 3. Pembayaran

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S8 | Sistem dan Owner | Selama uji coba tidak ada tagihan; di akhir uji coba (atau bila tanpa uji coba) **tagihan pertama** terbit (jalankan *Run daily job now* untuk mempercepat) | Tagihan berstatus **Unpaid** dengan jatuh tempo; langganan **Awaiting payment** bila tanpa uji coba | Tagihan terbit sekali per periode (tidak ganda bila job dijalankan dua kali); nominal = harga paket + add-on sesuai siklus |
| S9 | Klien | Buka **tautan pembayaran publik** tagihan itu (tanpa login), bayar lewat **QRIS akun gateway platform** (sandbox; simulasikan bayar di dashboard penyedia) | Halaman menampilkan tagihan dan QR; setelah webhook: tagihan **Paid**, periode diperpanjang, langganan **Active** | Token salah atau kedaluwarsa dijawab seperti tidak ada; tagihan lunas tidak bisa dibayar lagi; webhook ganda hanya mencatat sekali; nominal di luar batas penyedia ditolak; halaman tidak membocorkan data klien lain |
| S9a | Owner | Alternatif: konfirmasi pembayaran manual **Mark as paid** (transfer bank, tunai, lainnya) dengan referensi | Tagihan lunas dan langganan aktif | Metode wajib dipilih; referensi tercatat; tagihan **Voided** tidak bisa dilunasi |
| S10 | Owner | Lihat tahap onboarding | Tahap **payment** berstatus selesai (atau trial) | Tahap diturunkan dari data nyata (status langganan, tagihan lunas, login), bukan disimpan ganda |

## Fase 4. Serah kredensial dan login pertama

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S11 | Owner | Tandai **kredensial diserahkan** (email belum otomatis: G37) dan kirim kata sandi awal lewat saluran aman | Tahap **credentials handed** selesai, tercatat waktunya | Tahap ini terkunci sebelum provision |
| S12 | Klien | Login pertama di halaman masuk; ubah kata sandi awal; aktifkan verifikasi dua langkah | Masuk berhasil; tahap **first login** selesai dan onboarding berstatus **completed** | Kata sandi salah berulang dibatasi (per alamat dan IP); sesi yang kedaluwarsa kembali ke login; 2FA diminta bila aktif |
| S13 | Klien | Buka **Pengaturan → Langganan** | Tampil paket, status, periode, batas dan fitur yang termasuk atau bisa ditambah | Hanya langganan perusahaannya; peran biasa tidak melihat langganan perusahaan lain |

## Fase 5. Klien menyiapkan perusahaannya (mulai dari sini file `00` dikerjakan oleh klien)

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S14 | Klien | Tambah cabang lain (Apotek Bandung, Klinik Bekasi, Pabrik Sukabumi, Kafe, ...), pengguna, peran, karyawan | Terbentuk sesuai batas paket | Melebihi batas cabang, pengguna, atau karyawan ditolak dengan pesan batas paket; data lama tidak terhapus; peran klien hanya bisa memberi izin yang ia miliki |
| S15 | Klien | Atur master data, template, alur persetujuan, saldo awal (file `00`, `01` bagian A) | Siap bertransaksi | Menu hanya modul paket |

## Fase 6. Perjalanan langganan sesudah berjalan

| # | Aktor | Aksi | Hasil yang diharapkan | Periksa |
| --- | --- | --- | --- | --- |
| S16 | Klien | **Minta ganti paket atau tambah add-on** (mis. aktifkan fitur "Biaya logistik dan landed cost") | Permintaan tercatat (tanpa izin khusus, hanya untuk perusahaannya) | Permintaan ganda untuk hal sama ditolak atau digabung |
| S17 | Owner | Proses permintaan di **Subscription dashboard** lalu **Change plan** | Batas dan modul langsung mengikuti paket baru; tagihan berikut memakai harga baru | Turun paket di bawah pemakaian (mis. 8 cabang ke batas 5) ditolak atau diperingatkan [verifikasi]; fitur yang dicabut menghilangkan menu dan 403 |
| S18 | Sistem | Tagihan periode berikutnya terbit seminggu sebelum periode berakhir | Tagihan baru Unpaid | Tagihan tidak terbit ganda; klien yang berhenti di akhir periode tidak ditagih |
| S19 | Sistem dan Owner | Klien tidak membayar: jalankan job harian setelah jatuh tempo | Langganan **Past due**, lalu **Suspended** setelah masa tenggang | Klien tertangguhkan: login dan semua API menolak (kecuali keluar), halaman publik klien (karier, penawaran, tautan bayar) tertutup, **data tidak hilang** |
| S20 | Klien dan Owner | Klien membayar tagihan tertunggak | Langganan **Active**, akses pulih penuh | Webhook pembayaran memulihkan akses tanpa tindakan owner |
| S21 | Klien dan Owner | **Berhenti berlangganan** (di akhir periode atau sekarang) dengan alasan | Akses berjalan sampai periode habis atau langsung tertangguhkan | Alasan wajib; **Reactivate** menerbitkan tagihan baru dan akses kembali setelah dibayar |
| S22 | Owner | Dashboard langganan dan dashboard platform | Angka (langganan aktif, uji coba, menunggak, pendapatan berulang) cocok dengan daftar langganan dan tagihan | Angka sama dengan hasil filter di daftar |
| S23 | Mitra dan Owner | Klien lain datang lewat **Mitra (reseller)**: onboarding dengan partner, rekap tagihan mitra bulanan, finalisasi dan ekspor | Rekap mitra benar dan hanya memuat klien mitra itu | Rekap yang sudah difinalisasi tidak berubah; dibuka kembali hanya dengan aksi khusus |

## Kasus negatif dan batas yang menyeluruh

| Skenario | Hasil yang diharapkan |
| --- | --- |
| Peran selain owner memanggil endpoint onboarding, langganan, tagihan, lead | 403; tidak ada data bocor |
| Onboarding tanpa paket, tanpa email kontak, atau nama perusahaan kosong | Ditolak dengan pesan per kolom |
| Dua onboarding untuk perusahaan dan email yang sama | Ditolak atau diperingatkan duplikat [verifikasi] |
| Tautan pembayaran milik klien A dibuka dengan token B | Seperti tautan tidak ada |
| Klien tertangguhkan memanggil API setelah login lama | Ditolak dengan pesan penangguhan; sesi lama tidak lolos |
| Klien memanggil endpoint ganti paket milik perusahaan lain | Ditolak; hanya perusahaannya |
| Pembayaran tagihan dengan nominal berbeda dari tagihan | Ditolak atau ditandai perlu ditinjau; saldo tagihan konsisten |

## Hubungan angka dan data yang harus benar di akhir fase 3

1. Tagihan lunas pertama = harga paket (+ add-on) sesuai siklus; periode berakhir = awal periode + 1 siklus.
2. Provider memiliki tepat satu cabang, satu pengguna utama, dan satu peran awal sampai klien menambahkan.
3. Modul aktif klien = modul paket + add-on; batas angka = batas paket.
4. Tahap onboarding menurun dari data nyata: requested, plan selected, provisioned, payment, credentials handed, first login.

## Netralisasi

Pada database uji: batalkan langganan uji lalu hapus provider uji lewat salinan database, atau ulangi dengan `erp_scratch` baru. Jangan menghapus tagihan lunas atau data klien di produksi.
