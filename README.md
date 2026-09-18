# Proyecto Flask - Aplicacion Web & Modulo de Evaluacion Interactiva

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-WSGI-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Semantico-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Glassmorphism-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Render](https://img.shields.io/badge/Render-Cloud_Deploy-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Git](https://img.shields.io/badge/Git-VCS-F05032?style=for-the-badge&logo=git&logoColor=white)
![Licencia](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Aplicacion web moderna y responsiva desarrollada con **Python** y **Flask**, adaptada como parte de la evaluacion practica de **Ingenieria de Software II** de la **Corporacion Universitaria Lasallista**. Integra una estetica organica con efectos de cristal esmerilado (*glassmorphism*), graficos vectoriales SVG y un modulo evaluativo interactivo tipo Quiz enfocado en **Stack y Arquitecturas de Software**.

---

## Informacion del Estudiante y Autor

- **Estudiante y Desarrollador:** Juan Esteban Ospina Zapata
- **Programa:** Ingenieria Informatica / Ingenieria de Software II
- **Institucion:** Corporacion Universitaria Lasallista
- **Repositorio Fork:** [Juan112021/mi_parcial_juanes](https://github.com/Juan112021/mi_parcial_juanes)
- **Repositorio Base:** [g3in-unilasallista/mi_proyecto_python](https://github.com/g3in-unilasallista/mi_proyecto_python)
- **Credito del Proyecto Base:** Ing. Feibert Alirio Guzman Perez

---

## Seleccion de Stack y Arquitectura de Software

| Elemento | Seleccion Tecnologica |
| :--- | :--- |
| **Lenguaje de programacion** | Python 3.12+ |
| **Framework backend** | Flask (Microframework WSGI) |
| **Tecnologias frontend** | HTML5 semantico, CSS3 (Variables, Flexbox, Grid, Glassmorphism), Vanilla JavaScript |
| **Almacenamiento / Datos** | Renderizado del lado del servidor (SSR con Jinja2) y gestion de estado en memoria del cliente |
| **Arquitectura / Patron** | Arquitectura Monolitica ligera basada en el patron Modelo-Vista-Controlador (MVC / MVT) |
| **Servicio de despliegue** | Render (Web Service administrado con Gunicorn) |

### Justificacion de la Arquitectura y del Stack Tecnologico
Se selecciono una arquitectura monolitica ligera con Flask dado que satisface de forma directa los requisitos de simplicidad operativa, bajo consumo computacional y agilidad en el ciclo de vida del desarrollo. Al no requerir persistencia relacional compleja para esta fase evaluativa, el patron desacoplado de Flask en conjunto con JavaScript moderno en el cliente permite retroalimentacion inmediata al estudiante sin sobrecargar el servidor, garantizando ademas un empaquetado optimo para su puesta en produccion mediante Gunicorn en Render.

---

## Analisis de la Estructura del Proyecto

```text
parcial_juanes/
|-- .gitignore                     # Exclusion de temporales y entorno virtual (.venv)
|-- app.py                         # Punto de entrada y controlador principal de la aplicacion Flask
|-- Procfile                       # Definicion del proceso de inicio para la nube (Gunicorn)
|-- README.md                      # Documentacion integral y guia del proyecto
|-- requirements.txt               # Especificacion de dependencias del proyecto
|-- templates/
|   `-- index.html                 # Vista principal con diseno organico y quiz interactivo
`-- evidencias/
    |-- evidencia_ejecucion_local_venv.png   # Captura de ejecucion local con .venv
    `-- generar_evidencia.py       # Script utilitario de generacion de evidencias
```

- **Controlador (`app.py`):** Define la instancia de la aplicacion Flask, mapea la ruta raiz `/` y despacha la plantilla visual.
- **Vista (`templates/index.html`):** Contiene la estructura HTML5 semantica, el sistema de diseno CSS3 y la logica de evaluacion interactiva en JavaScript.
- **Configuracion de Produccion (`Procfile`):** Especifica el comando de ejecucion `web: gunicorn app:app` para el entorno de ejecucion en Render.

---

## Funcionalidad de Quiz Interactivo

El modulo de evaluacion sobre Arquitecturas de Software cumple con todas las especificaciones tecnicas:
- **Tematica abordada:** Arquitectura Hexagonal (Patron de Puertos y Adaptadores).
- **Opciones de respuesta:** Cuatro alternativas (A, B, C, D) con prefijo diferenciado y seleccion dinamica.
- **Identificacion visual:** La opcion seleccionada adquiere iluminacion y borde resaltado.
- **Retroalimentacion inmediata:**
  - Si es correcta: destello verde esmeralda con mensaje de felicitacion y justificacion tecnica del desacoplamiento de dominio.
  - Si es incorrecta: destello carmesi, indicacion didactica del error y revelacion de la respuesta acertada.
- **Reinicio:** Permite volver a practicar y limpiar los estados de seleccion.

---

## Guia de Instalacion y Ejecucion Local

Siga estas instrucciones paso a paso para desplegar la aplicacion en su entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/Juan112021/mi_parcial_juanes.git
cd mi_parcial_juanes
```

### 2. Crear y configurar el entorno virtual (.venv)
El entorno virtual aísla las librerias del proyecto sin alterar el sistema operativo base:
```bash
# Crear el entorno virtual con Python 3
python -m venv .venv

# Activar en Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Activar en Linux / macOS
source .venv/bin/activate
```
*(Nota en Windows: Si la directiva de ejecucion restringe scripts, ejecute antes `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`).*

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor de desarrollo Flask
```bash
python app.py
```

### 5. Acceder en el navegador
Abra su navegador web e ingrese a:
```text
http://127.0.0.1:5000/
```

---

## Evidencia Obligatoria de Ejecucion Local con `.venv`

A continuacion se presenta la evidencia grafica de la configuracion del entorno virtual, instalacion de paquetes y ejecucion del servidor Flask:

![Evidencia de ejecucion local con .venv](evidencias/evidencia_ejecucion_local_venv.png)

---

## Diagrama del Pipeline de Trabajo (Actividad 4)

El siguiente esquema representa el flujo continuo de trabajo tecnico desarrollado durante la practica:

```text
+-------------------+      +--------------------+      +---------------------------------+
|      1. FORK      | ---> |     2. CLONE       | ---> |    3. EJECUCION LOCAL (.venv)   |
| Repositorio Base  |      | Entorno Local      |      | Creacion, Activacion y Pip      |
+-------------------+      +--------------------+      +---------------------------------+
                                                                       |
                                                                       v
+-------------------+      +--------------------+      +---------------------------------+
|     6. QUIZ       | <--- | 5. MODIF. HTML     | <--- |   4. RAMA (branch de trabajo)   |
| Modulo Evaluativo |      | Seccion Autor      |      | feature/quiz-interactivo        |
+-------------------+      +--------------------+      +---------------------------------+
         |
         v
+-------------------+      +--------------------+      +---------------------------------+
|    7. COMMIT      | ---> |     8. PUSH        | ---> |       9. PULL REQUEST           |
| Guardado Semantico|      | Subida a GitHub    |      | Hacia g3in-unilasallista        |
+-------------------+      +--------------------+      +---------------------------------+
                                                                       |
                                                                       v
                                                       +---------------------------------+
                                                       |           10. RENDER            |
                                                       | Despliegue en la Nube (Gunicorn)|
                                                       +---------------------------------+
```

---

## Despliegue en la Nube (Render)

### Archivo `Procfile` y Gunicorn
- **`Procfile`:** Declara el tipo de proceso a inicializar en la plataforma de nube:
  ```text
  web: gunicorn app:app
  ```
- **Gunicorn:** Servidor WSGI robusto para entornos de produccion que gestiona multiples workers concurrentes de forma eficiente y segura.

### Pasos para el despliegue en Render
1. Iniciar sesion en [Render.com](https://render.com) vinculando la cuenta de GitHub.
2. Hacer clic en **New +** y seleccionar **Web Service**.
3. Seleccionar el repositorio `Juan112021/mi_parcial_juanes`.
4. Diligenciar la configuracion:
   - **Name:** `mi-parcial-juanes`
   - **Environment / Runtime:** `Python 3`
   - **Branch:** `main` (o `feature/quiz-interactivo` segun la rama elegida)
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Seleccionar el plan gratuito (**Free**) y pulsar **Deploy Web Service**.
6. Render generara una URL publica con certificado SSL HTTPS para el acceso global.

---

## Descripcion Creativa para el Pull Request

> Esta propuesta de integracion, desarrollada por **Juan Esteban Ospina Zapata**, enriquece la experiencia visual de la aplicacion mediante una evolucion armonica del frontend en HTML5 y CSS3, incorporando una distinguida seccion de autor que resalta la identidad del desarrollador y dando vida a un modulo interactivo de evaluacion sobre Arquitecturas de Software con validacion en tiempo real que potencia el aprendizaje colaborativo sin desdibujar la serenidad organica y elegancia del proyecto base.

---

## Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Consulte el archivo [LICENSE](LICENSE) para obtener mas detalles.
