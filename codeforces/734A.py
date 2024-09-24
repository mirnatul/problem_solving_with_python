import sys

ui = int(sys.stdin.readline().strip())
st = sys.stdin.readline().strip()

a = st.count("A")
d = st.count("D")

if a>d:
    print("Anton")
elif d>a:
    print("Danik")
else:
    print("Friendship")
