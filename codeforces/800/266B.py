import sys

n, t = list(map(int, sys.stdin.readline().split()))
st = sys.stdin.readline().strip()

for i in range(t):
    st = st.replace("BG", "GB")
print(st)
