import sys

ui1 = int(sys.stdin.readline().strip())
ui2 = sys.stdin.readline().strip()

count = 0

for i in range(1, ui1):
    if ui2[i] == ui2[i - 1]:
        count += 1

sys.stdout.write(f"{count}\n")