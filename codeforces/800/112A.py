import sys

word1 = sys.stdin.readline().strip().lower()
word2 = sys.stdin.readline().strip().lower()

length_of_word = len(word1)

for i in range(length_of_word):
    if word1[i] == word2[i]:
        x = 0
        continue
    elif word1[i] < word2[i]:
        x = -1
        break
    else:
        x = 1
        break

sys.stdout.write(f"{x}\n")