input_number = int(input())
array_of_word = []

while input_number>0:
    word = input()
    array_of_word.append(word)
    input_number = input_number-1

for x in array_of_word:
    if len(x)<=10:
        print(x)
    else:
        print(f"{x[0]}{len(x)-2}{x[-1]}")