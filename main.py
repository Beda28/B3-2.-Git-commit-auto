import argparse

from prompt import getPrompt
from util   import copy

parser = argparse.ArgumentParser()

parser.add_argument(
    "command",
    choices=["commit", "pr"],
    help="실행할 명령어"
)

args = parser.parse_args()

if   args.command == "commit": result = getPrompt("commit")
elif args.command == "pr":     result = getPrompt("pr")

print(result)
copy(result)