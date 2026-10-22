---
title: (PT Sehat Sentosa Farma) — 04. Inti: Persetujuan dan Asisten AI
category: sehat-sentosa-farma
description: Kasus uji per bab manual book modul core untuk skenario PT Sehat Sentosa Farma. Alur persetujuan lintas modul dan asisten AI dalam aplikasi.
visibility: internal
---

# 04. Inti: Persetujuan dan Asisten AI

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

**Dikerjakan oleh:** Konfigurasi alur persetujuan oleh **Dr. Rahmat**. Memproses permintaan persetujuan (bagian 4) oleh **Sari Wulandari** (Manajer Keuangan) lalu **Dr. Rahmat** sebagai persetujuan akhir. Kunci AI diisi sekali oleh admin.

**Cabang aktif:** Pusat.

**Cara membaca baris "Input di":** tiap bagian di bawah diawali satu baris itu, berisi menu sidebar dan alamat halaman tempat data dimasukkan. Data yang harus diisi ada di kolom "Langkah dan data uji" dan di file `00` (data acuan).

## Titik uji kunci modul ini (ditulis tangan)

- Alur persetujuan per modul dengan langkah dan peran; permintaan muncul di antrean penyetuju; dokumen tidak bisa diputuskan di luar antrean saat alur berjalan.
- Persetujuan dimatikan = dokumen langsung disetujui saat diajukan.
- Asisten AI memakai kunci API per cabang (bukan .env); jawaban memakai data cabang aktif; aksi berupa kartu yang dikonfirmasi pengguna.
- Playbook, jadwal, tutorial dan tata kelola aksi AI.

## 1. Konfigurasi Approval Workflow — Lintas Modul

Bab manual: [`core/01-konfigurasi-approval-workflow.md`](../../erpApiServices/docs/manualBook/core/01-konfigurasi-approval-workflow.md)

**Input di:** `Client Master → Approval Workflow Configurations` (`/client-master/approval-workflow-configs`).

**Perhatikan:** **Kerjakan ini SEBELUM mengaktifkan toggle "Require ... Approval" di modul manapun** (Purchase Configs, Sales Configs, Journal, dll).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi Approval Workflow (draf) | Membuat approval workflow untuk dokumen penjualan dengan 2 tahap dan batas nominal Rp1.000.000,00; mengonfirmasi setuju | Approve berhasil dilakukan oleh approver sesuai hak akses |
| Negatif — Konfigurasi Approval Workflow (draf) | Mengatur batas nominal lebih tinggi tanpa menyetujui tahap approval; mencoba approve melebihi batas nominal | Tidak dapat disetujui karena melampaui batas nominal yang ditentukan dan muncul pesan error |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Module Name dan Module Group — nama tampilan config ini (Module aslinya sendiri tetap mengikuti template yang dipilih, tidak bisa diganti di sini) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Approver harus di departemen yang sama dengan requester (toggle, opsional) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Asisten AI In-App — Modul Core

Bab manual: [`core/02-asisten-ai.md`](../../erpApiServices/docs/manualBook/core/02-asisten-ai.md)

**Input di:** tombol **Asisten AI** (ikon obrolan) di navbar aplikasi; kunci AI-nya diisi di `Core → Integrations` (`/core/integration-configs`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Aktivasi Asisten AI (draf) | Admin mengambil API key, memasukkan ke aplikasi, uji di server | Asisten AI berfungsi dengan baik, menjawab pertanyaan dan menyiapkan tombol pintasan |
| Negatif — Input API key salah (draf) | Admin memasukkan API key yang salah | Aplikasi menolak aktivasi pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tiap penyedia diuji dua hal: (1) balasan chat biasa, (2) satu pemanggilan tool. Harus muncul ✓ plain chat dan ✓ tool call. Output hanya menampilkan model + latensi + lulus/gagal — tidak menampilkan API key |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Cara Dapat API Key AI Provider — Modul Core

Bab manual: [`core/03-cara-dapat-api-key-ai.md`](../../erpApiServices/docs/manualBook/core/03-cara-dapat-api-key-ai.md)

**Input di:** kunci didapat dari situs penyedia AI (Gemini, OpenRouter, Groq, OpenAI, Anthropic), lalu diisi di `Core → Integrations` (`/core/integration-configs`).

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Google Gemini (draf) | Mendapatkan API key gratis, mengaktifkan asisten AI | Sukses mendapatkan dan mengintegrasikan API key ke sistem Sentosa Farma |
| Negatif — OpenRouter (draf) | Input salah dalam format key, menolak pesan penolakan yang jelas | Tidak dapat mengaktifkan asisten AI, memerlukan pengecekan kembali format key yang benar |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi saldo dulu — tanpa saldo, semua permintaan API ditolak: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Akun baru dapat ±$5 kredit uji coba tanpa kartu kredit (butuh verifikasi nomor HP). Setelah habis, harus isi billing untuk lanjut |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Verifikasi nomor HP (kode SMS) — wajib |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Harus muncul ✓ plain chat dan ✓ tool call. Output tidak menampilkan API key |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Memproses Approval Requests — Sisi Approver

Bab manual: [`core/04-approval-requests.md`](../../erpApiServices/docs/manualBook/core/04-approval-requests.md)

**Input di:** `Approvals → Approval Requests` (`/approvals/approval-requests`).

**Prasyarat:** Approval Workflow sudah dikonfigurasi (lihat chapter _01. Konfigurasi Approval Workflow_) dan user login sedang aktif dengan Role yang termasuk di salah satu step workflow tersebut.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Approve Purchase Request (draf) | Approver menyetujui permintaan pembelian Paracetamol dari PT Bintang Farmasi Utama | Persetujuan berhasil, status request berubah menjadi approved |
| Negatif — Menolak Sales Request tanpa alasan (draf) | Approver menolak penjualan Amoxicillin 500 mg ke Apotek Mitra Sehat tanpa memberikan alasan | Permintaan ditolak, status request tetap pending dan menampilkan pesan kesalahan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tombol "View Approval Config" (kalau tersedia) jadi jalan pintas untuk melihat konfigurasi lengkap workflow ini di Client Master → Approval Workflow Configs, berguna kalau perlu memastikan siapa saja yang seharusnya bisa approve |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Agen AI, Aksi, Mode Tutorial, Rangkaian, dan Jadwal — Modul Core

Bab manual: [`core/05-agen-ai-aksi-tutorial-dan-jadwal.md`](../../erpApiServices/docs/manualBook/core/05-agen-ai-aksi-tutorial-dan-jadwal.md)

**Input di:** di dalam panel **Asisten AI** (tombol obrolan di navbar); tidak punya halaman menu sendiri.

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Agen AI (draf) | Memasukkan SKU OBT-001, menekan "aksi", mengkonfirmasi penambahan stok 500 unit | Sistem mengirim notifikasi ke gudang untuk pengiriman 500 unit Paracetamol 500 mg strip |
| Negatif — Mode Tutorial (draf) | Menekan tombol "tutorial" tanpa login, mencoba menjawab pertanyaan | Akses ditolak pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Asisten bekerja sebagai kamu. Dia hanya bisa melakukan yang memang boleh kamu lakukan di aplikasi. Izin, validasi, dan catatan perubahan sama dengan kalau kamu mengerjakannya sendiri |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau aplikasi menolak (mis. "Quotation wajib dulu" atau periode tertutup), alasan penolakan tampil di kartu — itu aturan cabang, bukan kesalahan asisten |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
