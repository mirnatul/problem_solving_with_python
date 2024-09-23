import sys

ui = sys.stdin.readline().strip()

len_of_mySet = len(set(ui))

if len_of_mySet%2 == 0:
    sys.stdout.write("CHAT WITH HER!")
else:
    sys.stdout.write("IGNORE HIM!")
