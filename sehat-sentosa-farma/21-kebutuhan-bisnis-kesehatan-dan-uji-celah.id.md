---
title: (PT Sehat Sentosa Farma) — 21. Kebutuhan Bisnis Kesehatan dan Uji Celah
category: sehat-sentosa-farma
description: Kasus uji yang dirancang dari kebutuhan nyata grup usaha kesehatan (bukan dari menu aplikasi). Setiap baris menyatakan dukungan aplikasi saat ini (ada, sebagian, belum, perlu verifikasi) dan, bila belum, merujuk ke nomor celah di file 95.
visibility: internal
---

# 21. Kebutuhan Bisnis Kesehatan dan Uji Celah

> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md) (sampai langkah 14). Kebutuhan berasal dari
> [`96`](./96-riset-kebutuhan-bisnis-grup-kesehatan.id.md). **Cara memakai:** jalankan tiap skenario di aplikasi. Bila hasilnya sama dengan kolom *Hasil yang diharapkan*,
> tandai lulus. Bila fiturnya tidak ada, **itu temuan, bukan kegagalan penguji**: catat nomor celah (kolom terakhir) dan lanjut; daftar lengkap usulan perbaikan ada di
> [`95`](./95-daftar-celah-dan-usulan-perbaikan.id.md).
>
> **Kolom *Dukungan sekarang*** hasil pemeriksaan kode dan skema database per 2026-10-20: **Ada** = ditemukan fiturnya, **Sebagian** = ada tetapi tidak
> menutup seluruh kebutuhan, **Belum** = tidak ditemukan saat pencarian di kode dan skema (verifikasi ulang di layar sebelum dipastikan), **Verifikasi** = tidak bisa
> dipastikan dari kode, harus dicoba. Kebutuhan yang bergantung pada peraturan ditandai **[reg]** dan harus dicek ke teks peraturannya.

## A. Obat: batch, kedaluwarsa dan penarikan (apotek, PBF, pabrik)

**Halaman terdekat:** `/purchasing/purchase-receipts`, `/inventory/stock-lots`, `/sales/sales-deliveries`, `/sales/sales-returns`, `/inventory/stock-history`. Untuk kebutuhan yang belum didukung, tidak ada halaman input khusus; yang diuji adalah apakah ada tempat untuk mengisinya.

| ID | Kebutuhan | Skenario uji (data acuan file `00`) | Hasil yang diharapkan dari ERP yang matang | Dukungan sekarang | Celah |
| --- | --- | --- | --- | --- | --- |
| A1 | Penerimaan dengan batch dan kedaluwarsa | GR OBT-001 2.000 strip: batch `PCT-2610A` kedaluwarsa 2028-10 untuk 1.200 strip dan batch `PCT-2611B` kedaluwarsa 2027-06 untuk 800 strip | Dua lot tercatat di gudang dengan nomor batch, tanggal produksi dan kedaluwarsa masing-masing | **Sebagian**: lot punya nomor, tanggal produksi, kedaluwarsa, status (aktif, kedaluwarsa, karantina, habis); pengisian saat penerimaan perlu diverifikasi di layar GR | G02 |
| A2 | Keluar mengikuti FEFO | Kirim 600 strip OBT-001 ke CUS-01 tanpa memilih lot | Sistem mengambil `PCT-2611B` (kedaluwarsa lebih dekat) lebih dulu | **Sebagian**: strategi FEFO ada untuk produk berbiaya identifikasi khusus; produk metode rata-rata atau FIFO tidak otomatis FEFO | G02 |
| A3 | Peringatan mendekati kedaluwarsa | Buka daftar stok dengan lot yang kedaluwarsa dalam 6, 3 dan 1 bulan | Laporan atau dasbor menampilkan lot mendekati kedaluwarsa per gudang dengan nilai persediaannya | **Belum**: tidak ditemukan laporan, dasbor atau notifikasi kedaluwarsa persediaan (hanya ada untuk lisensi aplikasi dan tambang) | G01 |
| A4 | Lot kedaluwarsa otomatis berhenti dipakai | Majukan tanggal ke setelah kedaluwarsa `PCT-2611B` lalu jual atau transfer | Lot menjadi kedaluwarsa otomatis, tidak bisa dijual atau ditransfer, dan nilainya bisa dihapus lewat penyesuaian | **Belum**: status lot hanya diubah manual; tidak ada proses terjadwal; jual dari lot kedaluwarsa perlu diverifikasi | G02 |
| A5 | Karantina | Tandai batch `PCT-2610A` karantina karena laporan mutu | Stok batch itu tidak muncul di stok tersedia dan tidak bisa dijual tetapi tetap terlihat di laporan | **Sebagian**: status karantina ada di lot; efek ke ketersediaan perlu diverifikasi | G02 |
| A6 | Penelusuran batch ke pelanggan (recall) | BPOM menarik batch `PCT-2610A`: cari semua pelanggan yang menerima batch itu | Laporan satu layar: batch, pengiriman, pelanggan, jumlah, tanggal, kontak; bisa membuat retur massal | **Belum**: tidak ada laporan penelusuran batch dua arah; hanya penerimaan dan pengeluaran per lot | G03 |
| A7 | Pemusnahan obat kedaluwarsa | Musnahkan 50 strip kedaluwarsa dengan berita acara | Penyesuaian stok dengan alasan "kedaluwarsa", jurnal beban, lampiran berita acara | **Sebagian**: penyesuaian stok dengan alasan dan lampiran ada; alasan khusus dan format berita acara tidak ada | G02 |
| A8 | Retur ke pemasok karena kedaluwarsa atau rusak | Retur 100 strip batch bermasalah ke SUP-01 | Retur pembelian mengurangi stok dan utang; nomor batch ikut tercatat di dokumen | **Ada** (retur pembelian); pencatatan batch di dokumen retur perlu diverifikasi | G03 |
| A9 | Batch di kasir apotek | Jual Paracetamol di POS dengan dua batch tersedia | Kasir otomatis mengambil batch terdekat kedaluwarsa dan struk/riwayat mencatat batch | **Belum**: transaksi POS tidak memilih lot | G04 |
| A10 | Konsinyasi dengan pemasok | Barang titipan SUP-01 di Apotek Bandung, bayar saat terjual | Hutang muncul hanya untuk yang terjual; sisa dapat dikembalikan | **Ada**: penyelesaian konsinyasi dan penanda konsinyasi di kontak dan lot | — |

## B. Obat terkontrol, resep dan pelayanan apotek

**Halaman terdekat:** `/pos/pos-transactions/create`, `/client-master/products`, `/inventory/stock-history`. Untuk kebutuhan yang belum didukung, tidak ada halaman input khusus; yang diuji adalah apakah ada tempat untuk mengisinya.

| ID | Kebutuhan | Skenario uji | Hasil yang diharapkan | Dukungan sekarang | Celah |
| --- | --- | --- | --- | --- | --- |
| B1 | Golongan obat | Tandai OBT-002 sebagai obat keras, OBT-001 obat bebas, buat produk psikotropika uji | Produk punya golongan (bebas, bebas terbatas, keras, narkotika, psikotropika, prekursor, OOT) yang tampil di POS dan laporan | **Belum**: produk hanya punya merek dan pajak | G05 |
| B2 | Obat keras wajib resep **[reg]** | Jual OBT-002 di POS tanpa data resep | Ditolak atau memerlukan persetujuan Apoteker dengan alasan tercatat | **Belum** | G05, G06 |
| B3 | Data resep | Resep dr. Andi: pasien Budi, OBT-002 × 10, aturan pakai 3×1 | Penjualan terkait resep (dokter, pasien, tanggal, aturan pakai), salinan resep dan etiket obat dapat dicetak | **Belum**: tidak ada entitas resep, dokter atau pasien di penjualan | G06 |
| B4 | Racikan | Puyer 10 bungkus dari 3 obat dengan biaya racik per bungkus | Harga = bahan + tuslah/embalase; stok tiap bahan berkurang proporsional; satu baris racikan di struk | **Belum**: produksi (BOM) ada di modul manufaktur pabrik tetapi bukan untuk racikan di kasir | G07 |
| B5 | Pelaporan narkotika dan psikotropika **[reg]** | Satu bulan mutasi stok psikotropika uji | Laporan mutasi per produk (awal, masuk, keluar, akhir) yang bisa dipakai mengisi SIPNAP | **Belum** (laporan mutasi stok umum ada; format dan golongan tidak) | G08 |
| B6 | Batas harga | Atur HET OBT-001 Rp 6.500 lalu coba jual Rp 8.000 | Ditolak atau diperingatkan; margin per golongan terlihat | **Belum** (ada peringatan jual di bawah modal, bukan batas atas) | G09 |
| B7 | PPN campuran per produk **[reg]** | Satu transaksi memuat obat bebas PPN dan alkes kena PPN | Pajak dihitung per baris sesuai pajak produk; ringkasan pajak memisahkan DPP kena dan tidak kena | **Sebagian**: produk punya pajak sendiri; pemisahan dan aturan terkini perlu diverifikasi | G10 |
| B8 | Nomor izin edar produk | Isi NIE/TR, masa berlaku, produsen, kemasan | Data registrasi tersimpan di produk dan bisa dicetak di dokumen | **Belum** | G11 |
| B9 | Promo dan member apotek | Diskon member silver 5% untuk vitamin | Harga mengikuti tingkat member dan promo | **Ada** (tingkat member, promo SKU, cashback) | — |
| B10 | Struk dan label | Cetak struk berisi nama apotek, APJ, nomor izin | Struk memuat identitas apotek dan APJ sesuai pengaturan cabang | **Verifikasi** | G24 |

## C. PBF dan distribusi

**Halaman terdekat:** `/purchasing/purchase-invoices`, `/sales/sales-invoices`, `/canvassing/sales-stock-custodies`, `/client-master/contacts`. Untuk kebutuhan yang belum didukung, tidak ada halaman input khusus; yang diuji adalah apakah ada tempat untuk mengisinya.

| ID | Kebutuhan | Skenario uji | Hasil yang diharapkan | Dukungan sekarang | Celah |
| --- | --- | --- | --- | --- | --- |
| C1 | Kualifikasi pelanggan | Daftarkan CUS-02 dengan izin Apotek bermasa berlaku 2027-03 | Dokumen izin pelanggan tersimpan; penjualan obat keras diblokir bila izin kedaluwarsa | **Belum**: ada syarat dokumen hukum per penawaran (NDA, PKS), bukan izin sarana | G12 |
| C2 | Surat pesanan khusus **[reg]** | Pesanan narkotika dari apotek mitra | SP khusus bernomor, tertanda APJ, dilampirkan ke pesanan, dilaporkan | **Belum** | G13 |
| C3 | Pengiriman dan bukti terima | Kirim 600 strip ke CUS-01 dan unggah tanda terima | Delivery, status, bukti terima, selisih diterima | **Ada** (delivery penjualan, lampiran) | — |
| C4 | Rantai dingin | Pengiriman vaksin 2–8 °C | Log suhu penyimpanan dan pengiriman, peringatan penyimpangan, karantina otomatis | **Belum** | G14 |
| C5 | Batas kredit dan umur piutang apotek mitra | CUS-02 melebihi batas Rp 10.000.000 | Pesanan baru ditahan atau ditolak sesuai konfigurasi | **Ada** | — |
| C6 | Penagihan lapangan | Dewi menagih Apotek Mitra Sehat dan menyetor | Penagihan lapangan, setoran, jurnal | **Ada** (kanvasing) | — |
| C7 | Diskon bertingkat dan termin pemasok | Faktur SUP-01 dengan diskon tunai 2% bila lunas 10 hari | Jurnal diskon otomatis saat bayar dalam batas | **Belum**: hanya hari termin per kontak | G32 |
| C8 | Faktur pemasok ganda | Input dua kali faktur PBF dengan nomor pemasok sama | Peringatan atau penolakan faktur ganda | **Belum**: faktur pembelian tidak menyimpan nomor faktur pemasok | G31 |

## D. Klinik pratama dan laboratorium

**Halaman terdekat:** `/pos/pos-transactions/create`, `/client-master/contacts`, `/hrm/commission-rules`. Untuk kebutuhan yang belum didukung, tidak ada halaman input khusus; yang diuji adalah apakah ada tempat untuk mengisinya.

| ID | Kebutuhan | Skenario uji | Hasil yang diharapkan | Dukungan sekarang | Celah |
| --- | --- | --- | --- | --- | --- |
| D1 | Master pasien dan nomor rekam medis | Daftarkan pasien baru "Siti" dengan NIK dan nomor RM unik | Pasien tunggal terdaftar; pencarian cepat; pasien lama dikenali | **Belum**: hanya kontak umum, tanpa data klinis | G15 |
| D2 | Pendaftaran dan antrean | Siti mendaftar poli umum dr. Andi | Nomor antrean, status antrean, jadwal dokter | **Belum** (reservasi meja ada untuk restoran, bukan klinik) | G16 |
| D3 | Rekam medis elektronik **[reg]** | Dokter mencatat anamnesis, diagnosis (ICD), tindakan, resep | Catatan tersimpan, akses hanya tenaga berwenang, bisa dikirim ke SATUSEHAT | **Belum** | G17 |
| D4 | Tarif tindakan per penjamin | Konsultasi umum: pasien umum Rp 80.000, BPJS tidak ditagih per tindakan | Tarif mengikuti penjamin pasien | **Sebagian**: daftar harga per pelanggan dan layanan sebagai produk jasa ada; tidak terhubung ke penjamin pasien | G18 |
| D5 | Billing pasien | Total konsultasi + obat + tindakan menjadi satu tagihan dibayar tunai atau QRIS | Satu tagihan gabungan, pembayaran, kwitansi | **Sebagian**: dapat dibuat di kasir sebagai transaksi biasa; tanpa kunjungan sebagai induk | G18 |
| D6 | Jasa medis dokter | dr. Andi mendapat 60% dari tarif tindakan dan 30% dari konsultasi | Perhitungan jasa per tindakan, rekap bulanan, hutang jasa, pembayaran, PPh 21 | **Sebagian**: aturan komisi ada untuk penjualan; bukan untuk tindakan medis | G19 |
| D7 | Klaim penjamin | Tagihan asuransi PT Asuransi Sejahtera untuk 12 pasien | Piutang per penjamin, status klaim, pembayaran sebagian, penolakan | **Sebagian**: piutang dan faktur ke pelanggan korporat ada; tidak ada alur klaim | G20 |
| D8 | Kapitasi BPJS **[reg]** | Pendapatan kapitasi bulanan berdasarkan peserta terdaftar | Pendapatan kapitasi diakui flat per bulan, integrasi P-Care | **Sebagian**: bisa lewat jurnal manual (lihat suite `accounting-klinik-*`); tanpa P-Care | G21 |
| D9 | Order laboratorium | Dokter meminta pemeriksaan darah lengkap | Order, spesimen, hasil, validasi, pengiriman hasil ke dokter | **Belum** | G22 |
| D10 | Reagen laboratorium | Reagen lot `RG-77` kedaluwarsa 2027-01, pemakaian per pemeriksaan | Stok reagen per lot, pengurangan per pemeriksaan | **Sebagian**: stok lot ada; pemakaian per pemeriksaan tidak | G22 |
| D11 | Kalibrasi dan QC alat lab | Jadwal kalibrasi analyzer tiap 6 bulan | Pengingat dan riwayat kalibrasi | **Belum** | G28 |

## E. Produksi obat tradisional (Pabrik Herbal)

**Halaman terdekat:** `/manufacturing/boms`, `/manufacturing/production-orders`, `/inventory/stock-lots`. Untuk kebutuhan yang belum didukung, tidak ada halaman input khusus; yang diuji adalah apakah ada tempat untuk mengisinya.

| ID | Kebutuhan | Skenario uji | Hasil yang diharapkan | Dukungan sekarang | Celah |
| --- | --- | --- | --- | --- | --- |
| E1 | Formula dan perubahan formula | Revisi BOM Jamu Kunyit Asam (kunyit 20 kg menjadi 22 kg) | Versi formula baru berlaku mulai tanggal tertentu, pesanan lama memakai versi lama | **Verifikasi** (BOM ada; versi perlu dicoba) | G27 |
| E2 | Batch record | Produksi 2 batch; catat bahan lot mana dipakai, operator, hasil | Catatan batch memuat lot bahan, operator, waktu, hasil, penyimpangan | **Sebagian**: pesanan produksi dan persediaan berlot ada; pencatatan lot bahan per batch dan operator perlu diverifikasi | G26 |
| E3 | Pelepasan mutu (QC release) | Hasil uji batch belum keluar | Barang jadi berstatus karantina sampai QC melepas | **Sebagian**: status lot karantina ada; alur QC tidak | G26 |
| E4 | Penelusuran bahan baku ke produk jadi | Kalsium karbonat batch `KAL-77` dipakai di batch suplemen mana | Laporan maju dan mundur | **Belum** | G03, G26 |
| E5 | Toleransi dan bahan kurang | Produksi melebihi rencana 5%; bahan kurang saat selesai | Toleransi ditegakkan; selesai ditolak bila bahan kurang bila saklar menyala | **Ada** (toleransi produksi dan kendali penyelesaian) | — |
| E6 | Registrasi produk dan label **[reg]** | Isi TR dan masa berlaku, cetak label dengan batch dan kedaluwarsa | Label dengan nomor izin edar, batch, kedaluwarsa | **Belum** (label produk dasar ada) | G11 |
| E7 | Bahan baku dari tambang | Kalsium karbonat dari tambang kapur masuk persediaan bahan baku | Log tambang jadi stok bahan baku | **Ada** (stockpile dan penjualan bijih) | — |

## F. Alat kesehatan dan sewa

**Halaman terdekat:** `/rental/assets`, `/rental/orders`, `/fixed-assets/assets`. Untuk kebutuhan yang belum didukung, tidak ada halaman input khusus; yang diuji adalah apakah ada tempat untuk mengisinya.

| ID | Kebutuhan | Skenario uji | Hasil yang diharapkan | Dukungan sekarang | Celah |
| --- | --- | --- | --- | --- | --- |
| F1 | Sewa harian dan deposit | Sewa kursi roda 3 unit 7 hari, deposit, denda | Pesanan sewa, deposit, pengembalian dikurangi denda | **Ada** | — |
| F2 | Jadwal kalibrasi dan servis aset | Tabung oksigen wajib uji hidrostatik tiap 5 tahun; alat ukur kalibrasi tahunan | Pengingat jatuh tempo, riwayat servis, aset tidak bisa disewa bila kalibrasi lewat | **Belum** | G28 |
| F3 | Isi ulang berulang | Pelanggan tetap mengisi ulang tabung 6 m³ tiap minggu | Pesanan berulang atau layanan isi ulang dengan penukaran tabung | **Verifikasi** (sewa berbasis pemakaian ada) | G28 |
| F4 | Izin edar alat | AKL/AKD per alat dijual | Data izin edar di produk | **Belum** | G11 |

## G. SDM tenaga kesehatan

**Halaman terdekat:** `/hrm/employees`, `/hrm/shifts`, `/hrm/leave-requests`. Untuk kebutuhan yang belum didukung, tidak ada halaman input khusus; yang diuji adalah apakah ada tempat untuk mengisinya.

| ID | Kebutuhan | Skenario uji | Hasil yang diharapkan | Dukungan sekarang | Celah |
| --- | --- | --- | --- | --- | --- |
| G1 | Masa berlaku STR dan SIP | Apt. Lestari STR berlaku sampai 2027-02, SIP 2027-02 | Dokumen kompetensi per karyawan dengan masa berlaku dan peringatan 90/60/30 hari; tidak boleh dijadwalkan bila kedaluwarsa | **Belum** (ada lampiran dan data karyawan, tanpa jenis izin bermasa berlaku) | G23 |
| G2 | Shift jaga | Jadwal shift pagi, siang, malam dan jaga on-call klinik | Jadwal kerja per shift, absensi, lembur | **Ada** (shift, jadwal kerja, aturan absensi) | — |
| G3 | Honor dokter dan PPh 21 | Dokter paruh waktu dibayar per tindakan | Slip/honor dengan PPh 21 sesuai status | **Sebagian**: payroll ada untuk karyawan; honor per tindakan tidak | G19 |
| G4 | Rekrutmen tenaga medis | Lowongan Apoteker Pendamping, syarat STR | Lamaran dari halaman karier dengan CV | **Ada** (syarat STR hanya sebagai teks kualifikasi) | — |

## H. Keuangan, pajak dan grup

**Halaman terdekat:** `/accounting/journals`, `/reports/tax-summary`, `/client-master/branch-manage`, `/reports/*`. Untuk kebutuhan yang belum didukung, tidak ada halaman input khusus; yang diuji adalah apakah ada tempat untuk mengisinya.

| ID | Kebutuhan | Skenario uji | Hasil yang diharapkan | Dukungan sekarang | Celah |
| --- | --- | --- | --- | --- | --- |
| H1 | Banyak badan hukum | PBF, apotek dan klinik berbadan hukum berbeda | Pembukuan per entitas dengan laporan gabungan dan eliminasi transaksi antar entitas | **Sebagian**: cabang utama dengan laporan cabang anak; badan hukum terpisah dan eliminasi tidak ada | G29 |
| H2 | Penjualan antar entitas | PBF menjual ke apotek grup | Faktur antar entitas yang terhubung dan tereliminasi di laporan gabungan | **Belum** | G29 |
| H3 | Laba per lini usaha dan dokter | Laba Rugi per cabang dan per unit bisnis; laba per dokter | Laporan margin per dimensi | **Sebagian**: unit bisnis dan pusat biaya ada; dimensi dokter/penjamin tidak | G30 |
| H4 | Faktur pajak elektronik | Faktur penjualan grosir kena PPN | Data faktur pajak siap diunggah | **Sebagian**: ada data TKU kontak dan pencatatan pajak; keluaran e-faktur perlu diverifikasi | G10 |
| H5 | Selisih kurs impor bahan baku | Beli bahan baku valas | Selisih kurs saat bayar | **Sebagian**: hanya faktur biaya logistik | G35 |
| H6 | Periode terkunci setelah audit | Kunci Oktober setelah diaudit | Tidak ada perubahan lagi; pembukaan hanya dengan izin khusus | **Sebagian**: kunci ada tetapi bisa dibuka kembali | G33 |
| H7 | Pembayaran melalui QRIS menunggu settlement | QRIS terbayar, dana masuk H+1 | Akun penampung sampai dana diterima | **Sebagian**: ada penyelesaian dan akun penampung penyedia untuk gateway; akun penampung per metode tidak | G34 |

## I. Kepatuhan dan mutu

**Halaman terdekat:** `/client-master/legal-document-types`, `/client-master/data-subject-requests`, `/core/attachment`. Untuk kebutuhan yang belum didukung, tidak ada halaman input khusus; yang diuji adalah apakah ada tempat untuk mengisinya.

| ID | Kebutuhan | Skenario uji | Hasil yang diharapkan | Dukungan sekarang | Celah |
| --- | --- | --- | --- | --- | --- |
| I1 | Izin usaha per cabang | SIA Apotek, izin klinik, sertifikat CDOB pusat dengan masa berlaku | Daftar izin per cabang, peringatan perpanjangan, dokumen terlampir | **Belum** | G24 |
| I2 | Limbah medis B3 | Pencatatan limbah klinik per minggu dan manifes pengangkutan | Catatan volume, pengangkut, manifes | **Belum** | G25 |
| I3 | Persetujuan data pasien dan retensi | Persetujuan pengolahan data pasien, anonimisasi sesuai retensi | Persetujuan tersimpan; data dianonimkan sesuai masa simpan | **Sebagian**: persetujuan data pribadi pelamar dan anonimisasi karyawan ada; data pasien tidak ada | G15 |
| I4 | Dokumen akreditasi klinik | Proyek akreditasi dengan tugas, bukti, tenggat | Tugas, lampiran, persetujuan, laporan | **Ada** (proyek dan tugas) | — |
| I5 | Jejak audit | Ubah data stok sensitif | Siapa, kapan, sebelum dan sesudah | **Ada** (jejak aktivitas) | — |

## Cara menilai hasil suite ini

1. Hitung baris per status dukungan; **Ada** harus lulus. Bila baris berstatus **Ada** gagal, itu **bug**.
2. Baris **Sebagian** dan **Verifikasi**: catat tepat bagian yang kurang (di kolom komentar penguji) lalu perbarui status di file `95`.
3. Baris **Belum** yang ternyata ada: koreksi status di sini. Pencarian kode bisa salah; layar adalah sumber kebenaran.
4. Prioritas perbaikan ditentukan di file `95` berdasarkan dampak bisnis dan ketergantungan regulasi.
