for i in range(1000,10000):
    n=int(i)
    f=n
    g=n
    kl=n
    s=0
    s1=0
    s2=0
    while n>0:
        d=n%10
        s=s+d
        n=n//10

    while f>0:
        d=f%16
        s1=s1+d
        f=f//16
    while g>0:
        d=g%12
        s2=s2+d
        g=g//12
    if s==s1 and s1==s2:
        print(kl)