'''
from whisper import pipe
t=pipe("/Users/debruppaul/PycharmProjects/Jarvis_ai/output/recorded_audio_1.wav")
print(t['text'])
'''

import requests
from audio import record_audio,get_next_filename
output_directory="output"

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

#output = query("/Users/debruppaul/PycharmProjects/Jarvis_ai/"+record_audio(output_directory,record_seconds=5))
#print(output)
def speech_recog():
    return query("/Users/debruppaul/PycharmProjects/Jarvis_ai/"+record_audio(output_directory,record_seconds=5))["text"]