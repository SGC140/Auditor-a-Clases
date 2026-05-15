import pandas as pd
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import pydrive2
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import dotenv
from dotenv import load_dotenv
import json

#Para loggearse deben correr la función(def) esta función (sacado de su proyecto de la API de Google):

#credentials = "credentials_modules.json"
#gauth = GoogleAuth()
#gauth.SaveCredentialsFile(credentials)
#drive = GoogleDrive(gauth) 

credentials = "credentials_module.json"

def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(credentials)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(credentials)
    else:
        gauth.Authorize()

    return GoogleDrive(gauth)

drive = login()

#En el .env declaran la variable con el ID de su carpeta de Drive en la que tengan los videos que deseen auditar

load_dotenv()
id_carpeta = os.getenv("carpeta_drive")
query = f"'{id_carpeta}' in parents and trashed = false"

lista_clases = drive.ListFile({'q': query}).GetList()
for archivo in lista_clases:
    nombre_archivo = archivo['title']
    id_archivo = archivo['id']

    #si tienen más de un video en la carpeta pero no quieren auditar todos, pueden hacer

    # if nombre_archivo = "archvio_que_deseen" (y deben identar el resto del código a la derecha para que no arroje errores): 


    print(f"{nombre_archivo} : {id_archivo}")
    tamaño_esperado = int(archivo['fileSize'])
    print(f"Tamaño esperado: {tamaño_esperado / (1024*1024):.2f} MB")



    clase_auditada = drive.CreateFile({'id': id_archivo})
    nombre_del_temporal = "video_clase_temporal.mp4"
    max_intentos = 3
    descarga_exitosa = False

    for intento in range(max_intentos):
        try:
            print(f"Intento número {intento+1}/{max_intentos}")
            clase_auditada.GetContentFile(nombre_del_temporal)

            tamaño_clase_local = os.path.getsize(nombre_del_temporal)

            if tamaño_clase_local == tamaño_esperado:
                print("Descarga perfecta. Prosigue la compresión y la auditoría")
                descarga_exitosa = True
                break
            else:
                print("reintentando")
        except Exception as error:
            print(f"Error en la descarga (API/Conexión/Local): {error}")

        if intento < max_intentos - 1:
            print("Reintentando en 7 segundos")
            time.sleep(7)

    if not descarga_exitosa:
        print("Error iterativo, es importante revisar, pasa al siguiente")
        pass
            
    #compresión con Moviepy

    from moviepy import VideoFileClip
    import moviepy.video.fx as vfx
    from moviepy.video.fx import MultiplySpeed

    def compresion_optimizacion(video_original, video_optimizado):
        try:
            clase = VideoFileClip(video_original)
            redimencion = clase.resized(height=240)
            clase_acelerada = redimencion.fx(MultiplySpeed, 1.5)
            clase_acelerada.write_videofile(
                video_optimizado,
                fps=0.5,
                preset = 'ultrafast',
                audio_bitrate='32k',
                ffmpeg_params=['-ac', '1'],
                threads=4,
                logger = None
            )
        except Exception as error:
            print(f"Algo salió mal, entonces revisar {error}")
            raise

        finally:
            if 'clase_acelerada' in locals():
                clase_acelerada.close()        
            if 'redimencion' in locals():
                redimencion.close()
            if 'clase' in locals():
                clase.close()

    #compresión directa con FFMPEG

    import subprocess
    import imageio_ffmpeg

    ruta_ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

    def compresion_directa(clase_original, clase_optimizada):
        comando = [
            ruta_ffmpeg, '-y', '-i', clase_original,
            '-filter_complex', '[0:v]setpts=0.666667*PTS,scale=-2:360,fps=0.5[v];[0:a]atempo=1.5[a]',
            '-map', '[v]', '-map', '[a]',
            '-map_metadata', '-1',
            '-shortest',
            '-preset', 'ultrafast',
            '-b:a', '32k',
            '-ac', '1',
            clase_optimizada
        ]

        try:
            subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print("Clase optimizada con éxito")

        except subprocess.CalledProcessError as error:
            print(f"error en el motor FFMPEG. Detalles: {error.returncode}")


    #Optimización
    try:
        print("Intento con moviepy")
        compresion_optimizacion("video_clase_temporal.mp4", "clase_optimizada.mp4")
    except:
        print("Moviepy falló (como siempre) y toca usar el poderosísimo FFMPEG") 
        compresion_directa("video_clase_temporal.mp4", "clase_optimizada.mp4")

        print(f"Tamaño final del video comprimido: {os.path.getsize("clase_optimizada.mp4")/ (1024*1024):.2f} MB")

    #Proceso de Auditoría

    import google.generativeai as genai
    import glob


    #En el ".env" de su proyecto deben definir la variable que contiene su api_key ej: API_IA = "AI123X1CX312G3AJHSDASD"
    #Y con ello, declaran la variable de load_toenv para que la reconozca

    load_dotenv(override=True)
    api_gemini_key = os.getenv("API_KEY_GEMINI_PRO_1.5")

    genai.configure(api_key= api_gemini_key)

    nombre_modelo_IA = 'gemini-2.5-flash' 
    clase_para_auditar = "clase_optimizada.mp4"

    try:

        archivo_clase = genai.upload_file(path=clase_para_auditar)
        print(f"Archivo subido exitosamente. ID: {archivo_clase.name}")

            
        while archivo_clase.state.name == "PROCESSING":
            print(".", end="", flush=True)
            time.sleep(10)
            archivo_clase = genai.get_file(archivo_clase.name)

        if archivo_clase.state.name == "FAILED":
            detalle_error = archivo_clase.error
            
            print("Error crítico: Gemini no pudo procesar el video.")    
            if detalle_error:
                print(f"Código de error: {detalle_error.code}")
                print(f"Mensaje del sistema: {detalle_error.message}")
            else:
                print("No se recibió un mensaje de error específico del servidor.")

        else: 
            print("Todo en orden")

    except Exception as error:
        print(f"Problema en la subida (internet/local) {error}")


    configuracion_gemini = {
        "temperature": 0.1,  
        "response_mime_type": "application/json",}

    instrucciones = (
        "Eres un Auditor de Calidad Educativa. Tu misión es analizar grabaciones de clases "
        "y detectar: claridad del profesor, dominio del tema, uso de herramientas digitales, participación de la clase y resolución de dudas. "
        "Debes responder única y exclusivamente con un objeto JSON (no hace falta que saludes, ni que digas lo que hiciste, únicamente responde en función del rol que asumes)."
    )

    funcionalidad_gemini = genai.GenerativeModel(
        model_name = nombre_modelo_IA,
        generation_config= configuracion_gemini,
        system_instruction= instrucciones
    ) 

    prompt_final = """
    Eres un auditor académico experto. Analiza este video de una clase y genera un informe de auditoría estricto con la siguiente estructura JSON:

    {
    "resumen_clase": "Breve descripción de qué trato la clase",
    "objetivo_alcanzado": "Sí/No/Parcialmente - Breve justificación de si se logró el propósito de la lección",
    "puntos_fuertes": ["lista de aciertos del profesor, metodologías efectivas, buen trato, etc."],
    "oportunidades_mejora": ["lista de fallos, muletillas, confusiones o cosas a mejorar"],
    "recomendaciones_accionables": ["1 o 2 acciones prácticas y directas que el profesor debe aplicar en su próxima clase para mejorar"],
    "nivel_participacion": "Alta/Media/Baja - Breve descripción de cómo interactuaron los alumnos (si hubo preguntas, respuestas, o apatía)",
    "manejo_del_tiempo": "Breve evaluación de cómo se distribuyó el tiempo (ej. mucho tiempo explicando y poco practicando)",
    "herramientas_utilizadas": ["Lista las herramientas (como presentaciones, juegos interactivos, pizarrón, etc.)"],
    "incidencias_notables": ["Fallas de conexión, interrupciones, ruido de fondo prolongado, o 'Ninguna' si todo fluyó bien"],
    "calificacion_pedagogica": 0/100,
    "calificacion_tecnica": 0/100,
    "comentario_final": "Conclusión ejecutiva y directa para el director de la institución"
    }
    """

    calculo_tokens = funcionalidad_gemini.count_tokens([archivo_clase, prompt_final])
    total_tokens = calculo_tokens.total_tokens
    print(f"Tokens estimados: {total_tokens}")

    def generar_prompt_dinamico(parte_actual, total_partes, contexto_anterior):
        return f"""
    Eres un auditor académico experto. Estamos analizando una clase extensa que ha sido dividida en varias partes.
    Actualmente estás analizando el fragmento {parte_actual} de un total de {total_partes}.

    Para que tengas memoria del proceso y mantengas la coherencia, aquí tienes tu informe acumulado de las partes anteriores:
    {contexto_anterior}

    Tu misión es analizar este nuevo fragmento de video, fusionar tus nuevos hallazgos con el contexto anterior, y generar un informe de auditoría ÚNICO, ACTUALIZADO y GLOBAL.

    Devuelve única y exclusivamente el resultado en la siguiente estructura JSON:
    {{
    "resumen_clase": "Breve descripción acumulada de qué ha tratado la clase hasta ahora",
    "objetivo_alcanzado": "Sí/No/Parcialmente - Breve justificación global",
    "puntos_fuertes": ["lista unificada de aciertos del profesor (no borres los anteriores, suma los nuevos)"],
    "oportunidades_mejora": ["lista unificada de fallos o cosas a mejorar"],
    "recomendaciones_accionables": ["1 o 2 acciones prácticas generales basadas en todo lo visto"],
    "nivel_participacion": "Alta/Media/Baja - Evaluación global de la interacción",
    "manejo_del_tiempo": "Evaluación general del ritmo de la clase",
    "herramientas_utilizadas": ["Lista acumulada de todas las herramientas vistas en todos los fragmentos"],
    "incidencias_notables": ["Lista de fallas acumuladas, o 'Ninguna'"],
    "calificacion_pedagogica": 0/100,
    "calificacion_tecnica": 0/100,
    "comentario_final": "Conclusión ejecutiva que abarque todo lo analizado hasta este momento"
    }}
    """
    texto_reporte_final = ""

    if total_tokens <= 1000000:

        try:
            respuesta_IA = funcionalidad_gemini.generate_content([archivo_clase, prompt_final])
            print(f"Aduitoría finalizada:\n{respuesta_IA.text}")
            genai.delete_file(archivo_clase.name)
            print(f"Video: {archivo_clase.name} eliminado de la nube")


            metadata = respuesta_IA.usage_metadata

            print(f"""
            --- REPORTE DE CONSUMO ---
            Tokens de entrada (Prompt + Video): {metadata.prompt_token_count}
            Tokens de salida (Respuesta JSON):   {metadata.candidates_token_count}
            Total de tokens usados:            {metadata.total_token_count}""")

            texto_reporte_final = respuesta_IA.text

            if os.path.exists("video_clase_temporal.mp4"): os.remove("video_clase_temporal.mp4")
            if os.path.exists("clase_optimizada.mp4"): os.remove("clase_optimizada.mp4")

        except Exception as error:
            print(f"Hubo un error en el proceso: {error}") 

    else: 
        genai.delete_file(archivo_clase.name)
        comando_parseo = [
            ruta_ffmpeg, '-y', '-i', 'clase_optimizada.mp4',
            '-c', 'copy',
            '-f', 'segment',
            '-segment_time', '1500',
            '-reset_timestamps', '1',
            'clase_optimizada_parte_%03d.mp4'
        ]

        print("Parseo de videos con FFMPEG")
        subprocess.run(comando_parseo, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        partes_generadas = sorted(glob.glob("clase_optimizada_parte_*.mp4"))
        total_partes = len(partes_generadas)
        print(f"Se genero un total de {total_partes} videos parseados")

        contexto_acumulado = "Ninguno. Este es el primer fragmento del video, genera el primer reporte desde cero."

        for index, parte in enumerate(partes_generadas):
            parte_actual = index + 1
            print(f"Proceso con parte {parte_actual} de {total_partes} Video: {parte}")
        
            archivo_loop_parte = genai.upload_file(path=parte)
            while archivo_loop_parte.state.name == "PROCESSING":
                print(".", end="", flush=True)
                time.sleep(10)
                archivo_loop_parte = genai.get_file(archivo_loop_parte.name)

            if archivo_loop_parte.state.name == "FAILED":
                detalle_error = archivo_loop_parte.error
            
                print("Error crítico: Gemini no pudo procesar el video.")    
                if detalle_error:
                    print(f"Código de error: {detalle_error.code}")
                    print(f"Mensaje del sistema: {detalle_error.message}")
                else:
                    print("No se recibió un mensaje de error específico del servidor.")

            else: 
                print("Todo en orden")
                
            limite_intentos_ragelimit_api = 3

            for intentos_api in range(limite_intentos_ragelimit_api):                

                try:
                    prompt_loopeado = generar_prompt_dinamico(parte_actual, total_partes, contexto_acumulado)
                    respuesta_IA_loop = funcionalidad_gemini.generate_content([archivo_loop_parte, prompt_loopeado])

                    contexto_acumulado = respuesta_IA_loop.text
                    print(f"Auditoría parte {parte_actual} de {total_partes}")
                    break

                except Exception as error:
                    mensaje_error = str(error)
                    
                    if '429' in mensaje_error or 'Quota' in mensaje_error:
                        print(f'Se confirma que hubo un exceso de la cuota de peticiones. Esperando 30 segundos. Intento número {intentos_api + 1} de {limite_intentos_ragelimit_api} ')
                        if intentos_api < limite_intentos_ragelimit_api - 1:
                            time.sleep(30)
                        else:
                            print("Se agotó el número de reintentos")
                    
                    else:
                        print(f"Error (no asociado al rage_limit) auditando {parte}: {error}")

            texto_reporte_final = contexto_acumulado
            genai.delete_file(archivo_loop_parte.name)
            print(f"{parte} eliminada de la nube.")

        print("Eliminando parseos, videos temporales y optimizaciones")
        if os.path.exists("video_clase_temporal.mp4"): os.remove("video_clase_temporal.mp4")
        if os.path.exists("clase_optimizada.mp4"): os.remove("clase_optimizada.mp4")
        for parte in partes_generadas:
            os.remove(parte)

    print(f"""REPORTE FINAL DE AUDITORÍA:
        {texto_reporte_final}      
        """)

    res_limpio = contexto_acumulado.replace("```json", "").replace("```", "").strip()
    final_json = json.loads(res_limpio)

    with open(f"Reporte_Auditoria_{nombre_archivo}.txt", "w", encoding="utf-8") as f:
        f.write(res_limpio)

    df_dict = {k: ("\n".join(v) if isinstance(v, list) else v) for k, v in final_json.items()}
    pd.DataFrame([df_dict]).to_csv(f"Reporte_Auditoria_{nombre_archivo}.csv", index=False, encoding="utf-8-sig")

    print("Archivos generados.")