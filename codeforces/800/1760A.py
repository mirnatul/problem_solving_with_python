import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    # no need to sort, check with manual conditions
    nums = sorted(map(int, sys.stdin.readline().split()))
    print(nums[1])
