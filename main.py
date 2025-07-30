import os
import subprocess
import sys

SCRIPTS = [
    "scripts/0_generate_metadata.py",     # Generar título y descripción
    "scripts/1_generate_script.py",
    "scripts/2_generate_voice.py",
    "scripts/download_music.py",
    "scripts/3_generate_audio.py",
    "scripts/download_video.py",
    "scripts/4_generate_video.py",
    "scripts/upload_to_youtube.py"             # Subir a YouTube
]

def run_script(script_path):
    print(f"\n🚀 Ejecutando {script_path}...\n")
    result = subprocess.run([sys.executable, script_path])
    if result.returncode != 0:
        print(f"❌ Error al ejecutar {script_path}")
        exit(1)

if __name__ == "__main__":
    print("🧠 Comenzando generación automática de vídeo relajante...\n")
    for script in SCRIPTS:
        run_script(script)
    print("\n✅ ¡Proceso completo! El vídeo final ha sido generado y subido a YouTube.\n")
