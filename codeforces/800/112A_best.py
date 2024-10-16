# Python allows you to compare strings lexicographically with comparison operators, so there's no need to manually loop through each character.

import sys

word1 = sys.stdin.readline().strip().lower()
word2 = sys.stdin.readline().strip().lower()

if word1 < word2:
    sys.stdout.write("-1\n")
elif word1 > word2:
    sys.stdout.write("1\n")
else:
    sys.stdout.write("0\n")
