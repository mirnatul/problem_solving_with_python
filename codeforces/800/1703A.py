import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    inp = sys.stdin.readline().strip().lower()
    print("YES") if inp == "yes" else print("NO")