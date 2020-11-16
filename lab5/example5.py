firstNumber = 1
secondNumber = 1

fibonacci = [firstNumber,secondNumber]
for i in range(10):
    firstNumber,secondNumber = secondNumber,firstNumber + secondNumber

    fibonacci.append(secondNumber)

print(fibonacci)