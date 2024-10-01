import sys

n = int(sys.stdin.readline().strip())

people = list(map(int, sys.stdin.readline().split()))
highest = max(people)
given = 0

for _ in range(len(people)):
    if people[_] != highest:
        given += highest-people[_]

print(given)