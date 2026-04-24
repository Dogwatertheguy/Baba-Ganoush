import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import tempfile
import scipy.io.wavfile as wav
import keyboard  # pip install keyboard

# Load model once
model = WhisperModel("base", compute_type="int8")

def record_audio(samplerate=16000):
    print("Recording... Press 'P' to stop.")

    recording = []
    stream = sd.InputStream(samplerate=samplerate, channels=1, dtype='int16')
    stream.start()

    try:
        while True:
            data, _ = stream.read(1024)
            recording.append(data)

            if keyboard.is_pressed('p'):
                print("Stopping recording...")
                break
    finally:
        stream.stop()
        stream.close()

    audio = np.concatenate(recording, axis=0)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wav.write(temp_file.name, samplerate, audio)

    return temp_file.name

def transcribe():
    audio_path = record_audio()

    segments, _ = model.transcribe(audio_path)

    text = ""
    for segment in segments:
        text += segment.text

    print("Transcribed:", text)
    return text
