import os
import requests
from dotenv import load_dotenv

# Cargar API key del archivo .env
load_dotenv()
api_key = os.getenv("FREESOUND_API_KEY")

# Paso 1: Buscar música relajante con licencia CC0
print("🔍 Buscando música relajante (CC0)...")
url = "https://freesound.org/apiv2/search/text/"
params = {
    "query": "relaxing ambient music",
    "filter": "license:\"Creative Commons 0\"",
    "fields": "id,name,previews",
    "sort": "score",
    "page_size": 1,
    "token": api_key
}

response = requests.get(url, params=params)
if response.status_code != 200:
    print("❌ Error al buscar sonidos:", response.text)
    exit()

results = response.json().get("results", [])
if not results:
    print("⚠️ No se encontraron sonidos con licencia CC0.")
    exit()

# Paso 2: Descargar el audio
sound = results[0]
sound_name = sound["name"]
preview_url = sound["previews"]["preview-hq-mp3"]

print(f"🎵 Descargando: {sound_name}")
os.makedirs("audio", exist_ok=True)
output_path = os.path.join("audio", "musica.mp3")

audio_response = requests.get(preview_url)
with open(output_path, "wb") as f:
    f.write(audio_response.content)

print(f"✅ Música guardada en {output_path}")