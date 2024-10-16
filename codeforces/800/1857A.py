import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    arr_odd = [i for i in arr if i%2!=0]
    total_odd = sum(arr_odd)
    arr_even = [i for i in arr if i%2==0]
    total_even = sum(arr_even)

    if n%2==0 and len(arr_odd)%2==0:
        print("YES")
    elif n%2!=0 and len(arr_odd)%2==0:
        print("YES")
    else:
        print("NO")