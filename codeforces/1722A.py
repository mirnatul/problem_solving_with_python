import sys

t = int(sys.stdin.readline().strip())
constantSet = set("Timur")

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    string = sys.stdin.readline().strip()
    stringSet = set(string)
    if constantSet == stringSet and len(constantSet)==len(string):
        print("YES")
    else:
        print("NO")