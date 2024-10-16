import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = sorted(list(map(int, sys.stdin.readline().split())))
    sumOfArr = sum(arr)/2
    # print(sumOfArr)

    smallest = sys.maxsize
    # smallest = sum(i for i in arr if)
    tillSum = 0
    index = 0
    for i in range(len(arr)):
        tillSum += arr[i]
        # print("tillSum:----", tillSum)
        if abs(sumOfArr-tillSum)<smallest:
            # print("Enter")
            smallest = abs(sumOfArr-tillSum)
            index = i
        if tillSum>sumOfArr:
            if abs(sumOfArr-tillSum)<smallest:
                # print("Enter 2")
                index = i
                break
    # print(index)
    arr1 = max(arr[:index+1])
    arr2 = min(arr[index+1:])
    print(arr2-arr1)

    # learn next session