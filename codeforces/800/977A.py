import sys

n, k = list(map(int, sys.stdin.readline().split()))

for i in range(k):
    n = n-1 if n%10 != 0 else n//10
print(n)