#Made by Austin DeLauney
#Asks for a number and inserts it into a list

myList = [1,9,16,24] #original list
i = int(input("GIVE ME A NUMBER SO I CAN INSERT IT INTO THE LIST BRUH: ")) #Get a number from user
inserted = False #The numbder has yet to be inserted

for x in range(0, len(myList)): #For each variable in myList
	if myList[x] > i and not inserted: #If the number is smaller that i, and the number has yet to be inserted
		myList.insert(x, i) #Insert the number
		inserted=True #The number has been inserted, so set to True

print(myList) #Print myList
