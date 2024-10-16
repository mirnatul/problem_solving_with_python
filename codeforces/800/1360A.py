import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    ab = sorted(map(int, sys.stdin.readline().split()))
    if ab[0]+ab[0] >= ab[1]:
        print((ab[0]+ab[0])**2)
    else:
        print((ab[1])**2)