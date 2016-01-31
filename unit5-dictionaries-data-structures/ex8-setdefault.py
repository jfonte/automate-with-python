# example of setting a value in a dict for a key ONLY if that key does not have a value

# spam = {'name':'Pooka','age':5}
# 
# print(spam)
# if 'color' not in spam: #so if key does not exist
# 	spam['color']='black'

''' 
with setdefault() you can do this in one line
the 1st argument is the key to check, 
the 2nd argument is the value to set if the key does NOT exist.
IF the key exists, setdefault() returns the key's value.
'''

spam = {'name':'Pooka','age':5}

print(spam)

spam.setdefault('color','black') # returns black and adds it to dict

print(spam)

print(spam.setdefault('color','white')) # key exists so nothing is changed

print(spam)

