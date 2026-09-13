# 1. 프로젝트 개요
> 본 프로젝트는 파이썬을 활용한 깃허브 자동 커밋메시지 생성기 입니다.

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
```