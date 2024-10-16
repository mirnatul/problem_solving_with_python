import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    if n%3==0 or n%3==1:
        b = n//3
        a = n-(b*2)
    else:
        b = n//3+1
        a = n-b*2
    print(a, b)