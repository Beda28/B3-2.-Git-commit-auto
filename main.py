import argparse

from prompt import getPrompt
from util   import copy

parser = argparse.ArgumentParser()

parser.add_argument("command",       choices=["commit", "pr"])
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