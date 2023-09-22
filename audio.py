import pyaudio
import wave
import os


def get_next_filename(directory):
    # Find the highest numbered file in the directory
    existing_files = [f for f in os.listdir(directory) if f.startswith("recorded_audio_")]
    if not existing_files:
        return "recorded_audio_0.wav"
    else:
        highest_number = max([int(file.split("_")[2].split(".")[0]) for file in existing_files])
        return f"recorded_audio_{highest_number + 1}.wav"


def record_audio(output_directory, record_seconds=5):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()

    try:
        filename = get_next_filename(output_directory)
        FILENAME = os.path.join(output_directory, filename)

        # Start recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=1024)
        print("Recording...")

        frames = []

        for _ in range(0, int(RATE / 1024 * record_seconds)):
            data = stream.read(1024)
            frames.append(data)

        # Stop recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save the recorded audio to the generated filename
        with wave.open(FILENAME, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

        print(f"Audio recorded and saved to {FILENAME}")

        return FILENAME
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

'''
# Function to process the recorded audio file
def process_audio(audio_filename):
    if audio_filename:
        print(f"Processing audio file: {audio_filename}")
        # Your audio processing code goes here
    else:
        print("No audio file to process.")
'''

if __name__ == "__main__":
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)

    audio_filename = record_audio(output_directory, record_seconds=5)
   # process_audio(audio_filename)
