import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    
    # Check if n is divisible by 4
    if n % 4 == 0:
        print("YES")
        
        even_part = [i for i in range(2, n + 1, 2)]  # Even numbers
        odd_part = [i for i in range(1, n - 1, 2)]  # Odd numbers except last
        
        # Calculate the last odd number to balance the sum
        last_odd = sum(even_part) - sum(odd_part)
        odd_part.append(last_odd)
        
        print(*even_part, *odd_part)
    else:
        print("NO")
