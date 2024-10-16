import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    aas = sorted(list(map(int, sys.stdin.readline().split())))

    # in stead of removing, just go through the loop and see if the condition match or not. That will be more efficient.
    i = 0
    while True:
        if len(aas)==1:
            break
        elif abs(aas[i]-aas[i+1])<=1:
            if aas[i]<aas[i+1]:
                aas.remove(aas[i])
            else:
                aas.remove(aas[i+1])
        else:
            break
    print("YES" if len(aas)==1 else "NO")
