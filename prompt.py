from google import genai
from dotenv import load_dotenv

import subprocess
import os

load_dotenv()

key    = os.getenv('API_KEY')
client = genai.Client(api_key=key)

def getPrompt(rtype: str):
    status = subprocess.run("git status", shell=True, capture_output=True, text=True, encoding='utf-8')
    diff   = subprocess.run("git diff",   shell=True, capture_output=True, text=True, encoding='utf-8')

    prompt = f"""
            다음은 git status, git diff 명령어의 실행 결과이다. 
            해당 결과를 보고, 커밋 메시지를 작성하라.
            status: {status.stdout} / diff: {diff.stdout}"""

    if rtype == "commit":
        prompt += f"""
            메시지 작성 규칙은 다음을 따른다.
            1. 커밋 메시지는 변경 사항 요약을 기반으로 생성되어야 한다.
            2. 출력 결과에는 커밋 제목 1줄이 필수로 포함되어야 한다.
            3. 커밋 메시지는 50자 이내를 권장하며, 최대 72자로 제한한다."""
    elif rtype == "pr":
        prompt += f"""
            작성 규칙은 다음을 따른다.
            1. PR 본문은 템플릿 구조를 가져야 하며, 아래 섹션 헤더를 포함해야 한다.
                - Why         (변경 배경)
                - What        (핵심 변경 사항)
                - How To Test (테스트 방법)
            2. 각 섹션에는 최소 1개 이상의 불릿이 포함되어야 한다.
            3. PR 제목은 1줄로 출력하며, PR 본문과 함께 확인할 수 있어야 한다.
            4. 사용자가 결과를 검토할 수 있도록 구분선/헤더 등으로 구역을 나누어 표시하도록 한다.
            5. PR 제목은 최대 80자로 제한한다."""
        
    prompt += f"""
            또한 답변 작성시 다음을 따른다.
            1. 필요없는 이모지/설명은 사용하지 않는다.
            2. 실제와 다른 내용을 임의로 넣지 않는다.
            3. 간략하게, 한눈에 보일 수 있도록 핵심적인 요소들만 추려서 답변하도록 한다.
            4. 파일명을 설명할 때 강조하지 않는다."""
        
    result = client.interactions.create(model="gemini-3.6-flash", input=prompt)
    return result.output_text