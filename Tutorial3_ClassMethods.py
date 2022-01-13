
'''
NOTES:
1.Regular Methods in a class automatically pass 'instance' as first argument: (self)

2.Class Methods automatically pass 'class' as first argument: (cls)

3.Static Methods don't pass anything automatically, neither instance(self) nor class(cls)
	They are used as regular function because they have some logical connection with the class.

Class Methods are often used to replace constructors

'''

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

	#REGULAR METHODS
	def Printname(self):
		print(self.first +' ' + self.last)

	def Print_Email(self):
		print(self.email)

	def Compensation(self):
		print(self.pay)

	def applyRaise(self):
		self.pay = self.pay * self.raise_amount
		print(self.pay)


	#ClASS METHOD
	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	#STATIC METHOD:
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() ==6:
			return False
		return True



emp_str1 = 'Ronny-Singh-160000'
#emp_str2 = 'Bobby-Singh-200000'


#INSTANCE CREATION / OBJECT INSTANTIATION : 
#Object   = Class_name.class_method(Arguments)
New_emp = Employee.from_string(emp_str1)

print(New_emp.pay)

print("Employee Count = {}".format(Employee.num_employees))

# print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

import datetime
my_date = datetime.date(2016,7,11)
print("Is a Workday = {}".format(Employee.is_workday(my_date)))
