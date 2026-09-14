# 1. 프로젝트 개요
> 본 프로젝트는 파이썬을 활용한 깃허브 자동 커밋메시지 생성기 입니다.
> AI API는 GEMINI 기준으로 작업했습니다.

# 2. 프로젝트 세팅
```python
# requirements.txt 파일에 기재되어있는 패키지들을 한꺼번에 설치
pip install -r requirements.txt
```

```bash
# 환경변수 설정
# .env_sample => .env 이름 변경
API_KEY=대충_API_키  # API 키 기입
```

# 3. 사용법
```bash
python3 main.py commit  # 변경사항 기준으로 커밋 메시지 초안 생성
python3 main.py pr      # 변경사항 기준으로 pr 초안 생성
```

```bash
# option
--model [Gemini_모델명]             # 지정된 모델로 메시지를 생성합니다.
--temperature [가중치(0.1 ~ 1.0)]   # 가중치가 높을수록 실제보다 부풀려 작성합니다.
--max-tokens [토큰량]               # 생성할 응답의 최대 토큰량을 설정합니다.
--safe-mode                        # Gemini API에게 전달하는 Git diff의 범위를 제한합니다.
```

# 4. 생성 결과
```bash
python .\main.py commit  
refactor: commit 및 PR 프롬프트 작성 규칙 개선 및 문서 업데이트

python .\main.py commit --temperature 0.7 --max-tokens 1500
refactor: commit 및 PR 프롬프트 작성 규칙 개선

python .\main.py commit --max-tokens 1500                  
refactor: prompt.py 프롬프트 지침 개선 및 README 예시 업데이트
---
python .\main.py pr    
test.py 파일 추가

Why
- test.py 파일이 새롭게 추가됨

What
- 신규 파일 test.py 추가

How To Test
- git status 명령어로 test.py 파일 포함 여부 확인
---
python .\main.py pr --max-tokens 500
docs: README.md에 pr 명령어 실행 예시 추가

Why
- pr 명령어
결과 메시지가 제대로 출력되지 않았습니다.
---
python .\main.py pr --temperature 0.8
docs: README.md에 pr 명령어 실행 예시 추가 및 test.py 파일 추가

Why
- pr 명령어 사용 예시를 README.md 문서에 구체적으로 안내하기 위함

What
- README.md에 pr 명령어 및 옵션 실행 예시 추가
- 신규 파일 test.py 추가

How To Test
- README.md 파일 내용 및 예시 구문 확인
- git status 명령어로 test.py 파일 추가 상태 확인
```

# 5. 출력 검증
## Commit 검증
- 결과가 비어 있지 않은지 확인
- 한 줄로 작성되었는지 확인
- 최대 72자인지 확인

## PR 검증
- 결과가 비어 있지 않은지 확인
- 제목이 최대 80자인지 확인
- Why 섹션 존재 여부 확인
- What 섹션 존재 여부 확인
- How To Test 섹션 존재 여부 확인
- 각 섹션에 최소 하나의 bullet이 존재하는지 확인

# 6. 주의 사항
## API Key 보안
- API Key는 .env 파일에 저장하며, Git 저장소에 업로드 하지 않도록 합니다.