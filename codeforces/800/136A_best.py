import sys

# Read input
inp = int(sys.stdin.readline().strip())
fnd = list(map(int, sys.stdin.readline().split()))

# Initialize a result list with the same length as the input
result = [0] * inp

# Fill the result list with indices
for index, value in enumerate(fnd):
    result[value - 1] = index + 1  # Store the 1-based index

# Print the result list
sys.stdout.write(' '.join(map(str, result)) + '\n')
