this = []
x = 0
while x < 31: 
    this.append(x)
    x +=1

def fizzbuzz(intList):
    result = []
    for e in intList:
        result.append(e)
    for x in result:
        if x == 0:
            continue
        if x%15 == 0:
            result[result.index(x)] = 'FizzBuzz'
        elif x%3 == 0:
            result[result.index(x)] = 'Fizz'
        elif x%5 == 0:
            result[result.index(x)] = 'Buzz'
    return result


print(fizzbuzz(this))