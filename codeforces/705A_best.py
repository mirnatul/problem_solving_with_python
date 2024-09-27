n = int(input())

output = []
for i in range(1, n + 1):
    if i % 2 != 0:
        output.append("I hate")
    else:
        output.append("I love")

print(" that ".join(output) + " it")
