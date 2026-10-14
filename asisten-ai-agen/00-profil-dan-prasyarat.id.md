# Asisten AI Agen: Profil dan Prasyarat

Suite ini menguji kemampuan lanjutan asisten AI: kartu aksi (draft + Urungkan), pengisian form, Mode Tutorial, rangkaian prosedur, saran proaktif, pertanyaan terjadwal, tata kelola, dan Mode Penguji. Rujukan: `erpApiServices/docs/plan-ai-agent-aksi-mandiri.id.md` dan bab Manual Book `core/05-agen-ai-aksi-tutorial-dan-jadwal.md`.

## Skenario

| Peran | Nama | Keterangan |
| --- | --- | --- |
| Platform owner | lgrtaufit@gmail.com | Mode Penguji, saklar darurat |
| Admin cabang | Admin Uji | Menyalakan setup cabang, memegang izin keputusan aksi agen |
| Staf penjualan | Staf Uji | Hanya izin Sales (tanpa izin agen) untuk kasus negatif |

## Prasyarat

1. `migrate:all`, `seed:all`, `permission:sync --all` sudah dijalankan (izin `client-master.ai-agent-actions.decide` dan `client-master.ai-tutorial.progress` baru ada setelah sync).
2. Penyedia AI aktif di Integrasi dan pengungkapan AI sudah dikonfirmasi admin cabang.
3. Data master minimal di cabang uji: 1 pelanggan, 1 pemasok, 2 SKU berstok, 1 departemen, akun COA standar.
4. Setup cabang awal: `ai_assistant_enabled=true`, `ai_assistant_agent_mode=true`. Setup lain sesuai kasus.
5. Hard refresh browser (Ctrl+Shift+R) setelah deploy FE.

## Cakupan dan batas

- **Tercakup:** semua kemampuan di atas, termasuk batas dan penolakannya.
- **Tidak tercakup, memang belum ada:** Mode Tutorial tingkat Peragakan (data latihan), adaptor MCP untuk klien AI luar, streaming huruf demi huruf.
- **Catatan hasil:** jawaban model bisa berbeda antar penyedia; yang dinilai adalah **perilaku sistem** (kartu, izin, batas, catatan), bukan kata-kata persis.

## Urutan

| File | Isi |
| --- | --- |
| `01-kartu-aksi-draft-dan-urungkan.id.md` | Kartu konfirmasi, draft lintas modul, Urungkan, batas |
| `02-isi-form-dan-perbaikan-error.id.md` | Page bridge, isi form, Urungkan isian, perbaiki error |
| `03-mode-tutorial-dan-rangkaian.id.md` | Tutorial tingkat 1 sampai 3, rangkaian dengan titik berhenti |
| `04-proaktif-jadwal-dan-tata-kelola.id.md` | Saran, jadwal, batas per peran, saklar darurat, Mode Penguji |
