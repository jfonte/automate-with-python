# 2015-12-08
# methods: are like functions. each data type has a series of methods that can be called upon them

# example: find a value in a list using the index() method

spam = ['joshua', 'michael', 'jamie', 'josh', 'joshua']

try:
	print(spam.index('josh'))
	print(spam.index('joshua'))
	print(spam.index('sarah')) # will return error

except:
	print('value not found dude')

# example: adding values to lists with append() and insert()

spam.append('moose')
print(spam)

spam.insert(0,'chicken')
print(spam)

# neither append() nor insert() gives the new value of spam as its return value. As a matter of fact, the return value of append() is NONE. The list is modified in place. This is something you will learn later denominated "mutable and immutable objects"

# also, methods belong to a single data type. You can't use list methods on string for example.

# example: removing values from lists with remove()

spam.remove('joshua') # removes the FIRST instance of 'joshua'
print(spam)

try:
	spam.remove('rat')
except:
	print("ERROR: you can't remove something that does not exist amigo!")

# the del statement is great to use when you know the index of the value you want to remove from the list. the remove() method is useful when you know the value you want to remove.

# silly way to empty list

this = len(spam)
for i in range (0,this):
	del(spam[0])

print(spam)


