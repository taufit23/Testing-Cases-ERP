import json, os, re, glob, time, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
ROOT = r"C:/Users/LGRta/Desktop/personalRoom/ERP/ERP/ERP_PROJECT/erpApiServices/docs/manualBook"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chapters.jsonl")
SPINE = """Perusahaan uji: PT Sehat Sentosa Farma (merek "Sentosa Farma"), grup usaha kesehatan, NPWP PKP, mata uang Rupiah. Cabang: (1) Kantor Pusat & Distribusi Jakarta (gudang obat dan alat kesehatan, penjualan grosir ke klinik dan apotek mitra, akuntansi pusat); (2) Apotek Sentosa Bandung (POS, resep, QRIS); (3) Klinik Pratama & Laboratorium Bekasi (jasa, kasir, tenaga medis); (4) Pabrik Herbal Sukabumi (produksi jamu dan racikan, bahan baku kalsium karbonat dari tambang kapur CV Kapur Medika); (5) Kafe Sehat di lobi klinik (restoran); layanan Sewa Alat Medis (kursi roda, tabung oksigen, tempat tidur pasien).
Contoh data: produk Paracetamol 500 mg strip (SKU OBT-001), Amoxicillin 500 mg (OBT-002, resep), Vitamin C 1000 mg botol (SUP-001), Masker Medis box 50 (ALK-001), Alkohol Swab (ALK-002), Jamu Kunyit Asam sachet (HRB-001); pemasok PT Bintang Farmasi Utama dan PT Alkes Prima Mandiri; pelanggan Klinik Pratama Harapan Sehat dan Apotek Mitra Sehat; peran: Apoteker Penanggung Jawab, Kepala Gudang, Kasir, Staf Pembelian, Manajer Keuangan, Direktur."""
FORMAT = """Tulis HANYA 2 baris tabel markdown dengan 3 kolom `| Skenario | Langkah dan data uji | Hasil yang diharapkan |`. Baris 1 diawali "Positif — " (jalur normal berhasil), baris 2 diawali "Negatif — " (input salah atau syarat tidak terpenuhi, harus ditolak dengan pesan jelas). Pakai nama entitas dari data perusahaan uji. Tiap sel maksimal 30 kata, Bahasa Indonesia, tanpa baris header, tanpa teks lain, tanpa blok kode."""

def fm(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    d = {}
    if m:
        for line in m.group(1).split("\n"):
            mm = re.match(r"^(title|description):\s*(.*)$", line)
            if mm: d[mm.group(1)] = mm.group(2).strip().strip("'\"")
    return d

def heads(text):
    return [h.strip() for h in re.findall(r"^#{2,3}\s+(.+)$", text, re.M)][:10]

def chat(prompt):
    body = {"model": "qwen2.5:7b-instruct", "stream": False, "options": {"num_ctx": 8192, "temperature": 0.3, "num_predict": 300},
            "messages": [{"role": "system", "content": SPINE}, {"role": "user", "content": prompt}]}
    req = urllib.request.Request("http://localhost:11434/api/chat", data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=900))["message"]["content"]

def work(item):
    mod, path = item
    t = open(path, encoding="utf-8").read()
    meta = fm(t)
    prompt = f"Fitur yang diuji (bab manual book modul {mod}): {meta.get('title','')}\nRingkasan: {meta.get('description','')}\nBagian bab: {'; '.join(heads(t))}\n\n{FORMAT}"
    t0 = time.time()
    try:
        out = chat(prompt)
    except Exception as e:
        out = ""
    rec = {"module": mod, "file": os.path.relpath(path, ROOT).replace("\\", "/"), "title": meta.get("title", ""), "rows": out, "secs": round(time.time() - t0, 1)}
    with open(OUT, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec

if __name__ == "__main__":
    done = set()
    if os.path.exists(OUT):
        for l in open(OUT, encoding="utf-8"):
            r = json.loads(l)
            if r["rows"]: done.add(r["file"])
    items = []
    for d in sorted(os.listdir(ROOT)):
        for p in sorted(glob.glob(os.path.join(ROOT, d, "*.md"))):
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            if rel not in done: items.append((d, p))
    print("todo", len(items), flush=True)
    with ThreadPoolExecutor(max_workers=3) as ex:
        for r in ex.map(work, items):
            print(r["file"], r["secs"], len(r["rows"]), flush=True)
