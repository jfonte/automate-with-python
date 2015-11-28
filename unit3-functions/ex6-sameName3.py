def spam():
	global eggs # you can declare global variables within functions
	eggs = 'spam'


def bacon():
	eggs = 'bacon'

def ham():
	print(eggs)

eggs = 42
print(eggs)
spam()
print(eggs)