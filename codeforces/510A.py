import sys

n, m = map(int, sys.stdin.readline().split())

j = 1
for i in range(1, n+1):
    if i%2 != 0:
            sys.stdout.write("".join(["#"]*(m)))
            sys.stdout.write("\n")
    else:
        if j%4 == 0:
            sys.stdout.write("#"+"".join(["."]*(m-1)))
            sys.stdout.write("\n")
        else:
            sys.stdout.write("".join(["."]*(m-1))+"#")
            sys.stdout.write("\n")
    j += 1
