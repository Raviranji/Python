class Employee: #base class
    def __init__(self, name, id, basic_salary):
        self.name = name
        self.id = id
        self.basic_salary = basic_salary

    def display(self):
        print("  Employee Basic Details: ")
        print("Name       :", self.name)
        print("ID         :", self.id)
        print("Basic Pay  :", self.basic_salary)
        
class Developer(Employee): #dervied class1
    def __init__(self, name, id, basic_salary, project_bonus):
        super().__init__(name, id, basic_salary)
        self.project_bonus = project_bonus

    def total_salary(self):
        return self.basic_salary + self.project_bonus
    
    def display(self):
        super().display()
        print("Pro bonus  :", self.project_bonus)

class Manager(Employee): #derived class2
    def __init__(self, name, id, basic_salary, hra, da):
        super().__init__(name, id, basic_salary)
        self.hra = hra
        self.da = da

    def total_salary(self):
        return self.basic_salary + self.hra + self.da
    

    def display(self):
        super().display()
        print("HRA        :", self.hra)
        print("DA         :", self.da)

# Developer Object
obj1 = Developer("Ajay", 101, 30000, 8000)
obj1.display()
print("Developer Total Salary:", obj1.total_salary())
print()

# Manager Object
obj2 = Manager("Mahe", 201, 40000, 10000, 8000)
obj2.display()
print("Manager Total Salary  :", obj2.total_salary())
print()
