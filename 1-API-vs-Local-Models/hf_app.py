import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

prompt = "What is the currency of India?"

client = InferenceClient(
    api_key=os.getenv("HUGGINGFACE_API_KEY"),
    provider="auto"
)

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)