# ==================
# continue statement
# ==================
# similar to break statements. when a 'continue' statement is reached, the program JUMPS back to the start of the loop and reevaluates the loop's condition.

while True:
	print('Who are you? ')
	name = raw_input()
	if name != 'Joshua':
		print('Sorry. Wrong answer. I am not expecting you.')
		continue
	print("Greetings Professor. Could you tell me the password please? (HINT: It is a fish)")
	password = raw_input()
	if password == 'swordfish':
		break
	else:
		print('Sorry. Wrong answer. You must start again.')
print('Verification complete. Access granted.')