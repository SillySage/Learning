n= int(input("Enter n "))
for a in range(n,0,-1):
    for b in range(0,a,1):
        print ("*", end='')
    print ()
for a in range(1,n,1):
    for b in range(0,a+1,1):
        print ("*", end='')
    print ()