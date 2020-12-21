def evenlst(lst):
    if len(lst) == 0:
        return 0
    counter = 0
    
    if lst[0] % 2 == 0:
        counter = 1
    return counter + evenlst(lst[1:])
print(evenlst([0,1,2,3,4,5,6]))