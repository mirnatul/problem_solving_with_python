import sys

n = int(sys.stdin.readline().strip())
list1 = []
list2 = []
for i in range(n):
    h, a = map(int, sys.stdin.readline().split())
    list1.append(h)
    list2.append(a)

count = 0
for i in list1:
    count += list2.count(i)

print(count)