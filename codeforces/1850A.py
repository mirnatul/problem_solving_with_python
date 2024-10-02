import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    a, b, c = map(int, sys.stdin.readline().split())
    if a+b>=10 or b+c>=10 or a+c>=10:
        print("YES")
    else:
        print("NO")