import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12",
    database="todo_db"
)
cursor = db.cursor()

# Function to add a task to the database
def add_task():
    task = task_entry.get()
    if task:
        sql = "INSERT INTO tasks (task) VALUES (%s)"
        cursor.execute(sql, (task,))
        db.commit()
        task_entry.delete(0, tk.END)
        load_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to load tasks from the database
def load_tasks():
    task_listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        task_listbox.insert(tk.END, f"{task[0]}. {task[1]} - {task[2]}")

# Function to delete a selected task
def delete_task():
    try:
        selected_task = task_listbox.get(tk.ACTIVE)
        task_id = selected_task.split(".")[0]  # Extract task ID
        sql = "DELETE FROM tasks WHERE id = %s"
        cursor.execute(sql, (task_id,))
        db.commit()
        load_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to update a selected task as completed
def update_task():
    try:
        selected_task = task_listbox.get(tk.ACTIVE)
        task_id = selected_task.split(".")[0]
        sql = "UPDATE tasks SET status = 'completed' WHERE id = %s"
        cursor.execute(sql, (task_id,))
        db.commit()
        load_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

# Create the GUI window
root = tk.Tk()
root.title("To-Do List")
root.geometry("350x400")
root.configure(bg="#282c34")

title_label = tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), bg="#282c34", fg="white")
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.pack(pady=5)

btn_add = tk.Button(root, text="Add Task", command=add_task, width=20, bg="#61afef", fg="white", font=("Arial", 10, "bold"))
btn_add.pack(pady=2)

btn_update = tk.Button(root, text="Mark as Completed", command=update_task, width=20, bg="#e5c07b", fg="black", font=("Arial", 10, "bold"))
btn_update.pack(pady=2)

btn_delete = tk.Button(root, text="Delete Task", command=delete_task, width=20, bg="#e06c75", fg="white", font=("Arial", 10, "bold"))
btn_delete.pack(pady=2)

task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
task_listbox.pack(pady=10)

load_tasks()  # Load tasks from database when app starts

root.mainloop()

# Close database connection when app is closed
cursor.close()
db.close()
