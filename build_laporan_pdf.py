import os
import base64
import subprocess
import pypdf

BASE_DIR = r"c:\Users\user\Desktop\Lab4Web"
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OUTPUT_HTML = os.path.join(BASE_DIR, "laporan_praktikum_4.html")
OUTPUT_PDF_FULL = os.path.join(BASE_DIR, "Laporan_Praktikum_4_CSS_Layout_Margent_Ouwn_Sitompul.pdf")
OUTPUT_PDF_ALIAS = os.path.join(BASE_DIR, "LAPORAN_PRAKTIKUM_4.pdf")

def get_base64_img(filename):
    path = os.path.join(SCREENSHOT_DIR, filename)
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/png;base64,{data}"

# Pre-encode all screenshots
img_b64 = {}
for i in range(1, 14):
    prefix = f"{i:02d}"
    matches = [f for f in os.listdir(SCREENSHOT_DIR) if f.startswith(prefix) and f.endswith(".png")]
    if matches:
        img_b64[prefix] = get_base64_img(matches[0])
    else:
        img_b64[prefix] = ""

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Laporan Praktikum 4: CSS Layout - Margent Ouwn Sitompul</title>
    <style>
        @page {{
            size: A4 portrait;
            margin: 16mm 14mm 16mm 14mm;
            @top-right {{
                content: "Praktikum 4: CSS Layout | Margent Ouwn Sitompul";
                font-size: 8pt;
                color: #64748b;
            }}
            @bottom-center {{
                content: "Universitas Pelita Bangsa - Teknik Informatika";
                font-size: 8pt;
                color: #64748b;
            }}
        }}

        @page :first {{
            margin: 10mm 12mm 10mm 12mm;
        }}

        * {{
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            font-size: 10pt;
            line-height: 1.55;
            color: #1e293b;
            background-color: #ffffff;
            margin: 0;
            padding: 0;
        }}

        /* COVER PAGE STYLING */
        .cover-page {{
            page-break-after: always;
            break-after: page;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            text-align: center;
            border: 2px solid #1e3a8a;
            border-radius: 8px;
            padding: 35px 25px 25px 25px;
            background: linear-gradient(180deg, #f8fafc 0%, #ffffff 60%, #eff6ff 100%);
            box-shadow: inset 0 0 0 1px #93c5fd;
        }}

        .cover-header {{
            width: 100%;
        }}

        .cover-inst-name {{
            font-size: 14pt;
            font-weight: 800;
            letter-spacing: 1.5px;
            color: #1e3a8a;
            text-transform: uppercase;
            margin: 0;
        }}

        .cover-fac-name {{
            font-size: 10.5pt;
            font-weight: 600;
            color: #3b82f6;
            letter-spacing: 0.8px;
            text-transform: uppercase;
            margin-top: 4px;
        }}

        .cover-divider {{
            width: 90px;
            height: 3px;
            background: #2563eb;
            margin: 12px auto;
            border-radius: 2px;
        }}

        .cover-logo-box {{
            margin: 20px 0;
        }}

        .cover-title-box {{
            width: 100%;
            margin: 10px 0;
        }}

        .badge-type {{
            display: inline-block;
            background-color: #dbeafe;
            color: #1e40af;
            border: 1px solid #bfdbfe;
            padding: 5px 16px;
            border-radius: 20px;
            font-size: 9.5pt;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            margin-bottom: 12px;
        }}

        .cover-main-title {{
            font-size: 21pt;
            font-weight: 900;
            color: #0f172a;
            line-height: 1.25;
            margin: 6px 0 10px 0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .cover-sub-title {{
            font-size: 11pt;
            font-weight: 500;
            color: #475569;
            max-width: 85%;
            margin: 0 auto;
            line-height: 1.45;
        }}

        .cover-info-card {{
            width: 88%;
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 16px 20px;
            margin: 20px auto;
            text-align: left;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }}

        .cover-info-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 9.5pt;
        }}

        .cover-info-table td {{
            padding: 5px 4px;
            vertical-align: top;
        }}

        .cover-info-table td.label {{
            width: 32%;
            font-weight: 600;
            color: #475569;
        }}

        .cover-info-table td.colon {{
            width: 3%;
            text-align: center;
            font-weight: bold;
            color: #64748b;
        }}

        .cover-info-table td.value {{
            width: 65%;
            font-weight: 700;
            color: #0f172a;
        }}

        .cover-footer {{
            width: 100%;
            border-top: 1px solid #e2e8f0;
            padding-top: 12px;
            font-size: 9pt;
            color: #64748b;
            font-weight: 500;
        }}

        /* CONTENT STYLING */
        .page-break {{
            page-break-after: always;
            break-after: page;
        }}

        h1.doc-header {{
            font-size: 16pt;
            font-weight: 800;
            color: #1e3a8a;
            border-bottom: 2px solid #2563eb;
            padding-bottom: 6px;
            margin-top: 0;
            margin-bottom: 16px;
        }}

        h2.section-header {{
            font-size: 13pt;
            font-weight: 700;
            color: #1e3a8a;
            background-color: #f1f5f9;
            border-left: 4px solid #2563eb;
            padding: 6px 12px;
            margin-top: 24px;
            margin-bottom: 12px;
            break-after: avoid;
        }}

        h3.sub-header {{
            font-size: 11pt;
            font-weight: 700;
            color: #0f172a;
            margin-top: 16px;
            margin-bottom: 8px;
            break-after: avoid;
        }}

        p {{
            margin-top: 0;
            margin-bottom: 10px;
            text-align: justify;
        }}

        /* TABLES */
        table.data-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 9.5pt;
            margin: 12px 0 18px 0;
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        table.data-table th {{
            background-color: #1e3a8a;
            color: #ffffff;
            font-weight: 600;
            text-align: left;
            padding: 7px 10px;
            border: 1px solid #1e3a8a;
        }}

        table.data-table td {{
            padding: 7px 10px;
            border: 1px solid #cbd5e1;
            vertical-align: middle;
        }}

        table.data-table tr:nth-child(even) {{
            background-color: #f8fafc;
        }}

        /* BOX MODEL DIAGRAM (PURE CSS) */
        .box-model-container {{
            margin: 16px auto;
            max-width: 480px;
            page-break-inside: avoid;
            break-inside: avoid;
            font-size: 8.5pt;
            font-weight: 600;
            text-align: center;
        }}

        .bm-margin {{
            background: #ffedd5;
            border: 2px dashed #f97316;
            border-radius: 8px;
            padding: 10px;
            color: #c2410c;
        }}

        .bm-border {{
            background: #fef3c7;
            border: 2px solid #d97706;
            border-radius: 6px;
            padding: 10px;
            color: #b45309;
        }}

        .bm-padding {{
            background: #dcfce7;
            border: 2px solid #16a34a;
            border-radius: 4px;
            padding: 10px;
            color: #15803d;
        }}

        .bm-content {{
            background: #dbeafe;
            border: 2px solid #2563eb;
            border-radius: 4px;
            padding: 14px 10px;
            color: #1e40af;
            font-weight: bold;
        }}

        .bm-label {{
            font-size: 8pt;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            margin-bottom: 4px;
            display: block;
        }}

        /* STEP CARDS */
        .step-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 14px 16px;
            margin-bottom: 20px;
            page-break-inside: avoid;
            break-inside: avoid;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.03);
        }}

        .step-title {{
            font-size: 11pt;
            font-weight: 700;
            color: #1e3a8a;
            margin: 0 0 8px 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .step-badge {{
            display: inline-block;
            background: #2563eb;
            color: #ffffff;
            font-size: 8.5pt;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 700;
        }}

        /* CODE BLOCKS */
        .code-container {{
            background-color: #0f172a;
            border-radius: 5px;
            padding: 10px 14px;
            margin: 8px 0 12px 0;
            color: #e2e8f0;
            font-family: "JetBrains Mono", Consolas, "Courier New", monospace;
            font-size: 8.2pt;
            line-height: 1.45;
            overflow-x: hidden;
            page-break-inside: avoid;
            break-inside: avoid;
            border-left: 3px solid #38bdf8;
        }}

        .code-container pre {{
            margin: 0;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}

        .code-header {{
            font-size: 7.5pt;
            font-weight: bold;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 4px;
            border-bottom: 1px solid #334155;
            padding-bottom: 2px;
        }}

        /* SCREENSHOT FIGURES */
        .figure-box {{
            text-align: center;
            margin: 10px 0 6px 0;
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        .figure-box img {{
            max-width: 96%;
            max-height: 380px;
            border: 1px solid #cbd5e1;
            border-radius: 5px;
            box-shadow: 0 3px 6px -2px rgba(0, 0, 0, 0.1);
            object-fit: contain;
        }}

        .figure-caption {{
            font-size: 8pt;
            color: #64748b;
            font-style: italic;
            margin-top: 5px;
        }}

        /* CALLOUT NOTE */
        .callout-box {{
            background-color: #eff6ff;
            border-left: 4px solid #3b82f6;
            border-radius: 4px;
            padding: 9px 12px;
            margin: 10px 0;
            font-size: 9pt;
            color: #1e3a8a;
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        .callout-box strong {{
            color: #1d4ed8;
        }}

        /* SIGNATURE SECTION */
        .signature-section {{
            margin-top: 30px;
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        .sig-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }}

        .sig-table td {{
            width: 50%;
            vertical-align: top;
            text-align: center;
            padding: 8px;
        }}

        .sig-space {{
            height: 65px;
        }}

        .sig-name {{
            font-weight: 700;
            color: #0f172a;
            text-decoration: underline;
        }}

        .sig-nim {{
            font-size: 8.5pt;
            color: #475569;
        }}

        .link-text {{
            color: #2563eb;
            text-decoration: none;
            font-weight: 600;
        }}
    </style>
</head>
<body>

    <!-- ==================== HALAMAN 1: SAMPUL RESMI ==================== -->
    <div class="cover-page">
        <div class="cover-header">
            <h1 class="cover-inst-name">Universitas Pelita Bangsa</h1>
            <div class="cover-fac-name">Fakultas Teknik &bull; Program Studi Teknik Informatika</div>
            <div class="cover-divider"></div>
        </div>

        <div class="cover-logo-box">
            <!-- SVG CREST EMBLEM UNIVERSITAS PELITA BANGSA -->
            <svg width="115" height="115" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="60" cy="60" r="56" fill="#1e3a8a" stroke="#2563eb" stroke-width="3"/>
                <circle cx="60" cy="60" r="48" fill="#ffffff" stroke="#93c5fd" stroke-width="1.5" stroke-dasharray="3 3"/>
                <!-- Shield -->
                <path d="M60 26L35 37V62C35 77 46 90 60 95C74 90 85 77 85 62V37L60 26Z" fill="#1e40af"/>
                <!-- Open Book -->
                <path d="M60 48L42 42V68L60 74L78 68V42L60 48Z" fill="#3b82f6"/>
                <path d="M60 48V74" stroke="#ffffff" stroke-width="2"/>
                <path d="M42 42C50 45 56 47 60 48C64 47 70 45 78 42" stroke="#ffffff" stroke-width="1.5"/>
                <!-- Torch Flame -->
                <path d="M60 33C57 37 55 40 58 43C60 45 62 43 60 41C63 43 64 40 60 33Z" fill="#f59e0b"/>
                <!-- Star & Tech dots -->
                <circle cx="60" cy="85" r="3" fill="#fbbf24"/>
                <circle cx="48" cy="80" r="2" fill="#93c5fd"/>
                <circle cx="72" cy="80" r="2" fill="#93c5fd"/>
            </svg>
        </div>

        <div class="cover-title-box">
            <div class="badge-type">Laporan Praktikum Pemrograman Web</div>
            <div class="cover-main-title">Praktikum 4: CSS Layout</div>
            <div class="cover-sub-title">
                Implementasi CSS Box Model, Float Property, Clearfix Technique, dan HTML5 Semantic Elements Pada Tata Letak Web Terstruktur
            </div>
        </div>

        <div class="cover-info-card">
            <table class="cover-info-table">
                <tr>
                    <td class="label">Nama Mahasiswa</td>
                    <td class="colon">:</td>
                    <td class="value">Margent Ouwn Sitompul</td>
                </tr>
                <tr>
                    <td class="label">Nomor Induk Mahasiswa (NIM)</td>
                    <td class="colon">:</td>
                    <td class="value">312510463</td>
                </tr>
                <tr>
                    <td class="label">Program Studi / Kelas</td>
                    <td class="colon">:</td>
                    <td class="value">Teknik Informatika (TI)</td>
                </tr>
                <tr>
                    <td class="label">Mata Kuliah</td>
                    <td class="colon">:</td>
                    <td class="value">Pemrograman Web</td>
                </tr>
                <tr>
                    <td class="label">Dosen Pengampu</td>
                    <td class="colon">:</td>
                    <td class="value">Agung Nugroho, M.Kom</td>
                </tr>
                <tr>
                    <td class="label">Portofolio Live 1 (POS)</td>
                    <td class="colon">:</td>
                    <td class="value"><span class="link-text">https://kasir-prefektur.gt.tc/</span></td>
                </tr>
                <tr>
                    <td class="label">Portofolio Live 2 (Topup)</td>
                    <td class="colon">:</td>
                    <td class="value"><span class="link-text">https://topupgames.gt.tc/</span></td>
                </tr>
            </table>
        </div>

        <div class="cover-footer">
            Universitas Pelita Bangsa &bull; Jl. Inspeksi Kalimalang No.9, Cikarang Pusat, Kabupaten Bekasi, Jawa Barat &bull; 2026
        </div>
    </div>

    <!-- ==================== HALAMAN 2: IDENTITAS & DAFTAR ISI ==================== -->
    <div class="page-break">
        <h1 class="doc-header">DAFTAR ISI & IDENTITAS PRAKTIKUM</h1>

        <h2 class="section-header">Identitas Praktikan</h2>
        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 30%;">Atribut</th>
                    <th>Keterangan Lengkap</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Nama Mahasiswa</strong></td>
                    <td><strong>Margent Ouwn Sitompul</strong></td>
                </tr>
                <tr>
                    <td><strong>NIM</strong></td>
                    <td><strong>312510463</strong></td>
                </tr>
                <tr>
                    <td><strong>Program Studi</strong></td>
                    <td>Teknik Informatika (Fakultas Teknik)</td>
                </tr>
                <tr>
                    <td><strong>Perguruan Tinggi</strong></td>
                    <td>Universitas Pelita Bangsa</td>
                </tr>
                <tr>
                    <td><strong>Mata Kuliah</strong></td>
                    <td>Pemrograman Web</td>
                </tr>
                <tr>
                    <td><strong>Dosen Pengampu</strong></td>
                    <td>Agung Nugroho, M.Kom</td>
                </tr>
                <tr>
                    <td><strong>Proyek Portofolio 1</strong></td>
                    <td><a href="https://kasir-prefektur.gt.tc/" class="link-text">https://kasir-prefektur.gt.tc/</a> (Point of Sales System)</td>
                </tr>
                <tr>
                    <td><strong>Proyek Portofolio 2</strong></td>
                    <td><a href="https://topupgames.gt.tc/" class="link-text">https://topupgames.gt.tc/</a> (Game Voucher & Currency Top-Up Portal)</td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-header">Daftar Isi Dokumen</h2>
        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 15%; text-align: center;">Bab</th>
                    <th>Uraian Materi & Sub-Bab</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="text-align: center; font-weight: bold;">BAB I</td>
                    <td><strong>Tujuan Praktikum</strong> (Kompetensi yang Dicapai)</td>
                </tr>
                <tr>
                    <td style="text-align: center; font-weight: bold;">BAB II</td>
                    <td><strong>Dasar Teori Web Layouting</strong> (Web Layout, CSS Box Model, CSS Float, Clearfix, HTML5 Semantics)</td>
                </tr>
                <tr>
                    <td style="text-align: center; font-weight: bold;">BAB III</td>
                    <td><strong>Langkah-Langkah Praktikum</strong> (Tahap 1 s.d. 13 disertai Kode Sumber & Screenshot Pengujian)</td>
                </tr>
                <tr>
                    <td style="text-align: center; font-weight: bold;">BAB IV</td>
                    <td><strong>Jawaban Pertanyaan & Tugas Modul</strong> (Tugas 1 Menu About & Tugas 2 Form Menu Contact)</td>
                </tr>
                <tr>
                    <td style="text-align: center; font-weight: bold;">BAB V</td>
                    <td><strong>Halaman Tambahan & Struktur Proyek</strong> (Menu Artikel, Pohon Folder Direktori, dan Git)</td>
                </tr>
                <tr>
                    <td style="text-align: center; font-weight: bold;">BAB VI</td>
                    <td><strong>Kesimpulan Praktikum & Lembar Pengesahan</strong></td>
                </tr>
            </tbody>
        </table>

        <h2 class="section-header">BAB I: TUJUAN PRAKTIKUM</h2>
        <p>Praktikum Modul 4 Pemrograman Web ini dirancang guna membekali mahasiswa dengan penguasaan fundamental dalam menata antarmuka halaman web secara sistematis dan terstruktur. Adapun tujuan capaian pembelajaran praktikum ini adalah:</p>
        <ol style="margin-top: 6px; padding-left: 20px; line-height: 1.6;">
            <li><strong>Memahami Struktur Dasar Pembuatan Web Layout:</strong> Mampu merancang kerangka penempatan elemen antarmuka (header, navigasi, hero banner, area konten utama, sidebar widget, dan footer).</li>
            <li><strong>Menguasai Konsep Box Element (CSS Box Model):</strong> Memahami dan mampu mengontrol perpaduan content, padding, border, margin, serta penyesuaian dimensi dengan <code>box-sizing: border-box</code>.</li>
            <li><strong>Mengimplementasikan CSS Floating:</strong> Mampu mengatur aliran elemen secara horizontal menggunakan properti <code>float: left</code>, <code>float: right</code>, serta memahami dampaknya pada <em>normal document flow</em>.</li>
            <li><strong>Mengatasi Masalah Floating dengan Clearfix:</strong> Menguasai properti <code>clear</code> (left, right, both) dan implementasi teknik clearfix modern menggunakan pseudo-element <code>::after</code> untuk menanggulangi <em>height collapse</em>.</li>
            <li><strong>Menerapkan HTML5 Semantics Elements:</strong> Menggunakan elemen semantik baku (<code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;section&gt;</code>, <code>&lt;article&gt;</code>, <code>&lt;aside&gt;</code>, <code>&lt;footer&gt;</code>) untuk kode yang terstruktur, mudah dirawat, ramah SEO, dan berstandar aksesibilitas tinggi.</li>
        </ol>
    </div>

    <!-- ==================== HALAMAN 3: DASAR TEORI ==================== -->
    <div class="page-break">
        <h1 class="doc-header">BAB II: LANDASAN TEORI</h1>

        <h2 class="section-header">1. Web Layout</h2>
        <p>Web Layout merupakan rancangan penataan tata letak komponen grafis dan teks pada layar browser. Layout yang proporsional berfungsi memudahkan pengunjung dalam mencerna alur informasi, menyederhanakan navigasi, serta meningkatkan estetika dan kenyamanan pengalaman pengguna (*User Experience*).</p>

        <h2 class="section-header">2. Box Element (CSS Box Model)</h2>
        <p>Dalam paradigma peramban web modern, seluruh elemen HTML direpresentasikan sebagai sebuah kotak persegi panjang (*box*). CSS Box Model tersusun atas empat lapisan konsentris:</p>
        <ul>
            <li><strong>Content:</strong> Area inti tempat teks, gambar, atau media disajikan.</li>
            <li><strong>Padding:</strong> Ruang transparan di sekeliling konten di dalam border.</li>
            <li><strong>Border:</strong> Garis pembatas fisik yang mengelilingi padding dan konten.</li>
            <li><strong>Margin:</strong> Ruang pemisah transparan di luar border yang memisahkan elemen dari elemen tetangganya.</li>
        </ul>

        <!-- DIAGRAM VISUAL CSS BOX MODEL -->
        <div class="box-model-container">
            <div class="bm-margin">
                <span class="bm-label">MARGIN (Area Ruang Terluar)</span>
                <div class="bm-border">
                    <span class="bm-label">BORDER (Garis Batas Elemen)</span>
                    <div class="bm-padding">
                        <span class="bm-label">PADDING (Bantalan Ruang Dalam)</span>
                        <div class="bm-content">
                            CONTENT (Isi Teks / Gambar)
                        </div>
                    </div>
                </div>
            </div>
            <div class="figure-caption">Gambar 2.1: Visualisasi Konseptual CSS Box Model</div>
        </div>

        <div class="callout-box">
            <strong>Catatan Penting:</strong> Deklarasi <code>box-sizing: border-box;</code> memastikan bahwa penambahan <code>padding</code> dan <code>border</code> tidak akan memperbesar lebar total elemen yang telah ditetapkan, sehingga perhitungan layout multi-kolom menjadi presisi.
        </div>

        <h2 class="section-header">3. CSS Float Property & Clearfix Technique</h2>
        <p>Properti CSS <code>float</code> mengangkat elemen dari aliran normal dokumen (*normal document flow*) dan menggesernya ke sisi kiri atau kanan wadah induknya. Ketika seluruh elemen anak (*child elements*) menggunakan float, elemen pembungkus (*parent container*) akan kehilangan perhitungan tinggi fisiknya, suatu fenomena yang dikenal sebagai <strong>Height Collapse</strong>.</p>
        <p>Untuk menormalkan kembali aliran dokumen, digunakan properti <code>clear</code> atau teknik <strong>Clearfix Modern</strong>:</p>
        
        <div class="code-container">
            <div class="code-header">CSS: Standar Modern Clearfix</div>
            <pre>.row::after,
#wrapper::after {{
    content: "";
    display: table;
    clear: both;
}}</pre>
        </div>

        <h2 class="section-header">4. HTML5 Semantic Elements</h2>
        <p>Standar HTML5 memperkenalkan elemen-elemen yang memiliki arti semantik eksplisit bagi peramban dan mesin pencari, menggantikan ketergantungan pada generic div (*div soup*):</p>
        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 25%;">Elemen Semantik</th>
                    <th>Peran Struktural & Fungsi</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>&lt;header&gt;</code></td>
                    <td>Mendefinisikan bagian kepala dokumen, judul situs, logo, dan sub-judul.</td>
                </tr>
                <tr>
                    <td><code>&lt;nav&gt;</code></td>
                    <td>Membungkus menu navigasi utama situs atau tautan internal halaman.</td>
                </tr>
                <tr>
                    <td><code>&lt;section&gt;</code></td>
                    <td>Mengelompokkan babak konten mandiri bertema tertentu.</td>
                </tr>
                <tr>
                    <td><code>&lt;article&gt;</code></td>
                    <td>Menyajikan konten independen yang dapat disindikasikan (artikel berita, postingan blog).</td>
                </tr>
                <tr>
                    <td><code>&lt;aside&gt;</code></td>
                    <td>Mendefinisikan bilah samping (*sidebar*) untuk widget, daftar link, atau kutipan pendukung.</td>
                </tr>
                <tr>
                    <td><code>&lt;footer&gt;</code></td>
                    <td>Menyajikan bagian kaki halaman (hak cipta, info kontak, disclaimer).</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- ==================== HALAMAN 4: LANGKAH PRAKTIKUM 1 - 4 ==================== -->
    <div class="page-break">
        <h1 class="doc-header">BAB III: LANGKAH-LANGKAH PRAKTIKUM (BAGIAN 1)</h1>

        <!-- Langkah 1 -->
        <div class="step-card">
            <div class="step-title"><span class="step-badge">Langkah 1</span> Box Element Dasar Tanpa Float</div>
            <p>Pada tahap pertama, dibuat tiga buah tag <code>&lt;div&gt;</code> (Div 1, Div 2, Div 3) dengan warna latar berbeda. Karena elemen <code>&lt;div&gt;</code> merupakan elemen bertipe <em>block-level</em> secara default, setiap elemen mengambil 100% lebar yang tersedia dan tersusun secara vertikal dari atas ke bawah.</p>
            
            <div class="code-container">
                <div class="code-header">Kode HTML & CSS: Box Tanpa Float</div>
                <pre>&lt;style&gt;
    div {{ padding: 10px; }}
    .div1 {{ background: red; }}
    .div2 {{ background: yellow; }}
    .div3 {{ background: green; }}
&lt;/style&gt;
&lt;section&gt;
    &lt;div class="div1"&gt;Div 1&lt;/div&gt;
    &lt;div class="div2"&gt;Div 2&lt;/div&gt;
    &lt;div class="div3"&gt;Div 3&lt;/div&gt;
&lt;/section&gt;</pre>
            </div>

            <div class="figure-box">
                <img src="{img_b64.get('01', '')}" alt="Box Element Tanpa Float">
                <div class="figure-caption">Gambar 3.1: Tampilan Tiga Box Element Default Tanpa Float (Tersusun Vertikal)</div>
            </div>
        </div>

        <!-- Langkah 2 -->
        <div class="step-card">
            <div class="step-title"><span class="step-badge">Langkah 2</span> Penerapan CSS Float Property</div>
            <p>Menambahkan deklarasi <code>float: left;</code> pada selector <code>div</code>. Hal ini melepaskan elemen dari aliran baris normal dan menjejerkannya secara horizontal ke arah kiri secara bersebelahan.</p>
            
            <div class="code-container">
                <div class="code-header">Kode CSS: Box dengan Float Left</div>
                <pre>div {{
    float: left;
    padding: 10px;
}}
.div1 {{ background: red; }}
.div2 {{ background: yellow; }}
.div3 {{ background: green; }}</pre>
            </div>

            <div class="figure-box">
                <img src="{img_b64.get('02', '')}" alt="Box Element dengan Float">
                <div class="figure-caption">Gambar 3.2: Tampilan Tiga Box Element dengan Float Left (Tersusun Horizontal)</div>
            </div>
        </div>
    </div>

    <!-- ==================== HALAMAN 5: LANGKAH PRAKTIKUM 3 - 4 ==================== -->
    <div class="page-break">
        <h1 class="doc-header">BAB III: LANGKAH-LANGKAH PRAKTIKUM (BAGIAN 2)</h1>

        <!-- Langkah 3 -->
        <div class="step-card">
            <div class="step-title"><span class="step-badge">Langkah 3</span> Penerapan Clearfix pada Div 4</div>
            <p>Ketika ditambahkan elemen keempat (<code>&lt;div class="div4"&gt;Div 4&lt;/div&gt;</code>), tanpa aturan clear elemen tersebut akan tetap mengalir di samping elemen float sebelumnya. Dengan menerapkan <code>clear: left; float: none;</code>, Div 4 dipaksa turun ke baris baru tepat di bawah elemen-elemen float.</p>
            
            <div class="code-container">
                <div class="code-header">Kode CSS & HTML: Clearfix Div 4</div>
                <pre>&lt;div class="div4"&gt;Div 4&lt;/div&gt;
/* CSS */
.div4 {{
    background-color: blue;
    clear: left;
    float: none;
    color: white;
}}</pre>
            </div>

            <div class="figure-box">
                <img src="{img_b64.get('03', '')}" alt="Box Element Clearfix Div 4">
                <div class="figure-caption">Gambar 3.3: Tampilan Div 4 yang Turun ke Baris Baru Menggunakan Clear: Left</div>
            </div>
        </div>

        <!-- Langkah 4 -->
        <div class="step-card">
            <div class="step-title"><span class="step-badge">Langkah 4</span> Eksperimen Properti Clear (left, right, both)</div>
            <p>Eksperimen modul halaman 5 membuktikan bahwa <code>clear: both;</code> menjamin elemen berada di bawah semua elemen float baik dari sisi kiri maupun kanan. Pada pengujian ini, Div 2 diberi <code>float: right;</code> sementara Div 1 & 3 diberi <code>float: left;</code>. Deklarasi <code>clear: both;</code> pada Div 4 secara sempurna membersihkan kedua sisi.</p>
            
            <div class="code-container">
                <div class="code-header">Kode CSS: Eksperimen Clear Both</div>
                <pre>.div1 {{ background: red; float: left; }}
.div2 {{ background: yellow; float: right; }}
.div3 {{ background: green; float: left; }}
.div4 {{
    background-color: blue;
    clear: both;
    float: none;
    color: white;
}}</pre>
            </div>

            <div class="figure-box">
                <img src="{img_b64.get('04', '')}" alt="Box Element Clear Both">
                <div class="figure-caption">Gambar 3.4: Eksperimen Clear: Both Menurunkan Div 4 di Bawah Float Left dan Float Right</div>
            </div>
        </div>
    </div>

    <!-- ==================== HALAMAN 6: LANGKAH PRAKTIKUM 5 - 7 ==================== -->
    <div class="page-break">
        <h1 class="doc-header">BAB III: LANGKAH-LANGKAH PRAKTIKUM (BAGIAN 3)</h1>

        <!-- Langkah 5 -->
        <div class="step-card">
            <div class="step-title"><span class="step-badge">Langkah 5</span> Pembuatan Kerangka Layout Web Sederhana</div>
            <p>Membuat proyek di folder <code>lab4_layout/</code> dengan file <code>home.html</code> dan <code>style.css</code>. Kerangka semantik mencakup <code>#container</code>, <code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>#hero</code>, <code>#wrapper</code> (terdiri dari <code>#main</code> dan <code>#sidebar</code>), serta <code>&lt;footer&gt;</code>.</p>
            
            <div class="figure-box">
                <img src="{img_b64.get('05', '')}" alt="Kerangka Layout">
                <div class="figure-caption">Gambar 3.5: Kerangka Dokumen Semantik HTML5 Awal Sebelum Penataan Gaya Lengkap</div>
            </div>
        </div>

        <!-- Langkah 6 -->
        <div class="step-card">
            <div class="step-title"><span class="step-badge">Langkah 6</span> Penataan Gaya Header dan Kontainer Utama</div>
            <p>Menerapkan font Open Sans dari Google Fonts, CSS reset (<code>* {{ margin: 0; padding: 0; }}</code>), serta membungkus layout dalam kontainer selebar <code>980px</code> yang diposisikan di tengah layar (<code>margin: 0 auto;</code>) dengan efek bayangan <code>box-shadow</code>.</p>
            
            <div class="figure-box">
                <img src="{img_b64.get('06', '')}" alt="Styling Header">
                <div class="figure-caption">Gambar 3.6: Tampilan Header dengan Kontainer Tengah dan Efek Bayangan</div>
            </div>
        </div>

        <!-- Langkah 7 -->
        <div class="step-card">
            <div class="step-title"><span class="step-badge">Langkah 7</span> Styling Bilah Navigasi</div>
            <p>Bilah menu navigasi diberi warna biru solid <code>#1f5faa</code>, teks putih tebal, serta interaktivitas hover dan penanda menu aktif <code>.active</code> dengan warna biru cerah <code>#2b83ea</code>.</p>
            
            <div class="figure-box">
                <img src="{img_b64.get('07', '')}" alt="Styling Navigasi">
                <div class="figure-caption">Gambar 3.7: Bilah Menu Navigasi dengan State Active dan Efek Transisi Hover</div>
            </div>
        </div>
    </div>

    <!-- ==================== HALAMAN 7: LANGKAH PRAKTIKUM 8 - 11 ==================== -->
    <div class="page-break">
        <h1 class="doc-header">BAB III: LANGKAH-LANGKAH PRAKTIKUM (BAGIAN 4)</h1>

        <!-- Langkah 8 -->
        <div class="step-card">
            <div class="step-title"><span class="step-badge">Langkah 8</span> Pembuatan Hero Panel (Jumbotron Banner)</div>
            <p>Hero panel berfungsi sebagai sorotan utama antarmuka dengan latar belakang lembut <code>#e4e4e4</code>, judul besar "Hello World!", paragraf pembuka, serta tombol Call to Action (CTA) dengan class <code>.btn .btn-large</code>.</p>
            
            <div class="figure-box">
                <img src="{img_b64.get('08', '')}" alt="Hero Panel">
                <div class="figure-caption">Gambar 3.8: Tampilan Hero Panel Banner Responsif di Bawah Navigasi</div>
            </div>
        </div>

        <!-- Langkah 9 & 10 -->
        <div class="step-card">
            <div class="step-title"><span class="step-badge">Langkah 9-11</span> Layout Main Content, Sidebar Widget, dan Footer</div>
            <p>Area <code>#wrapper</code> dibagi menjadi dua kolom menggunakan teknik floating:</p>
            <ul>
                <li><strong>Kolom Konten Utama (<code>#main</code>):</strong> Menggunakan <code>float: left; width: 640px; padding: 20px;</code></li>
                <li><strong>Kolom Samping (<code>#sidebar</code>):</strong> Menggunakan <code>float: left; width: 340px; padding: 20px;</code></li>
                <li><strong>Sidebar Widget:</strong> Widget Header dengan link navigasi vertikal bergaris bawah tipis, serta Widget Text deskriptif.</li>
                <li><strong>Footer:</strong> Diberikan <code>clear: both; background-color: #1d1d1d;</code> untuk memastikan footer selalu berada di bawah kedua kolom floating.</li>
            </ul>
            
            <div class="figure-box">
                <img src="{img_b64.get('09', '')}" alt="Layout Sidebar dan Main">
                <div class="figure-caption">Gambar 3.9: Pembagian Dua Kolom Berdampingan (Main Content dan Sidebar Widget)</div>
            </div>
        </div>
    </div>

    <!-- ==================== HALAMAN 8: LANGKAH 12 - 13 (HOME LENGKAP) ==================== -->
    <div class="page-break">
        <h1 class="doc-header">BAB III: LANGKAH-LANGKAH PRAKTIKUM (BAGIAN 5)</h1>

        <!-- Langkah 12 & 13 -->
        <div class="step-card">
            <div class="step-title"><span class="step-badge">Langkah 12-13</span> Multi-Kolom Box, Featurette Artikel, & Home Lengkap</div>
            <p>Pada konten utama (<code>#main</code>) diintegrasikan komponen multi-kolom dan featurette:</p>
            <ol>
                <li><strong>Tiga Kolom Box Bundar:</strong> Tiga elemen box berjajar dengan lebar <code>33.333%</code>, foto sirkular (<code>border-radius: 50%</code>), judul tajuk, dan tombol navigasi rincian.</li>
                <li><strong>Divider Pemisah:</strong> Elemen horizontal line <code>&lt;hr class="divider"&gt;</code>.</li>
                <li><strong>Artikel Featurette Bergantian:</strong> Dua buah artikel (<code>&lt;article class="entry"&gt;</code>), artikel pertama menampilkan gambar mengambang di kiri, artikel kedua gambar mengambang di kanan dengan class <code>.right-img</code>.</li>
                <li><strong>Aturan Clearfix:</strong> Diterapkan pada <code>.row:after</code> dan <code>.entry:after</code> guna mengisolasi float antar blok artikel.</li>
            </ol>
            
            <div class="figure-box">
                <img src="{img_b64.get('10', '')}" alt="Home Layout Lengkap">
                <div class="figure-caption">Gambar 3.10: Tampilan Utuh Halaman Utama (home.html) Sesuai Modul Gambar 4.7 & 4.16</div>
            </div>
        </div>
    </div>

    <!-- ==================== HALAMAN 9: TUGAS 1 - ABOUT PAGE ==================== -->
    <div class="page-break">
        <h1 class="doc-header">BAB IV: PENYELESAIAN TUGAS MODUL (TUGAS 1)</h1>

        <div class="step-card">
            <div class="step-title"><span class="step-badge">Tugas 1</span> Pembuatan Layout Menu About (Single Layout)</div>
            <div class="callout-box">
                <strong>Ketentuan Tugas:</strong> Tambahkan Layout untuk menu <strong>About</strong> dengan model <em>Single Layout</em> yang berisi deskripsi profil, portofolio karya, dan keahlian praktikan.
            </div>

            <p><strong>Arsitektur Solusi Teknis:</strong></p>
            <p>Sesuai instruksi <em>"Single Layout"</em>, halaman <code>about.html</code> meniadakan sidebar widget konvensional dan mengalihkan struktur ke satu kontainer lebar penuh (<em>full-width container</em>) dengan padding yang leluasa dan tata letak elegan:</p>
            <ul style="line-height: 1.6;">
                <li><strong>Profile Card:</strong> Menampilkan foto profil avatar melingkar beraksen biru, nama lengkap mahasiswa <strong>Margent Ouwn Sitompul</strong>, NIM <strong>312510463</strong>, serta deskripsi minat akademik di bidang rekayasa web.</li>
                <li><strong>Showcase Portofolio Proyek Live:</strong>
                    <ul>
                        <li><strong>Kasir Prefektur (POS):</strong> Aplikasi Point of Sales modern berbasis web (<span class="link-text">https://kasir-prefektur.gt.tc/</span>).</li>
                        <li><strong>Topup Games Digital:</strong> Portal layanan voucher game online otomatis (<span class="link-text">https://topupgames.gt.tc/</span>).</li>
                        <li><strong>EAISY ERP Manufaktur:</strong> Sistem ERP industri elektroplating terintegrasi (Epindo Automation Integrated System).</li>
                    </ul>
                </li>
                <li><strong>Baris Indikator Keterampilan (Skills Progress Bar):</strong> Indikator visual penguasaan HTML5 Semantics (95%), CSS3 Layouting (90%), Responsive Web (88%), dan Git Version Control (85%).</li>
            </ul>

            <div class="code-container">
                <div class="code-header">Cuplikan Kode HTML: about.html (Struktur Single Layout)</div>
                <pre>&lt;div class="single-content"&gt;
    &lt;div class="profile-card"&gt;
        &lt;img src="images/avatar.svg" alt="Foto Profil" class="avatar"&gt;
        &lt;div class="bio"&gt;
            &lt;h2&gt;Margent Ouwn Sitompul&lt;/h2&gt;
            &lt;h4&gt;NIM: 312510463 &bull; Teknik Informatika - Universitas Pelita Bangsa&lt;/h4&gt;
            &lt;p&gt;Fokus pada rekayasa antarmuka web modern, CSS layouting, dan standar semantik.&lt;/p&gt;
        &lt;/div&gt;
    &lt;/div&gt;
    &lt;h3 class="section-title"&gt;Portofolio Karya & Proyek Web&lt;/h3&gt;
    &lt;div class="portfolio-grid"&gt;
        &lt;!-- Card Proyek Portofolio --&gt;
    &lt;/div&gt;
&lt;/div&gt;</pre>
            </div>

            <div class="figure-box">
                <img src="{img_b64.get('11', '')}" alt="Halaman About Lengkap">
                <div class="figure-caption">Gambar 4.1: Tampilan Single Layout Halaman About (Profil Mahasiswa, Galeri Portofolio, & Bar Keahlian)</div>
            </div>
        </div>
    </div>

    <!-- ==================== HALAMAN 10: TUGAS 2 - CONTACT PAGE ==================== -->
    <div class="page-break">
        <h1 class="doc-header">BAB IV: PENYELESAIAN TUGAS MODUL (TUGAS 2)</h1>

        <div class="step-card">
            <div class="step-title"><span class="step-badge">Tugas 2</span> Pembuatan Layout Menu Contact (Form Isian Lengkap)</div>
            <div class="callout-box">
                <strong>Ketentuan Tugas:</strong> Tambahkan layout untuk menu <strong>Contact</strong> yang berisi form isian interaktif: Nama, Email, Pesan/Message, dll.
            </div>

            <p><strong>Arsitektur Solusi Teknis:</strong></p>
            <p>Halaman <code>kontak.html</code> (dengan tautan kompatibilitas <code>contact.html</code>) mengimplementasikan tata letak dua kolom terpadu:</p>
            <ul>
                <li><strong>Kolom Konten Utama (<code>#main</code>):</strong> Memuat formulir komunikasi lengkap dengan validasi browser:
                    <ul>
                        <li><code>Nama Lengkap:</code> Field input teks wajib isi (<code>required</code>).</li>
                        <li><code>Alamat Email:</code> Input email dengan validasi format standar (<code>type="email"</code>).</li>
                        <li><code>Nomor Telepon / WhatsApp:</code> Input tipe <code>tel</code> untuk nomor pemohon.</li>
                        <li><code>Subjek Pesan:</code> Input penentu topik komunikasi.</li>
                        <li><code>Pesan / Message:</code> Elemen <code>&lt;textarea&gt;</code> berdimensi proporsional.</li>
                        <li><code>Tombol Aksi:</code> Tombol kirim pesan utama <code>.btn-large</code> dan tombol <code>Reset Form</code>.</li>
                    </ul>
                </li>
                <li><strong>Kolom Samping (<code>#sidebar</code>):</strong> Menampilkan kartu alamat resmi kampus Universitas Pelita Bangsa (Cikarang Pusat), kontak sekretariat, surel resmi, serta jam pelayanan akademik.</li>
            </ul>

            <div class="code-container">
                <div class="code-header">Cuplikan Kode HTML: kontak.html</div>
                <pre>&lt;form action="#" method="post"&gt;
    &lt;div class="form-group"&gt;
        &lt;label for="nama"&gt;Nama Lengkap *&lt;/label&gt;
        &lt;input type="text" id="nama" class="form-control" placeholder="Nama Anda" required&gt;
    &lt;/div&gt;
    &lt;div class="form-group"&gt;
        &lt;label for="email"&gt;Alamat Email *&lt;/label&gt;
        &lt;input type="email" id="email" class="form-control" placeholder="email@domain.com" required&gt;
    &lt;/div&gt;
    &lt;div class="form-group"&gt;
        &lt;label for="pesan"&gt;Pesan / Message *&lt;/label&gt;
        &lt;textarea id="pesan" class="form-control" rows="5" required&gt;&lt;/textarea&gt;
    &lt;/div&gt;
    &lt;button type="submit" class="btn btn-large"&gt;Kirim Pesan &raquo;&lt;/button&gt;
&lt;/form&gt;</pre>
            </div>

            <div class="figure-box">
                <img src="{img_b64.get('12', '')}" alt="Halaman Kontak">
                <div class="figure-caption">Gambar 4.2: Tampilan Halaman Kontak (Formulir Isian Interaktif & Informasi Kontak Kampus)</div>
            </div>
        </div>
    </div>

    <!-- ==================== HALAMAN 11: ARTIKEL & STRUKTUR REPO ==================== -->
    <div class="page-break">
        <h1 class="doc-header">BAB V: HALAMAN PENDUKUNG & STRUKTUR PROYEK</h1>

        <div class="step-card">
            <div class="step-title"><span class="step-badge">Halaman Tambahan</span> Menu Artikel Edukatif (artikel.html)</div>
            <p>Untuk memastikan keutuhan fungsional dari seluruh tautan navigasi utama (<code>Home</code>, <code>Artikel</code>, <code>About</code>, <code>Kontak</code>), dibuat halaman <code>artikel.html</code> yang memuat artikel teknis komprehensif mengenai perbandingan teknik tata letak CSS Float vs Flexbox/Grid, serta pentingnya HTML5 Semantics.</p>
            
            <div class="figure-box">
                <img src="{img_b64.get('13', '')}" alt="Halaman Artikel">
                <div class="figure-caption">Gambar 5.1: Tampilan Halaman Artikel Edukatif Terstruktur</div>
            </div>
        </div>

        <h2 class="section-header">Struktur Direktori Proyek</h2>
        <div class="code-container">
            <div class="code-header">Pohon Direktori: Lab4Web</div>
            <pre>Lab4Web/
├── .git/                               # Direktori Git Version Control
├── README.md                           # Dokumentasi Laporan Praktikum (Markdown)
├── lab4_box.html                       # File Latihan Awal Box Element & Float
├── generate_screenshots.py             # Script Otomasi Pengambilan Bukti Screenshot
├── build_laporan_pdf.py                # Script Kompilasi Laporan PDF Resmi
├── screenshots/                        # Direktori 13 Bukti Screenshot Hasil
│   ├── 01_box_tanpa_float.png
│   ├── 02_box_dengan_float.png
│   ├── 03_box_clearfix_div4.png
│   ├── 04_box_clear_both.png
│   ├── 05_layout_kerangka.png
│   ├── 06_layout_header.png
│   ├── 07_layout_navigasi.png
│   ├── 08_layout_hero.png
│   ├── 09_layout_sidebar.png
│   ├── 10_layout_home_lengkap.png
│   ├── 11_tugas_about_page.png
│   ├── 12_tugas_contact_page.png
│   └── 13_artikel_page.png
└── lab4_layout/                        # Proyek Utama Layouting Web
    ├── home.html                       # Halaman Beranda Utama Sesuai Modul
    ├── about.html                      # Halaman Single Layout Tugas 1
    ├── kontak.html                     # Halaman Formulir Kontak Tugas 2
    ├── contact.html                    # File Alias Redirection
    ├── artikel.html                    # Halaman Artikel Edukatif
    ├── style.css                       # Berkas Gaya CSS Terintegrasi
    └── images/                         # Aset Gambar Portofolio & SVG</pre>
        </div>

        <h2 class="section-header">Petunjuk Pengelolaan Git & Pengumpulan Tugas</h2>
        <p>Sesuai ketentuan penugasan mata kuliah Pemrograman Web Universitas Pelita Bangsa:</p>
        <ol>
            <li><strong>Komit Versi Git:</strong> Seluruh modifikasi berkas dikomit dengan pesan deskriptif:
                <div class="code-container" style="margin: 4px 0 8px 0;">
                    <pre>git add .
git commit -m "feat: complete Praktikum 4 CSS Layout, Pertanyaan dan Tugas, serta Laporan"</pre>
                </div>
            </li>
            <li><strong>Pengunggahan ke Remote Server:</strong> Proyek di-push ke repository GitHub/GitLab:
                <div class="code-container" style="margin: 4px 0 8px 0;">
                    <pre>git remote add origin https://github.com/username-anda/Lab4Web.git
git push -u origin main</pre>
                </div>
            </li>
            <li><strong>Pengumpulan e-Campus:</strong> Mengunggah berkas PDF laporan ini serta melampirkan tautan URL repositori GitHub pada portal pembelajaran e-Campus UPB.</li>
        </ol>
    </div>

    <!-- ==================== HALAMAN 12: KESIMPULAN & PENGESAHAN ==================== -->
    <div class="page-break">
        <h1 class="doc-header">BAB VI: KESIMPULAN & PENGESAHAN</h1>

        <h2 class="section-header">Kesimpulan Praktikum</h2>
        <p>Berdasarkan seluruh rangkaian praktikum dan penyelesaian tugas mandiri yang telah dilaksanakan pada Modul 4 CSS Layout, dapat ditarik kesimpulan komprehensif sebagai berikut:</p>
        <ol style="line-height: 1.6; padding-left: 20px;">
            <li><strong>Struktur Tata Letak Web:</strong> Penerapan kerangka layout yang terencana dengan pembagian header, menu navigasi, hero banner, main content, sidebar widget, dan footer menciptakan struktur web yang ergonomis, intuitif, dan nyaman dijelajahi oleh pengguna.</li>
            <li><strong>Penguasaan CSS Box Model:</strong> Pemahaman mendalam mengenai komponen <em>content</em>, <em>padding</em>, <em>border</em>, dan <em>margin</em> adalah kunci utama tata letak presisi. Penggunaan deklarasi <code>box-sizing: border-box;</code> sangat efektif mencegah kerusakan dimensi tata letak akibat penambahan padding dan border.</li>
            <li><strong>CSS Floating & Dampak Normal Flow:</strong> Properti <code>float: left</code> dan <code>float: right</code> memungkinkan penyusunan elemen multi-kolom horizontal. Namun, elemen float keluar dari aliran normal dokumen dan menyebabkan <em>height collapse</em> pada elemen induk.</li>
            <li><strong>Urgensi Clearfix & Properti Clear:</strong> Penggunaan properti <code>clear: both;</code> serta teknik pseudo-element modern <code>.clearfix::after</code> mutlak dibutuhkan untuk memulihkan aliran dokumen normal serta menjaga agar elemen di bawahnya (seperti footer) tidak tumpang tindih.</li>
            <li><strong>Manfaat HTML5 Semantics:</strong> Penggantian tag generic <code>&lt;div&gt;</code> dengan elemen semantik (<code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;section&gt;</code>, <code>&lt;article&gt;</code>, <code>&lt;aside&gt;</code>, <code>&lt;footer&gt;</code>) meningkatkan keterbacaan kode, mempermudah pemeliharaan, serta meningkatkan skor SEO dan aksesibilitas ramah pembaca layar (*screen reader*).</li>
            <li><strong>Penyelesaian Tugas 1 dan 2:</strong> Seluruh penugasan modul berhasil direalisasikan secara sempurna. Halaman <strong>About</strong> sukses menyajikan konsep <em>single layout</em> profesional lengkap dengan profil, galeri proyek live portofolio (<span class="link-text">https://kasir-prefektur.gt.tc/</span> dan <span class="link-text">https://topupgames.gt.tc/</span>), serta baris keterampilan. Halaman <strong>Contact</strong> berhasil menyajikan formulir interaktif lengkap beserta informasi institusi kampus.</li>
        </ol>

        <div class="signature-section">
            <h2 class="section-header">Lembar Pengesahan Praktikum</h2>
            <p style="text-align: center; margin-bottom: 20px;">
                Laporan Praktikum Pemrograman Web Modul 4 ini telah disusun dan diselesaikan secara mandiri dengan data yang sebenar-benarnya.
            </p>

            <table class="sig-table">
                <tr>
                    <td>
                        <div>Mengetahui,</div>
                        <div style="font-weight: 600; color: #1e3a8a;">Dosen Pengampu Mata Kuliah</div>
                        <div class="sig-space"></div>
                        <div class="sig-name">Agung Nugroho, M.Kom</div>
                        <div class="sig-nim">Dosen Pemrograman Web UPB</div>
                    </td>
                    <td>
                        <div>Bekasi, 13 Oktober 2026</div>
                        <div style="font-weight: 600; color: #1e3a8a;">Praktikan Mahasiswa</div>
                        <div class="sig-space"></div>
                        <div class="sig-name">Margent Ouwn Sitompul</div>
                        <div class="sig-nim">NIM: 312510463</div>
                    </td>
                </tr>
            </table>
        </div>
    </div>

</body>
</html>
"""

print(f"Menulis file HTML laporan ke: {OUTPUT_HTML}...")
with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Mengonversi HTML ke PDF menggunakan Google Chrome Headless...")
cmd = [
    CHROME_PATH,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--generate-pdf-document-outline",
    f"--print-to-pdf={OUTPUT_PDF_FULL}",
    "file:///" + OUTPUT_HTML.replace("\\", "/")
]

res = subprocess.run(cmd, capture_output=True)
print("Returncode:", res.returncode)
print("Stderr:", res.stderr.decode("utf-8", errors="ignore"))

if os.path.exists(OUTPUT_PDF_FULL):
    size_bytes = os.path.getsize(OUTPUT_PDF_FULL)
    print(f"PDF Berhasil dibuat: {OUTPUT_PDF_FULL} ({size_bytes} bytes)")
    
    # Buat salinan alias dengan nama ringkas LAPORAN_PRAKTIKUM_4.pdf
    import shutil
    shutil.copyfile(OUTPUT_PDF_FULL, OUTPUT_PDF_ALIAS)
    print(f"Salinan alias dibuat: {OUTPUT_PDF_ALIAS}")

    # Periksa jumlah halaman menggunakan pypdf
    reader = pypdf.PdfReader(OUTPUT_PDF_FULL)
    print(f"Total Halaman PDF: {len(reader.pages)} halaman")
else:
    print("Gagal membuat file PDF!")
