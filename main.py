import tkinter as tk
# had to do this too as ttk wouldn't work just from tkinter
from tkinter import ttk
from tkinter import messagebox

# Import your sudoku solver functions
import backtrack
import testSudoku


class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        # the defaults
        self.sudoku_option_text = tk.StringVar(value="sudokuEasy")
        self.algorithm_option_text = tk.StringVar(value="backtracking")
        self.custom_sudoku_var = tk.StringVar()

        # Create the widgets
        self.create_widgets()

    def create_widgets(self):
        # drop down menu for selecting a pre-made sudoku
        selected_a_sudoku = tk.Label(self.root, text="Select Sudoku:")
        sudoku_options = tk.ttk.Combobox(self.root, textvariable=self.sudoku_option_text, values=["sudokuEasy", "sudokuMedium", "sudokuHard", "sudokuExpert", "sudokuMaster", "worldsHardest", "sudokuWrong", "custom"])

        # Algorithm dropdown
        select_a_algorithm = tk.Label(self.root, text="Select Algorithm:")
        algorithm_options = tk.ttk.Combobox(self.root, textvariable=self.algorithm_option_text, values=["backtracking", "genetic", "another_algorithm?"])

        # for entering your own sudoku
        custom_sudoku_title = tk.Label(self.root, text="Enter Your Sudoku (0 for empty cells):")
        custom_sudoku_entered_string = tk.Entry(self.root, textvariable=self.custom_sudoku_var, width=50)

        # example for the custom format
        custom_sudoku_format_label = tk.Label(self.root, text="Enter Your Sudoku (0 for empty cells):\n"
                                                              "Use a text editor to make this format\n"
                                                              "Example Format:\n"
                                                              "000000000\n"
                                                              "000000000\n"
                                                              "000000000\n"
                                                              "000000000\n"
                                                              "000000000\n"
                                                              "000000000\n"
                                                              "000000000\n"
                                                              "000000000\n"
                                                              "000080000")

        # Solve button
        solve_button = tk.Button(self.root, text="Solve Sudoku", command=self.solve_sudoku)

        # for displaying the  unfinished and finished Sudoku
        self.initial_sudoku_text = tk.Text(self.root, height=13, width=25, wrap="none", state="disabled")
        self.solved_sudoku_text = tk.Text(self.root, height=13, width=25, wrap="none", state="disabled")

        # layout for the programn
        selected_a_sudoku.grid(row=0, column=0, padx=10, pady=10)
        sudoku_options.grid(row=0, column=1, padx=10, pady=10)
        select_a_algorithm.grid(row=1, column=0, padx=10, pady=10)
        algorithm_options.grid(row=1, column=1, padx=10, pady=10)
        custom_sudoku_title.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        custom_sudoku_entered_string.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
        custom_sudoku_format_label.grid(row=4, column=0, columnspan=2, pady=10)
        solve_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.initial_sudoku_text.grid(row=6, column=0, padx=10, pady=10)
        self.solved_sudoku_text.grid(row=6, column=1, padx=10, pady=10)

    def solve_sudoku(self):
        sudoku_type = self.sudoku_option_text.get()
        algorithm_type = self.algorithm_option_text.get()
        custom_sudoku_string = self.custom_sudoku_var.get()

        # Get the selected Sudoku puzzle
        if sudoku_type == "custom":
            puzzle = self.format_custom_sudoku(custom_sudoku_string)
        elif sudoku_type == "sudokuEasy":
            puzzle = testSudoku.sudokuEasy
        elif sudoku_type == "sudokuMedium":
            puzzle = testSudoku.sudokuMedium
        elif sudoku_type == "sudokuHard":
            puzzle = testSudoku.sudokuHard
        elif sudoku_type == "sudokuExpert":
            puzzle = testSudoku.sudokuExpert
        elif sudoku_type == "sudokuMaster":
            puzzle = testSudoku.sudokuMaster
        elif sudoku_type == "worldsHardest":
            puzzle = testSudoku.worldsHardest
        elif sudoku_type == "sudokuWrong":
            puzzle = testSudoku.sudokuWrong

        else:
            tk.messagebox.showerror("Error", "Invalid Sudoku selection.")
            return

        # Display initial Sudoku state
        initial_sudoku_str = self.format_sudoku_string(puzzle)
        self.initial_sudoku_text.configure(state="normal")
        self.initial_sudoku_text.delete(1.0, "end")
        self.initial_sudoku_text.insert("end", initial_sudoku_str)
        self.initial_sudoku_text.configure(state="disabled")

        # Solve the Sudoku using the selected algorithm
        if algorithm_type == "backtracking":
            if backtrack.solve_sudoku(puzzle):
                # Display solved Sudoku state
                solved_sudoku_str = self.format_sudoku_string(puzzle)
                self.solved_sudoku_text.configure(state="normal")
                self.solved_sudoku_text.delete(1.0, "end")
                self.solved_sudoku_text.insert("end", solved_sudoku_str)
                self.solved_sudoku_text.configure(state="disabled")

                # Print the solved Sudoku to the console
                backtrack.print_sudoku(puzzle)
                tk.messagebox.showinfo("Sudoku Solved", "Sudoku solved!")
            else:
                tk.messagebox.showinfo("No Solution", "No solution for the puzzle.")
        else:
            tk.messagebox.showerror("Error", "Invalid algorithm selection.")

    def format_sudoku_string(self, puzzle):
        tidied_sudoku = "+-------+-------+-------+\n"

        for a in range(len(puzzle)):
            if a % 3 == 0 and a != 0:
                tidied_sudoku += "|-------|-------|-------|\n"

            for b in range(len(puzzle[a])):
                if b % 3 == 0:
                    tidied_sudoku += "| "

                tidied_sudoku += str(puzzle[a][b]) + " "

                if b == 8:
                    tidied_sudoku += "|\n"

        tidied_sudoku += "+-------+-------+-------+"
        return tidied_sudoku

    def format_custom_sudoku(self, custom_sudoku_str):
        # Split the string up
        rows = custom_sudoku_str.splitlines()

        # Empty list for the string
        puzzle = []

        # for loop for each row
        for row_str in rows:
            # Create an empty list for each row
            current_row = []

            # Iterate through each character in the current row string
            for char in row_str:
                # Convert the character to an integer and add it to the row
                current_row.append(int(char))

            # add the row to the puzzle list
            puzzle.append(current_row)

        # Return the formatted Sudoku
        return puzzle


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
