def spam(divideBy):
	return 42 / divideBy

try:
	print(spam(2))
	print(spam(12))
	print(spam(0))
	print(spam(1)) # when an exception occurs here, the try clause STOPS
except ZeroDivisionError:
	print('problem in your code human!')



