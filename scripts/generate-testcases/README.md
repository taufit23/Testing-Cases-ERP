# Pembuat draf kasus uji (Ollama lokal)

1. `gen.py`: untuk setiap bab di `erpApiServices/docs/manualBook/*/*.md`, minta Ollama (`qwen2.5:7b-instruct`, `http://localhost:11434`) merancang 1 baris Positif dan 1 baris Negatif berdasarkan judul, ringkasan dan daftar bagian bab, memakai data perusahaan uji (konstanta `SPINE`). Hasil ditambahkan ke `chapters.jsonl` di folder skrip (bisa dilanjutkan bila terputus). 3 permintaan paralel, sekitar 6 bab per menit.
2. `assemble.py`: menyaring baris (membuang pesan error karangan model), menambah aturan larangan/kewajiban yang dikutip langsung dari bab manual, baris izin dan netralisasi, lalu menulis `sehat-sentosa-farma/02..20` dan `99-peta-cakupan`. File `00`, `01` dan `98` ditulis tangan.

Path di skrip masih absolut untuk mesin ini; ubah konstanta `ROOT`, `DEST`, `MANUAL_DIR` bila dipindah. Baris dari Ollama selalu berlabel `(draf)`: model 7B bisa mengarang perilaku, jadi penguji wajib memeriksanya.
