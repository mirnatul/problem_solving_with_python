import sys

levels = int(sys.stdin.readline().strip())

xPasses = set(map(int, sys.stdin.readline().split()[1:]))
yPasses = set(map(int, sys.stdin.readline().split()[1:]))

print("I become the guy.") if len(xPasses|yPasses) == levels else print("Oh, my keyboard!")
