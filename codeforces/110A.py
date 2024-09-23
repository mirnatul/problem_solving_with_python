import sys

ui = list(str(sys.stdin.readline().strip()))

total = sum(1 for i in ui if i == "4" or i == "7")

print("YES") if total == 7 or total == 4 else print("NO")
