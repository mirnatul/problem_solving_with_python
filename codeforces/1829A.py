import sys

codeforces = 'codeforces'

t = int(sys.stdin.readline().strip())

for _ in range(t):
    mystring = sys.stdin.readline().strip()

    ans = sum(1 for i in range(len(mystring)) if mystring[i] != codeforces[i])
    print(ans)
