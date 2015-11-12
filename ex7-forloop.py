################################################
#### examples of using for loops and ranges ####
################################################

# print('My name is')
# for i in range(5):
# 	print('Jimmy Five times (' +str(i) + ')')

#################################################
### example of iterating of indices of a sequence
#################################################

#a = ['Mary', 'had', 'a', 'little', 'lamb']
#for i in range(len(a)):
#	print(i, a[i])

################################################
############## 	SYNTAX FOR RANGE ###############
################################################
############## range(start, stop, step) ########
################################################

for i in list(range(0,10,2)):
	print(i)

# for n in range (2,10):
# 	for x in range (2, n):
# 		if n % x == 0:
# 			print(n, 'equals', x, '*', n//x)
# 			break
# 		else:
# 			 print(n, 'is a prime number')

#print(range(10)) # this will return an object, if we want to create a list from the object we can use list(range(x,x,x))
