import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
HEADERS = {"xi-api-key": API_KEY}
BASE_URL = "https://api.elevenlabs.io/v1"

def list_voices():
    response = requests.get(f"{BASE_URL}/voices", headers=HEADERS)
    response.raise_for_status()
    voices = response.json()["voices"]

    for idx, voice in enumerate(voices):
        print(f"\n🎤 Voz #{idx + 1}")
        print(f"ID: {voice['voice_id']}")
        print(f"Nombre: {voice['name']}")
        print(f"Idioma(s): {', '.join(voice['labels'].get('accent', []))}")
        print(f"Descripción: {voice.get('description', 'Sin descripción')}")

        # Opción de escuchar una muestra
        sample_url = voice.get("preview_url")
        if sample_url:
            sample_response = requests.get(sample_url)
            sample_path = f"audio/sample_{voice['name'].replace(' ', '_')}.mp3"
            with open(sample_path, "wb") as f:
                f.write(sample_response.content)
            print(f"🔊 Muestra guardada como {sample_path}")

if __name__ == "__main__":
    print("📋 Listando voces disponibles en ElevenLabs...")
    list_voices()
