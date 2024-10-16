import sys

user_input = list(map(int, sys.stdin.readline().split("+")))
user_input.sort()

ans = "+".join(map(str, user_input))
print(ans)
