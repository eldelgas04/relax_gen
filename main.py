import os
import subprocess

SCRIPTS = [
    "scripts/1_generate_script.py",
    "scripts/2_generate_voice.py",
    "scripts/download_music.py",
    "scripts/3_generate_audio.py",
    "scripts/download_video.py",
    "scripts/4_generate_video.py"
]

def run_script(script_path):
    print(f"\n🚀 Ejecutando {script_path}...\n")
    result = subprocess.run(["python", script_path])
    if result.returncode != 0:
        print(f"❌ Error al ejecutar {script_path}")
        exit(1)

if __name__ == "__main__":
    print("🧠 Comenzando generación automática de vídeo relajante...\n")
    for script in SCRIPTS:
        run_script(script)
    print("\n✅ ¡Proceso completo! El vídeo final ha sido generado.\n")
