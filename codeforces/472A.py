import sys

def is_prime(n):
    prime = True
    for i in range(2, n-1):
        if n%i == 0:
            prime = False
            break
    return prime

n = int(sys.stdin.readline().strip())

first = 4
second = n-4
while True:
    if is_prime(first) == True or is_prime(second) == True:
        first += 1
        second -= 1
    else:
        break

print(first, second)