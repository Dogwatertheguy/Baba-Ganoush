import requests

class OllamaManager:
    def __init__(self, model="gemma4:31b-cloud"):
        self.model = model
        self.chat_history = []

    def chat_with_history(self, user_input):
        self.chat_history.append({"role": "user", "content": user_input})

        try:
            response = requests.post(
                "http://localhost:11434/api/chat",
                json={
                    "model": self.model,
                    "messages": self.chat_history,
                    "stream": False
                }
            )

            result = response.json()

            # =========================
            # SAFE CHECKS (IMPORTANT)
            # =========================
            if "message" not in result:
                print("[red]Ollama error response:", result)
                return "Sorry, something went wrong with the model."

            assistant_message = result["message"].get("content", "")

            if not assistant_message:
                return "Sorry, I got an empty response."

            self.chat_history.append({
                "role": "assistant",
                "content": assistant_message
            })

            return assistant_message

        except Exception as e:
            print("[red]Ollama request failed:", e)
            return "Ollama is not responding right now."