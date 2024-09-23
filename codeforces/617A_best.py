import sys

ui = int(sys.stdin.readline().strip())

# Calculate the minimum steps by dividing by 5, and if there's any remainder, add 1
steps = (ui + 4) // 5

print(steps)
