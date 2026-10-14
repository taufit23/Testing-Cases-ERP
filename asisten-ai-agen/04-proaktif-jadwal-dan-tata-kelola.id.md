# 04. Saran Proaktif, Jadwal, Tata Kelola, dan Mode Penguji

## Saran proaktif (`ai_agent_proactive_enabled=true`)

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 4.1 | Siapkan: 1 tugas terlambat milik user terkait karyawan, 1 jurnal draft berumur lebih dari 3 hari, SKU di bawah titik pesan ulang | Buka widget (chat kosong): bagian "perlu perhatian" menampilkan tiga sinyal dengan jumlahnya |
| 4.2 | Ketuk satu sinyal | Dikirim sebagai pertanyaan; asisten menjawab dari data |
| 4.3 | Cabut izin daftar jurnal dari peran, buka widget lagi | Sinyal jurnal tidak muncul |
| 4.4 | `ai_agent_proactive_enabled=false` | Tidak ada sinyal |

## Pertanyaan terjadwal (`ai_agent_schedules_enabled=true`)

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 4.5 | "Setiap hari jam 08:00 cek barang di bawah titik pesan ulang" | Jadwal dibuat; "tampilkan jadwal saya" menampilkannya dengan jam berikutnya |
| 4.6 | Jalankan `php artisan ai:run-scheduled-prompts` setelah memajukan waktunya | Percakapan baru "[Terjadwal] ..." di riwayat; jadwal maju ke slot berikutnya |
| 4.7 | Buat jadwal ke-6 | Ditolak: batas 5 per pengguna |
| 4.8 | Jadwal berisi "buatkan kontak ..." lalu dijalankan | Tidak ada kontak dibuat; jawaban menjelaskan bahwa jalan terjadwal hanya membaca |
| 4.9 | `ai_agent_schedules_enabled=false` lalu jalankan runner | Jadwal dilewati dan tetap maju |
| 4.10 | "Hapus jadwal nomor 1" | Jadwal hilang dari daftar |

## Tata kelola

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 4.11 | `ai_agent_allowed_actions=contacts.search` | Permintaan membuat kontak ditolak; pencarian kontak tetap jalan |
| 4.12 | `ai_agent_role_limits` untuk peran Admin: `{"<id>":{"max_amount":1000000}}` sementara batas cabang 5.000.000 | Berlaku 1.000.000 (peran lebih ketat) |
| 4.13 | Peran meminta batas lebih longgar dari cabang | Batas cabang tetap berlaku |
| 4.14 | `ai_assistant_daily_message_limit=3`, kirim pesan ke-4 oleh user biasa | Ditolak ramah (HTTP 429) dengan pesan anggaran harian habis |
| 4.15 | `ai_agent_strong_model` diisi | Giliran yang menulis memakai model itu; tanya jawab tetap model bawaan |
| 4.16 | Login platform owner, aktifkan Mode Penguji (ikon labu) | Pita "Mode Penguji", pilihan model/peran/gangguan tampil |
| 4.17 | Kirim pertanyaan dengan model lokal | Jawaban datang; panel "Langkah" memuat panggilan model dan tool beserta waktunya |
| 4.18 | Simpan jawaban sebagai skenario, buka `/dashboard/ai-tester`, jalankan | Skenario lulus; ubah gangguan ke "tool call rusak" lalu jalankan: gagal dengan alasan |
| 4.19 | Akun non-owner memanggil endpoint Mode Penguji | 403 |
| 4.20 | Mode Penguji: minta aksi tulis | Ditolak (terkunci) kecuali `AI_TESTER_ALLOW_WRITE=true`, dan itu pun hanya kartu |
| 4.21 | Simulasi peran Staf Uji | Asisten hanya melihat menu dan data yang boleh peran itu |

## Netralisasi

Kembalikan semua setup `ai_agent_*` ke bawaan, hapus jadwal dan skenario uji, matikan Mode Penguji.
