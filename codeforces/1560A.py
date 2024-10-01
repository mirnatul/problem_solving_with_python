import sys

nums = []
i = 0
count = 1
while True:
    if count%3 != 0 and count%10 != 3:
        nums.append(count)
        i += 1
        if i == 1000:
            break
    count += 1

t = int(sys.stdin.readline().strip())

for i in range(t):
    key = int(sys.stdin.readline().strip())
    print(nums[key-1])