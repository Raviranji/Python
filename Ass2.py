#Task manager list
a=[]

#List to store
while True:
    print(" Task manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Task
    if choice == "1":
        task =input("Enter your task: ")
        a.append(task)
        print("Task added")

    # View Tasks
    elif choice == "2":
        if(len(a)==0):
            print("No Task added ")
        else:
            for i in range(len(a)):
                print(i+1," ",a[i])

    # Remove Task
    elif choice == "3":
        if(len(a)==0):
            print("No Task to remove ")
        else:
            for i in range(len(a)):
                print(i+1," ",a[i])

        num =int(input("Task number to be removed: "))
        if num>0 and num<=len(a):
            a.pop(num-1)
            print("Task removed")
        else:
            print("Invalid number ")

    # Exit Program
    elif choice == "4":
            print("Exit the process") 
            break
    else:
        print("Invalid choice ")
