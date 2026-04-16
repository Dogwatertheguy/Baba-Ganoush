# Baba Ganoush
Simple app that lets you have a verbal conversation with Ollama AI Models.
Original Babagaboosh Code Written by [DougDoug.](https://github.com/DougDougGithub/Babagaboosh) 

## P.S. if the guide sounds a little too similar to the Original Guide, That's because the Open Source modules that replace ChatGPT-4o, Microsoft Azure, and Elevenlabs do the same exact goddamn thing! Don't kill me please :3
e
## SETUP:
1) This was written in Python 3.13.0.  install it here: https://www.python.org/downloads/release/python-3130/

2)  Create the environment with either generate-enviornment.sh(Linux) or generate-enviornment.bat(Windows), activate it using `.venv\Scripts\activate`(Windows) or `source .venv/bin/activate`(Linux) and run `pip install -r requirements.txt` to install all modules.

3) There are certain packages left out of the requirements, specifically `torch`, `torchvision`, `torchaudio`, and `faster-whisper` for customization on whether you want GPU or CPU power for Whisper. So, install them with `pip install faster-whisper torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121` (This is a GPU based version of torch, which is used in the script for Whisper by default. If you wish to use it with CPU power, replace `from faster_whisper import WhisperModel` in whisper_speech_to_text.py with
```python
from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu")
```
then, install torch using this command instead
`pip install torch --index-url https://download.pytorch.org/whl/cpu`)

4) This app uses Ollama as opposed to OpenAI's ChatGPT. Install it from here https://ollama.com/

5) Piper-TTS is also required and is installed automatically, however, it does not include voices automatically but you can download voices from the website here: https://huggingface.co/rhasspy/piper-voices/tree/main .
   After that, replace the values of `model_path` and `config_path`in `piper_manager` in ollama_character.py. For more info on the documentation and stuff heres the link:  https://github.com/OHF-Voice/piper1-gpl

## Using the App

1) Run `ollama_character.py'

2) Once it's running, press F4 to start the conversation, and Whisperd will listen to your microphone and transcribe it into text.

3) Once you're done talking, press P. Then the code will send all of the recorded text to the Ai. Note that you should wait a second or two after you're done talking before pressing P so that Whisper has enough time to process all of the audio.

4) Wait a few seconds for Ollama to generate a response and for PiperTTS to turn that response into audio. Once it's done playing the response, you can press F4 to start the loop again and continue the conversation.
