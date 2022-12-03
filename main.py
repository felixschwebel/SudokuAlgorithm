import tkinter as tk

window = tk.Tk()
window.title('Sudoku Solving')
window.config(bg="white")
window.minsize()

canvas = tk.Canvas(width=504, height=504)
sudoku_grid = tk.PhotoImage(file="sudoku_grid.png")
canvas.create_image(252, 252, image=sudoku_grid)
canvas.grid(column=0, row=0)


window.mainloop()




