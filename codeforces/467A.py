import sys

ui = int(sys.stdin.readline().strip())

count = 0
for i in range(ui):
    p, q = list(map(int, sys.stdin.readline().split()))
    if q-p>=2:
        count += 1

print(count)