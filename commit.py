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
    해당 결과를 보고, 커밋 메시지를 작성하라.
    status: {status.stdout} / diff: {diff.stdout}
    
    메시지 작성 규칙은 다음을 따른다.
    1. 커밋 메시지는 변경 사항 요약을 기반으로 생성되어야 한다.
    2. 출력 결과에는 커밋 제목 1줄이 필수로 포함되어야 한다.
    3. 커밋 메시지는 50자 이내를 권장하며, 최대 72자로 제한한다.

    또한 답변 작성시 다음을 따른다.
    1. 필요없는 이모지/설명은 사용하지 않는다.
    2. 실제와 다른 내용을 임의로 넣지 않는다.
    3. 간략하게, 한눈에 보일 수 있도록 핵심적인 요소들만 추려서 답변하도록 한다.
    4. 파일명을 설명할 때 강조하지 않는다."""

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt
)
print(interaction.output_text)
