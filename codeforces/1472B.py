import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    array = list(map(int, sys.stdin.readline().split()))
    sumOfTwo = sum(2 for i in array if i==2)
    sumOfOne = sum(1 for i in array if i==1)
    if sumOfTwo%4==0 and sumOfOne%2==0:
        print("YES")
    elif sumOfTwo%4!=0 and sumOfOne>=2 and sumOfOne%2==0:
        print("YES")
    else:
        print("NO")
