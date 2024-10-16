import math
t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    
    if n <= 2:
        print(1)
    else:
        floors = math.ceil((n - 2) / x)
        print(floors + 1)
