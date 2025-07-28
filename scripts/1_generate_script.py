import openai
import os
from dotenv import load_dotenv

# Cargar claves desde .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Cliente OpenAI (nuevo estilo desde v1.0.0+)
client = openai.OpenAI(api_key=api_key)

prompt = "Escribe una visualización guiada para relajarse antes de dormir, en segunda persona, de unos 3 minutos."

def generar_guion():
    print("📡 Solicitando guion a OpenAI...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    texto = response.choices[0].message.content.strip()

    with open("audio/guion.txt", "w", encoding="utf-8") as f:
        f.write(texto)

    print("✅ Guion generado correctamente.")
    return texto

if __name__ == "__main__":
    generar_guion()
