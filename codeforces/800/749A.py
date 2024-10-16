import sys

n = int(sys.stdin.readline().strip())
if n%2==0:
    print(n//2)
    print("2 "*(n//2))
else:
    print(n//2)
    sys.stdout.write("2 "*((n-2)//2))
    sys.stdout.write("3")