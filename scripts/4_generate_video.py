
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.editor import concatenate_videoclips

# Rutas
VIDEO_PATH = "video/base.mp4"
AUDIO_PATH = "audio/final.mp3"
OUTPUT_PATH = "video/final.mp4"

print("🎞️ Cargando vídeo base...")
video = VideoFileClip(VIDEO_PATH)

print("🎧 Cargando audio final...")
audio = AudioFileClip(AUDIO_PATH)

# Calcular cuántas veces hay que repetir el vídeo para cubrir el audio
repeticiones = int(audio.duration // video.duration) + 1
print(f"🔁 Repeticiones necesarias: {repeticiones}")

# Repetir el vídeo en bucle tipo gif
video_loop = concatenate_videoclips([video] * repeticiones)

# Recortar el vídeo al tamaño exacto del audio
video_final = video_loop.subclip(0, audio.duration)

# Asignar el audio
video_final = video_final.set_audio(audio)

# Exportar
print("📤 Exportando vídeo final...")
video_final.write_videofile(OUTPUT_PATH, codec="libx264", audio_codec="aac")
print("✅ ¡Vídeo final exportado con éxito!")