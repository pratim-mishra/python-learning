import os

import google.genai as genai
from openai import OpenAI
from huggingface_hub import InferenceClient

class LLMProvider:
    def __init__(self, config: dict):
        self.provider = config.get("provider")
        self.model = config.get("models", {}).get(self.provider)

        if str(self.provider).lower() == "openai":
            key = os.getenv("OPENAI_API_KEY")
            if not key:
                raise ValueError("OPENAI_API_KEY env variable was not set.")
            self.client = OpenAI(api_key=key)
        elif str(self.provider).lower() == "gemini":
            key = os.getenv("GEMINI_API_KEY")
            if not key:
                raise ValueError("GEMINI_API_KEY env variable was not set.")
            self.client = genai.Client(api_key=key)
        elif str(self.provider).lower() == "huggingface":
            key = os.getenv("HUGGINGFACE_API_KEY")
            if not key:
                raise ValueError("HUGGINGFACE_API_KEY env variable was not set.")
            self.client = InferenceClient(
                api_key = key,
                provider = "auto"
                )
        else:
            raise ValueError(f"Unsupported Provider: {self.provider}")
        print(f"{self.provider.title()} client initiated successfully.✅")

    def chat(self, user_message:str) -> str:
        try:
            if str(self.provider).lower() == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": user_message}]
                )
                return response.choices[0].message.content.strip()
            elif str(self.provider).lower() == "gemini":
                response = self.client.models.generate_content(
                    model = self.model,
                    contents=[
                        genai.types.Content(
                            role="user",
                            parts=[genai.types.Part.from_text(text=user_message)]
                        )
                    ]
                )
                return response.text.strip()
            elif str(self.provider).lower() == "huggingface":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": user_message}]
                )
                return response.choices[0].message.content.strip()
            
        except Exception as e:
            raise Exception(f"Error in {self.provider} chat: {str(e)}")