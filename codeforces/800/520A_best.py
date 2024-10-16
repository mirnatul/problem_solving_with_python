n = int(input())
word = input().strip().lower()

# Use a set to collect unique alphabetic characters
unique_letters = set(ch for ch in word if ch.isalpha())

print("YES" if len(unique_letters) == 26 else "NO")
