import sys

n = int(sys.stdin.readline().strip())
all_soldier = list(map(int, sys.stdin.readline().split()))
length = len(all_soldier)

move = 0

maxHeight = all_soldier.index(max(all_soldier))
move += maxHeight
all_soldier.reverse()
minHeight = all_soldier.index(min(all_soldier))
minHeight = all_soldier.index(min(all_soldier))
move += minHeight

print(move-1) if maxHeight>(length-1)-minHeight else print(move)
