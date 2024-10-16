import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    people = list(map(int, sys.stdin.readline().split()))
    timur = people[0]
    # Don't use the sort here. It increases the time complexity
    people.sort(reverse=True)
    print(people.index(timur))