import sys

n = int(sys.stdin.readline().strip())

mishka = 0
chris = 0
for i in range(n):
    m, c = map(int, sys.stdin.readline().split())
    if m>c:
        mishka += 1
    elif c>m:
        chris += 1

if mishka>chris:
    print("Mishka")
elif chris>mishka:
    print("Chris")
else:
    print("Friendship is magic!^^")