birthdays = {'alice': 'apr 1', 'bob':'dec 12', 'carol': 'mar 4'}

while True: 
	print('enter a name: (blank to quit) ')
	name = input()
	if name == '':
		break

	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' +name)
	else:
		print('i do not have bday info for ' +name)
		print('what is their bday?')
		bday= input()
		birthdays[name] = bday
		print('Birthdays updated.')

# data is not saved but you will learn how to save data iin ch8

