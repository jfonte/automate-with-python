# practice questions ch3-lists

## 6 - what happens to variables in a local scope when the function call returns?

- the variable is destroyed

## 7 - what is a return value? can a return value be part of an expression?

- a return value is the value/output a function returns or "evaluates to". If nothing is specified to be returned then NONE is returned by default. Like any value, a returned value can be used as part of an expression

## 8 - if a function does not have a return statement, what is the return value of a call to that function?

- the NONE data type

## 9 - how can you force a variable in a function to refer to a global variable?

- define the variable using the **global** keyword before it. Ex. ```global this_is_a_global_variable```

## 10 - what is the data type of None?

- the data type of None is nonetype

## 11 - what does the ```import ALLOFTHIS``` statement do?

- imports the module ALLOFTHIS so you can use all of its functions

## 12 - if you had a function named ```bacon()``` in a module named ```spam```, how would you call it after importing ```spam```?

- type ```spam.bacon```

## 13 - how can you prevent a program from crashing when it gets an error?

- use the following code when declaring statements:

```
    try:
        whatever_function()
    except NameOfYourError:
        print('you have an error sir!')
```

## 14 - what goes in the ```try``` clause? what goes in the ```except``` clause?

- whatever code you want to try goes in the ```try:``` clause, and the action you want to take when the error presents itself goes in the ```except: ``` part.