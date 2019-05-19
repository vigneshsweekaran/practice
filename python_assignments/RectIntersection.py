import sys
# Function to calculate and print the Intersect triangke co-ordinates
def  intersection(A,B):
    Xrange = []
    Yrange = []
    for x in range (A[0][0],A[1][0]):
        Xrange.append(x)
    for y in range (A[0][1],A[1][1]):
        Yrange.append(y)
    # If second rectangle in right-up side
    Posibility_1 = (B[0][0] in Xrange) and (B[1][1] in Yrange)
    # If second rectangle in left-up side
    Posibility_2 = (B[1][0] in Xrange) and (B[1][1] in Yrange)
    # If second rectangle in right-down side
    Posibility_3 = (B[0][0] in Xrange) and (B[0][1] in Yrange)
    # If second rectangle in left-down side
    Posibility_4 = (B[1][0] in Xrange) and (B[0][1] in Yrange)
    if(Posibility_1):
        print ((B[0][0],A[0][1]),(A[1][0],B[1][1]))
    elif(Posibility_2):
        print ((A[0][0],A[0][1]),(B[1][0],B[1][1]))
    elif(Posibility_3):
        print ((B[0][0],B[0][1]),(A[1][0],A[1][1]))
    elif(Posibility_4):
        print ((A[0][0],B[0][1]),(B[1][0],A[1][1]))
    else:
        print("None")

def Collectdata(input,x):
    output = ((int(input[x]),int(input[x+1])),(int(input[x+2]),int(input[x+3])))
    return output

data = ' '.join(sys.argv[1:])
inputdata =(data.split())
A = Collectdata(inputdata,0)
B = Collectdata(inputdata,4)
intersection(A,B)
