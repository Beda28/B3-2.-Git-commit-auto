import subprocess
from functools    import wraps
from google.genai import errors

def handle_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:   return func(*args, **kwargs)
        except errors.APIError               as e: print(f"GEMINI API 오류: {e}")
        except errors.ServerError            as e: print(f"GEMINI 서버 오류: {e}")
        except subprocess.CalledProcessError as e: print(f"명령 실행을 실패했습니다.: {e}")
        except EnvironmentError              as e: print(f"API_KEY가 설정되지 않았습니다.")
        except Exception                     as e: print(f"예상하지 못한 오류가 발생했습니다.: {e}")

    return wrapper