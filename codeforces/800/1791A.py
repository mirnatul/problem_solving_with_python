import sys

string = "codeforces"
t = int(sys.stdin.readline().strip())

for _ in range(t):
    inp = sys.stdin.readline().strip()
    if inp in string:
        print("YES")
    else:
        print("NO")