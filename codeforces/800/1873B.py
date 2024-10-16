import sys
import math
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    # instead of sorting and updating use min method
    arr = sorted(list(map(int, sys.stdin.readline().split())))
    arr[0] = arr[0]+1
    print(math.prod(arr))
