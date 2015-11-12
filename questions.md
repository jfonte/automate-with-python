# questions

- how do I prevent this type of errors like in ex5 when I provide an empty input?

```
Traceback (most recent call last):
  File "ex5-continue-statement.py", line 8, in <module>
    name = input()
  File "<string>", line 0

    ^
SyntaxError: unexpected EOF while parsing
```

SOLUTION: This happens if you are using python version <3, so if using that use ```raw_input() instead``` more about this here https://stackoverflow.com/questions/5074225/python-unexpected-eof-while-parsing Why? "If you use input, then the data you type is is interpreted as a [b]Python Expression[/b] which means that you end up with gawd knows what type of object in your target variable, and a heck of a wide range of exceptions that can be generated. So you should NOT use input unless you're putting something in for temporary testing, to be used only by someone who knows a bit about Python expressions"

- 