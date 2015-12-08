spam = [1,2,3,4,5]
print(spam)
del spam[4]
print(spam)
del spam # unassigns the variable
try: 
	print(spam)
except:
	print('sorry, you made an mistake')