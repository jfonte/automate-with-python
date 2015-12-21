# sort() method sorts shit out!

spam = [2,5,3.14,1, -7]
spam.sort()
print(spam)

# reverse sort()

spam.sort(reverse=True) 
print(spam)

# sorts IN PLACE assignment does not work!
something = spam.sort()
print(something)

# you can not sort both numbers and strings

try:
	spam = [1,2,3,4,'alice','bob']
	print(spam.sort())
except:
	print("sorry buddy this won't work!")

# sort works with lowercase and uppercase letters, from uppercase first and then into lowercase

spam=['Alice','ants','Bob','badgers','Carol','cats']
spam.sort()
print(spam)

# if one needs to sort values alphabetically, you can use the ```str.lower``` for the ```key``` keyword argument in sort(). This causes the sort() function to treat everything as lowercase without changing anything

span = ['a','z','A','Z']
spam.sort(key=str.lower)
print(spam)

