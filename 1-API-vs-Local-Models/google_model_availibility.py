import os

import google.genai as genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

models = client.models.list()

for m in models:
    actions = getattr(m, "supported_actions", []) or []
    if "generateContent" in actions:
        print("Valid:", m.name)
    else:
        print("SKIP:", m.name, "-> supports:", actions)