#Made by Austin DeLaundry
#Creates a triangle based on input

h = int(input("GIMME DA HEIGHT"))

for i in range(0, h):
	for symbols in range(0, i + 1):
		print ("*", end = "")
	print("")
