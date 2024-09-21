import sys

# Read input data in a single go
n, k = map(int, sys.stdin.readline().split())
participants = list(map(int, sys.stdin.readline().split()))

# Threshold is the score of the k-th participant
threshold = participants[k-1]

# Count participants with score >= threshold and score > 0
passed = sum(1 for i in participants if i >= threshold and i > 0)

sys.stdout.write(f"{passed}\n")
