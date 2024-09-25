import sys

ui = sys.stdin.readline().strip()
num2 = int(ui)

while True:
    num2 += 1
    setNum2 = set(map(str, str(num2)))
    if len(setNum2) == 4:
        print(num2)
        break
