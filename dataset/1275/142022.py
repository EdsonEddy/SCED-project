x=2992
while x<=9999:
	c=0
	y=x
	while y>0:
		c=y%16+c
		y=y//16
	h=c
	c=0
	y=x
	while y>0:
		c=y%12+c
		y=y//12
	dou=c
	c=0
	y=x
	while y>0:
		c=y%10+c
		y=y//10
	dec=c
	if h==dou and h==dec and dou==dec:
		print(x)
	x+=1