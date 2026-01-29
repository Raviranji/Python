students =[]

def add_student():
    print("Enter the student details: ")
    name = input("Enter the name: ")
    age = input("Enter the age: ")
    roll= input("Enter the roll_no: ")
    course = input("Enter the course: ")

    students.append({"name": name, "age": age,"roll": roll, "course": course })
    print("Student details added successfully!")

def view_student():
    print("\n All students: ")
    if not students:
        print("\n No students found ")
    else:
        for s in students:
            print(f"Name: {s['name']} | Age: {s['age']} | Roll: {s['roll']} | Course: {s['course']}")
        
def search_student():
    print("\n--- Search Student ---")
    name = input("Enter name to search: ")
    found = False
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"Found: \n Name: {s['name']} | Age: {s['age']} | Roll: {s['roll']} | Course: {s['course']}")
            found = True
    if not found:
        print("No student found with that name.")

def delete_student():
    print("\n Delete Student ")
    name = input("Enter name to delete: ")
    global students
    students = [s for s in students if s["name"].lower() != name.lower()]
    print("Student deleted (if existed).")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
