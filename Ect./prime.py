#Made by Austin DeLaunedry
#Finds prime numbers without using modulus

num = int(input("Give me a number bruh: "))
isPrime = True
for i in range(2,num):
	n = num
	while n >= i:
		n -= i

	if n == 0:
		isPrime = False

if(isPrime):
	print(str(num) + " is a prime number")
else:
	print(str(num) + " is not a prime number")
