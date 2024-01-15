def print_sudoku(puzzle):
    print("-" * 25)
    for a in range(len(puzzle)):
        if a % 3 == 0 and a != 0:
            print("-" * 25)
        print("|", end=" ")
        for b in range(len(puzzle[a])):
            if b % 3 == 0 and b != 0:
                print("|", end=" ")
            print(puzzle[a][b], end=" ")
        print("|")
    print("-" * 25)


# checks if number placment is valid
def is_correct(puzzle, row, column, number):
    # this checks the row and column the number is in
    for num in range(9):
        if puzzle[row][num] == number or puzzle[num][column] == number:
            return False

    # this checks the grid for the number
    row_start = 3*(row//3)
    column_start = 3*(column//3)
    for a in range(3):
        for b in range(3):
            if puzzle[row_start+a][column_start+b] == number:
                return False

    return True


# looks for empty spaces on the puzzle
def look_for_blanks(puzzle):
    for a in range(9):
        for b in range(9):
            if puzzle[a][b] == 0:
                return a, b
    return None


def solve_sudoku(puzzle):
    blank = look_for_blanks(puzzle)

    if not blank:
        return True

    row, column = blank

    for number in range(1, 10):
        if is_correct(puzzle, row, column, number):
            puzzle[row][column] = number

            if solve_sudoku(puzzle):
                return True

            # backtrack for if the number is incorrect
            puzzle[row][column] = 0

    # if there's no number that can be placed backtrack again
    return False

