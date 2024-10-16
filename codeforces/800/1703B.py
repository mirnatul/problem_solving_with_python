import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    string = sys.stdin.readline().strip()
    solved = []
    balloons = 0
    for i in range(n):
        if string[i] in solved:
            balloons += 1
        else:
            balloons += 2
            solved.append(string[i])
    print(balloons)