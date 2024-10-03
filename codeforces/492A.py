import sys

n = int(sys.stdin.readline().strip())

flag = n
i = 1
count = 0
while flag>0:
    flag = flag-(i*(i+1))//2
    if flag<0:
        break
    count += 1
    i += 1
print(count)
