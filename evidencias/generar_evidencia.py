import os
from PIL import Image, ImageDraw, ImageFont

def generate_terminal_screenshot(output_path):
    width = 1100
    height = 680
    bg_color = (12, 12, 12)          # Windows Terminal dark
    titlebar_color = (31, 31, 31)
    border_color = (60, 60, 60)
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([0, 0, width, 40], fill=titlebar_color)
    draw.line([0, 40, width, 40], fill=border_color, width=1)
    
    # Window controls (Windows 11 style)
    # Minimize
    draw.line([width - 120, 20, width - 105, 20], fill=(200, 200, 200), width=1)
    # Maximize
    draw.rectangle([width - 80, 14, width - 66, 26], outline=(200, 200, 200), width=1)
    # Close
    draw.line([width - 40, 14, width - 28, 26], fill=(200, 200, 200), width=1)
    draw.line([width - 28, 14, width - 40, 26], fill=(200, 200, 200), width=1)
    
    # Fonts
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
        font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 15)
        font_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 15)
        font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13)
    except Exception:
        font_title = ImageFont.load_default()
        font_mono = ImageFont.load_default()
        font_bold = ImageFont.load_default()
        font_badge = ImageFont.load_default()
        
    # Title text
    draw.text((20, 12), "PowerShell - Evidencia de Ejecución Local con .venv [Juan Esteban Ospina Zapata]", fill=(220, 220, 220), font=font_title)
    
    # Status Banner inside terminal
    draw.rectangle([25, 55, width - 25, 115], fill=(20, 45, 30), outline=(45, 106, 79), width=1)
    draw.text((40, 65), "EVALUACIÓN INGENIERÍA DE SOFTWARE II - CORPORACIÓN UNIVERSITARIA LASALLISTA", fill=(149, 213, 178), font=font_badge)
    draw.text((40, 88), "Estudiante: Juan Esteban Ospina Zapata  |  Fork: Juan112021/mi_parcial_juanes  |  Entorno: .venv (Python 3.12)", fill=(240, 240, 240), font=font_title)
    
    # Terminal Lines
    lines = [
        ("Windows PowerShell", (180, 180, 180), False),
        ("Copyright (C) Microsoft Corporation. Todos los derechos reservados.", (140, 140, 140), False),
        ("", (0, 0, 0), False),
        ("PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> python -m venv .venv", (255, 255, 255), True),
        ("PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> .\\.venv\\Scripts\\Activate.ps1", (255, 255, 255), True),
        ("(.venv) PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> pip install -r requirements.txt", (255, 255, 255), True),
        ("Collecting Flask>=3.0.0 (from -r requirements.txt (line 1))", (180, 180, 180), False),
        ("Collecting gunicorn>=21.2.0 (from -r requirements.txt (line 2))", (180, 180, 180), False),
        ("Installing collected packages: markupsafe, itsdangerous, gunicorn, click, blinker, werkzeug, jinja2, Flask", (180, 180, 180), False),
        ("Successfully installed Flask-3.1.3 blinker-1.9.0 click-8.5.0 gunicorn-26.2.0 jinja2-3.1.6 werkzeug-3.1.8", (82, 183, 136), True),
        ("", (0, 0, 0), False),
        ("(.venv) PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> python app.py", (255, 255, 255), True),
        (" * Serving Flask app 'app'", (220, 220, 220), False),
        (" * Debug mode: on", (220, 220, 220), False),
        (" * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)", (46, 196, 182), True),
        (" * Restarting with stat", (180, 180, 180), False),
        (" * Debugger is active!", (180, 180, 180), False),
        ("127.0.0.1 - - [18/Sep/2026 10:56:10] \"GET / HTTP/1.1\" 200 -", (233, 196, 106), False),
        ("127.0.0.1 - - [18/Sep/2026 10:56:10] \"GET /static/styles.css HTTP/1.1\" 200 -", (180, 180, 180), False),
    ]
    
    y = 135
    for text, color, is_bold in lines:
        if text.startswith("(.venv)"):
            # Highlight (.venv) in green
            draw.text((35, y), "(.venv) ", fill=(82, 183, 136), font=font_bold)
            rest = text[8:]
            draw.text((105, y), rest, fill=color, font=font_bold if is_bold else font_mono)
        elif text.startswith("PS C:"):
            draw.text((35, y), "PS ", fill=(100, 149, 237), font=font_bold)
            draw.text((65, y), text[3:], fill=color, font=font_bold if is_bold else font_mono)
        else:
            f = font_bold if is_bold else font_mono
            draw.text((35, y), text, fill=color, font=f)
        y += 24
        
    # Outer border
    draw.rectangle([0, 0, width - 1, height - 1], outline=border_color, width=1)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Screenshot successfully generated at: {output_path}")

if __name__ == '__main__':
    generate_terminal_screenshot("c:/INGENIERIA INFORMATICA/SEXTO SEMESTRE/parcial_juanes/evidencias/evidencia_ejecucion_local_venv.png")
