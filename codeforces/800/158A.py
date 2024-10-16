import sys

passed = 0

data = sys.stdin.readline().strip()
n, k = map(int, data.split())

data2 = sys.stdin.readline().strip()
participants = list(map(int, data2.split()))

for i in participants:
    if i >= participants[k-1] and i > 0:
        passed += 1

sys.stdout.write(f"{passed}")