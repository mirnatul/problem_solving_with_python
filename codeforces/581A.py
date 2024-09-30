import sys

a, b = map(int, sys.stdin.readline().split())

x = a if a<b else b
y = (a + b - (x*2)) // 2

print(x, y)