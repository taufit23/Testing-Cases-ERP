# Prompt sesi cloud untuk pengujian ERP

Berkas di folder ini adalah prompt siap pakai untuk sesi cloud Claude Code (memakai kredit sesi cloud). Dijalankan **dari folder repo backend**
(`erpApiServices`), karena sesi cloud hanya melihat satu repo. Semua repo harus sudah di-push; sesi mengkloning dari GitHub, bukan dari mesinmu.

## Sebelum mulai (sekali)

1. `claude auth login` (harus akun claude.ai, bukan API key).
2. GitHub terhubung: jalankan `/web-setup` di terminal Claude Code, atau lewat onboarding claude.ai/code.
3. Environment di claude.ai/code: jaringan **Trusted**, variabel `DB_CONNECTION=pgsql DB_HOST=127.0.0.1 DB_USERNAME=postgres DB_PASSWORD=postgres DB_DATABASE=erp_test`.
   Tanpa environment khusus, sesi memakai Default; prompt sudah menyuruh sesi menyalakan Postgres sendiri, jadi ini boleh dilewati untuk Sesi 0.
4. Jangan isi kunci produksi atau kunci AI di environment. Tes memakai penyedia palsu.

## Sesi 0: bukti lingkungan dan peta celah (jalankan dulu, paling murah)

Git Bash:

```bash
cd /c/Users/LGRta/Desktop/personalRoom/ERP/ERP/ERP_PROJECT/erpApiServices
claude --cloud "$(cat ../Testing-Cases-ERP/cloud-prompts/sesi-0-peta-celah.md)"
```

PowerShell:

```powershell
cd C:\Users\LGRta\Desktop\personalRoom\ERP\ERP\ERP_PROJECT\erpApiServices
claude --cloud (Get-Content ..\Testing-Cases-ERP\cloud-prompts\sesi-0-peta-celah.md -Raw)
```

Hasilnya: branch `test/peta-celah` berisi `docs/peta-celah-tes.id.md`, dan balasan ringkas (lingkungan berhasil atau tidak, tiga hasil tes, 8 modul teratas).
**Catat angka kredit di halaman usage sebelum dan sesudah** untuk mengukur biaya satu sesi.

## Sesi modul: tulis tes dari dokumen uji

Setelah Sesi 0, pilih modul dari rekomendasinya. `templat-tes-modul.md` punya lima isian; sesi mengkloning repo dokumen uji sendiri (bila gagal, dia berhenti dan melapor).

| Modul | `{{MODUL}}` | `{{SLUG}}` | `{{FILE_DOKUMEN}}` | `{{LANGKAH_01}}` | `{{NAMA_BERKAS}}` |
| --- | --- | --- | --- | --- | --- |
| Pembelian | Pembelian | pembelian | `05-pembelian.id.md` | 6 sampai 10 | PembelianCelah |
| Persediaan | Persediaan | persediaan | `06-persediaan.id.md` | 7, 11, dan 22 | PersediaanCelah |
| Penjualan | Penjualan | penjualan | `07-penjualan.id.md` | 12 sampai 14 | PenjualanCelah |
| Kanvasing | Kanvasing | kanvasing | `08-kanvasing.id.md` | 15 dan 16 | KanvasingCelah |
| POS | POS | pos | `09-pos.id.md` | 17 dan 18 | PosCelah |
| Restoran | Restoran | restoran | `10-restoran.id.md` | 19 | RestoranCelah |
| Manufaktur | Manufaktur | manufaktur | `11-manufaktur.id.md` | 21 | ManufakturCelah |
| Pertambangan | Pertambangan | pertambangan | `12-pertambangan.id.md` | 20 | PertambanganCelah |
| Sewa | Sewa | sewa | `13-sewa.id.md` | 23 | SewaCelah |
| Akuntansi | Akuntansi | akuntansi | `14-akuntansi-dan-aset-tetap.id.md` | 5, 27, dan 29 | AkuntansiCelah |
| Keuangan | Keuangan | keuangan | `15-keuangan.id.md` | 14 dan 28 | KeuanganCelah |
| SDM | SDM | sdm | `16-sdm.id.md` | 24 dan 25 | SdmCelah |
| Proyek | Proyek | proyek | `17-proyek-dan-tugas.id.md` | 26 | ProyekCelah |

PowerShell (contoh Pembelian):

```powershell
$p = (Get-Content ..\Testing-Cases-ERP\cloud-prompts\templat-tes-modul.md -Raw).
  Replace('{{MODUL}}','Pembelian').Replace('{{SLUG}}','pembelian').
  Replace('{{FILE_DOKUMEN}}','05-pembelian.id.md').Replace('{{LANGKAH_01}}','6 sampai 10').
  Replace('{{NAMA_BERKAS}}','PembelianCelah')
claude --cloud $p
```

## Aturan jalan

- **Dua sampai tiga sesi sekaligus**, tidak lebih. Sesi paralel memakai batas laju paket Pro bersama; pantau halaman usage.
- Setiap sesi bekerja di branch `test/<slug>` dan tidak menyentuh `main` (deploy otomatis berasal dari `main`).
- Tinjau di claude.ai/code: lihat diff, buat PR, jalankan berkas tesnya di mesinmu sebelum menggabungkan.
- Bug yang ditemukan sesi dicatat di `docs/laporan-tes-<slug>.id.md` dan **tidak diperbaiki** oleh sesi; perbaikannya keputusan terpisah.
- Kredit habis 5 November 2026; jangan menjadwalkan apa pun sesudahnya.
