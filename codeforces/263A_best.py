import sys

# Loop through the input and search for the '1'
for i in range(5):
    row = list(map(int, sys.stdin.readline().split()))
    if 1 in row:
        # Find the column where '1' is located
        j = row.index(1)
        # Calculate the minimum number of moves to reach the center (3,3)
        result = abs(2 - i) + abs(2 - j)
        print(result)
        break
