import sys

n1 = sys.stdin.readline().strip()
n2 = sys.stdin.readline().strip()

out = ""

length = len(n1)
for i in range(length):
    if n1[i] == n2[i]:
        out += "0"
    else:
        out += "1"
print(out)