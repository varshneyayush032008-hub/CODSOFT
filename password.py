import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return

        characters = ""

        if lowercase_var.get():
            characters += string.ascii_lowercase
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


# Function to copy password
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first.")


# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("420x360")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

# Title
title = tk.Label(root, text="🔐 Password Generator",
                 font=("Arial", 18, "bold"),
                 bg="#f4f4f4")
title.pack(pady=10)

# Password Length
tk.Label(root, text="Password Length:",
         font=("Arial", 11),
         bg="#f4f4f4").pack()

length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

# Checkboxes
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Lowercase (a-z)", variable=lowercase_var,
               bg="#f4f4f4").pack(anchor="w", padx=100)

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=uppercase_var,
               bg="#f4f4f4").pack(anchor="w", padx=100)

tk.Checkbutton(root, text="Numbers (0-9)", variable=numbers_var,
               bg="#f4f4f4").pack(anchor="w", padx=100)

tk.Checkbutton(root, text="Symbols (!@#$)", variable=symbols_var,
               bg="#f4f4f4").pack(anchor="w", padx=100)

# Generate Button
generate_btn = tk.Button(root,
                         text="Generate Password",
                         command=generate_password,
                         bg="#4CAF50",
                         fg="white",
                         font=("Arial", 11, "bold"))
generate_btn.pack(pady=10)

# Password Display
password_entry = tk.Entry(root,
                          font=("Arial", 12),
                          width=30,
                          justify="center",
                          state="readonly")
password_entry.pack(pady=5)

# Copy Button
copy_btn = tk.Button(root,
                     text="Copy Password",
                     command=copy_password,
                     bg="#2196F3",
                     fg="white",
                     font=("Arial", 11, "bold"))
copy_btn.pack(pady=10)

root.mainloop()