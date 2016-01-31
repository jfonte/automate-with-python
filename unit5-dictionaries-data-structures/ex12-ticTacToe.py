# tictactoe
# 


theBoard = {'top-L':' ', 'top-M':' ','top-R':' ',
'mid-L':' ', 'mid-M':' ', 'mid-R':' ','low-L':' ', 'low-M':' ', 'low-R':' '}

# print(type(theBoard))
count = 1;

# print board or function to 'model' tictactoe board

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# initialize turn
turn = 'X'

for i in range(9):
	printBoard(theBoard)
	print('Turn for ' +turn + '. Move on which space?')
	move = input()
	theBoard[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'

printBoard(theBoard)








# TODO -> REFACTOR CODE to use a loop to draw stuff
'''
for v in theBoard.values():
	print(v,end="");
	count+=1;
	if count%1==0 or count%2==0:
		print('|',end="");
	if count%3==0:
		print('\n'+'-+-+-');
'''

