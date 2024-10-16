import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    h, m = map(int, sys.stdin.readline().split())
    remain = (23-h)*60 + (60-m)
    print(remain)