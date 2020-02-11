GRID_SIZE = 4


def place_queen(row, columns, results):
    if row == GRID_SIZE:
        results.append(columns)
    else:
        for col in range(GRID_SIZE):
            if check_valid(columns, row, col) == True:
                columns_cp = columns.copy()
                columns[row] = col
                place_queen(row+1, columns_cp, results)


def check_valid(columns, row1, column1):
    for row2 in range(0, row1):
        column2 = columns[row2]

        if column1 == column2:
            return False

        column_distance = abs(column1 - column2)
        row_distance = row1 - row2

        if column_distance == row_distance:
            return False

    return True


columns = [None] * GRID_SIZE
results = []
place_queen(0, columns, results)
print(results)
