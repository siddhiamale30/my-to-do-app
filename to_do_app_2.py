import json
import os
from datetime import datetime

# Define a list to store tasks
tasks = []

# Function to display the to-do list
def show_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']}")

# Function to add a task
def add_task():
    title = input("Enter the task title: ")
    priority = input("Enter the task priority (High, Medium, Low): ").capitalize()
    due_date_str = input("Enter the due date (YYYY-MM-DD): ")
    
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        task = {
            'title': title,
            'priority': priority,
            'due_date': due_date.strftime("%Y-%m-%d")
        }
        tasks.append(task)
        print(f"Task '{title}' added to the to-do list.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Function to remove a task
def remove_task():
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['title']}' removed from the to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to save tasks to a JSON file
def save_tasks(filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

# Function to load tasks from a JSON file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []

# Main loop
if __name__ == "__main__":
    filename = "tasks.json"
    tasks = load_tasks(filename)

    while True:
        print("\nOptions:")
        print("1. Show to-do list")
        print("2. Add task")
        print("3. Remove task")
        print("4. Save tasks")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            save_tasks(filename)
            print(f"Tasks saved to '{filename}'.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
