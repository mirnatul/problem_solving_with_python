import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    a, b, c = map(int, sys.stdin.readline().split())
    if a==b:
        print(c)
    elif a==c:
        print(b)
    else:
        print(a)
