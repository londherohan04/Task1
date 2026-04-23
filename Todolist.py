# Simple To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        print(f"Task '{removed}' deleted.")
    except:
        print("Invalid input!")

def update_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to update: "))
        new_task = input("Enter updated task: ")
        tasks[task_no - 1] = new_task
        print("Task updated successfully!")
    except:
        print("Invalid input!")

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
