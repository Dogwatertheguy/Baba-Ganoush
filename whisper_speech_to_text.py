import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import tempfile
import scipy.io.wavfile as wav

# Load model once
model = WhisperModel("base", compute_type="int8")  # or "small", "medium"

def record_audio(duration=5, samplerate=16000):
    print("Recording...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    print("Done recording")

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