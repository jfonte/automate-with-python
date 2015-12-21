# sometimes when using lists and other mutable objects in functions, you  might not want to modify the original list. For this, Python has a module called ```copy``` with two very useful functions: copy() and deepcopy()

# copy.copy() can be used to make a duplicate copy of a mutable value like a list or dictionary

import copy
spam = ['a','b','c','d']
cheese=copy.copy(spam)
cheese[0]=42
print(spam)
print(cheese)

# spam and cheese now refer to different separate lists.

# copy.deepcopy is used when you need to copy a list that contains lists
# the deepcopy() function does this as well

