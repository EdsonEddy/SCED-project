def suma(num,base):
   c = 0
   while num:
      c += num % base
      num //= base
   return c
for i in range(2992,10000):
   a = suma(i,10)
   b = suma(i,12)
   c = suma(i,16)
   if a == b and b == c:print(i)
