from tkinter import *

something = Tk()

something.title("Calculator")
something.geometry("400x600")

# Lets make the GUI first, only *, +, -, and / operations will be implemented later
# Lets make it super simple

# Create a text entry for the calculator display
display = Entry(something, font=('Arial', 24), bd=10, insertwidth
=4, width=14, borderwidth=4)

display.grid(row=0, column=0, columnspan=4)

# Create buttons for digits 0-9

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create a grid of buttons
row_val = 1
col_val = 0
for button in buttons:
    Button(something, text=button, padx=20, pady=20, font=('Arial', 18),
           command=lambda b=button: display.insert(END, b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Function to clear the display
def clear_display():
    display.delete(0, END)

# Function to evaluate the expression in the display
def evaluate_expression():
    try:
        result = eval(display.get())
        display.delete(0, END)  
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, END)
        display.insert(0, "Error")

# Bind the clear button
Button(something, text='C', padx=20, pady=20, font=('Arial', 18),
       command=clear_display).grid(row=row_val, column=1)
# Bind the equals button
Button(something, text='=', padx=20, pady=20, font=('Arial',
    18),
        command=evaluate_expression).grid(row=row_val, column=2)

# Start the main loop
something.mainloop()