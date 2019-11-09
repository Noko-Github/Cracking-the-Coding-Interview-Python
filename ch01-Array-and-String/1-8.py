def set_zeros(matrix):
    row = [False] * len(matrix)
    column = [False] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    for i in range(len(row)):
        if row[i] == True:
            nullify_row(matrix, i)

    for i in range(len(column)):
        if column[i] == True:
            nullify_col(matrix, i)

    return matrix


def nullify_row(matrix, index):
    for i in range(len(matrix[index])):
        matrix[index][i] = 0


def nullify_col(matrix, index):
    for i in range(len(matrix)):
        matrix[i][index] = 0


matrix = [
    [1, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]

print(set_zeros(matrix))
