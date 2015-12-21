this = ['fuck','merde', 'putain']
that = [1,5,2,3,4,5,82123,-43]

that.sort()
print(that)

# strings are immutable

try:
	name = 'zoe the cat'
	name[0] = 'p'
	print(name)
except:
	print('error overlord')


# to mutate strings, instead use slicing and concatenation to build new strings

name = 'zoe the cat'
newName = 'p'+name[1:]
print(newName)