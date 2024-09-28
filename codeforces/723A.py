import sys

distance = list(map(int, sys.stdin.readline().split()))

distance.sort()
point = distance[1]
print(abs(distance[0]-distance[1]) + abs(distance[2]-distance[1]))