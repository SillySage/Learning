n=int(input("Введите число "))
x=1
f=0
for i in range(0, n , 1):
    f= f+x
    x= f-x
print (f)
if n<1:
    print ("Введите другое число")