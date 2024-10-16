import sys

ui = int(sys.stdin.readline().strip())
ui2 = list(map(int, sys.stdin.readline().split()))

print("HARD") if 1 in ui2 else print("EASY")
