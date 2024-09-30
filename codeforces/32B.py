import sys

code = sys.stdin.readline().strip()
two = code.replace("--", "2")
one = two.replace("-.", "1")
zero = one.replace(".", "0")

print(zero)