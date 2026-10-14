# 01. Kartu Aksi, Draft, dan Urungkan

Setup: `ai_agent_write_enabled=true`, `ai_agent_autonomy_level=confirm_all`. Login sebagai Admin Uji (memegang izin keputusan aksi agen).

## Positif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 1.1 | Chat: "buatkan kontak pelanggan PT Maju Jaya" | Kartu "Buat kontak" berisi nama dan tipe; belum ada kontak baru di daftar |
| 1.2 | Tekan **Jalankan** | Kartu berstatus selesai; kontak muncul di daftar kontak cabang |
| 1.3 | Tekan **Urungkan** pada kartu tadi | Kontak hilang dari daftar; kartu berstatus dibatalkan/diurungkan |
| 1.4 | Chat: "buat purchase request 20 kopi tanggal besok" | Kartu menampilkan daftar item (SKU, qty) agar bisa diperiksa |
| 1.5 | Jalankan | PR berstatus **draft**, belum disubmit; ada di daftar PR |
| 1.6 | Ulangi untuk Quotation, Sales Order, Purchase Order (item dengan SKU dan harga) | Masing-masing draft; tidak ada yang disubmit atau disetujui |
| 1.7 | Chat: "buat jurnal manual debit kas 1.000.000 kredit modal" | Kartu berisi 2 baris; setelah Jalankan jurnal berstatus draft, **tidak diposting** |
| 1.8 | Chat: "buat tugas telpon supplier prioritas tinggi" lalu Jalankan | Tugas muncul di Proyek dan Tugas |
| 1.9 | Chat: "tambahkan catatan ke tugas tadi: sudah dihubungi" | Kartu catatan; setelah Jalankan catatan muncul di tugas |
| 1.10 | Setelah beberapa kartu, buka dasbor **AI Usage** | Bagian audit aksi memuat aksi tadi dengan status, pengguna, dan jumlah |
| 1.11 | Ubah `ai_agent_autonomy_level=auto_low_risk`, minta "buatkan kontak CV Baru" | Kontak dibuat **tanpa** kartu (berlabel tanpa konfirmasi) |
| 1.12 | Pada autonomy yang sama minta "buat purchase order ..." | Tetap muncul kartu (dokumen tidak pernah otomatis) |

## Negatif

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 1.13 | `ai_agent_write_enabled=false`, minta "buatkan kontak ..." | Asisten menjelaskan langkah dan menawarkan membuka halaman; tidak ada kartu |
| 1.14 | Login Staf Uji (tanpa izin keputusan aksi agen), minta membuat kontak | Tidak ada kartu; asisten mengarahkan ke halaman biasa |
| 1.15 | Biarkan kartu menganggur melewati masa berlaku, lalu Jalankan | Ditolak: kartu kedaluwarsa |
| 1.16 | Klik **Jalankan** dua kali cepat | Hanya satu kontak terbentuk |
| 1.17 | Minta kontak tanpa tipe (hanya nama) | Asisten menanyakan tipe; tidak ada kartu dengan data kurang |
| 1.18 | Periode akuntansi ditutup, minta jurnal draft di tanggal periode itu lalu Jalankan | Gagal dengan alasan dari aplikasi di kartu; tidak ada jurnal |
| 1.19 | Minta "setujui PO tadi" / "posting jurnal tadi" / "bayar faktur" | Asisten menolak dan mengarahkan ke halaman; tidak ada kartu |
| 1.20 | Batas: `ai_agent_max_amount_per_action=1000000`, minta PO senilai 5.000.000 | Ditolak dengan alasan batas agen; tidak ada kartu |
| 1.21 | `ai_agent_max_rows_per_action=2`, minta PR 3 item | Ditolak: terlalu banyak baris |
| 1.22 | Platform owner menyalakan saklar darurat (`ai_agent_write_kill_switch=true`) | Semua permintaan tulis ditolak di semua cabang; pertanyaan baca tetap dijawab |
| 1.23 | Urungkan kontak yang sudah dipakai di dokumen | Ditolak aplikasi; kartu tetap "selesai" dan alasannya tampil |

## Netralisasi

Matikan saklar darurat, kembalikan `ai_agent_autonomy_level=confirm_all`, hapus data uji (kontak, draft, tugas).
