n = int(input())  # Read the number of words

for _ in range(n):
    word = input()  # Read each word
    if len(word) <= 10:
        print(word)  # If the word is short, print it as is
    else:
        print(f"{word[0]}{len(word) - 2}{word[-1]}")  # Abbreviate longer words

