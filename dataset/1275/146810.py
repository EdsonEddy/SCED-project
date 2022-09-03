def hexa(n):
    r=0
    res=[]
    while n>16:
        d=n%16
        n=n//16
        r+=d
        res.append(d)
    r+=n
    return r

def doce(n):
    r=0
    res=[]
    while n>12:
        d=n%12
        n=n//12
        r+=d
        res.append(d)
    r+=n
    return r


ini=1000
max=9999
for i in range(1000,10000,1):
    b = hexa(i)
    c = doce(i)
    a=str(i)
    s=0
    for j in a:
        s+=int(j)
    if s==b and s==c:
        print(i)
