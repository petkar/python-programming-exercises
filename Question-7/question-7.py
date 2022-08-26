size = list(map(int, input("Enter the size of the matrix as m, n: ").split(",")))
matrix = []

for i in range(size[0]):
    row = []
    for j in range(size[1]):
        row.append(i * j)
    matrix.append(row)

print(matrix)
