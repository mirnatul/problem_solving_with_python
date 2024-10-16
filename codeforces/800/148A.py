import sys

k = int(sys.stdin.readline().strip())
l = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
d = int(sys.stdin.readline().strip())

count = 0
for i in range(1, d+1):
    if i%k == 0 or i%l == 0 or i%m == 0 or i%n == 0:
        count += 1

print(count)