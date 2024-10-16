import sys

ui1 = int(sys.stdin.readline().strip())
ui2 = sys.stdin.readline().strip()
count = 0

while ("RR" in ui2) or ("BB" in ui2) or ("GG" in ui2):
    if "RR" in ui2:
        ui2 = ui2.replace("RR", "R", 1)
        count += 1
    if "BB" in ui2:
        ui2 = ui2.replace("BB", "B", 1)
        count += 1
    if "GG" in ui2:
        ui2 = ui2.replace("GG", "G", 1)
        count += 1

sys.stdout.write(f"{count}\n")
