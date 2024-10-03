import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    a, b, c = map(int, sys.stdin.readline().split())
    if c>b and b>a:
        print("STAIR")
    elif b>a and b>c:
        print("PEAK")
    else:
        print("NONE")