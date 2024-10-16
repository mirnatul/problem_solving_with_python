import sys

n = int(sys.stdin.readline().strip())
word = set(map(str, sys.stdin.readline().strip().lower()))

print("YES") if len(word) == 26 else print("NO")