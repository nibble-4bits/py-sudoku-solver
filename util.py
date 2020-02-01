def is_number_valid(sudoku, row, col, number):
    '''Checks if number can be placed in the square specified by (row, col)'''
    return is_number_valid_row(sudoku, row, number) and is_number_valid_col(sudoku, col, number) and is_number_valid_box(sudoku, row, col, number)


def is_number_valid_row(sudoku, row, number):
    '''Checks if number can be placed in the row specified'''
    for y in range(len(sudoku)):
        if sudoku[row][y] == number:
            return False
    return True


def is_number_valid_col(sudoku, col, number):
    '''Checks if number can be placed in the column specified'''
    for x in range(len(sudoku)):
        if sudoku[x][col] == number:
            return False
    return True


def is_number_valid_box(sudoku, row, col, number):
    '''Checks if number can be placed in the box that contains the square specified by (row, col)'''
    row_start = row - row % 3
    row_end = row_start + 3
    col_start = col - col % 3
    col_end = col_start + 3

    for x in range(row_start, row_end):
        for y in range(col_start, col_end):
            if sudoku[x][y] == number:
                return False
    return True
