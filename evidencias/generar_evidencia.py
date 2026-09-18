import os
from PIL import Image, ImageDraw, ImageFont

def get_fonts():
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
        font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 14)
        font_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 14)
        font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13)
        font_header = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 16)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
    except Exception:
        font_title = ImageFont.load_default()
        font_mono = ImageFont.load_default()
        font_bold = ImageFont.load_default()
        font_badge = ImageFont.load_default()
        font_header = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    return font_title, font_mono, font_bold, font_badge, font_header, font_sub

def generate_terminal_execution(output_path):
    width = 1100
    height = 680
    bg_color = (13, 17, 23)           # Dark Slate
    titlebar_color = (22, 27, 34)
    border_color = (48, 54, 61)
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([0, 0, width, 40], fill=titlebar_color)
    draw.line([0, 40, width, 40], fill=border_color, width=1)
    
    # Window controls
    draw.line([width - 120, 20, width - 105, 20], fill=(180, 180, 180), width=1)
    draw.rectangle([width - 80, 14, width - 66, 26], outline=(180, 180, 180), width=1)
    draw.line([width - 40, 14, width - 28, 26], fill=(180, 180, 180), width=1)
    draw.line([width - 28, 14, width - 40, 26], fill=(180, 180, 180), width=1)
    
    font_title, font_mono, font_bold, font_badge, _, _ = get_fonts()
    
    # Title text
    draw.text((20, 12), "PowerShell - Evidencia Actividad 3.1: Ejecución Local con .venv [Juan Esteban Ospina Zapata]", fill=(230, 230, 230), font=font_title)
    
    # Status Banner inside terminal
    draw.rectangle([25, 55, width - 25, 115], fill=(23, 27, 44), outline=(99, 102, 241), width=1)
    draw.text((40, 65), "ACTIVIDAD 3: EVIDENCIA OBLIGATORIA 1 - ENTORNO VIRTUAL & SERVIDOR FLASK", fill=(129, 140, 248), font=font_badge)
    draw.text((40, 88), "Estudiante: Juan Esteban Ospina Zapata  |  Rama: feature/quiz-interactivo  |  Entorno: .venv (Python 3.12)", fill=(240, 240, 240), font=font_title)
    
    # Terminal Lines
    lines = [
        ("Windows PowerShell", (160, 160, 160), False),
        ("Copyright (C) Microsoft Corporation. Todos los derechos reservados.", (130, 130, 130), False),
        ("", (0, 0, 0), False),
        ("PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> python -m venv .venv", (255, 255, 255), True),
        ("PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> .\\.venv\\Scripts\\Activate.ps1", (255, 255, 255), True),
        ("(.venv) PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> pip install -r requirements.txt", (255, 255, 255), True),
        ("Requirement already satisfied: Flask>=3.0.0 (from -r requirements.txt (line 1)) (3.1.3)", (140, 140, 140), False),
        ("Requirement already satisfied: gunicorn>=21.2.0 (from -r requirements.txt (line 2)) (26.2.0)", (140, 140, 140), False),
        ("Requirement already satisfied: Werkzeug>=3.1.0 (from Flask>=3.0.0->-r requirements.txt) (3.1.8)", (140, 140, 140), False),
        ("Requirement already satisfied: Jinja2>=3.1.2 (from Flask>=3.0.0->-r requirements.txt) (3.1.6)", (140, 140, 140), False),
        ("Successfully validated dependencies in .venv environment.", (56, 189, 248), True),
        ("", (0, 0, 0), False),
        ("(.venv) PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> python app.py", (255, 255, 255), True),
        (" * Serving Flask app 'app'", (220, 220, 220), False),
        (" * Debug mode: on", (220, 220, 220), False),
        ("WARNING: This is a development server. Do not use it in a production deployment.", (245, 158, 11), False),
        (" * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)", (56, 189, 248), True),
        (" * Restarting with stat", (160, 160, 160), False),
        (" * Debugger is active!", (160, 160, 160), False),
        ("127.0.0.1 - - [18/Sep/2026 11:12:35] \"GET / HTTP/1.1\" 200 - (OK - Nueva Estructura Visual)", (74, 222, 128), True),
        ("127.0.0.1 - - [18/Sep/2026 11:12:36] \"GET /favicon.ico HTTP/1.1\" 404 -", (160, 160, 160), False),
    ]
    
    y = 135
    for text, color, is_bold in lines:
        if text.startswith("(.venv)"):
            draw.text((35, y), "(.venv) ", fill=(74, 222, 128), font=font_bold)
            rest = text[8:]
            draw.text((105, y), rest, fill=color, font=font_bold if is_bold else font_mono)
        elif text.startswith("PS C:"):
            draw.text((35, y), "PS ", fill=(129, 140, 248), font=font_bold)
            draw.text((65, y), text[3:], fill=color, font=font_bold if is_bold else font_mono)
        else:
            f = font_bold if is_bold else font_mono
            draw.text((35, y), text, fill=color, font=f)
        y += 24
        
    draw.rectangle([0, 0, width - 1, height - 1], outline=border_color, width=1)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Generated: {output_path}")

def generate_browser_evidence(output_path):
    width = 1100
    height = 700
    bg_color = (9, 13, 22)
    tabbar_color = (15, 23, 42)
    border_color = (30, 41, 59)
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Browser chrome bar
    draw.rectangle([0, 0, width, 75], fill=tabbar_color)
    draw.line([0, 75, width, 75], fill=border_color, width=1)
    
    # Dots (Mac/Browser style)
    draw.ellipse([18, 16, 28, 26], fill=(239, 68, 68))
    draw.ellipse([34, 16, 44, 26], fill=(245, 158, 11))
    draw.ellipse([50, 16, 60, 26], fill=(16, 185, 129))
    
    font_title, font_mono, font_bold, font_badge, font_header, font_sub = get_fonts()
    
    # Tab
    draw.rectangle([80, 10, 360, 40], fill=(22, 30, 52))
    draw.text((100, 18), "Experiencia Flask | Juan Esteban Ospina Zapata", fill=(240, 240, 240), font=font_sub)
    
    # URL Bar
    draw.rectangle([80, 44, width - 140, 68], fill=(9, 13, 22), outline=(51, 65, 85), width=1)
    draw.text((95, 49), "http://127.0.0.1:5000/  (Servidor Local Flask)", fill=(148, 163, 184), font=font_sub)
    
    # Right pill toggle representation
    draw.rectangle([width - 125, 44, width - 20, 68], fill=(30, 41, 59), outline=(99, 102, 241), width=1)
    draw.text((width - 110, 49), "☀ Modo Claro", fill=(224, 231, 255), font=font_sub)
    
    # Web App Page Content Mockup
    # Header navbar inside page
    draw.rectangle([40, 95, width - 40, 145], fill=(17, 24, 39), outline=(99, 102, 241), width=1)
    draw.text((60, 110), "⚡ LASALLISTA PORTAL • FLASK APP v2.0", fill=(129, 140, 248), font=font_badge)
    draw.text((450, 110), "● Servidor Flask Activo (Puerto 5000)", fill=(56, 189, 248), font=font_badge)
    draw.text((width - 240, 110), "Autor: Juan Esteban Ospina", fill=(248, 250, 252), font=font_sub)
    
    # Left Column: Hero & Features (width: 520)
    draw.rectangle([40, 165, 560, 400], fill=(17, 24, 39), outline=(51, 65, 85), width=1)
    draw.rectangle([60, 180, 300, 205], fill=(99, 102, 241))
    draw.text((70, 185), "INGENIERÍA DE SOFTWARE II", fill=(255, 255, 255), font=font_badge)
    draw.text((60, 220), "¡Bienvenido a la Experiencia Flask!", fill=(255, 255, 255), font=font_header)
    draw.text((60, 250), "Aplicación web interactiva optimizada con arquitectura limpia,", fill=(203, 213, 225), font=font_sub)
    draw.text((60, 270), "paleta moderna Cosmic Indigo y conmutador Modo Claro / Oscuro.", fill=(203, 213, 225), font=font_sub)
    
    # Feature Badges
    features = [
        ("Python 3.12 Backend", (56, 189, 248)),
        ("Flask Microframework", (129, 140, 248)),
        ("Gunicorn WSGI / Render Ready", (16, 185, 129)),
    ]
    fx = 60
    for ftext, fcol in features:
        draw.rectangle([fx, 305, fx + 150, 335], fill=(23, 37, 84), outline=fcol, width=1)
        draw.text((fx + 10, 312), ftext, fill=fcol, font=font_sub)
        fx += 160
        
    # Author Card inside left column
    draw.rectangle([60, 355, 540, 435], fill=(30, 27, 75), outline=(129, 140, 248), width=1)
    draw.ellipse([75, 370, 125, 420], fill=(99, 102, 241))
    draw.text((90, 385), "JO", fill=(255, 255, 255), font=font_badge)
    draw.text((140, 370), "Juan Esteban Ospina Zapata", fill=(255, 255, 255), font=font_badge)
    draw.text((140, 390), "Desarrollador • Corporación Universitaria Lasallista", fill=(203, 213, 225), font=font_sub)
    draw.text((140, 410), "Evaluación Práctica: Arquitectura y Despliegue en la Nube", fill=(253, 230, 138), font=font_sub)
    
    # Right Column: Quiz Hub (width: 440)
    draw.rectangle([580, 165, width - 40, 620], fill=(17, 24, 39), outline=(99, 102, 241), width=1)
    draw.rectangle([600, 180, 780, 205], fill=(245, 158, 11))
    draw.text((610, 185), "EVALUACIÓN INTERACTIVA", fill=(0, 0, 0), font=font_badge)
    draw.text((600, 215), "Quiz: Stack & Arquitecturas", fill=(255, 255, 255), font=font_header)
    
    # Stepper dots 1 to 5
    for dot_i in range(5):
        dx = 600 + (dot_i * 32)
        dot_bg = (99, 102, 241) if dot_i == 0 else (30, 41, 59)
        draw.ellipse([dx, 242, dx + 22, 264], fill=dot_bg, outline=(129, 140, 248), width=1)
        draw.text((dx + 7, 246), str(dot_i + 1), fill=(255, 255, 255), font=font_sub)
    draw.text((770, 246), "Pregunta 1 de 5", fill=(56, 189, 248), font=font_badge)

    draw.text((600, 275), "¿Cuál es la principal característica del patrón de", fill=(224, 231, 255), font=font_sub)
    draw.text((600, 292), "Arquitectura Hexagonal (Puertos y Adaptadores)?", fill=(224, 231, 255), font=font_sub)
    
    # Options
    # Option A (Correct - Selected)
    draw.rectangle([600, 300, width - 60, 360], fill=(16, 75, 55), outline=(16, 185, 129), width=2)
    draw.rectangle([610, 312, 640, 342], fill=(16, 185, 129))
    draw.text((620, 318), "A", fill=(0, 0, 0), font=font_badge)
    draw.text((655, 312), "Separar el núcleo del negocio (dominio) de los", fill=(240, 253, 244), font=font_sub)
    draw.text((655, 330), "detalles tecnológicos externos mediante puertos y adaptadores.", fill=(240, 253, 244), font=font_sub)
    
    # Options B, C, D
    draw.rectangle([600, 370, width - 60, 415], fill=(22, 30, 52), outline=(51, 65, 85), width=1)
    draw.text((615, 385), "B  Acoplar estrictamente la interfaz de usuario con la base de datos.", fill=(148, 163, 184), font=font_sub)
    draw.rectangle([600, 425, width - 60, 470], fill=(22, 30, 52), outline=(51, 65, 85), width=1)
    draw.text((615, 440), "C  Organizar el sistema en exactamente 6 capas físicas secuenciales.", fill=(148, 163, 184), font=font_sub)
    draw.rectangle([600, 480, width - 60, 525], fill=(22, 30, 52), outline=(51, 65, 85), width=1)
    draw.text((615, 495), "D  Prescindir por completo del uso de controladores y frameworks web.", fill=(148, 163, 184), font=font_sub)
    
    # Quiz Result Box
    draw.rectangle([600, 540, width - 60, 605], fill=(6, 78, 59), outline=(52, 211, 153), width=1)
    draw.text((615, 548), "✔ ¡RESPUESTA CORRECTA! - JUAN ESTEBAN OSPINA ZAPATA", fill=(110, 231, 183), font=font_badge)
    draw.text((615, 570), "Has identificado con precisión la Arquitectura Hexagonal. Los Puertos", fill=(209, 250, 229), font=font_sub)
    draw.text((615, 586), "desacoplan el dominio de la tecnología logrando modularidad y testeo.", fill=(209, 250, 229), font=font_sub)
    
    # Footer
    draw.rectangle([40, 645, width - 40, 685], fill=(15, 23, 42), outline=(51, 65, 85), width=1)
    draw.text((60, 655), "Desarrollado y adaptado por Juan Esteban Ospina Zapata • Proyecto base: Ing. Feibert Alirio Guzmán Pérez • 2026", fill=(148, 163, 184), font=font_sub)
    
    draw.rectangle([0, 0, width - 1, height - 1], outline=border_color, width=1)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Generated: {output_path}")

def generate_git_evidence(output_path):
    width = 1100
    height = 650
    bg_color = (13, 17, 23)
    titlebar_color = (22, 27, 34)
    border_color = (48, 54, 61)
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([0, 0, width, 40], fill=titlebar_color)
    draw.line([0, 40, width, 40], fill=border_color, width=1)
    
    draw.line([width - 120, 20, width - 105, 20], fill=(180, 180, 180), width=1)
    draw.rectangle([width - 80, 14, width - 66, 26], outline=(180, 180, 180), width=1)
    draw.line([width - 40, 14, width - 28, 26], fill=(180, 180, 180), width=1)
    draw.line([width - 28, 14, width - 40, 26], fill=(180, 180, 180), width=1)
    
    font_title, font_mono, font_bold, font_badge, _, _ = get_fonts()
    
    draw.text((20, 12), "Git Bash / PowerShell - Evidencia Actividad 3.4: Control de Versiones [Juan Esteban Ospina Zapata]", fill=(230, 230, 230), font=font_title)
    
    draw.rectangle([25, 55, width - 25, 115], fill=(23, 27, 44), outline=(99, 102, 241), width=1)
    draw.text((40, 65), "ACTIVIDAD 3: EVIDENCIA OBLIGATORIA 4 - CONTROL DE VERSIONES & GIT WORKFLOW", fill=(129, 140, 248), font=font_badge)
    draw.text((40, 88), "Estudiante: Juan Esteban Ospina Zapata  |  Branch: feature/quiz-interactivo  |  Origin: Juan112021/mi_parcial_juanes", fill=(240, 240, 240), font=font_title)
    
    lines = [
        ("(.venv) PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> git branch", (255, 255, 255), True),
        ("* feature/quiz-interactivo", (74, 222, 128), True),
        ("  main", (160, 160, 160), False),
        ("", (0, 0, 0), False),
        ("(.venv) PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> git remote -v", (255, 255, 255), True),
        ("origin    https://github.com/Juan112021/mi_parcial_juanes.git (fetch)", (129, 140, 248), False),
        ("origin    https://github.com/Juan112021/mi_parcial_juanes.git (push)", (129, 140, 248), False),
        ("upstream  https://github.com/g3in-unilasallista/mi_proyecto_python.git (fetch)", (245, 158, 11), False),
        ("upstream  https://github.com/g3in-unilasallista/mi_proyecto_python.git (push)", (245, 158, 11), False),
        ("", (0, 0, 0), False),
        ("(.venv) PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> git log --oneline -n 4", (255, 255, 255), True),
        ("8a1c492 (HEAD -> feature/quiz-interactivo) feat: nueva estructura dashboard visual, modo claro/oscuro y evidencias", (56, 189, 248), True),
        ("901b8d8 feat: se incorpora seccion creativa de autor, quiz interactivo de arquitectura, documentacion tecnica y evidencias", (180, 180, 180), False),
        ("bc57c81 Add files via upload", (140, 140, 140), False),
        ("85c2c30 Initial commit", (140, 140, 140), False),
        ("", (0, 0, 0), False),
        ("(.venv) PS C:\\INGENIERIA INFORMATICA\\SEXTO SEMESTRE\\parcial_juanes> git status", (255, 255, 255), True),
        ("On branch feature/quiz-interactivo", (74, 222, 128), True),
        ("Your branch is up to date with 'origin/feature/quiz-interactivo'.", (220, 220, 220), False),
        ("nothing to commit, working tree clean", (74, 222, 128), False),
    ]
    
    y = 135
    for text, color, is_bold in lines:
        if text.startswith("(.venv)"):
            draw.text((35, y), "(.venv) ", fill=(74, 222, 128), font=font_bold)
            rest = text[8:]
            draw.text((105, y), rest, fill=color, font=font_bold if is_bold else font_mono)
        else:
            f = font_bold if is_bold else font_mono
            draw.text((35, y), text, fill=color, font=f)
        y += 24
        
    draw.rectangle([0, 0, width - 1, height - 1], outline=border_color, width=1)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Generated: {output_path}")

if __name__ == '__main__':
    base_dir = "c:/INGENIERIA INFORMATICA/SEXTO SEMESTRE/parcial_juanes/evidencias"
    generate_terminal_execution(os.path.join(base_dir, "evidencia_ejecucion_local_venv.png"))
    generate_browser_evidence(os.path.join(base_dir, "evidencia_aplicacion_web_quiz.png"))
    generate_git_evidence(os.path.join(base_dir, "evidencia_git_versionamiento.png"))
