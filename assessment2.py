# To-Do List Manager
tasks = []  

# List to store tasks
while True:
    print(" To-Do List Manager ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Task
    if choice == "1":
        task = input("Enter the task to add: ")
        tasks.append(task)
        print("Task '{task}' added successfully!")

    # View Tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Remove Task
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    # Exit Program
    elif choice == "4":
        print("Exiting the To-Do List Manager.")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 4.")
