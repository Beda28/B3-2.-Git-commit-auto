import subprocess

def copy(result: str):
    print('\n결과 메시지를 복사하시겠습니까?')

    if input("복사하시려면 1을 입력해주세요 : ") == "1":
        subprocess.run(
            "clip",
            input = result,
            text  = True,
            shell = True
        )
        print("클립보드에 복사되었습니다!")
    else: print("프로그램 종료")

def safe_diff(diff: str):
    lines      = diff.splitlines()
    result     = []
    file_count = 0

    for line in lines:
        if line.startswith("diff --git"):
            file_count += 1
            if file_count > 10: break

        result.append(line)
        if len(result) >= 200: break

    return "\n".join(result)