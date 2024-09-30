import sys

n, k, l, c, d, p, nl, np = map(int, sys.stdin.readline().split())

toast = (k*l)//nl
if (p//np)<toast:
    toast = p//np
if c*d<toast:
    toast = d

print(toast//n)