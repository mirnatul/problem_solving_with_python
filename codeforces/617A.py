import sys

ui = int(sys.stdin.readline().strip())

c1 = ui//5
c1_rem = ui%5
c2 = c1_rem//4
c2_rem = c1_rem%4
c3 = c2_rem//3
c3_rem = c2_rem%3
c4 = c3_rem//2
c4_rem = c3_rem%2
c5 = c4_rem//1

print(c1+c2+c3+c4+c5)