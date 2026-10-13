import os
import subprocess
import time

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE_DIR = r"c:\Users\user\Desktop\Lab4Web"
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
TEMP_DIR = os.path.join(BASE_DIR, "temp_steps")

os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

steps = {
    "01_box_tanpa_float.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Box Element Tanpa Float</title>
    <style>
        div { padding: 10px; }
        .div1 { background: red; }
        .div2 { background: yellow; }
        .div3 { background: green; }
    </style>
</head>
<body>
    <header><h1>Box Element (Tanpa Float)</h1></header>
    <section>
        <div class="div1">Div 1</div>
        <div class="div2">Div 2</div>
        <div class="div3">Div 3</div>
    </section>
</body>
</html>""",

    "02_box_dengan_float.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Box Element Float</title>
    <style>
        div { float: left; padding: 10px; }
        .div1 { background: red; }
        .div2 { background: yellow; }
        .div3 { background: green; }
    </style>
</head>
<body>
    <header><h1>Box Element (Dengan Float)</h1></header>
    <section>
        <div class="div1">Div 1</div>
        <div class="div2">Div 2</div>
        <div class="div3">Div 3</div>
    </section>
</body>
</html>""",

    "03_box_clearfix_div4.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Box Element Clearfix</title>
    <style>
        div { float: left; padding: 10px; }
        .div1 { background: red; }
        .div2 { background: yellow; }
        .div3 { background: green; }
        .div4 { background-color: blue; clear: left; float: none; color: white; }
    </style>
</head>
<body>
    <header><h1>Box Element (Clearfix Div 4)</h1></header>
    <section>
        <div class="div1">Div 1</div>
        <div class="div2">Div 2</div>
        <div class="div3">Div 3</div>
        <div class="div4">Div 4</div>
    </section>
</body>
</html>""",

    "04_box_clear_both.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Box Element Clear Both</title>
    <style>
        div { float: left; padding: 10px; }
        .div1 { background: red; }
        .div2 { background: yellow; float: right; }
        .div3 { background: green; }
        .div4 { background-color: blue; clear: both; float: none; color: white; }
    </style>
</head>
<body>
    <header><h1>Eksperimen Clear Both (Div 4 di bawah float left & right)</h1></header>
    <section>
        <div class="div1">Div 1 (Float Left)</div>
        <div class="div2">Div 2 (Float Right)</div>
        <div class="div3">Div 3 (Float Left)</div>
        <div class="div4">Div 4 (Clear: Both)</div>
    </section>
</body>
</html>""",

    "05_layout_kerangka.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Layout Sederhana - Kerangka</title>
</head>
<body>
    <div id="container">
        <header><h1>Layout Sederhana</h1></header>
        <nav>
            <a href="#">Home</a>
            <a href="#">Artikel</a>
            <a href="#">About</a>
            <a href="#">Kontak</a>
        </nav>
        <section id="hero"></section>
        <section id="wrapper">
            <section id="main"></section>
            <aside id="sidebar"></aside>
        </section>
        <footer><p>&copy; 2021 - Universitas Pelita Bangsa</p></footer>
    </div>
</body>
</html>""",

    "06_layout_header.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Layout Sederhana - Header</title>
    <style>
        * { margin: 0; padding: 0; }
        body { font-family: 'Open Sans', sans-serif; color: #5a5a5a; }
        #container { width: 980px; margin: 0 auto; box-shadow: 0 0 1em #cccccc; }
        header { padding: 20px; }
        header h1 { margin: 20px 10px; color: #b5b5b5; font-size: 32px; }
    </style>
</head>
<body>
    <div id="container">
        <header><h1>Layout Sederhana</h1></header>
        <p style="padding: 20px; color: #888;">[Konten halaman akan ditambahkan pada tahap berikutnya]</p>
        <footer style="padding: 20px; background: #1d1d1d; color: #eee;"><p>&copy; 2021 - Universitas Pelita Bangsa</p></footer>
    </div>
</body>
</html>""",

    "07_layout_navigasi.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Layout Sederhana - Navigasi</title>
    <style>
        * { margin: 0; padding: 0; }
        body { font-family: 'Open Sans', sans-serif; color: #5a5a5a; }
        #container { width: 980px; margin: 0 auto; box-shadow: 0 0 1em #cccccc; }
        header { padding: 20px; }
        header h1 { margin: 20px 10px; color: #b5b5b5; font-size: 32px; }
        nav { display: block; background-color: #1f5faa; }
        nav a { padding: 15px 30px; display: inline-block; color: #ffffff; font-size: 14px; text-decoration: none; font-weight: bold; }
        nav a.active, nav a:hover { background-color: #2b83ea; }
    </style>
</head>
<body>
    <div id="container">
        <header><h1>Layout Sederhana</h1></header>
        <nav>
            <a href="#" class="active">Home</a>
            <a href="#">Artikel</a>
            <a href="#">About</a>
            <a href="#">Kontak</a>
        </nav>
        <p style="padding: 20px; color: #888;">[Menu navigasi telah aktif dan bergaya modern]</p>
        <footer style="padding: 20px; background: #1d1d1d; color: #eee;"><p>&copy; 2021 - Universitas Pelita Bangsa</p></footer>
    </div>
</body>
</html>""",

    "08_layout_hero.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Layout Sederhana - Hero Panel</title>
    <style>
        * { margin: 0; padding: 0; }
        body { font-family: 'Open Sans', sans-serif; color: #5a5a5a; }
        #container { width: 980px; margin: 0 auto; box-shadow: 0 0 1em #cccccc; }
        header { padding: 20px; }
        header h1 { margin: 20px 10px; color: #b5b5b5; font-size: 32px; }
        nav { display: block; background-color: #1f5faa; }
        nav a { padding: 15px 30px; display: inline-block; color: #ffffff; font-size: 14px; text-decoration: none; font-weight: bold; }
        nav a.active { background-color: #2b83ea; }
        #hero { background-color: #e4e4e5; padding: 50px 20px; margin-bottom: 20px; }
        #hero h1 { margin-bottom: 20px; font-size: 35px; color: #333; }
        #hero p { margin-bottom: 20px; font-size: 18px; line-height: 25px; color: #666; }
        .btn { display: inline-block; padding: 10px 20px; font-size: 16px; background-color: #2b83ea; color: #fff; text-decoration: none; border-radius: 4px; }
    </style>
</head>
<body>
    <div id="container">
        <header><h1>Layout Sederhana</h1></header>
        <nav>
            <a href="#" class="active">Home</a>
            <a href="#">Artikel</a>
            <a href="#">About</a>
            <a href="#">Kontak</a>
        </nav>
        <section id="hero">
            <h1>Hello World!</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum lorem elit, iaculis innisl volutpat, malesuada tincidunt arcu. Proin in leo fringilla, vestibulum mi porta, faucibus felis. Integer pharetra est nunc, nec pretium nunc pretium ac.</p>
            <a href="#" class="btn">Learn more &raquo;</a>
        </section>
        <footer style="padding: 20px; background: #1d1d1d; color: #eee;"><p>&copy; 2021 - Universitas Pelita Bangsa</p></footer>
    </div>
</body>
</html>""",

    "09_layout_sidebar.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Layout Sederhana - Main & Sidebar</title>
    <link rel="stylesheet" href="../lab4_layout/style.css">
</head>
<body>
    <div id="container">
        <header><h1>Layout Sederhana</h1></header>
        <nav>
            <a href="#" class="active">Home</a>
            <a href="#">Artikel</a>
            <a href="#">About</a>
            <a href="#">Kontak</a>
        </nav>
        <section id="hero">
            <h1>Hello World!</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum lorem elit, iaculis innisl volutpat, malesuada tincidunt arcu. Proin in leo fringilla, vestibulum mi porta, faucibus felis.</p>
            <a href="#" class="btn btn-large">Learn more &raquo;</a>
        </section>
        <section id="wrapper">
            <section id="main">
                <h2>Area Main Content (Lebar 640px)</h2>
                <p style="margin-top: 15px; line-height: 24px;">Konten utama berada di sebelah kiri dengan properti float: left. Konten dapat berupa grid box maupun artikel featurette.</p>
            </section>
            <aside id="sidebar">
                <div class="widget-box">
                    <h3 class="title">Widget Header</h3>
                    <ul>
                        <li><a href="#">Widget Link 1</a></li>
                        <li><a href="#">Widget Link 2</a></li>
                        <li><a href="#">Widget Link 3</a></li>
                    </ul>
                </div>
                <div class="widget-box">
                    <h3 class="title">Widget Text</h3>
                    <p>Vestibulum lorem elit, iaculis in nisl volutpat, malesuada tincidunt arcu. Proin in leo fringilla.</p>
                </div>
            </aside>
        </section>
        <footer><p>&copy; 2021 - Universitas Pelita Bangsa</p></footer>
    </div>
</body>
</html>"""
}

# Create temp files
for filename, content in steps.items():
    filepath = os.path.join(TEMP_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# File to screenshot mapping
screenshot_targets = [
    (os.path.join(TEMP_DIR, "01_box_tanpa_float.html"), "01_box_tanpa_float.png", "1000,600"),
    (os.path.join(TEMP_DIR, "02_box_dengan_float.html"), "02_box_dengan_float.png", "1000,600"),
    (os.path.join(TEMP_DIR, "03_box_clearfix_div4.html"), "03_box_clearfix_div4.png", "1000,600"),
    (os.path.join(TEMP_DIR, "04_box_clear_both.html"), "04_box_clear_both.png", "1000,600"),
    (os.path.join(TEMP_DIR, "05_layout_kerangka.html"), "05_layout_kerangka.png", "1080,700"),
    (os.path.join(TEMP_DIR, "06_layout_header.html"), "06_layout_header.png", "1080,700"),
    (os.path.join(TEMP_DIR, "07_layout_navigasi.html"), "07_layout_navigasi.png", "1080,700"),
    (os.path.join(TEMP_DIR, "08_layout_hero.html"), "08_layout_hero.png", "1080,750"),
    (os.path.join(TEMP_DIR, "09_layout_sidebar.html"), "09_layout_sidebar.png", "1080,850"),
    (os.path.join(BASE_DIR, "lab4_layout", "home.html"), "10_layout_home_lengkap.png", "1080,1150"),
    (os.path.join(BASE_DIR, "lab4_layout", "about.html"), "11_tugas_about_page.png", "1080,1350"),
    (os.path.join(BASE_DIR, "lab4_layout", "kontak.html"), "12_tugas_contact_page.png", "1080,1100"),
    (os.path.join(BASE_DIR, "lab4_layout", "artikel.html"), "13_artikel_page.png", "1080,1050"),
]

for html_path, output_name, win_size in screenshot_targets:
    output_path = os.path.join(SCREENSHOT_DIR, output_name)
    url = "file:///" + html_path.replace("\\", "/")
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        f"--window-size={win_size}",
        f"--screenshot={output_path}",
        url
    ]
    print(f"Capturing: {output_name}...")
    subprocess.run(cmd, check=True)
    time.sleep(0.5)

print("All screenshots captured successfully!")
