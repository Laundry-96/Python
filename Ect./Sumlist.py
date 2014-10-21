#Made by Austin DeLauney
#Sums lists (sorta like a matrix)

list1 = [] #Create the lists
list2 = []
sumList = []

#Get the variables for the first list
i = input("Give me a number, type 'end' to end: ")
while(i != "end"):
	list1.append(int(i))
	i = input("Give me a number, type 'end' to end: ")

#Get the variables for the second list
i = input("Give me a number, type 'end' to end: ")
while(i != "end"):
	list2.append(int(i))
	i = input("Give me a number, type 'end' to end: ")



if len(list1) > len(list2): #List 2 is shorter than the first
	for x in range(len(list2)): #For each number in list 2
		sumList.append(list1[x] + list2[x])
	for x in range(len(list2), len(list1)):
		sumList.append(list1[x])

else:
	for x in range(len(list1)): #For each number in list 2
		sumList.append(list1[x] + list2[x])
	for x in range(len(list2), len(list1)):
		sumList.append(list1[x])


print(sumList)
