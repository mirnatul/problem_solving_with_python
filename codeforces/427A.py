import sys

n = int(sys.stdin.readline().strip())
event = list(map(int, sys.stdin.readline().split()))

event_length = len(event)

flag = 0
crime_count = 0
for i in range(event_length):
    if event[i]<0 and flag <= 0:
        crime_count += 1
        flag = 0
    else:
        flag += event[i]

print(crime_count)