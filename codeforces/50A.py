import sys

a, b = map(int, sys.stdin.readline().split())

sq = (a*b)//2
sys.stdout.write(f"{sq}\n")