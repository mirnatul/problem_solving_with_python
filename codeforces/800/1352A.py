import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    num = sys.stdin.readline().strip()
    listOfNum = list(num)
    count = 0
    output = ""
    for j in range(len(listOfNum)):
        if listOfNum[j] != '0':
            count += 1
            zeroStr = "0" * (len(listOfNum) - j - 1)
            new_num = int(listOfNum[j] + zeroStr)
            output += f"{new_num} "
    print(count)
    print(output)
