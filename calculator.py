import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if current == '0':
        display_var.set(symbol)
    else:
        display_var.set(current + symbol)

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except:
        display_var.set("Error")

def clear():
    display_var.set("0")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a variable to store the display value
display_var = tk.StringVar()
display_var.set("0")

# Create the display
display = tk.Entry(root, textvariable=display_var, font=('Arial', 18), bd=5, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=('Arial', 14), padx=20, pady=10,
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=column)

# Clear button
clear_button = tk.Button(root, text='C', font=('Arial', 14), padx=20, pady=10, command=clear)
clear_button.grid(row=5, column=0, columnspan=3)

# Equal button
equal_button = tk.Button(root, text='=', font=('Arial', 14), padx=20, pady=10, command=calculate)
equal_button.grid(row=5, column=3)

# Run the application
root.mainloop()
