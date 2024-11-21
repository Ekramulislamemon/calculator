import tkinter as tk

# Function to update the expression in the display
def click_button(value):
    current_expression = display.get()
    display.delete(0, tk.END)  # Clear the display
    display.insert(tk.END, current_expression + value)  # Add the clicked value

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(display.get())  # Evaluate the expression
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))  # Show the result
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")  # Show error if invalid expression

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the display entry widget
display = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4)

# Define the button layout and labels
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Add buttons to the GUI
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=evaluate_expression)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear_display)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: click_button(value))
    button.grid(row=row, column=col)

# Run the application
root.mainloop()
