import os
from pydub import AudioSegment

# Cargar archivos de audio
print("🎙️ Cargando voz...")
voz = AudioSegment.from_file("audio/voz.mp3")

print("🎼 Cargando música...")
musica = AudioSegment.from_file("audio/musica.mp3")

# Si la música es más corta que la voz, la repetimos hasta que sea igual o mayor
if len(musica) < len(voz):
    repeticiones = int(len(voz) / len(musica)) + 1
    musica = musica * repeticiones

# Cortamos la música para que tenga exactamente la misma duración que la voz
musica = musica[:len(voz)]

# Bajamos el volumen de la música para que no tape la voz
musica = musica - 18  # en decibelios

# Mezclamos la música con la voz
print("🔊 Mezclando voz y música...")
final = musica.overlay(voz)

# Exportamos el resultado
os.makedirs("audio", exist_ok=True)
output_path = "audio/final.mp3"
final.export(output_path, format="mp3")

print(f"✅ Audio final exportado como {output_path}")
