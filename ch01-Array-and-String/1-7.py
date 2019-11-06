def rotate(matrix):
    num_layer = int(len(matrix)/2)
    for layer in range(num_layer):
        offset = len(matrix) - layer - 1
        for i in range(layer, offset):
            tmp = matrix[layer][i]
            matrix[layer][i] = matrix[offset-i][layer]
            matrix[offset-i][layer] = matrix[offset][offset-i]
            matrix[offset][offset-i] = matrix[i][offset]
            matrix[i][offset] = tmp

    return matrix


matrix = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

matrix = rotate(matrix)
print(matrix)
