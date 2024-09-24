import sys

n, h = list(map(int, sys.stdin.readline().split()))

all_fnd = list(map(int, sys.stdin.readline().split()))

min_width = sum(1 if i<=h else 2 for i in all_fnd)

print(min_width)
