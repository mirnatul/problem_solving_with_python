import sys

n, m = map(int, sys.stdin.readline().split())
prime_array = []

for i in range(n+1, m+1):
    is_prime = True
    for j in range(2, i):
        if i%j==0:
            is_prime = False
            break
    if is_prime == True:
        prime_array.append(i)
        break

if len(prime_array)>=1 and prime_array[0] == m:
    print("YES")
else:
    print("NO")