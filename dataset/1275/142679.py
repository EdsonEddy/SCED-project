def DecimalaX(n, m=2):
    valores = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    valor = []
    while n:
        n, r = divmod(n, m)
        valor.append(valores[r]) if (r > 9) else valor.append(str(r))
    return ''.join(valor[::-1])

for i in range (2992,10000):
    b10=str(i)
    b16='%x'%i
    b12=DecimalaX(i,12)
    b10,b16,b12=list(b10),list(b16),list(b12)
    for j in range(0, len(b16)):
        if b16[j] == 'a':
            b16[j] = 10
        if b16[j] == 'b':
            b16[j] = 11
        if b16[j] == 'c':
            b16[j] = 12
        if b16[j] == 'd':
            b16[j] = 13
        if b16[j] == 'e':
            b16[j] = 14
        if b16[j] == 'f':
            b16[j] = 15
    for l in range(0, len(b12)):
        if b12[l] == 'a':
            b12[l] = 10
        if b12[l] == 'b':
            b12[l] = 11
    b10=[int(b10[f]) for f in range(0,len(b10))]
    b16=[int(b16[f]) for f in range(0,len(b16))]
    b12=[int(b12[f]) for f in range(0,len(b12))]
    a,b,c=sum(b10),sum(b16),sum(b12)
    if a==b and a==c and b==c :
        print(i)
