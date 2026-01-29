class student:
	def __init__(self,name,m1,m2,m3):
		self.name = name
		self.m1= m1
		self.m2 = m2
		self.m3 = m3
	
	def total(self):
		self.total_mark=self.m1 + self.m2 + self.m3
		return self.total_mark

	def display(self):
		print("Name: ", self.name)
		print("Mark1: ", self.m1)
		print("Mark2: ", self.m2)
		print("Mark3: ", self.m3)
		print("Total: ", self.total_mark)

obj = student("Ajay", 80, 60, 70)
print(obj.total())
obj.display()
