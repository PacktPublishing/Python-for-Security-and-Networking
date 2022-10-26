#!/usr/bin/python3

class MainClass:
     
    def message_main(self):
        print('Welcome to Main Class')
 
class Child(MainClass):
 
    def message_child(self):
        print('Welcome to Child Class')
        print('This is inherited from Main')
 
class ChildDerived(Child):
 
    def message_derived(self):
        print('Welcome to Derived Class')
        print('This is inherited from Child')
 
if __name__ == '__main__':        
	child_derived_obj = ChildDerived()
	child_derived_obj.message_main()
	child_derived_obj.message_child()
	child_derived_obj.message_derived()

	print(issubclass(ChildDerived, Child))
	print(issubclass(ChildDerived, MainClass))
	print(issubclass(Child, MainClass))
	print(issubclass(MainClass, ChildDerived))

	print(isinstance(child_derived_obj, Child))
	print(isinstance(child_derived_obj, MainClass))
	print(isinstance(child_derived_obj, ChildDerived))
