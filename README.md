# Sistema Automatizado de Auditoría de Clases y Generación de Informes

Este repositorio contiene un sistema automatizado diseñado para la auditoría de contenido de video educativo y la generación de informes detallados. El flujo de trabajo abarca desde la descarga y optimización de videos alojados en Google Drive, su análisis mediante inteligencia artificial (IA) para evaluar aspectos pedagógicos y técnicos, hasta la creación de informes estructurados en formatos JSON, CSV y PDF profesionalmente estilizados.

## Descripción General

El proyecto se compone de dos módulos principales: `main.py` y `Create_html_to_PDF.py`. `main.py` orquesta el proceso de adquisición, preprocesamiento, análisis con IA y generación de informes de texto/CSV. `Create_html_to_PDF.py` toma estos informes de texto y los transforma en documentos HTML estilizados, que luego son convertidos a PDF para una presentación final. Este sistema está optimizado para manejar videos de diversas duraciones, incluyendo aquellos que exceden los límites de procesamiento de la API de IA, mediante una estrategia de segmentación inteligente.

## Arquitectura del Sistema

La arquitectura del sistema se puede describir en las siguientes fases:

1.  **Origen de Datos:** Videos de clases almacenados en una carpeta específica de Google Drive.
2.  **Módulo de Procesamiento (`main.py`):**
    *   **Autenticación y Descarga:** Conexión a Google Drive para listar y descargar videos. Incluye mecanismos de reintento y verificación de integridad de descarga.
    *   **Optimización de Video:** Compresión y aceleración de los videos descargados para reducir el tamaño y la duración, optimizando el consumo de tokens de la API de IA. Se utiliza una estrategia dual (MoviePy y FFmpeg) para robustez.
    *   **Análisis con IA:** Carga de videos optimizados a la API de Google Gemini (modelo `gemini-2.5-flash`). Se utiliza un `system_instruction` y un `prompt` detallado para guiar a la IA en la generación de un informe de auditoría estructurado en formato JSON.
    *   **Manejo de Videos Extensos:** Para videos que superan el límite de tokens de la API, se implementa una segmentación automática mediante FFmpeg. Cada segmento es analizado iterativamente, y la IA mantiene un "contexto acumulado" para generar un informe unificado y coherente.
    *   **Generación de Salida Intermedia:** Los resultados de la auditoría se guardan como archivos `.txt` (JSON en texto plano) y `.csv`.
    *   **Limpieza:** Eliminación de archivos temporales de video y de los archivos subidos a la API de Gemini.
3.  **Módulo de Generación de Informes Finales (`Create_html_to_PDF.py`):**
    *   **Lectura de Informes:** Identificación de los archivos `.txt` generados por `main.py`.
    *   **Transformación a HTML con IA:** Utilización de la API de Google Gemini para convertir el contenido del informe de texto en un documento HTML con un estilo predefinido (CSS en línea, paleta de colores corporativa, estructura profesional).
    *   **Conversión a PDF:** Los archivos HTML generados son convertidos a documentos PDF utilizando `xhtml2pdf`, asegurando una presentación final consistente y profesional.
    *   **Limpieza:** Eliminación de los archivos subidos a la API de Gemini.

## Características Principales

*   **Automatización Completa:** Desde la descarga de videos hasta la generación de informes PDF.
*   **Optimización de Recursos:** Compresión y aceleración de videos para minimizar el tiempo de procesamiento y el costo de la API de IA.
*   **Auditoría Inteligente:** Análisis detallado de contenido de video mediante el modelo `gemini-2.5-flash` de Google, enfocado en métricas pedagógicas y técnicas.
*   **Escalabilidad:** Capacidad para procesar videos de larga duración mediante segmentación automática y análisis iterativo con mantenimiento de contexto.
*   **Informes Estructurados:** Generación de resultados en formatos JSON, CSV y PDF, facilitando la integración y el análisis posterior.
*   **Estilización Profesional:** Informes PDF con un diseño coherente y una paleta de colores corporativa, listos para su presentación.
*   **Manejo de Errores:** Mecanismos de reintento para descargas y llamadas a la API, incluyendo gestión de límites de cuota (rate limits).

## Tecnologías Utilizadas

*   **Lenguaje de Programación:** Python 3.x
*   **APIs y Librerías Principales:**
    *   `google.generativeai`: Interacción con la API de Google Gemini para análisis de video y generación de HTML.
    *   `pydrive2`, `oauth2client`: Autenticación y gestión de archivos en Google Drive.
    *   `moviepy`: Edición y compresión de video (como primera opción).
    *   `subprocess`, `imageio_ffmpeg`: Ejecución directa de FFmpeg para compresión avanzada y segmentación de video (como fallback y para videos grandes).
    *   `pandas`: Manipulación y exportación de datos a formato CSV.
    *   `dotenv`: Gestión de variables de entorno para credenciales y configuraciones sensibles.
    *   `json`: Procesamiento de datos en formato JSON.
    *   `xhtml2pdf` (con `pisa`): Conversión de HTML a PDF.
    *   `os`, `glob`, `time`, `datetime`: Operaciones de sistema de archivos, gestión de rutas, control de tiempo.

## Configuración del Entorno

Para ejecutar este proyecto, siga los siguientes pasos:

1.  **Clonar el Repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2.  **Crear un Entorno Virtual (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # venv\Scripts\activate   # En Windows
    ```

3.  **Instalar Dependencias:**
    Se recomienda crear un archivo `requirements.txt` con las siguientes dependencias:
    ```
    google-generativeai
    python-dotenv
    pydrive2
    oauth2client
    moviepy
    imageio-ffmpeg
    pandas
    xhtml2pdf
    ```
    Luego, instálelas:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar Variables de Entorno:**
    Cree un archivo `.env` en la raíz del proyecto con las siguientes variables:
    ```
    API_KEY_GEMINI_PRO_1.5="TU_API_KEY_DE_GEMINI"
    carpeta_drive="ID_DE_LA_CARPETA_DE_GOOGLE_DRIVE"
    ```
    *   `API_KEY_GEMINI_PRO_1.5`: Obtenga su clave API de Google AI Studio.
    *   `carpeta_drive`: El ID de la carpeta de Google Drive donde se encuentran los videos a auditar. Puede encontrarlo en la URL de la carpeta de Drive.

5.  **Configurar Credenciales de Google Drive:**
    Este proyecto utiliza `pydrive2` para interactuar con Google Drive. Necesitará un archivo `credentials_module.json`.
    *   Vaya a la [Consola de Desarrolladores de Google Cloud](https://console.cloud.google.com/).
    *   Cree un nuevo proyecto o seleccione uno existente.
    *   Habilite la "Google Drive API".
    *   Vaya a "Credenciales" y cree nuevas credenciales de "ID de cliente de OAuth".
    *   Seleccione "Aplicación de escritorio" como tipo de aplicación.
    *   Descargue el archivo JSON de las credenciales y renómbrelo a `credentials_module.json`. Colóquelo en la raíz del proyecto.
    *   **IMPORTANTE:** Este archivo contiene información sensible. **NO LO SUBAS A UN REPOSITORIO PÚBLICO.**

## Uso

El flujo de trabajo se ejecuta en dos fases secuenciales:

1.  **Ejecutar el Módulo de Auditoría y Generación de Informes (TXT/CSV):**
    ```bash
    python main.py
    ```
    Este script descargará, optimizará, auditará los videos y generará los archivos `Reporte_Auditoria_*.txt` y `Reporte_Auditoria_*.csv` en la raíz del proyecto.

2.  **Ejecutar el Módulo de Conversión a PDF:**
    ```bash
    python Create_html_to_PDF.py
    ```
    Este script leerá los archivos `.txt` generados, los convertirá a HTML estilizado usando la IA, y finalmente generará los archivos `Reporte_Auditoria_*.pdf` en la raíz del proyecto.

## Estructura del Proyecto

```
.
├── main.py
├── Create_html_to_PDF.py
├── .env
├── credentials_module.json
├── requirements.txt
├── Reporte_Auditoria_NombreVideo.txt  # Salida de main.py
├── Reporte_Auditoria_NombreVideo.csv  # Salida de main.py
├── Reporte_Auditoria_NombreVideo.html # Intermedio de Create_html_to_PDF.py
├── Reporte_Auditoria_NombreVideo.pdf  # Salida final de Create_html_to_PDF.py
├── video_clase_temporal.mp4           # Archivo temporal de descarga
├── clase_optimizada.mp4               # Archivo temporal optimizado
└── clase_optimizada_parte_XXX.mp4     # Archivos temporales de segmentos (si aplica)
```

## Lógica Principal

### `main.py`: Orquestación de Auditoría

1.  **Autenticación y Descarga de Google Drive:**
    La función `login()` utiliza `pydrive2` y `oauth2client` para autenticarse con Google Drive. Se carga el archivo `credentials_module.json` y se gestiona la expiración y refresco del token de acceso.
    Se itera sobre los archivos en la `carpeta_drive` definida en `.env`. Cada video se descarga con un mecanismo de reintento (`max_intentos`) y verificación de tamaño (`os.path.getsize`) para asegurar la integridad de la descarga.

2.  **Compresión y Optimización de Video:**
    Se implementa una estrategia de compresión dual para garantizar la robustez y eficiencia:
    *   **`compresion_optimizacion(video_original, video_optimizado)` (MoviePy):** Intenta comprimir y acelerar el video utilizando `moviepy`. Reduce la altura a 240p y acelera la reproducción 1.5 veces (`MultiplySpeed`). Los parámetros de `write_videofile` están ajustados para una compresión agresiva (preset `ultrafast`, `fps=0.5`, `audio_bitrate='32k'`, `ac=1`).
    *   **`compresion_directa(clase_original, clase_optimizada)` (FFmpeg):** Si MoviePy falla, se utiliza `subprocess` para ejecutar FFmpeg directamente. El comando FFmpeg aplica filtros complejos (`-filter_complex`) para acelerar el video (`setpts=0.666667*PTS` para 1.5x velocidad), escalar a 360p (`scale=-2:360`), reducir FPS (`fps=0.5`), y ajustar el audio (`atempo=1.5`, `-b:a 32k`, `-ac 1`). FFmpeg es generalmente más rápido y eficiente para estas tareas.
    La compresión es crucial para reducir el tamaño del video, lo que se traduce en un menor consumo de tokens y un procesamiento más rápido por parte de la API de Gemini.

3.  **Auditoría con Google Gemini:**
    *   **Configuración de la API:** Se carga la `API_KEY_GEMINI_PRO_1.5` desde `.env` y se configura `genai`. Se utiliza el modelo `gemini-2.5-flash` por su equilibrio entre rendimiento y costo.
    *   **Carga de Video:** El video optimizado (`clase_optimizada.mp4`) se sube a la API de Gemini (`genai.upload_file`). Se implementa un bucle de espera (`while archivo_clase.state.name == "PROCESSING"`) para monitorear el estado de procesamiento del archivo en la nube.
    *   **Instrucciones y Prompt:**
        *   `system_instruction`: Define el rol de la IA como "Auditor de Calidad Educativa", enfocándose en métricas clave.
        *   `generation_config`: Establece `temperature=0.1` para respuestas más determinísticas y `response_mime_type="application/json"` para asegurar la salida estructurada.
        *   `prompt_final`: Un prompt detallado que solicita un informe de auditoría estricto en formato JSON, especificando cada campo y su contenido esperado (resumen, puntos fuertes, oportunidades de mejora, calificaciones, etc.).
    *   **Manejo de Videos Extensos (Segmentación):**
        Si el `total_tokens` estimado para el video excede 1,000,000 (un umbral de seguridad para evitar errores de API o costos excesivos), el video se segmenta.
        *   `comando_parseo` (FFmpeg): Divide el video en partes de 1500 segundos (25 minutos) utilizando `-segment_time`.
        *   **Auditoría Iterativa:** Se procesa cada segmento individualmente. La función `generar_prompt_dinamico` crea un prompt que incluye el `contexto_acumulado` del informe de las partes anteriores. Esto permite a la IA mantener la coherencia y fusionar los hallazgos en un informe global.
        *   **Manejo de Rate Limits:** Se implementa un bucle de reintento (`limite_intentos_ragelimit_api`) con `time.sleep(30)` para gestionar errores `429` (Too Many Requests) de la API.
    *   **Salida y Limpieza:** El informe final (JSON) se guarda como `.txt` y se convierte a un `pandas.DataFrame` para exportarlo a `.csv`. Todos los archivos temporales de video (original, optimizado, segmentos) y los archivos subidos a Gemini se eliminan para liberar espacio y asegurar la privacidad.

### `Create_html_to_PDF.py`: Generación de Informes PDF

1.  **Lectura de Informes de Auditoría:**
    `glob.glob("Reporte_Auditoria_*.txt")` se utiliza para encontrar todos los archivos de informe generados por `main.py`.

2.  **Generación de HTML con Google Gemini:**
    *   **Configuración de la API:** Similar a `main.py`, se configura `genai` con la clave API.
    *   **Plantilla CSS:** Se define una `Plantilla_HTML` con CSS básico para el estilo del informe (fuente Tahoma, colores naranjas, estructura con divs y tablas). Esto sirve como base estilística para la IA.
    *   **Prompt para HTML:** Un `PROMPT` específico instruye a la IA para convertir el contenido del archivo `.txt` en un HTML "muy bonito y profesional". Se imponen reglas estrictas:
        *   Uso exclusivo de CSS básico en línea o en `<style>`.
        *   **Prohibición explícita de `flexbox`, `CSS grid`, y variables `:root`** para asegurar compatibilidad con `xhtml2pdf` y evitar complejidad innecesaria.
        *   Énfasis en el uso de tablas o divs con márgenes para la estructura.
        *   Requerimiento de una paleta de colores alrededor del naranja y un `disclaimer` de copyright.
    *   **Procesamiento:** El archivo `.txt` se sube a Gemini, y la IA genera el código HTML.
    *   **Guardado de HTML:** El HTML generado se guarda en un archivo `.html` intermedio.

3.  **Conversión de HTML a PDF:**
    *   `xhtml2pdf.pisa.CreatePDF()` es la función central para esta conversión. Toma el archivo HTML (`archivo_html_final`) y lo convierte a un archivo PDF (`archivo_pdf_final`). Esta librería es robusta para convertir HTML con CSS básico a PDF.

4.  **Limpieza:** Los archivos de texto subidos a la API de Gemini son eliminados.

## Valor Agregado

Este sistema ofrece un valor significativo sobre soluciones manuales o menos integradas:

*   **Eficiencia Operacional:** Automatiza un proceso que de otro modo sería intensivo en mano de obra, liberando recursos para tareas de mayor valor.
*   **Consistencia y Estandarización:** Garantiza que todos los informes de auditoría sigan una estructura y un estilo uniformes, facilitando la comparación y el análisis.
*   **Análisis Profundo con IA:** Aprovecha las capacidades avanzadas de los modelos multimodales de Google Gemini para extraer insights cualitativos y cuantitativos de los videos, algo inviable con métodos tradicionales.
*   **Escalabilidad Robusta:** La capacidad de segmentar videos grandes y procesarlos iterativamente permite auditar colecciones extensas de contenido sin preocuparse por los límites de la API.
*   **Presentación Profesional:** Los informes PDF generados son visualmente atractivos y listos para ser compartidos con stakeholders, mejorando la percepción de calidad y profesionalismo.
*   **Reducción de Costos:** La optimización de video antes de la auditoría con IA minimiza el consumo de tokens, lo que se traduce en una reducción directa de los costos operativos de la API.
*   **Flexibilidad Tecnológica:** La implementación de una estrategia dual para la compresión de video (MoviePy/FFmpeg) asegura la robustez del proceso frente a posibles fallos de una de las herramientas.

## Consideraciones de Seguridad

*   **Variables de Entorno:** Las claves API y los IDs de carpetas se gestionan a través de un archivo `.env`, que debe ser excluido del control de versiones (`.gitignore`).
*   **Credenciales de Google Drive:** El archivo `credentials_module.json` es sensible y **nunca debe ser subido a un repositorio público**.
*   **Limpieza de Datos:** El sistema elimina proactivamente los archivos temporales de video y los archivos subidos a la API de Gemini una vez que han sido procesados, minimizando la exposición de datos.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulte el archivo `LICENSE` para más detalles.