import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    n1 = int(sys.stdin.readline().strip())
    if n1%2 == 0:
        print((n1//2) - 1)
    elif n1%2 != 0:
        print(n1//2)
