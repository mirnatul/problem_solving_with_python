import sys

inp = set(sys.stdin.readline().strip())
rem_set = {'}', ',', ' ', '{'}
finalSet = inp - rem_set
print(len(finalSet))
