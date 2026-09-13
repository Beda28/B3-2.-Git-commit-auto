from google import genai
from dotenv import load_dotenv

import subprocess
import os

load_dotenv()

key    = os.getenv('API_KEY')
client = genai.Client(api_key=key)

status = subprocess.run("git status", shell=True, capture_output=True, text=True, encoding='utf-8')
diff   = subprocess.run("git diff",   shell=True, capture_output=True, text=True, encoding='utf-8')

prompt = f"""
    다음은 git status, git diff 명령어의 실행 결과이다. 
    해당 결과를 보고, 변경사항 요약을 진행해보라. 
    status: {status.stdout} / diff: {diff.stdout}  """

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt
)
print(interaction.output_text)
