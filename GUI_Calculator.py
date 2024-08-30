import tkinter as tk

# Function to evaluate the expression
def evaluate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to append the clicked button text to the entry
def append(text):
    entry.insert(tk.END, text)

# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying input and results
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=evaluate)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: append(t))
    btn.grid(row=row, column=col, sticky="nsew")

# Clear button
btn_clear = tk.Button(root, text="C", padx=20, pady=20, command=clear)
btn_clear.grid(row=4, column=3, sticky="nsew")

# Bind the Enter key to evaluate function
root.bind('<Return>', evaluate)

# Configure the grid
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the main loop
root.mainloop()
