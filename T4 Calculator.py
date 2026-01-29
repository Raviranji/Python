a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
opr = input("Enter the operator (+, -, *, /): ")

if opr == '+':
            res = a + b
elif opr == '-':
            res = a - b
elif opr == '*':
            res = a * b
elif opr == '/':
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        res = a / b
else:
    print("Error: Invalid operator.")

print(f"The result of {a} {opr} {b} is: {res}")