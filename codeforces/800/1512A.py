import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))

    if nums[0] == nums[1] or nums[0] == nums[2]:
        common = nums[0]
    elif nums[1] == nums[2]:
        common = nums[1]
    else:
        common = nums[0]
    
    for i in range(len(nums)):
        if nums[i] != common:
            print(i+1)
            break
