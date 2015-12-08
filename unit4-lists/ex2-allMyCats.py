catNames = []
while True:
	print('Enter the name of cat ' +str(len(catNames) +1) + ' (or enter nothing to stop.):')
	name = input()
	if name =='':
		break
	catNames = catNames+[name] # start list concatenation
print('the current cat names are:')
for name in catNames:
	print(name+' ')
