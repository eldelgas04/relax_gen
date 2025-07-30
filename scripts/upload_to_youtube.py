import os
import pickle
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

# Constantes
CLIENT_SECRETS_FILE = "client_secret.json"
CREDENTIALS_PICKLE = "token.pickle"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
VIDEO_FILE = "video/final.mp4"
METADATA_FILE = "video/metadata.json"

# Cargar título y descripción generados
if os.path.exists(METADATA_FILE):
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        metadata = json.load(f)
    TITLE = metadata.get("title", "Vídeo relajante automático")
    DESCRIPTION = metadata.get("description", "")
else:
    TITLE = "🌿 Relajación profunda con música suave"
    DESCRIPTION = "Disfruta de unos minutos de calma con este vídeo."

TAGS = ["relax", "meditación", "naturaleza", "calma", "sonidos relajantes"]
CATEGORY_ID = "22"  # People & Blogs
PRIVACY = "unlisted"  # Puedes poner "public" o "private"

def authenticate_youtube():
    creds = None
    if os.path.exists(CREDENTIALS_PICKLE):
        with open(CREDENTIALS_PICKLE, "rb") as token:
            creds = pickle.load(token)

    if not creds:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)

        with open(CREDENTIALS_PICKLE, "wb") as token:
            pickle.dump(creds, token)

    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)
    return youtube

def upload_video():
    youtube = authenticate_youtube()

    request_body = {
        "snippet": {
            "title": TITLE,
            "description": DESCRIPTION,
            "tags": TAGS,
            "categoryId": CATEGORY_ID
        },
        "status": {
            "privacyStatus": PRIVACY
        }
    }

    media = MediaFileUpload(VIDEO_FILE, mimetype="video/mp4", resumable=True)

    print("📤 Subiendo vídeo a YouTube...")
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )
    response = request.execute()

    print("✅ Vídeo subido con ID:", response["id"])
    print("📺 Ver en: https://www.youtube.com/watch?v=" + response["id"])

if __name__ == "__main__":
    upload_video()
