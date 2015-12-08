def collatz(number):
	if number%2 == 0:
		return number//2
	elif number%2 ==1:
		return 3*number+1
	else:
		print('number is neither even nor odd')

try:
	# mynumber = input('enter your number please! ')
	mynumber = 0
	while collatz(int(mynumber))!=1:
		mynumber = input('Type your number: ')
except:
	print('whoops something went wrong partner. are you sure you typed a number?')

