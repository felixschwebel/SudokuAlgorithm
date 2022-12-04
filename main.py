import tkinter as tk

FONT = ('Times New Roman', 24, "normal")

window = tk.Tk()
window.title('Sudoku Solving')
window.config(bg="white")
window.minsize()

canvas = tk.Canvas(width=504, height=504)
sudoku_grid = tk.PhotoImage(file="sudoku_grid.png")
canvas.create_image(252, 252, image=sudoku_grid)
canvas.grid(column=0, columnspan=81, row=0, rowspan=81, padx=20, pady=20)

new_input = tk.Entry(width=2, font=FONT)
canvas.create_window(31, 30, window=new_input)

new_input2 = tk.Entry(width=2, font=FONT)
canvas.create_window(31, 86, window=new_input2)

new_input3 = tk.Entry(width=2, font=FONT)
canvas.create_window(86, 31, window=new_input3)

# input_list = []
# for i in range(81):
#     new_input =

button = tk.Button(text='Solve', bg='black')
button.config(highlightthickness=0, highlightbackground='white', fg='red')
button.grid(column=0, row=82, padx=20, pady=20)

window.mainloop()




