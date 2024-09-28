import sys

n = int(sys.stdin.readline().strip())
police = 0
crime_count = 0

for event in map(int, sys.stdin.readline().split()):
    if event > 0:
        police += event
    else:
        if police > 0:
            police -= 1  
        else:
            crime_count += 1  
print(crime_count)  