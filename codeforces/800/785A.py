import sys

n = int(sys.stdin.readline().strip())

count = 0
for i in range(n):
    name = sys.stdin.readline().strip()
    if name == "Tetrahedron":
        count += 4
    elif name == "Cube":
        count += 6
    elif name == "Octahedron":
        count += 8
    elif name == "Dodecahedron":
        count += 12
    elif name == "Icosahedron":
        count += 20
print(count)