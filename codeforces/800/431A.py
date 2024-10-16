import sys

calories = list(map(int, sys.stdin.readline().split()))
s = sys.stdin.readline().strip()

count = 0
for i in range(len(s)):
    count += int(calories[int(s[i])-1])

print(count)