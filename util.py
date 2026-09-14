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

def validate_commit(result: str):
    result = result.strip()

    if not result      : return False
    if "\n" in result  : return False
    if len(result) > 72: return False
    return True

def validate_pr(result: str):
    result   = result.strip()
    if not result: return False

    lines    = result.splitlines()
    sections = [
        "Why",
        "What",
        "How To Test"
    ]
    if len(lines[0]) > 80: return False

    for sec in sections:
        if sec not in result:
            return False

    for i, line in enumerate(lines):
        if any(section in line for section in sections):
            if i + 1 >= len(lines): 
                return False
            if not lines[i + 1].strip().startswith(("-", "*")):
                return False

    return True