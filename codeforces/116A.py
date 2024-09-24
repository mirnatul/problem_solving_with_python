import sys

n = int(sys.stdin.readline().strip())

initial = max_passenger = 0
for i in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    initial = initial + (b - a)
    max_passenger = max(max_passenger, initial)

print(max_passenger)
