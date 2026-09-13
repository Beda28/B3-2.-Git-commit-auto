import argparse

from prompt    import getPrompt
from util      import copy
from decorator import handle_error

@handle_error
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("command",       choices=["commit", "pr"], help="실행할 명령어")
    parser.add_argument("--model",       default="gemini-3.6-flash")
    parser.add_argument("--temperature", default=0.3, type=float)
    parser.add_argument("--max-tokens",  default=500, type=int)

    args = parser.parse_args()

    result = getPrompt(
        args.command, 
        args.model,
        args.temperature, 
        args.max_tokens )

    print(result)
    copy(result)

if __name__ == "__main__":
    main()