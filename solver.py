import time
from util import is_number_valid
from pprint import pprint


def find_empty_squares(sudoku):
    '''Finds all empty squares that need to be filled to solve the sudoku

    Args:
        sudoku (list[list[int]]): The sudoku of which to find the empty squares

    Returns:
        list[tuple[int]]: A list that contains all pairs of (row, col) that are empty squares
    '''
    empty_squares = []

    for row in range(len(sudoku)):
        for col in range(len(sudoku[row])):
            if sudoku[row][col] == 0:
                empty_squares.append((row, col))
    return empty_squares


def solve(sudoku, empty_sq, curr_sq_idx=0):
    '''Recursively solves and prints all solutions to the given sudoku

    Args:
        sudoku (list[list[int]]): The sudoku to solve
        empty_sq (list[tuple[int]]): The (row, col) pairs of empty squares to fill
        curr_sq_idx (int): The current index of empty_sq trying to be filled
    '''
    if curr_sq_idx == len(empty_sq):
        pprint(sudoku)
        print()
    else:
        row = empty_sq[curr_sq_idx][0]
        col = empty_sq[curr_sq_idx][1]
        for possible_num in range(1, 10):
            if is_number_valid(sudoku, row, col, possible_num):
                sudoku[row][col] = possible_num
                solve(sudoku, empty_sq, curr_sq_idx + 1)
                sudoku[row][col] = 0


if __name__ == '__main__':
    sudoku = [
        [0, 2, 0, 0, 0, 0, 0, 0, 7],
        [4, 0, 0, 0, 0, 5, 0, 8, 0],
        [0, 3, 0, 0, 9, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 8, 0, 7, 4],
        [0, 0, 4, 2, 0, 0, 1, 0, 0],
        [0, 6, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 3, 8, 0, 6, 0, 0]
    ]
    empty_squares = find_empty_squares(sudoku)
    t1 = time.perf_counter()
    solve(sudoku, empty_squares)
    t2 = time.perf_counter()
    print(f'Time taken: {t2 - t1}s')
