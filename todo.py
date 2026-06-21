import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

FILE_NAME = "tasks.json"


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Management System")
        self.root.geometry("850x550")
        self.root.resizable(False, False)

        self.tasks = []

        # ---------------- Heading ----------------
        title = tk.Label(
            root,
            text="TO-DO LIST MANAGEMENT SYSTEM",
            font=("Arial", 20, "bold"),
            bg="#4CAF50",
            fg="white",
            pady=10,
        )
        title.pack(fill="x")

        # ---------------- Input Frame ----------------
        input_frame = tk.Frame(root, pady=10)
        input_frame.pack(fill="x")

        tk.Label(input_frame, text="Task").grid(row=0, column=0, padx=5)

        self.task_entry = tk.Entry(input_frame, width=30)
        self.task_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Priority").grid(row=0, column=2)

        self.priority = ttk.Combobox(
            input_frame,
            values=["High", "Medium", "Low"],
            state="readonly",
            width=12,
        )
        self.priority.current(1)
        self.priority.grid(row=0, column=3)

        tk.Label(input_frame, text="Due Date").grid(row=0, column=4)

        self.due_entry = tk.Entry(input_frame, width=15)
        self.due_entry.grid(row=0, column=5)

        # ---------------- Buttons ----------------
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Add Task",
            bg="#4CAF50",
            fg="white",
            width=15,
            command=self.add_task,
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Update",
            bg="#2196F3",
            fg="white",
            width=15,
            command=self.update_task,
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            bg="#f44336",
            fg="white",
            width=15,
            command=self.delete_task,
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Complete",
            bg="#9C27B0",
            fg="white",
            width=15,
            command=self.complete_task,
        ).grid(row=0, column=3, padx=5)

        # ---------------- Table ----------------
        columns = ("Task", "Priority", "Due Date", "Status")

        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=16)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=180)

        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side="left", padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

        self.load_tasks()

    # ---------------- Save ----------------
    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.tasks, file, indent=4)

    # ---------------- Load ----------------
    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                self.tasks = json.load(file)

        self.refresh_table()

    # ---------------- Refresh ----------------
    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())

        for task in self.tasks:
            self.tree.insert(
                "",
                "end",
                values=(
                    task["task"],
                    task["priority"],
                    task["due"],
                    task["status"],
                ),
            )

    # ---------------- Add ----------------
    def add_task(self):
        task = self.task_entry.get().strip()
        priority = self.priority.get()
        due = self.due_entry.get().strip()

        if task == "":
            messagebox.showerror("Error", "Enter Task Name")
            return

        self.tasks.append(
            {
                "task": task,
                "priority": priority,
                "due": due,
                "status": "Pending",
            }
        )

        self.save_tasks()
        self.refresh_table()

        self.task_entry.delete(0, tk.END)
        self.due_entry.delete(0, tk.END)

    # ---------------- Delete ----------------
    def delete_task(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning("Warning", "Select a task.")
            return

        index = self.tree.index(selected[0])

        self.tasks.pop(index)

        self.save_tasks()
        self.refresh_table()

    # ---------------- Complete ----------------
    def complete_task(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning("Warning", "Select a task.")
            return

        index = self.tree.index(selected[0])

        self.tasks[index]["status"] = "Completed"

        self.save_tasks()
        self.refresh_table()

    # ---------------- Update ----------------
    def update_task(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning("Warning", "Select a task.")
            return

        index = self.tree.index(selected[0])

        self.tasks[index]["task"] = self.task_entry.get()
        self.tasks[index]["priority"] = self.priority.get()
        self.tasks[index]["due"] = self.due_entry.get()

        self.save_tasks()
        self.refresh_table()

        self.task_entry.delete(0, tk.END)
        self.due_entry.delete(0, tk.END)


# ---------------- Main ----------------
root = tk.Tk()
app = TodoApp(root)
root.mainloop()