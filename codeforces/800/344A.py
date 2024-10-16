import sys

ui = int(sys.stdin.readline().strip())

count = 1
first = int(sys.stdin.readline().strip())

for i in range(ui-1):
    ui2 = int(sys.stdin.readline().strip())
    if ui2 != first:
        count += 1
        first = ui2
print(count)
