# 02. Isi Form di Layar dan Perbaikan Error

Halaman rujukan: **Sales → Quotations → Buat** (bridge eksplisit) dan modal **Client Master → Payment Methods** (cadangan DOM). Mode Agent menyala.

## Positif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 2.1 | Buka Buat Quotation, chat: "isi untuk pelanggan PT Maju, 10 kopi, tanggal hari ini" | Pelanggan terpilih, tanggal terisi, satu baris item (SKU kopi, qty 10); muncul kartu "form diisi" |
| 2.2 | Periksa harga dan satuan baris | Terisi dari SKU (harga aktif) atau sesuai yang diminta; total terhitung |
| 2.3 | Tekan **Urungkan** pada kartu "form diisi" | Isian kembali seperti sebelum diisi |
| 2.4 | Isi ulang, lalu tekan Simpan sendiri | Quotation tersimpan atas tindakan **kamu**; tidak tersimpan sebelum itu |
| 2.5 | Minta "ganti catatannya jadi: penawaran khusus" | Hanya field catatan berubah |
| 2.6 | Kosongkan pelanggan, tekan Simpan sampai muncul error, lalu tekan **Perbaiki error form** | Asisten mengisi field yang bermasalah; error hilang saat Simpan ulang |
| 2.7 | Buka modal Payment Methods (tambah), chat: "isi nama Transfer BCA kode TRF-BCA" | Input nama dan kode terisi lewat cadangan DOM |

## Negatif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 2.8 | Minta pelanggan yang tidak ada ("PT Tidak Ada") | Asisten menyatakan tidak ditemukan, tidak menebak id; field tidak terisi |
| 2.9 | Minta tanggal "kapan-kapan" | Asisten meminta tanggal pasti; field tanggal tidak berubah |
| 2.10 | Minta SKU yang tidak ada | Baris tidak ditambahkan; kartu menyebut yang dilewati |
| 2.11 | Buka halaman tanpa dukungan bridge (mis. halaman daftar), minta "isi formnya" | Asisten menjelaskan tidak ada form yang bisa diisi di halaman ini |
| 2.12 | Permintaan agar asisten "simpan sekalian" | Asisten menolak: kamu yang menekan Simpan |
| 2.13 | Mode Tutorial menyala, minta isi form | Ditolak: tutorial tidak mengisi form |
| 2.14 | Field sensitif pada form (NPWP, rekening) | Nilainya tidak dikirim ke asisten; asisten tidak bisa membacanya |
