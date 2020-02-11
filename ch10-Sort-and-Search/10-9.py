def find_element(matrix, value):
    row = 0
    col = len(matrix[0]) - 1
    while(row < len(matrix[0]) and col >= 0):
        if matrix[row][col] == value:
            print("value {} is located at {},{}".format(value, row, col))
            return value
        elif matrix[row][col] < value:
            row += 1
        else:
            col -= 1


matrix = [
    [15, 20, 40, 85],
    [20, 35, 80, 95],
    [30, 55, 95, 105],
    [40, 80, 100, 120],


]

print(find_element(matrix, 80))
