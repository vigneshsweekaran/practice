def isListOfInts(data):
    output = True
    if type(data) is list:
        if (data):
            for x in data:
                if(type(x) is not int):
                    output = False
        return output
    else:
        try:
            raise ValueError()
        except ValueError :
            print('ValueError: {} - arg not of <list> type'.format(data))

def testList(data):
    result = isListOfInts(data)
    list = [True,False]
    if (result in list):
        print("{} --> {}".format(data,result))

testList([])
testList([1])
testList([1,2])
testList([0])
testList(['1'])
testList([1,'a'])
testList(['a',1])
testList([1, 1.])
testList([1., 1.])
testList((1,2))
