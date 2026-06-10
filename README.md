# 🚀 Auditoría Automatizada de Clases y Generación de Reportes

Este repositorio alberga un sistema integral para la auditoría automatizada de grabaciones de clases, utilizando capacidades avanzadas de inteligencia artificial multimodal y herramientas de procesamiento de video. El proyecto está diseñado para descargar videos de Google Drive, optimizarlos, analizarlos mediante la API de Google Gemini, y generar reportes de auditoría detallados en formatos estructurados (JSON, TXT, CSV) y convertirlos a PDF profesionales.

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Unlicensed-red.svg)](https://choosealicense.com/no-permission/)
[![Project Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/yourusername/yourrepo/pulse)
[![Google Gemini API](https://img.shields.io/badge/Google%20Gemini%20API-2.5%20Flash-orange.svg)](https://ai.google.dev/models/gemini)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-lightgrey.svg)](https://ffmpeg.org/)

## 📋 Tabla de Contenidos

1.  [Arquitectura del Proyecto](#1-arquitectura-del-proyecto)
    *   [Módulo `main.py`](#módulo-mainpy)
    *   [Módulo `Create_html_to_PDF.py`](#módulo-create_html_to_pdfpy)
2.  [Requisitos del Sistema Operativo](#2-requisitos-del-sistema-operativo)
3.  [Dependencias de Python](#3-dependencias-de-python)
4.  [Configuración del Entorno](#4-configuración-del-entorno)
    *   [Variables de Entorno (`.env`)](#variables-de-entorno-env)
    *   [Credenciales de Google (`credentials_module.json`)](#credenciales-de-google-credentials_modulejson)
5.  [Uso](#5-uso)
    *   [Paso 1: Descargar y Auditar Videos](#paso-1-descargar-y-auditar-videos)
    *   [Paso 2: Generar Reportes HTML y PDF](#paso-2-generar-reportes-html-y-pdf)
6.  [Ejemplos de Salida](#6-ejemplos-de-salida)
    *   [Estructura JSON del Reporte de Auditoría](#estructura-json-del-reporte-de-auditoría)
7.  [Detalles Técnicos y Valor Agregado](#7-detalles-técnicos-y-valor-agregado)
    *   [Integración con Google Drive (`pydrive2`)](#integración-con-google-drive-pydrive2)
    *   [Optimización y Procesamiento de Video (`moviepy`, `FFmpeg`)](#optimización-y-procesamiento-de-video-moviepy-ffmpeg)
    *   [Análisis Multimodal con Google Gemini API](#análisis-multimodal-con-google-gemini-api)
    *   [Generación de Reportes Estructurados (`pandas`, `xhtml2pdf`)](#generación-de-reportes-estructurados-pandas-xhtml2pdf)
8.  [Consideraciones de Seguridad](#8-consideraciones-de-seguridad)

---

## 1. Arquitectura del Proyecto

El sistema se compone de dos módulos principales que operan de forma secuencial para lograr la automatización completa:

### Módulo `main.py`

Este script es el orquestador principal del proceso de auditoría. Sus funciones clave incluyen:

*   **Autenticación y Descarga de Google Drive**: Se conecta a Google Drive utilizando `pydrive2` para listar y descargar videos de una carpeta específica. Implementa reintentos y verificación de tamaño para asegurar descargas completas.
*   **Optimización de Video**: Comprime y acelera los videos descargados para reducir su tamaño y duración, optimizándolos para la ingesta en la API de Google Gemini. Utiliza `moviepy` como primera opción y `FFmpeg` directo como fallback robusto.
*   **Análisis Multimodal con Google Gemini**: Sube los videos optimizados a la API de Google Gemini (modelo `gemini-2.5-flash`) para un análisis profundo del contenido de la clase.
*   **Manejo de Videos Largos**: Si un video excede los límites de tokens de la API, `FFmpeg` lo segmenta automáticamente en partes más pequeñas. Gemini procesa cada segmento, acumulando y refinando el informe de auditoría de forma iterativa.
*   **Generación de Reportes Estructurados**: La respuesta de Gemini, formateada como JSON, se guarda en archivos `.txt` y se convierte en un `DataFrame` de `pandas` para generar un archivo `.csv` detallado.

### Módulo `Create_html_to_PDF.py`

Este script se encarga de la presentación final de los reportes de auditoría:

*   **Lectura de Reportes TXT**: Identifica los archivos de reporte `.txt` generados por `main.py`.
*   **Generación de HTML con Gemini**: Utiliza la API de Google Gemini para transformar el contenido de los reportes `.txt` en código HTML estético y profesional, siguiendo una plantilla CSS predefinida y restricciones de estilo específicas.
*   **Conversión a PDF**: Convierte los archivos HTML generados en documentos PDF utilizando la librería `xhtml2pdf`, asegurando un formato de reporte final listo para su distribución.

## 2. Requisitos del Sistema Operativo

Para el correcto funcionamiento del proyecto, es indispensable tener instaladas las siguientes herramientas a nivel de sistema operativo:

*   **FFmpeg**: Es la herramienta fundamental para el procesamiento de video (compresión, aceleración, segmentación).
    *   **Instalación (Linux/macOS)**: `sudo apt-get install ffmpeg` o `brew install ffmpeg`
    *   **Instalación (Windows)**: Descargar el ejecutable desde [ffmpeg.org](https://ffmpeg.org/download.html) y añadirlo a la variable de entorno PATH del sistema. La librería `imageio-ffmpeg` ayuda a localizarlo, pero `ffmpeg` debe estar disponible en el sistema.

## 3. Dependencias de Python

Se recomienda instalar las dependencias en un entorno virtual.

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

El archivo `requirements.txt` debe contener las siguientes librerías:

```
google-generativeai
python-dotenv
pydrive2
moviepy
imageio-ffmpeg
pandas
xhtml2pdf
oauth2client # Necesario para pydrive2 y gspread (si se usa)
gspread # Importado en main.py, aunque no usado en la lógica actual, se mantiene por si se extiende.
```

## 4. Configuración del Entorno

### Variables de Entorno (`.env`)

Cree un archivo `.env` en la raíz del proyecto con las siguientes variables:

```ini
API_KEY_GEMINI_PRO_1.5="TU_API_KEY_DE_GOOGLE_GEMINI"
carpeta_drive="ID_DE_TU_CARPETA_DE_GOOGLE_DRIVE"
```

*   **`API_KEY_GEMINI_PRO_1.5`**: Su clave de API para acceder a Google Gemini. Puede obtenerla desde [Google AI Studio](https://aistudio.google.com/app/apikey).
*   **`carpeta_drive`**: El ID de la carpeta de Google Drive donde se encuentran los videos a auditar. Este ID se encuentra en la URL de la carpeta (ej. `https://drive.google.com/drive/folders/ESTE_ES_EL_ID`).

### Credenciales de Google (`credentials_module.json`)

Para interactuar con Google Drive, el proyecto requiere un archivo de credenciales de cuenta de servicio.

1.  **Crear un Proyecto en Google Cloud Console**: Vaya a [console.cloud.google.com](https://console.cloud.google.com/) y cree un nuevo proyecto.
2.  **Habilitar APIs**: Habilite las APIs de `Google Drive API` y `Google Sheets API` (si planea usar `gspread` en el futuro) para su proyecto.
3.  **Crear Cuenta de Servicio**:
    *   Navegue a "IAM y administración" -> "Cuentas de servicio".
    *   Cree una nueva cuenta de servicio.
    *   Asigne un rol que permita el acceso a Google Drive (ej. "Lector de Drive" o "Editor de Drive" si necesita subir archivos).
4.  **Generar Clave JSON**:
    *   Edite la cuenta de servicio recién creada.
    *   Vaya a la sección "Claves" y haga clic en "Añadir clave" -> "Crear nueva clave".
    *   Seleccione "JSON" como tipo de clave y descárguela.
5.  **Renombrar y Ubicar**: Renombre el archivo JSON descargado a `credentials_module.json` y colóquelo en la raíz de su proyecto.
6.  **Compartir Carpeta de Drive**: Comparta la carpeta de Google Drive (`carpeta_drive`) con la dirección de correo electrónico de la cuenta de servicio (ej. `nombre-cuenta-servicio@proyecto-id.iam.gserviceaccount.com`).

## 5. Uso

El proceso se ejecuta en dos fases principales.

### Paso 1: Descargar y Auditar Videos

Ejecute el script `main.py` para iniciar la descarga, optimización y auditoría de los videos.

```bash
python main.py
```

Este script realizará las siguientes acciones:
1.  Se autenticará con Google Drive.
2.  Listará los videos en la carpeta especificada.
3.  Descargará cada video, verificando la integridad de la descarga.
4.  Optimizará el video (compresión y aceleración).
5.  Subirá el video (o sus segmentos) a Google Gemini para análisis.
6.  Generará un reporte de auditoría en formato JSON, TXT y CSV para cada video.
7.  Eliminará los archivos temporales de video y los archivos subidos a Gemini para optimizar el almacenamiento y los costos.

### Paso 2: Generar Reportes HTML y PDF

Una vez que `main.py` haya generado los archivos `.txt` de auditoría, ejecute `Create_html_to_PDF.py` para convertirlos en reportes HTML y PDF.

```bash
python Create_html_to_PDF.py
```

Este script:
1.  Leerá todos los archivos `Reporte_Auditoria_*.txt`.
2.  Utilizará Google Gemini para transformar el texto en HTML estilizado.
3.  Convertirá el HTML resultante en un archivo PDF.

## 6. Ejemplos de Salida

### Estructura JSON del Reporte de Auditoría

El módulo `main.py` genera un archivo `.txt` y `.csv` con la siguiente estructura JSON como base:

```json
{
  "resumen_clase": "La clase se centró en la introducción a la programación en Python, cubriendo variables, tipos de datos y estructuras de control básicas.",
  "objetivo_alcanzado": "Sí - Se cubrieron todos los temas planificados y se realizaron ejercicios prácticos.",
  "puntos_fuertes": [
    "Claridad en la explicación de conceptos complejos.",
    "Uso efectivo de ejemplos de código en tiempo real.",
    "Fomento de la participación activa con preguntas abiertas."
  ],
  "oportunidades_mejora": [
    "Algunas pausas prolongadas al buscar ejemplos.",
    "La velocidad de la presentación fue inconsistente en ciertos segmentos.",
    "No se utilizó una herramienta interactiva para encuestas rápidas."
  ],
  "recomendaciones_accionables": [
    "Preparar ejemplos de código con antelación para evitar pausas.",
    "Implementar una herramienta de votación rápida para evaluar la comprensión."
  ],
  "nivel_participacion": "Alta - Los alumnos hicieron preguntas pertinentes y respondieron a los ejercicios propuestos.",
  "manejo_del_tiempo": "Adecuado - El tiempo se distribuyó equitativamente entre explicación teórica y práctica, aunque el cierre fue un poco apresurado.",
  "herramientas_utilizadas": [
    "Presentación de diapositivas (Google Slides)",
    "IDE en línea (Replit)",
    "Pizarrón virtual (Jamboard)"
  ],
  "incidencias_notables": [
    "Breve interrupción de audio al inicio (30 segundos).",
    "Ninguna"
  ],
  "calificacion_pedagogica": 85,
  "calificacion_tecnica": 90,
  "comentario_final": "El profesor demostró un excelente dominio del tema y una metodología efectiva. Se sugiere optimizar la fluidez en las transiciones y explorar herramientas interactivas para maximizar el engagement."
}
```

El archivo `.csv` representará esta estructura en formato tabular, con las listas (`puntos_fuertes`, `oportunidades_mejora`, etc.) unidas por saltos de línea dentro de una misma celda.

## 7. Detalles Técnicos y Valor Agregado

### Integración con Google Drive (`pydrive2`)

*   **Robustez**: `pydrive2` ofrece una interfaz programática robusta y segura para interactuar con Google Drive. La implementación incluye lógica de reintentos y verificación de tamaño de archivo (`os.path.getsize` vs `fileSize` de Drive) para garantizar descargas completas y manejar fallos de red o API.
*   **Autenticación**: Utiliza `oauth2client.service_account.ServiceAccountCredentials` a través de `GoogleAuth` de `pydrive2` para una autenticación no interactiva, ideal para flujos de trabajo automatizados en servidores o scripts.

### Optimización y Procesamiento de Video (`moviepy`, `FFmpeg`)

*   **Estrategia de Compresión**: Los videos se optimizan para reducir el tamaño y la duración, lo cual es crucial para cumplir con los límites de tamaño y velocidad de procesamiento de la API de Gemini.
    *   **Redimensionamiento**: `height=240` (o `scale=-2:360` con FFmpeg) reduce drásticamente la resolución sin perder la inteligibilidad del contenido educativo.
    *   **Aceleración**: `MultiplySpeed(1.5)` (o `setpts=0.666667*PTS, atempo=1.5` con FFmpeg) acelera el video y el audio, permitiendo un análisis más rápido de clases extensas.
    *   **`fps=0.5`**: Reduce la tasa de fotogramas a un nivel mínimo aceptable para el análisis de contenido estático o semidinámico, optimizando aún más el tamaño.
    *   **`preset='ultrafast'`**: Prioriza la velocidad de codificación sobre la calidad, adecuado para videos destinados a análisis por IA.
    *   **`audio_bitrate='32k'`, `ac='1'`**: Reduce la calidad y convierte el audio a mono, minimizando el tamaño del componente de audio.
*   **Resiliencia**: La implementación prioriza `moviepy` por su API de alto nivel, pero incluye un fallback directo a `FFmpeg` a través de `subprocess` y `imageio-ffmpeg`. Esta estrategia asegura que el procesamiento de video sea robusto incluso si `moviepy` encuentra problemas específicos de códecs o configuraciones, aprovechando la eficiencia y fiabilidad de `FFmpeg`.
*   **Segmentación Inteligente**: Para videos que exceden los límites de tokens de la API de Gemini, `FFmpeg` se utiliza para segmentar el video en partes más pequeñas (`-segment_time '1500'` para segmentos de 25 minutos). Esto permite procesar clases de larga duración de forma incremental.

### Análisis Multimodal con Google Gemini API

*   **Modelo `gemini-2.5-flash`**: Elegido por su equilibrio entre rendimiento, velocidad y costo, siendo ideal para tareas de análisis de video donde la latencia es un factor.
*   **Análisis Multimodal**: La API de Gemini permite el análisis directo de contenido de video junto con prompts textuales, lo que es fundamental para el rol de "Auditor de Calidad Educativa".
*   **Output Estructurado (JSON)**: La `generation_config` se establece para forzar la respuesta en formato `application/json`, garantizando la consistencia y facilidad de parseo de los reportes.
*   **Dynamic Prompting para Videos Largos**: La función `generar_prompt_dinamico` permite a Gemini mantener un "contexto acumulado" de las partes anteriores del video. Esto asegura que el informe final sea coherente y global, fusionando los hallazgos de cada segmento en un único reporte unificado.
*   **Gestión de Tokens y Costos**: Se realiza un cálculo de tokens (`funcionalidad_gemini.count_tokens`) para prever el consumo. La segmentación de videos y la eliminación de archivos de la nube (`genai.delete_file`) son prácticas clave para optimizar los costos de la API.
*   **Manejo de Rate Limits**: Se implementa un mecanismo de reintentos con `time.sleep` para manejar errores `429` (Too Many Requests) o `Quota` de la API, mejorando la robustez del sistema en entornos de alta demanda.

### Generación de Reportes Estructurados (`pandas`, `xhtml2pdf`)

*   **`pandas` para CSV**: La conversión del JSON de Gemini a un `DataFrame` de `pandas` facilita la generación de archivos CSV, permitiendo un análisis tabular posterior en herramientas como Excel o Google Sheets. La lógica de unir listas con saltos de línea (`"\n".join(v)`) es clave para mantener la legibilidad en celdas CSV.
*   **`xhtml2pdf` para PDF**: A diferencia de `pdfkit` (que a menudo requiere `wkhtmltopdf` externo), `xhtml2pdf` (`pisa`) es una solución puramente Python para convertir HTML a PDF. Esto simplifica la implementación y reduce las dependencias a nivel de sistema operativo para la fase de generación de reportes.
*   **HTML Dinámico con Gemini**: La capacidad de Gemini para generar HTML a partir de un prompt y una plantilla CSS permite una personalización flexible y profesional de los reportes, sin necesidad de mantener plantillas HTML estáticas complejas. El prompt guía a Gemini para usar CSS básico y evitar frameworks modernos, asegurando compatibilidad con `xhtml2pdf`.

## 8. Consideraciones de Seguridad

*   **Credenciales**: Nunca se deben exponer las claves de API o credenciales de servicio directamente en el código fuente o en el repositorio. El uso de archivos `.env` y `credentials_module.json` gestionados localmente es una práctica de seguridad estándar.
*   **Acceso a Google Drive**: La cuenta de servicio debe tener los permisos mínimos necesarios para la operación (ej. solo lectura si no se requiere subir archivos).
*   **Datos Sensibles**: El sistema está diseñado para auditar contenido educativo. Asegúrese de que el contenido de los videos cumpla con las políticas de privacidad y uso de datos de su organización.