
# when a functions is called/executed, the values of the arguments are copied to the parameter variables. For mutable objects like lists, this means a copy of the reference is used for the parameter.

def eggs(someParameter):
	someParameter.append('Hello') # no return value, the list is modified in place

spam = [1,2,3]

eggs(spam)
print(spam)