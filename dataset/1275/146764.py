def contar(x,b):
    sum=0
    while x>0:
        y=x%b
        x=x//b
        sum=sum+y
    return sum

def expo(x,k):
    j=1
    e=1
    if k!=0:
        while j<=k:
            e=e*x
            j=j+1
    else:
        e=x
    return e
def comparar(x,y,z):
    if (x==y):
        if (y==z):
            return 1
        else:
            return 0
    return 0
        
        
i=2991
while i<10000:
    y=contar(i,10)
    x=contar(i,12)
    z=contar(i,16)
    if (comparar(x,y,z)):
        print(i)
    i=i+1