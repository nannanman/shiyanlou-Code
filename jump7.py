a = 0
while a<=99:
	a=a+1
	b=a%7
	c=int(a/10)
	d=a%10
	if b==0 or c==7 or d==7:
		continue
	print(a)
