tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' deleted.")
    else:
        print(f"Task '{task}' not found.")

def show_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")

while True:
    print("\nTodo App Menu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to delete: ")
        delete_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Exiting Todo App.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
