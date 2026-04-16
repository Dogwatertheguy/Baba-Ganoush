import subprocess
import tempfile
import os

class PiperTTSManager:
    def __init__(self, model_path, config_path):
        self.model_path = model_path
        self.config_path = config_path

    def text_to_audio(self, text):
        output_file = tempfile.mktemp(suffix=".wav")

        cmd = [
            "piper",
            "--model", self.model_path,
            "--config", self.config_path,
            "--output_file", output_file
        ]

        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            text=True
        )

        process.communicate(input=text)

        return output_file