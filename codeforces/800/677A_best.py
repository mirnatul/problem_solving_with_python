import sys

n, h = map(int, sys.stdin.readline().split())  # No need for list() around map

min_width = 0
for i in map(int, sys.stdin.readline().split()):
    min_width += 1 if i <= h else 2  # Calculate width directly

print(min_width)
