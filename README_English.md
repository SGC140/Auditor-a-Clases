# 🚀 Automated Educational Content Auditing System

This repository hosts a comprehensive system for automated auditing of educational video content, designed to optimize quality control processes in digital learning environments. Utilizing Google Gemini's artificial intelligence, Google Drive integration, and advanced video processing tools, the system downloads, optimizes, analyzes, and generates detailed PDF reports from class recordings.

The main objective is to provide a scalable and objective solution for evaluating the pedagogical and technical quality of classes, enabling educational institutions to quickly identify areas for improvement and standardize academic excellence.

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

## 📝 Table of Contents

*   [💡 Introduction](#-introduction)
*   [🏗️ System Architecture](#-system-architecture)
*   [✨ Key Features](#-key-features)
*   [⚙️ System Requirements](#-system-requirements)
    *   [Operating System Dependencies](#operating-system-dependencies)
    *   [Python Dependencies](#python-dependencies)
*   [🛠️ Project Setup](#-project-setup)
    *   [Google Drive Credentials Setup](#google-drive-credentials-setup)
    *   [Google Gemini API Setup](#google-gemini-api-setup)
    *   [Environment Variables](#environment-variables)
*   [🚀 Project Usage](#-project-usage)
    *   [Execution Flow](#execution-flow)
    *   [Running the Main Script (`main.py`)](#running-the-main-script-mainpy)
    *   [Generating HTML and PDF Reports (`Create_html_to_PDF.py`)](#generating-html-and-pdf-reports-create_html_to_pdfpy)
*   [📊 Output Data Structure](#-output-data-structure)
    *   [JSON Output Example](#json-output-example)
    *   [CSV Output Example](#csv-output-example)
*   [🔬 Technical Analysis and Added Value](#-technical-analysis-and-added-value)
    *   [Google Drive Integration](#google-drive-integration)
    *   [Video Optimization with FFmpeg and MoviePy](#video-optimization-with-ffmpeg-and-moviepy)
    *   [Content Auditing with Google Gemini](#content-auditing-with-google-gemini)
    *   [Professional Report Generation](#professional-report-generation)
*   [📈 Business Impact](#-business-impact)
    *   [Business Questions Addressed](#business-questions-addressed)
    *   [Added Value](#added-value)
    *   [Enables Measurement](#enables-measurement)
    *   [Enables Diagnosis](#enables-diagnosis)
    *   [Enables Resolution and Scoping](#enables-resolution-and-scoping)
    *   [Enables Optimization](#enables-optimization)
    *   [Enables Standardization](#enables-standardization)
    *   [Enables Rethinking](#enables-rethinking)
*   [📄 License](#-license)

---

## 💡 Introduction

This project automates the class video auditing process, transforming manual supervision into an efficient, AI-driven workflow. From downloading videos from Google Drive to generating standardized PDF reports, the system ensures consistent and detailed evaluation of educational quality. It is an essential tool for institutions looking to scale their quality control operations without compromising the depth of analysis.

## 🏗️ System Architecture

The system operates through a sequential and modular pipeline, designed to process class videos and generate comprehensive audit reports.

**General Pipeline:**

1.  **Video Ingestion:** Class videos are obtained from a specific folder in Google Drive.
2.  **Download and Verification:** Videos are downloaded locally, with retry mechanisms and integrity verification.
3.  **Video Optimization:** Downloaded videos are compressed and accelerated to reduce size and AI processing time.
4.  **AI Auditing (Google Gemini):** The optimized video (or its segments) is sent to Google Gemini for a deep analysis of its pedagogical and technical content, generating a structured report in JSON format.
5.  **Data Persistence:** The JSON report is saved locally as a `.txt` file and converted to `.csv` for easier data analysis.
6.  **AI Styling (Google Gemini):** The JSON report (`.txt`) is sent back to Google Gemini to be transformed into a professional and aesthetically designed HTML document.
7.  **PDF Generation:** The generated HTML is converted into a final PDF file, ready for distribution.

**Key Components:**

*   **Google Drive Integration Module (`main.py`):** Manages authentication, listing, and downloading of video files.
*   **Video Processing Module (`main.py`):** Employs `MoviePy` and `FFmpeg` for compression, resizing, acceleration, and, if necessary, video segmentation.
*   **AI Auditing Module (`main.py`):** Interacts with the Google Gemini API (`gemini-2.5-flash`) to analyze video content, using structured prompts and context handling for long videos.
*   **Structured Data Generation Module (`main.py`):** Processes Gemini's JSON response and saves it in `.txt` and `.csv` formats.
*   **Professional Report Generation Module (`Create_html_to_PDF.py`):** Uses Google Gemini to style the text report into HTML and `xhtml2pdf` for the final PDF conversion.

## ✨ Key Features

*   **Complete Automation:** From video download to PDF report generation, the process is fully automated.
*   **Robust Google Drive Integration:** Secure and verified downloading of videos from specific folders.
*   **Intelligent Video Optimization:** Compression and acceleration of videos to reduce AI processing costs and times, with a robust fallback system between `MoviePy` and `FFmpeg`.
*   **AI-Powered Content Auditing:** Uses Google Gemini for in-depth analysis of instructor clarity, subject mastery, tool usage, engagement, and time management.
*   **Handling of Extensive Videos:** Ability to segment long videos and process them iteratively with AI, maintaining the consistency of the final report through an accumulated context mechanism.
*   **Structured and Actionable Reports:** Generates reports in JSON and CSV formats, facilitating programmatic analysis and integration with other systems.
*   **Professional PDF Report Generation:** Transforms audit data into aesthetically pleasing HTML documents and then into presentation-ready PDFs, with a coherent and professional design.
*   **Error Handling and Retries:** Includes logic to retry failed downloads and handle Gemini API quota limits.

## ⚙️ System Requirements

### Operating System Dependencies

*   **FFmpeg:** This is a fundamental tool for video manipulation. It is used for video compression, acceleration, and segmentation.
    *   **Installation (Linux/macOS):**
        ```bash
        sudo apt update && sudo apt install ffmpeg # Debian/Ubuntu
        brew install ffmpeg # macOS (Homebrew)
        ```
    *   **Installation (Windows):** Download the executable from the [official FFmpeg website](https://ffmpeg.org/download.html) and ensure that the path to the `ffmpeg.exe` executable is included in your system's PATH environment variable.

### Python Dependencies

It is recommended to use a virtual environment to manage dependencies.

```bash
pip install pandas gspread oauth2client pydrive2 python-dotenv moviepy imageio-ffmpeg google-generativeai xhtml2pdf
```

## 🛠️ Project Setup

### Google Drive Credentials Setup

This project uses `pydrive2` to interact with Google Drive. You will need a credentials file for authentication.

1.  **Create a Project in Google Cloud Console:**
    *   Go to [Google Cloud Console](https://console.cloud.google.com/).
    *   Create a new project or select an existing one.
2.  **Enable the Google Drive API:**
    *   In the navigation menu, go to "APIs & Services" > "Library".
    *   Search for "Google Drive API" and enable it.
3.  **Create OAuth 2.0 Credentials (Desktop Client ID):**
    *   Go to "APIs & Services" > "Credentials".
    *   Click "Create credentials" > "OAuth client ID".
    *   Select "Desktop app" as the application type.
    *   Assign a name and click "Create".
    *   Download the resulting JSON file.
4.  **Rename and Place the File:**
    *   Rename the downloaded JSON file to `credentials_module.json`.
    *   Place it in the root of your project.

The first time you run the `main.py` script, a browser window will open for you to authorize access to your Google Drive account. Once authorized, `pydrive2` will save an access token in `credentials_module.json` for future authentications.

### Google Gemini API Setup

The project requires an API key for Google Gemini.

1.  **Obtain an API Key:**
    *   Visit [Google AI Studio](https://aistudio.google.com/app/apikey) or the Google Cloud console to generate an API key for Gemini.
2.  **Configure the Environment Variable:**
    *   Create a `.env` file in the root of your project.
    *   Add your Gemini API key as follows:
        ```dotenv
        API_KEY_GEMINI_PRO_1.5="YOUR_GEMINI_API_KEY"
        ```
    *   **Note:** The variable name `API_KEY_GEMINI_PRO_1.5` is the one expected in the code.

### Environment Variables

In addition to the Gemini API key, you need to specify the Google Drive folder from which videos will be downloaded.

*   In the `.env` file, add the following variable:
    ```dotenv
    carpeta_drive="GOOGLE_DRIVE_FOLDER_ID"
    ```
    *   To get a Google Drive folder ID, open the folder in your browser. The ID is the part of the URL after `/folders/` (e.g., `https://drive.google.com/drive/folders/THIS_IS_THE_ID`).

## 🚀 Project Usage

### Execution Flow

The system is designed to run in two main phases:

1.  **Auditing and Data Generation Phase (`main.py`):** Downloads videos, processes them with AI, and generates JSON/CSV reports.
2.  **PDF Report Generation Phase (`Create_html_to_PDF.py`):** Takes the generated JSON reports and converts them into stylized HTML documents and then into PDFs.

### Running the Main Script (`main.py`)

This script is responsible for auditing the videos.

1.  Ensure all [dependencies](#python-dependencies) are installed and [environment variables](#environment-variables) are configured.
2.  Run the script from the terminal:
    ```bash
    python main.py
    ```
3.  The script will:
    *   Authenticate with Google Drive.
    *   List and download videos from the specified folder.
    *   Optimize each video.
    *   Upload the video (or its parts) to Google Gemini for auditing.
    *   Generate a `Reporte_Auditoria_VIDEO_NAME.txt` (JSON) and `Reporte_Auditoria_VIDEO_NAME.csv` file for each audited video.
    *   Delete temporary video files.

### Generating HTML and PDF Reports (`Create_html_to_PDF.py`)

Once `main.py` has generated the `.txt` files with the JSON reports, this script will transform them into professional PDF reports.

1.  Ensure the [Google Gemini API](#google-gemini-api-setup) is configured in your `.env` file.
2.  Run the script from the terminal:
    ```bash
    python Create_html_to_PDF.py
    ```
3.  The script will:
    *   Search for all `Reporte_Auditoria_*.txt` files in the current directory.
    *   For each file, it will upload it to Google Gemini.
    *   Request Gemini to convert the report content into stylized HTML code, following predefined design guidelines.
    *   Save the generated HTML as `Reporte_Auditoria_VIDEO_NAME.html`.
    *   Convert the HTML file to `Reporte_Auditoria_VIDEO_NAME.pdf` using `xhtml2pdf`.
    *   Delete temporary Gemini files.

## 📊 Output Data Structure

The auditing process generates structured data in JSON format, which can then be exported to CSV for tabular analysis.

### JSON Output Example

The `Reporte_Auditoria_VIDEO_NAME.txt` file will contain a JSON object with the following structure:

```json
{
  "resumen_clase": "Concise description of the topics covered in the class, including main points and pedagogical approach.",
  "objetivo_alcanzado": "Yes - The lesson objective was clearly achieved, with an effective demonstration of key concepts.",
  "puntos_fuertes": [
    "Exceptional clarity in explaining complex concepts.",
    "Effective use of practical examples and analogies to facilitate understanding.",
    "Active encouragement of student participation through open-ended questions.",
    "Excellent handling of digital tools for content presentation."
  ],
  "oportunidades_mejora": [
    "Some transitions between topics were abrupt, slightly affecting the flow.",
    "Could integrate more interactive activities to reinforce practical learning.",
    "The pace in the final section was a bit fast, leaving less time for questions."
  ],
  "recomendaciones_accionables": [
    "Plan smoother transitions between thematic modules.",
    "Incorporate a brief practical exercise or quiz at the end of each main section."
  ],
  "nivel_participacion": "High - Students actively interacted, asking pertinent questions and responding to the instructor's prompts.",
  "manejo_del_tiempo": "Adequate - Time was balanced between theoretical exposition, examples, and a Q&A session, though the end was a bit tight.",
  "herramientas_utilizadas": [
    "Slide presentation (Google Slides)",
    "Virtual whiteboard (Jamboard)",
    "Quick polls (Mentimeter)"
  ],
  "incidencias_notables": [
    "Brief audio interruption at the beginning due to a misconfigured microphone (quickly resolved)."
  ],
  "calificacion_pedagogica": 92,
  "calificacion_tecnica": 88,
  "comentario_final": "The class demonstrated a high level of preparation and pedagogical execution. A focus on smoother transitions and integrating more interactive elements is recommended to maximize learning retention."
}
```

### CSV Output Example

The `Reporte_Auditoria_VIDEO_NAME.csv` file will present the JSON data in a tabular format, with lists concatenated by newlines to keep the information within a single cell.

```csv
resumen_clase,objetivo_alcanzado,puntos_fuertes,oportunidades_mejora,recomendaciones_accionables,nivel_participacion,manejo_del_tiempo,herramientas_utilizadas,incidencias_notables,calificacion_pedagogica,calificacion_tecnica,comentario_final
"Concise description of the topics covered in the class, including main points and pedagogical approach.","Yes - The lesson objective was clearly achieved, with an effective demonstration of key concepts.","Exceptional clarity in explaining complex concepts.\nEffective use of practical examples and analogies to facilitate understanding.\nActive encouragement of student participation through open-ended questions.\nExcellent handling of digital tools for content presentation.","Some transitions between topics were abrupt, slightly affecting the flow.\nCould integrate more interactive activities to reinforce practical learning.\nThe pace in the final section was a bit fast, leaving less time for questions.","Plan smoother transitions between thematic modules.\nIncorporate a brief practical exercise or quiz at the end of each main section.","High - Students actively interacted, asking pertinent questions and responding to the instructor's prompts.","Adequate - Time was balanced between theoretical exposition, examples, and a Q&A session, though the end was a bit tight.","Slide presentation (Google Slides)\nVirtual whiteboard (Jamboard)\nQuick polls (Mentimeter)","Brief audio interruption at the beginning due to a misconfigured microphone (quickly resolved).",92,88,"The class demonstrated a high level of preparation and pedagogical execution. A focus on smoother transitions and integrating more interactive elements is recommended to maximize learning retention."
```

## 🔬 Technical Analysis and Added Value

This project integrates various technologies to build a robust and efficient auditing pipeline. The selection of each tool is based on its ability to provide technical value and solve specific challenges.

### Google Drive Integration

*   **Technology:** `pydrive2`
*   **Added Value:** `pydrive2` provides a Pythonic interface for the Google Drive API, simplifying authentication (OAuth 2.0), file navigation, and downloading. The implementation includes retry logic and file size verification (`os.path.getsize` vs `archivo['fileSize']`) to ensure complete and reliable downloads, mitigating network or API issues. This is crucial to guarantee the integrity of the source material for auditing.

### Video Optimization with FFmpeg and MoviePy

Video optimization is a critical step to reduce AI processing costs and time, as multimodal language models consume resources based on video duration and quality.

*   **Technology:** `MoviePy` (with `imageio-ffmpeg` as backend) and `FFmpeg` (directly via `subprocess`).
*   **Added Value:**
    *   **Cost and Time Reduction:** By reducing resolution (`height=240` or `scale=-2:360`), accelerating playback (`MultiplySpeed, 1.5` or `setpts=0.666667*PTS, atempo=1.5`), and decreasing `fps` (`0.5`), the amount of data the AI needs to process is minimized, optimizing token consumption and response time.
    *   **MoviePy:** Offers a high-level abstraction for video editing, facilitating operations like resizing and speed changes with intuitive syntax. It is useful for rapid prototyping.
    *   **FFmpeg (Direct):** The `subprocess.run` implementation with `FFmpeg` is a robust *fallback* mechanism. `FFmpeg` is the industry standard for media processing, known for its efficiency and granular control. When `MoviePy` (which can sometimes be less stable or slower for certain operations) fails, the direct call to `FFmpeg` ensures that optimization is completed reliably. Parameters such as `-filter_complex`, `-preset ultrafast`, `-b:a 32k`, and `-ac 1` are tuned for maximum compression with sufficient quality for content analysis (not for high-fidelity viewing).
    *   **Long Video Segmentation:** For videos exceeding Gemini's token limits, `FFmpeg` is used to segment the video into smaller parts (`-segment_time 1500` for 25 minutes per segment). This allows processing videos of any duration, overcoming API limitations.

### Content Auditing with Google Gemini

The heart of the system lies in the AI's ability to analyze the pedagogical and technical content of classes.

*   **Technology:** `google.generativeai` with the `gemini-2.5-flash` model.
*   **Added Value:**
    *   **Advanced Multimodal Analysis:** `gemini-2.5-flash` is a multimodal model optimized for speed and efficiency, ideal for processing videos and extracting relevant information about class dynamics.
    *   **Structured Prompts and `system_instruction`:** Defining a `system_instruction` (`You are an Educational Quality Auditor...`) and a detailed `prompt_final` that demands specific JSON output ensures the AI adheres to a predefined role and format. This is crucial for report consistency and parseability.
    *   **Context Handling for Segmented Videos (RAG-like):** The `generar_prompt_dinamico` function implements a "memory" or accumulated context mechanism. For segmented videos, the JSON report generated by a previous fragment is fed back to the AI as `contexto_anterior` for the next fragment. This allows Gemini to build a unified and coherent report across the entire video, overcoming API context window limitations for very long inputs.
    *   **Rate Limit Handling:** Retry logic with `time.sleep(30)` for `429` (Quota Exceeded) errors ensures the robustness of the process against API limitations, preventing failures in auditing extensive or batch videos.
    *   **Quantitative and Qualitative Metrics:** The JSON structure requests numerical ratings (`calificacion_pedagogica`, `calificacion_tecnica`) along with detailed qualitative descriptions, providing a holistic view.

### Professional Report Generation

The presentation of results is as important as the analysis itself.

*   **Technology:** `google.generativeai` (for HTML) and `xhtml2pdf` (for PDF).
*   **Added Value:**
    *   **AI Styling:** Using Gemini to convert JSON to HTML (`PROMPT` in `Create_html_to_PDF.py`) allows for dynamic report generation with a professional and aesthetic design, without the need for complex static HTML templates. The strict directive **not to use flexbox, CSS grid, or :root variables** in the prompt ensures compatibility with `xhtml2pdf` and avoids rendering complexities that might arise with modern CSS.
    *   **Brand Consistency:** The `Plantilla_HTML` (CSS) embedded in the prompt guides Gemini to use specific colors and fonts (`Tahoma`, orange palette), ensuring that the final reports align with the company's visual identity.
    *   **Robust PDF Generation:** `xhtml2pdf` (`pisa.CreatePDF`) is a reliable Python library for converting HTML and CSS to PDF. Unlike `pdfkit` (which often requires `wkhtmltopdf` as an external OS dependency), `xhtml2pdf` is a more self-contained Python solution, simplifying implementation and deployment. It produces high-quality PDF documents, ready for distribution or archiving.

## 📈 Business Impact

This automated educational content auditing system is not just a technical tool, but a strategic lever for continuous improvement and operational efficiency in educational institutions.

### Business Questions Addressed

*   How can we ensure consistent teaching quality across all our recorded classes?
*   What specific areas do our instructors need to improve to optimize the learning experience?
*   Is it possible to scale our quality control process without incurring prohibitive staffing costs?
*   Are we making the most of digital tools in our classes?
*   How can we obtain objective and standardized feedback on teaching performance?

### Added Value

The system provides significant added value by transforming a manual, subjective, and slow process into an automated, objective, and scalable one. It frees human auditors to focus on higher-value strategic tasks, such as developing training programs or individualized mentoring, instead of routine video review. Consistency in evaluation and speed in report delivery enable agile, data-driven decision-making.

### Enables Measurement

*   **Pedagogical and Technical Quality:** Quantifies instructor performance with numerical ratings (0-100), complemented by qualitative descriptions.
*   **Engagement Level:** Evaluates student interaction (High/Medium/Low) and describes its dynamics.
*   **Time Management:** Measures efficiency in class time distribution.
*   **Tool Usage:** Records digital tools used, allowing tracking of technology adoption.
*   **Incidents:** Identifies and records technical issues or interruptions, quantifying their frequency and type.
*   **Strengths and Opportunities:** Provides structured lists of successes and areas for improvement, facilitating trend analysis.

### Enables Diagnosis

*   **Specific Instructor Weaknesses:** Identifies patterns of failures (e.g., "filler words," confusing explanations, lack of interaction) that require attention.
*   **Methodological Inefficiencies:** Diagnoses whether certain methodologies are not being effective or if the class pace is inadequate.
*   **Recurring Technical Problems:** Points out incidents such as connection failures or audio problems, which may indicate infrastructure or technical training needs.
*   **Gaps in Technology Adoption:** Reveals whether digital tools are not being used or if their use is suboptimal.
*   **Training Needs:** Aggregates data to identify common areas for improvement in the teaching staff, informing the design of professional development programs.

### Enables Resolution and Scoping

*   **Actionable Recommendations:** Provides concrete and direct suggestions for teachers to improve in their next class.
*   **Focus on Improvement:** Allows academic directors to narrow down areas for improvement for each instructor, making feedback more effective and less overwhelming.
*   **Early Intervention:** By quickly identifying problems, solutions can be implemented before they affect a large number of students.
*   **Resource Optimization:** Directs training and technical support resources to where they are most needed.

### Enables Optimization

*   **QA Process:** Drastically reduces the time and cost associated with manual video auditing.
*   **Teacher Development:** Optimizes the effectiveness of training programs by basing them on real data and identified needs.
*   **Student Experience:** Indirectly improves teaching quality, leading to a better learning experience and higher retention rates.
*   **Bandwidth and Storage Usage:** Video compression for AI optimizes network and cloud storage resource usage.
*   **Scalability:** Allows auditing a massive volume of classes without a linear increase in QA staff.

### Enables Standardization

*   **Evaluation Criteria:** Establishes a uniform and objective set of evaluation criteria applied by AI, eliminating human subjectivity.
*   **Report Format:** Generates standardized reports in JSON, CSV, and PDF, facilitating comparison, archiving, and integration with academic management systems.
*   **Quality Level:** Defines a consistent quality threshold for all classes, ensuring institutional standards are met.
*   **Internal Processes:** Standardizes the quality control workflow, from video ingestion to report delivery.

### Enables Rethinking

*   **Institutional Pedagogical Strategies:** Aggregated data can reveal the need to rethink and adapt teaching methodologies at an institutional level, promoting more effective and participatory approaches.
*   **Curriculum Design:** If reports consistently show difficulties in certain topics or a lack of use of specific tools, it may lead to a review of course design.
*   **Teacher Training Programs:** Allows redesigning professional development programs to address the most critical competencies and common deficiencies identified by AI.
*   **Technological Infrastructure:** The recurrence of technical incidents can drive a re-evaluation and improvement of network infrastructure, LMS platforms, or recording equipment.
*   **Performance Evaluation Model:** The system can integrate new metrics or adjust existing ones, allowing for continuous evolution of the teacher evaluation model.
*   **Classroom Innovation:** By freeing up QA team time and providing clear insights, experimentation with new tools and pedagogical approaches is encouraged, knowing that their impact will be measured and reported.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.