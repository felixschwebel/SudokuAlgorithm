import tkinter
import tkinter as tk
from tkinter import messagebox
import copy

FONT = ('Times New Roman', 24, "normal")


# ---------------------------- FUNCTIONS ----------------------------
# function to get the inputs
def get_inputs():
    # Check all the Entry fields and put the values in a dictionary
    entry_data = {}
    # get the values for the different quadrants
    for n in range(3):
        for m in range(1 + n * 27, 8 + n * 27, 3):
            for k in range(3):
                for l in range(m, m + 3):
                    number = l + k * 9
                    quadrant = None
                    if m == 1:
                        quadrant = 1
                    elif m == 4:
                        quadrant = 2
                    elif m == 7:
                        quadrant = 3
                    elif m == 28:
                        quadrant = 4
                    elif m == 31:
                        quadrant = 5
                    elif m == 34:
                        quadrant = 6
                    elif m == 55:
                        quadrant = 7
                    elif m == 58:
                        quadrant = 8
                    elif m == 61:
                        quadrant = 9
                    entry_data[number] = {
                        'quadrant': quadrant,
                        'possible_num': [],
                    }
    # get the value of the entry field, the column and the row
    entry = 1
    for row in range(1, 10):
        for col in range(1, 10):
            entry_data[entry]['row'] = row
            entry_data[entry]['col'] = col
            # get the value of the field and check if it's between 1 and 9
            try:
                input_list[entry - 1].config(bg='white')
                value = int(input_list[entry - 1].get())
                if value > 9:
                    input_list[entry - 1].config(bg='red')
                    return messagebox.showerror(message="Please make sure to only put in numbers between 1 and 9!")
            except ValueError:
                value = None
                # if the value is empty create a list with all values possible
                entry_data[entry]['possible_num'] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            entry_data[entry]['value'] = value
            entry += 1
    # get the list in order by field indices
    ordered_data = []
    for index in range(1, 82):
        entry_data[index]['index'] = index
        ordered_data.append(entry_data[index])
    return ordered_data


# ----------------------------- SOLVE -----------------------------
# Global Variables
data = []
backup = []
stop = False
checked = []
backup_done = False


def guess_value():
    global data, checked, stop

    data = copy.deepcopy(backup)
    for entry in data:
        if len(entry['possible_num']) == 2 and checked.count(entry['index']) < 2:
            if checked.count(entry['index']) == 0:
                entry['value'] = entry['possible_num'][0]
                checked.append(entry['index'])
            elif checked.count(entry['index']) == 1:
                entry['value'] = entry['possible_num'][1]
                checked.append(entry['index'])
            stop = True
            break


def missing_values():
    global stop

    value_none = 0
    for entry in data:
        if entry['value'] is not None:
            value_none += 1
    if value_none == 81:
        stop = True


def display():
    # clear the field and display the found values
    for field in range(0, 81):
        if data[field]['value'] is not None:
            input_list[field].delete(0, tkinter.END)
            input_list[field].insert(0, data[field]['value'])


def solve():
    global data, stop, checked, backup_done, backup
    data = get_inputs()
    stop = False

    while not stop:
        # Check Fields
        for index in range(0, 81):
            things_to_check = ['quadrant', 'col', 'row']
            for thing in things_to_check:
                for entry in data:
                    if entry[thing] == data[index][thing]:
                        if entry['value'] is not None:
                            try:
                                data[index]['possible_num'].remove(entry['value'])
                            except ValueError:
                                pass

        # Fill Values
        filled_values = 0
        if checked:
            for index in range(1, 10):
                possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for entry in data:
                    if entry['quadrant'] == index:
                        if len(entry['possible_num']) == 1:
                            try:
                                possible_values.remove(entry['possible_num'][0])
                            except ValueError:
                                guess_value()
        for entry in data:
            if len(entry['possible_num']) == 1:
                entry['value'] = entry['possible_num'][0]
                filled_values += 1

        missing_values()

        if filled_values == 0 and stop is not True:
            if backup_done is False:
                backup = copy.deepcopy(data)
                backup_done = True
            guess_value()

        # Check for missing values
        missing_values()

    # Display values
    display()


# ------------------------------- UI -------------------------------
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
