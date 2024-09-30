import sys

n = int(sys.stdin.readline().strip())

cards = list(map(int, sys.stdin.readline().split()))

s = d = 0
start = 0
end = n-1

for i in range(n):
    if cards[start]>cards[end]:
        theCard = cards[start]
        start += 1
    else:
        theCard = cards[end]
        end -= 1
    
    if i%2==0:
        s += theCard
    else:
        d += theCard

print(s, d)