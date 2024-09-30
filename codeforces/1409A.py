import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    value = abs(a-b)
    if a == b:
        ans = 0
    else:
        ans = (value//10) if value%10==0 else (value//10 +1)
    print(ans)