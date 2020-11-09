age = int(input("your age: "))
normalPrice = 3
youngerSixOrOlderSixty = 0
betweenSixAndEighteen = 0.5
if age < 6 or age > 60:
    print(normalPrice*youngerSixOrOlderSixty)
elif age > 6 and age <18:
    print(normalPrice*betweenSixAndEighteen)
else:
     print("NORMAL PRİCE")