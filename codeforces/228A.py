import sys

s = set(map(int, sys.stdin.readline().split()))
length = len(s)

print(4-length)