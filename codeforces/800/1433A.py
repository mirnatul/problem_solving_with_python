import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    s = sys.stdin.readline().strip()

    ans = (int(s[0])-1)*10 + (len(s)*(len(s)+1))//2
    print(ans)
