import collections

message = 'It was a bright cold day in April and the clocks were striking thirteen'

count = {}

# counts shit
for character in message:
	count.setdefault(character, 0)
	count[character]=count[character]+1

ordered = collections.OrderedDict(sorted(count.items()))

for k,v in ordered.items(): 
	print('Char: '+ '\'' + str(k) + '\' ' + 'count is: '+str(v))