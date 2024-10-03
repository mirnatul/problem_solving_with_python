import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    caught = False
    myDict = {}
    for i in range(n):
        if s[i] in myDict:
            if abs(myDict[s[i]]-i)>1:
                caught = True
                break
            else:
                myDict[s[i]] = i
        else:
            myDict[s[i]] = i

    if caught:
        print("NO")
    else:
        print("YES")