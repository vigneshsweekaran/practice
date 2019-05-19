import sys

output = []
# Function to justify the line
def justify(str, width):
    striped_data = str.strip()
    splited_string = striped_data.split()
    splited_char = []
    for x in striped_data:
        splited_char.append(x)
    data = "".join(splited_char)
    length = len(splited_char)
    count = 1
    while(length != width):
        if(data.find(splited_string[count]) != -1):
            index = data.find(splited_string[count])
            splited_char.insert(index," ")
            count +=1
            data = "".join(splited_char)
        if(count == len(splited_string)):
                count=1
        length = len(splited_char)

    for x in range (len(splited_string)):
        if(x == len(splited_string)-1):
            output.append(splited_string[x])
        else:
            output.append(splited_string[x])
            output.append(data.find(splited_string[x+1]) - (data.find(splited_string[x])+(len(splited_string[x]))))
    print(data)

# Read file name and width from command line arguments
file = sys.argv[1]
width = int(sys.argv[2])

f = open(file,'r')
for x in f:
    justify(x,width)
#Print the words list with spaces count
print(output)
