import sys

n = int(sys.stdin.readline().strip())
points = list(map(int, sys.stdin.readline().split()))

best = points[0]
worst = points[0]
count = 0
for i in range(1, n):
    if points[i] > best:
        count += 1
        best = points[i]
    elif points[i] < worst:
        count += 1
        worst = points[i]
print(count)