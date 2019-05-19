n=int(input("Enter number of rows: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n,0,-1):
    print("   "*(n-i),end="")
    for j in range(0,i):
        print('{0:6}'.format(a[i-1][j]),end="")
    print()
