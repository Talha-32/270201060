numCount = int(input("how many numbers : "))
evenCount = 0
for _ in range (numCount):
    number = int(input("type a number: "))
    if number % 2 == 0:
        evenCount+=1
print(evenCount/numCount*100,"%")        