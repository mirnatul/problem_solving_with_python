import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    num = list(sys.stdin.readline().strip())
    sum1 = int(num[0])+int(num[1])+int(num[2])
    sum2 = int(num[3])+int(num[4])+int(num[5])
    print("YES" if sum1==sum2 else "NO")