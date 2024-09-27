import sys

money = int(sys.stdin.readline().strip())
note_count = 0

for i in [100, 20, 10, 5, 1]:
    count_add = money // i
    note_count += count_add
    money = money - i*count_add

print(note_count)