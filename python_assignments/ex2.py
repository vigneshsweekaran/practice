import sys
def isWhiteLine(data):
    if not data.strip() :
        return True
    else:
        return False

file = sys.argv[1]
f = open(file, "r")
for x in f:
    if(isWhiteLine(x)==False):
        print(x)
