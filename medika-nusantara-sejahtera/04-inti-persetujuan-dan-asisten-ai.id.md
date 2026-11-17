---
title: (PT Medika Nusantara Sejahtera) — 04. Inti: Persetujuan dan Asisten AI
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul core untuk skenario PT Medika Nusantara Sejahtera. Alur persetujuan lintas modul dan asisten AI dalam aplikasi.
visibility: internal
---

# 04. Inti: Persetujuan dan Asisten AI

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji alur persetujuan (siapa menyetujui apa), pengingat, dan asisten AI di dalam aplikasi.
>
> **Kalau semuanya benar, artinya:** Dokumen penting tertahan sampai disetujui orang yang berhak, dan asisten AI membantu tanpa melewati aturan izin.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Alur persetujuan per modul dengan langkah dan peran; permintaan muncul di antrean penyetuju; dokumen tidak bisa diputuskan di luar antrean saat alur berjalan.
- Persetujuan dimatikan = dokumen langsung disetujui saat diajukan.
- Asisten AI memakai kunci API per cabang (bukan .env); jawaban memakai data cabang aktif; aksi berupa kartu yang dikonfirmasi pengguna.
- Playbook, jadwal, tutorial dan tata kelola aksi AI.

## 1. Konfigurasi Approval Workflow — Lintas Modul

Bab manual: [`core/01-konfigurasi-approval-workflow.md`](../../erpApiServices/docs/manualBook/core/01-konfigurasi-approval-workflow.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Menyiapkan konfigurasi approve PO (draf) | Klik "Use Template" Purchase Order; Pilih template "Basic"; Isi nama step 1 menjadi "Review Manager"; Tambah role "Kepala Gudang" ke step tersebut; Aktifkan "Is Required" dan "Is Final" untuk step ini | Step "Review Managerpesan yang jelasKepala Gudang", status step wajib dan final |
| Negatif — Menambah tahap approve tanpa mengcopy template (draf) | Coba klik "Add Step" tanpa menyalin template terlebih dahulu; Klik "Save" | Muncul pesan error pesan yang jelas karena konfigurasi PO belum dibuat sebelumnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Module Name dan Module Group — nama tampilan config ini (Module aslinya sendiri tetap mengikuti template yang dipilih, tidak bisa diganti di sini) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Approver harus di departemen yang sama dengan requester (toggle, opsional) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Asisten AI In-App — Modul Core

Bab manual: [`core/02-asisten-ai.md`](../../erpApiServices/docs/manualBook/core/02-asisten-ai.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Aktivasi asisten AI (draf) | Admin mengambil API key dari penyedia gratis; memasukkan ke aplikasi; menguji fitur Tanya-jawab. | Panel chat muncul dengan tampilan Bubble, menjawab pertanyaan pesan yang jelas tanpa membuka halaman atau form. |
| Negatif — Input API key salah (draf) | Admin memasukkan API key yang tidak valid ke aplikasi; menguji fitur Tanya-jawab. | Aplikasi menampilkan pesan kesalahan pesan yang jelas dan asisten tidak aktif sampai API key diperbaiki. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tampilan mengambang dan dock tidak bisa aktif bersamaan. Menutup panel juga menutup jendela terpisah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tiap penyedia diuji dua hal: (1) balasan chat biasa, (2) satu pemanggilan tool. Harus muncul ✓ plain chat dan ✓ tool call. Output hanya menampilkan model + latensi + lulus/gagal — tidak menampilkan API key |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Cara Dapat API Key AI Provider — Modul Core

Bab manual: [`core/03-cara-dapat-api-key-ai.md`](../../erpApiServices/docs/manualBook/core/03-cara-dapat-api-key-ai.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mendapatkan API Key Google Gemini (draf) | Buka https://aistudio.google.com; Sign in dengan akun Gmail; Setujui ToS; Klik Create API key; Pilih Create API key in new project; Klik Copy | Key muncul diawali AIza… dan bisa digunakan dalam aplikasi |
| Negatif — Tidak Mendapatkan API Key Google Gemini (draf) | Input data sign in salah; Belum setuju ToS; Cabut key sebelum salin | Muncul pesan kesalahan, tidak dapat membuat key baru; Tidak bisa mengakses halaman API keys; Cabut key berhasil tetapi key hilang |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi saldo dulu — tanpa saldo, semua permintaan API ditolak: |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Akun baru dapat ±$5 kredit uji coba tanpa kartu kredit (butuh verifikasi nomor HP). Setelah habis, harus isi billing untuk lanjut |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. Verifikasi nomor HP (kode SMS) — wajib |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Harus muncul ✓ plain chat dan ✓ tool call. Output tidak menampilkan API key |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Memproses Approval Requests — Sisi Approver

Bab manual: [`core/04-approval-requests.md`](../../erpApiServices/docs/manualBook/core/04-approval-requests.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Approver mengapprove request Purchase Order (draf) | Login sebagai approver; Pilih "Approve" pada PO dari Medika Nusantara; Isi catatan jika diperlukan | Status PO berubah menjadi Approved, ditandai dengan tanda ceklis di kolom Step dan timestamp di Completed At |
| Negatif — Approver mencoba reject request Purchase Invoice tanpa login sebagai approver (draf) | Coba klik "Reject" pada PI dari Medika Nusantara tanpa login; Dapat pesan error "Anda tidak memiliki hak akses untuk melakukan tindakan ini" | Tidak ada perubahan status, tetap menunjukkan status Pending di PI |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tombol "View Approval Config" (kalau tersedia) jadi jalan pintas untuk melihat konfigurasi lengkap workflow ini di Client Master → Approval Workflow Configs, berguna kalau perlu memastikan siapa saja yang seharusnya bisa approve |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Catatan wajib saat memilih Reject atau Request Revision |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Penyetuju harus berhak pada langkah yang sedang berjalan (peran atau pengguna yang ditetapkan) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau pengaturan cegah persetujuan sendiri (approvalpreventselfapproval) aktif, pengaju tidak bisa menyetujui permintaan yang ia ajukan sendiri |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Agen AI, Aksi, Mode Tutorial, Rangkaian, dan Jadwal — Modul Core

Bab manual: [`core/05-agen-ai-aksi-tutorial-dan-jadwal.md`](../../erpApiServices/docs/manualBook/core/05-agen-ai-aksi-tutorial-dan-jadwal.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat draft purchase request (draf) | "buatkan purchase request 10 kopi untuk PT Maju" | Kartu draft purchase request muncul dengan detail, bisa diperiksa sebelum disubmit. |
| Negatif — Input supplier salah (draf) | "buatkan purchase request 10 kopi untuk PT TidakAda" | Kartu dibuang dan tampil pesan penolakan yang jelas. |
| Positif — Mengisi form Quotation (draf) | "isi untuk PT Maju, 10 kopi, tanggal besok" saat membuka halaman Buat Quotation | Form Quotation terisi dengan detail sesuai permintaan. |
| Negatif — Tanggal di masa lalu (draf) | "isi untuk PT Maju, 10 kopi, tanggal kemarin" saat membuka halaman Buat Quotation | Muncul error validasi dan tampil pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 1. Asisten bekerja sebagai kamu. Dia hanya bisa melakukan yang memang boleh kamu lakukan di aplikasi. Izin, validasi, dan catatan perubahan sama dengan kalau kamu mengerjakannya sendiri |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kalau aplikasi menolak (mis. "Quotation wajib dulu" atau periode tertutup), alasan penolakan tampil di kartu — itu aturan cabang, bukan kesalahan asisten |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Diagram Alur Persetujuan — Modul Core

Bab manual: [`core/06-diagram-alur-persetujuan.md`](../../erpApiServices/docs/manualBook/core/06-diagram-alur-persetujuan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal bab ini | Ikuti langkah di bab manual dengan data acuan file `00` (draf Ollama tidak dapat dipakai, isi manual) | Hasil sesuai uraian bab |
| Negatif — input tidak valid | Kosongkan field wajib atau isi di luar batas | Ditolak dengan pesan yang jelas, tidak ada data tersimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | H --/"Reject, catatan wajib"/ L(["Dokumen Rejected"]) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | H --/"Request Revision, catatan wajib"/ M(["Dokumen kembali ke Draft"]) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | B --/"Ya"/ X1["Ditolak: permintaan sudah selesai"] |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | C --/"Tidak"/ X2["Ditolak: tidak berwenang pada langkah ini"] |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Hubungan Antar Modul — Modul Core

Bab manual: [`core/07-hubungan-antar-modul.md`](../../erpApiServices/docs/manualBook/core/07-hubungan-antar-modul.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Delivery Approved (draf) | Approve delivery OBT-001 di Sales; stok Paracetamol 500 mg strip (SKU OBT-001) bertambah | Stok dan jurnal terbentuk sesuai data delivery approved |
| Negatif — Purchase Return Rejected (draf) | Input Purchase Return OBT-002 tanpa PO asal; klik Submit | Muncul pesan penolakan yang jelas dan Purchase Return tidak disimpan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Hubungan di atas ikut cabang aktif; dokumen cabang lain tidak bisa ditautkan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Dokumen yang sudah punya dampak di modul lain umumnya tidak bisa dihapus; batalkan atau buat dokumen pembalik |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
