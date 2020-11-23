elementCount = int(input("How many elements will you enter?  "))
usersList = list()
uniqueList = list()
counter = 0
for i in range(elementCount):
	usersList.append(input(f"{i+1}. element: "))
for i in range(elementCount):
	if not usersList[i] in uniqueList:
		uniqueList.append(usersList[i])
print(usersList,"\n",uniqueList)