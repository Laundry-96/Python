#Made by Austin DeLauney
#I forget what it does

for i in range(0,100):
	na=nb=i
	while na>=3:
		na-=3
		#print(na)
	while nb>=5:
		nb-=5
	if na == 0 and nb == 0:
		print("baz")
	elif na == 0:
		print("foo")
	elif nb == 0:
		print("bar")
	else:
		print(i)
