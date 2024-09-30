import sys

nums = sorted(map(int, sys.stdin.readline().split()))

a = nums[3] - nums[0]
b = nums[3] - nums[1]
c = nums[3] - nums[2]
print(a, b, c)