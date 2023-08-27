import pyaudio
from pydub import AudioSegment
from io import BytesIO
import requests
import os
from dotenv import load_dotenv

load_dotenv()

voice_id = os.getenv("xi-voice-id")
api_key = os.getenv("xi-api-key")

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice_id + "/stream"
headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": api_key
}

def play_text_as_audio(text):
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(url, json=data, headers=headers)
    audio_bytes = BytesIO(response.content)

    audio_segment = AudioSegment.from_mp3(audio_bytes)
    audio_segment.export("output.wav", format="wav")  # Convert to WAV for compatibility

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(audio_segment.sample_width),
                    channels=audio_segment.channels,
                    rate=audio_segment.frame_rate,
                    output=True)

    chunk_size = CHUNK_SIZE
    offset = 0

    while offset < len(audio_segment):
        chunk = audio_segment[offset:offset + chunk_size]
        offset += chunk_size
        stream.write(chunk.raw_data)

    stream.stop_stream()
    stream.close()
    p.terminate()
