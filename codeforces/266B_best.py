import sys

n, t = map(int, sys.stdin.readline().split())
queue = list(sys.stdin.readline().strip())  # Convert to list for mutability

for _ in range(t):
    i = 0
    while i < n - 1:
        if queue[i] == 'B' and queue[i + 1] == 'G':
            # Swap 'B' and 'G'
            queue[i], queue[i + 1] = queue[i + 1], queue[i]
            i += 1  # Skip next position after a swap
        i += 1

print("".join(queue))
