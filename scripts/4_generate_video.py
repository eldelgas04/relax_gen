
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

# Rutas
VIDEO_PATH = "video/base.mp4"
AUDIO_PATH = "audio/final.mp3"
OUTPUT_PATH = "video/final.mp4"

print("🎞️ Cargando vídeo base...")
video = VideoFileClip(VIDEO_PATH)

print("🎧 Cargando audio final...")
audio = AudioFileClip(AUDIO_PATH)

# Ajustar duración del audio al video
if video.duration < audio.duration:
    print("⚠️ El audio es más largo que el vídeo. Recortando audio.")
    audio = audio.with_duration(video.duration)
else:
    print("⚠️ El vídeo es más largo que el audio. Se usará sólo parte del vídeo.")
    video = video.subclip(0, audio.duration)

# Combinar video y audio
video = video.with_audio(audio)

# Exportar
print("📤 Exportando vídeo final...")
video.write_videofile(OUTPUT_PATH, codec="libx264", audio_codec="aac")
print("✅ ¡Vídeo final exportado con éxito!")
