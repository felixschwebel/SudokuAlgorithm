import tkinter as tk
from sudoku_solver import SudokuSolver

FONT = ('Times New Roman', 24, "normal")

# function to get the inputs
def get_inputs():
    # Check all the Entry fields and put the values in a dictionary
    entry_data = {}
    return entry_data

# Solve Sudoku
def solve():
    # uses the SudokuSolver Class
    solver = SudokuSolver(get_inputs())
    # displays the found values

# Set up the Window for Tkinter
window = tk.Tk()
window.title('Sudoku Solving')
window.config(bg="white")
window.minsize()

# Canvas class from tkinter to get the Sudo-grid as background image
canvas = tk.Canvas(width=504, height=504)
sudoku_grid = tk.PhotoImage(file="sudoku_grid.png")
canvas.create_image(252, 252, image=sudoku_grid)
canvas.config(borderwidth=0, highlightthickness=0)
canvas.grid(column=0, columnspan=81, row=0, rowspan=81, padx=20, pady=20)

# Create a list of Entries to populate the Sudoku-field
input_list = []
list_index = 0
x_start = 31
y_start = 31

for i in range(9):
    for j in range(9):
        input_list.append(tk.Entry(width=1, font=FONT, fg='black', bg='white',
                                   borderwidth=0, highlightthickness=0))
        canvas.create_window(x_start, y_start, window=input_list[list_index])
        list_index += 1
        x_start += 55
    x_start = 31
    y_start += 55

# button to start the calculation
button = tk.Button(text='Solve', bg='black', command=solve)
button.config(highlightthickness=0, highlightbackground='white', fg='red')
button.grid(column=0, row=82, padx=20, pady=20)

window.mainloop()




