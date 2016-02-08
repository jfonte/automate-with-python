# dictionary data types

- Similar to a list, a *dictionary* is a collection of many values. Unlike indexes for lists though, indexes for dictionaries can use many different data types, not just integers.
- indexes for dictionaries are called *keys*
- a key with its associated value is called a *key-value-pair*
- in code, a dictionary is typed with braces: {}
- dictionaries can still use integers as keys, but they can be any number:

```
spam = {12345: 'luggage combination', 42: 'the answer'}
```

- dictionaries are unordered. there is no "first" item in a dictionary. If you compared two lists, their order would matter. However in dictionaries, the order and even the keys DO NOT MATTER. Only their values:

```
>>> spam = ['cats',
>>>  'dogs', 'moose']
>>> bacon = ['dogs', 'moose', 'cats']
>>> spam == bacon
False
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
>>> eggs == ham
True
```

- because dictionaries are not ordered they can not be sliced like lists

## keys(), values(), and items() methods

- there are 3 methods that return list-like values from dictionary's keys, values and both: ```keys()```, ```values()```, and ```items()```. They are not mutable objects like lists, BUT these data types (```dict_keys```, ```dict_values``` and ```dict_items```) can be used in for loops.

- it's possible to assign keys and values in separate variables with the multiple assignment trick.

## checking existence of key or value in Dictionary



