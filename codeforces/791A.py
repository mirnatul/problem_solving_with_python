import sys

a, b = map(int, sys.stdin.readline().split())
year = 0

while a<=b:
    a *= 3
    b *= 2
    year += 1

sys.stdout.write(f"{year}\n")