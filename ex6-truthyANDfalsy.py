# “There are some values in other data types that conditions will consider equivalent to True and False. When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True. For example:”

name = '' # name is currently False
numOfGuests = ''
while not name: # since name is False, while cycle will run until name has something in it
	print('enter your name please: ')
	name = input()
	print('how many guests will you have? ')
	try:
		numOfGuests = int(input())
	except ValueError:
		print("You misbehaved. That is not a number.")

		
