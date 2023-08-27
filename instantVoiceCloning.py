# Load sample files
# Use eleven labs api syncronously to clone steve's voice

import os
import requests
from dotenv import load_dotenv

load_dotenv()
# Get api key from .env file
api_key = os.getenv("xi-api-key")

# Clone Steve Jobs voice
url = "https://api.elevenlabs.io/v1/voices/add"

headers = {
  "Accept": "application/json",
  "xi-api-key": api_key
}

data = {
    'name': 'Voice name',
    'labels': '{"accent": "American"}',
    'description': 'Similar replica to Steve Jobs voice'
}

files = [
    ('files', ('./samples/016-TheThirdCategoryOfDevice.mp3', open('./samples/016-TheThirdCategoryOfDevice.mp3', 'rb'), 'audio/mpeg')),
    ('files', ('./samples/019-ImLucky.mp3', open('./samples/019-ImLucky.mp3', 'rb'), 'audio/mpeg')),
    ('files', ('./samples/022-StartedPixarIn1986.mp3', open('./samples/022-StartedPixarIn1986.mp3', 'rb'), 'audio/mpeg')),
    ('files', ('./samples/023-BeatlesAsBusinessModel.mp3', open('./samples/023-BeatlesAsBusinessModel.mp3', 'rb'), 'audio/mpeg'))
]

response = requests.post(url, headers=headers, data=data, files=files)
print(response.text)

