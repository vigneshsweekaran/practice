import sys
def isWhiteLine(data):
    if not data.strip() :
        return True
    else:
        return False

file = sys.argv[1]
f = open(file, "r")
for x in f:
    if (isWhiteLine(x)==False):
        for y in x:
            if(isWhiteLine(y)==False):
                print(y, end = "")
        print()
