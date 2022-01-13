class Employee:
	#CONSTRUCTOR
	def __init__(self,first, last,pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@company.com'
		self.pay = pay

	# def Printname(self):
	# 	return "{} {}" .format(self.first,self.last)

	def Printname(self):
		print(self.first +' ' + self.last)

	def Print_Email(self):
		print(self.email)

	def Compensation(self):
		print(self.pay)


employee1 = Employee("Ronny", 'Singh',160000)
print('///////////////')
#Object   = Class_name(Arguments) ---> Instance 
employee1.Printname()
employee1.Print_Email()
employee1.Compensation()

#print(employee1.Printname())
employee2 = Employee('Bobby', 'Singh', 200000)
print('///////////////')

employee2.Printname()
employee2.Print_Email()
employee2.Compensation()
print('///////////////')
Employee.Printname(employee1)