n = int(input())
home = []
away = []

for _ in range(n):
    h, a = map(int, input().split())
    home.append(h)
    away.append(a)

# Use a dictionary to count occurrences of each away uniform
away_count = {}
for a in away:
    if a in away_count:
        away_count[a] += 1
    else:
        away_count[a] = 1
print(away_count)

# Count the number of matches where home uniform matches any away uniform
count = 0
for h in home:
    if h in away_count:
        count += away_count[h]

print(count)
