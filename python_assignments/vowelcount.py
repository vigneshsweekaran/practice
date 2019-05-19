import sys

dictionary = {}

def check(data):
    count = 0
    list = data.strip().split()
    vowels = ('a','A','e','E','i','I','o','O','u','U')
    for x in list:
        for y in x:
            if(y in vowels):
                count +=1
        dictionary[x] = count
        count = 0
def SortAndPrint(data = dictionary):
    highest = max(dictionary.values())
    for x,y in data.items():
        if y is highest:
            print(y," ",x)

file = sys.argv[1];
f = open(file,"r")
for data in f:
    check(data)
SortAndPrint()
