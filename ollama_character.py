import time
import keyboard
import sys
sys.stdout.reconfigure(encoding="utf-8")
import unicodedata
from rich import print

from whisper_speech_to_text import transcribe
from ollama_manager import OllamaManager
from piper_tts_manager import PiperTTSManager
from audio_player import AudioManager


sys.stdout.reconfigure(encoding="utf-8")


BACKUP_FILE = "ChatHistoryBackup.txt"


ollama_manager = OllamaManager(model="gemma4:31b-cloud")  # change model if needed hehe
piper_manager = PiperTTSManager(
    model_path="en_GB-northern_english_male-medium.onnx",
    config_path="en_GB-northern_english_male-medium.onnx.json"
)
audio_manager = AudioManager()


FIRST_SYSTEM_MESSAGE = {
    "role": "system",
    "content": '''
You are Baba Ganoush, Fun man with a wacky personality.

While responding as Baba, you must obey the following rules: 
1) Provide short responses, about 1 paragraph max. 
2) Always stay in character, no matter what. 
3) Keep your answers limited to just a few sentences.
'''
}

ollama_manager.chat_history.append(FIRST_SYSTEM_MESSAGE)

def clean_text(text: str) -> str:
    """Prevents Unicode crashes from weird AI characters"""
    return unicodedata.normalize("NFKD", text)

def wait_for_key(key="-"):
    """Debounced key press detection"""
    while True:
        if keyboard.is_pressed(key):
            time.sleep(0.3)  # debounce
            return
        time.sleep(0.05)


print("[green]Press 'F4' to start speaking...")

while True:
    wait_for_key("f4")

    print("[green]Listening to microphone...")

    mic_result = transcribe()

    if not mic_result or mic_result.strip() == "":
        print("[red]No speech detected!")
        continue

    mic_result = clean_text(mic_result)


    response = ollama_manager.chat_with_history(mic_result)
    response = clean_text(response)


    with open(BACKUP_FILE, "w", encoding="utf-8") as file:
        file.write(str(ollama_manager.chat_history))


    audio_file = piper_manager.text_to_audio(response)

    audio_manager.play_audio(audio_file, True, True, True)






    print("[green]Done! Press '-' again.\n")
