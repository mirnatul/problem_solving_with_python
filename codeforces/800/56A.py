import sys

ui = sys.stdin.readline().strip()

len_of_lower = sum(1 for char in ui if char.islower())
len_of_upper = len(ui)-len_of_lower

ans = ui.lower() if len_of_lower >= len_of_upper else ui.upper()

print(ans)