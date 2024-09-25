import sys
import math

n = int(sys.stdin.readline().strip())
preAns = math.ceil(n/2)

print(preAns) if n%2 == 0 else print(-preAns)
