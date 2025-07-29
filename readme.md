# 🧘‍♂️ RelaxGen - Generador Automático de Videos de Relajación

Este proyecto genera automáticamente vídeos relajantes combinando texto generado por IA, voz sintética, música ambiental y vídeos de naturaleza.

## 🚀 Características

- 🧠 Generación de guiones con GPT
- 🗣️ Conversión a voz usando ElevenLabs
- 🎶 Descarga automática de música desde FreeSound
- 🎞️ Descarga de vídeos relajantes desde Pixabay
- 🧩 Mezcla automática de audio y vídeo
- 🎥 Exportación final a un archivo MP4 listo para publicar

## 📁 Estructura del proyecto
relax_gen/
├── audio/ # Archivos de voz y música generados
├── video/ # Clips de vídeo base y exportaciones
├── scripts/ # Scripts de cada paso
├── .env # Variables de entorno (NO subir a Git)
├── main.py # Ejecuta todo el flujo automáticamente
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo


## ⚙️ Requisitos

- Python 3.9+
- API Key de ElevenLabs
- API Key de Pixabay
- API Key o Token de FreeSound
- Credenciales OAuth para futura subida a YouTube

## 🧪 Instalación

```bash
git clone https://github.com/TU_USUARIO/relax_gen.git
cd relax_gen
python -m venv venv
venv\\Scripts\\activate  # O source venv/bin/activate en Mac/Linux
pip install -r requirements.txt

## Crea un archivo .env con tus claves:

ELEVENLABS_API_KEY=tu_clave
PIXABAY_API_KEY=tu_clave
FREESOUND_CLIENT_ID=tu_id
FREESOUND_CLIENT_SECRET=tu_secreto

▶️ Uso

python main.py

El vídeo final se generará como: video/final.mp4 🎬
🔜 Próximamente

    ☁️ Subida automática a YouTube

    🪄 Opciones de personalización: duración, temas, idiomas

    💡 Interfaz gráfica (GUI) en fase beta

    Creado con ❤️ por alguien que quiere relajarse y automatizarlo todo.