def hailstone(n):
    if(n<0):
        print("Invalid input")
        return
    if(n==1):
        print(1)
        return
    if(n%2 == 0):
        print(n)
        hailstone(n/2)
        return
    if(n%2==1):
        print(n)
        hailstone((n*3) + 1)
        return