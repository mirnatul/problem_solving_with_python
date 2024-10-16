import sys

n, m = map(int, sys.stdin.readline().split())
ans = "#Black&White"
for i in range(n):
    array = list(map(str, sys.stdin.readline().split()))
    if 'C' in array or 'M' in array or 'Y' in array:
        ans = "#Color"
        break

print(ans)