import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    x, y, n = map(int, sys.stdin.readline().split())
    ans = ((n-y)//x)*x+y
    print(ans)
