import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")
        
        label_result.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Enter the first number:").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the second number:").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Choose an operation:").grid(row=2, column=0, padx=10, pady=5)

operation_var = tk.StringVar(root)
operation_var.set("+")
operations_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operations_menu.grid(row=2, column=1, padx=10, pady=5)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, columnspan=2, pady=10)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, columnspan=2, pady=5)

root.mainloop()