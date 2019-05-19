

def ruler(data):
    counter = 1
    for x in range(data):
        if counter != 10:
            print(counter, end="")
        else:
            print(0,end="")
            counter = 0
        counter +=1
inputdata = int(input("Enter the Number : "))
ruler(inputdata)
