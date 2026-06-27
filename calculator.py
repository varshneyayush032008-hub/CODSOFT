import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Warning", "Please select an operation!")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Heading
title = tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold"))
title.pack(pady=10)

# First Number
tk.Label(root, text="First Number:").pack()
entry1 = tk.Entry(root, width=25)
entry1.pack(pady=5)

# Second Number
tk.Label(root, text="Second Number:").pack()
entry2 = tk.Entry(root, width=25)
entry2.pack(pady=5)

# Operation Selection
tk.Label(root, text="Select Operation:").pack()

operation_var = tk.StringVar(value="+")

frame = tk.Frame(root)
frame.pack()

tk.Radiobutton(frame, text="+", variable=operation_var, value="+").grid(row=0, column=0)
tk.Radiobutton(frame, text="-", variable=operation_var, value="-").grid(row=0, column=1)
tk.Radiobutton(frame, text="*", variable=operation_var, value="*").grid(row=0, column=2)
tk.Radiobutton(frame, text="/", variable=operation_var, value="/").grid(row=0, column=3)

# Calculate Button
calc_btn = tk.Button(root, text="Calculate", command=calculate,
                     bg="blue", fg="white", font=("Arial", 12))
calc_btn.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack()

# Run application
root.mainloop()