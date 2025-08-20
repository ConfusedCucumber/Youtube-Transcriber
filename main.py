# 1. Lépés: Beimportáljuk a szükséges osztályt.
from youtube_transcript_api import YouTubeTranscriptApi

# 2. Lépés: Add meg a YouTube videó azonosítóját.
video_id = 'dQw4w9WgXcQ'

try:
    # 3. Lépés: Létrehozzuk az API "példányát". Ez az új, fontos lépés!
    api = YouTubeTranscriptApi()

    # 4. Lépés: A "fetch" metódussal letöltjük az átiratot a példányon keresztül.
    transcript_list = api.fetch(video_id, languages=['hu', 'en'])

    # 5. Lépés: Létrehozunk egy listát, amibe csak a szövegrészeket gyűjtjük.
    text_parts = []
    for item in transcript_list:
        text_parts.append(item.text)

    # 6. Lépés: Összefűzzük a szövegrészeket.
    final_text = " ".join(text_parts)

    # 7. Lépés: Kiírjuk az eredményt.
    print(final_text)

except Exception as e:
    print(f"Hiba történt: {e}")
    print("Lehet, hogy ehhez a videóhoz nincs elérhető átirat, vagy rossz az azonosító.")
    print(video_id)