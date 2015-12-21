# tuples are like lists but defined with () instead of [], however they are like strings in that they are immutable

eggs = ('hello',42,0.5)
print(eggs[0])

try:
	eggs[1]=99
except:
	print('sorry buddy, you can\'t do that')

# it's possible to tell python you are defining a one value tuple by indicating it with a trailing comma

print(type(('hello',)))

# tuples are useful when you need an ordered sequence of values that will never change. Because they are immutable, Python can implement optimizations that make code using tuples slightly faster than code using lists

# it's possible to convert types with the list() and tuple() functions

print(tuple(['cat','dog',5]))
print(list(eggs))

# converting is useful if you want a mutable version of a tuple value