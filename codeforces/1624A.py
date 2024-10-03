import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    array = list(map(int, sys.stdin.readline().split()))
    maximum = max(array)
    minimum = min(array)
    print(maximum-minimum)