n= int(input("Введите число "))
x = 1
for i in range(n,0,-1):
    x = x * i
m= int(input("Введите число "))
z = 1
for o in range(m,0,-1):
    z = z * o
t=1
for p in range(n-m,0,-1):
    t = t * p
    r=x/z*t
print(r)