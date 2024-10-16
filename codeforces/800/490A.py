import sys

n = int(sys.stdin.readline().strip())
skills = list(map(int, sys.stdin.readline().split()))

team = min(skills.count(1), skills.count(2), skills.count(3))
print(team)

a_index = 0
b_index = 0
c_index = 0
for i in range(team):
    a = skills.index(1, a_index) + 1
    a_index = a
    b = skills.index(2, b_index) + 1
    b_index = b
    c = skills.index(3, c_index) + 1
    c_index = c

    print(a, b, c)