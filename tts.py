# tts.py
import edge_tts
import asyncio
import tempfile

VOICE = "en-IN-NeerjaNeural"

def ayra_speak_bytes(text: str) -> bytes:
    async def _gen(path):
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(path)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        path = f.name

    asyncio.run(_gen(path))

    with open(path, "rb") as audio:
        return audio.read()