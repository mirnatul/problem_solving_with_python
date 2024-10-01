import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    num = int(sys.stdin.readline().strip())
    if num <= 1399:
        print("Division 4")
    elif num <= 1599:
        print("Division 3")
    elif num <= 1899:
        print("Division 2")
    else:
        print("Division 1")