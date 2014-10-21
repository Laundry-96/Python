#Made by Austin DeLauney
#Simple program that uses for loops to create a box

row = int(input("GIVE ME DA ROW"))
column = int(input("GIVE ME DA COL"))

for x in range(0, column) :
	print('*', end="")

print()

for y in range(0, row - 2):
	print("*", end="")
	for x in range(1, column - 1):
		print(" ", end="")
	print("*")

for x in range(0, column):
	print('*', end="")

print()
