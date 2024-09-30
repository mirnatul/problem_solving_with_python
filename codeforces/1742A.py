import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    if nums[2] == nums[0] + nums[1]:
        print("YES")
    else:
        print("NO")