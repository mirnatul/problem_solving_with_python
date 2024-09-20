x = 0

user_input = int(input())

for i in range(user_input):
    sign = input()
    if sign == "X++" or sign == "++X":
        x += 1
    if sign == "X--" or sign == "--X":
        x -= 1

print(x)