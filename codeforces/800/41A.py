import sys

ui1 = sys.stdin.readline().strip()
ui2 = sys.stdin.readline().strip()

print("YES") if list(reversed(ui1)) == list(ui2) else print("NO")
