import openai
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

def generar_metadata():
    prompt = (
        "Genera un título y una descripción atractiva para un vídeo relajante de YouTube "
        "con música suave y paisajes de naturaleza. El estilo debe ser tranquilo, relajante y amigable para SEO."
        "No menciones nada sobre la automatizacion de este video ni sobre SEO."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()

    # Separar título y descripción
    lines = content.split("\n")
    title = lines[0].replace("Título:", "").strip()
    description = "\n".join(lines[1:]).replace("Descripción:", "").strip()

    metadata = {
        "title": title,
        "description": description
    }

    os.makedirs("video", exist_ok=True)
    with open("video/metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print("✅ Título y descripción generados:")
    print("📝 Título:", title)
    print("📄 Descripción:", description)

if __name__ == "__main__":
    generar_metadata()
