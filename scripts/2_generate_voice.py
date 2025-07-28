import os
import requests
from dotenv import load_dotenv

# Cargar API Key desde .env
load_dotenv()
api_key = os.getenv("ELEVEN_API_KEY")

# ID de voz (puedes cambiarlo por cualquier voz disponible en tu cuenta)
voice_id = os.getenv("VOICE_ID_ELEVENPATH")

# Leer el guion desde archivo
try:
    with open("audio/guion.txt", "r", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:
    print("❌ ERROR: No se encontró el archivo guion.txt. Ejecuta primero 1_generate_script.py")
    exit()

# Validar que la API key esté cargada
if not api_key:
    print("❌ ERROR: No se encontró ELEVEN_API_KEY en el archivo .env")
    exit()

# Preparar llamada a ElevenLabs API
print("📡 Enviando texto a ElevenLabs para generar voz...")

url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}
body = {
    "text": texto,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    }
}

# Enviar solicitud
response = requests.post(url, headers=headers, json=body)

# Guardar el audio resultante
if response.status_code == 200:
    with open("audio/voz.mp3", "wb") as f:
        f.write(response.content)
    print("✅ Voz generada correctamente y guardada como audio/voz.mp3")
else:
    print(f"❌ ERROR al generar voz: {response.status_code}")
    print(response.text)