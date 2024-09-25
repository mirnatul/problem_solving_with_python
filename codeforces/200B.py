import sys

n = int(sys.stdin.readline().strip())
i = list(map(int, sys.stdin.readline().split()))

ans = sum(i)/n
print(ans)