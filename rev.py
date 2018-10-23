a= int(input("Enter a "))
for x in range(0,5,1):
    k = 0
    for i in range(a,0,-2):
        for b in range(0,k,1):
            print (' ', end = '')
        for b in range(0,i,1):
            print ("*", end='')
        print ()
        k = k + 1
    k = k - 2
    for i in range(2,a,2):
        for b in range(0,k,1):
            print (' ', end = '')
        for b in range(0,i+1,1):
            print ("*", end='')
        print ()
        k = k - 1
