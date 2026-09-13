from google import genai
from dotenv import load_dotenv

load_dotenv()

import os

key    = os.getenv('API_KEY')
client = genai.Client(api_key=key)

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="한국어로 인사해봐"
)
print(interaction.output_text)