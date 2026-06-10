# 🚀 Sistema de Auditoría Automatizada de Contenido Educativo

Este repositorio alberga un sistema integral para la auditoría automatizada de contenido de video educativo, diseñado para optimizar los procesos de control de calidad en entornos de aprendizaje digital. Utilizando la inteligencia artificial de Google Gemini, integración con Google Drive y herramientas avanzadas de procesamiento de video, el sistema descarga, optimiza, analiza y genera informes detallados en formato PDF a partir de grabaciones de clases.

El objetivo principal es proporcionar una solución escalable y objetiva para evaluar la calidad pedagógica y técnica de las clases, permitiendo a las instituciones educativas identificar rápidamente áreas de mejora y estandarizar la excelencia académica.

## 🛡️ Badges

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![Google Drive](https://img.shields.io/badge/Google%20Drive-Integration-green?style=flat-square&logo=google-drive&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI%20Powered-orange?style=flat-square&logo=google-gemini&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Video%20Processing-lightgrey?style=flat-square&logo=ffmpeg&logoColor=white)
![MoviePy](https://img.shields.io/badge/MoviePy-Video%20Editing-purple?style=flat-square&logo=moviepy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white)
![PyDrive2](https://img.shields.io/badge/PyDrive2-Google%20Drive%20API-yellowgreen?style=flat-square&logo=google-drive&logoColor=white)
![XHTML2PDF](https://img.shields.io/badge/XHTML2PDF-PDF%20Generation-red?style=flat-square&logo=pdf&logoColor=white)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

## 📝 Índice

*   [Introducción](#-introducción)
*   [Arquitectura del Sistema](#-arquitectura-del-sistema)
*   [Características Principales](#-características-principales)
*   [Requisitos del Sistema](#-requisitos-del-sistema)
    *   [Dependencias de Sistema Operativo](#dependencias-de-sistema-operativo)
    *   [Dependencias de Python](#dependencias-de-python)
*   [Configuración del Proyecto](#-configuración-del-proyecto)
    *   [Configuración de Credenciales de Google Drive](#configuración-de-credenciales-de-google-drive)
    *   [Configuración de la API de Google Gemini](#configuración-de-la-api-de-google-gemini)
    *   [Variables de Entorno](#variables-de-entorno)
*   [Uso del Proyecto](#-uso-del-proyecto)
    *   [Flujo de Ejecución](#flujo-de-ejecución)
    *   [Ejecución del Script Principal (`main.py`)](#ejecución-del-script-principal-mainpy)
    *   [Generación de Informes HTML y PDF (`Create_html_to_PDF.py`)](#generación-de-informes-html-y-pdf-create_html_to_pdfpy)
*   [Estructura de Datos de Salida](#-estructura-de-datos-de-salida)
    *   [Ejemplo de Salida JSON](#ejemplo-de-salida-json)
    *   [Ejemplo de Salida CSV](#ejemplo-de-salida-csv)
*   [Análisis Técnico y Valor Agregado](#-análisis-técnico-y-valor-agregado)
    *   [Integración con Google Drive](#integración-con-google-drive)
    *   [Optimización de Video con FFmpeg y MoviePy](#optimización-de-video-con-ffmpeg-y-moviepy)
    *   [Auditoría de Contenido con Google Gemini](#auditoría-de-contenido-con-google-gemini)
    *   [Generación de Informes Profesionales](#generación-de-informes-profesionales)
*   [Impacto en el Negocio](#-impacto-en-el-negocio)
    *   [Preguntas de Negocio Abordadas](#preguntas-de-negocio-abordadas)
    *   [Valor Agregado](#valor-agregado)
    *   [Permite Medir](#permite-medir)
    *   [Permite Diagnosticar](#permite-diagnosticar)
    *   [Permite Resolver y Acotar](#permite-resolver-y-acotar)
    *   [Permite Optimizar](#permite-optimizar)
    *   [Permite Estandarizar](#permite-estandarizar)
    *   [Permite Repensar](#permite-repensar)
*   [Licencia](#-licencia)

---

## 💡 Introducción

Este proyecto automatiza el proceso de auditoría de videos de clases, transformando la supervisión manual en un flujo de trabajo eficiente y basado en IA. Desde la descarga de videos desde Google Drive hasta la generación de informes PDF estandarizados, el sistema garantiza una evaluación consistente y detallada de la calidad educativa. Es una herramienta esencial para instituciones que buscan escalar sus operaciones de control de calidad sin comprometer la profundidad del análisis.

## 🏗️ Arquitectura del Sistema

El sistema opera a través de un pipeline secuencial y modular, diseñado para procesar videos de clases y generar informes de auditoría completos.

**Pipeline General:**

1.  **Ingesta de Videos:** Los videos de clases son obtenidos desde una carpeta específica en Google Drive.
2.  **Descarga y Verificación:** Los videos se descargan localmente, con mecanismos de reintento y verificación de integridad.
3.  **Optimización de Video:** Los videos descargados se comprimen y aceleran para reducir el tamaño y el tiempo de procesamiento por la IA.
4.  **Auditoría con IA (Google Gemini):** El video optimizado (o sus segmentos) se envía a Google Gemini para un análisis profundo de su contenido pedagógico y técnico, generando un informe estructurado en formato JSON.
5.  **Persistencia de Datos:** El informe JSON se guarda localmente como archivo `.txt` y se convierte a `.csv` para facilitar el análisis de datos.
6.  **Estilización con IA (Google Gemini):** El informe JSON (`.txt`) se envía nuevamente a Google Gemini para ser transformado en un documento HTML profesional y estéticamente diseñado.
7.  **Generación de PDF:** El HTML generado se convierte a un archivo PDF final, listo para su distribución.

**Componentes Clave:**

*   **Módulo de Integración con Google Drive (`main.py`):** Gestiona la autenticación, listado y descarga de archivos de video.
*   **Módulo de Procesamiento de Video (`main.py`):** Emplea `MoviePy` y `FFmpeg` para la compresión, redimensionamiento, aceleración y, si es necesario, segmentación de videos.
*   **Módulo de Auditoría con IA (`main.py`):** Interactúa con la API de Google Gemini (`gemini-2.5-flash`) para analizar el contenido del video, utilizando prompts estructurados y manejo de contexto para videos largos.
*   **Módulo de Generación de Datos Estructurados (`main.py`):** Procesa la respuesta JSON de Gemini y la guarda en formatos `.txt` y `.csv`.
*   **Módulo de Generación de Informes Profesionales (`Create_html_to_PDF.py`):** Utiliza Google Gemini para estilizar el informe de texto en HTML y `xhtml2pdf` para la conversión final a PDF.

## ✨ Características Principales

*   **Automatización Completa:** Desde la descarga de videos hasta la generación de informes PDF, el proceso es totalmente automatizado.
*   **Integración Robusta con Google Drive:** Descarga segura y verificada de videos desde carpetas específicas.
*   **Optimización Inteligente de Video:** Compresión y aceleración de videos para reducir costos y tiempos de procesamiento de la IA, con un robusto sistema de fallback entre `MoviePy` y `FFmpeg`.
*   **Auditoría de Contenido Basada en IA:** Utiliza Google Gemini para un análisis profundo de la claridad del profesor, dominio del tema, uso de herramientas, participación y manejo del tiempo.
*   **Manejo de Videos Extensos:** Capacidad para segmentar videos largos y procesarlos iterativamente con la IA, manteniendo la coherencia del informe final mediante un mecanismo de contexto acumulado.
*   **Informes Estructurados y Accionables:** Genera informes en formato JSON y CSV, facilitando el análisis programático y la integración con otros sistemas.
*   **Generación de Informes Profesionales en PDF:** Transforma los datos de auditoría en documentos HTML estéticamente agradables y luego en PDFs listos para su presentación, con un diseño coherente y profesional.
*   **Manejo de Errores y Reintentos:** Incluye lógica para reintentar descargas fallidas y manejar límites de cuota de la API de Gemini.

## ⚙️ Requisitos del Sistema

### Dependencias de Sistema Operativo

*   **FFmpeg:** Es una herramienta fundamental para la manipulación de video. Se utiliza para la compresión, aceleración y segmentación de videos.
    *   **Instalación (Linux/macOS):**
        ```bash
        sudo apt update && sudo apt install ffmpeg # Debian/Ubuntu
        brew install ffmpeg # macOS (Homebrew)
        ```
    *   **Instalación (Windows):** Descargue el ejecutable desde el [sitio oficial de FFmpeg](https://ffmpeg.org/download.html) y asegúrese de que la ruta al ejecutable `ffmpeg.exe` esté incluida en la variable de entorno PATH de su sistema.

### Dependencias de Python

Se recomienda el uso de un entorno virtual para gestionar las dependencias.

```bash
pip install pandas gspread oauth2client pydrive2 python-dotenv moviepy imageio-ffmpeg google-generativeai xhtml2pdf
```

## 🛠️ Configuración del Proyecto

### Configuración de Credenciales de Google Drive

Este proyecto utiliza `pydrive2` para interactuar con Google Drive. Necesitará un archivo de credenciales para autenticarse.

1.  **Crear un Proyecto en Google Cloud Console:**
    *   Vaya a [Google Cloud Console](https://console.cloud.google.com/).
    *   Cree un nuevo proyecto o seleccione uno existente.
2.  **Habilitar la API de Google Drive:**
    *   En el menú de navegación, vaya a "APIs y servicios" > "Biblioteca".
    *   Busque "Google Drive API" y habilítela.
3.  **Crear Credenciales de OAuth 2.0 (ID de Cliente de Escritorio):**
    *   Vaya a "APIs y servicios" > "Credenciales".
    *   Haga clic en "Crear credenciales" > "ID de cliente de OAuth".
    *   Seleccione "Aplicación de escritorio" como tipo de aplicación.
    *   Asigne un nombre y haga clic en "Crear".
    *   Descargue el archivo JSON resultante.
4.  **Renombrar y Colocar el Archivo:**
    *   Renombre el archivo JSON descargado a `credentials_module.json`.
    *   Colóquelo en la raíz de su proyecto.

La primera vez que ejecute el script `main.py`, se abrirá una ventana del navegador para que autorice el acceso a su cuenta de Google Drive. Una vez autorizado, `pydrive2` guardará un token de acceso en `credentials_module.json` para futuras autenticaciones.

### Configuración de la API de Google Gemini

El proyecto requiere una clave de API para Google Gemini.

1.  **Obtener una Clave de API:**
    *   Visite [Google AI Studio](https://aistudio.google.com/app/apikey) o la consola de Google Cloud para generar una clave de API para Gemini.
2.  **Configurar la Variable de Entorno:**
    *   Cree un archivo `.env` en la raíz de su proyecto.
    *   Agregue su clave de API de Gemini de la siguiente manera:
        ```dotenv
        API_KEY_GEMINI_PRO_1.5="TU_CLAVE_API_DE_GEMINI"
        ```
    *   **Nota:** El nombre de la variable `API_KEY_GEMINI_PRO_1.5` es el que se espera en el código.

### Variables de Entorno

Además de la clave de API de Gemini, necesita especificar la carpeta de Google Drive de donde se descargarán los videos.

*   En el archivo `.env`, agregue la siguiente variable:
    ```dotenv
    carpeta_drive="ID_DE_LA_CARPETA_DE_GOOGLE_DRIVE"
    ```
    *   Para obtener el ID de una carpeta de Google Drive, abra la carpeta en su navegador. El ID es la parte de la URL después de `/folders/` (ej. `https://drive.google.com/drive/folders/ESTE_ES_EL_ID`).

## 🚀 Uso del Proyecto

### Flujo de Ejecución

El sistema está diseñado para ejecutarse en dos fases principales:

1.  **Fase de Auditoría y Generación de Datos (`main.py`):** Descarga videos, los procesa con IA y genera informes JSON/CSV.
2.  **Fase de Generación de Informes PDF (`Create_html_to_PDF.py`):** Toma los informes JSON generados y los convierte en documentos HTML estilizados y luego en PDFs.

### Ejecución del Script Principal (`main.py`)

Este script es el encargado de la auditoría de los videos.

1.  Asegúrese de que todas las [dependencias](#dependencias-de-python) estén instaladas y las [variables de entorno](#variables-de-entorno) configuradas.
2.  Ejecute el script desde la terminal:
    ```bash
    python main.py
    ```
3.  El script:
    *   Se autenticará con Google Drive.
    *   Listará y descargará los videos de la carpeta especificada.
    *   Optimizará cada video.
    *   Subirá el video (o sus partes) a Google Gemini para su auditoría.
    *   Generará un archivo `Reporte_Auditoria_NOMBRE_VIDEO.txt` (JSON) y `Reporte_Auditoria_NOMBRE_VIDEO.csv` por cada video auditado.
    *   Eliminará los archivos temporales de video.

### Generación de Informes HTML y PDF (`Create_html_to_PDF.py`)

Una vez que `main.py` ha generado los archivos `.txt` con los informes JSON, este script los transformará en informes PDF profesionales.

1.  Asegúrese de que la [API de Google Gemini](#configuración-de-la-api-de-google-gemini) esté configurada en su archivo `.env`.
2.  Ejecute el script desde la terminal:
    ```bash
    python Create_html_to_PDF.py
    ```
3.  El script:
    *   Buscará todos los archivos `Reporte_Auditoria_*.txt` en el directorio actual.
    *   Para cada archivo, lo subirá a Google Gemini.
    *   Solicitará a Gemini que convierta el contenido del informe en un código HTML estilizado, siguiendo las directrices de diseño predefinidas.
    *   Guardará el HTML generado como `Reporte_Auditoria_NOMBRE_VIDEO.html`.
    *   Convertirá el archivo HTML a `Reporte_Auditoria_NOMBRE_VIDEO.pdf` utilizando `xhtml2pdf`.
    *   Eliminará los archivos temporales de Gemini.

## 📊 Estructura de Datos de Salida

El proceso de auditoría genera datos estructurados en formato JSON, que luego se pueden exportar a CSV para un análisis tabular.

### Ejemplo de Salida JSON

El archivo `Reporte_Auditoria_NOMBRE_VIDEO.txt` contendrá un objeto JSON con la siguiente estructura:

```json
{
  "resumen_clase": "Descripción concisa de los temas cubiertos en la clase, incluyendo los puntos principales y el enfoque pedagógico.",
  "objetivo_alcanzado": "Sí - El objetivo de la lección fue claramente alcanzado, con una demostración efectiva de los conceptos clave.",
  "puntos_fuertes": [
    "Claridad excepcional en la explicación de conceptos complejos.",
    "Uso efectivo de ejemplos prácticos y analogías para facilitar la comprensión.",
    "Fomento activo de la participación estudiantil mediante preguntas abiertas.",
    "Excelente manejo de las herramientas digitales para la presentación de contenido."
  ],
  "oportunidades_mejora": [
    "Algunas transiciones entre temas fueron abruptas, afectando ligeramente el flujo.",
    "Podría integrar más actividades interactivas para reforzar el aprendizaje práctico.",
    "El ritmo en la sección final fue un poco acelerado, dejando menos tiempo para preguntas."
  ],
  "recomendaciones_accionables": [
    "Planificar transiciones más suaves entre los módulos temáticos.",
    "Incorporar un breve ejercicio práctico o un quiz al final de cada sección principal."
  ],
  "nivel_participacion": "Alta - Los alumnos interactuaron activamente, haciendo preguntas pertinentes y respondiendo a los planteamientos del profesor.",
  "manejo_del_tiempo": "Adecuado - El tiempo se distribuyó de manera equilibrada entre la exposición teórica, ejemplos y un espacio para preguntas, aunque el final fue un poco ajustado.",
  "herramientas_utilizadas": [
    "Presentación de diapositivas (Google Slides)",
    "Pizarrón virtual (Jamboard)",
    "Encuestas rápidas (Mentimeter)"
  ],
  "incidencias_notables": [
    "Breve interrupción de audio al inicio debido a un micrófono mal configurado (resuelto rápidamente)."
  ],
  "calificacion_pedagogica": 92,
  "calificacion_tecnica": 88,
  "comentario_final": "La clase demostró un alto nivel de preparación y ejecución pedagógica. Se recomienda un enfoque en la fluidez de las transiciones y la integración de más elementos interactivos para maximizar la retención del aprendizaje."
}
```

### Ejemplo de Salida CSV

El archivo `Reporte_Auditoria_NOMBRE_VIDEO.csv` presentará los datos del JSON en un formato tabular, con las listas concatenadas por saltos de línea para mantener la información en una sola celda.

```csv
resumen_clase,objetivo_alcanzado,puntos_fuertes,oportunidades_mejora,recomendaciones_accionables,nivel_participacion,manejo_del_tiempo,herramientas_utilizadas,incidencias_notables,calificacion_pedagogica,calificacion_tecnica,comentario_final
"Descripción concisa de los temas cubiertos en la clase, incluyendo los puntos principales y el enfoque pedagógico.","Sí - El objetivo de la lección fue claramente alcanzado, con una demostración efectiva de los conceptos clave.","Claridad excepcional en la explicación de conceptos complejos.\nUso efectivo de ejemplos prácticos y analogías para facilitar la comprensión.\nFomento activo de la participación estudiantil mediante preguntas abiertas.\nExcelente manejo de las herramientas digitales para la presentación de contenido.","Algunas transiciones entre temas fueron abruptas, afectando ligeramente el flujo.\nPodría integrar más actividades interactivas para reforzar el aprendizaje práctico.\nEl ritmo en la sección final fue un poco acelerado, dejando menos tiempo para preguntas.","Planificar transiciones más suaves entre los módulos temáticos.\nIncorporar un breve ejercicio práctico o un quiz al final de cada sección principal.","Alta - Los alumnos interactuaron activamente, haciendo preguntas pertinentes y respondiendo a los planteamientos del profesor.","Adecuado - El tiempo se distribuyó de manera equilibrada entre la exposición teórica, ejemplos y un espacio para preguntas, aunque el final fue un poco ajustado.","Presentación de diapositivas (Google Slides)\nPizarrón virtual (Jamboard)\nEncuestas rápidas (Mentimeter)","Breve interrupción de audio al inicio debido a un micrófono mal configurado (resuelto rápidamente).",92,88,"La clase demostró un alto nivel de preparación y ejecución pedagógica. Se recomienda un enfoque en la fluidez de las transiciones y la integración de más elementos interactivos para maximizar la retención del aprendizaje."
```

## 🔬 Análisis Técnico y Valor Agregado

Este proyecto integra diversas tecnologías para construir un pipeline de auditoría robusto y eficiente. La selección de cada herramienta se basa en su capacidad para aportar valor técnico y resolver desafíos específicos.

### Integración con Google Drive

*   **Tecnología:** `pydrive2`
*   **Valor Agregado:** `pydrive2` proporciona una interfaz Pythonic para la API de Google Drive, simplificando la autenticación (OAuth 2.0), la navegación de archivos y la descarga. La implementación incluye lógica de reintento y verificación del tamaño del archivo (`os.path.getsize` vs `archivo['fileSize']`) para asegurar descargas completas y fiables, mitigando problemas de red o de la API. Esto es crucial para garantizar que el material fuente para la auditoría sea íntegro.

### Optimización de Video con FFmpeg y MoviePy

La optimización de video es un paso crítico para reducir los costos y el tiempo de procesamiento de la IA, ya que los modelos de lenguaje multimodal consumen recursos en función de la duración y calidad del video.

*   **Tecnología:** `MoviePy` (con `imageio-ffmpeg` como backend) y `FFmpeg` (directamente vía `subprocess`).
*   **Valor Agregado:**
    *   **Reducción de Costos y Tiempo:** Al reducir la resolución (`height=240` o `scale=-2:360`), acelerar la reproducción (`MultiplySpeed, 1.5` o `setpts=0.666667*PTS, atempo=1.5`), y disminuir el `fps` (`0.5`), se minimiza la cantidad de datos que la IA debe procesar, optimizando el consumo de tokens y el tiempo de respuesta.
    *   **MoviePy:** Ofrece una abstracción de alto nivel para la edición de video, facilitando operaciones como redimensionamiento y cambio de velocidad con una sintaxis intuitiva. Es útil para prototipado rápido.
    *   **FFmpeg (Directo):** La implementación de `subprocess.run` con `FFmpeg` es un mecanismo de *fallback* robusto. `FFmpeg` es el estándar de la industria para el procesamiento de medios, conocido por su eficiencia y control granular. Cuando `MoviePy` (que a veces puede ser menos estable o más lento para ciertas operaciones) falla, la llamada directa a `FFmpeg` garantiza que la optimización se complete de manera fiable. Los parámetros como `-filter_complex`, `-preset ultrafast`, `-b:a 32k`, y `-ac 1` están ajustados para una compresión máxima con una calidad suficiente para el análisis de contenido (no para visualización de alta fidelidad).
    *   **Segmentación de Videos Largos:** Para videos que exceden los límites de tokens de Gemini, `FFmpeg` se utiliza para segmentar el video en partes más pequeñas (`-segment_time 1500` para 25 minutos por segmento). Esto permite procesar videos de cualquier duración, superando las limitaciones de la API.

### Auditoría de Contenido con Google Gemini

El corazón del sistema reside en la capacidad de la IA para analizar el contenido pedagógico y técnico de las clases.

*   **Tecnología:** `google.generativeai` con el modelo `gemini-2.5-flash`.
*   **Valor Agregado:**
    *   **Análisis Multimodal Avanzado:** `gemini-2.5-flash` es un modelo multimodal optimizado para velocidad y eficiencia, ideal para procesar videos y extraer información relevante sobre la dinámica de la clase.
    *   **Prompts Estructurados y `system_instruction`:** La definición de un `system_instruction` (`Eres un Auditor de Calidad Educativa...`) y un `prompt_final` detallado que exige una salida JSON específica, asegura que la IA se adhiera a un rol y formato predefinidos. Esto es crucial para la consistencia y la parseabilidad de los informes.
    *   **Manejo de Contexto para Videos Segmentados (RAG-like):** La función `generar_prompt_dinamico` implementa un mecanismo de "memoria" o contexto acumulado. Para videos segmentados, el informe JSON generado por un fragmento anterior se alimenta de nuevo a la IA como `contexto_anterior` para el siguiente fragmento. Esto permite a Gemini construir un informe unificado y coherente a lo largo de todo el video, superando las limitaciones de la ventana de contexto de la API para entradas muy largas.
    *   **Manejo de Rate Limits:** La lógica de reintento con `time.sleep(30)` para errores `429` (Quota Exceeded) garantiza la robustez del proceso frente a las limitaciones de la API, evitando fallos en la auditoría de videos extensos o en lotes.
    *   **Métricas Cuantitativas y Cualitativas:** La estructura JSON solicita calificaciones numéricas (`calificacion_pedagogica`, `calificacion_tecnica`) junto con descripciones cualitativas detalladas, proporcionando una visión holística.

### Generación de Informes Profesionales

La presentación de los resultados es tan importante como el análisis en sí.

*   **Tecnología:** `google.generativeai` (para HTML) y `xhtml2pdf` (para PDF).
*   **Valor Agregado:**
    *   **Estilización con IA:** Utilizar Gemini para convertir el JSON en HTML (`PROMPT` en `Create_html_to_PDF.py`) permite una generación dinámica de informes con un diseño profesional y estético, sin necesidad de plantillas HTML estáticas complejas. La estricta directriz de **no usar flexbox, CSS grid, ni variables :root** en el prompt asegura la compatibilidad con `xhtml2pdf` y evita complejidades de renderizado que podrían surgir con CSS moderno.
    *   **Consistencia de Marca:** La `Plantilla_HTML` (CSS) incrustada en el prompt guía a Gemini para usar colores y fuentes específicos (`Tahoma`, paleta naranja), asegurando que los informes finales se alineen con la identidad visual de la compañía.
    *   **Generación de PDF Robusta:** `xhtml2pdf` (`pisa.CreatePDF`) es una biblioteca Python fiable para convertir HTML y CSS a PDF. A diferencia de `pdfkit` (que a menudo requiere `wkhtmltopdf` como dependencia externa de SO), `xhtml2pdf` es una solución más autocontenida en Python, lo que simplifica la implementación y el despliegue. Produce documentos PDF de alta calidad, listos para su distribución o archivo.

## 📈 Impacto en el Negocio

Este sistema de auditoría automatizada de contenido educativo no es solo una herramienta técnica, sino una palanca estratégica para la mejora continua y la eficiencia operativa en instituciones educativas.

### Preguntas de Negocio Abordadas

*   ¿Cómo podemos asegurar una calidad de enseñanza consistente en todas nuestras clases grabadas?
*   ¿Qué puntos específicos necesitan mejorar nuestros instructores para optimizar la experiencia de aprendizaje?
*   ¿Es posible escalar nuestro proceso de control de calidad sin incurrir en costos prohibitivos de personal?
*   ¿Estamos aprovechando al máximo las herramientas digitales en nuestras clases?
*   ¿Cómo podemos obtener retroalimentación objetiva y estandarizada sobre el desempeño docente?

### Valor Agregado

El sistema proporciona un valor agregado significativo al transformar un proceso manual, subjetivo y lento en uno automatizado, objetivo y escalable. Libera a los auditores humanos para que se concentren en tareas de mayor valor estratégico, como el desarrollo de programas de capacitación o la mentoría individualizada, en lugar de la revisión rutinaria de videos. La consistencia en la evaluación y la rapidez en la entrega de informes permiten una toma de decisiones ágil y basada en datos.

### Permite Medir

*   **Calidad Pedagógica y Técnica:** Cuantifica el desempeño del instructor con calificaciones numéricas (0-100), complementadas con descripciones cualitativas.
*   **Nivel de Participación:** Evalúa la interacción de los alumnos (Alta/Media/Baja) y describe su dinámica.
*   **Manejo del Tiempo:** Mide la eficiencia en la distribución del tiempo de la clase.
*   **Uso de Herramientas:** Registra las herramientas digitales utilizadas, permitiendo un seguimiento de la adopción tecnológica.
*   **Incidencias:** Identifica y registra problemas técnicos o interrupciones, cuantificando su frecuencia y tipo.
*   **Puntos Fuertes y Oportunidades:** Proporciona listas estructuradas de aciertos y áreas de mejora, facilitando el análisis de tendencias.

### Permite Diagnosticar

*   **Debilidades Específicas del Instructor:** Identifica patrones de fallos (ej. "muletillas", explicaciones confusas, falta de interacción) que requieren atención.
*   **Ineficiencias Metodológicas:** Diagnostica si ciertas metodologías no están siendo efectivas o si el ritmo de la clase es inadecuado.
*   **Problemas Técnicos Recurrentes:** Señala incidencias como fallas de conexión o problemas de audio, que pueden indicar necesidades de infraestructura o capacitación técnica.
*   **Brechas en la Adopción Tecnológica:** Revela si las herramientas digitales no se están utilizando o si su uso es subóptimo.
*   **Necesidades de Capacitación:** Agrega datos para identificar áreas comunes de mejora en el cuerpo docente, informando el diseño de programas de desarrollo profesional.

### Permite Resolver y Acotar

*   **Recomendaciones Accionables:** Proporciona sugerencias concretas y directas para que los profesores mejoren en su próxima clase.
*   **Foco en la Mejora:** Permite a los directores académicos acotar las áreas de mejora para cada instructor, haciendo la retroalimentación más efectiva y menos abrumadora.
*   **Intervención Temprana:** Al identificar rápidamente problemas, se pueden implementar soluciones antes de que afecten a un gran número de estudiantes.
*   **Optimización de Recursos:** Dirige los recursos de capacitación y soporte técnico hacia donde son más necesarios.

### Permite Optimizar

*   **Proceso de QA:** Reduce drásticamente el tiempo y el costo asociados con la auditoría manual de videos.
*   **Desarrollo Docente:** Optimiza la efectividad de los programas de capacitación al basarlos en datos reales y necesidades identificadas.
*   **Experiencia del Estudiante:** Mejora indirectamente la calidad de la enseñanza, lo que se traduce en una mejor experiencia de aprendizaje y mayores tasas de retención.
*   **Uso de Ancho de Banda y Almacenamiento:** La compresión de videos para la IA optimiza el uso de recursos de red y almacenamiento en la nube.
*   **Escalabilidad:** Permite auditar un volumen masivo de clases sin un aumento lineal en el personal de QA.

### Permite Estandarizar

*   **Criterios de Evaluación:** Establece un conjunto uniforme y objetivo de criterios de evaluación aplicados por la IA, eliminando la subjetividad humana.
*   **Formato de Informes:** Genera informes estandarizados en JSON, CSV y PDF, facilitando la comparación, el archivo y la integración con sistemas de gestión académica.
*   **Nivel de Calidad:** Define un umbral de calidad consistente para todas las clases, asegurando que se cumplan los estándares institucionales.
*   **Procesos Internos:** Estandariza el flujo de trabajo de control de calidad, desde la ingesta de videos hasta la entrega de informes.

### Permite Repensar

*   **Estrategias Pedagógicas Institucionales:** Los datos agregados pueden revelar la necesidad de repensar y adaptar las metodologías de enseñanza a nivel institucional, promoviendo enfoques más efectivos y participativos.
*   **Diseño Curricular:** Si los informes muestran consistentemente dificultades en ciertos temas o la falta de uso de herramientas específicas, puede llevar a una revisión del diseño de los cursos.
*   **Programas de Formación Docente:** Permite rediseñar los programas de desarrollo profesional para abordar las competencias más críticas y las deficiencias comunes identificadas por la IA.
*   **Infraestructura Tecnológica:** La recurrencia de incidencias técnicas puede impulsar una reevaluación y mejora de la infraestructura de red, plataformas LMS o equipos de grabación.
*   **Modelo de Evaluación de Desempeño:** El sistema puede integrar nuevas métricas o ajustar las existentes, permitiendo una evolución continua del modelo de evaluación docente.
*   **Innovación en el Aula:** Al liberar tiempo de los equipos de QA y proporcionar insights claros, se fomenta la experimentación con nuevas herramientas y enfoques pedagógicos, sabiendo que su impacto será medido y reportado.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo `LICENSE` para obtener más detalles.