import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    a, b, c = map(int, sys.stdin.readline().split())
    if a+b==c:
        sys.stdout.write(f"+\n")
    else:
        sys.stdout.write(f"-\n")