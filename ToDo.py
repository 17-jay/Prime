import tkinter as tk  # Import Tkinter for GUI development
from tkinter import messagebox  # Import messagebox for pop-up alerts

# Function to add a task to the list
def add_task():
    task = task_entry.get()  # Get the task from the input field
    if task:  # Ensure the task is not empty
        task_listbox.insert(tk.END, task)  # Add task to the listbox
        task_entry.delete(0, tk.END)  # Clear the input field after adding
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")  # Show warning if input is empty

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get index of selected task
        task_listbox.delete(selected_task_index)  # Remove task from listbox
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")  # Show warning if no task selected

# Function to save tasks to a file
def save_tasks():
    tasks = task_listbox.get(0, tk.END)  # Get all tasks from the listbox
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")  # Write each task on a new line
    messagebox.showinfo("Success", "Tasks saved successfully!")  # Show success message

# Function to load tasks from a file when the app starts
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file.readlines():
                task_listbox.insert(tk.END, task.strip())  # Add tasks to the listbox
    except FileNotFoundError:
        open("tasks.txt", "w").close()  # Create the file if it doesn't exist

# Function to update the selected task
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        new_task = task_entry.get()  # Get the new task text
        if new_task:
            task_listbox.delete(selected_task_index)  # Remove the old task
            task_listbox.insert(selected_task_index, new_task)  # Insert updated task
            task_entry.delete(0, tk.END)  # Clear input field
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")  # Show warning if input is empty
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")  # Show warning if no task is selected

# Create the main application window
root = tk.Tk()
root.title("To-Do List")  # Set window title
root.geometry("317x317")  # Set window size
root.configure(bg="#282c34")  # Set background color

# Create a Label for the title
title_label = tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), bg="#282c34", fg="white")
title_label.pack(pady=10)

# Create an Entry widget for user input
task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.pack(pady=5)

# Create buttons for adding, deleting, updating, and saving tasks
btn_add = tk.Button(root, text="Add Task", command=add_task, width=20, bg="#61afef", fg="white", font=("Arial", 10, "bold"))
btn_add.pack(pady=2)

btn_update = tk.Button(root, text="Update Task", command=update_task, width=20, bg="#e5c07b", fg="black", font=("Arial", 10, "bold"))
btn_update.pack(pady=2)

btn_delete = tk.Button(root, text="Delete Task", command=delete_task, width=20, bg="#e06c75", fg="white", font=("Arial", 10, "bold"))
btn_delete.pack(pady=2)

btn_save = tk.Button(root, text="Save Tasks", command=save_tasks, width=20, bg="#98c379", fg="black", font=("Arial", 10, "bold"))
btn_save.pack(pady=2)

# Create a Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
task_listbox.pack(pady=10)

# Load previous tasks when app starts
load_tasks()

# Run the Tkinter event loop
root.mainloop()
