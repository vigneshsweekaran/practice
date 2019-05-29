firstLine = []
secondLine = []

def ruler(data):
    rulerValue = 1
    counter = 1
    for x in range(data):
        if counter != 10:
            firstLine.append(" ")
            secondLine.append(counter)
        else:
            firstLine.append(rulerValue)
            secondLine.append(0)
            rulerValue +=1
            counter = 0
        counter +=1
    for x in firstLine:
        print(x,end = "")
    print()
    for x in secondLine:
        print(x, end = "")

inputdata = int(input("Enter the Number : "))
ruler(inputdata)
