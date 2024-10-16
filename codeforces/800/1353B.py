import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    a = sorted(list(map(int, sys.stdin.readline().split())))
    b = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

    for i in range(k):
        if b[i]<a[i]:
            break
        else:
            a[i] = b[i]
    print(sum(a))