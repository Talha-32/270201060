def multiplication(n):
    if (n == 1):
        return 3
    else:
        return 3 + multiplication(n-1)
print(multiplication(3))