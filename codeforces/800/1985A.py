import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    a, b = map(str, sys.stdin.readline().split())
    new_a = b[0]+a[1:len(a)]
    new_b = a[0]+b[1:len(b)]
    print(new_a, new_b)