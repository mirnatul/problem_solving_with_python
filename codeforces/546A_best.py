import sys

k, n, w = map(int, sys.stdin.readline().split())

# Use the arithmetic series formula
total_cost = k * w * (w + 1) // 2

# Calculate the amount the soldier needs to borrow
ans = max(0, total_cost - n)

print(ans)
