import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    a = sys.stdin.readline().strip()
    b = ""
    for i in range(len(a)-1):
        if i%2 == 0:
            b += a[i]
    print(b+a[-1])