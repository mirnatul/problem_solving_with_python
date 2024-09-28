import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
letter = sys.stdin.readline().strip()

all = first + second

nameDict = {}
for i in all:
    if i in nameDict:
        nameDict[i] += 1
    else:
        nameDict[i] = 1

letterDict = {}
for i in letter:
    if i in letterDict:
        letterDict[i] += 1
    else:
        letterDict[i] = 1

print("YES") if nameDict==letterDict else print("NO")
