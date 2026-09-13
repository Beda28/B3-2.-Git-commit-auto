import subprocess

def copy(result: str):
    print('\n커밋 메시지를 복사하시겠습니까?')
    if input("복사하시려면 1을 입력해주세요 : ") == "1":
        subprocess.run(
            "clip",
            input = result,
            text  = True,
            shell = True
        )
        print("클립보드에 복사되었습니다!")
    else: print("프로그램 종료")