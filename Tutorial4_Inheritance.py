class Employee:
	
	raise_amount = 1.04  # Class Variable

	#CONSTRUCTOR
	def __init__(self,first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@company.com'
		self.pay = pay


	# def Printname(self):
	# 	return "{} {}" .format(self.first,self.last)

	def Fullname(self):
		print(self.first +' ' + self.last)

	def Print_Email(self):
		print(self.email)

	def Compensation(self):
		print(self.pay)

	def applyRaise(self):
		self.pay = self.pay * self.raise_amount
		print(self.pay)

#INHERITANCE: class Child_class(Parent_class):
class Developer(Employee):
	raise_amount = 1.10

	def __init__(self,first, last, pay, prog_lang):
		Employee.__init__(self,first, last ,pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	def __init__(self,first, last, pay, employees = None):
		Employee.__init__(self,first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def rem_employee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def Print_employee(self):
		for emp in self.employees:
			print('{}'.format(emp.Fullname()))



dev_1 = Developer('Patel', 'Sahab', 212000, 'Python') 
dev_2 = Developer('Mr', 'Singh', 222000, 'Java')

mang_1 = Manager('Sue', 'Pat', 90000, [dev_1])

print(isinstance(mang_1, Developer))
print(issubclass(Developer, Employee))

#mang_1.add_employee(dev_2)
# print(dev_1.pay)
# dev_1.applyRaise()

# print(dev_1.email)
# print(dev_1.prog_lang)

# dev_1.Print_Email()
# dev_2.Print_Email()

