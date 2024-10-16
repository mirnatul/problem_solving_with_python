import sys

k, n, w = list(map(int, sys.stdin.readline().split()))

sum = 0
for i in range(1, w+1):
    sum += i*k

if sum-n>0:
    ans = sum-n
else:
    ans = 0

print(ans)