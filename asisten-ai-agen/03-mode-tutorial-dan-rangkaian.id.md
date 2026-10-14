# 03. Mode Tutorial dan Rangkaian Prosedur

Setup: `ai_tutorial_enabled=true`. Bab Manual Book ber-playbook sudah ada (hasil `ai:playbooks-scaffold`).

## Mode Tutorial

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 3.1 | Tekan tombol topi wisuda | Pita "Mode Tutorial" tampil; chat baru dimulai; tutor menawarkan modul yang tersedia |
| 3.2 | "Jelaskan modul Penjualan" | Penjelasan dari Manual Book; menyebut hanya modul yang aktif untuk akun |
| 3.3 | "Tunjukkan di mana membuat Sales Order" | Halaman dibuka dan tombol/bagian yang dibahas **disorot** sementara |
| 3.4 | "Ajak saya membuat Sales Order" | Tutor memberi satu langkah, menunggu, lalu memeriksa dan mengoreksi |
| 3.5 | Selesaikan pelajaran | Progres tercatat selesai; membuka lagi tidak mengembalikan ke "mulai" |
| 3.6 | Admin dengan izin progres membuka ringkasan progres tutorial cabang | Menampilkan pengguna, jumlah selesai/mulai, aktivitas terakhir |
| 3.7 | Di Mode Tutorial minta "buatkan kontak X" | Ditolak: tutorial hanya mengajar, tidak mengubah data |
| 3.8 | Akun tanpa menu Pembelian bertanya tentang Purchase Order | Disebut belum tersedia untuk akun; tidak diajarkan |
| 3.9 | `ai_tutorial_mention_locked_modules=false` | Modul yang tidak tersedia tidak disebut sama sekali |
| 3.10 | `ai_tutorial_enabled=false` | Tombol tutorial ditolak (pesan tutorial dimatikan cabang) |
| 3.11 | Tanya alur yang tidak ada di Manual Book | Tutor jujur "belum didokumentasikan", tidak mengarang |

## Rangkaian prosedur

| No | Langkah | Hasil yang diharapkan |
| --- | --- | --- |
| 3.12 | Chat: "mulai prosedur dari permintaan pembelian sampai pesanan" | Rangkaian dimulai; asisten mengajukan kartu PR draft dan berhenti |
| 3.13 | Katakan "sudah" **sebelum** menjalankan kartu | Rangkaian tidak maju (aksi belum benar-benar terjadi) |
| 3.14 | Jalankan kartu, lanjutkan | Maju ke langkah halaman (submit dan persetujuan oleh manusia) |
| 3.15 | Tutup chat, buka lagi besok, "lanjutkan prosedur tadi" | Posisi dan variabel (mis. slug PR) tetap; lanjut dari langkah terakhir |
| 3.16 | Minta rangkaian kedua saat satu masih berjalan | Ditolak kecuali diganti/dibatalkan |
| 3.17 | "Batalkan prosedur" | Status dibatalkan; tidak ada data yang ikut dihapus |
| 3.18 | Jalankan "checklist tutup bulan" | Langkah baca dijalankan sendiri; berhenti di tiap langkah manusia; **tidak menutup periode** sendiri |
| 3.19 | Jalankan "tutup sesi kasir" tanpa izin Kasir | Rangkaian tidak tersedia untuk akun |
