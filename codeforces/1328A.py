import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a%b == 0:
        print(0)
    else:
        print(b*(a//b+1) - a)
