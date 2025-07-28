
import requests
import os
import random
from urllib.parse import urlencode
from dotenv import load_dotenv

# Cargar API Key
load_dotenv()
PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")

# Parámetros
SEARCH_QUERY = "relaxing nature background"
VIDEO_SAVE_PATH = "video/base.mp4"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def buscar_y_descargar_video():
    print("🔍 Buscando vídeos relajantes en Pixabay...")

    params = {
        "key": PIXABAY_API_KEY,
        "q": SEARCH_QUERY,
        "video_type": "film",
        "per_page": 10
    }

    url = f"https://pixabay.com/api/videos/?{urlencode(params)}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("❌ Error al consultar Pixabay:", response.status_code, response.text)
        return

    data = response.json()
    hits = data.get("hits", [])
    if not hits:
        print("⚠️ No se encontraron vídeos para la búsqueda.")
        return

    # Seleccionar un vídeo aleatorio
    video = random.choice(hits)
    video_url = video["videos"]["medium"]["url"]
    tags = video.get("tags", "Sin título")

    print(f"🎞️ Vídeo seleccionado: {tags}")
    print(f"📥 Descargando: {video_url}")

    # Descargar el vídeo
    try:
        video_response = requests.get(video_url, headers=HEADERS)
        if video_response.status_code != 200:
            print("❌ Error al descargar el vídeo:", video_response.status_code)
            return

        os.makedirs("video", exist_ok=True)
        with open(VIDEO_SAVE_PATH, "wb") as f:
            f.write(video_response.content)

        # Validar tamaño del archivo
        size_kb = os.path.getsize(VIDEO_SAVE_PATH) / 1024
        if size_kb < 100:
            print(f"⚠️ El archivo parece corrupto o vacío ({size_kb:.2f} KB).")
        else:
            print(f"✅ Vídeo guardado como {VIDEO_SAVE_PATH} ({size_kb:.2f} KB)")

    except Exception as e:
        print("❌ Error durante la descarga:", str(e))

if __name__ == "__main__":
    buscar_y_descargar_video()
