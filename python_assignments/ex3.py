def isListOfInts(data):
    output = True
    if type(data) is list:
        if (data):
            for x in data:
                if(type(x) is not int):
                    output = False
    else:
        raise ValueError('{} - arg not of <list> type'.format(data))
    return output
print(isListOfInts([]))
print(isListOfInts([1]))
print(isListOfInts([1,4,8,9]))
print(isListOfInts([0]))
print(isListOfInts(['0']))
print(isListOfInts([0,'a']))
print(isListOfInts(['a',0]))
print(isListOfInts([0,1.0]))
print(isListOfInts([1.0,1.0]))
print(isListOfInts([1,4,8,'9']))
print(isListOfInts((1,2,5)))
