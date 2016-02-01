# simple tictactoe

import os # used to clear screen
import time

theBoard = {'1':' ', '2':' ','3':' ',
'4':' ', '5':' ', '6':' ','7':' ', '8':' ', '9':' '}

# print board or function to 'model' tictactoe board

def drawBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def startGame():
	os.system('clear') # clears screen
	turn = 'X' # x begins
	count = 0
	while count <9:
		os.system('clear')
		drawBoard(theBoard)
		print('Turn for ' +turn + '. Move on which space?')
		move = input()
		if move == 'e':
			raise SystemExit;
		elif move == 'd':
			break
		# check if position is already taken
		if theBoard[move] == ' ':
			theBoard[move] = turn
			count +=1
			if count>4:
				checkWinner();
			if turn == 'X':
				turn = 'O'
			else:
				turn = 'X'
		else:
			print('That position is taken.')
			time.sleep(1)
	os.system('clear')
	print('###################\n'+'# NOBODY WON! :( #\n'+'###################')

def checkWinner():
	# check rows
	if theBoard['1'] == theBoard['2'] == theBoard['3']:
		printWinnerRestart(theBoard['1'])
	elif theBoard['4'] == theBoard['5'] == theBoard['6']:
		printWinnerRestart(theBoard['4'])
	elif theBoard['7'] == theBoard['8'] == theBoard['9']:
		printWinnerRestart(theBoard['7'])
	# check cols
	elif theBoard['1'] == theBoard['4'] == theBoard['7']:
		printWinnerRestart(theBoard['4'])
	elif theBoard['2'] == theBoard['5'] == theBoard['8']:
		printWinnerRestart(theBoard['5'])
	elif theBoard['3'] == theBoard['6'] == theBoard['9']:
		printWinnerRestart(theBoard['6'])
	# check diagonals
	elif theBoard['1'] == theBoard['5'] == theBoard['9']:
		printWinnerRestart(theBoard['5'])	
	elif theBoard['3'] == theBoard['5'] == theBoard['7']:
		printWinnerRestart(theBoard['5'])

def printWinnerRestart(winner):
	os.system('clear')
	print("============================")
	drawBoard(theBoard)
	print("============================")
	print(winner+' has WON! Exiting to menu')
	resetBoard();
	menu();

def resetBoard():
	for i in range(1,10):
		theBoard[str(i)]=' '

def menu():
	print('============================\n'+'Greetings Professor Falken. ' + 'Shall we play a game of TicTacToe?\n\n'+'TYPE y TO BEGIN, OR any other key TO EXIT')
	choice = input()
	if choice == 'y':
		startGame();
	else:
		raise SystemExit;

# load menu screen
menu();

# TODO -> REFACTOR CODE to use a loop/matrix to draw stuff & checkWinner

