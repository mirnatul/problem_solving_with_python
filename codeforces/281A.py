import sys

ui = list(sys.stdin.readline().strip())
first, *others = ui

op = first.upper() + "".join(others)
print(op)
