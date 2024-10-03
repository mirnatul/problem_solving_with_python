import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    string = sys.stdin.readline().strip()
    length = len(string)
    if length%2==0:
        string1 = string[0:length//2]
        string2 = string[length//2:]
        if string1==string2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")