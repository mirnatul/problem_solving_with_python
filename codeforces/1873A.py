import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    s = sys.stdin.readline().strip()
    if s[1]=="b" or (s[1]=="c" and s[0]=="a") or (s[1]=="a" and s[0]=="b"):
        print("YES")
    else:
        print("NO")