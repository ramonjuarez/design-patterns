from functools import wraps 

def make_blink(function):
	'''Defines the decorator'''

	#This makes the decorator transparent in terms of its name and docstring
	@wraps(function)

	def decorator():
		#Grab the return value of the function being decorated
		ret = function()

		#Add new funcionality to the function being decorated
		return "<blink>" + ret + "</blink>"
	return decorator

#Apply the decorator here!
@make_blink
def hello_world():
	'''Original function'''
	return "hello world"

#Check the result of the decorating
print(hello_world())

#Check if the function name is still the same name of the function being decorated
print(hello_world.__name__)

#Check if the function docstring is still the same name of the function being decorated
print(hello_world.__doc__)
