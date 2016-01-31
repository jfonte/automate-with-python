import pprint

message = 'It was a bright cold day in April and the clocks were striking thirteen'

count = {}

for character in message:
	count.setdefault(character, 0)
	count[character]=count[character]+1

pprint.pprint(count)

# You can also get the output as a string value with pprint.pformat(), which is the same as the above code

print(pprint.pformat(count))

