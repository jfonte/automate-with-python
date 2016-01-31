# get() method looks for key and returns a value you define if not found

picnicItems = {'apples':5,'cups':2}

print('i am bringing ' +str(picnicItems.get('cups',0))+ ' cups.')

# the 0 value is used as a default value to return in case a key does not exist

print('i am bringing ' +str(picnicItems.get('eggs',0))+ ' eggs.')
