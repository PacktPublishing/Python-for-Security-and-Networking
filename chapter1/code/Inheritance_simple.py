#!/usr/bin/python3

class BaseClass:

	def __init__(self, property):
		self.property = property

	def message(self):
		print('Welcome to Base Class')
	
	def message_base_class(self):
		print('This is a message from Base Class')

class ChildClass(BaseClass):

	def __init__(self, property):
         BaseClass.__init__(self, property)

	def message(self):
		print('Welcome to ChildClass')
		print('This is inherited from BaseClass')

if __name__ == '__main__':
	base_obj = BaseClass('property')
	base_obj.message()
	child_obj = ChildClass('property')
	child_obj.message()
	child_obj.message_base_class()

	print(issubclass(ChildClass, BaseClass))
	print(issubclass(BaseClass, ChildClass))

	print(isinstance(base_obj, BaseClass))
	print(isinstance(child_obj, ChildClass))
	print(isinstance(child_obj, BaseClass))
