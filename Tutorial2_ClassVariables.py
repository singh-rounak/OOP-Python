class Employee:
	
	num_employees = 0 
	raise_amount = 1.04  # Class Variable

	#CONSTRUCTOR
	def __init__(self,first, last,pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@company.com'
		self.pay = pay

		Employee.num_employees +=1

	# def Printname(self):
	# 	return "{} {}" .format(self.first,self.last)

	def Printname(self):
		print(self.first +' ' + self.last)

	def Print_Email(self):
		print(self.email)

	def Compensation(self):
		print(self.pay)

	def applyRaise(self):
		self.pay = self.pay * self.raise_amount
		print(self.pay)


"""
Instantiation : Object   = Class_name(Arguments) ---> Instance 
"""
emp1 = Employee("Ronny", 'Singh',160000)
emp2 = Employee('Bobby', 'Singh', 200000)
#print('///////////////')

emp1.applyRaise()

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

#print(employee1.Printname())

#print(Employee.num_employees)