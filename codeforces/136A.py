import sys

inp = int(sys.stdin.readline().strip())

fnd = list(map(int, sys.stdin.readline().split()))

fndLen = len(fnd)
for i in range(fndLen):
    sys.stdout.write(f"{fnd.index(i+1) + 1} ")
