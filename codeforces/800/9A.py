import sys

dice = [1, 2, 3, 4, 5, 6]
y, w = map(int, sys.stdin.readline().split())
maximum = max(y, w)
probability = len(dice[dice.index(maximum):])

# in stead of using long if-else use dictionary
if probability == 6:
    print("1/1")
elif probability == 5:
    print("5/6")
elif probability == 4:
    print("2/3")
elif probability == 3:
    print("1/2")
elif probability == 2:
    print("1/3")
else:
    print("1/6")