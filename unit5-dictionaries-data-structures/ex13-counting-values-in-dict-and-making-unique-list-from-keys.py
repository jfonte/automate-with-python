# simple program to add values from values in a dictionary and create a unique list from their keys with set()
# reference https://stackoverflow.com/questions/17218139/print-all-unique-values-in-a-python-dictionary

allGuests = {'Alice':{'apples':5, 'pretzels':12},'Bob':{'ham sandwiches':3,'apples':2},'Carol':{'cups':3,'apple pies':1}}

def totalBrought(guests, item):
	numBrought = 0
	for k,v in guests.items():
		numBrought = numBrought +v.get(item, 0)
	return numBrought

# create a list of the unique items
s = set()
for key,value in allGuests.items():
	for key in value.keys():
		s.add(key)

print('number of things brought:')
for i in s:
	print('- '+i+':'+ str(totalBrought(allGuests, i)))

		