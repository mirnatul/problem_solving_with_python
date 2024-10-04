import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    minimum = min(arr)
    ans = sum(i-minimum for i in arr)
    print(ans)