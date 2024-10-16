import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    array = list(map(int, sys.stdin.readline().split()))
    sorted_array = sorted(array, reverse=True)
    if (sorted_array[0] == array[0] or sorted_array[0] == array[1]) and (sorted_array[1] == array[2] or sorted_array[1] == array[3]):
        print("YES")
    elif (sorted_array[0] == array[2] or sorted_array[0] == array[3]) and (sorted_array[1] == array[0] or sorted_array[1] == array[1]):
        print("YES")
    else:
        print("NO")
