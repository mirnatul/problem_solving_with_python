import sys

n, k = map(int, sys.stdin.readline().split())
members = list(map(int, sys.stdin.readline().split()))

for i in range(len(members)):
    members[i] += k

eligible = sum(1 for i in members if i<=5)
print(eligible//3)
