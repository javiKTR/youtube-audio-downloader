# 🎵 YouTube Audio Downloader

Descarga audios de YouTube en formato MP3 de manera eficiente. Ideal para crear tu biblioteca musical personal.

---

## 📋 Requisitos Previos

- Python 3.8 o superior
- FFmpeg (para conversión de audio)
- Conexión a Internet

---

## 🛠 Instalación

### 1. Clonar el Repositorio
git clone https://github.com/tu-usuario/youtube-audio-downloader.git
cd youtube-audio-downloader

### 2. Instalar Dependencias de Python
pip install -r requirements.txt

Archivo requirements.txt:
yt-dlp==2023.11.16

### 3. Instalar FFmpeg

#### Windows:
1. Descarga FFmpeg desde: https://www.gyan.dev/ffmpeg/builds/
2. Extrae el ZIP en C:\ffmpeg
3. Añade C:\ffmpeg\bin al PATH del sistema

#### Linux (Debian/Ubuntu):
sudo apt update && sudo apt install ffmpeg

#### macOS (via Homebrew):
brew install ffmpeg

---

## 🚀 Uso

### 1. Preparar URLs
Crea un archivo url.txt con este formato:
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2

### 2. Ejecutar el Script
python main.py

### 3. Resultados
- Audios descargados: Carpeta musica/
- URLs procesadas: Archivo canciones.txt
- URLs pendientes: Archivo url.txt

---

## 🎨 Funcionalidades Clave

- Descarga múltiple simultánea
- Progreso visual con estadísticas en tiempo real
- Tiempos de ejecución detallados
- Reintentos automáticos en fallos
- Organización automática de archivos
- Calidad de audio 192kbps (MP3)

---

## 📂 Estructura del Proyecto

.
├── musica/           # Audios descargados
├── url.txt           # URLs por procesar
├── canciones.txt     # URLs completadas
├── main.py           # Script principal
└── requirements.txt  # Dependencias

---

## ⚠️ Notas Importantes

- El script solo descarga audio, no videos
- Las URLs fallidas permanecen en url.txt
- Verifica los términos de servicio de YouTube
- Uso educativo/demostrativo

---

## 🔄 Proceso de Descarga

1. Descarga el audio en formato original (webm/m4a)
2. Convierte a MP3 usando FFmpeg
3. Elimina el archivo temporal
4. Registra la URL en canciones.txt

---

## 📜 Licencia
MIT License - Ver archivo LICENSE