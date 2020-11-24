myList = []
fullList = []
summationList = []
total = 0
counter = 0;
print("Enter n : ")
n = int(input())

for i in range(n * n):
    print("Enter element : ")
    element = input()
    myList.append(element)
    if ((i + 1) % n == 0):
        fullList.append(myList)
        myList = []

print("\n")
print("Created matrix:\n\n")

for i in fullList:
    print(i[0] + " " + i[1] + " " + i[2] + "\n")
    summationList.append(int(i[counter]))
    counter = counter + 1

for i in range(counter):
    total = total + summationList[i]

print("Total : ")
print(total)
