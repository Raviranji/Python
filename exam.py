
total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter attended classes: "))
medical = input("Medical certificate (Yes/No): ").strip().lower()

if attended_classes > total_classes or total_classes <= 0:
    print("Invalid input")
else:
    attendance = (attended_classes / total_classes) * 100
    print(f"Attendance: {attendance:.2f}%")

    if attendance >= 75:
        print("Result: Eligible (Attendance is 75% or more)")
    else:
        if medical == "yes":
            print("Result: Eligible (Medical certificate provided)")
        else:
            print("Result: Not Eligible (Low attendance and no medical certificate)")
