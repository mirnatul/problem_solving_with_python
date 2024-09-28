import sys

n, k = list(map(int, sys.stdin.readline().split()))
time_remain = 240-k

p_time = 0
solve = 0
for i in range(n):
    if time_remain >= p_time+5:
        solve += 1
        p_time += 5
        time_remain -= p_time
    else:
        break

print(solve)
