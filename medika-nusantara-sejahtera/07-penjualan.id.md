---
title: (PT Medika Nusantara Sejahtera) — 07. Penjualan
category: medika-nusantara-sejahtera
description: Kasus uji per bab manual book modul sales untuk skenario PT Medika Nusantara Sejahtera. Dari penawaran sampai retur penjualan.
visibility: internal
---

# 07. Penjualan

> **Kenapa bagian ini diuji (bahasa sederhana).** Menguji proses menjual: penawaran, pesanan, pengiriman, faktur, sampai pembayaran pelanggan.
>
> **Kalau semuanya benar, artinya:** Stok berkurang saat barang dikirim, piutang tercatat, dan pembayaran melunasi faktur dengan benar.


> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: **(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.

## Titik uji kunci modul ini (ditulis tangan)

- Quotation, SO, delivery, faktur, pembayaran dan retur; HPP terjurnal saat pengiriman.
- Batas kredit pelanggan dan batas diskon (cap) ditegakkan.
- Tautan pembayaran online per faktur memakai saldo terutang; pembayaran sebagian dan lunas dicatat sekali walau webhook berulang.
- Retur: pembalikan PPN sesuai saklar konfigurasi penjualan.
- Penawaran publik dapat dibuka tanpa login lewat token dan kedaluwarsa.

## 1. Konfigurasi Alur Sales — Modul Sales

Bab manual: [`sales/01-konfigurasi-alur-sales.md`](../../erpApiServices/docs/manualBook/sales/01-konfigurasi-alur-sales.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi alur sales (draf) | Masuk ke `/sales/sales-configs`; Aktifkan "Require Sales Order Approval"; Isi persentase "Payment Threshold Percentage" 50; Simpan konfigurasi | Alur approval SO sekarang memerlukan persetujuan, dan barang hanya boleh dikirim setelah 50% pembayaran diterima |
| Negatif — Konfigurasi alur sales (draf) | Masuk ke `/sales/sales-configs`; Aktifkan "Require Sales Order Approval"; Tidak mengisi "Payment Threshold Percentage"; Coba simpan konfigurasi | Gagal menyimpan konfigurasi dengan pesan error: pesan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Require Quotation for SO — kalau aktif, Sales Order wajib berasal dari Quotation yang sudah accepted customer (tidak bisa buat SO manual langsung) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Restrict Agreed Due Date to Quotation Range — kalau aktif, tanggal jatuh tempo yang disepakati di SO tidak boleh melebihi rentang validitas Quotation asalnya |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Kapan pakai "Minimum Payment Percentage": cocok untuk bisnis yang mewajibkan uang muka (DP) sebelum barang dikirim — misalnya wajib bayar 50% dulu baru barang jalan, sisanya ditagih belakangan |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Require Payment Proof — mewajibkan bukti pembayaran (upload) saat mencatat penerimaan pembayaran dari customer |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 2. Quotation — Modul Sales

Bab manual: [`sales/02-quotation.md`](../../erpApiServices/docs/manualBook/sales/02-quotation.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat Quotation baru (draf) | Buka `/sales/quotations`; klik "+ Create"; masukkan Contact: Apotek Mitra Sehat; item: Paracetamol 500 mg strip (SKU OBT-001), harga: Rp2.000, PPN 10%; klik Save → Submit | Status Quotation berubah menjadi Submitted; jika Require Quotation Approval aktif, pergi ke View Approval Request; jika tidak aktif, status langsung Approved |
| Negatif — Mengirim Quotation tanpa item (draf) | Buka `/sales/quotations`; klik "+ Create"; masukkan Contact: Apotek Mitra Sehat; klik Save → Submit | Sistem menolak submit karena item harganya masih kosong atau nol |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Klik Save → Submit. Submit ditolak kalau ada item yang harganya masih kosong atau nol |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Tombol "Download PDF" dan "Resend to Customer" hanya aktif selama status masih Awaiting Customer Response. Begitu penawaran sudah diterima, ditolak customer, atau dikonversi, kedua tombol ini nonaktif karena penawaran sudah final |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 2. "Record Customer Declined": customer menolak. Catatan wajib diisi. Status menjadi Customer Declined |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. "Record Customer Negotiating": customer ingin menawar. Catatan wajib diisi. Quotation kembali ke Draft supaya harga bisa diubah, lalu di-Submit lagi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 3. Sales Order — Modul Sales

Bab manual: [`sales/03-sales-order.md`](../../erpApiServices/docs/manualBook/sales/03-sales-order.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Membuat SO dari Quotation (draf) | Pilih Quotation OBT-001; klik "Convert to SO"; masukkan detail SO; cek batas kredit customer; approve | SO terbentuk dengan item & harga sama, status Confirmed tanpa approval tambahan |
| Negatif — Melebihi Batas Kredit Tanpa Approval Tambahan (draf) | Membuat SO OBT-001 melebihi limit credit; cek batas kredit; approve | Peringatan pesan yang jelas muncul, SO tetap disimpan tapi memerlukan approval tambahan |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 4. Sales Delivery — Modul Sales

Bab manual: [`sales/04-sales-delivery.md`](../../erpApiServices/docs/manualBook/sales/04-sales-delivery.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat pengiriman barang (draf) | Buka Sales Deliveries; pilih SO OBT-001; isi qty 20 dari total 30; klik Save | Pengiriman berhasil, sisa qty menjadi 10, status Delivery Draft |
| Negatif — Mengirim melebihi qty SO (draf) | Buka Sales Deliveries; pilih SO OBT-001; isi qty 40 dari total 30; klik Save | Tidak bisa mengirim, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sistem menolak kalau qty yang diinput melebihi sisa qty yang belum dikirim untuk item tersebut — sama seperti guard di Goods Receipt (modul Purchasing) |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sales Delivery baru ditolak bila: |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 5. Sales Invoice — Modul Sales

Bab manual: [`sales/05-sales-invoice.md`](../../erpApiServices/docs/manualBook/sales/05-sales-invoice.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — jalur normal (draf) | Buka Sales Invoices; klik "+ Create"; pilih SO OBT-001; isi item Paracetamol 500 mg strip; masukkan PPN Keluaran 11%; klik Save. | Tagihan berhasil dibuat untuk SO OBT-001 dengan item Paracetamol 500 mg strip dan PPN Keluaran 11%. |
| Negatif — input salah (draf) | Mencoba membuat tagihan tanpa SO yang dikonfirmasi; masukkan nilai invoice melebihi subtotal SO. | Sistem menolak input karena SO belum dikonfirmasi customer atau total invoice melebihi subtotal SO, pesan penolakan yang jelas. |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sudah Dibayar (Mark as Paid) — invoice langsung dianggap lunas saat disimpan; kalau Require Payment Proof aktif di Sales Configs, wajib upload bukti pembayaran di step ini juga |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Invoice dari SO hanya bisa dibuat bila SO sudah dikonfirmasi customer. Pada mode Delivery Before Invoice, SO harus sudah punya pengiriman |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Total semua invoice aktif untuk satu SO tidak boleh melebihi total SO |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Diskon tidak boleh lebih besar dari subtotal invoice |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 6. Sales Payment Bill — Modul Sales

Bab manual: [`sales/06-sales-payment-bill.md`](../../erpApiServices/docs/manualBook/sales/06-sales-payment-bill.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat penerimaan pembayaran (draf) | Buka Sales Payment Bills; "+ Create"; Pilih OBT-001 (Sales Invoice); Isi Amount 50000; Payment Method Transfer; Upload Bukti; Save | Pembayaran berhasil dicatat, sisa tagihan invoice berkurang |
| Negatif — Membuat payment tanpa bukti (draf) | Buka Sales Payment Bills; "+ Create"; Pilih OBT-001 (Sales Invoice); Isi Amount 50000; Payment Method Transfer; Tidak upload Bukti; Save | Tidak bisa simpan, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | 3. Isi Amount, Payment Method, dan bukti pembayaran (wajib kalau Require Payment Proof aktif di konfigurasi — lihat chapter 01) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 7. Sales Return — Modul Sales

Bab manual: [`sales/07-sales-return.md`](../../erpApiServices/docs/manualBook/sales/07-sales-return.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Mencatat retur obat Paracetamol 500 mg strip (draf) | Buka Sales Returns; pilih Sales Delivery OBT-001; isikan qty 200 dari total terkirim 300; klik Save | Retur disimpan dengan status Draft, stok kembali 200 unit ke gudang |
| Negatif — Mencoba retur lebih dari qty terkirim (draf) | Buka Sales Returns; pilih Sales Delivery OBT-001; isikan qty 400 dari total terkirim 300; klik Save | Input ditolak, pesan penolakan yang jelas |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Menu: Sales → Sales Returns (/sales/sales-returns) · Prasyarat: ada Sales Delivery yang sudah tercatat (barang harus sudah "terkirim" dulu sebelum bisa "dikembalikan") |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Sama seperti Purchase Return, retur tidak bisa melebihi qty yang terkirim (dikurangi retur sebelumnya untuk item yang sama) |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 8. Verifikasi Sales ke Accounting — Modul Sales

Bab manual: [`sales/08-verifikasi-ke-accounting.md`](../../erpApiServices/docs/manualBook/sales/08-verifikasi-ke-accounting.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Verifikasi sales ke accounting berhasil (draf) | Buka General Ledger; Cek Detail Ledger Piutang Dagang bertambah saat Sales Invoice, berkurang saat Payment Bill/Sales Return; Cek Trial Balance Total Debit=Total Kredit seimbang; Cek AR Aging Invoice belum lunas muncul; Periksa Detail Ledger jurnal HPP dari Sales Delivery terbentuk | Piutang Dagang dan Penjualan di General Ledger sesuai, Trial Balance seimbang, Invoice lunas tidak muncul di AR Aging, Margin kotor di Income Statement masuk akal |
| Negatif — Payment Bill belum export ke jurnal (draf) | Buka detail Payment Bill; Cek status Mark as Received belum dilakukan; Export to Journal belum dilakukan | Piutang Dagang tidak berkurang, Payment Bill muncul di AR Aging, Margin kotor di Income Statement terlalu tinggi |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 9. Konfigurasi Jurnal Penjualan

Bab manual: [`sales/09-konfigurasi-jurnal-penjualan.md`](../../erpApiServices/docs/manualBook/sales/09-konfigurasi-jurnal-penjualan.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Konfigurasi jurnal penjualan (draf) | Klik Sales; Sales Journal Configuration; pilih mode otomatis untuk semua; aktifkan konfigurasi; simpan | Jurnal penjualan secara otomatis terbuat berdasarkan transaksi penjualan, status konfigurasi diaktifkan |
| Negatif — Konfigurasi jurnal penjualan tidak diterapkan (draf) | Tidak mengaktifkan Configuration Active; mencoba membuat jurnal penjualan | Muncul pesan penolakan yang jelas dan konfigurasi tidak berubah |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |

## 10. Diagram Alur Sales — Modul Sales

Bab manual: [`sales/10-diagram-alur-sales.md`](../../erpApiServices/docs/manualBook/sales/10-diagram-alur-sales.md)

| Skenario | Langkah dan data uji | Hasil yang diharapkan |
| --- | --- | --- |
| Positif — Quotation diterima oleh customer (draf) | Record Customer Accepted; Quotation ID OBT-001; Tanggal kesepakatan 2023-10-15; Persyaratan legal Draft | Status Quotation OBT-001: Legal Required, SO Created |
| Negatif — Sales Order tanpa Sales Delivery (draf) | Convert to SO; SO ID SO-001; Approve; Tidak ada Sales Delivery | Status SO SO-001: Unpaid, Stok tidak berubah |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Submitted -- Rejected: Ditolak |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | MenungguCustomer -- DitolakCustomer: Record Customer Declined |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | state "Ditolak Customer" as DitolakCustomer |
| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | Quotation hanya bisa di-Submit kalau semua item sudah punya harga lebih dari nol |
| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |
| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |
