import yt_dlp
import os
import time
from pathlib import Path
from datetime import timedelta
import sys

class SilentLogger:
    """Clase para silenciar los logs de yt-dlp"""
    def debug(self, msg): pass
    def info(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass

def mostrar_progreso(info):
    if info['status'] == 'downloading':
        porcentaje = info.get('_percent_str', '0.0%')
        velocidad = info.get('_speed_str', 'N/A')
        eta = info.get('_eta_str', 'N/A')
        duracion = str(timedelta(seconds=info.get('duration', 0)))
        
        print(f"\r\033[K⏳ {duracion} | 🚀 {velocidad} | 🕑 ETA: {eta} | {porcentaje}", end='', flush=True)
        
    elif info['status'] == 'finished':
        # Obtener el nombre base y cambiar extensión a .mp3
        filename = os.path.basename(info['filename'])
        nombre_base = os.path.splitext(filename)[0]  # Elimina la extensión original
        print(f"\r\033[K✅ {nombre_base}.mp3")  # Fuerza la extensión .mp3

def descargar_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join('musica', '%(title)s.%(ext)s'),
        'progress_hooks': [mostrar_progreso],
        'keepvideo': False,
        'writethumbnail': False,
        'logger': SilentLogger(),
        'quiet': True,
        'no_warnings': True,
        'noprogress': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return False

def main():
    start_time = time.time()  # Tiempo de inicio del programa
    Path("musica").mkdir(exist_ok=True)
    
    try:
        with open("url.txt", "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print("⚠️ ¡url.txt no encontrado!")
        return

    if not urls:
        print("ℹ️ No hay URLs en el archivo")
        return

    descargadas = []
    total = len(urls)
    
    for i, url in enumerate(urls, 1):
        print(f"\n📥 URL {i}/{total} - {url}")
        inicio_descarga = time.time()  # Tiempo de inicio de esta descarga
        
        if descargar_audio(url):
            descargadas.append(url)
        
        # Calcular tiempos
        tiempo_transcurrido = time.time() - start_time
        tiempo_descarga = time.time() - inicio_descarga
        
        # Formatear tiempos
        horas, resto = divmod(tiempo_transcurrido, 3600)
        minutos, segundos = divmod(resto, 60)
        tiempo_total = f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}"
        
        print(f"\n🕛 Tiempo total: {tiempo_total} | Tiempo descarga: {tiempo_descarga:.1f}s")
        print("<" + "-" * 50 + ">")

    with open("canciones.txt", "a") as f:
        f.write("\n".join(descargadas) + "\n")
        
    with open("url.txt", "w") as f:
        remaining = list(set(urls) - set(descargadas))
        f.write("\n".join(remaining))

    # Tiempo final total
    tiempo_total = timedelta(seconds=int(time.time() - start_time))
    print(f"\n🎉 {len(descargadas)} descargadas | {len(remaining)} fallidas | Tiempo total: {tiempo_total}")

if __name__ == "__main__":
    main()