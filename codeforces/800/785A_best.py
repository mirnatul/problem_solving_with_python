n = int(input())
faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

count = 0
for _ in range(n):
    name = input().strip()
    count += faces[name]

print(count)
