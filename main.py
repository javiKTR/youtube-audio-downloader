import yt_dlp
import os
import time
from pathlib import Path
from datetime import timedelta

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
        filename = os.path.basename(info['filename'])
        nombre_base = os.path.splitext(filename)[0]
        print(f"\r\033[K✅ {nombre_base}.mp3")

def descargar_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'writethumbnail': True,
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
            {'key': 'FFmpegMetadata'},
            {'key': 'EmbedThumbnail', 'already_have_thumbnail': False}
        ],
        'outtmpl': os.path.join('musica', '%(title)s.%(ext)s'),
        'progress_hooks': [mostrar_progreso],
        'keepvideo': False,
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
        print(f"\n❌ Error: {e}")
        return False

def main():
    start_time = time.time()

    Path("musica").mkdir(exist_ok=True)
    Path("url.txt").touch(exist_ok=True)
    Path("canciones.txt").touch(exist_ok=True)

    with open("url.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("ℹ️ No hay URLs en 'url.txt'. Añade alguna URL y vuelve a ejecutar.")
        return

    descargadas = []
    total = len(urls)

    for i, url in enumerate(urls, 1):
        print(f"\n📥 URL {i}/{total} - {url}")
        inicio = time.time()
        if descargar_audio(url):
            descargadas.append(url)
        td = time.time() - inicio
        tt = timedelta(seconds=int(time.time() - start_time))
        print(f"\n🕛 Tiempo total: {tt} | Tiempo descarga: {td:.1f}s")
        print("<" + "-" * 50 + ">")

    # 3) Registrar canciones descargadas
    if descargadas:
        with open("canciones.txt", "a") as f:
            f.write("\n".join(descargadas) + "\n")

    # 4) Actualizar url.txt con las que fallaron
    restantes = list(set(urls) - set(descargadas))
    with open("url.txt", "w") as f:
        f.write("\n".join(restantes))

    resumen = timedelta(seconds=int(time.time() - start_time))
    print(f"\n🎉 {len(descargadas)} descargadas | {len(restantes)} fallidas | Tiempo total: {resumen}")

if __name__ == "__main__":
    main()
