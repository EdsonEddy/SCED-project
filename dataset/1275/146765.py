def funcion(n,b):
    s=0
    while (n!=0):
        d=n%b
        n=n//b
        s=s+d
    return s


for i in range (1000,10000):
    a=funcion(i,10)
    b=funcion(i,12)
    c=funcion(i,16)
    if (a==b and b==c):
        print (i)