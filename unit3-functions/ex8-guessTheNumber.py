# this is a guess the number game

import random
secretNumber = random.randint(1,20)
print('I am thinking of a number betweeen 1 and 20.\nCan you guess the number?')

# ask the player to guess 6 times.
for guessesTaken in range(1,7):
	print('Take a guess')
	guess = int(input())
	if guess < secretNumber:
		print('your guess is too low')
	elif guess > secretNumber:
		print('your guess is too high')
	else:
		break # you guessed the number!

if guess == secretNumber:
	print('good job! you guessed my number in ' +str(guessesTaken) + ' guesses!')
else:
	print('Sorry. You had 7 tries and did not guess right! The number was:' +str(secretNumber))
