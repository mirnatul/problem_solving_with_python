import sys

k, r = map(int, sys.stdin.readline().split())

i = 1
while True:
    if (k*i)%10 == r or (k*i)%10 == 0:
        break
    else:
        i += 1

print(i)