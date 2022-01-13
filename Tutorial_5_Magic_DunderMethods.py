
"""
NOTES: dunder methods('__abc__') are basically functions with underscores that have a special representation.

1.'__repr__': is used for unambiguous representation of the object 
and is used for debugging and logging - for developers

2.'__str__': is meant to be a readable representation of the object 
- display to end user

"""


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

	def applyRaise(self):
		self.pay = self.pay * self.raise_amount
		print(self.pay)

	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

	def __str__(self):
		return '{}-{}'.format(self.Printname(), self.email)


emp1 = Employee("Ronny", 'Singh',160000)




print(repr(emp1))
print(str(emp1))
