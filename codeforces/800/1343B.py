import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    sumN = (n//2)*((n//2)+1)
    if n%4==0:
        print("YES")
        for i in range(1, n+1):
            if i%2==0:
                sys.stdout.write(f"{i} ")
        count = 0
        for i in range(n-1):
            if i%2!=0:
                count += i
                sys.stdout.write(f"{i} ")
        sys.stdout.write(f"{sumN-count}\n")
    else:
        print("NO")