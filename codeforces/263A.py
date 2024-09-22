import sys

main_list = []

for i in range(5):
    main_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(main_list)):
    for j in range(len(main_list[i])):
        if main_list[i][j] == 1:
            row = i+1
            column = j+1

sys.stdout.write(f"{abs(3-row)+abs(3-column)}\n")
