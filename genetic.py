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

