class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        print("\n--- Add New Student ---")
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return

        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Invalid age! Please enter a number.")
            return

        student_id = input("Enter student ID: ").strip()
        if not student_id:
            print("Student ID cannot be empty!")
            return

        # Check for duplicate ID
        for s in self.students:
            if s.student_id == student_id:
                print("A student with this ID already exists!")
                return

        new_student = Student(name, age, student_id)
        self.students.append(new_student)
        print("Student added successfully!")

    def view_students(self):
        print("\n--- All Students ---")
        if not self.students:
            print("No students found.")
            return

        for idx, student in enumerate(self.students, start=1):
            print(f"{idx}. {student}")

    def search_student_by_name(self):
        print("\n--- Search Student ---")
        name = input("Enter name to search: ").strip().lower()
        if not name:
            print("Name cannot be empty!")
            return

        found = [s for s in self.students if s.name.lower() == name]

        if not found:
            print("No student found with that name.")
        else:
            print(f"Found {len(found)} student(s):")
            for s in found:
                print(s)

    def delete_student_by_name(self):
        print("\n--- Delete Student ---")
        name = input("Enter name to delete: ").strip().lower()
        if not name:
            print("Name cannot be empty!")
            return

        # Find all students with that name
        matched = [s for s in self.students if s.name.lower() == name]

        if not matched:
            print("No student found with that name.")
            return

        if len(matched) == 1:
            self.students.remove(matched[0])
            print("Student deleted successfully.")
        else:
            print(f"Multiple students found with the name '{name}':")
            for i, s in enumerate(matched, start=1):
                print(f"{i}. {s}")
            try:
                choice = int(input("Enter the number of the student to delete: "))
                if 1 <= choice <= len(matched):
                    self.students.remove(matched[choice - 1])
                    print("Student deleted successfully.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")


def print_menu():
    print("\n===== Student Management System =====")
    print("1. Add new student")
    print("2. View all students")
    print("3. Search student by name")
    print("4. Delete student by name")
    print("5. Exit")


def main():
    manager = StudentManager()

    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            manager.add_student()
        elif choice == 2:
            manager.view_students()
        elif choice == 3:
            manager.search_student_by_name()
        elif choice == 4:
            manager.delete_student_by_name()
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
