import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    array = list(map(int, sys.stdin.readline().split()))
    sumOfEven = sum(1 for i in array if i%2==0)
    if (n%2 == 0 and sumOfEven == n//2) or (n%2!=0 and sumOfEven == (n//2)+1):
        count = 0
        for i in range(n):
            if i%2==0 and array[i]%2!=0:
                count += 1
        print(count)
    else:
        print(-1)