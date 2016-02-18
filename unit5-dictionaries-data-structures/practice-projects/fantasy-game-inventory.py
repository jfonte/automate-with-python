# whoopie kayekayo!
# WHAT THIS IS
# function that takes a dictionary and dresses it up in a fancy way and sums up total items in keys! yay SO FUN!
'''
the end result needs to look like this:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger

Total number of items: 63”
'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
order = ['arrow', 'gold coin', 'rope', 'torch', 'dagger']

def displayInventory(mystuff):
	tot = 0
	print('Inventory:')
	for i in order:
	    print(stuff[i], i)
	    tot+=stuff[i]
	print('Total number of items: ' +str(tot))

# displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
	# first we access the loot
	for i in addedItems:
		# then we open the box and add the loot
		if i in inventory.keys():
			inventory[i]+=1
		else:
			inventory.setdefault(i,1)
	return inventory

print(addToInventory(stuff, dragonLoot))


