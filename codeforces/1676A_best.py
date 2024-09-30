import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    num = sys.stdin.readline().strip()
    sum1 = sum(map(int, num[:3]))
    sum2 = sum(map(int, num[3:]))
    print("YES" if sum1 == sum2 else "NO")
