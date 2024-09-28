from collections import Counter

first = input().strip()
second = input().strip()
letter = input().strip()

# Use Counter to count characters in both concatenated string and letter
if Counter(first + second) == Counter(letter):
    print("YES")
else:
    print("NO")
