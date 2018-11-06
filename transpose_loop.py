matrix = [[1,2], [4,5,], [7,8]]
result = [[0,0,0], [0,0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[j][i] = matrix[i][j]

for r in result:
    print(r)
        