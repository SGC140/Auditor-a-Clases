import google.generativeai as genai
import os
import glob
import time
from dotenv import load_dotenv
import pdfkit
from xhtml2pdf import pisa
from datetime import date 

    #En el ".env" de su proyecto deben definir la variable que contiene su api_key ej: API_IA = "AI123X1CX312G3AJHSDASD"
    #Y con ello, declaran la variable de load_toenv para que la reconozca

load_dotenv(override=True)

documentos_conversion = sorted(glob.glob("Reporte_Auditoria_*.txt"))
nombre_modelo_IA = 'gemini-2.5-flash' 
api_gemini_key = os.getenv("API_KEY_GEMINI_PRO_1.5")
genai.configure(api_key= api_gemini_key)
año_actual = date.today().year

Plantilla_HTML = ("""
body { font-family: 'Tahoma', sans-serif; font-size: 12px; color: #333; background-color: #FFF8F0; }
.container { width: 90%; margin: 20px auto; padding: 25px; background-color: #FFF; border: 1px solid #FFBE7D; }
h1 { color: #CC5500; text-align: center; border-bottom: 2px solid #FF9933; }
h2 { color: #E67E22; border-left: 5px solid #FF9933; padding-left: 10px; }
.section-box { background-color: #FFF2E6; border: 1px solid #FFDAB9; padding: 15px; margin-bottom: 15px; }
.key-metrics-table { width: 100%; border-collapse: collapse; }
.key-metrics-table th { background-color: #FFB380; border: 1px solid #FFBE7D; padding: 8px; }
.key-metrics-table td { border: 1px solid #FFBE7D; padding: 8px; text-align: center; font-weight: bold; color: #CC5500; }
.footer { text-align: center; font-size: 10px; color: #777; margin-top: 30px; }
""")


PROMPT = (
    "Convierte este archivo en un código HTML muy bonito y profesional (sin emojis). "
    "REGLA ESTRICTA: Usa CSS básico en línea o en <style>. NO uses flexbox, CSS grid, ni variables :root. "
    "Usa tablas o divs con márgenes para la estructura. "
    "Abstente a responder únicamente con el contenido del HTML y NO PONGAS '```html' AL PRINCIPIO."
    "Con margen justificado, letra grande y bonita, colores naranjas (que son los de la compañía). Buen uso de la negrilla y el tamaño de la letra. Letra Tahoma 12 para el cuerpo."
    "Interlineado sencillo, mucha creatividad sin perder lo técnico y lo profesional un buen título en función del nombre del archivo que estás analizando y sin tanto gasto de espacios y páginas"
    f"Manten un buen uso de los recuadros, las listas, el texto, las filas y los diseños, usa buenas paletas de color al rededor del naranja (uso bueno de la intensidad de la variación en la paleta de color naranja, genera un último disclamer de 'Copyrigth Kuepa {año_actual}'."
    f"Básate en esta plantilla: {Plantilla_HTML} (solo el diseño. El único texto debe ser el que te cargo como archivo HTML)"
)

configuracion_gemini = genai.GenerativeModel(model_name=nombre_modelo_IA)


for documento in documentos_conversion:
    intentos = 0
    documento_subido = genai.upload_file(documento)
    time.sleep(30)
    while documento_subido.state.name == 'PROCESSING':
        intentos += 1
        print(f"contador {intentos} x5")
        time.sleep(10)
        documento_subido = genai.get_file(documento_subido.name)

    if documento_subido.state.name == 'ACTIVE':
        print("Documento cargado exitosamente")
        print(f"ID: {documento_subido.name}")
        print("Esperando 10 segundos después del cargue")
        time.sleep(10)

        resultado_prompt = configuracion_gemini.generate_content([documento_subido, PROMPT])


        print("Generando HTML")
        html_input = resultado_prompt.text
        print(html_input)
        genai.delete_file(documento_subido.name)

        tipo_archivo_html = documento.replace(".txt", ".html")
        with open(tipo_archivo_html, "w", encoding="utf-8") as documento_html:
            documento_html.write(html_input)

        concepto_pdf = tipo_archivo_html.replace(".html", ".pdf")

        print("Generando PDF")
        with open(tipo_archivo_html, "r", encoding="utf-8") as archivo_html_final:
            with open(concepto_pdf, "wb") as archivo_pdf_final:
                auditoria_pdf = pisa.CreatePDF(archivo_html_final, dest=archivo_pdf_final)

        
        print(f"PDF Generado: {concepto_pdf}")
        time.sleep(20)
        




