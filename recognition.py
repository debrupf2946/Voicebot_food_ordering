import requests

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("/Users/debruppaul/PycharmProjects/Jarvis_ai/output/recorded_audio_0.wav")
print(output)