# Create a dictionary with students and their marks
students = {
   "Ajay": 85,
    "Chandru": 78,
    "Dhanalakshmi": 98
}

# Print all students with their marks
print("All students and their marks:")
for i, mark in students.items():
    print(f"{i}: {mark}")

# Find the highest mark
high_mark = max(students.values())
print("Highest mark:", high_mark)

# Find the student who got the highest mark
for i, mark in students.items():
    if mark == high_mark:
        print("Student with the highest mark:", i)
        break
