import sys

t = int(sys.stdin.readline().strip())
constantStr = "Timur"

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    string = sys.stdin.readline().strip()
    
    # Check if length is equal to 5 (since "Timur" has 5 characters)
    if n == 5 and sorted(string) == sorted(constantStr):
        print("YES")
    else:
        print("NO")
