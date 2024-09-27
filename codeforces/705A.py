import sys

n = int(sys.stdin.readline().strip())
hateLast = "I hate it"
loveLast = "I love it"

hate = "I hate that "
love = "I love that "

output = ""
for i in range(1, n):
    if n == 1:
        break
    elif i%2 != 0:
        output += hate
    else:
        output += love
print(output + hateLast) if n%2 != 0 else print(output + loveLast)
