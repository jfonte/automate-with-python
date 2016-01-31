spam = {'color': 'red', 'age': 42}
for v in spam.values():
	print(v)

for v in spam.keys():
	print(v)

for v in spam.items(): # returned as a tuple
	print(list(v))
