a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a>b and a>c:
    print(a, "is the greatest of all numbers.")
elif b>c:
    print(b, "is the greatest of all numbers.")
else:
    print(c, "is the greatest of all numbers.")
