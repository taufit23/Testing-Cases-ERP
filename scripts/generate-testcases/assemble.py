import json, os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__))
DEST = r"C:/Users/LGRta/Desktop/personalRoom/ERP/ERP/ERP_PROJECT/Testing-Cases-ERP/sehat-sentosa-farma"
MANUAL_DIR = r"C:/Users/LGRta/Desktop/personalRoom/ERP/ERP/ERP_PROJECT/erpApiServices/docs/manualBook/"
MAN = "erpApiServices/docs/manualBook/"

# nomor file -> (slug, judul, folder manual, ringkasan, titik uji kunci)
FILES = {
 "02": ("platform-dan-akun", "Platform Owner, Mulai Menggunakan dan Pengaturan Akun", ["platform-owner", "mulai-menggunakan", "pengaturan-akun"],
   "Dari penjualan aplikasi ke klien sampai pengguna pertama masuk.",
   ["Paket menentukan modul dan batas (cabang, pengguna, karyawan); modul di luar paket hilang dari menu dan endpoint-nya 403.",
    "Onboard Client membuat provider, cabang pertama, peran dan pengguna awal; data klien tidak pernah terlihat klien lain.",
    "Penangguhan klien menutup login dan semua API (kecuali keluar) serta halaman publik klien; pemulihan mengembalikan semuanya tanpa kehilangan data.",
    "Ganti role Admin wajib PIN owner; role yang baru ditambahkan belum aktif sampai diaktifkan (izin hanya dihitung dari role aktif).",
    "Kata sandi, 2FA dan batas percobaan masuk."]),
 "03": ("konfigurasi-umum", "Konfigurasi Umum dan Master Data", ["konfigurasi-umum"],
   "Master data dan pengaturan yang dipakai semua modul.",
   ["Nomor dokumen memakai awalan dari pengaturan cabang dan unik per cabang.",
    "Status dokumen berasal dari master status per cabang dengan nama sesuai bahasa pengguna; mengganti nama status cabang tidak merusak terjemahan.",
    "Metode pembayaran dapat dipetakan ke akun buku besar sendiri; kosong berarti memakai akun kas/bank modul.",
    "Dropdown panjang bisa dicari; dropdown modul lain memakai sumber tanpa izin khusus (options), bukan halaman daftar.",
    "Impor Excel dan unduh template tersedia di master data berbaris banyak; header mengikuti bahasa pengguna dan impor menerima bahasa mana pun."]),
 "04": ("inti-persetujuan-dan-asisten-ai", "Inti: Persetujuan dan Asisten AI", ["core"],
   "Alur persetujuan lintas modul dan asisten AI dalam aplikasi.",
   ["Alur persetujuan per modul dengan langkah dan peran; permintaan muncul di antrean penyetuju; dokumen tidak bisa diputuskan di luar antrean saat alur berjalan.",
    "Persetujuan dimatikan = dokumen langsung disetujui saat diajukan.",
    "Asisten AI memakai kunci API per cabang (bukan .env); jawaban memakai data cabang aktif; aksi berupa kartu yang dikonfirmasi pengguna.",
    "Playbook, jadwal, tutorial dan tata kelola aksi AI."]),
 "05": ("pembelian", "Pembelian", ["purchasing"], "Dari permintaan sampai pembayaran pemasok.",
   ["PR lalu PQ lalu PO lalu GR lalu PI lalu pembayaran; urutan GR dan faktur mengikuti konfigurasi.",
    "Penerimaan tidak boleh melebihi sisa PO; pembayaran tidak boleh melebihi faktur; faktur belum disetujui tidak bisa dibayar.",
    "PO dengan pengiriman bertahap dan pemberitahuan pengiriman pemasok (halaman publik).",
    "Faktur biaya logistik: alokasi landed cost, pembebanan ulang ke pelanggan, selisih kurs bila akunnya diatur.",
    "Pencocokan faktur dengan barang diterima (mati, peringatkan, tolak) dan produk yang tidak dapat dibeli tidak muncul di pemilih."]),
 "06": ("persediaan", "Persediaan", ["inventory"], "Stok, transfer, opname dan nilai persediaan.",
   ["Transfer stok bertahap (pengiriman ganda) dan penerimaan di gudang tujuan; nilai gabungan tidak berubah.",
    "Stok opname menghasilkan penyesuaian yang disetujui dan terjurnal.",
    "Metode costing rata-rata/FIFO terbuka untuk semua; LIFO, identifikasi khusus dan biaya standar hanya bila paket memuat fitur lanjutan.",
    "Rekonsiliasi Persediaan: nilai stok dari lapisan biaya = saldo akun persediaan di buku besar.",
    "Stok minimum per gudang dan riwayat pergerakan stok."]),
 "07": ("penjualan", "Penjualan", ["sales"], "Dari penawaran sampai retur penjualan.",
   ["Quotation, SO, delivery, faktur, pembayaran dan retur; HPP terjurnal saat pengiriman.",
    "Batas kredit pelanggan dan batas diskon (cap) ditegakkan.",
    "Tautan pembayaran online per faktur memakai saldo terutang; pembayaran sebagian dan lunas dicatat sekali walau webhook berulang.",
    "Retur: pembalikan PPN sesuai saklar konfigurasi penjualan.",
    "Penawaran publik dapat dibuka tanpa login lewat token dan kedaluwarsa."]),
 "08": ("kanvasing", "Kanvasing (Sales Lapangan)", ["canvassing"], "Kunjungan, calon pelanggan, stok titipan dan penagihan lapangan.",
   ["Calon pelanggan terpisah dari master pelanggan; menang hanya lewat konversi; kalah wajib alasan.",
    "Kunjungan tak terjadwal melakukan check-in GPS otomatis; hasil kunjungan berasal dari master yang bisa dikonfigurasi.",
    "Stok titipan sales mengurangi gudang dan menjadi dasar order lapangan.",
    "Penagihan lapangan dan setoran terjurnal; target dan realisasi per wilayah/sales."]),
 "09": ("pos", "Point of Sale (Apotek)", ["pos"], "Kasir, sesi kas, pembayaran QRIS dan penutupan sesi.",
   ["Satu sesi per kasir; modal awal, hitung pecahan, selisih kas menurut mode.",
    "Transaksi tunai dan QRIS; QRIS membuat transaksi pending lalu lunas setelah webhook; layar pelanggan ikut menampilkan QR.",
    "Hold, void, retur dengan persetujuan; mode offline dan antrean sinkron.",
    "Jurnal POS per sesi atau langsung; promo, cashback, member."]),
 "10": ("restoran", "Restoran (Kafe Sehat)", ["restaurant"], "Pesanan meja, dapur, tagihan dan pembayaran.",
   ["Pesanan per meja, kirim ke dapur (KDS), pisah tagihan, reservasi dan pesanan mandiri lewat QR.",
    "Pembayaran tagihan (tunai/QRIS) menutup pesanan dan membebaskan meja.",
    "Stok bahan menu berkurang sesuai resep bila diaktifkan."]),
 "11": ("manufaktur", "Manufaktur (Pabrik Herbal)", ["manufacturing"], "BOM, rute produksi dan pesanan produksi.",
   ["Biaya bahan per BOM menjadi HPP barang jadi.",
    "Pesanan produksi: bahan keluar, hasil masuk; bahan kurang menghalangi penyelesaian bila saklar menyala; toleransi produksi melebihi rencana.",
    "Persetujuan pesanan produksi bila menyala."]),
 "12": ("pertambangan", "Pertambangan (Tambang Kapur)", ["mining"], "Pit, stockpile, log produksi dan penjualan bijih.",
   ["Log produksi masuk ke stockpile; stockpile boleh dibatasi ke produk tertentu.",
    "Produksi melebihi estimasi cadangan pit diperingatkan atau ditolak menurut saklar.",
    "Jurnal tambang terposting di bawah tipe jurnal persediaan cabang."]),
 "13": ("sewa", "Sewa Alat Medis", ["rental"], "Aset sewa, pesanan sewa, deposit dan pengembalian.",
   ["Pesanan sewa dari draf ke aktif lalu selesai; aset tidak bisa disewa ganda pada periode yang sama.",
    "Deposit dicatat sebagai kewajiban lalu dikembalikan dikurangi denda kerusakan.",
    "Faktur dan pembayaran sewa memakai akun sewa dan metode pembayaran."]),
 "14": ("akuntansi-dan-aset-tetap", "Akuntansi, Aset Tetap dan Pajak", ["accounting"], "Jurnal, buku besar, penutupan, laporan, anggaran, aset tetap, bank dan PPN.",
   ["Jurnal tidak seimbang tidak bisa diposting; jurnal reverse bersifat aditif; periode tertutup menolak posting.",
    "Tutup tahun membuat jurnal penutup; Laba Rugi dan Anggaran vs Aktual tidak menghitung jurnal penutup, Neraca tetap menghitungnya.",
    "Ringkasan Pajak hanya menghitung jurnal yang sudah masuk buku besar.",
    "Aset tetap: jurnal akuisisi opsional, penyusutan bulanan, pelepasan tidak membuat akun aset negatif.",
    "Rekonsiliasi bank dan rekonsiliasi persediaan; saldo awal ke buku besar."]),
 "15": ("keuangan", "Keuangan: Biaya dan Pembayaran Online", ["finance"], "Pencatatan biaya, persetujuan dan pembayaran online.",
   ["Biaya per kategori dengan persetujuan di atas batas; jurnal biaya saat disetujui.",
    "Pembayaran online (QRIS) dan transfer bank keluar (payout) lewat penyedia sandbox; status mengikuti peta status penyedia.",
    "Penyelesaian (settlement) dan akun penampung penyedia."]),
 "16": ("sdm", "SDM, Absensi, Payroll dan Rekrutmen", ["hrm"], "Karyawan, absensi, cuti, gaji, rekrutmen dan halaman karier.",
   ["Aturan absensi: toleransi, pulang cepat, lembur otomatis dengan persetujuan, konsekuensi gaji hanya bila dinyalakan.",
    "Payroll: PTKP wajib, slip hanya terlihat pemilik, periode berstatus draf lalu diproses, disetujui, dibayar.",
    "Rekrutmen: lowongan, lamaran, wawancara, penawaran; halaman karier publik, CV privat, persetujuan data pribadi.",
    "Cuti dan saldo cuti, kerahasiaan data karyawan, anonimisasi."]),
 "17": ("proyek-dan-tugas", "Proyek dan Tugas", ["proyek-dan-tugas"], "Proyek, tugas, waktu, change request dan integrasi.",
   ["Tugas, papan, linimasa dan daftar; WIP limit; alur kerja per tipe tugas.",
    "Timesheet dan change request lewat persetujuan bila menyala; biaya tenaga kerja terjurnal bila saklarnya menyala.",
    "Tombol buat tugas dari dokumen (PO, SO, produksi, sewa) dan tautan ke dokumen."]),
 "18": ("dasbor", "Dasbor", ["dashboard"], "Angka ringkasan per peran.",
   ["Angka dasbor sama dengan laporan sumbernya; dasbor hanya menampilkan data cabang aktif atau gabungan sesuai peran."]),
 "19": ("laporan", "Laporan", ["reports"], "Laporan lintas modul dan ekspor.",
   ["Laporan mendukung cabang anak bila cabang aktif adalah cabang utama.",
    "Ekspor PDF dan Excel memakai bahasa pengguna dan tata letak cabang."]),
 "20": ("halaman-publik", "Halaman Publik", ["halaman-publik"], "Halaman tanpa login untuk pihak luar.",
   ["Token kedaluwarsa dan tidak dapat ditebak; data internal tidak bocor.",
    "Halaman karier, penawaran, tautan bayar, pemberitahuan pengiriman pemasok dan penangguhan klien menutup semuanya."]),
}

# Bab yang draf Ollama-nya gagal: ditulis tangan dari isi bab manual.
MANUAL_ROWS = {
 "pos/03-void-dan-refund.md": [
  "| Positif — void transaksi Held | Buat transaksi OBT-001 × 2 lalu tahan (Held), buka detailnya dan Void dengan alasan | Transaksi berstatus Voided; stok tidak berubah karena belum pernah dikurangi |",
  "| Positif — refund sebagian transaksi Completed | Transaksi OBT-001 × 10 selesai; Refund 3 strip dengan alasan barang rusak | Stok bertambah 3 di warehouse asal; jurnal kontra mengurangi Penjualan dan Kas Hasil Penjualan POS sebesar nilai 3 strip |",
  "| Negatif — refund melebihi qty yang dibeli | Refund 11 strip pada transaksi yang hanya 10 strip | Ditolak; tidak ada perubahan stok dan jurnal |",
  "| Negatif — void transaksi yang sudah punya refund | Void transaksi yang sebelumnya sudah di-refund sebagian | Ditolak secara khusus karena akan menghitung ganda qty yang sudah dikembalikan |",
 ],
 "rental/05-usage-entries.md": [
  "| Positif — catat pemakaian dan tagih | Aset sewa berbasis pemakaian: catat 3 usage entry harian lalu buat Rental Invoice dari entry itu | Entry yang ikut invoice berstatus sudah ditagih; total invoice = jumlah pemakaian dikali tarif |",
  "| Negatif — entry yang sudah ditagih ikut ditagih lagi | Buat invoice baru untuk item yang sama | Entry berstatus sudah ditagih tidak ikut lagi; tidak ada penagihan ganda |",
 ],
}

PAT_MSG = re.compile(r'(?:dengan pesan|menampilkan pesan|muncul pesan|menyebutkan|pesan)\s*"[^"]*"')
PAT_Q = re.compile(r'"[^"]{16,}"')
RULE_WORDS = re.compile(r"(tidak bisa|tidak boleh|ditolak|menolak|wajib|harus|tidak dapat|dilarang|hanya bisa)", re.I)
MD_CHARS = re.compile(r"[*_`>#]")
MD_LINKS = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def manual_rules(relpath, limit=4):
    """Aturan tegas yang tertulis di bab manual (kalimat dengan kata larangan/kewajiban): fakta, bukan karangan model."""
    try:
        text = open(MANUAL_DIR + relpath, encoding="utf-8").read()
    except Exception:
        return []
    text = re.sub(r"^---\n.*?\n---", "", text, count=1, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    found = []
    for line in text.split("\n"):
        raw = line.strip()
        if not raw or raw.startswith(("|", "<", "```", "#", "![")):
            continue
        clean = MD_LINKS.sub(r"\1", raw)
        clean = re.sub(r"\s+", " ", MD_CHARS.sub("", clean)).strip(" -.")
        if len(clean) < 30 or len(clean) > 260 or not RULE_WORDS.search(clean):
            continue
        if clean not in found:
            found.append(clean)
    return found[:limit]


def sanitize(rows):
    out = []
    for line in rows.split("\n"):
        line = line.strip()
        if not line.startswith("|") or set(line) <= set("|- :"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        if len(cells) > 3:
            cells = cells[:2] + [" ".join(cells[2:])]
        cells = [PAT_MSG.sub("pesan penolakan yang jelas", c) for c in cells]
        cells = [PAT_Q.sub("pesan yang jelas", c) for c in cells]
        m = re.match(r"^(Positif|Negatif)\s*[—-]?\s*(.*)$", cells[0])
        if not m:
            continue
        label = m.group(2).strip() or ("jalur normal" if m.group(1) == "Positif" else "input salah")
        cells[0] = "%s — %s (draf)" % (m.group(1), label)
        out.append("| " + " | ".join(cells) + " |")
    return out


recs = [json.loads(l) for l in open(os.path.join(HERE, "chapters.jsonl"), encoding="utf-8")]
best = {}
for r in recs:
    if r["rows"] or r["file"] not in best:
        best[r["file"]] = r
bymod = collections.defaultdict(list)
for f, r in sorted(best.items()):
    bymod[r["module"]].append(r)

os.makedirs(DEST, exist_ok=True)
matrix = []
rule_total = 0
for num, (slug, judul, folders, ringkas, kunci) in sorted(FILES.items()):
    lines = ["---", "title: (PT Sehat Sentosa Farma) — %s. %s" % (num, judul), "category: sehat-sentosa-farma",
             "description: Kasus uji per bab manual book modul %s untuk skenario PT Sehat Sentosa Farma. %s" % (", ".join(folders), ringkas), "visibility: internal", "---", "",
             "# %s. %s" % (num, judul), "",
             "> Prasyarat: file [`00`](./00-profil-perusahaan-dan-prasyarat.id.md) dan, untuk transaksi, langkah terkait di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md). "
             "Tiap bagian di bawah sama dengan **satu bab manual book** (tautan di bawah judul bagian). Ada tiga jenis baris: "
             "**(draf)** dirancang Ollama lokal dari isi bab dan harus disesuaikan penguji dengan layar sebenarnya; **aturan tegas di manual** adalah "
             "kalimat larangan/kewajiban yang dikutip langsung dari bab (fakta, bukan karangan model); **izin** dan **netralisasi** ditulis tangan dan berlaku untuk semua bab.", "",
             "## Titik uji kunci modul ini (ditulis tangan)", ""]
    lines += ["- " + k for k in kunci]
    lines += [""]
    n = 0
    for folder in folders:
        for r in bymod.get(folder, []):
            n += 1
            title = r["title"] or r["file"]
            lines += ["## %d. %s" % (n, title), "", "Bab manual: [`%s`](../../%s%s)" % (r["file"], MAN, r["file"]), "",
                      "| Skenario | Langkah dan data uji | Hasil yang diharapkan |", "| --- | --- | --- |"]
            rows = sanitize(r["rows"])
            if r["file"] in MANUAL_ROWS:
                rows = MANUAL_ROWS[r["file"]]
            if not rows:
                rows = ["| Positif — jalur normal bab ini | Ikuti langkah di bab manual dengan data acuan file `00` (draf Ollama tidak dapat dipakai, isi manual) | Hasil sesuai uraian bab |",
                        "| Negatif — input tidak valid | Kosongkan field wajib atau isi di luar batas | Ditolak dengan pesan yang jelas, tidak ada data tersimpan |"]
            lines += rows
            for rule in manual_rules(r["file"]):
                rule_total += 1
                lines.append("| Aturan manual — uji dilanggar dan dipatuhi | Lakukan tindakan yang sesuai aturan, lalu yang melanggarnya, dengan data acuan file `00` | %s |" % rule.replace("|", "/"))
            lines += ["| Negatif — peran tanpa izin | Masuk sebagai peran yang tidak memegang izin fitur ini (mis. Kasir untuk fitur Keuangan) lalu buka halaman atau panggil endpoint | Menu atau tombol tidak dapat dipakai dengan alasan jelas (tombol nonaktif dengan tooltip), endpoint menjawab 403 |",
                      "| Netralisasi | Batalkan, balik, atau retur dokumen uji sesuai modul; jangan hapus dokumen yang sudah berjurnal | Data kembali ke keadaan awal tanpa merusak data yang dipakai langkah `01` berikutnya |", ""]
            matrix.append((folder, title, r["file"], "`%s` bagian %d" % (num, n)))
    open(os.path.join(DEST, "%s-%s.id.md" % (num, slug)), "w", encoding="utf-8").write("\n".join(lines))
    print(num, slug, n, "bab")

m = ["---", "title: (PT Sehat Sentosa Farma) — 99. Peta Cakupan Bab Manual Book ke Kasus Uji", "category: sehat-sentosa-farma",
     "description: Daftar seluruh bab manual book dan file kasus ujinya, supaya terlihat bahwa semua modul dan fitur tersentuh.", "visibility: internal", "---", "",
     "# 99. Peta Cakupan", "",
     "Jumlah bab manual book yang dipetakan: **%d**. Dihasilkan otomatis dari folder manual book; bab baru yang belum ada di sini berarti belum punya kasus uji." % len(matrix), "",
     "| Modul manual | Bab | Berkas bab | Kasus uji |", "| --- | --- | --- | --- |"]
for folder, title, f, where in matrix:
    m.append("| %s | %s | `%s` | %s |" % (folder, title, f, where))
m += ["", "Alur lintas modul ada di [`01`](./01-alur-bisnis-terpadu-lintas-modul.id.md); izin, isolasi dan kasus batas di [`98`](./98-izin-isolasi-dan-kasus-batas.id.md)."]
open(os.path.join(DEST, "99-peta-cakupan.id.md"), "w", encoding="utf-8").write("\n".join(m))
print("matrix", len(matrix), "aturan tegas", rule_total)
