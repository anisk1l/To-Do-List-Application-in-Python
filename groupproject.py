import tkinter as tk
from tkinter import messagebox
import json
import os


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []
        self.load_tasks()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame,
            width=50,
            height=10,
            selectmode=tk.SINGLE,
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(
            self.button_frame,
            text="Add Task",
            command=self.add_task,
        )
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.remove_button = tk.Button(
            self.button_frame,
            text="Remove Task",
            command=self.remove_task,
        )
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(
            self.button_frame,
            text="Mark as Complete",
            command=self.mark_complete,
        )
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.populate_tasks()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append({"task": task, "completed": False})
            self.entry.delete(0, tk.END)
            self.save_tasks()
            self.populate_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.save_tasks()
            self.populate_tasks()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def mark_complete(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            self.save_tasks()
            self.populate_tasks()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def populate_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["task"]
            if task["completed"]:
                task_text += " (completed)"
            self.listbox.insert(tk.END, task_text)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
