import os
import requests
from dotenv import load_dotenv

# Cargar clave API desde .env
load_dotenv()
api_key = os.getenv("ELEVEN_API_KEY")

if not api_key:
    print("❌ ERROR: No se encontró ELEVEN_API_KEY en el archivo .env")
    exit()

url = "https://api.elevenlabs.io/v1/voices"
headers = {"xi-api-key": api_key}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    voces = response.json()["voices"]

    print("🗣️ Voces disponibles en tu cuenta:\n")
    for voz in voces:
        nombre = voz.get("name", "Desconocido")
        voice_id = voz.get("voice_id", "N/A")
        idioma = voz.get("labels", {}).get("language", "No especificado")
        codigos = voz.get("language_codes", [])
        if "es" in idioma:
            print(f"- {nombre} (ID: {voice_id})")
            print(f"  🌍 Idioma principal: {idioma}")
            print(f"  📄 Códigos de idioma: {', '.join(codigos) if codigos else 'No disponibles'}\n")
else:
    print(f"❌ Error al obtener voces: {response.status_code}")
    print(response.text)
