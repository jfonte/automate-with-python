# review

spam = 42
cheese = spam
print(spam)
print(cheese) # points to a value NOT a variable

# changeing spam does not affect cheese

spam = 32
print(spam)
print(cheese)

# lists don't work this way. When you assign a list to a variable you're actually assigning a list REFERENCE to the variable

# a reference is a value that points to some bit of data, and a list reference is a value that points to a list.

# example

spam = [0,1,2,3,4,5] # the variable contains the reference TO THE LIST, not the values themself
cheese = spam # cheese is pointing to the list's reference
cheese[1]='Hello'
print(cheese)
print(spam)

# when we create the list, we're actually assigning a reference to it in the spam variable. the second assignment above is merely copying the list reference in spam to cheese, NOT the list value itself. Both values refer to the same list.

# altering any variable that makes reference to a list, changes the list and thereby all references/variables to it!

# python uses references for mutable data types like lists & dictionaries, but stores values for immutable data types like strings, integers and tuples